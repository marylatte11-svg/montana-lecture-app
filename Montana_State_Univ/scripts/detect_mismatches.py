import json
import re

with open('Montana_State_Univ/scripts/full_slide_script_audit.json', 'r', encoding='utf-8') as f:
    slides = json.load(f)

mismatches = []

for s in slides:
    lec = s['lec']
    num = s['slide']
    title = s['title']
    prob = s['problemShort']
    script = s['scriptShort']
    
    # Extract math terms from title and problem
    # Look for functions like g(x) = ..., equations like 2x^2 ..., etc.
    # Look for specific numbers in problem
    title_formulas = re.findall(r'\$([^\$]+)\$', title)
    prob_formulas = re.findall(r'\$\$?([^\$]+)\$\$?', prob)
    
    # Check if any distinctive equation in title or problem is missing in script
    # Special focus on Unit 3 (Lectures 31 to 45) and Unit 2 (Lectures 16 to 30)
    issue = False
    details = []
    
    # Check common quadratic equations
    # e.g. title has x^2 + 6x, but script mentions x^2 - 36
    if "x^2 + 6x" in title and "x^2 - 36" in script:
        issue = True
        details.append("Title has x^2+6x but script has x^2-36")
    elif "h(x) = -2x^2 + 5x + 6" in title and "x^2 - 7x + 10" in script:
        issue = True
        details.append("Title has -2x^2+5x+6 but script has x^2-7x+10")
    elif "f(x) = 4x^2 - 28" in title and "x^2 + 6x - 2" in script:
        issue = True
        details.append("Title has 4x^2-28 but script has x^2+6x-2")
    elif "f(x) = x^2 - 15x + 50" in title and "3x^2 - 5x - 4" in script:
        issue = True
        details.append("Title has x^2-15x+50 but script has 3x^2-5x-4")
    elif "h(x) = x^2 - 5x - 7" in title and "2x^2 + 5x - 3" in script:
        issue = True
        details.append("Title has x^2-5x-7 but script has 2x^2+5x-3")
    elif "h(x) = 13x - x^2 + 1" in title and "3x^2 - 4x + 1" in script:
        issue = True
        details.append("Title has 13x-x^2+1 but script has 3x^2-4x+1")
    elif "f(x) = -x^2 - 5x + 7" in title and "x^2 + 4x + 1" in script:
        issue = True
        details.append("Title has -x^2-5x+7 but script has x^2+4x+1")
    elif "f(x) = -1 + 2x^2 - 3x" in title and "3x^2" in script and "-1 + 2x^2 - 3x" not in script:
        issue = True
        details.append("Title has -1+2x^2-3x but script has 3x^2")
    elif "g(x) = 2x^2 - 8x" in title and "x^2 + 2x + 2" in script:
        issue = True
        details.append("Title has 2x^2-8x but script has x^2+2x+2")
    elif "f(x) = -\\frac{1}{2}(x+1)^2 + 8" in title and "-x^2 + 4x - 4" in script:
        issue = True
        details.append("Title has vertex form -1/2(x+1)^2+8 but script has -x^2+4x-4")

    # General heuristic: check if title formula numbers are mentioned at all in the first 200 chars of script
    # Only for problem slides (not intro or summary)
    if not issue and "Example" in title or "Problem" in title or "Board Work" in title:
        # Check if the title formula appears in script
        for tf in title_formulas:
            clean_tf = tf.replace(' ', '').replace('\\,', '')
            clean_sc = script.replace(' ', '').replace('\\,', '')
            if len(clean_tf) > 4 and clean_tf not in clean_sc:
                # Potential mismatch
                pass

    if issue:
        mismatches.append({
            'lec': lec,
            'slide': num,
            'title': title,
            'details': details
        })

print(f"Found {len(mismatches)} specific known mismatches:")
for m in mismatches:
    print(f"  L{m['lec']} S{m['slide']}: {m['title']} -> {m['details']}")
