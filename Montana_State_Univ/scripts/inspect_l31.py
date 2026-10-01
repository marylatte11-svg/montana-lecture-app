import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('SLIDES_MONTANA_L31')
end = text.find('SLIDES_MONTANA_L32', pos)
sec = text[pos:end]
slides = re.findall(r'"num":\s*(\d+),[\s\S]*?"script":\s*"((?:\\.|[^"\\])*)"', sec)
clean = slides[0][1].encode('utf-8').decode('unicode_escape')
print("=== L31 Slide 1 Full Script ===")
print(clean)
