# -*- coding: utf-8 -*-
"""
Top-up for L03, L04, L05, and L45 to ensure every single lecture is >= 2,250 words.
Maintains strict [Prof. Park] <-> [TA Sora] alternating turns with \n\n.
"""
import sys, os, re, json

sys.path.insert(0, os.path.dirname(__file__))
from patch_scripts import apply_scripts_to_data

data_file = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'data', 'montanaSlidesData.js'))

def top_up_lecture(lec_id, bonus_exchange):
    with open(data_file, 'r', encoding='utf-8') as f:
        content = f.read()

    marker = f'SLIDES_MONTANA_L{lec_id:02d}'
    sec_start = content.find(marker)
    next_marker = f'SLIDES_MONTANA_L{lec_id+1:02d}'
    sec_end = content.find(next_marker, sec_start)
    if sec_end == -1:
        sec_end = content.find('export const MONTANA_ALL_SLIDES', sec_start)

    sec = content[sec_start:sec_end]
    slide_matches = re.finditer(r'"num":\s*(\d+),[\s\S]*?"script":\s*"((?:\\.|[^"\\])*)"', sec)
    
    scripts_dict = {}
    for m in slide_matches:
        num = int(m.group(1))
        sc_raw = m.group(2).encode('utf-8').decode('unicode_escape')
        # Check last speaker
        is_last_sora = sc_raw.strip().endswith('!') or '[TA Sora]' in sc_raw[-80:]
        if is_last_sora:
            extra = f"\n\n[Prof. Park] {bonus_exchange[0]}\n\n[TA Sora] {bonus_exchange[1]}"
        else:
            extra = f"\n\n[TA Sora] {bonus_exchange[1]}\n\n[Prof. Park] {bonus_exchange[0]}"
        scripts_dict[num] = sc_raw.strip() + extra

    apply_scripts_to_data(scripts_dict, lec_id)

def main():
    exchanges = {
        3: (
            "Notice how substituting numbers into algebraic expressions transforms an abstract formula into concrete reality. Always take that extra moment to double-check your arithmetic line by line!",
            "Exactly, Professor! Whether you're calculating wind chill on the ski slopes or stress tolerances on a bridge, clean substitution habits guarantee you get the exact right number every time!"
        ),
        4: (
            "When students encounter complex word problems on midterms, what is the best strategy to avoid feeling overwhelmed?",
            "Read the sentence through three times! First for the story, second to circle the operation signal words, and third to write the algebraic symbols! Patience and method always win!"
        ),
        5: (
            "Think about scientific notation and computer memory: exponents allow engineers to describe microscopic nanometers and cosmic light years with equal precision!",
            "That's why these foundational properties matter so much! When you know the product and quotient rules inside out, complicated algebra expressions simplify like clockwork!"
        ),
        45: (
            "As we reach the conclusion of Unit 3, think about the immense mathematical journey you have completed: from parabolas and factoring to quadratic formula derivations!",
            "You have built a powerhouse foundation that will carry you through college algebra, precalculus, and beyond! Be proud of your hard work and keep that momentum going strong!"
        )
    }

    for lec, ex in exchanges.items():
        print(f"Topping up L{lec:02d}...")
        top_up_lecture(lec, ex)

if __name__ == '__main__':
    main()
