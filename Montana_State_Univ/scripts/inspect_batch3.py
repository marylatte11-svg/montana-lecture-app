# -*- coding: utf-8 -*-
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

marker = 'SLIDES_MONTANA_L11'
start = text.find(marker)
end = text.find('SLIDES_MONTANA_L12', start)
sec = text[start:end]
slides = re.findall(r'"num":\s*(\d+),[\s\S]*?"title":\s*"([^"]+)"[\s\S]*?"problem":\s*"([^"]*)"', sec)
print(f'=== Lecture 11 ({len(slides)} slides) ===')
for num, title, prob in slides:
    print(f'  Slide {num}: {title} | Prob: {prob}')
