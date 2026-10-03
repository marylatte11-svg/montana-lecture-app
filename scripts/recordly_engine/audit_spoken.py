import sys, os
sys.path.insert(0, r"c:\Oikos Univ")
import json
from scripts.recordly_engine.render_montana_recordly import convert_math_to_spoken_english, load_official_montana_slides

slides = load_official_montana_slides(1)
for s in slides:
    print(f"\n==========================================")
    print(f"SLIDE {s['num']}: {s['title']}")
    print(f"==========================================")
    for idx, t in enumerate(s['turns']):
        raw = t['raw_text']
        spoken = t['spoken_text']
        print(f"--- Turn {idx+1} ({t['speaker_name']}) ---")
        print(f"RAW:    {raw}")
        print(f"SPOKEN: {spoken}")
