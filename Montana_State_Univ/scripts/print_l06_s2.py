# -*- coding: utf-8 -*-
import sys, os, re, json
sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('SLIDES_MONTANA_L06')
end = text.find('SLIDES_MONTANA_L07', pos)
sec = text[pos:end]
m = re.search(r'"num":\s*2,[\s\S]*?"script":\s*"((?:\\.|[^"\\])*)"', sec)
if m:
    sc = m.group(1).encode('utf-8').decode('unicode_escape')
    print("=== L06 Slide 2 Full Script ===")
    print(sc)
