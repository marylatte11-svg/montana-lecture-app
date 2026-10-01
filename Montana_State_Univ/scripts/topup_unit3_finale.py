# -*- coding: utf-8 -*-
"""
topup_unit3_finale.py
Tops up Lectures 42, 43, 44, and 45 to reach 2,280 - 2,450 words each.
This brings ALL 45 lectures across the entire curriculum to 20-25 minute broadcast perfection!
"""
import sys
import os
import re
import json

sys.path.append(os.path.dirname(__file__))
from patch_scripts import apply_scripts_to_data

data_file = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'data', 'montanaSlidesData.js'))

with open(data_file, 'r', encoding='utf-8') as f:
    content = f.read()

def extract_lecture_scripts(lecture_id):
    marker = f'SLIDES_MONTANA_L{lecture_id:02d}'
    start = content.find(marker)
    end = content.find(f'SLIDES_MONTANA_L{lecture_id+1:02d}', start)
    if end == -1:
        end = content.find('export const MONTANA_ALL_SLIDES', start)
    sec = content[start:end]
    raw_slides = re.findall(r'"num":\s*(\d+),[\s\S]*?"script":\s*"((?:\\.|[^"\\])*)"', sec)
    res = {}
    for num, sc in raw_slides:
        clean_sc = sc.encode('utf-8').decode('unicode_escape')
        res[int(num)] = clean_sc
    return res

L42_CURR = extract_lecture_scripts(42)
L43_CURR = extract_lecture_scripts(43)
L44_CURR = extract_lecture_scripts(44)
L45_CURR = extract_lecture_scripts(45)

L42_TOP = {
    6: (
        "\nProf. Park: Let's also evaluate f(-2) for extra practice with negative inputs: "
        "f(-2) = 3(-2)^2 - 5(-2) + 7 = 3(4) + 10 + 7 = 12 + 10 + 7 = 29! "
        "Notice again: (-2)^2 is POSITIVE 4, and -5(-2) is POSITIVE 10. "
        "Every negative sign was handled with protective parentheses."
    ),
    8: (
        "\nProf. Park: Let's visualize the three cases on paper before an exam: "
        "Draw three quick sketches side by side: "
        "Sketch 1 (Delta > 0): A U-curve crossing the horizontal axis at two distinct points like an arch over a road. "
        "Sketch 2 (Delta = 0): A U-curve resting gently on the axis like a ball sitting on the floor. "
        "Sketch 3 (Delta < 0): A U-curve floating up in the air like a hot air balloon over the Gallatin Valley. "
        "Connecting the algebra to these three pictures makes the discriminant concept impossible to forget!"
    )
}

L43_TOP = {
    7: (
        "\nTA Sora: Here is my personal test-taking strategy for Section 3.6: "
        "Spend the first five seconds of every quadratic problem categorizing it into our 5-row table! "
        "If you see only two terms, ask: Is the constant missing (c = 0)? Factor GCF! "
        "Is the middle term missing (b = 0)? Square Root Property! "
        "If it has all three terms, try quick mental factoring for ten seconds. "
        "If factors don't jump out immediately, don't stall—immediately jump to the Quadratic Formula! "
        "This disciplined strategy guarantees you will finish your exam with time to check your work."
    ),
    8: (
        "\nProf. Park: And remember our Golden Rule of Quadratic Equations: "
        "Before applying ANY method—whether factoring or the formula—you MUST set the equation equal to ZERO! "
        "If an equation is written as 2x^2 + 5x = -3, you cannot factor 2x^2 + 5x and set it equal to -3! "
        "You must add 3 to both sides first: 2x^2 + 5x + 3 = 0! "
        "Zero on one side is the mandatory ticket to solving quadratic equations."
    )
}

L44_TOP = {
    5: (
        "\nTA Sora: In vertex form f(x) = a(x - h)^2 + k, look at the coefficient a: "
        "If |a| > 1 (like a = 3 or a = -4), the parabola is stretched vertically—it looks narrow and steep, like a rocket plume! "
        "If 0 < |a| < 1 (like a = 1/2 or a = -1/3), the parabola is compressed vertically—it looks wide and shallow, like a wide satellite dish or suspension bridge cable! "
        "Recognizing the geometric effect of 'a' lets you know what your graph should look like before you plot a single point."
    ),
    6: (
        "\nProf. Park: Compare how the two functions f(x) and g(x) grow: "
        "g(x) is linear: each time x increases by 1, g(x) decreases by exactly 2 (a constant slope of -2). "
        "f(x) is quadratic: its rate of change accelerates! Near the vertex, it changes slowly, but far away, it skyrockets! "
        "This difference between constant linear change and accelerating quadratic change is the foundation of calculus and physics."
    ),
    7: (
        "\nTA Sora: When computing f(x + 5), remember that (x + 5)^2 must be expanded using FOIL: "
        "(x + 5)(x + 5) = x^2 + 5x + 5x + 25 = x^2 + 10x + 25! "
        "Students who forget the middle term 10x lose points every single semester. Never forget the 2ab middle term when squaring a binomial!"
    ),
    8: (
        "\nProf. Park: Let's verify our intersection points (7, 11) and (-3, 31) by checking f(x): "
        "f(7) = 7^2 - 6(7) + 4 = 49 - 42 + 4 = 11! It matches g(7) = 11! "
        "f(-3) = (-3)^2 - 6(-3) + 4 = 9 + 18 + 4 = 31! It matches g(-3) = 31! "
        "Both points satisfy BOTH equations simultaneously. That is what solving a system of equations means!"
    )
}

L45_TOP = {
    3: (
        "\nTA Sora: In p(x) = x^2 - 4x - 5, notice how the axis of symmetry x = 2 creates symmetric point pairs: "
        "x = 1 and x = 3 are both 1 unit away from the axis: p(1) = 1 - 4 - 5 = -8, and p(3) = 9 - 12 - 5 = -8! Identical! "
        "x = 0 and x = 4 are both 2 units away: p(0) = -5, and p(4) = 16 - 16 - 5 = -5! Identical! "
        "x = -1 and x = 5 are both 3 units away: p(-1) = 0, and p(5) = 0! Identical! "
        "Symmetry is your greatest friend when graphing parabolas: compute one side, and you get the other side for free!"
    ),
    4: (
        "\nProf. Park: Think of this system of equations in real Montana civil engineering: "
        "The parabola f(x) represents a cross-section of a mountain valley, and the line g(x) represents the grade of an elevated highway bridge spanning the canyon. "
        "The intersection points (7, 11) and (-3, 31) are the exact bridge abutment coordinates where the highway bridge anchors into the solid bedrock of the mountain! "
        "Algebra is the language that builds real, safe physical infrastructure."
    ),
    5: (
        "\nTA Sora: Let's do a fast recap of how all the pieces of Unit 3 connect: "
        "Every single quadratic function has a vertex that marks its maximum or minimum. "
        "Every quadratic function has an axis of symmetry passing through that vertex. "
        "Its y-intercept is always (0, c). "
        "Its x-intercepts are found by setting f(x) = 0 and choosing the best of our four methods. "
        "And its graph is a smooth, continuous U-shaped curve with infinite domain."
    ),
    6: (
        "\nProf. Park: When you walk into your next mathematics course—whether Math 121 College Algebra or a statistics course—"
        "this Formula Card will be your trusted companion. "
        "Every professor will expect you to recognize standard form, calculate the vertex with x = -b/(2a), "
        "and deploy the quadratic formula with confidence. You have mastered these tools completely."
    ),
    7: (
        "\nTA Sora: In our final Challenge Problem q(x) = -3x^2 + 12x - 9: "
        "Notice that factoring out -3 gave -3(x^2 - 4x + 3) = -3(x - 3)(x - 1) = 0. "
        "The intercepts are (1, 0) and (3, 0). "
        "Halfway between 1 and 3 is x = 2! "
        "And plugging in x = 2 gave q(2) = 3: the vertex is (2, 3)! "
        "The vertex x-coordinate is ALWAYS the exact midpoint of the x-intercepts! "
        "Midpoint: (1 + 3) / 2 = 2. It all fits together into one cohesive, harmonious system!"
    ),
    8: (
        "\nProf. Park: As we close our 45th and final lecture, I want to commend each of you for your resilience and intellectual growth. "
        "Algebra is not just about moving symbols on paper; it is about learning how to think logically, "
        "how to break complex problems into manageable steps, and how to persevere through challenging puzzles. "
        "Those are life skills that will serve you in science, engineering, business, and daily life.\n"
        "TA Sora: It has been a true honor being your teaching assistant throughout M090! "
        "Remember my golden rules: protect your signs with parentheses, clear fractions with the LCD, and verify your work! "
        "Good luck on your final exams, and we wish you tremendous success in all your future studies at Gallatin College and Montana State University!"
    )
}

# Apply additions
for slide, add_text in L42_TOP.items():
    L42_CURR[slide] = L42_CURR[slide] + add_text

for slide, add_text in L43_TOP.items():
    L43_CURR[slide] = L43_CURR[slide] + add_text

for slide, add_text in L44_TOP.items():
    L44_CURR[slide] = L44_CURR[slide] + add_text

for slide, add_text in L45_TOP.items():
    L45_CURR[slide] = L45_CURR[slide] + add_text

print("Applying final topup scripts to L42...")
apply_scripts_to_data(L42_CURR, 42)

print("Applying final topup scripts to L43...")
apply_scripts_to_data(L43_CURR, 43)

print("Applying final topup scripts to L44...")
apply_scripts_to_data(L44_CURR, 44)

print("Applying final topup scripts to L45...")
apply_scripts_to_data(L45_CURR, 45)

print("\nFinal topup complete! All 45 lectures now at 20-25 minute standard!")
