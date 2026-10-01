# -*- coding: utf-8 -*-
"""
expand_unit3_l39_l41.py
Expands Lectures 39, 40, and 41 to reach full 20-25 minute length (2,280 - 2,500 words each).
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

L39_CURR = extract_lecture_scripts(39)
L40_CURR = extract_lecture_scripts(40)
L41_CURR = extract_lecture_scripts(41)

L39_ADD = {
    1: (
        "\nProf. Park: When factoring a trinomial with leading coefficient a not equal to 1, like 2x^2 + 7x + 3 = 0, "
        "many students waste time guessing and checking endless combinations. "
        "The ac method eliminates all guesswork: multiply a times c: 2 · 3 = 6. "
        "Now find two numbers that multiply to 6 and add to b = 7: 6 and 1! "
        "Split the middle term: 2x^2 + 6x + 1x + 3 = 0. "
        "Now group: 2x(x + 3) + 1(x + 3) = (2x + 1)(x + 3) = 0! "
        "Setting each factor to zero gives x = -1/2 and x = -3. "
        "The ac method transforms trial-and-error into a deterministic, repeatable algorithm!"
    ),
    2: (
        "\nTA Sora: In Example 6 with g(x) = 3x^2 - 10x - 8, notice that finding the x-intercepts corresponds to finding the roots or zeros of the function. "
        "In projectile physics, such as launching an avalanche control projectile at Bridger Bowl, "
        "if height h(t) = -16t^2 + v0 t + s0, the t-intercepts tell the safety crew exactly when the projectile leaves the launcher and when it impacts the snowpack. "
        "Factoring is how engineers calculate physical impact timing!"
    ),
    3: (
        "\nProf. Park: In Example 7 with -x^2 + 4x + 5 = 0, notice Sora's golden advice: "
        "Whenever a quadratic equation has a negative leading coefficient, multiply both sides of the equation by -1 before factoring! "
        "Multiplying 0 by -1 is still 0, but -x^2 becomes +x^2, +4x becomes -4x, and +5 becomes -5: x^2 - 4x - 5 = 0! "
        "Factoring (x - 5)(x + 1) = 0 gives x = 5 and x = -1. "
        "Notice that while multiplying by -1 reflects the parabola upside down, its x-intercepts remain completely unchanged because zero multiplied by -1 is still zero!"
    ),
    4: (
        "\nTA Sora: On slide 4, when f(x) = x^2 - 6x + 9 = (x - 3)^2 = 0, we get x = 3 with multiplicity 2! "
        "On the graph, this means the parabola does not cross through the x-axis—it kisses the x-axis at the single point (3, 0) and bounces right back up! "
        "Whenever a quadratic has exactly one x-intercept, that intercept is GUARANTEED to be the vertex of the parabola!"
    ),
    5: (
        "\nProf. Park: Visualizing the three geometric cases is crucial: "
        "Case 1: The parabola crosses the axis twice (two distinct real roots). "
        "Case 2: The vertex rests directly on the axis (one repeated real root). "
        "Case 3: The parabola floats entirely above or below the axis (no real roots, two complex roots). "
        "Understanding these geometric configurations allows you to instantly anticipate solution sets."
    ),
    7: (
        "\nTA Sora: In Checkpoint Practice 3x^2 - 12 = 0, always look for a Greatest Common Factor (GCF) first! "
        "Factoring out 3 gives 3(x^2 - 4) = 0. "
        "Now x^2 - 4 is a Difference of Squares from Section 1.4: 3(x - 2)(x + 2) = 0! "
        "The solutions are x = 2 and x = -2. "
        "Factoring out the GCF first keeps your numbers small and prevents complicated quadratic calculations."
    ),
    8: (
        "\nProf. Park: That concludes Section 3.3! You have mastered factoring by GCF, grouping, difference of squares, and the ac method for quadratic equations. "
        "In Lecture 40, we explore what to do when a quadratic CANNOT be factored: Section 3.4: Completing the Square!"
    )
}

L40_ADD = {
    1: (
        "\nProf. Park: Completing the Square is one of the most intellectually beautiful ideas in mathematics. "
        "It was invented over 1,200 years ago by Persian and Arabic astronomers who literally completed geometric physical squares of clay tiles! "
        "If you have an area x^2 + bx, you have a square of side x and two rectangular wings of width b/2. "
        "To make the entire shape into a perfect giant square, you are missing one tiny corner piece! "
        "That missing corner piece measures (b/2) by (b/2), which has area (b/2)^2! "
        "Adding (b/2)^2 physically completes the square!"
    ),
    2: (
        "\nTA Sora: That visual tile explanation is why the formula is (b/2)^2! "
        "You divide the middle coefficient by 2 because the rectangle was cut into two equal wings, "
        "and you square it because the missing corner is a square of side (b/2)! "
        "In Example 1: for x^2 + 8x, half of 8 is 4, and 4 squared is 16! "
        "Add 16, and you get x^2 + 8x + 16 = (x + 4)^2! Instant perfect square binomial!"
    ),
    3: (
        "\nProf. Park: In Example 2: x^2 + 6x = 7. "
        "Notice the constant 7 is already isolated on the right side! "
        "Take half of 6: 3. Square it: 9. "
        "Now add 9 to BOTH sides: x^2 + 6x + 9 = 7 + 9. "
        "The left side factors into (x + 3)^2, and the right side is 16! "
        "Apply the Square Root Property: x + 3 = plus or minus sqrt(16) = plus or minus 4! "
        "x = -3 + 4 = 1, or x = -3 - 4 = -7. "
        "Clean, elegant, and completely justified by geometry!"
    ),
    4: (
        "\nTA Sora: In Example 3: x^2 - 8x - 5 = 0, "
        "we got x = 4 plus or minus sqrt(21). "
        "Notice that 21 is not a perfect square, so sqrt(21) is an irrational number (about 4.58). "
        "That explains why this equation could NEVER be factored with rational integers! "
        "Completing the square broke through the barrier where factoring failed!"
    ),
    5: (
        "\nProf. Park: In Example 4, when a is not 1 (like 2x^2 - 12x + 10 = 0), "
        "our mandatory first step is to divide every single term on both sides by a = 2: "
        "x^2 - 6x + 5 = 0! "
        "Only when the leading coefficient is strictly positive 1 can you apply the (b/2)^2 rule!"
    ),
    6: (
        "\nTA Sora: Notice the huge engineering advantage of completing the square: "
        "It converts general form f(x) = ax^2 + bx + c into VERTEX FORM f(x) = a(x - h)^2 + k! "
        "From vertex form, you can read the peak height and location (h, k) instantly with zero extra calculations! "
        "In satellite dish design and parabolic microphone engineering at MSU, vertex form is the industry standard."
    ),
    8: (
        "\nProf. Park: That concludes Section 3.4! Completing the Square proved that ANY quadratic equation can be solved analytically. "
        "And in fact, if you complete the square on the general formula ax^2 + bx + c = 0, "
        "you derive the most famous formula in algebra: The Quadratic Formula! "
        "We will master that universal master key in Lecture 41!"
    )
}

L41_ADD = {
    1: (
        "\nProf. Park: The Quadratic Formula: x = [ -b plus or minus sqrt(b^2 - 4ac) ] / (2a). "
        "It solves 100% of all quadratic equations in existence—whether the coefficients are integers, fractions, decimals, or square roots! "
        "It is the Swiss Army knife of high school and college algebra. "
        "Whenever an equation resists factoring or completing the square looks tedious, the Quadratic Formula delivers the exact solution every time."
    ),
    2: (
        "\nTA Sora: In Example 1 with g(x) = x^2 - 17x + 72: "
        "Notice the term b^2: (-17)^2 = +289! "
        "A negative number squared is ALWAYS positive! "
        "A fatal student error is typing -17^2 into a calculator without parentheses and getting -289. "
        "Always remember: b squared can NEVER be negative! "
        "Here, 289 - 4(1)(72) = 289 - 288 = 1. "
        "sqrt(1) = 1, giving roots (17 + 1)/2 = 9 and (17 - 1)/2 = 8!"
    ),
    3: (
        "\nProf. Park: In Example 2 with h(x) = x^2 - 5x - 7: "
        "Look at -4ac: -4(1)(-7) = +28! "
        "Because c was negative (-7), the product -4ac became POSITIVE 28! "
        "So inside the radical: 25 + 28 = 53! "
        "x = (5 plus or minus sqrt(53)) / 2. "
        "Always watch the sign of c: a negative c turns -4ac into addition!"
    ),
    4: (
        "\nTA Sora: In Example 3 with h(x) = 13x - x^2 + 1: "
        "Notice the order of terms: 13x is linear, -x^2 is quadratic, and 1 is constant! "
        "Before identifying a, b, and c, you MUST rewrite the equation in standard descending order: -x^2 + 13x + 1 = 0! "
        "Here, a = -1, b = 13, and c = 1. "
        "If a student carelessly grabbed a = 13 from the first term, their entire formula calculation would be completely invalid!"
    ),
    5: (
        "\nProf. Park: In Example 4 with f(x) = -x^2 - 5x + 7: "
        "Look at the denominator: 2a = 2(-1) = -2! "
        "Dividing by a negative denominator means you must distribute the negative sign carefully: "
        "x = [ 5 plus or minus sqrt(53) ] / (-2) = [ -5 plus or minus sqrt(53) ] / 2. "
        "Parentheses around the denominator protect your signs."
    ),
    6: (
        "\nTA Sora: In Example 5 with f(x) = -1 + 2x^2 - 3x: "
        "Standard order gives 2x^2 - 3x - 1 = 0, so a = 2, b = -3, c = -1. "
        "Discriminant: (-3)^2 - 4(2)(-1) = 9 + 8 = 17! "
        "Roots: x = (3 plus or minus sqrt(17)) / 4. "
        "Notice that neither 3 nor sqrt(17) divides evenly by 4, so this expression is already in simplest radical form!"
    ),
    7: (
        "\nProf. Park: On slide 7, evaluating functions: "
        "f(4) = 3(4^2) - 5(4) + 7 = 3(16) - 20 + 7 = 48 - 20 + 7 = 35! "
        "And f(p) = 3p^2 - 5p + 7. "
        "Function notation simply means replacing the input variable x with whatever is inside the parentheses."
    ),
    8: (
        "\nTA Sora: To conclude Lecture 41: "
        "Always write down a, b, and c explicitly in the margin of your test paper before plugging into the formula! "
        "In Lecture 42, we will study the expression inside the radical—the Discriminant b^2 - 4ac—and how it reveals the nature of solutions before you ever solve the equation!"
    )
}

# Apply additions
for slide, add_text in L39_ADD.items():
    L39_CURR[slide] = L39_CURR[slide] + add_text

for slide, add_text in L40_ADD.items():
    L40_CURR[slide] = L40_CURR[slide] + add_text

for slide, add_text in L41_ADD.items():
    L41_CURR[slide] = L41_CURR[slide] + add_text

print("Applying expanded scripts to L39...")
apply_scripts_to_data(L39_CURR, 39)

print("Applying expanded scripts to L40...")
apply_scripts_to_data(L40_CURR, 40)

print("Applying expanded scripts to L41...")
apply_scripts_to_data(L41_CURR, 41)

print("\nUnit 3 Batch A (L39-L41) expansion complete!")
