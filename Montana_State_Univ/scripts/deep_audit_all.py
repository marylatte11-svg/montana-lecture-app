import json
import re

with open('Montana_State_Univ/scripts/full_slide_script_audit.json', 'r', encoding='utf-8') as f:
    slides = json.load(f)

print(f"Loaded {len(slides)} slides. Checking consistency across all lectures...")

suspects = []

for s in slides:
    lec = s['lec']
    num = s['slide']
    title = s['title']
    prob = s['problemShort']
    script = s['scriptShort']
    
    # Extract math formulas in title: e.g. $...$
    math_in_title = re.findall(r'\$([^\$]+)\$', title)
    
    # If title has a specific equation like f(x) = ... or 2x - 3 = 5, check if the formula appears in script
    for m in math_in_title:
        # Simplify math expression to core alphanumeric and operations
        # e.g., "g(x) = x^2 + 6x" -> check if "x^2 + 6x" or "x^2+6x" in script
        clean_m = re.sub(r'\\(?:dfrac|frac|cdot|times|text\{[^}]+\})', '', m)
        clean_m = re.sub(r'\s+', '', clean_m)
        
        # We only care about equations or expressions with numbers/variables longer than 3 chars
        if len(clean_m) >= 4 and not clean_m.startswith('\\Delta') and not clean_m.startswith('\\mathbb'):
            # search in script
            clean_script = re.sub(r'\s+', '', script)
            clean_script_full = clean_script # search in full
            
            # Check if clean_m is in script
            if clean_m not in clean_script:
                # Also try checking just the right side of = if any
                if '=' in clean_m:
                    rhs = clean_m.split('=')[1]
                    lhs = clean_m.split('=')[0]
                    if len(rhs) >= 4 and rhs in clean_script:
                        continue
                    if len(lhs) >= 4 and lhs in clean_script:
                        continue
                
                suspects.append({
                    'lec': lec,
                    'slide': num,
                    'title': title,
                    'missing_term': clean_m,
                    'script_head': script[:140]
                })

print(f"\nTotal suspicious mismatches found: {len(suspects)}")
# Group by lecture
by_lec = {}
for sus in suspects:
    by_lec.setdefault(sus['lec'], []).append(sus)

for l in sorted(by_lec.keys()):
    print(f"\n--- Lecture {l} ({len(by_lec[l])} items) ---")
    for item in by_lec[l]:
        print(f"  Slide {item['slide']}: {item['title']}")
        print(f"    Target formula: '{item['missing_term']}'")
        print(f"    Script preview: {item['script_head']}")
