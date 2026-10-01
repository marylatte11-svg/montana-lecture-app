# Montana State University - M090 Introductory Algebra
# Expanded Unit 2 Generator (Lectures 16 - 30)
# 100% faithful to M090 Full Student Workbook pp. 29-56
# Every graphing problem includes a dedicated Cartesian Coordinate Grid (`graph` object)!

import json
import re

print("Building Expanded Unit 2 Slides with Cartesian Coordinate Grids...")

# Define lectures data
lectures = {}

# L16: Section 2.0 Part 1 (Workbook p. 30) - 10 slides
lectures[16] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept & Cartesian Grid",
        "title": "The Rectangular (Cartesian) Coordinate System",
        "subtitle": "Unit 2 • Lecture 16 • Section 2.0 (Workbook p. 30)",
        "detail": "Lecture 16: The Cartesian Plane & Plotting Points",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### The Rectangular (Cartesian) Coordinate Plane (Workbook p. 30)\n- **Axes:** The horizontal line is the **$x$-axis**, and the vertical line is the **$y$-axis**.\n- **Origin:** The intersection of the two axes at $(0, 0)$.\n- **Quadrants:** The axes divide the plane into four quadrants:\n  - **Quadrant I:** $(+, +)$\n  - **Quadrant II:** $(-, +)$\n  - **Quadrant III:** $(- , -)$\n  - **Quadrant IV:** $(+, -)$\n- **Ordered Pair:** $(x, y)$ where $x$ is horizontal position and $y$ is vertical position.",
        "solution": "$$\\begin{aligned}\n\\text{Origin: } & (0, 0) \\\\\n\\text{Quadrant I: } & x > 0, y > 0 \\quad (+, +) \\\\\n\\text{Quadrant II: } & x < 0, y > 0 \\quad (-, +) \\\\\n\\text{Quadrant III: } & x < 0, y < 0 \\quad (-, -) \\\\\n\\text{Quadrant IV: } & x > 0, y < 0 \\quad (+, -)\n\\end{aligned}$$",
        "pitfall": "**Ordered Pair Sequence:** Always move horizontally along the $x$-axis first, then vertically along the $y$-axis! $(x, y) \\neq (y, x)$.",
        "script": "[Prof. Park] Welcome to Unit 2 of M090! Today we step into the visual world of mathematics: the Cartesian Coordinate Plane.\n\n[TA Sora] Named after René Descartes! Remember the order: $x$ comes first alphabetically, so you walk along the hallway ($x$-axis) before taking the elevator ($y$-axis)!\n\n[Prof. Park] Look at the four quadrants labeled on your screen. Notice how they run counterclockwise starting from the top-right!",
        "graph": {
            "xMin": -8, "xMax": 8, "yMin": -8, "yMax": 8,
            "title": "Cartesian Coordinate Plane: Quadrants & Axes",
            "points": [{"x": 0, "y": 0, "label": "Origin (0,0)", "color": "#38bdf8", "labelOffsetX": 8, "labelOffsetY": 14}]
        }
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.0 Example 1A: Plotting Point (4, 0)",
        "subtitle": "Unit 2 • Lecture 16 • Section 2.0 Example 1A (Workbook p. 30)",
        "detail": "Lecture 16: The Cartesian Plane & Plotting Points",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1A (Workbook p. 30)\nPlot and label the ordered pair on the Cartesian plane:\n$$\\mathbf{A.\\; (4, 0)}$$\n- Identify the $x$-coordinate and $y$-coordinate.\n- State its location: Does it lie in a quadrant or on an axis?",
        "solution": "$$\\begin{aligned}\n\\text{Given: } & (x, y) = (4, 0) \\\\[0.5em]\n\\text{Step 1: } & \\text{Start at the origin } (0, 0). \\\\\n\\text{Step 2: } & \\text{Move } \\mathbf{4 \\text{ units right}} \\text{ along the } x\\text{-axis.} \\\\\n\\text{Step 3: } & y = 0 \\implies \\text{Do not move vertically.} \\\\[0.5em]\n\\text{Location: } & \\mathbf{\\text{On the positive } x\\text{-axis (an } x\\text{-intercept)}}.\n\\end{aligned}$$",
        "pitfall": "**Points with zero coordinates:** If $y = 0$, the point lies directly on the $x$-axis. It does NOT belong to any quadrant!",
        "script": "[Prof. Park] In Example 1A, we plot $(4, 0)$. Where do we go, Sora?\n\n[TA Sora] We start at $(0,0)$, go 4 units to the right, and stay right there on the axis because $y=0$!\n\n[Prof. Park] Excellent. Any point with $y=0$ is an $x$-intercept.",
        "graph": {
            "xMin": -8, "xMax": 8, "yMin": -8, "yMax": 8,
            "title": "Plotting Point A: (4, 0) on X-Axis",
            "points": [{"x": 4, "y": 0, "label": "A (4, 0)", "color": "#f59e0b", "labelOffsetX": 8, "labelOffsetY": -18}]
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.0 Example 1B: Plotting Point (-1, 3)",
        "subtitle": "Unit 2 • Lecture 16 • Section 2.0 Example 1B (Workbook p. 30)",
        "detail": "Lecture 16: The Cartesian Plane & Plotting Points",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1B (Workbook p. 30)\nPlot and label the ordered pair on the Cartesian plane:\n$$\\mathbf{B.\\; (-1, 3)}$$\n- Identify the direction of horizontal and vertical displacement.\n- State which quadrant contains this point.",
        "solution": "$$\\begin{aligned}\n\\text{Given: } & (x, y) = (-1, 3) \\\\[0.5em]\n\\text{Step 1: } & \\text{Start at the origin } (0, 0). \\\\\n\\text{Step 2: } & x = -1 \\implies \\text{Move } \\mathbf{1 \\text{ unit left}}. \\\\\n\\text{Step 3: } & y = 3 \\implies \\text{Move } \\mathbf{3 \\text{ units up}}. \\\\[0.5em]\n\\text{Location: } & \\mathbf{\\text{Quadrant II } (-, +)}.\n\\end{aligned}$$",
        "pitfall": "**Sign awareness:** A negative $x$ means move left, while a positive $y$ means move up. That places us in Quadrant II!",
        "script": "[Prof. Park] Now Example 1B: $(-1, 3)$. Watch the negative sign carefully.\n\n[TA Sora] $x = -1$ means 1 step left of the origin, then $y = 3$ means 3 steps up. We land squarely in Quadrant II!\n\n[Prof. Park] Notice the glowing point on your coordinate grid.",
        "graph": {
            "xMin": -8, "xMax": 8, "yMin": -8, "yMax": 8,
            "title": "Plotting Point B: (-1, 3) in Quadrant II",
            "points": [{"x": -1, "y": 3, "label": "B (-1, 3)", "color": "#38bdf8", "labelOffsetX": 8, "labelOffsetY": -18}]
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.0 Example 1C: Plotting Point (0, 5)",
        "subtitle": "Unit 2 • Lecture 16 • Section 2.0 Example 1C (Workbook p. 30)",
        "detail": "Lecture 16: The Cartesian Plane & Plotting Points",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1C (Workbook p. 30)\nPlot and label the ordered pair on the Cartesian plane:\n$$\\mathbf{C.\\; (0, 5)}$$\n- Identify the $x$-coordinate and $y$-coordinate.\n- State its location: Does it lie in a quadrant or on an axis?",
        "solution": "$$\\begin{aligned}\n\\text{Given: } & (x, y) = (0, 5) \\\\[0.5em]\n\\text{Step 1: } & \\text{Start at the origin } (0, 0). \\\\\n\\text{Step 2: } & x = 0 \\implies \\text{No horizontal movement.} \\\\\n\\text{Step 3: } & y = 5 \\implies \\text{Move } \\mathbf{5 \\text{ units up}} \\text{ along the } y\\text{-axis.} \\\\[0.5em]\n\\text{Location: } & \\mathbf{\\text{On the positive } y\\text{-axis (a } y\\text{-intercept)}}.\n\\end{aligned}$$",
        "pitfall": "**Do not confuse $(0, 5)$ with $(5, 0)$!** $(0, 5)$ is 5 units straight UP on the vertical axis. $(5, 0)$ is 5 units to the RIGHT on the horizontal axis.",
        "script": "[Prof. Park] Example 1C gives us $(0, 5)$. Students often mix this up with $(5, 0)$.\n\n[TA Sora] Yes! $(0, 5)$ means zero horizontal shift, then move 5 units straight up. It's a $y$-intercept on the vertical axis!",
        "graph": {
            "xMin": -8, "xMax": 8, "yMin": -8, "yMax": 8,
            "title": "Plotting Point C: (0, 5) on Y-Axis",
            "points": [{"x": 0, "y": 5, "label": "C (0, 5)", "color": "#10b981", "labelOffsetX": 8, "labelOffsetY": -18}]
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.0 Example 1D: Plotting Point (-3, -4)",
        "subtitle": "Unit 2 • Lecture 16 • Section 2.0 Example 1D (Workbook p. 30)",
        "detail": "Lecture 16: The Cartesian Plane & Plotting Points",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1D (Workbook p. 30)\nPlot and label the ordered pair on the Cartesian plane:\n$$\\mathbf{D.\\; (-3, -4)}$$\n- Identify the horizontal and vertical displacement.\n- State which quadrant contains this point.",
        "solution": "$$\\begin{aligned}\n\\text{Given: } & (x, y) = (-3, -4) \\\\[0.5em]\n\\text{Step 1: } & \\text{Start at the origin } (0, 0). \\\\\n\\text{Step 2: } & x = -3 \\implies \\text{Move } \\mathbf{3 \\text{ units left}}. \\\\\n\\text{Step 3: } & y = -4 \\implies \\text{Move } \\mathbf{4 \\text{ units down}}. \\\\[0.5em]\n\\text{Location: } & \\mathbf{\\text{Quadrant III } (-, -)}.\n\\end{aligned}$$",
        "pitfall": "**Both coordinates negative:** When both $x < 0$ and $y < 0$, the point is strictly in Quadrant III (bottom-left quadrant).",
        "script": "[Prof. Park] In Example 1D, both coordinates are negative: $(-3, -4)$.\n\n[TA Sora] 3 units to the left, 4 units down. We arrive in Quadrant III!",
        "graph": {
            "xMin": -8, "xMax": 8, "yMin": -8, "yMax": 8,
            "title": "Plotting Point D: (-3, -4) in Quadrant III",
            "points": [{"x": -3, "y": -4, "label": "D (-3, -4)", "color": "#ec4899", "labelOffsetX": 8, "labelOffsetY": 12}]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Synthesis & Comparison",
        "title": "Section 2.0 Example 1 Synthesis: All 4 Points",
        "subtitle": "Unit 2 • Lecture 16 • Section 2.0 Complete Set (Workbook p. 30)",
        "detail": "Lecture 16: The Cartesian Plane & Plotting Points",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 Complete Grid Overview (Workbook p. 30)\nCompare all four points plotted together on the same Cartesian coordinate plane:\n- $\\mathbf{A(4, 0)}$ — $x$-axis intercept\n- $\\mathbf{B(-1, 3)}$ — Quadrant II\n- $\\mathbf{C(0, 5)}$ — $y$-axis intercept\n- $\\mathbf{D(-3, -4)}$ — Quadrant III",
        "solution": "$$\\begin{array}{|c|c|c|c|}\n\\hline\n\\textbf{Point} & \\textbf{Coordinates} & \\textbf{Signs } (x, y) & \\textbf{Location} \\\\\n\\hline\nA & (4, 0) & (+, 0) & x\\text{-axis (Intercept)} \\\\\nB & (-1, 3) & (-, +) & \\text{Quadrant II} \\\\\nC & (0, 5) & (0, +) & y\\text{-axis (Intercept)} \\\\\nD & (-3, -4) & (-, -) & \\text{Quadrant III} \\\\\n\\hline\n\\end{array}$$",
        "pitfall": "**Axis points are NOT in quadrants:** Remember points on axes (like $A$ and $C$) do not belong to any quadrant.",
        "script": "[Prof. Park] Here are all four points plotted simultaneously on the Cartesian coordinate plane.\n\n[TA Sora] Notice how each color highlights a distinct region: $A$ on the horizontal axis, $C$ on the vertical axis, $B$ in Quadrant II, and $D$ in Quadrant III!",
        "graph": {
            "xMin": -8, "xMax": 8, "yMin": -8, "yMax": 8,
            "title": "Example 1 All 4 Points: A(4,0), B(-1,3), C(0,5), D(-3,-4)",
            "points": [
                {"x": 4, "y": 0, "label": "A (4, 0)", "color": "#f59e0b", "labelOffsetX": 8, "labelOffsetY": -18},
                {"x": -1, "y": 3, "label": "B (-1, 3)", "color": "#38bdf8", "labelOffsetX": 8, "labelOffsetY": -18},
                {"x": 0, "y": 5, "label": "C (0, 5)", "color": "#10b981", "labelOffsetX": 8, "labelOffsetY": -18},
                {"x": -3, "y": -4, "label": "D (-3, -4)", "color": "#ec4899", "labelOffsetX": 8, "labelOffsetY": 12}
            ]
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Basic Graphing Strategy: Input (x) & Output (y)",
        "subtitle": "Unit 2 • Lecture 16 • Section 2.0 Strategy (Workbook p. 30)",
        "detail": "Lecture 16: The Cartesian Plane & Plotting Points",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Basic Graphing Strategy (Workbook p. 30)\n- **Input values ($x$):** The independent variable chosen from the domain.\n- **Output values ($y$):** The dependent variable computed from the algebraic expression.\n- **Graph:** The set of all ordered pairs $(x, y)$ that satisfy the equation.\n- **Rule of Thumb:** Plot enough points to clearly see the geometric trend (straight line, curve, or V-shape)!",
        "solution": "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Choose a convenient set of } x\\text{-values (e.g. } -2, -1, 0, 1, 2\\text{).} \\\\\n\\text{Step 2: } & \\text{Substitute each } x \\text{ into the equation to calculate } y. \\\\\n\\text{Step 3: } & \\text{List ordered pairs } (x, y) \\text{ in a table of values.} \\\\\n\\text{Step 4: } & \\text{Plot each point on the coordinate plane.} \\\\\n\\text{Step 5: } & \\text{Connect the points with a smooth line or curve with arrows.}\n\\end{aligned}$$",
        "pitfall": "**Picking convenient numbers:** Choose $x$-values that keep calculations simple, like $0$ and values that cancel out denominators if fractions are involved!",
        "script": "[Prof. Park] In Section 2.0 of our workbook, the authors emphasize the Basic Graphing Strategy. $x$ is the input, $y$ is the output.\n\n[TA Sora] We construct a table, calculate the output, and plot points to see the shape."
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Formal Definition",
        "title": "Definition: Solution of an Equation in Two Variables",
        "subtitle": "Unit 2 • Lecture 16 • Section 2.0 Definition (Workbook p. 30)",
        "detail": "Lecture 16: The Cartesian Plane & Plotting Points",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Definition of a Solution (Workbook p. 30)\nAn ordered pair $(x, y)$ is a **solution to an equation involving $x$ and $y$** if the equation becomes a **true statement** when the $x$- and $y$-values of the ordered pair are substituted into the equation.\n\n$$\\text{If substituted: } \\text{Left Side} = \\text{Right Side} \\implies \\text{Solution (Point lies on graph)}$$",
        "solution": "$$\\begin{aligned}\n\\text{Given equation: } & 2x + y = 7 \\\\[0.5em]\n\\text{Test Point } (2, 3): & 2(2) + 3 = 4 + 3 = 7 \\implies \\mathbf{7 = 7 \\; (\\text{TRUE! Solution})} \\\\\n\\text{Test Point } (1, 4): & 2(1) + 4 = 2 + 4 = 6 \\neq 7 \\implies \\mathbf{6 = 7 \\; (\\text{FALSE! Not a solution})}\n\\end{aligned}$$",
        "pitfall": "**Check both coordinates:** Always put $x$ into the $x$-spot and $y$ into the $y$-spot. Don't swap them!",
        "script": "[Prof. Park] This definition is fundamental: a point is a solution if and only if it makes the statement true.\n\n[TA Sora] Visually, that means the point lies directly ON the line or curve!"
    },
    {
        "num": 9,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Testing Solutions on the Coordinate Plane: 2x + y = 7",
        "subtitle": "Unit 2 • Lecture 16 • Section 2.0 Verification (Workbook p. 30)",
        "detail": "Lecture 16: The Cartesian Plane & Plotting Points",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Testing Points for $2x + y = 7$\nDetermine algebraically and visually whether the following points are solutions to $2x + y = 7$:\n- **Point P:** $(2, 3)$\n- **Point Q:** $(4, -1)$\n- **Point R:** $(1, 2)$",
        "solution": "$$\\begin{aligned}\n\\text{Point P } (2, 3): & 2(2) + 3 = 4 + 3 = 7 \\implies \\mathbf{\\text{TRUE } \\implies \\text{ON LINE}} \\\\[0.5em]\n\\text{Point Q } (4, -1): & 2(4) + (-1) = 8 - 1 = 7 \\implies \\mathbf{\\text{TRUE } \\implies \\text{ON LINE}} \\\\[0.5em]\n\\text{Point R } (1, 2): & 2(1) + 2 = 2 + 2 = 4 \\neq 7 \\implies \\mathbf{\\text{FALSE } \\implies \\text{OFF LINE}}\n\\end{aligned}$$",
        "pitfall": "**Visual connection:** Notice on the coordinate plane how $(2, 3)$ and $(4, -1)$ sit perfectly on the line $y = -2x + 7$, while $(1, 2)$ is completely off the line!",
        "script": "[Prof. Park] Look at the graph. The blue line represents all solutions to $2x + y = 7$.\n\n[TA Sora] Point P $(2, 3)$ and Point Q $(4, -1)$ light up directly on the blue line! Point R $(1, 2)$ misses the line entirely!",
        "graph": {
            "xMin": -2, "xMax": 8, "yMin": -3, "yMax": 9,
            "title": "Testing Solutions to 2x + y = 7 (y = -2x + 7)",
            "points": [
                {"x": 2, "y": 3, "label": "P(2,3) [ON]", "color": "#10b981", "labelOffsetX": 8, "labelOffsetY": -18},
                {"x": 4, "y": -1, "label": "Q(4,-1) [ON]", "color": "#10b981", "labelOffsetX": 8, "labelOffsetY": 12},
                {"x": 1, "y": 2, "label": "R(1,2) [OFF]", "color": "#ef4444", "labelOffsetX": 8, "labelOffsetY": -18}
            ],
            "lines": [
                {"slope": -2, "yIntercept": 7, "color": "#38bdf8", "strokeWidth": 2.5, "label": "2x + y = 7"}
            ]
        }
    },
    {
        "num": 10,
        "type": "math_problem",
        "slideTypeLabel": "Sora's Pro-Tip & Mastery",
        "title": "Lecture 16 Mastery: Quadrant Signs & Coordinate Plane",
        "subtitle": "Unit 2 • Lecture 16 • Section 2.0 Wrap-up",
        "detail": "Lecture 16: The Cartesian Plane & Plotting Points",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Summary of Cartesian Coordinates\n- **Quadrant I:** $(+, +)$ — Upper Right\n- **Quadrant II:** $(-, +)$ — Upper Left\n- **Quadrant III:** $(-, -)$ — Lower Left\n- **Quadrant IV:** $(+, -)$ — Lower Right\n- **$x$-axis intercept:** $(a, 0)$ where $y = 0$\n- **$y$-axis intercept:** $(0, b)$ where $x = 0$\n- **Origin:** $(0, 0)$ where both axes cross",
        "solution": "$$\\mathbf{\\text{Lecture 16 Complete! Ready for Section 2.0 Part 2: Basic Graphs \\& Domain/Range!}}$$",
        "pitfall": "**Memory Anchor:** Quadrants are numbered counterclockwise (I $\\rightarrow$ II $\\rightarrow$ III $\\rightarrow$ IV), forming the shape of a capital 'C' for Cartesian!",
        "script": "[Prof. Park] Outstanding work on Lecture 16! You have mastered plotting points and testing solutions.\n\n[TA Sora] In Lecture 17, we take this exact coordinate grid and plot the 7 fundamental parent equations of algebra!"
    }
]

print("L16 defined.")
