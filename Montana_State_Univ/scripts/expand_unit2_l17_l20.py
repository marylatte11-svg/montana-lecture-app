# -*- coding: utf-8 -*-
"""
expand_unit2_l17_l20.py
Expands Lectures 17, 18, 19, and 20 to reach full 20-25 minute length (2,280 - 2,500 words each).
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

L17_CURR = extract_lecture_scripts(17)
L18_CURR = extract_lecture_scripts(18)
L19_CURR = extract_lecture_scripts(19)
L20_CURR = extract_lecture_scripts(20)

L17_ADD = {
    1: (
        "\nProf. Park: Think of parent functions as the fundamental DNA strands of mathematical physics. "
        "Just as all musical melodies in an orchestra are built from combinations of basic pure frequencies, "
        "all advanced curves in science and engineering—from the trajectory of an avalanche control mortar at Bridger Bowl "
        "to the resonant frequency of an optical laser cavity at Montana State University—are simple transformations of these seven basic parent graphs!"
    ),
    3: (
        "\nTA Sora: For y = x, notice that the slope is 1 and the y-intercept is (0, 0). "
        "It forms a perfect 45-degree diagonal through the origin! "
        "In laser optics calibration in Bozeman's photonics labs, y = x represents the ideal 1:1 input-output fidelity transfer line. "
        "Any deviation from y = x indicates sensor distortion or signal loss!"
    ),
    5: (
        "\nTA Sora: Look at the square root curve y = sqrt(x): the domain is [0, infinity) and the range is [0, infinity)! "
        "Why can't x be negative? Because taking the square root of a negative number produces an imaginary number, not a real point on our Cartesian plane! "
        "In Montana highway safety physics, emergency stopping distance on snowy roads scales with the square of speed: d = k v^2, "
        "so estimated vehicle speed from skid marks is v = sqrt(d / k). Because distance and speed are physically positive, the square root parent curve models real-world traffic reconstruction!"
    ),
    7: (
        "\nProf. Park: Notice the inflection point of the cubic curve y = x^3 right at the origin (0, 0): "
        "The graph is flat right at zero, but then accelerates rapidly upward for positive x and downward for negative x. "
        "Civil engineers use cubic polynomial splines to design highway transition spirals on Interstate 90 through Bozeman Pass "
        "so that cars experience smooth, gradual centrifugal acceleration rather than an abrupt jerk into mountain curves!"
    ),
    8: (
        "\nTA Sora: Contrast the cube root y = cbrt(x) with the square root y = sqrt(x): "
        "For square roots, negatives are forbidden. But for cube roots, the domain is ALL REAL NUMBERS (-infinity, infinity)! "
        "Why? Because (-2)^3 = -8, which means cbrt(-8) = -2! "
        "Odd roots preserve negative signs, while even roots demand non-negative inputs. Always remember that fundamental distinction!"
    ),
    9: (
        "\nProf. Park: That concludes our grand overview of parent functions in Section 2.0! "
        "Mastering these shapes and their interval domains gives you an intuitive mental map for every graph you will encounter in higher algebra. "
        "In Lecture 18, we begin Section 2.1: Linear Equations in Two Variables!"
    )
}

L18_ADD = {
    1: (
        "\nProf. Park: In the Gallatin Valley, agricultural economists and civil engineers constantly use linear equations in two variables. "
        "For example, a rancher balancing cattle grazing acreage x and winter hay production acreage y subject to water rights constraints "
        "expresses their production boundary as a standard linear equation: Ax + By = C. "
        "Every single point (x, y) along that line represents a balanced operational allocation!"
    ),
    3: (
        "\nTA Sora: Notice why solving for y—converting to y = mx + b—is such an incredible advantage: "
        "When an equation is in standard form 2x + 3y = 6, picking random values of x often gives awkward fractions for y. "
        "But once you solve for y to get y = -(2/3)x + 2, you immediately see the denominator is 3! "
        "That tells you: pick multiples of 3 for x (like x = -3, 0, 3, 6), and all your y-values will be clean, beautiful whole integers! "
        "Solving for y lets you choose smart input values that avoid fraction headaches entirely!"
    ),
    4: (
        "\nProf. Park: Why do we always calculate THREE points instead of just two? "
        "Euclid's first postulate tells us that two points determine a unique straight line. "
        "However, if you make a simple arithmetic mistake on one of those two points, you will still draw a perfectly straight line—it will just be completely WRONG! "
        "The third point serves as your mathematical safety checkpoint: if all three points do not line up in a perfect collinear line with your ruler, "
        "you know immediately that one of your calculations contains an error before turning in your exam!"
    ),
    5: (
        "\nTA Sora: In Example 2A: y = (1/4)x - 6. "
        "Look at the slope: m = 1/4. "
        "That means: Rise 1 unit vertically, and Run 4 units horizontally to the right! "
        "And the y-intercept is (0, -6). "
        "Always write the y-intercept as an ORDERED PAIR: (0, -6)! "
        "If a student just writes '-6', strict professors will deduct points because an intercept is a location on the Cartesian coordinate plane!"
    ),
    6: (
        "\nProf. Park: In Example 2B: 2x - y = 7, "
        "watch that negative coefficient on y: -y = -2x + 7. "
        "To isolate y, divide every term by -1: y = 2x - 7. "
        "Here, the slope is m = 2 (or 2/1: rise 2, run 1), and the y-intercept is (0, -7). "
        "Handling that negative sign with precision makes all the difference."
    ),
    7: (
        "\nTA Sora: Here is the Golden Key to intercepts: "
        "To find where a graph crosses the x-axis (the x-intercept), the height MUST be zero: set y = 0! "
        "To find where a graph crosses the y-axis (the y-intercept), the horizontal position MUST be zero: set x = 0! "
        "Setting one variable to zero wipes out that entire term, leaving a one-step equation!"
    ),
    8: (
        "\nProf. Park: In Example 3A: 5x + 2y = 6. "
        "When y = 0: 5x = 6, so x = 6/5 = 1.2. The x-intercept is (6/5, 0). "
        "When x = 0: 2y = 6, so y = 3. The y-intercept is (0, 3). "
        "Plot those two intercepts, connect them with a ruler, and your line is complete! "
        "In Lecture 19, we will explore special horizontal and vertical lines and the famous HOY VUX rule!"
    )
}

L19_ADD = {
    1: (
        "\nTA Sora: In Example 3B: 4x - 5y = 10. "
        "Let's find the intercepts: "
        "Set y = 0: 4x = 10 -> x = 10/4 = 5/2 = 2.5. So the x-intercept is (5/2, 0). "
        "Set x = 0: -5y = 10 -> y = 10 / -5 = -2. So the y-intercept is (0, -2)! "
        "Notice how quickly the intercept method works when an equation is in standard form Ax + By = C: "
        "You simply cover up one term with your thumb and solve for the other in your head! That is why it's often called the 'Cover-Up Method!'"
    ),
    2: (
        "\nProf. Park: In Example 3C: y = -(3/2)x - 3. "
        "Notice the slope is negative: -3/2. That means as you move from left to right, the line goes DOWNHILL! "
        "Like skiing down the slopes at Bridger Bowl or Big Sky, negative slope always moves downward. "
        "The y-intercept is (0, -3), and the x-intercept is found by setting y = 0: 0 = -(3/2)x - 3 -> (3/2)x = -3 -> x = -2: (-2, 0)."
    ),
    3: (
        "\nTA Sora: In Example 3D: y = 2x. "
        "Watch what happens with the intercept method here: "
        "If you set x = 0, y = 2(0) = 0, giving the origin (0, 0). "
        "If you set y = 0, 0 = 2x -> x = 0, giving the origin (0, 0) AGAIN! "
        "The x-intercept and y-intercept are the EXACT SAME POINT! "
        "Because you cannot draw a line with only one point, the intercept method fails here! "
        "Whenever a line passes through the origin (y = kx, direct variation), you MUST pick a second independent point, such as x = 1 -> y = 2: (1, 2)!"
    ),
    4: (
        "\nProf. Park: Now let's explore horizontal lines: Example 3E: y = -2. "
        "Notice there is NO x in this equation! "
        "That means x can be absolutely ANY real number in the universe: x = -10, x = 0, x = 500. "
        "No matter what x is, y is locked at -2! "
        "Points include (-3, -2), (0, -2), (4, -2). "
        "Connecting them gives a perfectly flat, horizontal line! "
        "What is the slope of a flat line? Zero! m = 0. "
        "Think of cross-country skiing on a frozen flat lake in Yellowstone: zero incline, zero effort, slope = 0!"
    ),
    5: (
        "\nTA Sora: Now compare that with a vertical line: Example 3F: x = 3. "
        "Here, there is NO y in the equation! "
        "That means y can be anything: (3, -5), (3, 0), (3, 4). "
        "Connecting them gives a completely vertical line! "
        "What is the slope of a vertical line? "
        "If you try to calculate slope: m = (4 - 0) / (3 - 3) = 4 / 0! "
        "Division by zero is strictly UNDEFINED! "
        "Think of skiing: could you ski a vertical 90-degree cliff wall at the top of the Bridger Ridge? "
        "No! That is not a ski slope—you would fall into freefall! A vertical line has NO slope; its slope is UNDEFINED!"
    ),
    6: (
        "\nProf. Park: Let's cement the famous 'HOY VUX' memory rule: "
        "H - O - Y: Horizontal lines have Zero (0) slope, and their equation is Y = [constant number]! "
        "V - U - X: Vertical lines have Undefined slope, and their equation is X = [constant number]! "
        "Write HOY VUX on the front cover of your course notebook! It guarantees you will never confuse horizontal and vertical lines on an exam."
    ),
    7: (
        "\nTA Sora: When you graph y = -2 and x = 3 on the same coordinate plane, "
        "the horizontal line and vertical line cross at a crisp 90-degree right angle at the coordinate point (3, -2)! "
        "In Cartesian geometry, horizontal and vertical lines are always perpendicular to each other."
    ),
    8: (
        "\nProf. Park: That brings us to the end of Section 2.1! "
        "You now have three powerful tools for graphing linear equations: "
        "1. The Table Method (pick smart x-values). "
        "2. The Intercept Method (set x=0, set y=0; best for Ax + By = C). "
        "3. The HOY VUX rule for horizontal (y=b) and vertical (x=a) lines. "
        "In Lecture 20, we will dive deep into the numerical calculation of slope!"
    )
}

L20_ADD = {
    1: (
        "\nProf. Park: In the Rocky Mountains of Montana, slope is not an abstract formula—it is a physical reality that dictates highway design and avalanche safety. "
        "The Montana Department of Transportation posts yellow warning signs on Interstate 90 over Bozeman Pass: '6% Grade Next 5 Miles.' "
        "What does a 6% grade mean in algebra? "
        "It means a slope of m = 6 / 100 = 3 / 50: for every 100 feet of horizontal run, the highway rises or drops 6 vertical feet! "
        "Slope is the universal measure of steepness and rate of change."
    ),
    2: (
        "\nTA Sora: In Example 1A, finding the slope between (2, 3) and (5, 7): "
        "m = (7 - 3) / (5 - 2) = 4 / 3. "
        "Notice what happens if you reverse the points: "
        "m = (3 - 7) / (2 - 5) = -4 / -3 = +4/3! "
        "You get the exact same answer! "
        "It does not matter which point you designate as Point 1 and which as Point 2, "
        "as long as you stay consistent: if you start with the y-value of the second point upstairs, you MUST start with the x-value of the second point downstairs!"
    ),
    3: (
        "\nProf. Park: In Example 1B, between (3, -4) and (-2, -8): "
        "Look at the double negative upstairs: y2 - y1 = -8 - (-4) = -8 + 4 = -4. "
        "And downstairs: x2 - x1 = -2 - 3 = -5. "
        "Then -4 / -5 = +4/5! "
        "That is where Sora's protective parentheses pay off: wrapping negative coordinates in parentheses prevents accidental addition errors!"
    ),
    4: (
        "\nTA Sora: Look at Example 1C between (3, 7) and (3, -10): "
        "Notice the x-coordinates: both are 3! "
        "Downstairs we get: 3 - 3 = 0. "
        "m = -17 / 0 = UNDEFINED! "
        "Whenever two points share the exact same x-coordinate, the line connecting them is VERTICAL (VUX: x = 3), and the slope is UNDEFINED!"
    ),
    5: (
        "\nProf. Park: And compare that with Example 1D between (-2, -5) and (3, -5): "
        "Notice the y-coordinates: both are -5! "
        "Upstairs we get: -5 - (-5) = -5 + 5 = 0. "
        "m = 0 / 5 = 0! "
        "Whenever two points share the exact same y-coordinate, the line is HORIZONTAL (HOY: y = -5), and the slope is exactly ZERO!"
    ),
    6: (
        "\nTA Sora: In Example 1E with fraction coordinates, always multiply numerator and denominator by the common denominator to clear inner fractions. "
        "Never fear fractions—treat them with our clear-by-LCD strategy from Lecture 13!"
    ),
    7: (
        "\nProf. Park: In Example 2A, counting slope from a graph: "
        "Start at the lower point, count up (rise), then count right (run). "
        "Drawing a right-triangle on your graph paper makes finding slope completely visual and intuitive."
    ),
    8: (
        "\nTA Sora: In Example 2B, when counting a negative slope: "
        "If you count down, rise is negative: -3. Run is positive: +4. "
        "m = -3/4. Always verify that a downhill line gets a negative sign!"
    ),
    9: (
        "\nProf. Park: To summarize Section 2.2 Part 1: "
        "1. Uphill lines have POSITIVE slope (m > 0). "
        "2. Downhill lines have NEGATIVE slope (m < 0). "
        "3. Flat horizontal lines have ZERO slope (m = 0). "
        "4. Straight vertical lines have UNDEFINED slope (m = undefined). "
        "In Lecture 21, we will explore parallel and perpendicular line slopes!"
    )
}

# Apply additions
for slide, add_text in L17_ADD.items():
    L17_CURR[slide] = L17_CURR[slide] + add_text

for slide, add_text in L18_ADD.items():
    L18_CURR[slide] = L18_CURR[slide] + add_text

for slide, add_text in L19_ADD.items():
    L19_CURR[slide] = L19_CURR[slide] + add_text

for slide, add_text in L20_ADD.items():
    L20_CURR[slide] = L20_CURR[slide] + add_text

print("Applying expanded scripts to L17...")
apply_scripts_to_data(L17_CURR, 17)

print("Applying expanded scripts to L18...")
apply_scripts_to_data(L18_CURR, 18)

print("Applying expanded scripts to L19...")
apply_scripts_to_data(L19_CURR, 19)

print("Applying expanded scripts to L20...")
apply_scripts_to_data(L20_CURR, 20)

print("\nUnit 2 expansion (L17-L20) complete!")
