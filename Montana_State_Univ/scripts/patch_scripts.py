# -*- coding: utf-8 -*-
"""
patch_scripts.py
Applies high-volume broadcast tiki-taka scripts to montanaSlidesData.js
"""
import sys
import os
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

data_file = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'data', 'montanaSlidesData.js'))

def apply_scripts_to_data(scripts_dict, lecture_id):
    """
    scripts_dict: { slide_num: script_text }
    lecture_id: int (e.g. 31)
    """
    with open(data_file, 'r', encoding='utf-8') as f:
        content = f.read()

    marker = f'SLIDES_MONTANA_L{lecture_id:02d}'
    sec_start = content.find(marker)
    if sec_start == -1:
        print(f"ERROR: Marker {marker} not found!")
        return False

    next_marker = f'SLIDES_MONTANA_L{lecture_id+1:02d}'
    sec_end = content.find(next_marker, sec_start)
    if sec_end == -1:
        sec_end = content.find('export const MONTANA_ALL_SLIDES', sec_start)
    if sec_end == -1:
        sec_end = len(content)

    lecture_content = content[sec_start:sec_end]

    # For each slide, find "num": slide_num, then replace its "script": "..."
    modified_lecture_content = lecture_content

    for slide_key, new_script in sorted(scripts_dict.items(), key=lambda x: int(x[0])):
        slide_num = int(slide_key)
        # Find where this slide starts
        slide_pattern = rf'("num":\s*{slide_num},[\s\S]*?)(}}|\Z)'
        # More precise: find "num": slide_num, then find the next "script": "..." before the next slide
        num_pos = modified_lecture_content.find(f'"num": {slide_num},')
        if num_pos == -1:
            num_pos = modified_lecture_content.find(f'"num":{slide_num},')
        if num_pos == -1:
            print(f"WARN: Slide {slide_num} not found in L{lecture_id}")
            continue

        # Next slide pos or end of array
        next_slide_pos = modified_lecture_content.find(f'"num": {slide_num + 1},', num_pos)
        if next_slide_pos == -1:
            next_slide_pos = len(modified_lecture_content)

        slide_block = modified_lecture_content[num_pos:next_slide_pos]

        # Find "script": "..." inside slide_block
        # We need to match "script": "..." with escaped quotes properly
        # JSON serialize new_script
        new_script_json = json.dumps(new_script, ensure_ascii=False)

        # Regex to find "script": "..." (matching multiline string if broken, or standard single line)
        script_pattern = r'("script":\s*)"(?:\\.|[^"\\])*"'
        if re.search(script_pattern, slide_block):
            new_slide_block = re.sub(script_pattern, lambda m: m.group(1) + new_script_json, slide_block, count=1)
            modified_lecture_content = modified_lecture_content[:num_pos] + new_slide_block + modified_lecture_content[next_slide_pos:]
            print(f"  Updated L{lecture_id} Slide {slide_num} script ({len(new_script.split())} words)")
        else:
            # Fallback if the previous corrupted script had raw multiline
            corrupt_pattern = r'("script":\s*)"[\s\S]*?"\s*(?=,|\n\s*})'
            if re.search(corrupt_pattern, slide_block):
                new_slide_block = re.sub(corrupt_pattern, lambda m: m.group(1) + new_script_json, slide_block, count=1)
                modified_lecture_content = modified_lecture_content[:num_pos] + new_slide_block + modified_lecture_content[next_slide_pos:]
                print(f"  Updated L{lecture_id} Slide {slide_num} script (recovered multiline, {len(new_script.split())} words)")
            else:
                print(f"WARN: 'script' field not found in L{lecture_id} Slide {slide_num}")

    new_content = content[:sec_start] + modified_lecture_content + content[sec_end:]

    with open(data_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Successfully applied scripts to L{lecture_id} in {data_file}")
    return True

if __name__ == '__main__':
    from unit3_scripts_l31 import SCRIPTS_L31
    apply_scripts_to_data(SCRIPTS_L31, 31)
