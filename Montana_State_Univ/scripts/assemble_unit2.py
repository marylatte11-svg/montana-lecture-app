# Assembles all Unit 2 expanded lectures and updates montanaSlidesData.js
import json
import re
import os
import sys

from unit2_data_l16_l20 import data_16_20
from unit2_data_l21_l25 import data_21_25
from unit2_data_l26_l30 import data_26_30

all_unit2 = {}
all_unit2.update(data_16_20)
all_unit2.update(data_21_25)
all_unit2.update(data_26_30)

print(f"Total Unit 2 lectures ready: {len(all_unit2)}")
for lec_num in sorted(all_unit2.keys()):
    slides = all_unit2[lec_num]
    graph_count = sum(1 for s in slides if "graph" in s)
    print(f"Lecture {lec_num}: {len(slides)} slides (with {graph_count} Cartesian grids)")

# Convert python dictionary to JavaScript code
def to_js_code(lec_id, slides):
    js_slides = json.dumps(slides, indent=2)
    return f"export const SLIDES_MONTANA_L{lec_id:02d} = {js_slides};\n"

js_blocks = []
for lec_id in range(16, 31):
    js_blocks.append(to_js_code(lec_id, all_unit2[lec_id]))

unit2_js_text = "\n".join(js_blocks)

# Read montanaSlidesData.js
js_file_path = os.path.abspath("src/data/montanaSlidesData.js")
with open(js_file_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# Find where SLIDES_MONTANA_L16 begins and where MONTANA_ALL_SLIDES begins
start_marker = "export const SLIDES_MONTANA_L16 = ["
end_marker = "export const MONTANA_ALL_SLIDES = {"

start_idx = js_content.find(start_marker)
end_idx = js_content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print(f"ERROR: Markers not found! start_idx={start_idx}, end_idx={end_idx}")
    sys.exit(1)

new_content = js_content[:start_idx] + unit2_js_text + "\n" + js_content[end_idx:]

with open(js_file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"SUCCESS: {js_file_path} updated with expanded Unit 2 slides!")
