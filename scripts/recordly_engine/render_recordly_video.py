# -*- coding: utf-8 -*-
"""
Recordly-Powered Autonomous Motion Lecture Video Engine
Transforms raw lecture slides and conversational scripts into polished Screen Studio / Recordly videos:
- Auto-Zoom & Pan (Camera Tracking to active topic elements)
- Studio Canvas & 3D Window Frame with Ambient Glow
- Smooth Animated Cursor with Ripple Click Effects
- Presenter Avatar Bubble with Real-time Pulsing Soundwaves
- Glassmorphic Floating Subtitles
"""

import os
import sys
import json
import re
import argparse
import asyncio
import subprocess
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import imageio_ffmpeg
import edge_tts
from playwright.async_api import async_playwright

BASE_DIR = r"c:\Oikos Univ"
ENGINE_DIR = os.path.join(BASE_DIR, "scripts", "recordly_engine")
OUTPUT_DIR = os.path.join(BASE_DIR, "recordly_videos")
SLIDES_IMG_DIR = os.path.join(OUTPUT_DIR, "slide_images")
AUDIO_DIR = os.path.join(OUTPUT_DIR, "audio_segments")
TEMP_VIDEO_DIR = os.path.join(OUTPUT_DIR, "temp_rec")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SLIDES_IMG_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(TEMP_VIDEO_DIR, exist_ok=True)

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

# Voice Configs
VOICE_PETER = "en-US-ChristopherNeural"
VOICE_PETER_RATE = "-2%"
VOICE_PETER_PITCH = "-2Hz"

VOICE_SARAH = "en-US-JennyNeural"
VOICE_SARAH_RATE = "+2%"
VOICE_SARAH_PITCH = "+1Hz"

VOICE_JAMES = "en-US-GuyNeural"
VOICE_JAMES_RATE = "+3%"
VOICE_JAMES_PITCH = "+0Hz"

def get_audio_duration_ms(audio_path):
    cmd = [FFMPEG_EXE, "-i", audio_path]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if match:
        hours = int(match.group(1))
        mins = int(match.group(2))
        secs = float(match.group(3))
        return int((hours * 3600 + mins * 60 + secs) * 1000)
    return 3000

def parse_dialogue_turns(script_text):
    paragraphs = script_text.split('\n\n')
    turns = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith('[Prof. Peter]') or p.startswith('[Prof. Peter Kim]'):
            speaker_key = "peter"
            speaker_name = "Prof. Peter Kim"
            role = "Lead Instructor"
            voice = VOICE_PETER
            rate = VOICE_PETER_RATE
            pitch = VOICE_PETER_PITCH
            clean_text = re.sub(r'^\[Prof\.\s*Peter(\s*Kim)?\]\s*', '', p)
        elif p.startswith('[TA Sarah]') or p.startswith('[Sarah (TA)]') or p.startswith('[Prof. Sarah]'):
            speaker_key = "sarah"
            speaker_name = "TA Sarah Jenkins"
            role = "Senior Research TA"
            voice = VOICE_SARAH
            rate = VOICE_SARAH_RATE
            pitch = VOICE_SARAH_PITCH
            clean_text = re.sub(r'^\[(TA\s*Sarah|Sarah\s*\(TA\)|Prof\.\s*Sarah)\]\s*', '', p)
        elif p.startswith('[TA James]') or p.startswith('[James (TA)]') or p.startswith('[James]'):
            speaker_key = "james"
            speaker_name = "TA James Wilson"
            role = "DevOps Specialist"
            voice = VOICE_JAMES
            rate = VOICE_JAMES_RATE
            pitch = VOICE_JAMES_PITCH
            clean_text = re.sub(r'^\[(TA\s*James|James\s*\(TA\)|James)\]\s*', '', p)
        else:
            # Alternating fallback or single narrator (Prof. Peter)
            speaker_key = "peter"
            speaker_name = "Prof. Peter Kim"
            role = "Lead Instructor"
            voice = VOICE_PETER
            rate = VOICE_PETER_RATE
            pitch = VOICE_PETER_PITCH
            clean_text = p
            
        turns.append({
            "speaker_key": speaker_key,
            "speaker_name": speaker_name,
            "role": role,
            "voice": voice,
            "rate": rate,
            "pitch": pitch,
            "text": clean_text
        })
    return turns

async def generate_turn_audio(turn_idx, turn_data, slide_num):
    final_audio_path = os.path.join(AUDIO_DIR, f"slide_{slide_num:02d}_turn_{turn_idx:02d}.mp3")
    
    # Optional voice morphing if available
    try:
        from voice_morphing_engine import morph_to_professor_voice
        has_morph = True
    except ImportError:
        has_morph = False

    if has_morph and turn_data["speaker_key"] == "peter":
        raw_audio_path = os.path.join(AUDIO_DIR, f"slide_{slide_num:02d}_turn_{turn_idx:02d}_raw.mp3")
        communicate = edge_tts.Communicate(
            text=turn_data["text"],
            voice=turn_data["voice"],
            rate=turn_data["rate"],
            pitch=turn_data["pitch"]
        )
        await communicate.save(raw_audio_path)
        await asyncio.sleep(0.05)
        morph_to_professor_voice(raw_audio_path, final_audio_path)
    else:
        communicate = edge_tts.Communicate(
            text=turn_data["text"],
            voice=turn_data["voice"],
            rate=turn_data["rate"],
            pitch=turn_data["pitch"]
        )
        await communicate.save(final_audio_path)
        await asyncio.sleep(0.05)

    return final_audio_path

async def capture_slide_image(slide_num, page, session_id=1):
    img_path = os.path.join(SLIDES_IMG_DIR, f"session_{session_id}_slide_{slide_num:02d}.png")
    if os.path.exists(img_path) and os.path.getsize(img_path) > 50000:
        return img_path
    
    # Capture directly from local or remote app
    url = f"https://oikos-lecture-app.vercel.app/?session={session_id}&slide={slide_num}"
    try:
        await page.goto(url, wait_until="networkidle", timeout=30000)
    except Exception:
        await page.goto(url, wait_until="domcontentloaded")
    
    await asyncio.sleep(0.5)
    await page.evaluate("""() => {
        const header = document.querySelector('header');
        if (header) header.style.display = 'none';
        return true;
    }""")
    
    await page.screenshot(path=img_path, full_page=False)
    print(f"  📸 Captured 1080p slide: {img_path}")
    return img_path

def analyze_motion_target(text, turn_idx):
    """
    Intelligently determines Recordly camera target and cursor location
    based on keywords in the dialogue text.
    """
    lower = text.lower()
    
    # Left Box / Problem / Traditional / Yesterday
    if any(k in lower for k in ['left', 'yesterday', 'chatbot', 'passive', 'traditional', 'problem', 'waiting', 'past', 'pillar 1']):
        return {
            "scale": 1.32,
            "ox": 28,
            "oy": 52,
            "cx": 380,
            "cy": 420
        }
    # Right Box / Solution / Modern / Avatar / Agentic / Today
    elif any(k in lower for k in ['right', 'today', 'avatar', 'proactive', 'agentic', 'solution', 'future', 'cloud', 'pillar 2', 'dividend']):
        return {
            "scale": 1.32,
            "ox": 72,
            "oy": 52,
            "cx": 1150,
            "cy": 420
        }
    # Bottom Summary / Charts / Metrics / Tables / Formula
    elif any(k in lower for k in ['chart', 'graph', 'metric', 'hours', 'percent', 'formula', 'equation', 'bottom', 'third', 'pillar 3', 'lab']):
        return {
            "scale": 1.28,
            "ox": 50,
            "oy": 72,
            "cx": 860,
            "cy": 680
        }
    # Title / Header / Main Concept
    elif any(k in lower for k in ['title', 'welcome', 'motto', 'objective', 'overview', 'concept', 'paradigm']):
        return {
            "scale": 1.15,
            "ox": 50,
            "oy": 35,
            "cx": 860,
            "cy": 240
        }
    else:
        # Alternating dynamic camera pan
        if turn_idx % 2 == 0:
            return {"scale": 1.25, "ox": 35, "oy": 50, "cx": 480, "cy": 450}
        else:
            return {"scale": 1.25, "ox": 65, "oy": 50, "cx": 1050, "cy": 450}

async def render_recordly_slide_video(slide_data, session_id=1):
    slide_num = slide_data["num"]
    print(f"\n=======================================================")
    print(f"🎬 Recordly Engine: Session {session_id} • Slide {slide_num:02d}: {slide_data['title']}")
    print(f"=======================================================")

    turns = parse_dialogue_turns(slide_data["script"])
    print(f"  👥 Dialogue Turns: {len(turns)}")

    # 1. Synthesize audio segments
    turn_audio_records = []
    timeline_events = []
    
    lead_in_ms = 800
    turn_gap_ms = 700
    current_time_ms = lead_in_ms

    # Initial slide overview camera event
    timeline_events.append({"t": 0, "type": "camera", "scale": 1.0, "ox": 50, "oy": 50})
    timeline_events.append({"t": 0, "type": "cursor", "x": 860, "y": 900, "click": False})
    timeline_events.append({"t": 0, "type": "speaker", "speaker": turns[0]["speaker_key"], "isSpeaking": False})
    timeline_events.append({"t": 0, "type": "subtitle", "text": slide_data["title"]})

    for idx, turn in enumerate(turns):
        audio_file = await generate_turn_audio(idx, turn, slide_num)
        dur_ms = get_audio_duration_ms(audio_file)
        turn_audio_records.append((audio_file, dur_ms))

        # Target camera & cursor
        target = analyze_motion_target(turn["text"], idx)

        # Event: Speaker starts
        timeline_events.append({
            "t": current_time_ms,
            "type": "speaker",
            "speaker": turn["speaker_key"],
            "isSpeaking": True
        })
        timeline_events.append({
            "t": current_time_ms,
            "type": "subtitle",
            "text": turn["text"]
        })

        # Event: Recordly Auto-Zoom & Smooth Cursor Move (delayed by 300ms for natural reaction)
        zoom_time = current_time_ms + 300
        timeline_events.append({
            "t": zoom_time,
            "type": "camera",
            "scale": target["scale"],
            "ox": target["ox"],
            "oy": target["oy"]
        })
        timeline_events.append({
            "t": zoom_time + 100,
            "type": "cursor",
            "x": target["cx"],
            "y": target["cy"],
            "click": True
        })

        current_time_ms += dur_ms + turn_gap_ms

    # Final wrap-up zoom out
    outro_ms = 2500
    timeline_events.append({
        "t": current_time_ms - turn_gap_ms + 200,
        "type": "camera",
        "scale": 1.0,
        "ox": 50,
        "oy": 50
    })
    timeline_events.append({
        "t": current_time_ms - turn_gap_ms + 300,
        "type": "speaker",
        "speaker": turns[-1]["speaker_key"],
        "isSpeaking": False
    })
    timeline_events.append({
        "t": current_time_ms - turn_gap_ms + 400,
        "type": "subtitle",
        "text": "— Slide Complete —"
    })

    total_duration_ms = current_time_ms + outro_ms
    total_duration_sec = total_duration_ms / 1000.0
    print(f"  ⏱️ Total Video Timeline: {total_duration_sec:.2f} seconds ({len(timeline_events)} motion events)")

    # 2. Concat Full Master Audio Track with FFmpeg
    silence_lead_file = os.path.join(AUDIO_DIR, "silence_lead.mp3")
    silence_gap_file = os.path.join(AUDIO_DIR, "silence_gap.mp3")
    silence_outro_file = os.path.join(AUDIO_DIR, "silence_outro.mp3")
    
    for s_file, dur in [(silence_lead_file, lead_in_ms/1000.0), (silence_gap_file, turn_gap_ms/1000.0), (silence_outro_file, outro_ms/1000.0)]:
        subprocess.run([
            FFMPEG_EXE, "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
            "-t", str(dur), "-q:a", "9", "-acodec", "libmp3lame", s_file
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    concat_txt = os.path.join(AUDIO_DIR, f"slide_{slide_num:02d}_concat.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        f.write(f"file '{silence_lead_file.replace(os.sep, '/')}'\n")
        for i, (a_file, _) in enumerate(turn_audio_records):
            f.write(f"file '{a_file.replace(os.sep, '/')}'\n")
            if i < len(turn_audio_records) - 1:
                f.write(f"file '{silence_gap_file.replace(os.sep, '/')}'\n")
        f.write(f"file '{silence_outro_file.replace(os.sep, '/')}'\n")

    master_audio_path = os.path.join(AUDIO_DIR, f"slide_{slide_num:02d}_master_audio.mp3")
    subprocess.run([
        FFMPEG_EXE, "-y", "-f", "concat", "-safe", "0", "-i", concat_txt,
        "-c:a", "libmp3lame", "-b:a", "192k", master_audio_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  🎵 Master Audio Assembled: {master_audio_path}")

    # 3. Capture Slide Image and Setup Recordly Stage
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=[
            "--disable-web-security",
            "--allow-file-access-from-files",
            "--enable-gpu"
        ])
        
        # Temp page to capture slide snapshot
        capture_page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        slide_img_path = await capture_slide_image(slide_num, capture_page, session_id=session_id)
        await capture_page.close()

        # Recording Context with Chromium native video recorder
        rec_dir = os.path.join(TEMP_VIDEO_DIR, f"slide_{slide_num:02d}")
        os.makedirs(rec_dir, exist_ok=True)
        
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir=rec_dir,
            record_video_size={"width": 1920, "height": 1080}
        )

        stage_page = await context.new_page()
        stage_html_path = os.path.join(ENGINE_DIR, "recordly_stage.html")
        stage_url = f"file:///{stage_html_path.replace(os.sep, '/')}"

        await stage_page.goto(stage_url)
        await stage_page.wait_for_selector("#slideViewport")

        # Prepare Avatar file paths
        peter_avatar = f"file:///{os.path.join(ENGINE_DIR, 'assets', 'avatar_peter.svg').replace(os.sep, '/')}"
        sarah_avatar = f"file:///{os.path.join(ENGINE_DIR, 'assets', 'avatar_sarah.svg').replace(os.sep, '/')}"

        # Initialize Recordly Engine in the browser
        config = {
            "slideImage": f"file:///{slide_img_path.replace(os.sep, '/')}",
            "badge": f"OIKOS SESSION {session_id}",
            "title": f"Slide {slide_num:02d} • {slide_data['title']}",
            "timeline": timeline_events,
            "presenters": {
                "peter": {
                    "name": "Prof. Peter Kim",
                    "role": "Lead Instructor",
                    "avatar": peter_avatar
                },
                "sarah": {
                    "name": "TA Sarah Jenkins",
                    "role": "Senior Research TA",
                    "avatar": sarah_avatar
                },
                "james": {
                    "name": "TA James Wilson",
                    "role": "DevOps Specialist",
                    "avatar": peter_avatar
                }
            }
        }

        await stage_page.evaluate("(cfg) => window.RecordlyEngine.init(cfg)", config)
        await asyncio.sleep(0.3)

        # Trigger Motion Timeline!
        print(f"  🎥 Recording Recordly Motion Timeline ({total_duration_sec:.1f}s)...")
        await stage_page.evaluate("() => window.RecordlyEngine.startTimeline()")

        # Wait for the exact duration of the lecture
        await asyncio.sleep(total_duration_sec + 0.5)

        # Close page to flush video file
        video_obj = stage_page.video
        video_temp_path = await video_obj.path() if video_obj else None
        await stage_page.close()
        await context.close()
        await browser.close()

    if not video_temp_path or not os.path.exists(video_temp_path):
        # Locate generated webm file in rec_dir
        files = [os.path.join(rec_dir, f) for f in os.listdir(rec_dir) if f.endswith(".webm")]
        if files:
            video_temp_path = sorted(files, key=os.path.getmtime)[-1]

    print(f"  📹 Raw Recorded Motion Video: {video_temp_path}")

    # 4. Final Merge with FFmpeg: Recorded Video + Master Audio -> Final 1080p MP4
    final_mp4_path = os.path.join(OUTPUT_DIR, f"Recordly_Session{session_id}_Slide_{slide_num:02d}.mp4")
    
    cmd_merge = [
        FFMPEG_EXE, "-y",
        "-i", video_temp_path,
        "-i", master_audio_path,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        final_mp4_path
    ]

    print("  ⚙️ Encoding Final Recordly 1080p MP4...")
    subprocess.run(cmd_merge, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Cleanup temp video dir
    try:
        shutil.rmtree(rec_dir, ignore_errors=True)
    except Exception:
        pass

    file_size_mb = os.path.getsize(final_mp4_path) / (1024 * 1024)
    print(f"  🎉 SUCCESS! Recordly Master Video Created: {final_mp4_path} ({file_size_mb:.2f} MB)")
    return final_mp4_path

async def main():
    parser = argparse.ArgumentParser(description="Recordly Autonomous Motion Video Engine")
    parser.add_argument("--type", type=str, default="oikos", choices=["oikos", "montana"], help="Lecture app type")
    parser.add_argument("--session", type=int, default=1, help="Session / Lecture ID (1-15)")
    parser.add_argument("--slide", type=int, default=8, help="Slide number")
    parser.add_argument("--slides", type=str, default=None, help="Comma-separated slide numbers (e.g. 1,5,8)")
    parser.add_argument("--all", action="store_true", help="Render all slides in the session")
    args = parser.parse_args()

    slides_to_process = []

    if args.type == "montana":
        # Load from Montana JS/JSON
        montana_js_path = os.path.join(BASE_DIR, "src", "data", "montanaSlidesData.js")
        # Run node to extract JSON safely
        node_cmd = [
            "node", "-e",
            f"import('{montana_js_path.replace(os.sep, '/')}').then(m => console.log(JSON.stringify(m.MONTANA_ALL_SLIDES[{args.session}] || [])))"
        ]
        res = subprocess.run(node_cmd, capture_output=True, text=True, cwd=BASE_DIR)
        try:
            montana_slides = json.loads(res.stdout.strip())
        except Exception:
            montana_slides = []

        if args.all:
            slides_to_process = montana_slides
        elif args.slides:
            nums = [int(n.strip()) for n in args.slides.split(",") if n.strip().isdigit()]
            slides_to_process = [s for s in montana_slides if s.get("num") in nums]
        else:
            found = [s for s in montana_slides if s.get("num") == args.slide]
            slides_to_process = found if found else [{
                "num": args.slide,
                "title": f"Montana Lecture {args.session} Slide {args.slide}",
                "script": "Welcome to Montana State University M090 lecture."
            }]
    else:
        # Load Oikos scripts
        scripts_file = os.path.join(BASE_DIR, "files_analysis", "presenter_mode_session1_scripts.json")
        all_scripts = {}
        if os.path.exists(scripts_file):
            with open(scripts_file, "r", encoding="utf-8") as f:
                all_scripts = json.load(f)

        if args.all:
            slides_to_process = [all_scripts[str(k)] for k in sorted(all_scripts.keys(), key=lambda x: int(x))]
        elif args.slides:
            nums = [n.strip() for n in args.slides.split(",") if n.strip()]
            slides_to_process = [all_scripts[n] for n in nums if n in all_scripts]
        else:
            slide_str = str(args.slide)
            if slide_str in all_scripts:
                slides_to_process = [all_scripts[slide_str]]
            else:
                slides_to_process = [{
                    "num": args.slide,
                    "title": f"Oikos Session {args.session} Slide {args.slide}",
                    "script": "Welcome everyone to our advanced lecture on Autonomous Avatars."
                }]

    print(f"🚀 Recordly Engine Pipeline: Ready to render {len(slides_to_process)} slide(s) [Type: {args.type.upper()}, Session: {args.session}]")
    for s_data in slides_to_process:
        await render_recordly_slide_video(s_data, session_id=args.session)

if __name__ == "__main__":
    asyncio.run(main())
