import os
import sys
import re
import json

sys.stdout.reconfigure(encoding="utf-8")

lectures_dir = r"c:\Oikos Univ\Montana_State_Univ\lectures"
output_js = r"c:\Oikos Univ\src\data\montanaSlidesData.js"

lectures = []

for i in range(1, 16):
    fname = f"lecture{i:02d}.md"
    fpath = os.path.join(lectures_dir, fname)
    if not os.path.exists(fpath):
        continue
    
    with open(fpath, encoding="utf-8") as f:
        content = f.read()
    
    # Extract Title & Metadata
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    lecture_title = title_match.group(1).strip() if title_match else f"Lecture {i:02d}"
    
    # Split slides by ## Slide
    slide_chunks = re.split(r"\n##\s+Slide\s+", content)
    slides = []
    
    for chunk in slide_chunks[1:]:
        lines = chunk.strip().split("\n")
        header_line = lines[0].strip()
        
        num_match = re.match(r"^(\d+):\s*(.+)$", header_line)
        slide_num = int(num_match.group(1)) if num_match else len(slides) + 1
        slide_title = num_match.group(2).strip() if num_match else header_line
        
        chunk_text = "\n".join(lines[1:])
        
        # Extract Slide Type
        type_match = re.search(r"\*\*Slide Type:\*\*\s*(.+)", chunk_text)
        slide_type_str = type_match.group(1).strip() if type_match else "Problem Breakdown"
        
        # Extract Workbook Source
        source_match = re.search(r"\*\*Workbook Source:\*\*\s*(.+)", chunk_text)
        workbook_source = source_match.group(1).strip() if source_match else f"Unit 1 • Lecture {i:02d}"
        
        # Extract Problem Statement
        prob_match = re.search(r"###\s+📝\s+Problem Statement[^\n]*\n([\s\S]*?)(?=###|\Z)", chunk_text)
        if not prob_match:
            prob_match = re.search(r"###\s+📝\s+[^\n]*\n([\s\S]*?)(?=###|\Z)", chunk_text)
        problem_text = prob_match.group(1).strip() if prob_match else ""
        
        # Extract AI Solution Breakdown
        sol_match = re.search(r"###\s+💡\s+AI Step-by-Step Solution Breakdown[^\n]*\n([\s\S]*?)(?=###|\Z)", chunk_text)
        if not sol_match:
            sol_match = re.search(r"###\s+💡\s+[^\n]*\n([\s\S]*?)(?=###|\Z)", chunk_text)
        solution_text = sol_match.group(1).strip() if sol_match else ""
        
        # Extract Sora Pitfall Alert
        pit_match = re.search(r"###\s+⚠️\s+Sora's Pitfall Alert[^\n]*\n([\s\S]*?)(?=###|\Z)", chunk_text)
        pitfall_text = pit_match.group(1).strip() if pit_match else ""
        
        # Extract Dialogue Script
        script_match = re.search(r"###\s+🎙️\s+English Lecture Script[^\n]*\n([\s\S]*?)(?=###|\Z)", chunk_text)
        script_text = script_match.group(1).strip() if script_match else ""
        
        slides.append({
            "num": slide_num,
            "type": "math_problem",
            "slideTypeLabel": slide_type_str,
            "title": slide_title,
            "subtitle": f"Unit 1 • Lecture {i:02d} • {workbook_source}",
            "detail": lecture_title,
            "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
            "problem": problem_text,
            "solution": solution_text,
            "pitfall": pitfall_text,
            "script": script_text
        })
    
    lectures.append({
        "id": i,
        "lectureNum": i,
        "title": f"Lecture {i:02d}: {lecture_title.split(':')[-1].strip() if ':' in lecture_title else lecture_title}",
        "fullTitle": lecture_title,
        "active": True,
        "slides": slides
    })

# Format as JavaScript module export
js_content = "/* Montana State University - Gallatin College: M090 Introductory Algebra (Unit 1: Lectures 01-15) - 100% English */\n\n"

lecture_meta = [{"id": l["id"], "title": l["title"], "active": True} for l in lectures]
js_content += f"export const MONTANA_LECTURES = {json.dumps(lecture_meta, ensure_ascii=False, indent=2)};\n\n"

for l in lectures:
    var_name = f"SLIDES_MONTANA_L{l['id']:02d}"
    js_content += f"export const {var_name} = {json.dumps(l['slides'], ensure_ascii=False, indent=2)};\n\n"

js_content += "export const MONTANA_ALL_SLIDES = {\n"
for l in lectures:
    js_content += f"  {l['id']}: SLIDES_MONTANA_L{l['id']:02d},\n"
js_content += "};\n"

with open(output_js, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated 100% pure English {output_js}")
