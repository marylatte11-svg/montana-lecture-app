"""
sync_unit3_lectures.py
Syncs lecture31.md to lecture45.md from montanaSlidesData.js
"""
import sys
import os
import json
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from unit3_data_l31_l35 import data_31_35
from unit3_data_l36_l40 import data_36_40
from unit3_data_l41_l45 import (
    SLIDES_MONTANA_L41, SLIDES_MONTANA_L42, SLIDES_MONTANA_L43,
    SLIDES_MONTANA_L44, SLIDES_MONTANA_L45
)

ALL_SLIDES = {}
for k, v in data_31_35.items():
    ALL_SLIDES[k] = v
for k, v in data_36_40.items():
    ALL_SLIDES[k] = v
ALL_SLIDES[41] = SLIDES_MONTANA_L41
ALL_SLIDES[42] = SLIDES_MONTANA_L42
ALL_SLIDES[43] = SLIDES_MONTANA_L43
ALL_SLIDES[44] = SLIDES_MONTANA_L44
ALL_SLIDES[45] = SLIDES_MONTANA_L45

lectures_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'lectures'))
os.makedirs(lectures_dir, exist_ok=True)

for lid in range(31, 46):
    slides = ALL_SLIDES[lid]
    md_path = os.path.join(lectures_dir, f'lecture{lid:02d}.md')
    
    lines = [f"# Lecture {lid} - {len(slides)} slides\n\n"]
    
    for slide in slides:
        lines.append(f"## Slide {slide.get('num', '?')}: {slide.get('title', '')}\n\n")
        lines.append(f"**Subtitle:** {slide.get('subtitle', '')}\n\n")
        if slide.get('problem'):
            lines.append(f"### Problem\n{slide['problem']}\n\n")
        if slide.get('solution'):
            lines.append(f"### Solution\n{slide['solution']}\n\n")
        if slide.get('pitfall'):
            lines.append(f"### Key Note\n{slide['pitfall']}\n\n")
        if slide.get('script'):
            lines.append(f"### Script\n{slide['script']}\n\n")
        lines.append("---\n\n")
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"Written: lecture{lid:02d}.md ({len(slides)} slides)")

print("Done! All L31-L45 lecture files synced.")
