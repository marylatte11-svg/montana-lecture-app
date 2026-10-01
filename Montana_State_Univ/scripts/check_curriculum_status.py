# -*- coding: utf-8 -*-
"""
check_curriculum_status.py
Audits slides and script word counts across all 45 lectures.
"""
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"{'Lecture':<12} | {'Slides':<8} | {'Script Words':<14} | {'Est. Minutes':<12} | {'Status'}")
print("-" * 65)

total_slides = 0
total_words = 0

for lid in range(1, 46):
    marker = f'SLIDES_MONTANA_L{lid:02d}'
    pos = content.find(marker)
    if pos == -1:
        print(f"L{lid:02d} NOT FOUND")
        continue

    next_marker = f'SLIDES_MONTANA_L{lid+1:02d}' if lid < 45 else 'export const MONTANA_ALL_SLIDES'
    next_pos = content.find(next_marker, pos)
    if next_pos == -1:
        next_pos = len(content)

    chunk = content[pos:next_pos]

    # count slides
    slides = len(re.findall(r'"num":\s*\d+', chunk))
    # count words in scripts
    scripts = re.findall(r'"script":\s*"([^"]+)"', chunk)
    words = sum(len(s.split()) for s in scripts)

    total_slides += slides
    total_words += words

    status = "Expanded (20m+)" if words >= 1800 else "Short (~3-5m)"
    print(f"L{lid:02d}{'':<9} | {slides:<8} | {words:<14} | {words/130:<12.1f} | {status}")

print("-" * 65)
print(f"Total: {total_slides} slides across 45 lectures, {total_words} words ({total_words/130:.1f} minutes)")
