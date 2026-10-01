"""
audit_coordinates.py
Audits which slides in Unit 3 (L31-L45) have coordinate grids vs not.
"""
import sys
import os
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

print("=== Coordinate Grid Audit: L31 ~ L45 ===\n")
total = 0
with_coord = 0
without_coord = []

for lid in range(31, 46):
    slides = ALL_SLIDES[lid]
    for s in slides:
        total += 1
        has_coord = 'coordinate' in s
        if has_coord:
            with_coord += 1
        else:
            without_coord.append((lid, s['num'], s.get('title', '')[:60]))

print(f"Total slides L31-L45: {total}")
print(f"With coordinate:      {with_coord}")
print(f"Without coordinate:   {total - with_coord}")
print()

print("Slides WITHOUT coordinate grid:")
for lid, num, title in without_coord:
    print(f"  L{lid} Slide {num}: {title}")
