# -*- coding: utf-8 -*-
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

for lec in range(17, 21):
    marker = f'SLIDES_MONTANA_L{lec:02d}'
    start = text.find(marker)
    end = text.find(f'SLIDES_MONTANA_L{lec+1:02d}', start)
    if end == -1:
        end = text.find('export const MONTANA_ALL_SLIDES', start)
    sec = text[start:end]
    slides = re.findall(r'"num":\s*(\d+),[\s\S]*?"script":\s*"((?:\\.|[^"\\])*)"', sec)
    print(f'=== Lecture {lec} ({len(slides)} slides) ===')
    total = 0
    for num, sc in slides:
        wc = len(sc.split())
        total += wc
        print(f'  Slide {num}: {wc} words')
    print(f'  Total: {total} words ({total/130:.1f} mins)')
