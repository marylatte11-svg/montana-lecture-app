with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Find scripts in L01, L16, L31, L38
for lid in [1, 16, 31, 38]:
    marker = f'SLIDES_MONTANA_L{lid:02d}'
    idx = content.find(marker)
    if idx != -1:
        chunk = content[idx:idx+8000]
        s_match = re.search(r'"script":\s*"([^"]+)"', chunk)
        if s_match:
            script_text = s_match.group(1).replace(r'\n', '\n').replace(r'\"', '"')
            words = len(script_text.split())
            print(f"=== L{lid:02d} Slide 1 Script ({words} words) ===")
            print(script_text[:400] + "...\n")


