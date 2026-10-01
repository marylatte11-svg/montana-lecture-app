import json
import re

with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's extract each lecture array
lecture_pattern = r'export const (SLIDES_MONTANA_L\d+) = (\[[\s\S]*?\n\]);'
matches = re.findall(lecture_pattern, text)

print(f"Total lectures found: {len(matches)}")

audit_results = []

for lec_var, arr_text in matches:
    lec_id = int(re.search(r'\d+', lec_var).group())
    
    # Try parsing slides by finding slide objects
    # Object pattern: {"num": N, ...}
    # To parse safely in JS, let's extract objects with regex
    slide_chunks = re.split(r'\n    \{', arr_text)
    
    for chunk in slide_chunks[1:]: # skip first
        num_m = re.search(r'"num":\s*(\d+)', chunk)
        if not num_m:
            continue
        slide_num = int(num_m.group(1))
        
        title_m = re.search(r'"title":\s*"([^"]+)"', chunk)
        title = title_m.group(1) if title_m else ""
        
        prob_m = re.search(r'"problem":\s*"([\s\S]*?)(?<!\\)",', chunk)
        prob = prob_m.group(1) if prob_m else ""
        
        script_m = re.search(r'"script":\s*"([\s\S]*?)(?<!\\)",', chunk)
        script = script_m.group(1) if script_m else ""
        
        # Check mismatch
        # Look at L43 slide 2 pattern: script mentions "x^2 - 36" or "Problem 1" while title is "g(x) = x^2 + 6x"
        # Extract main math expressions from problem and check if they appear in script
        audit_results.append({
            'lec': lec_id,
            'slide': slide_num,
            'title': title,
            'prob': prob[:120].replace('\n', ' '),
            'script_start': script[:150].replace('\n', ' '),
            'script_full': script
        })

print(f"Total slides extracted: {len(audit_results)}")

# Let's check L43 specifically first
print("\n--- LECTURE 43 SLIDES ---")
for s in audit_results:
    if s['lec'] == 43:
        print(f"L{s['lec']} S{s['slide']}: Title='{s['title']}'")
        print(f"   Script start: {s['script_start']}")
