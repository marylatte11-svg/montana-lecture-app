# -*- coding: utf-8 -*-
with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for lec in [1, 6, 11, 14, 20, 31]:
    pos = text.find(f'SLIDES_MONTANA_L{lec:02d}')
    end = text.find(f'SLIDES_MONTANA_L{lec+1:02d}', pos)
    sec = text[pos:end]
    slides = re.findall(r'"num":\s*(\d+),[\s\S]*?"script":\s*"((?:\\.|[^"\\])*)"', sec)
    if slides:
        clean = slides[0][1].encode('utf-8').decode('unicode_escape')
        print(f'=== L{lec:02d} Slide 1 ===')
        turns_double = clean.split('\n\n')
        turns_single = clean.split('\n')
        print(f'  Double \\n\\n count: {len(turns_double)}')
        print(f'  Single \\n count: {len(turns_single)}')
        for i, t in enumerate(turns_double[:3]):
            print(f'    Turn {i+1} ({len(t.split())} words): {t[:70]}')
