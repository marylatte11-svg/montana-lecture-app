import fitz
import json
import re
import os

pdf_path = r"c:\Oikos Univ\Montana_State_Univ\M090 Full Student Workbook.pdf"
output_json = r"c:\Oikos Univ\Montana_State_Univ\scripts\workbook_sections_index.json"

os.makedirs(os.path.dirname(output_json), exist_ok=True)

doc = fitz.open(pdf_path)

section_data = []

# Mapping defined in syllabus
sections = [
    {"unit": 1, "sec": "1.0", "title": "The Language of Algebra and Arithmetic Review", "pages": (7, 8)},
    {"unit": 1, "sec": "1.1", "title": "Evaluating and Translating Algebraic Expressions", "pages": (9, 10)},
    {"unit": 1, "sec": "1.2", "title": "Simplifying Monomial Expressions with Exponents", "pages": (11, 14)},
    {"unit": 1, "sec": "1.3", "title": "Adding and Subtracting Polynomials; Distributive Property", "pages": (15, 16)},
    {"unit": 1, "sec": "1.4", "title": "Multiplying Polynomials", "pages": (17, 18)},
    {"unit": 1, "sec": "1.5", "title": "Adding and Subtracting Rational Expressions", "pages": (19, 20)},
    {"unit": 1, "sec": "1.6", "title": "Solving Linear Equations", "pages": (21, 22)},
    {"unit": 1, "sec": "1.7", "title": "Solving Linear Equations with Fractions", "pages": (23, 25)},
    {"unit": 1, "sec": "1.8", "title": "Solving Formulas for a Specified Variable", "pages": (26, 27)},
    {"unit": 1, "sec": "1.9", "title": "Solving Linear Inequalities", "pages": (28, 32)},
    {"unit": 2, "sec": "2.0", "title": "Intro to Graphing", "pages": (33, 35)},
    {"unit": 2, "sec": "2.1", "title": "Linear Equations in Two Variables", "pages": (36, 40)},
    {"unit": 2, "sec": "2.2", "title": "Slope of a Line", "pages": (41, 43)},
    {"unit": 2, "sec": "2.3", "title": "Finding the Equation of a Line", "pages": (44, 47)},
    {"unit": 2, "sec": "2.4", "title": "Intro to Functions", "pages": (48, 49)},
    {"unit": 2, "sec": "2.5", "title": "Function Notation", "pages": (50, 53)},
    {"unit": 2, "sec": "2.6", "title": "Linear Functions", "pages": (54, 55)},
    {"unit": 2, "sec": "2.7", "title": "Applications of Linear Functions", "pages": (56, 59)},
    {"unit": 3, "sec": "3.0", "title": "Intro to Quadratic Functions", "pages": (62, 65)},
    {"unit": 3, "sec": "3.1", "title": "Finding the Vertex and y-intercept for Quadratic Functions", "pages": (66, 68)},
    {"unit": 3, "sec": "3.2", "title": "Finding Intercepts of Quadratic Functions (Square Root Property)", "pages": (69, 72)},
    {"unit": 3, "sec": "3.3", "title": "Finding Intercepts of Quadratic Functions (Greatest Common Factor)", "pages": (73, 76)},
    {"unit": 3, "sec": "3.4_1", "title": "Finding Intercepts of Quadratic Functions (Factoring Trinomials Part 1)", "pages": (77, 78)},
    {"unit": 3, "sec": "3.4_2", "title": "Finding Intercepts of Quadratic Functions (Factoring Trinomials Part 2)", "pages": (79, 81)},
    {"unit": 3, "sec": "3.5", "title": "Finding Intercepts of Quadratic Functions (Quadratic Formula)", "pages": (82, 85)},
    {"unit": 3, "sec": "3.6", "title": "Finding Intercepts and Vertex for Quadratic Functions", "pages": (86, 89)},
    {"unit": 3, "sec": "3.7", "title": "Graphing Quadratic Functions", "pages": (90, 93)}
]

for s in sections:
    p_start, p_end = s["pages"]
    extracted_text = ""
    for p in range(p_start - 1, min(p_end, len(doc))):
        extracted_text += f"\n--- Page {p+1} ---\n" + doc[p].get_text()
    
    section_data.append({
        "unit": s["unit"],
        "section": s["sec"],
        "title": s["title"],
        "startPage": p_start,
        "endPage": p_end,
        "charCount": len(extracted_text),
        "text": extracted_text
    })

with open(output_json, "w", encoding="utf-8") as f:
    json.dump(section_data, f, ensure_ascii=False, indent=2)

print(f"Successfully extracted {len(section_data)} sections into {output_json}")
