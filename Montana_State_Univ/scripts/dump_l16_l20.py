import re

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

for lec_id in range(16, 21):
    marker = f"SLIDES_MONTANA_L{lec_id:02d}"
    next_marker = f"SLIDES_MONTANA_L{lec_id+1:02d}"
    start = text.find(marker)
    if start == -1:
        print(f"Missing {marker}")
        continue
    end = text.find(next_marker, start)
    if end == -1:
        end = text.find("export const MONTANA_ALL_SLIDES", start)
    lec_text = text[start:end]
    
    # find all slides
    slides = re.split(r'\{\s*"num":', lec_text)[1:]
    print(f"\n==========================================")
    print(f"LECTURE {lec_id} (Total slides: {len(slides)})")
    print(f"==========================================")
    for idx, s in enumerate(slides, 1):
        title = re.search(r'"title":\s*"([^"]*)"', s)
        title = title.group(1) if title else ""
        sub = re.search(r'"subtitle":\s*"([^"]*)"', s)
        sub = sub.group(1) if sub else ""
        prob = re.search(r'"problem":\s*"([^"]*)"', s)
        prob_str = prob.group(1).replace('\\n', ' ') if prob else ""
        sol = re.search(r'"solution":\s*"([^"]*)"', s)
        sol_str = sol.group(1).replace('\\n', ' ') if sol else ""
        print(f"\n[Slide {idx}] {title}")
        print(f"  Subtitle: {sub}")
        print(f"  Problem : {prob_str[:120]}...")
        print(f"  Solution: {sol_str[:100]}...")
