import re

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

for lec_id in [16, 17, 18]:
    marker = f"SLIDES_MONTANA_L{lec_id:02d}"
    next_marker = f"SLIDES_MONTANA_L{lec_id+1:02d}"
    start = text.find(marker)
    if start == -1:
        continue
    end = text.find(next_marker, start)
    lec_text = text[start:end]
    slides = re.split(r'\{\s*"num":', lec_text)[1:]
    print(f"\n==========================================")
    print(f"LECTURE {lec_id} (Total slides: {len(slides)})")
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
        print(f"    Prob: {p[:100]}...")
