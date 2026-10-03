import re
import json

# Read lecture01.md
with open(r"c:\Oikos Univ\Montana_State_Univ\lectures\lecture01.md", "r", encoding="utf-8") as f:
    text = f.read()

slides_raw = re.split(r'###\s*\[Slide\s*(\d+)\]', text)[1:]
new_slides = []

for i in range(0, len(slides_raw), 2):
    s_num = int(slides_raw[i])
    s_body = slides_raw[i+1]

    lines = s_body.strip().split('\n')
    title = lines[0].strip()

    sub_match = re.search(r'\*([^*]+)\*', s_body)
    sub = sub_match.group(1).strip() if sub_match else ''

    prob_match = re.search(r'####\s*📖\s*Official Workbook Problem[^\n]*\n([\s\S]*?)(?=####|\n---\s*\n|\Z)', s_body)
    prob = prob_match.group(1).strip() if prob_match else ''

    sol_match = re.search(r'####\s*💡\s*Complete Step-by-Step Solution[^\n]*\n([\s\S]*?)(?=####|\n---\s*\n|\Z)', s_body)
    sol = sol_match.group(1).strip() if sol_match else ''

    pit_match = re.search(r'####\s*⚠️\s*Pitfall & Strategy[^\n]*\n([\s\S]*?)(?=####|\n---\s*\n|\Z)', s_body)
    pit = pit_match.group(1).strip() if pit_match else ''

    diag_match = re.search(r'####\s*🎙️\s*Lecture Dialogue[^\n]*\n([\s\S]*?)(?=\n---\s*\n|\Z)', s_body)
    diag = diag_match.group(1).strip() if diag_match else ''

    # Custom enrichment for Slide 1 Orientation
    if s_num == 1:
        slide_type = "Course Orientation & Welcome"
        prob = (
            "$$\\mathbf{M090\\text{ Introductory Algebra} \\quad \\bullet \\quad \\text{Montana State University}}$$\n"
            "- **Instructional Team:** Prof. Eunju Park (Lead Instructor) & TA Sora (Gallatin College)\n"
            "- **Teaching Philosophy:** Banish math anxiety through conceptual understanding and practical modeling.\n"
            "- **The Golden Rule:** **One Problem = One Slide** (Zero clutter, 100% step-by-step clarity).\n"
            "- **Course Materials:** Gallatin College M090 Student Notes Packet (Section 1.0, Page 3)."
        )
        pit = "**Sora's Pro-Tip:** Never hesitate to ask questions! In M090, every question helps the entire class learn and succeed together."
    elif s_num == 2:
        slide_type = "Core Mathematical Definition"
    elif s_num == 3:
        slide_type = "Conceptual Dissection"
    else:
        bw_num = s_num - 3
        slide_type = f"Workbook Board Work #{bw_num}"

    new_slides.append({
        "num": s_num,
        "type": "math_problem",
        "slideTypeLabel": slide_type,
        "title": title,
        "subtitle": sub,
        "detail": "Lecture 01: Welcome to M090 & The Language of Algebra",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": prob,
        "solution": sol,
        "pitfall": pit,
        "script": diag
    })

# Format as JavaScript array
js_code = "export const SLIDES_MONTANA_L01 = " + json.dumps(new_slides, indent=2, ensure_ascii=False) + ";\n"

# Replace SLIDES_MONTANA_L01 in montanaSlidesData.js using string partition or lambda to avoid backslash escaping issues
target_file = r"c:\Oikos Univ\src\data\montanaSlidesData.js"
with open(target_file, "r", encoding="utf-8") as f:
    orig_content = f.read()

pattern = r"export const SLIDES_MONTANA_L01 = \[[\s\S]*?\n\];"
if not re.search(pattern, orig_content):
    print("ERROR: Could not find SLIDES_MONTANA_L01 pattern in montanaSlidesData.js!")
else:
    # Use lambda to avoid re.sub interpretation of \n as literal newlines!
    updated_content = re.sub(pattern, lambda m: js_code.strip(), orig_content, count=1)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print("SUCCESS: Updated SLIDES_MONTANA_L01 in montanaSlidesData.js successfully with lambda replacement!")
