# -*- coding: utf-8 -*-
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

for lec in range(39, 46):
    marker = f'SLIDES_MONTANA_L{lec:02d}'
    start = text.find(marker)
    end = text.find(f'SLIDES_MONTANA_L{lec+1:02d}', start)
    if end == -1:
        end = text.find('export const MONTANA_ALL_SLIDES', start)
    sec = text[start:end]
    slides = re.findall(r'"num":\s*(\d+),[\s\S]*?"title":\s*"([^"]+)"[\s\S]*?"problem":\s*"([^"]*)"', sec)
    print(f'=== Lecture {lec} ({len(slides)} slides) ===')
    for num, title, prob in slides:
        clean_prob = prob.replace('\\n', ' ')[:75]
        print(f'  Slide {num}: {title} | {clean_prob}')
