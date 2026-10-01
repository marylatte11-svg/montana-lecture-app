"""
assemble_unit3.py
Assembles all Unit 3 lectures (L31-L45) into montanaSlidesData.js
"""

import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

from unit3_data_l31_l35 import data_31_35
from unit3_data_l36_l40 import data_36_40
from unit3_data_l41_l45 import (
    SLIDES_MONTANA_L41, SLIDES_MONTANA_L42, SLIDES_MONTANA_L43,
    SLIDES_MONTANA_L44, SLIDES_MONTANA_L45
)

# Merge all lecture slides into one dict
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

LECTURE_TITLES = {
    31: "Lecture 31: Intro to Quadratic Functions & Identifying the Vertex",
    32: "Lecture 32: Finding the Vertex by Formula & the y-Intercept",
    33: "Lecture 33: Graphing Parabolas Using Vertex and Table of Values",
    34: "Lecture 34: x-Intercepts via the Square Root Property",
    35: "Lecture 35: Square Root Property with Fractions & Completing the Square Intro",
    36: "Lecture 36: Completing the Square — Full Method",
    37: "Lecture 37: Completing the Square with Leading Coefficient",
    38: "Lecture 38: Factoring Quadratics — GCF and Trinomial",
    39: "Lecture 39: Factoring with a not equal to 1 and Special Forms",
    40: "Lecture 40: Mixed Factoring Methods & Unit 3 Mid-Point Review",
    41: "Lecture 41: The Quadratic Formula — Derivation and Application",
    42: "Lecture 42: The Discriminant — Classifying Solutions",
    43: "Lecture 43: Section 3.6 — Mixed Methods for Intercepts and Vertex",
    44: "Lecture 44: Section 3.7 Part 1 — Graphing with the 5-Point Method",
    45: "Lecture 45: Section 3.7 Part 2 — Comprehensive Graphing & Unit 3 Grand Review",
}

# ─────────────────────────────────────────────
# Read current montanaSlidesData.js
# ─────────────────────────────────────────────
data_file = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'data', 'montanaSlidesData.js'))
print(f"Reading: {data_file}")
with open(data_file, 'r', encoding='utf-8') as f:
    content = f.read()
print(f"Original file size: {len(content):,} bytes")

# ─────────────────────────────────────────────
# Helper: convert Python obj to JS string
# ─────────────────────────────────────────────
def to_js(obj, depth=0):
    pad = "  " * depth
    ipad = "  " * (depth + 1)
    if isinstance(obj, dict):
        if not obj:
            return "{}"
        items = [f'{ipad}"{k}": {to_js(v, depth+1)}' for k, v in obj.items()]
        return "{\n" + ",\n".join(items) + "\n" + pad + "}"
    elif isinstance(obj, list):
        if not obj:
            return "[]"
        items = [ipad + to_js(item, depth+1) for item in obj]
        return "[\n" + ",\n".join(items) + "\n" + pad + "]"
    elif isinstance(obj, bool):
        return "true" if obj else "false"
    elif isinstance(obj, str):
        escaped = obj.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '')
        return f'"{escaped}"'
    elif obj is None:
        return "null"
    else:
        return str(obj)

# ─────────────────────────────────────────────
# 1. Add lecture entries to MONTANA_LECTURES
# ─────────────────────────────────────────────
# Find the end of the MONTANA_LECTURES array 
# (after lecture 30 entry, before ];)

# Check if L31+ already exist
if '"id": 31' in content:
    print("WARN: Lecture 31 already exists in MONTANA_LECTURES. Skipping lecture list update.")
    skip_lectures = True
else:
    skip_lectures = False

if not skip_lectures:
    # Find insert position: last } before ]; at end of MONTANA_LECTURES
    lectures_end_marker = '  }\n];\n\nexport const SLIDES_MONTANA_L01'
    insert_at = content.find(lectures_end_marker)
    if insert_at == -1:
        # Try alternative
        insert_at = content.find('\n];\n\nexport const SLIDES_MONTANA_L01')
        insert_at += 1  # after the newline before ]

    new_entries = ""
    for lid in range(31, 46):
        title = LECTURE_TITLES[lid]
        new_entries += f',\n  {{\n    "id": {lid},\n    "title": "{title}",\n    "active": true\n  }}'

    content = content[:insert_at + 3] + new_entries + content[insert_at + 3:]
    print("Added 15 lecture entries to MONTANA_LECTURES")

# ─────────────────────────────────────────────
# 2. Add slide arrays for L31-L45
# ─────────────────────────────────────────────
if 'SLIDES_MONTANA_L31' in content:
    print("WARN: SLIDES_MONTANA_L31 already exists. Skipping slide array insertion.")
    skip_slides = True
else:
    skip_slides = False

if not skip_slides:
    new_slide_arrays = ""
    for lid in range(31, 46):
        varname = f"SLIDES_MONTANA_L{lid:02d}"
        js_slides = to_js(ALL_SLIDES[lid])
        new_slide_arrays += f"\nexport const {varname} = {js_slides};\n"

    map_pos = content.find("export const MONTANA_ALL_SLIDES")
    content = content[:map_pos] + new_slide_arrays + "\n" + content[map_pos:]
    print("Added slide arrays for L31-L45")

# ─────────────────────────────────────────────
# 3. Update MONTANA_ALL_SLIDES map
# ─────────────────────────────────────────────
if '  31: SLIDES_MONTANA_L31' in content:
    print("WARN: L31 already in MONTANA_ALL_SLIDES. Skipping map update.")
else:
    # Find the closing }; of MONTANA_ALL_SLIDES
    old_entry = '  30: SLIDES_MONTANA_L30,'
    pos30 = content.find(old_entry)
    close_pos = content.find('};', pos30)

    new_entries = ""
    for lid in range(31, 46):
        new_entries += f"  {lid}: SLIDES_MONTANA_L{lid:02d},\n"

    content = content[:close_pos] + new_entries + content[close_pos:]
    print("Updated MONTANA_ALL_SLIDES map with L31-L45")

# ─────────────────────────────────────────────
# 4. Write updated file
# ─────────────────────────────────────────────
with open(data_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nFinal file size: {len(content):,} bytes")
print("\nSlide counts per lecture:")
for lid in range(31, 46):
    print(f"  L{lid}: {len(ALL_SLIDES[lid])} slides")
total = sum(len(v) for v in ALL_SLIDES.values())
print(f"  TOTAL L31-L45: {total} slides")
print("\nassemble_unit3.py COMPLETE!")
