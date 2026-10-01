import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

for lec_id in range(6, 11):
    marker = f"SLIDES_MONTANA_L{lec_id:02d}"
    next_marker = f"SLIDES_MONTANA_L{lec_id+1:02d}"
    start = text.find(marker)
    if start == -1:
        marker = f"SLIDES_MONTANA_L{lec_id}"
        next_marker = f"SLIDES_MONTANA_L{lec_id+1}"
        start = text.find(marker)
    if start == -1:
        print(f"Missing L{lec_id}")
        continue
    end = text.find(next_marker, start)
    if end == -1:
        end = text.find("SLIDES_MONTANA_L", start + 20)
    lec_text = text[start:end]
    slides = re.split(r'\{\s*"num":', lec_text)[1:]
    print(f"\n==========================================")
    print(f"LECTURE {lec_id} (Marker: {marker}, Total slides: {len(slides)})")
    print(f"==========================================")
    for idx, s in enumerate(slides, 1):
        title = re.search(r'"title":\s*"([^"]*)"', s)
        t = title.group(1) if title else ""
        sub = re.search(r'"subtitle":\s*"([^"]*)"', s)
        sb = sub.group(1) if sub else ""
        prob = re.search(r'"problem":\s*"([^"]*)"', s)
        p = prob.group(1).replace('\\n', ' ') if prob else ""
        print(f"  [Slide {idx}] {t}")
        print(f"    Sub: {sb}")
        print(f"    Prob: {p[:110]}...")
