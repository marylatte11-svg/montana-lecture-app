# -*- coding: utf-8 -*-
"""
Autonomous 2-Presenter Duo Lecture Video & Subtitle Generator (MP4 Master Pipeline)
- Presenter 1: Prof. Peter Kim (54) -> Microsoft Neural Voice 'en-US-ChristopherNeural'
- Presenter 2: TA Sarah Jenkins (31) -> Microsoft Neural Voice 'en-US-JennyNeural'
- Features:
  1. High-Resolution 1080p Slide Capture from Web App
  2. Neural Voice Duo Conversational Synthesis with realistic timing pauses
  3. SRT / VTT Subtitle Generation
  4. 1080p MP4 Video Rendering with Embedded Subtitles
  5. Master Full Lecture Concat (40 Slides -> 60-min Master Video)
"""

import os
import sys
import json
import re
import argparse
import asyncio
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import imageio_ffmpeg
import edge_tts
from playwright.async_api import async_playwright

# Paths & Directory Helper
BASE_DIR = r"c:\Oikos Univ"

def set_session_directories(session_id):
    global OUTPUT_DIR, SLIDES_IMG_DIR, AUDIO_DIR
    OUTPUT_DIR = os.path.join(BASE_DIR, f"session{session_id}_videos")
    SLIDES_IMG_DIR = os.path.join(OUTPUT_DIR, "slide_images")
    AUDIO_DIR = os.path.join(OUTPUT_DIR, "audio_segments")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(SLIDES_IMG_DIR, exist_ok=True)
    os.makedirs(AUDIO_DIR, exist_ok=True)

# Default initialization
set_session_directories(1)

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

# Voice Configs
VOICE_PETER = "en-US-ChristopherNeural"  # Mature, authoritative 50s professor tone (Morphed with clean_*.wav)
VOICE_PETER_RATE = "-2%"
VOICE_PETER_PITCH = "-2Hz"

VOICE_SARAH = "en-US-JennyNeural"        # Bright, articulate, smart 30s Senior TA tone
VOICE_SARAH_RATE = "+2%"
VOICE_SARAH_PITCH = "+1Hz"

VOICE_JAMES = "en-US-GuyNeural"          # Energetic, sharp, knowledgeable 20s Tech/DevOps TA tone
VOICE_JAMES_RATE = "+3%"
VOICE_JAMES_PITCH = "+0Hz"

def format_srt_time(ms):
    total_sec = ms / 1000.0
    millis = int(ms % 1000)
    secs = int(total_sec) % 60
    mins = int(total_sec // 60) % 60
    hours = int(total_sec // 3600)
    return f"{hours:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def parse_dialogue_turns(script_text):
    paragraphs = script_text.split('\n\n')
    turns = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith('[Prof. Peter]') or p.startswith('[Prof. Peter Kim]'):
            speaker = "Prof. Peter Kim"
            voice = VOICE_PETER
            rate = VOICE_PETER_RATE
            pitch = VOICE_PETER_PITCH
            clean_text = re.sub(r'^\[Prof\.\s*Peter(\s*Kim)?\]\s*', '', p)
        elif p.startswith('[TA Sarah]') or p.startswith('[Sarah (TA)]') or p.startswith('[Prof. Sarah]'):
            speaker = "TA Sarah Jenkins"
            voice = VOICE_SARAH
            rate = VOICE_SARAH_RATE
            pitch = VOICE_SARAH_PITCH
            clean_text = re.sub(r'^\[(TA\s*Sarah|Sarah\s*\(TA\)|Prof\.\s*Sarah)\]\s*', '', p)
        elif p.startswith('[TA James]') or p.startswith('[James (TA)]') or p.startswith('[James]'):
            speaker = "TA James Wilson"
            voice = VOICE_JAMES
            rate = VOICE_JAMES_RATE
            pitch = VOICE_JAMES_PITCH
            clean_text = re.sub(r'^\[(TA\s*James|James\s*\(TA\)|James)\]\s*', '', p)
        else:
            speaker = "Narrator"
            voice = VOICE_PETER
            rate = "+0%"
            pitch = "+0Hz"
            clean_text = p
            
        turns.append({
            "speaker": speaker,
            "voice": voice,
            "rate": rate,
            "pitch": pitch,
            "text": clean_text
        })
    return turns

from voice_morphing_engine import morph_to_professor_voice

async def generate_turn_audio(turn_idx, turn_data, slide_num):
    final_audio_path = os.path.join(AUDIO_DIR, f"slide_{slide_num:02d}_turn_{turn_idx:02d}.mp3")
    
    # If speaker is Professor Peter Kim, apply RVC-style voice morphing to match authentic voice
    if "Peter" in turn_data["speaker"]:
        raw_audio_path = os.path.join(AUDIO_DIR, f"slide_{slide_num:02d}_turn_{turn_idx:02d}_raw.mp3")
        communicate = edge_tts.Communicate(
            text=turn_data["text"],
            voice=turn_data["voice"],
            rate=turn_data["rate"],
            pitch=turn_data["pitch"]
        )
        await communicate.save(raw_audio_path)
        await asyncio.sleep(0.05)  # Yield for Windows file release
        morph_to_professor_voice(raw_audio_path, final_audio_path)
    else:
        # Save TA Sarah directly to final path
        communicate = edge_tts.Communicate(
            text=turn_data["text"],
            voice=turn_data["voice"],
            rate=turn_data["rate"],
            pitch=turn_data["pitch"]
        )
        await communicate.save(final_audio_path)
        await asyncio.sleep(0.05)
        
    return final_audio_path

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

async def capture_slide_image(slide_num, page, session_id=1):
    img_path = os.path.join(SLIDES_IMG_DIR, f"session_{session_id}_slide_{slide_num:02d}.png")
    if os.path.exists(img_path) and os.path.getsize(img_path) > 50000:
        return img_path
    
    url = f"https://oikos-lecture-app.vercel.app/?session={session_id}&slide={slide_num}"
    await page.goto(url, wait_until="networkidle")
    await asyncio.sleep(0.4)
    
    await page.evaluate("""() => {
        const header = document.querySelector('header');
        if (header) header.style.display = 'none';
        return true;
    }""")
    
    await page.screenshot(path=img_path, full_page=False)
    print(f"  📸 Captured 1080p slide image for Session {session_id} Slide {slide_num:02d}: {img_path}")
    return img_path

async def build_slide_video(slide_data, page=None, session_id=1):
    slide_num = slide_data["num"]
    print(f"\n=======================================================")
    print(f"🎬 Processing Session {session_id} • Slide {slide_num:02d}: {slide_data['title']}")
    print(f"=======================================================")
    
    turns = parse_dialogue_turns(slide_data["script"])
    print(f"  👥 Dialogue Turns: {len(turns)} between Prof. Peter Kim & TA Sarah")
    
    # 1. Synthesize audio with natural 60-min lecture pacing
    turn_audio_files = []
    srt_entries = []
    
    # Lead-in pause at the start of each slide (0.8s for transition)
    # Helper to chunk long text into 1-2 line subtitle sentences
    def chunk_turn_into_subtitles(turn_text, start_ms, total_dur_ms, base_idx):
        sentences = re.split(r'(?<=[.!?])\s+', turn_text.strip())
        valid_sentences = [s.strip() for s in sentences if s.strip()]
        if not valid_sentences:
            valid_sentences = [turn_text]
        
        total_chars = sum(len(s) for s in valid_sentences)
        entries = []
        cur_st = start_ms
        
        for i, s in enumerate(valid_sentences):
            # Calculate proportion of duration based on character length
            s_dur = int((len(s) / max(total_chars, 1)) * total_dur_ms)
            s_dur = max(s_dur, 1200) # Minimum 1.2s per subtitle line
            cur_et = cur_st + s_dur
            if i == len(valid_sentences) - 1:
                cur_et = start_ms + total_dur_ms
            
            entries.append({
                "idx": base_idx + len(entries),
                "start": format_srt_time(cur_st),
                "end": format_srt_time(cur_et),
                "text": s
            })
            cur_st = cur_et
        return entries

    lead_in_ms = 1000
    current_time_ms = lead_in_ms
    turn_gap_ms = 900  # Natural breathing pause between speakers
    
    for idx, turn in enumerate(turns):
        audio_file = await generate_turn_audio(idx, turn, slide_num)
        duration_ms = get_audio_duration_ms(audio_file)
        turn_audio_files.append((audio_file, duration_ms))
        
        start_time = current_time_ms
        chunked = chunk_turn_into_subtitles(turn["text"], start_time, duration_ms, len(srt_entries) + 1)
        srt_entries.extend(chunked)
        
        current_time_ms = start_time + duration_ms + turn_gap_ms
        print(f"    [Turn {idx+1}] {turn['speaker']} ({duration_ms/1000:.1f}s, {len(chunked)} subtitle lines): \"{turn['text'][:35]}...\"")

    # Determine post-slide reflection / intermission pause to achieve 60-min pace
    # Major Section slides or Labs get longer reflection breaks
    if slide_num in [2, 11, 21, 31]:
        outro_pause_sec = 6.0  # Section Introduction Pause
    elif slide_num in [14, 15, 30]:
        outro_pause_sec = 8.0  # Interactive Discussion / Quiz Thinking Time
    elif slide_num == 40:
        outro_pause_sec = 10.0 # Final Lab Conclusion Pause
    else:
        outro_pause_sec = 4.0  # Standard Slide Review & Note-taking Pause

    outro_pause_ms = int(outro_pause_sec * 1000)
    current_time_ms += outro_pause_ms

    # 2. Concat audio with lead-in, turn pauses, and outro break
    concat_txt_path = os.path.join(AUDIO_DIR, f"slide_{slide_num:02d}_concat.txt")
    silence_gap_file = os.path.join(AUDIO_DIR, "silence_900ms.mp3")
    silence_lead_file = os.path.join(AUDIO_DIR, "silence_1000ms.mp3")
    silence_outro_file = os.path.join(AUDIO_DIR, f"silence_{outro_pause_ms}ms.mp3")
    
    # Generate needed silence assets
    for s_file, dur in [
        (silence_gap_file, 0.9),
        (silence_lead_file, 1.0),
        (silence_outro_file, outro_pause_sec)
    ]:
        if not os.path.exists(s_file):
            subprocess.run([
                FFMPEG_EXE, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                "-t", str(dur), "-q:a", "9", s_file
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    with open(concat_txt_path, "w", encoding="utf-8") as f:
        # Lead in
        f.write(f"file '{silence_lead_file.replace('\\', '/')}'\n")
        for i, (audio_file, _) in enumerate(turn_audio_files):
            clean_audio = audio_file.replace("\\", "/")
            clean_gap = silence_gap_file.replace("\\", "/")
            f.write(f"file '{clean_audio}'\n")
            if i < len(turn_audio_files) - 1:
                f.write(f"file '{clean_gap}'\n")
        # Outro reflection break
        f.write(f"file '{silence_outro_file.replace('\\', '/')}'\n")
            
    merged_audio_path = os.path.join(AUDIO_DIR, f"slide_{slide_num:02d}_merged.mp3")
    subprocess.run([
        FFMPEG_EXE, "-y", "-f", "concat", "-safe", "0", "-i", concat_txt_path,
        "-c", "copy", merged_audio_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    total_audio_sec = current_time_ms / 1000.0
    print(f"  🎙️ Merged Audio Track (with breaks): {total_audio_sec:.1f} seconds")
    
    # 3. Clean Subtitles SRT (NO speaker name prefixes)
    srt_path = os.path.join(OUTPUT_DIR, f"Slide_{slide_num:02d}_Subtitles.srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        for entry in srt_entries:
            f.write(f"{entry['idx']}\n")
            f.write(f"{entry['start']} --> {entry['end']}\n")
            f.write(f"{entry['text']}\n\n")
    print(f"  📝 Clean Subtitle SRT saved: {srt_path}")

    # 4. Slide Image Capture
    if page:
        img_path = await capture_slide_image(slide_num, page, session_id)
    else:
        img_path = os.path.join(SLIDES_IMG_DIR, f"session_{session_id}_slide_{slide_num:02d}.png")
        if not os.path.exists(img_path):
            cmd = [
                FFMPEG_EXE, "-y", "-f", "lavfi",
                "-i", f"color=c=0x0B132B:s=1920x1080:d=1",
                "-vframes", "1", img_path
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 5. Render 1080p MP4 Video with Permanent Burned-In Subtitles
    out_video_path = os.path.join(OUTPUT_DIR, f"Session{session_id}_Slide_{slide_num:02d}_DuoLecture.mp4")
    
    # Format SRT path for FFmpeg subtitles filter on Windows with Paperlogy Font
    clean_srt_path = srt_path.replace("\\", "/").replace(":", "\\:")
    fonts_dir = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts").replace("\\", "/").replace(":", "\\:")
    subtitle_filter = f"subtitles='{clean_srt_path}':fontsdir='{fonts_dir}':force_style='FontSize=16,Fontname=Paperlogy 6 SemiBold,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BackColour=&H80000000,BorderStyle=4,MarginV=26'"
    
    cmd_encode = [
        FFMPEG_EXE, "-y",
        "-loop", "1",
        "-i", img_path,
        "-i", merged_audio_path,
        "-vf", subtitle_filter,
        "-c:v", "libx264",
        "-preset", "fast",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-t", f"{total_audio_sec:.3f}",
        "-movflags", "+faststart",
        out_video_path
    ]
    
    print(f"  ⚡ Encoding 1080p MP4 with Burned-In Subtitles...")
    subprocess.run(cmd_encode, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(out_video_path):
        size_mb = os.path.getsize(out_video_path) / (1024 * 1024)
        print(f"  🎉 SUCCESS! Video Created: {out_video_path} ({size_mb:.2f} MB)")
        return out_video_path
    return None

async def build_master_concatenation(video_paths=None, session_id=1, total_slides=45):
    # If video_paths is not provided or incomplete, auto-discover all slide videos in directory
    if not video_paths:
        video_paths = []
        for i in range(1, total_slides + 1):
            vp = os.path.join(OUTPUT_DIR, f"Session{session_id}_Slide_{i:02d}_DuoLecture.mp4")
            if os.path.exists(vp):
                video_paths.append(vp)
    
    if not video_paths:
        return
    
    # 1. 4x Modular Part Videos (Universal 45-Slide Architecture):
    # - Part 1: Slides 01 ~ 11
    # - Part 2: Slides 12 ~ 22
    # - Part 3: Slides 23 ~ 33
    # - Part 4: Slides 34 ~ 45
    parts_config = [
        ("Part1_Module", list(range(1, 12)), "Slides 01~11: Module 1"),
        ("Part2_Module", list(range(12, 23)), "Slides 12~22: Module 2"),
        ("Part3_Module", list(range(23, 34)), "Slides 23~33: Module 3"),
        ("Part4_Module", list(range(34, total_slides + 1)), f"Slides 34~{total_slides:02d}: Module 4 & Lab")
    ]
    
    print(f"\n=======================================================")
    print(f"🎞️ Generating 4x Module Split Videos (Session {session_id})...")
    print(f"=======================================================")
    
    for part_name, slide_nums, desc in parts_config:
        part_vpaths = []
        for num in slide_nums:
            vp = os.path.join(OUTPUT_DIR, f"Session{session_id}_Slide_{num:02d}_DuoLecture.mp4")
            if os.path.exists(vp):
                part_vpaths.append(vp)
                
        if part_vpaths:
            concat_txt = os.path.join(OUTPUT_DIR, f"concat_session{session_id}_{part_name}.txt")
            with open(concat_txt, "w", encoding="utf-8") as f:
                for v in part_vpaths:
                    f.write(f"file '{v.replace('\\', '/')}'\n")
            
            part_video_path = os.path.join(OUTPUT_DIR, f"Session{session_id}_{part_name}.mp4")
            cmd = [FFMPEG_EXE, "-y", "-f", "concat", "-safe", "0", "-i", concat_txt, "-c", "copy", part_video_path]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if os.path.exists(part_video_path):
                size_mb = os.path.getsize(part_video_path) / (1024 * 1024)
                print(f"  🎬 Created Module: {os.path.basename(part_video_path)} ({desc} | {size_mb:.2f} MB)")
                
    # 2. Full 75-Minute Master Video (Slides 01 ~ 45 sequential)
    ordered_master_vpaths = []
    for i in range(1, total_slides + 1):
        vp = os.path.join(OUTPUT_DIR, f"Session{session_id}_Slide_{i:02d}_DuoLecture.mp4")
        if os.path.exists(vp):
            ordered_master_vpaths.append(vp)
            
    master_concat_txt = os.path.join(OUTPUT_DIR, f"master_video_concat_session{session_id}.txt")
    with open(master_concat_txt, "w", encoding="utf-8") as f:
        for v in ordered_master_vpaths:
            clean_v = v.replace("\\", "/")
            f.write(f"file '{clean_v}'\n")
            
    master_video_path = os.path.join(OUTPUT_DIR, f"Session{session_id}_Full_Master_Lecture.mp4")
    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", master_concat_txt,
        "-c", "copy",
        master_video_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(master_video_path):
        size_mb = os.path.getsize(master_video_path) / (1024 * 1024)
        print(f"\n🏆 FULL MASTER DUO LECTURE VIDEO COMPLETED!")
        print(f"📍 Location: {master_video_path} ({size_mb:.2f} MB)")

def load_session_slides(session_id):
    slides_data_path = os.path.join(BASE_DIR, "src", "data", "slidesData.js")
    with open(slides_data_path, "r", encoding="utf-8") as f:
        content = f.read()
    var_name = f"SLIDES_SESSION_{session_id}"
    pattern = rf"export const {var_name} = (\[[\s\S]*?\n\]);"
    match = re.search(pattern, content)
    if not match:
        raise ValueError(f"Could not find {var_name} in slidesData.js")
    return json.loads(match.group(1))

async def main():
    parser = argparse.ArgumentParser(description="Generate Duo Lecture MP4 Videos for Student Pair Projects")
    parser.add_argument("--session", type=int, default=1, help="Session number (1 to 15, default: 1)")
    parser.add_argument("--slide", type=int, help="Generate video for a single slide number (e.g. --slide 1)")
    parser.add_argument("--slides", type=str, help="Comma-separated slide numbers (e.g. --slides 1,8,14,40)")
    parser.add_argument("--all", action="store_true", help="Generate all 40 slides and build Master Video")
    args = parser.parse_args()
    set_session_directories(args.session)

    session_slides = load_session_slides(args.session)
    target_slides = []
    
    if args.slide:
        target_slides = [s for s in session_slides if s["num"] == args.slide]
    elif args.slides:
        nums = [int(n.strip()) for n in args.slides.split(",") if n.strip()]
        target_slides = [s for s in session_slides if s["num"] in nums]
    elif args.all:
        target_slides = session_slides
    else:
        # Default: generate demo slides (Slide 1 & Slide 8)
        target_slides = [s for s in session_slides if s["num"] in [1, 8]]

    print("=======================================================")
    print(f"🚀 Oikos Univ 3-Presenter Trio Lecture Video Generator (Session {args.session})")
    print("👨‍🏫 Lead: Prof. Peter Kim | 👩‍💻 TA: Sarah Jenkins | 👨‍💻 TA: James Wilson")
    print(f"📋 Target: {len(target_slides)} slides from Session {args.session}")
    print("⏱️ Pacing: Broadcast Quality Master Lecture with Intermissions & Reflection Breaks")
    print("=======================================================")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()
        
        generated_videos = []
        for s in target_slides:
            vpath = await build_slide_video(s, page, args.session)
            if vpath:
                generated_videos.append(vpath)
                
        await browser.close()
        
    if args.all and len(generated_videos) == len(session_slides):
        await build_master_concatenation(generated_videos, args.session, len(session_slides))

    print(f"\n✨ All completed! Files saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    asyncio.run(main())
