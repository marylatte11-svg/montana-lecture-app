# -*- coding: utf-8 -*-
import sys, os, re, json
sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

for lec in [6, 7, 8, 9, 10]:
    pos = text.find(f'SLIDES_MONTANA_L{lec:02d}')
    end = text.find(f'SLIDES_MONTANA_L{lec+1:02d}', pos)
    sec = text[pos:end]
    m = re.search(r'"num":\s*1,[\s\S]*?"script":\s*"((?:\\.|[^"\\])*)"', sec)
    if m:
        sc = m.group(1).encode('utf-8').decode('unicode_escape')
        print(f"=== L{lec:02d} Slide 1 Script Preview ===")
        print(sc[:250] + "...\n")
