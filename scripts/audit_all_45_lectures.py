import re
import json

def deep_audit():
    with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find each lecture array
    lectures = re.findall(r'export const (SLIDES_MONTANA_L(\d+))\s*=\s*(\[.*?\]);', content, re.DOTALL)
    print(f"Found {len(lectures)} lecture definitions.")

    stats = {
        "total_slides": 0,
        "single_line_problems": [],
        "slides_per_lecture": {},
        "empty_problems": [],
        "problem_types": set()
    }

    for const_name, lec_id_str, array_str in lectures:
        lec_id = int(lec_id_str)
        # Parse JSON array: in JS, property names might be unquoted or double quoted
        # Since montanaSlidesData.js uses valid JSON-like object notation:
        # let's extract each slide object
        slide_objs = re.findall(r'(\{[^{}]*"num":\s*\d+.*?script":\s*"(?:\\.|[^"\\])*"\s*\})', array_str, re.DOTALL)
        stats["slides_per_lecture"][lec_id] = len(slide_objs)
        stats["total_slides"] += len(slide_objs)

        for s_raw in slide_objs:
            # extract num
            num_m = re.search(r'"num":\s*(\d+)', s_raw)
            slide_num = int(num_m.group(1)) if num_m else 0
            
            # extract problem
            prob_m = re.search(r'"problem":\s*("(?:\\.|[^"\\])*")', s_raw)
            if prob_m:
                prob = json.loads(prob_m.group(1))
                # Check single-line math + text
                if prob.startswith("$$") and ("\\text{" in prob) and ("\n\n$$" not in prob):
                    stats["single_line_problems"].append((lec_id, slide_num, prob))
                elif prob.startswith("$$") and len(prob) > 90 and ("\n\n$$" not in prob):
                    # Check if it has text or is just long
                    if "\\text{" in prob:
                        stats["single_line_problems"].append((lec_id, slide_num, prob))

    print(f"Total slides processed: {stats['total_slides']}")
    print(f"Single line problems needing 2-line split: {len(stats['single_line_problems'])}")
    for lec_id, s_num, prob in stats['single_line_problems']:
        print(f"L{lec_id:02d} S{s_num:02d}: {prob[:90]}...")

if __name__ == '__main__':
    deep_audit()
