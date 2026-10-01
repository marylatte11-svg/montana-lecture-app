# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

for lec in range(1, 46):
    pos = text.find(f'SLIDES_MONTANA_L{lec:02d}')
    end = text.find(f'SLIDES_MONTANA_L{lec+1:02d}', pos)
    if end == -1:
        end = text.find('export const MONTANA_ALL_SLIDES', pos)
    sec = text[pos:end]
    slides = re.findall(r'"num":\s*(\d+),[\s\S]*?"script":\s*"((?:\\.|[^"\\])*)"', sec)
    if not slides: continue
    
    total_turns = 0
    bracket_count = 0
    colon_count = 0
    for num, sc in slides:
        clean = sc.encode('utf-8').decode('unicode_escape')
        turns = [t for t in re.split(r'\n\n+|\n(?=\[(?:Prof|TA)|(?:Prof\.|TA\s)[\w\s]+:)', clean) if t.strip()]
        total_turns += len(turns)
        bracket_count += len(re.findall(r'\[Prof\.|\[TA\s', clean))
        colon_count += len(re.findall(r'Prof\.\s*Park:|TA\s*Sora:', clean))
    
    avg_turns = total_turns / len(slides)
    print(f'L{lec:02d} ({len(slides)} slides): avg {avg_turns:.1f} turns/slide | brackets: {bracket_count}, colons: {colon_count}')
