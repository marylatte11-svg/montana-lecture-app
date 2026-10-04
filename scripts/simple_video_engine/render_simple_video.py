# -*- coding: utf-8 -*-
"""
Montana State University - Gallatin College: M090 Introductory Algebra
Method 2: Simple Slide Video Engine (Fast, Lightweight, Robust)
- Pipeline:
  1. Capture 1080p slide snapshot (Playwright)
  2. Parse presenter script & speechify math formulas (Edge-TTS)
  3. Overlay sleek glassmorphic Presenter Subtitle HUD (Pillow)
  4. Ultra-fast still-image loop synthesis (FFmpeg CPU or NVENC GPU)
  5. Concatenate into full lecture master video
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
from PIL import Image, ImageDraw, ImageFont

# Path definitions
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MONTANA_DIR = os.path.join(BASE_DIR, "Montana_State_Univ")
SIMPLE_ENGINE_DIR = os.path.dirname(os.path.abspath(__file__))
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

# Voice Configs
VOICE_PARK = "en-US-AvaNeural"
VOICE_PARK_RATE = "+0%"
VOICE_PARK_PITCH = "+0Hz"

VOICE_SORA = "en-US-AriaNeural"
VOICE_SORA_RATE = "+4%"
VOICE_SORA_PITCH = "+2Hz"

VOICE_NARRATOR = "en-US-AndrewNeural"

def check_nvenc_support():
    """Detect if NVIDIA NVENC hardware acceleration is actually functional on this hardware."""
    try:
        res = subprocess.run(
            [FFMPEG_EXE, "-f", "lavfi", "-i", "nullsrc=s=256x256:d=0.1", "-c:v", "h264_nvenc", "-f", "null", "-"],
            capture_output=True,
            timeout=3
        )
        return res.returncode == 0
    except Exception:
        return False

HAS_NVENC = check_nvenc_support()

def get_lecture_dirs(lecture_id):
    lecture_dir = os.path.join(MONTANA_DIR, "simple_videos", f"Lecture{lecture_id:02d}")
    slides_img_dir = os.path.join(lecture_dir, "slide_images")
    audio_dir = os.path.join(lecture_dir, "audio_segments")
    frames_dir = os.path.join(lecture_dir, "hud_frames")
    temp_video_dir = os.path.join(lecture_dir, "temp_clips")
    for d in [lecture_dir, slides_img_dir, audio_dir, frames_dir, temp_video_dir]:
        os.makedirs(d, exist_ok=True)
    return lecture_dir, slides_img_dir, audio_dir, frames_dir, temp_video_dir

def convert_math_to_spoken_english(text):
    """
    Converts mathematical formulas, LaTeX markup, and markdown in spoken script
    into clean, natural spoken English for the TTS engine.
    Ensures numbers like $8$ are ALWAYS pronounced as 'eight', NEVER as 'eight dollar'!
    """
    if not text:
        return ""
    spoken = text

    # Strip inline math markers ($...$) and all dollar signs immediately
    spoken = re.sub(r'\$([^$]+)\$', r' \1 ', spoken)
    spoken = spoken.replace('$', '')

    # Common LaTeX fractions: \frac{a}{b} -> a over b
    spoken = re.sub(r'\\(?:d?frac)\{([^}]+)\}\{([^}]+)\}', r'\1 over \2', spoken)

    # Square roots
    spoken = re.sub(r'\\sqrt\[(\d+)\]\{([^}]+)\}', r'the \1th root of \2', spoken)
    spoken = re.sub(r'\\sqrt\{([^}]+)\}', r'the square root of \1', spoken)
    spoken = re.sub(r'\\sqrt\s*(\d+|[a-zA-Z])', r'the square root of \1', spoken)
    spoken = re.sub(r'√\{?([^}\s,]+)\}?', r'the square root of \1', spoken)
    spoken = re.sub(r'\bsqrt\(?([^)\s,]+)\)?', r'the square root of \1', spoken)

    # Math operators
    spoken = spoken.replace('\\cdot', ' times ')
    spoken = spoken.replace('\\times', ' times ')
    spoken = spoken.replace('\\div', ' divided by ')
    spoken = spoken.replace('\\pm', ' plus or minus ')
    spoken = spoken.replace('±', ' plus or minus ')
    spoken = spoken.replace('\\mp', ' minus or plus ')
    spoken = spoken.replace('\\neq', ' is not equal to ')
    spoken = spoken.replace('\\approx', ' is approximately ')
    spoken = spoken.replace('\\leq', ' is less than or equal to ')
    spoken = spoken.replace('\\le', ' is less than or equal to ')
    spoken = spoken.replace('\\geq', ' is greater than or equal to ')
    spoken = spoken.replace('\\ge', ' is greater than or equal to ')
    spoken = spoken.replace('\\mathbb{R}', 'the real numbers')
    spoken = spoken.replace('\\mathbb{Z}', 'the integers')
    spoken = spoken.replace('\\mathbb{Q}', 'the rational numbers')
    spoken = spoken.replace('\\mathbb{N}', 'the natural numbers')
    spoken = spoken.replace('\\pi', 'pi')
    spoken = spoken.replace('\\circ', ' degrees ')
    spoken = re.sub(r'\\text\{([^}]+)\}', r' \1 ', spoken)
    spoken = spoken.replace('\\quad', ' ')
    spoken = spoken.replace('\\;', ' ')
    spoken = spoken.replace('\\\\', '. ')

    # Absolute value: |-8| -> "the absolute value of -8"
    spoken = re.sub(r'\|([^|]+)\|', r'the absolute value of \1', spoken)

    # Exponents: x^2 -> x squared, x^3 -> x cubed
    spoken = re.sub(r'([a-zA-Z0-9\(\)]+)\^2\b', r'\1 squared', spoken)
    spoken = re.sub(r'([a-zA-Z0-9\(\)]+)\^3\b', r'\1 cubed', spoken)
    spoken = re.sub(r'([a-zA-Z0-9\(\)]+)\^{?([a-zA-Z0-9\+\-]+)}?', r'\1 to the \2', spoken)

    # Clean markdown formatting (**bold**, *italic*)
    spoken = re.sub(r'\*\*([^*]+)\*\*', r'\1', spoken)
    spoken = re.sub(r'\*([^*]+)\*', r'\1', spoken)

    # Clean residual backslashes or braces
    spoken = re.sub(r'\\[a-zA-Z]+', ' ', spoken)
    spoken = re.sub(r'[{}\\]', ' ', spoken)

    # Normalise spaces and clean repeated punctuation
    spoken = re.sub(r'\s+', ' ', spoken).strip()
    return spoken

def clean_math_for_subtitles(text):
    """
    Cleans LaTeX formulas for display on glassmorphic subtitle bar.
    Converts LaTeX operators and square roots to crisp Unicode symbols (√, ±, ×, ÷, ≤, ≥).
    """
    if not text:
        return ""
    sub = text
    sub = re.sub(r'\\sqrt\{([^}]+)\}', r'√\1', sub)
    sub = re.sub(r'\\sqrt\s*(\d+|[a-zA-Z])', r'√\1', sub)
    sub = re.sub(r'\\sqrt\[(\d+)\]\{([^}]+)\}', r'(\1)√\2', sub)
    sub = re.sub(r'\bsqrt\(?([^)\s,]+)\)?', r'√\1', sub)
    sub = sub.replace('\\pm', '±')
    sub = sub.replace('\\mp', '∓')
    sub = sub.replace('\\cdot', '·')
    sub = sub.replace('\\times', '×')
    sub = sub.replace('\\div', '÷')
    sub = sub.replace('\\neq', '≠')
    sub = sub.replace('\\ne', '≠')
    sub = sub.replace('\\approx', '≈')
    sub = sub.replace('\\leq', '≤')
    sub = sub.replace('\\le', '≤')
    sub = sub.replace('\\geq', '≥')
    sub = sub.replace('\\ge', '≥')
    sub = sub.replace('\\implies', '⟹')
    sub = sub.replace('\\rightarrow', '→')
    sub = sub.replace('\\frac', '')
    sub = re.sub(r'\\text\{([^}]+)\}', r'\1', sub)
    sub = re.sub(r'[{}\\]', '', sub)
    sub = re.sub(r'\$([^$]+)\$', r'\1', sub)
    sub = sub.replace('$', '')
    sub = re.sub(r'\*\*([^*]+)\*\*', r'\1', sub)
    sub = re.sub(r'\*([^*]+)\*', r'\1', sub)
    sub = re.sub(r'\s+', ' ', sub).strip()
    return sub

def load_official_montana_slides(lecture_id=1):
    """Loads slide objects directly from src/data/montanaSlidesData.js."""
    export_script = os.path.join(BASE_DIR, "scripts", "recordly_engine", "export_lecture.mjs")
    subprocess.run(["node", export_script, str(lecture_id)], cwd=BASE_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    json_path = os.path.join(BASE_DIR, "scripts", "recordly_engine", f"lecture_{lecture_id}_slides.json")
    if not os.path.exists(json_path):
        print(f"❌ Failed to load exported JSON: {json_path}")
        return []

    with open(json_path, "r", encoding="utf-8") as f:
        raw_slides = json.load(f)

    parsed_slides = []
    for s in raw_slides:
        script_text = s.get("script", "")
        paragraphs = [p.strip() for p in script_text.split('\n\n') if p.strip()]
        turns = []
        for p in paragraphs:
            if p.startswith('[Prof. Park]') or p.startswith('[Prof. Eunju Park]') or p.startswith('[Prof Park]'):
                speaker_key = "park"
                speaker_name = "Prof. Eunju Park"
                role = "Course Professor"
                voice = VOICE_PARK
                rate = VOICE_PARK_RATE
                pitch = VOICE_PARK_PITCH
                raw_text = re.sub(r'^\[Prof\.\s*(Eunju\s*)?Park\]\s*', '', p)
            elif p.startswith('[TA Sora]') or p.startswith('[Sora (TA)]') or p.startswith('[Sora]'):
                speaker_key = "sora"
                speaker_name = "TA Sora"
                role = "Teaching Assistant"
                voice = VOICE_SORA
                rate = VOICE_SORA_RATE
                pitch = VOICE_SORA_PITCH
                raw_text = re.sub(r'^\[(TA\s*Sora|Sora\s*\(TA\)|Sora)\]\s*', '', p)
            else:
                speaker_key = "park"
                speaker_name = "Prof. Eunju Park"
                role = "Course Professor"
                voice = VOICE_PARK
                rate = VOICE_PARK_RATE
                pitch = VOICE_PARK_PITCH
                raw_text = p

            spoken_text = convert_math_to_spoken_english(raw_text)
            sub_text = clean_math_for_subtitles(raw_text)

            turns.append({
                "speaker_key": speaker_key,
                "speaker_name": speaker_name,
                "role": role,
                "voice": voice,
                "rate": rate,
                "pitch": pitch,
                "spoken_text": spoken_text,
                "subtitle_text": sub_text,
                "raw_text": raw_text
            })

        parsed_slides.append({
            "num": s.get("num", 1),
            "title": s.get("title", f"Slide {s.get('num', 1)}"),
            "turns": turns
        })

    return parsed_slides

async def capture_all_slides(parsed_slides, lecture_id=1, slides_img_dir=None):
    """Captures 1080p full slide snapshots using Playwright headless."""
    from playwright.async_api import async_playwright
    import urllib.request
    captured_paths = {}

    server_proc = None
    dist_dir = os.path.join(BASE_DIR, "dist")
    
    # Check if local server is already running on 4173
    is_running = False
    try:
        with urllib.request.urlopen("http://localhost:4173", timeout=0.5) as r:
            if r.status == 200:
                is_running = True
    except Exception:
        pass

    if not is_running and os.path.exists(dist_dir):
        print(f"  🚀 Starting local slide static server from dist/ on port 4173...")
        server_proc = subprocess.Popen(
            [sys.executable, "-m", "http.server", "4173", "--directory", dist_dir],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        await asyncio.sleep(0.8)

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
            page = await context.new_page()

            for s in parsed_slides:
                slide_num = s["num"]
                img_path = os.path.join(slides_img_dir, f"msu_l{lecture_id:02d}_slide_{slide_num:02d}.png")
                if os.path.exists(img_path) and os.path.getsize(img_path) > 40000:
                    captured_paths[slide_num] = img_path
                    print(f"  ⚡ Slide {slide_num:02d} cached: {img_path}")
                    continue

                url_local = f"http://localhost:4173/?lecture={lecture_id}&slide={slide_num}"
                try:
                    await page.goto(url_local, wait_until="domcontentloaded", timeout=6000)
                except Exception:
                    url_remote = f"https://montana-lecture-app.vercel.app/?lecture={lecture_id}&slide={slide_num}"
                    await page.goto(url_remote, wait_until="domcontentloaded", timeout=15000)

                await asyncio.sleep(0.4)
                # Remove distracting web UI elements
                await page.evaluate("""() => {
                    const header = document.querySelector('header');
                    if (header) header.style.display = 'none';
                    document.querySelectorAll('footer, [class*="fixed bottom"]').forEach(el => el.style.display = 'none');
                    const pbar = document.getElementById('keyboard-help-toast');
                    if (pbar) pbar.style.display = 'none';
                    document.querySelectorAll('.overflow-y-auto').forEach(el => {
                        el.style.overflow = 'visible';
                        el.style.maxHeight = 'none';
                    });
                    return true;
                }""")
                await page.screenshot(path=img_path, full_page=False)
                captured_paths[slide_num] = img_path
                print(f"  📸 Captured Slide {slide_num:02d} (1080p)")

            await browser.close()
    finally:
        if server_proc:
            server_proc.terminate()

    return captured_paths

def render_hud_frame(base_img_path, turn_data, slide_num, total_slides, out_frame_path):
    """
    Overlays a sleek, glassmorphic HUD Subtitle Bar onto the slide image using Pillow.
    Includes:
    - Speaker badge (Prof. Park in Blue / TA Sora in Amber)
    - Formatted, clean subtitle text
    - Slide indicator badge
    """
    base = Image.open(base_img_path).convert("RGBA")
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    W, H = base.size  # 1920 x 1080

    # Subtitle Card Dimensions
    card_h = 112
    card_margin_x = 100
    card_y = H - card_h - 45
    card_w = W - (card_margin_x * 2)

    # Semi-transparent dark glass background with subtle cyan/amber border
    is_park = (turn_data["speaker_key"] == "park")
    accent_rgb = (56, 189, 248) if is_park else (251, 191, 36) # Sky-400 vs Amber-400
    border_color = (*accent_rgb, 200)
    badge_bg = (15, 23, 42, 240)

    # Glass backdrop
    draw.rounded_rectangle(
        [card_margin_x, card_y, card_margin_x + card_w, card_y + card_h],
        radius=14,
        fill=(10, 15, 28, 230),
        outline=border_color,
        width=2
    )

    # Load system fonts
    font_speaker = None
    font_sub = None
    font_slide = None
    for fn in ["segoeui.ttf", "arial.ttf", "DejaVuSans.ttf", "LiberationSans-Regular.ttf"]:
        try:
            font_speaker = ImageFont.truetype(fn, 19)
            font_sub = ImageFont.truetype(fn, 23)
            font_slide = ImageFont.truetype(fn, 16)
            break
        except Exception:
            pass

    if not font_speaker:
        font_speaker = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_slide = ImageFont.load_default()

    # Draw Speaker Badge (Top-left of HUD Card)
    badge_x = card_margin_x + 24
    badge_y = card_y + 12
    badge_txt = f"{turn_data['speaker_name']}  •  {turn_data['role']}"
    
    # Calculate badge width
    try:
        bbox = font_speaker.getbbox(badge_txt)
        txt_w = bbox[2] - bbox[0]
    except Exception:
        txt_w = len(badge_txt) * 11

    badge_w = txt_w + 38
    draw.rounded_rectangle(
        [badge_x, badge_y, badge_x + badge_w, badge_y + 28],
        radius=8,
        fill=badge_bg,
        outline=border_color,
        width=1
    )
    # Vibrant glowing dot indicator
    draw.ellipse(
        [badge_x + 10, badge_y + 9, badge_x + 20, badge_y + 19],
        fill=accent_rgb
    )
    draw.text((badge_x + 28, badge_y + 4), badge_txt, font=font_speaker, fill=(240, 249, 255) if is_park else (254, 243, 199))

    # Slide Number Badge (Top-right of HUD Card)
    slide_badge_txt = f"Slide {slide_num} / {total_slides}"
    draw.text((card_margin_x + card_w - 140, badge_y + 4), slide_badge_txt, font=font_slide, fill=(148, 163, 184))

    # Draw Subtitle Text (Wrapped nicely)
    sub_text = turn_data["subtitle_text"]
    words = sub_text.split()
    lines = []
    curr_line = ""
    for w in words:
        if len(curr_line) + len(w) + 1 <= 88:
            curr_line = f"{curr_line} {w}".strip()
        else:
            lines.append(curr_line)
            curr_line = w
    if curr_line:
        lines.append(curr_line)

    sub_y = card_y + 46
    for line in lines[:2]:  # Up to 2 lines
        draw.text((card_margin_x + 28, sub_y), line, font=font_sub, fill=(255, 255, 255))
        sub_y += 30

    # Composite & Save
    final_img = Image.alpha_composite(base, overlay).convert("RGB")
    final_img.save(out_frame_path, quality=95)
    return out_frame_path

async def generate_turn_audio(turn_data, out_audio_path):
    """Generates audio for a turn using Edge-TTS."""
    if os.path.exists(out_audio_path) and os.path.getsize(out_audio_path) > 3000:
        return out_audio_path

    communicate = edge_tts.Communicate(
        text=turn_data["spoken_text"],
        voice=turn_data["voice"],
        rate=turn_data["rate"],
        pitch=turn_data["pitch"]
    )
    await communicate.save(out_audio_path)
    return out_audio_path

def synthesize_clip(image_path, audio_path, output_clip_path):
    """
    Synthesizes a single turn video clip using FFmpeg still-image loop.
    Ultra-fast execution: uses h264_nvenc if GPU present, else libx264 veryfast.
    """
    v_codec = ["-c:v", "h264_nvenc", "-preset", "p4", "-cq", "20"] if HAS_NVENC else ["-c:v", "libx264", "-preset", "veryfast", "-crf", "20"]
    
    cmd = [
        FFMPEG_EXE, "-y",
        "-loop", "1",
        "-i", image_path,
        "-i", audio_path,
        *v_codec,
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        output_clip_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return output_clip_path

def concat_clips(clip_list, output_master_path):
    """Concatenates multiple MP4 clips using FFmpeg concat demuxer without re-encoding."""
    list_file = output_master_path + ".txt"
    with open(list_file, "w", encoding="utf-8") as f:
        for c in clip_list:
            f.write(f"file '{c.replace(chr(92), '/')}'\n")

    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", list_file,
        "-c", "copy",
        output_master_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    if os.path.exists(list_file):
        os.remove(list_file)
    return output_master_path

async def main():
    parser = argparse.ArgumentParser(description="MSU Method 2: Simple Slide Video Engine")
    parser.add_argument("--lecture", type=int, default=1, help="Lecture number (1-45)")
    parser.add_argument("--limit-slides", type=int, default=0, help="Limit number of slides to process (for quick testing)")
    args = parser.parse_args()

    lec_id = args.lecture
    print(f"\n==================================================================")
    print(f"🎬 MSU M090 Method 2: Simple Slide Video Engine")
    print(f"📌 Lecture: {lec_id:02d} | Hardware Acceleration: {'⚡ NVIDIA NVENC (GPU)' if HAS_NVENC else '💻 CPU (x264 fast)'}")
    print(f"==================================================================\n")

    lecture_dir, slides_img_dir, audio_dir, frames_dir, temp_video_dir = get_lecture_dirs(lec_id)

    # 1. Load slides data
    slides = load_official_montana_slides(lec_id)
    if not slides:
        print(f"❌ No slides found for Lecture {lec_id}!")
        return

    if args.limit_slides > 0:
        slides = slides[:args.limit_slides]
        print(f"⚠️ Limiting execution to first {len(slides)} slides for quick testing")

    total_slides = len(slides)

    # 2. Capture slide snapshots (Playwright)
    print(f"\n📸 Step 1: Capturing {total_slides} slides in 1080p...")
    captured_paths = await capture_all_slides(slides, lec_id, slides_img_dir)

    # 3. Process each slide & turn
    print(f"\n🎙️ Step 2: Generating TTS Audio & Synthesizing Video Clips...")
    all_master_clips = []

    for s in slides:
        s_num = s["num"]
        turns = s["turns"]
        slide_img = captured_paths.get(s_num)
        if not slide_img:
            continue

        print(f"\n--- [Slide {s_num:02d}/{total_slides:02d}: {s['title']}] ({len(turns)} turns) ---")
        slide_turn_clips = []

        for t_idx, turn in enumerate(turns):
            # Audio path
            turn_audio_path = os.path.join(audio_dir, f"l{lec_id:02d}_s{s_num:02d}_turn_{t_idx:02d}.mp3")
            await generate_turn_audio(turn, turn_audio_path)

            # HUD frame path
            turn_frame_path = os.path.join(frames_dir, f"l{lec_id:02d}_s{s_num:02d}_turn_{t_idx:02d}.jpg")
            render_hud_frame(slide_img, turn, s_num, total_slides, turn_frame_path)

            # Fast video clip synthesis
            turn_clip_path = os.path.join(temp_video_dir, f"l{lec_id:02d}_s{s_num:02d}_turn_{t_idx:02d}.mp4")
            synthesize_clip(turn_frame_path, turn_audio_path, turn_clip_path)

            slide_turn_clips.append(turn_clip_path)
            print(f"  ✅ Turn {t_idx+1}/{len(turns)}: [{turn['speaker_name']}] -> {os.path.basename(turn_clip_path)}")

        # Concat turns for this slide
        slide_video_path = os.path.join(lecture_dir, f"MSU_M090_Lecture{lec_id:02d}_Slide{s_num:02d}.mp4")
        concat_clips(slide_turn_clips, slide_video_path)
        all_master_clips.append(slide_video_path)
        print(f"  🎬 Slide {s_num:02d} Completed: {os.path.basename(slide_video_path)}")

    # 4. Master Full Lecture Video Concatenation
    print(f"\n==================================================================")
    print(f"📦 Step 3: Stitching Final Full Master Video...")
    final_master_path = os.path.join(lecture_dir, f"MSU_M090_Lecture{lec_id:02d}_Simple_Master.mp4")
    concat_clips(all_master_clips, final_master_path)

    size_mb = os.path.getsize(final_master_path) / (1024 * 1024)
    print(f"🎉 SUCCESS! Full Lecture Master Video Created:")
    print(f"   📁 Path: {final_master_path}")
    print(f"   💾 Size: {size_mb:.2f} MB")
    print(f"==================================================================\n")

if __name__ == "__main__":
    asyncio.run(main())
