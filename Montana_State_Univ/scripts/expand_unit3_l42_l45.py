# -*- coding: utf-8 -*-
"""
expand_unit3_l42_l45.py
Expands Lectures 42, 43, 44, and 45 to reach full 20-25 minute length (2,280 - 2,550 words each).
This completes the entire 45-lecture M090 curriculum!
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

L42_ADD = {
    1: (
        "\nProf. Park: In scientific computing and engineering simulations at Montana State University, calculating full roots of quadratic systems is often computationally expensive. "
        "Engineers designing radar detection systems or structural truss stability checks first compute the DISCRIMINANT: Delta = b^2 - 4ac. "
        "In one single arithmetic step, the discriminant reveals the structural fate of the system: "
        "Will the beams cross? Will the laser beam focus on the target? Will the vehicle skid or stop? "
        "The sign of Delta is a diagnostic crystal ball that answers these questions instantly!"
    ),
    2: (
        "\nTA Sora: In Case 1 when Delta > 0, the number inside the square root is strictly positive, like Delta = 9 in f(x) = x^2 - 5x + 4. "
        "Because sqrt(9) = 3, the plus-or-minus operator creates TWO distinct real solutions: x = (5 + 3)/2 = 4, and x = (5 - 3)/2 = 1. "
        "On the graph, the parabola plunges down through the x-axis at (1, 0), reaches its vertex at (2.5, -2.25), and climbs back up through (4, 0). "
        "It acts like a secant line cutting through the axis in two distinct places!"
    ),
    3: (
        "\nProf. Park: In Case 2 when Delta = 0, look at what happens in the formula: plus or minus sqrt(0) = plus or minus 0! "
        "Adding zero and subtracting zero gives the EXACT same number: x = -b / (2a)! "
        "In f(x) = x^2 - 6x + 9, Delta = (-6)^2 - 4(1)(9) = 36 - 36 = 0! "
        "The only root is x = 6/2 = 3. "
        "Notice that x = -b / (2a) is the exact formula for the x-coordinate of the VERTEX! "
        "That proves mathematically that when Delta = 0, the vertex of the parabola rests directly on the x-axis!"
    ),
    4: (
        "\nTA Sora: In Case 3 when Delta < 0, like Delta = -16 in f(x) = x^2 + 2x + 5: "
        "Inside the square root, we have sqrt(-16). In real numbers, sqrt(-16) is NOT a real number! "
        "That means there are ZERO real x-intercepts. "
        "On the graph, the vertex is at (-1, 4), and since a = 1 > 0, the parabola opens upward! "
        "It floats completely in the upper half-plane and never touches the x-axis. "
        "In physics, this represents an object that never reaches the ground, like a projectile that explodes in mid-air!"
    ),
    5: (
        "\nProf. Park: In slide 5 with h(x) = -2x^2 + 3x - 5, we are asked to classify the intercepts WITHOUT solving the equation! "
        "This is a classic high-value exam question. "
        "Compute Delta = b^2 - 4ac: a = -2, b = 3, c = -5. "
        "Delta = 3^2 - 4(-2)(-5) = 9 - 40 = -31. "
        "Because -31 is negative, we immediately state: ZERO real x-intercepts (the parabola opens downward with vertex below the axis)! "
        "We answered the question in thirty seconds without ever touching the quadratic formula."
    ),
    6: (
        "\nTA Sora: On slide 6, function notation review: "
        "Remember that f(input) means: wherever you see x, open a set of empty parentheses and place the input inside! "
        "For f(4): 3(4)^2 - 5(4) + 7 = 3(16) - 20 + 7 = 48 - 20 + 7 = 35. "
        "For f(p): 3(p)^2 - 5(p) + 7 = 3p^2 - 5p + 7. "
        "Treating function evaluation as a mechanical substitution protocol prevents sign errors."
    ),
    7: (
        "\nProf. Park: On slide 7, look at Part C: f(x + 3): "
        "f(x + 3) = 3(x + 3)^2 - 5(x + 3) + 7. "
        "Remember Section 1.4: (x + 3)^2 = x^2 + 6x + 9! Do NOT forget the middle term 6x! "
        "Then 3(x^2 + 6x + 9) = 3x^2 + 18x + 27. "
        "Distribute -5: -5x - 15. "
        "Combine: 3x^2 + 13x + 19! "
        "And in Part D, solving f(x) = 7 means setting the OUTPUT to 7: 3x^2 - 5x + 7 = 7 -> 3x^2 - 5x = 0 -> x(3x - 5) = 0 -> x = 0, 5/3!"
    ),
    8: (
        "\nTA Sora: To summarize Section 3.5 Part 2: "
        "The Discriminant Delta = b^2 - 4ac is your navigational compass for quadratic equations: "
        "Delta > 0: 2 real x-intercepts. "
        "Delta = 0: 1 real x-intercept (tangent vertex). "
        "Delta < 0: 0 real x-intercepts (floating parabola). "
        "In Lecture 43, we compare all four intercept methods side-by-side!"
    )
}

L43_ADD = {
    1: (
        "\nProf. Park: In Lecture 43, we address the most common question students ask right before Final Exams: "
        "'Professor Park, how do I know WHICH method to use on a quadratic problem?' "
        "On an exam, problems are mixed up. Nobody tells you: 'Use factoring here' or 'Use the formula here.' "
        "You must be the mathematical doctor who diagnoses the equation and selects the most efficient surgical tool! "
        "Using the wrong tool—like using the quadratic formula on an equation that factors in two seconds—wastes precious exam time."
    ),
    2: (
        "\nTA Sora: Look at Method 1 on slide 2: g(x) = x^2 + 6x = 0. "
        "Notice what is MISSING: there is NO constant term c! c = 0. "
        "Whenever the constant term is zero, NEVER use the quadratic formula! "
        "Simply factor out the common factor x: x(x + 6) = 0! "
        "Immediately: x = 0 or x = -6. "
        "Solved in five seconds flat! If you used the formula, you would be calculating 6^2 - 4(1)(0) across half a page. "
        "Always look for a GCF first!"
    ),
    3: (
        "\nProf. Park: Now look at Method 2 on slide 3: h(x) = -2x^2 + 5x + 6 = 0. "
        "Here, a = -2, b = 5, c = 6. "
        "a · c = -2 · 6 = -12. Factors of -12 that add to 5? "
        "Let's check: 1 and -12 (sum -11), 2 and -6 (sum -4), 3 and -4 (sum -1). None of them add to 5! "
        "The equation CANNOT be factored! "
        "Once you confirm it doesn't factor, immediately deploy the Quadratic Formula: "
        "x = [ -5 plus or minus sqrt(25 - 4(-2)(6)) ] / (-4) = [ -5 plus or minus sqrt(73) ] / (-4). "
        "When factoring fails, the Quadratic Formula is your unstoppable backup!"
    ),
    4: (
        "\nTA Sora: Method 3 on slide 4: f(x) = 4x^2 - 28 = 0. "
        "Notice what is MISSING here: there is NO linear term bx! b = 0! "
        "Whenever the middle linear term is missing, use the Square Root Property: "
        "Isolate x^2: 4x^2 = 28 -> x^2 = 7! "
        "Take the square root of both sides: x = plus or minus sqrt(7)! "
        "Never use the quadratic formula when b = 0—the square root property is five times faster!"
    ),
    5: (
        "\nProf. Park: Method 4 on slide 5: f(x) = x^2 - 15x + 50 = 0. "
        "Here a = 1, and the numbers are friendly: what factors of 50 add to -15? "
        "-10 and -5! (-10)(-5) = +50, and -10 + -5 = -15. "
        "(x - 10)(x - 5) = 0 -> x = 10, x = 5. "
        "When a = 1 and factors are obvious, factoring is king!"
    ),
    6: (
        "\nTA Sora: On slide 6, look at vertex form: f(x) = -2(x - 15)^2 + 50. "
        "To find the x-intercepts, set f(x) = 0: -2(x - 15)^2 + 50 = 0. "
        "Subtract 50: -2(x - 15)^2 = -50. "
        "Divide by -2: (x - 15)^2 = 25! "
        "Square root property: x - 15 = plus or minus 5! "
        "x = 15 + 5 = 20, or x = 15 - 5 = 10! "
        "Notice we did NOT multiply out (x - 15)^2! We used the square root property directly on the vertex form!"
    ),
    7: (
        "\nProf. Park: Study our summary decision chart on slide 7: "
        "1. No constant (c = 0): Factor GCF x. "
        "2. No middle term (b = 0): Square Root Property. "
        "3. Nice trinomial: Factor (ac method). "
        "4. Vertex form: Square Root Property. "
        "5. Ugly trinomial or non-factoring: Quadratic Formula! "
        "Following this decision hierarchy guarantees maximum efficiency and speed on your exams."
    ),
    8: (
        "\nTA Sora: That concludes Section 3.6! In Lecture 44, we synthesize everything we have learned into Section 3.7: Graphing Quadratic Functions with the complete 5-Point Method!"
    )
}

L44_ADD = {
    1: (
        "\nProf. Park: Welcome to Lecture 44! In Section 3.7, we master the complete 5-Point Graphing Protocol for quadratic functions. "
        "Just as architects in Bozeman draw detailed blueprint elevations before breaking ground on custom homes, "
        "a mathematician uses five critical anchor points to sketch a flawless parabola: "
        "Point 1: The Vertex (the turning peak or valley: x = -b/(2a), y = f(-b/(2a))). "
        "Point 2: The Axis of Symmetry (the vertical mirror line x = -b/(2a)). "
        "Point 3: The y-intercept (0, c) and its symmetric mirror reflection across the axis of symmetry. "
        "Points 4 and 5: The two x-intercepts (the real roots where the curve meets the ground)."
    ),
    2: (
        "\nTA Sora: In slide 2, graphing g(x) = x^2 + 6x + 5: "
        "Step 1: a = 1 > 0, so the parabola opens UPWARD like a cup! "
        "Step 2: Vertex x = -6 / (2 · 1) = -3. "
        "Plug in x = -3: g(-3) = (-3)^2 + 6(-3) + 5 = 9 - 18 + 5 = -4. Vertex is (-3, -4)! "
        "Step 3: Axis of symmetry is the vertical line x = -3. "
        "Step 4: y-intercept is (0, 5). Its reflection across x = -3 is (-6, 5)! "
        "Step 5: x-intercepts: (x + 5)(x + 1) = 0 -> (-5, 0) and (-1, 0). "
        "Plot all five points: (-6, 5), (-5, 0), (-3, -4), (-1, 0), (0, 5), and sketch the smooth U-curve!"
    ),
    3: (
        "\nProf. Park: In slide 3, graphing h(x) = -2x^2 + 4x + 6: "
        "Notice a = -2 < 0, so the parabola opens DOWNWARD like an umbrella! "
        "Vertex x = -4 / (2 · -2) = -4 / -4 = +1. "
        "Plug in x = 1: h(1) = -2(1)^2 + 4(1) + 6 = -2 + 4 + 6 = +8. Vertex is (1, 8)! "
        "Because it opens downward, the vertex (1, 8) is the absolute MAXIMUM point of the function! "
        "y-intercept is (0, 6). Its symmetric partner is (2, 6). "
        "x-intercepts: -2(x^2 - 2x - 3) = -2(x - 3)(x + 1) = 0 -> (3, 0) and (-1, 0). "
        "Connect the five points in a graceful arched curve."
    ),
    4: (
        "\nTA Sora: In slide 4, graphing g(x) = 2x^2 - 8x: "
        "Here c = 0, so the y-intercept is the ORIGIN (0, 0)! "
        "Vertex: x = -(-8) / (2 · 2) = 8 / 4 = 2. "
        "g(2) = 2(2^2) - 8(2) = 8 - 16 = -8. Vertex is (2, -8). "
        "x-intercepts: 2x(x - 4) = 0 -> (0, 0) and (4, 0). "
        "Notice the symmetry: the vertex at x = 2 sits exactly halfway between the intercepts x = 0 and x = 4!"
    ),
    5: (
        "\nProf. Park: In slide 5, graphing from vertex form: f(x) = -(1/2)(x + 1)^2 + 8: "
        "Compare with f(x) = a(x - h)^2 + k: "
        "h = -1, k = 8, so the vertex is immediately (-1, 8)! "
        "a = -1/2 means the parabola opens downward and is vertically compressed (wider than standard). "
        "When x = 0: f(0) = -(1/2)(1)^2 + 8 = 7.5: (0, 7.5). "
        "Finding x-intercepts: -(1/2)(x + 1)^2 + 8 = 0 -> (x + 1)^2 = 16 -> x + 1 = plus or minus 4 -> x = 3, -5!"
    ),
    6: (
        "\nTA Sora: On slide 6, evaluating two simultaneous functions: f(x) = x^2 - 6x + 4 and g(x) = -2x + 25. "
        "For f(-7): (-7)^2 - 6(-7) + 4 = 49 + 42 + 4 = 95. "
        "For g(-7): -2(-7) + 25 = 14 + 25 = 39. "
        "Notice f(x) is quadratic and grows much faster than linear function g(x)!"
    ),
    7: (
        "\nProf. Park: On slide 7, function composition with binomials: "
        "f(x + 5) = (x + 5)^2 - 6(x + 5) + 4 = x^2 + 10x + 25 - 6x - 30 + 4 = x^2 + 4x - 1. "
        "And g(x + 5) = -2(x + 5) + 25 = -2x - 10 + 25 = -2x + 15. "
        "This combines Section 1.4 polynomial expansion with function notation."
    ),
    8: (
        "\nTA Sora: On slide 8, finding where the parabola f(x) and line g(x) intersect: "
        "Set them equal: x^2 - 6x + 4 = -2x + 25! "
        "Add 2x: x^2 - 4x + 4 = 25. "
        "Subtract 25: x^2 - 4x - 21 = 0! "
        "Factor: (x - 7)(x + 3) = 0 -> x = 7, x = -3! "
        "Plugging into g(x): g(7) = -2(7) + 25 = 11: (7, 11). "
        "g(-3) = -2(-3) + 25 = 31: (-3, 31). "
        "The line cuts through the parabola at two distinct points! "
        "In Lecture 45, we conduct our Grand Finale Course Review!"
    )
}

L45_ADD = {
    1: (
        "\nProf. Park: Welcome everyone to Lecture 45—the final lecture of M090 Introductory Algebra! "
        "I am Professor Eunju Park, and joining me at the teaching desk for our grand course conclusion is TA Sora. "
        "Today is a triumphant milestone: we review the complete domain and range of quadratic functions, "
        "execute our master 5-point graphing method on a full-scale problem, analyze parabola-line linear systems, "
        "assemble your permanent Unit 3 Formula Card, and celebrate everything you have achieved across the entire semester!"
    ),
    2: (
        "\nTA Sora: Let's master Domain and Range for quadratic functions once and for all: "
        "For ANY quadratic function f(x) = ax^2 + bx + c, the DOMAIN is ALWAYS all real numbers: (-infinity, infinity)! "
        "You can square any number in the universe—positive, negative, zero, or fraction—with zero mathematical restriction. "
        "The RANGE, however, is bounded by the VERTEX (h, k): "
        "If a > 0 (opens upward), the vertex is the absolute bottom valley: Range is [k, infinity)! "
        "If a < 0 (opens downward), the vertex is the absolute mountain peak: Range is (-infinity, k]! "
        "Always use a square bracket [ ] at the vertex y-coordinate k because that peak or valley point IS physically achieved by the graph!"
    ),
    3: (
        "\nProf. Park: On slide 3, let's execute the full 5-Point Graphing Method on p(x) = x^2 - 4x - 5: "
        "1. a = 1 > 0: opens upward. "
        "2. Vertex x = -(-4) / (2 · 1) = 4 / 2 = 2. "
        "p(2) = 2^2 - 4(2) - 5 = 4 - 8 - 5 = -9. Vertex is (2, -9)! "
        "3. Axis of symmetry: x = 2. "
        "4. y-intercept: (0, -5). Its reflection across x = 2 is (4, -5)! "
        "5. x-intercepts: (x - 5)(x + 1) = 0 -> (5, 0) and (-1, 0). "
        "Look at our five points: (-1, 0), (0, -5), (2, -9), (4, -5), (5, 0). "
        "They form a gorgeously symmetric parabola with domain (-infinity, infinity) and range [-9, infinity)!"
    ),
    4: (
        "\nTA Sora: On slide 4, visualizing the intersection of f(x) = x^2 - 6x + 4 and g(x) = -2x + 25: "
        "A line and a parabola can interact in three distinct geometric ways: "
        "They can miss each other entirely (0 intersection points, Delta < 0). "
        "The line can graze the parabola tangentially (1 intersection point, Delta = 0). "
        "Or the line can cut through both branches (2 intersection points, Delta > 0). "
        "Here, our system had Delta = (-4)^2 - 4(1)(-21) = 16 + 84 = 100 > 0, producing two real intersection coordinates: (-3, 31) and (7, 11)!"
    ),
    5: (
        "\nProf. Park: Look at our Unit 3 Grand Review table on slide 5: "
        "In Section 3.0, we explored the geometry of parabolas. "
        "In Section 3.1 and 3.2, we mastered the Vertex Formula x = -b/(2a) and standard form. "
        "In Section 3.3, we solved equations and found intercepts by Factoring. "
        "In Section 3.4, we completed the square and built vertex form. "
        "In Section 3.5, we mastered the Quadratic Formula and the Discriminant. "
        "In Section 3.6, we learned how to choose the best method for any problem. "
        "And in Section 3.7, we mastered full 5-point graphing and system intersections!"
    ),
    6: (
        "\nTA Sora: Keep this Formula Card on slide 6 forever! "
        "1. Standard Form: f(x) = ax^2 + bx + c. "
        "2. Vertex: x = -b / (2a), y = f(-b / (2a)). "
        "3. Vertex Form: f(x) = a(x - h)^2 + k with vertex (h, k). "
        "4. Quadratic Formula: x = [ -b plus or minus sqrt(b^2 - 4ac) ] / (2a). "
        "5. Discriminant: Delta = b^2 - 4ac (positive: 2 roots, zero: 1 root, negative: 0 real roots). "
        "These five formulas are the permanent foundation for all college algebra, precalculus, and calculus!"
    ),
    7: (
        "\nProf. Park: In Challenge Problem q(x) = -3x^2 + 12x - 9: "
        "a = -3 (opens down). "
        "Vertex x = -12 / (2 · -3) = -12 / -6 = 2. "
        "q(2) = -3(4) + 12(2) - 9 = -12 + 24 - 9 = +3. Vertex is (2, 3)! "
        "Factor: -3(x^2 - 4x + 3) = -3(x - 3)(x - 1) = 0 -> intercepts (1, 0) and (3, 0). "
        "y-intercept: (0, -9). Symmetric point: (4, -9). "
        "Domain: (-infinity, infinity). Range: (-infinity, 3]! "
        "Complete, elegant, and fully verified."
    ),
    8: (
        "\nTA Sora: Congratulations to every single student who has traveled this journey with Professor Park and me! "
        "Think back to where we started in Lecture 01: working with simple fractions and number lines. "
        "From arithmetic to linear equations, literal formulas, inequalities, Cartesian coordinates, slope, parent functions, "
        "polynomials, rational expressions, and full quadratic theory—you have conquered 45 lectures of rigorous college mathematics! "
        "You have built problem-solving stamina, algebraic precision, and intellectual confidence that will serve you throughout your academic and professional career.\n"
        "Prof. Park: On behalf of Gallatin College Montana State University and the Department of Mathematical Sciences, "
        "I want to thank you for your extraordinary dedication and hard work. "
        "Walk into your final exam with your head held high—you are fully prepared, you have mastered the material, and you are ready to succeed. "
        "Thank you everyone, and congratulations on completing M090 Introductory Algebra!"
    )
}

# Apply additions
for slide, add_text in L42_ADD.items():
    L42_CURR[slide] = L42_CURR[slide] + add_text

for slide, add_text in L43_ADD.items():
    L43_CURR[slide] = L43_CURR[slide] + add_text

for slide, add_text in L44_ADD.items():
    L44_CURR[slide] = L44_CURR[slide] + add_text

for slide, add_text in L45_ADD.items():
    L45_CURR[slide] = L45_CURR[slide] + add_text

print("Applying expanded scripts to L42...")
apply_scripts_to_data(L42_CURR, 42)

print("Applying expanded scripts to L43...")
apply_scripts_to_data(L43_CURR, 43)

print("Applying expanded scripts to L44...")
apply_scripts_to_data(L44_CURR, 44)

print("Applying expanded scripts to L45...")
apply_scripts_to_data(L45_CURR, 45)

print("\nUnit 3 Batch B (L42-L45) expansion complete!")
