# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('SLIDES_MONTANA_L20')
end = text.find('SLIDES_MONTANA_L21', pos)
sec = text[pos:end]
slides = re.findall(r'"num":\s*(\d+),[\s\S]*?"script":\s*"((?:\\.|[^"\\])*)"', sec)
for num, sc in slides:
    clean = sc.encode('utf-8').decode('unicode_escape')
    print(f'=== L20 Slide {num} ===')
    turns = re.split(r'\n\n+|\n(?=\[(?:Prof|TA)|(?:Prof\.|TA\s)[\w\s]+:)', clean)
    prof_words = 0
    sora_words = 0
    other_words = 0
    for t in turns:
        t = t.strip()
        if not t: continue
        w = len(t.split())
        if t.startswith('[Prof. Park]') or t.startswith('Prof. Park:'):
            prof_words += w
        elif t.startswith('[TA Sora]') or t.startswith('TA Sora:'):
            sora_words += w
        else:
            other_words += w
    print(f'  Total turns: {len(turns)} | Prof: {prof_words}w, Sora: {sora_words}w, Other: {other_words}w')
    for i, t in enumerate(turns):
        print(f'    [{t[:15].strip()}] ({len(t.split())}w): {t[15:80].strip()}...')
