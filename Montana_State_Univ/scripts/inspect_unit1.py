# -*- coding: utf-8 -*-
import sys, io, re, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

for lec in range(1, 16):
    pos = text.find(f'SLIDES_MONTANA_L{lec:02d}')
    end = text.find(f'SLIDES_MONTANA_L{lec+1:02d}', pos)
    if end == -1:
        end = text.find('export const MONTANA_ALL_SLIDES', pos)
    sec = text[pos:end]
    slides = re.findall(r'"num":\s*(\d+),[\s\S]*?"title":\s*"([^"]+)"[\s\S]*?"problem":\s*"((?:\\.|[^"\\])*)"[\s\S]*?"solution":\s*"((?:\\.|[^"\\])*)"', sec)
    print(f'=== L{lec:02d} ({len(slides)} slides) ===')
    for num, title, prob, sol in slides:
        clean_prob = prob.replace('\\n', ' ')[:60]
        print(f'  Slide {num}: {title} | Prob: {clean_prob}')
