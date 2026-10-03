# -*- coding: utf-8 -*-
"""
Montana State University - Gallatin College: M090 Introductory Algebra
Advanced Recordly Engine with Precision Left/Right Panel Panning & Spoken Math Engine
- Lead Instructor: Prof. Eunju Park (en-US-AvaNeural)
- Teaching Assistant: TA Sora (en-US-JennyNeural)
- Panning Architecture:
  1. Left Panel Focus (Problem, Formula, Definitions)
  2. Right Panel Focus (Step-by-Step Solution, Dialogues, Charts)
  3. Sora's Pro-Tip Focus (Bottom Callout Card)
  4. Global Overview (Full 2-Panel View)
- Audio Engine:
  - convert_math_to_spoken_english(): Natural pronunciation of formulas (no dollar signs)
  - clean_math_for_subtitles(): Clean, elegant typography for subtitles
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
MONTANA_DIR = os.path.join(BASE_DIR, "Montana_State_Univ")
ENGINE_DIR = os.path.join(BASE_DIR, "scripts", "recordly_engine")

def get_lecture_dirs(lecture_id):
    lecture_dir = os.path.join(MONTANA_DIR, "recordly_videos", f"Lecture{lecture_id:02d}")
    slides_img_dir = os.path.join(lecture_dir, "slide_images")
    audio_dir = os.path.join(lecture_dir, "audio_segments")
    temp_video_dir = os.path.join(lecture_dir, "temp_rec")
    os.makedirs(lecture_dir, exist_ok=True)
    os.makedirs(slides_img_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(temp_video_dir, exist_ok=True)
    return lecture_dir, slides_img_dir, audio_dir, temp_video_dir

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

# Voice Configs
VOICE_PARK = "en-US-AvaNeural"
VOICE_PARK_RATE = "+0%"
VOICE_PARK_PITCH = "+0Hz"

VOICE_SORA = "en-US-AriaNeural"
VOICE_SORA_RATE = "+4%"
VOICE_SORA_PITCH = "+2Hz"

def convert_math_to_spoken_english(text):
    """
    Ported directly from PresenterMode.jsx
    Converts mathematical formulas, LaTeX markup, and markdown in spoken script
    into clean, natural spoken English for the TTS engine.
    Ensures numbers like $8$ are ALWAYS pronounced as 'eight', NEVER as 'eight dollar'!
    """
    if not text:
        return ""
    spoken = text

    # Strip inline math markers ($...$) and all dollar signs immediately
    # Math numbers like $8$, $7$, $140$ are pure algebraic quantities, NEVER currency!
    spoken = re.sub(r'\$([^$]+)\$', r' \1 ', spoken)
    spoken = spoken.replace('$', '')

    # Common LaTeX math symbols & fractions
    spoken = re.sub(r'\\(?:d?frac)\{([^}]+)\}\{([^}]+)\}', r'\1 over \2', spoken)
    spoken = re.sub(r'\\sqrt\[(\d+)\]\{([^}]+)\}', r'the \1th root of \2', spoken)
    spoken = re.sub(r'\\sqrt\{([^}]+)\}', r'the square root of \1', spoken)
    spoken = re.sub(r'\\sqrt\s*(\d+|[a-zA-Z])', r'the square root of \1', spoken)
    spoken = re.sub(r'√\{?([^}\s,]+)\}?', r'the square root of \1', spoken)
    spoken = re.sub(r'\bsqrt\(?([^)\s,]+)\)?', r'the square root of \1', spoken)
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
    r"""
    Cleans LaTeX formulas for display on glassmorphic subtitle bar.
    Converts LaTeX operators and square roots to crisp Unicode symbols (√, ±, ×, ÷, ≤, ≥).
    NEVER strips the root or plus-or-minus sign (e.g., prevents '\sqrt{16} = 4' from becoming '16 = 4').
    """
    if not text:
        return ""
    sub = text

    # 1. Convert square roots with braces first: \sqrt{16} -> √16, \sqrt{k} -> √k
    sub = re.sub(r'\\sqrt\{([^}]+)\}', r'√\1', sub)
    # 2. Convert square roots without braces: \sqrt 16 -> √16
    sub = re.sub(r'\\sqrt\s*(\d+|[a-zA-Z])', r'√\1', sub)
    # 3. Higher order roots: \sqrt[3]{8} -> (3)√8
    sub = re.sub(r'\\sqrt\[(\d+)\]\{([^}]+)\}', r'(\1)√\2', sub)
    # 4. Text roots: sqrt(16) -> √16
    sub = re.sub(r'\bsqrt\(?([^)\s,]+)\)?', r'√\1', sub)

    # 5. Core Mathematical Operators to Unicode
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
    sub = sub.replace('\\to', '→')
    sub = sub.replace('\\infty', '∞')
    sub = sub.replace('\\in', '∈')
    sub = sub.replace('\\pi', 'π')
    sub = sub.replace('\\circ', '°')

    # 6. Fractions & text macros
    sub = re.sub(r'\\(?:d?frac)\{([^}]+)\}\{([^}]+)\}', r'\1/\2', sub)
    sub = re.sub(r'\\text\{([^}]+)\}', r'\1', sub)

    # 7. Strip inline math delimiters ($...$)
    sub = re.sub(r'\$([^$]+)\$', r'\1', sub)
    sub = sub.replace('$', '')

    # 8. Set notation braces \{ ... \} -> { ... }
    sub = sub.replace(r'\{', '{').replace(r'\}', '}')

    # 9. Clean residual backslash commands
    sub = re.sub(r'\\[a-zA-Z]+', '', sub)
    # 10. Remove single unescaped curly braces
    sub = re.sub(r'[{}]', '', sub)

    # 11. Clean markdown formatting
    sub = re.sub(r'\*\*([^*]+)\*\*', r'\1', sub)
    sub = re.sub(r'\*([^*]+)\*', r'\1', sub)

    # 12. Normalise whitespace
    sub = re.sub(r'\s+', ' ', sub).strip()
    return sub

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

def load_official_montana_slides(lecture_id=1):
    """
    Loads official lecture slide objects directly from src/data/montanaSlidesData.js
    (matching exactly what PresenterMode.jsx uses) via export_lecture.mjs.
    """
    export_script = os.path.join(ENGINE_DIR, "export_lecture.mjs")
    subprocess.run(["node", export_script, str(lecture_id)], cwd=BASE_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    json_path = os.path.join(ENGINE_DIR, f"lecture_{lecture_id}_slides.json")
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

def analyze_slide_motion(slide_num, turn_idx, raw_text, total_turns, lecture_id=1, prev_motion=None):
    """
    Active Panning & Camera Framing:
    - Lecture 1, Slide 1: Progressive vertical tracking down the right dialogue panel
    - Standard Slides:
      - Left Panel (Problem Statement, Formulas, Definitions): panX: +22%, panY: 0%
      - Right Panel (Step-by-Step Solution, Calculation, SVG Graph): panX: -22%, panY: 0%
      - Sora's Pro-Tip / Pitfall Alert (Bottom-Left Card): panX: +20%, panY: -22%
      - Overview: Intro and Wrap-up (scale: 1.0, panX: 0, panY: 0)
    """
    lower = raw_text.lower()

    # SLIDE 1 (Lecture 1 only): Orientation & Progressive Vertical Tracking down Right Dialogue Panel
    if lecture_id == 1 and slide_num == 1:
        card_coords = [
            {"panY": "15%", "cursorY": 377},
            {"panY": "6%",  "cursorY": 481},
            {"panY": "-5%", "cursorY": 594},
            {"panY": "-15%", "cursorY": 698},
            {"panY": "-23%", "cursorY": 793},
            {"panY": "-32%", "cursorY": 887},
        ]
        target = card_coords[min(turn_idx, len(card_coords)-1)]
        return {
            "mode": "card",
            "camera": {"scale": 1.40, "panX": "-22%", "panY": target["panY"]},
            "cursor": {"x": 1200, "y": target["cursorY"], "click": True}
        }

    # STANDARD DEFINITIONS
    CAM_LEFT = {
        "mode": "left",
        "camera": {"scale": 1.42, "panX": "22%", "panY": "0%"},
        "cursor": {"x": 480, "y": 440, "click": True}
    }
    CAM_RIGHT = {
        "mode": "right",
        "camera": {"scale": 1.42, "panX": "-22%", "panY": "0%"},
        "cursor": {"x": 1380, "y": 460, "click": True}
    }
    CAM_TIP = {
        "mode": "tip",
        "camera": {"scale": 1.42, "panX": "20%", "panY": "-22%"},
        "cursor": {"x": 500, "y": 800, "click": True}
    }
    CAM_OVERVIEW = {
        "mode": "overview",
        "camera": {"scale": 1.0, "panX": "0%", "panY": "0%"},
        "cursor": {"x": 960, "y": 540, "click": False}
    }

    # Rule 0: Always start on LEFT panel (Problem / Definition statement)
    if turn_idx == 0:
        return CAM_LEFT

    # Rule 1: SORA'S TIP / PITFALL / WARNING / TRAP
    tip_keywords = [
        'pro-tip', 'pitfall', 'trap', 'mistake', 'warning', "sora's rule", 'mandatory',
        'never confuse', 'lose half your solutions',
        'isolate first', 'isolate x^2 first', 'phantom equal sign', 'adding straight across',
        'multiplying both top and bottom', 'forgetting to reduce', 'flipping the wrong fraction',
        'divide before taking square root', 'no real solution vs no solution'
    ]
    prev_mode = prev_motion.get("mode") if prev_motion else None
    if any(k in lower for k in tip_keywords) and prev_mode != "tip":
        return CAM_TIP

    # Rule 2: Final wrap-up turn -> OVERVIEW
    if turn_idx == total_turns - 1 and any(k in lower for k in ['next up', 'lecture', 'summary', 'solution set', 'good job', 'see you', 'mastery']):
        return CAM_OVERVIEW

    # Rule 3: Explicit keywords
    right_keywords = [
        'step 1', 'step 2', 'step 3', 'step 4', 'step 5',
        'graph of', 'coordinate grid', 'horizontal line', 'intersects', 'intersection',
        'axis of symmetry', 'vertex is located', 'simplifying the radical',
        'take the square root of both sides', 'plugging in', 'subtract 2 from both sides',
        'divide both sides by', 'gives us', 'gives x =', 'which means x =',
        'check your answers', 'substituting them back', 'check!'
    ]
    left_keywords = [
        'problem', 'workbook page', 'look at section', 'definition', 'formula',
        'variables and constants', 'in real life', 'water rocket', 'break-even',
        'original equation', 'on the left side', 'categories'
    ]
    is_r = any(k in lower for k in right_keywords)
    is_l = any(k in lower for k in left_keywords)

    if is_r and not is_l and prev_mode != "right":
        return CAM_RIGHT
    if is_l and not is_r and prev_mode != "left":
        return CAM_LEFT

    # Rule 4: Frequent Alternation! If previous was LEFT, go RIGHT. If previous was RIGHT, go LEFT.
    if prev_mode == "right":
        return CAM_LEFT
    elif prev_mode == "left":
        return CAM_RIGHT
    elif prev_mode == "tip":
        return CAM_RIGHT

    return CAM_LEFT if (turn_idx % 2 == 0) else CAM_RIGHT

async def generate_turn_audio(turn_idx, turn_data, slide_num, lecture_id=1, audio_dir=None):
    final_audio_path = os.path.join(audio_dir, f"l{lecture_id:02d}_s{slide_num:02d}_turn_{turn_idx:02d}.mp3")
    communicate = edge_tts.Communicate(
        text=turn_data["spoken_text"],
        voice=turn_data["voice"],
        rate=turn_data["rate"],
        pitch=turn_data["pitch"]
    )
    await communicate.save(final_audio_path)
    await asyncio.sleep(0.04)
    return final_audio_path

async def capture_slide_image(slide_num, page, lecture_id=1, slides_img_dir=None, force_recapture=True):
    img_path = os.path.join(slides_img_dir, f"msu_l{lecture_id:02d}_slide_{slide_num:02d}.png")
    if not force_recapture and os.path.exists(img_path) and os.path.getsize(img_path) > 40000:
        return img_path

    url = f"http://localhost:4173/?lecture={lecture_id}&slide={slide_num}"
    try:
        await page.goto(url, wait_until="networkidle", timeout=8000)
    except Exception:
        url_remote = f"https://montana-lecture-app.vercel.app/?lecture={lecture_id}&slide={slide_num}"
        try:
            await page.goto(url_remote, wait_until="networkidle", timeout=20000)
        except Exception:
            await page.goto(url_remote, wait_until="domcontentloaded")

    await asyncio.sleep(0.4)
    await page.evaluate("""() => {
        const header = document.querySelector('header');
        if (header) header.style.display = 'none';
        document.querySelectorAll('footer, [class*="fixed bottom"]').forEach(el => el.style.display = 'none');
        const pbar = document.getElementById('keyboard-help-toast');
        if (pbar) pbar.style.display = 'none';

        // Ensure dialogue card container expands so all turns are rendered in snapshot
        document.querySelectorAll('.overflow-y-auto').forEach(el => {
            el.style.overflow = 'visible';
            el.style.maxHeight = 'none';
        });
        return true;
    }""")

    # Overview snapshot
    await page.screenshot(path=img_path, full_page=False)
    print(f"  📸 Captured MSU Slide {slide_num:02d}: {img_path}")

    # For Lecture 1 Slide 1 only: Capture turn-specific snapshots with active glowing card highlight!
    if lecture_id == 1 and slide_num == 1:
        for t_idx in range(6):
            turn_img_path = os.path.join(slides_img_dir, f"msu_l01_slide_01_turn_{t_idx:02d}.png")
            turn_url = f"http://localhost:4173/?lecture={lecture_id}&slide={slide_num}&activeTurn={t_idx}"
            try:
                await page.goto(turn_url, wait_until="networkidle", timeout=8000)
            except Exception:
                pass
            await page.evaluate("""() => {
                const header = document.querySelector('header');
                if (header) header.style.display = 'none';
                document.querySelectorAll('footer, [class*="fixed bottom"]').forEach(el => el.style.display = 'none');
            }""")
            await asyncio.sleep(0.08)
            await page.screenshot(path=turn_img_path, full_page=False)
        print(f"  ✨ Captured 6 active turn snapshots for Slide 1 with native highlighted dialogue cards")

    return img_path

async def render_montana_slide_video(slide_data, lecture_id=1, force_rerender=True):
    out_dir, slides_img_dir, audio_dir, temp_video_dir = get_lecture_dirs(lecture_id)
    slide_num = slide_data["num"]
    final_mp4_path = os.path.join(out_dir, f"MSU_M090_L{lecture_id:02d}_Slide_{slide_num:02d}.mp4")

    if not force_rerender and os.path.exists(final_mp4_path) and os.path.getsize(final_mp4_path) > 1000000:
        print(f"\n=======================================================")
        print(f"🎬 MSU M090 Recordly Engine: Lecture {lecture_id:02d} • Slide {slide_num:02d} [CACHED]")
        print(f"   ⚡ Reusing existing video: {final_mp4_path} ({os.path.getsize(final_mp4_path)/(1024*1024):.2f} MB)")
        print(f"=======================================================")
        return final_mp4_path

    print(f"\n=======================================================")
    print(f"🎬 MSU M090 Recordly Engine: Lecture {lecture_id:02d} • Slide {slide_num:02d}")
    print(f"   Title: {slide_data['title']}")
    print(f"=======================================================")

    turns = slide_data["turns"]
    if not turns:
        print("  ⚠️ No dialogue turns found, skipping.")
        return None

    print(f"  👥 Dialogue Turns: {len(turns)} (Prof. Park & TA Sora)")

    # 1. Synthesize audio segments & build timeline
    turn_audio_records = []
    timeline_events = []

    lead_in_ms = 700
    turn_gap_ms = 650
    current_time_ms = lead_in_ms

    # Intro overview
    timeline_events.append({"t": 0, "type": "camera", "scale": 1.0, "panX": "0%", "panY": "0%"})
    timeline_events.append({"t": 0, "type": "cursor", "x": 860, "y": 900, "click": False})
    timeline_events.append({"t": 0, "type": "speaker", "speaker": turns[0]["speaker_key"], "isSpeaking": False})
    timeline_events.append({"t": 0, "type": "subtitle", "text": clean_math_for_subtitles(slide_data["title"])})

    prev_motion = None
    for idx, turn in enumerate(turns):
        audio_file = await generate_turn_audio(idx, turn, slide_num, lecture_id=lecture_id, audio_dir=audio_dir)
        dur_ms = get_audio_duration_ms(audio_file)
        turn_audio_records.append((audio_file, dur_ms))

        # Precision Camera Motion (Left, Right, or Pro-Tip with Frequent Alternation)
        motion = analyze_slide_motion(slide_num, idx, turn["raw_text"], len(turns), lecture_id=lecture_id, prev_motion=prev_motion)
        prev_motion = motion

        # Slide 1 (Lecture 1 only): Switch to active highlighted card image
        if lecture_id == 1 and slide_num == 1:
            turn_img_path = os.path.join(slides_img_dir, f"msu_l01_slide_01_turn_{idx:02d}.png")
            turn_img_url = f"file:///{turn_img_path.replace(os.sep, '/')}"
            timeline_events.append({
                "t": current_time_ms,
                "type": "slideImage",
                "src": turn_img_url
            })

        # Speaker event
        timeline_events.append({
            "t": current_time_ms,
            "type": "speaker",
            "speaker": turn["speaker_key"],
            "isSpeaking": True
        })
        timeline_events.append({
            "t": current_time_ms,
            "type": "subtitle",
            "text": turn["subtitle_text"]
        })

        # Recordly Auto-Zoom & Active Panning
        zoom_time = current_time_ms + 250
        timeline_events.append({
            "t": zoom_time,
            "type": "camera",
            "scale": motion["camera"]["scale"],
            "panX": motion["camera"]["panX"],
            "panY": motion["camera"]["panY"]
        })
        timeline_events.append({
            "t": zoom_time + 80,
            "type": "cursor",
            "x": motion["cursor"]["x"],
            "y": motion["cursor"]["y"],
            "click": motion["cursor"]["click"]
        })

        current_time_ms += dur_ms + turn_gap_ms

    # Outro zoom-out to full overview
    outro_ms = 2200
    if lecture_id == 1 and slide_num == 1:
        overview_img_path = os.path.join(slides_img_dir, f"msu_l01_slide_01.png")
        overview_img_url = f"file:///{overview_img_path.replace(os.sep, '/')}"
        timeline_events.append({
            "t": current_time_ms - turn_gap_ms + 150,
            "type": "slideImage",
            "src": overview_img_url
        })
    timeline_events.append({
        "t": current_time_ms - turn_gap_ms + 200,
        "type": "camera",
        "scale": 1.0,
        "panX": "0%",
        "panY": "0%"
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
        "text": f"— Complete: Slide {slide_num:02d} —"
    })

    total_duration_ms = current_time_ms + outro_ms
    total_duration_sec = total_duration_ms / 1000.0
    print(f"  ⏱️ Video Duration: {total_duration_sec:.2f}s ({len(timeline_events)} motion keyframes)")

    # 2. Concat Full Master Audio
    silence_lead = os.path.join(audio_dir, "silence_lead.mp3")
    silence_gap = os.path.join(audio_dir, "silence_gap.mp3")
    silence_outro = os.path.join(audio_dir, "silence_outro.mp3")

    for s_file, dur in [(silence_lead, lead_in_ms/1000.0), (silence_gap, turn_gap_ms/1000.0), (silence_outro, outro_ms/1000.0)]:
        subprocess.run([
            FFMPEG_EXE, "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
            "-t", str(dur), "-q:a", "9", "-acodec", "libmp3lame", s_file
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    concat_txt = os.path.join(audio_dir, f"l{lecture_id:02d}_s{slide_num:02d}_concat.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        f.write(f"file '{silence_lead.replace(os.sep, '/')}'\n")
        for i, (a_file, _) in enumerate(turn_audio_records):
            f.write(f"file '{a_file.replace(os.sep, '/')}'\n")
            if i < len(turn_audio_records) - 1:
                f.write(f"file '{silence_gap.replace(os.sep, '/')}'\n")
        f.write(f"file '{silence_outro.replace(os.sep, '/')}'\n")

    master_audio_path = os.path.join(audio_dir, f"l{lecture_id:02d}_s{slide_num:02d}_master.mp3")
    subprocess.run([
        FFMPEG_EXE, "-y", "-f", "concat", "-safe", "0", "-i", concat_txt,
        "-c:a", "libmp3lame", "-b:a", "192k", master_audio_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 3. Capture Slide and Record Stage in Playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=[
            "--disable-web-security",
            "--allow-file-access-from-files",
            "--enable-gpu"
        ])

        capture_page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        slide_img_path = await capture_slide_image(slide_num, capture_page, lecture_id=lecture_id, slides_img_dir=slides_img_dir, force_recapture=force_rerender)
        await capture_page.close()

        rec_dir = os.path.join(temp_video_dir, f"slide_{slide_num:02d}")
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

        park_avatar = f"file:///{os.path.join(ENGINE_DIR, 'assets', 'avatar_prof_park.svg').replace(os.sep, '/')}"
        sora_avatar = f"file:///{os.path.join(ENGINE_DIR, 'assets', 'avatar_ta_sora.svg').replace(os.sep, '/')}"

        config = {
            "slideImage": f"file:///{slide_img_path.replace(os.sep, '/')}",
            "badge": "MONTANA STATE UNIV • M090",
            "title": f"Lecture {lecture_id:02d} • Slide {slide_num:02d}: {slide_data['title']}",
            "timeline": timeline_events,
            "presenters": {
                "park": {
                    "name": "Prof. Eunju Park",
                    "role": "Course Professor",
                    "avatar": park_avatar
                },
                "sora": {
                    "name": "TA Sora",
                    "role": "Teaching Assistant",
                    "avatar": sora_avatar
                }
            }
        }

        await stage_page.evaluate("(cfg) => window.RecordlyEngine.init(cfg)", config)
        await asyncio.sleep(0.3)

        print(f"  🎥 Recording Recordly Motion Timeline ({total_duration_sec:.1f}s)...")
        await stage_page.evaluate("() => window.RecordlyEngine.startTimeline()")

        await asyncio.sleep(total_duration_sec + 0.5)

        video_obj = stage_page.video
        video_temp_path = await video_obj.path() if video_obj else None
        await stage_page.close()
        await context.close()
        await browser.close()

    if not video_temp_path or not os.path.exists(video_temp_path):
        files = [os.path.join(rec_dir, f) for f in os.listdir(rec_dir) if f.endswith(".webm")]
        if files:
            video_temp_path = sorted(files, key=os.path.getmtime)[-1]

    # 4. Final Merge to 1080p MP4
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

    print("  ⚙️ Encoding Final MSU Recordly 1080p MP4...")
    subprocess.run(cmd_merge, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        shutil.rmtree(rec_dir, ignore_errors=True)
    except Exception:
        pass

    file_size_mb = os.path.getsize(final_mp4_path) / (1024 * 1024)
    print(f"  🎉 SUCCESS! Slide {slide_num:02d} Video: {final_mp4_path} ({file_size_mb:.2f} MB)")
    return final_mp4_path

async def main():
    parser = argparse.ArgumentParser(description="MSU M090 Recordly Motion Lecture Video Engine")
    parser.add_argument("--lecture", type=int, default=1, help="Lecture number (1-45)")
    parser.add_argument("--slide", type=int, default=1, help="Specific slide number to render")
    parser.add_argument("--slides", type=str, default=None, help="Comma-separated slide numbers (e.g. 1,2,3)")
    parser.add_argument("--all", action="store_true", help="Render all slides in the lecture and concatenate into master video")
    parser.add_argument("--force", action="store_true", help="Force re-rendering even if cached")
    args = parser.parse_args()

    slides = load_official_montana_slides(lecture_id=args.lecture)
    print(f"📚 Loaded {len(slides)} official slides from montanaSlidesData.js for Lecture {args.lecture}")

    if args.all:
        selected_slides = slides
    elif args.slides:
        nums = [int(n.strip()) for n in args.slides.split(",") if n.strip().isdigit()]
        selected_slides = [s for s in slides if s["num"] in nums]
    else:
        selected_slides = [s for s in slides if s["num"] == args.slide]
        if not selected_slides and slides:
            selected_slides = [slides[0]]

    rendered_videos = []
    for s in selected_slides:
        v_path = await render_montana_slide_video(s, lecture_id=args.lecture, force_rerender=args.force or args.all)
        if v_path and os.path.exists(v_path):
            rendered_videos.append(v_path)

    # If --all and multiple videos rendered, concatenate into Master Lecture Video
    if args.all and len(rendered_videos) > 1:
        out_dir, _, _, _ = get_lecture_dirs(args.lecture)
        master_concat_txt = os.path.join(out_dir, f"MSU_M090_L{args.lecture:02d}_concat_list.txt")
        with open(master_concat_txt, "w", encoding="utf-8") as f:
            for v in rendered_videos:
                f.write(f"file '{v.replace(os.sep, '/')}'\n")

        master_video_path = os.path.join(out_dir, f"MSU_M090_Lecture{args.lecture:02d}_Full_Master.mp4")
        print(f"\n=======================================================")
        print(f"🏆 Concatenating all {len(rendered_videos)} slides into Master Lecture Video...")
        print(f"=======================================================")
        cmd_master = [
            FFMPEG_EXE, "-y", "-f", "concat", "-safe", "0", "-i", master_concat_txt,
            "-c:v", "libx264", "-preset", "fast", "-crf", "19", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            master_video_path
        ]
        subprocess.run(cmd_master, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        master_size_mb = os.path.getsize(master_video_path) / (1024 * 1024)
        print(f"🌟 Master Full Lecture Video Complete: {master_video_path} ({master_size_mb:.2f} MB)")

if __name__ == "__main__":
    asyncio.run(main())
