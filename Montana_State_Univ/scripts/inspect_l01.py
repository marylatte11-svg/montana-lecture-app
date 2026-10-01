# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('SLIDES_MONTANA_L01')
end = text.find('SLIDES_MONTANA_L02', pos)
sec = text[pos:end]
slides = re.findall(r'"num":\s*(\d+),[\s\S]*?"title":\s*"([^"]+)"[\s\S]*?"problem":\s*"([^"]*)"', sec)
for num, title, prob in slides:
    clean_prob = prob.replace('\\n', ' ')[:70]
    print(f'Slide {num}: {title} | {clean_prob}')
