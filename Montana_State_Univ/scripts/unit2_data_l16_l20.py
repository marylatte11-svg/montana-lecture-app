# Unit 2 Lectures 16 - 20 Data
# Faithful to M090 Workbook pp. 30 - 39

data_16_20 = {}

# L16: Section 2.0 Part 1 (Workbook p. 30) - 10 slides
data_16_20[16] = [
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

# L17: Section 2.0 Part 2 (Workbook pp. 31 - 32) - 9 slides
data_16_20[17] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Library of Basic Parent Functions & Interval Notation",
        "subtitle": "Unit 2 • Lecture 17 • Section 2.0 (Workbook p. 31)",
        "detail": "Lecture 17: Elementary Functions & Domain/Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Basic Equations & Domain/Range (Workbook p. 31)\nIn Section 2.0, we explore the 7 fundamental shapes of algebra:\n1. Constant: $y = c$\n2. Linear: $y = x$\n3. Quadratic: $y = x^2$\n4. Square Root: $y = \\sqrt{x}$\n5. Absolute Value: $y = \\lvert x \\rvert$\n6. Cubic: $y = x^3$\n7. Cube Root: $y = \\sqrt[3]{x}$\n\nState the **Domain** ($x$-values) and **Range** ($y$-values) in **interval notation**.",
        "solution": "$$\\begin{aligned}\n\\text{Domain: } & \\text{Set of all possible input } x\\text{-values (left-to-right)} \\\\\n\\text{Range: } & \\text{Set of all possible output } y\\text{-values (bottom-to-top)} \\\\\n\\text{Interval Notation: } & [\\text{inclusive}], \\quad (\\text{exclusive or } \\pm\\infty)\n\\end{aligned}$$",
        "pitfall": "**Interval bounds order:** Always write intervals from least to greatest: $(\\text{smaller}, \\text{larger})$. Never write $(5, -2)$!",
        "script": "[Prof. Park] In Lecture 17, we build the fundamental library of function shapes that you will use in all future math courses.\n\n[TA Sora] We will graph each equation by plotting points, and state its domain and range in interval notation!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Basic Equation A: Constant Function y = 3",
        "subtitle": "Unit 2 • Lecture 17 • Section 2.0 A (Workbook p. 31)",
        "detail": "Lecture 17: Elementary Functions & Domain/Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Equation A: $y = 3$ (Workbook p. 31)\n- Create a table of values for $x = -2, 0, 2$.\n- Graph the equation on the Cartesian coordinate plane.\n- State the **Domain** and **Range** in interval notation.",
        "solution": "$$\\begin{aligned}\n\\text{Table of Values: } & (-2, 3), \\; (0, 3), \\; (2, 3) \\\\[0.5em]\n\\text{Graph Shape: } & \\mathbf{\\text{Horizontal Line at } y = 3} \\\\[0.5em]\n\\mathbf{\\text{Domain: }} & \\mathbf{(-\\infty, \\infty)} \\quad (x \\text{ can be any real number}) \\\\\n\\mathbf{\\text{Range: }} & \\mathbf{\\{3\\}} \\quad (y \\text{ is strictly locked at } 3)\n\\end{aligned}$$",
        "pitfall": "**Range of a constant:** The range contains only a single number, so we write $\\{3\\}$ or $[3, 3]$, not $(-\\infty, \\infty)$!",
        "script": "[Prof. Park] Notice that no matter what $x$ you pick, $y$ remains 3. That produces a perfectly flat, horizontal line.\n\n[TA Sora] Domain is $(-\\infty, \\infty)$ because the line extends left and right forever. But range is just the single value $\\{3\\}$!",
        "graph": {
            "xMin": -8, "xMax": 8, "yMin": -4, "yMax": 8,
            "title": "Constant Function: y = 3 (Horizontal Line)",
            "points": [
                {"x": -2, "y": 3, "label": "(-2, 3)", "color": "#f59e0b"},
                {"x": 0, "y": 3, "label": "(0, 3)", "color": "#38bdf8"},
                {"x": 2, "y": 3, "label": "(2, 3)", "color": "#10b981"}
            ],
            "lines": [
                {"horizontal": 3, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = 3"}
            ]
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Basic Equation B: Linear Identity y = x",
        "subtitle": "Unit 2 • Lecture 17 • Section 2.0 B (Workbook p. 31)",
        "detail": "Lecture 17: Elementary Functions & Domain/Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Equation B: $y = x$ (Workbook p. 31)\n- Create a table of values for $x = -2, 0, 2$.\n- Graph the equation on the Cartesian coordinate plane.\n- State the **Domain** and **Range** in interval notation.",
        "solution": "$$\\begin{aligned}\n\\text{Table of Values: } & (-2, -2), \\; (0, 0), \\; (2, 2) \\\\[0.5em]\n\\text{Graph Shape: } & \\mathbf{\\text{Diagonal Line passing through the origin at } 45^\\circ} \\\\[0.5em]\n\\mathbf{\\text{Domain: }} & \\mathbf{(-\\infty, \\infty)} \\\\\n\\mathbf{\\text{Range: }} & \\mathbf{(-\\infty, \\infty)}\n\\end{aligned}$$",
        "pitfall": "**Identity relationship:** Every output equals its input: $x = y$. It passes directly through $(0, 0)$ with slope $m = 1$.",
        "script": "[Prof. Park] In $y = x$, the input and output are identical. $(-2, -2)$, $(0,0)$, $(2,2)$.\n\n[TA Sora] It slants upward at a perfect 45-degree angle. Both domain and range are all real numbers $(-\\infty, \\infty)$!",
        "graph": {
            "xMin": -6, "xMax": 6, "yMin": -6, "yMax": 6,
            "title": "Linear Identity: y = x (Diagonal Line)",
            "points": [
                {"x": -2, "y": -2, "label": "(-2, -2)", "color": "#f59e0b"},
                {"x": 0, "y": 0, "label": "(0, 0)", "color": "#38bdf8"},
                {"x": 2, "y": 2, "label": "(2, 2)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": 1, "yIntercept": 0, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = x"}
            ]
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Basic Equation C: Quadratic Parabola y = x^2",
        "subtitle": "Unit 2 • Lecture 17 • Section 2.0 C (Workbook p. 31)",
        "detail": "Lecture 17: Elementary Functions & Domain/Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Equation C: $y = x^2$ (Workbook p. 31)\n- Create a table of values for $x = -2, -1, 0, 1, 2$.\n- Graph the equation on the Cartesian coordinate plane.\n- State the **Domain** and **Range** in interval notation.",
        "solution": "$$\\begin{aligned}\n\\text{Table of Values: } & (-2, 4), \\; (-1, 1), \\; (0, 0), \\; (1, 1), \\; (2, 4) \\\\[0.5em]\n\\text{Graph Shape: } & \\mathbf{\\text{U-shaped Curve (Parabola) with vertex at } (0, 0)} \\\\[0.5em]\n\\mathbf{\\text{Domain: }} & \\mathbf{(-\\infty, \\infty)} \\\\\n\\mathbf{\\text{Range: }} & \\mathbf{[0, \\infty)} \\quad (\\text{since } x^2 \\ge 0 \\text{ for all real } x)\n\\end{aligned}$$",
        "pitfall": "**Squaring negatives:** $(-2)^2 = +4$, NOT $-4$! Because outputs are never negative, the range starts at $0$ with a bracket $[0, \\infty)$.",
        "script": "[Prof. Park] When we square a real number, the result is never negative. Look at the U-shape called a parabola.\n\n[TA Sora] Notice the lowest point is the vertex at $(0,0)$. The range is $[0, \\infty)$ with a bracket on 0 because 0 is included!",
        "graph": {
            "xMin": -5, "xMax": 5, "yMin": -2, "yMax": 8,
            "title": "Quadratic Parabola: y = x^2",
            "points": [
                {"x": -2, "y": 4, "label": "(-2, 4)", "color": "#f59e0b"},
                {"x": -1, "y": 1, "label": "(-1, 1)", "color": "#38bdf8"},
                {"x": 0, "y": 0, "label": "Vertex (0, 0)", "color": "#10b981"},
                {"x": 1, "y": 1, "label": "(1, 1)", "color": "#38bdf8"},
                {"x": 2, "y": 4, "label": "(2, 4)", "color": "#f59e0b"}
            ]
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Basic Equation D: Square Root Curve y = sqrt(x)",
        "subtitle": "Unit 2 • Lecture 17 • Section 2.0 D (Workbook p. 31)",
        "detail": "Lecture 17: Elementary Functions & Domain/Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Equation D: $y = \\sqrt{x}$ (Workbook p. 31)\n- Create a table of values for $x = 0, 1, 4, 9$.\n- Graph the equation on the Cartesian coordinate plane.\n- State the **Domain** and **Range** in interval notation.",
        "solution": "$$\\begin{aligned}\n\\text{Table of Values: } & (0, 0), \\; (1, 1), \\; (4, 2), \\; (9, 3) \\\\[0.5em]\n\\text{Graph Shape: } & \\mathbf{\\text{Half-sideways curve starting at } (0, 0)} \\\\[0.5em]\n\\mathbf{\\text{Domain: }} & \\mathbf{[0, \\infty)} \\quad (\\text{cannot take square root of negative numbers}) \\\\\n\\mathbf{\\text{Range: }} & \\mathbf{[0, \\infty)} \\quad (\\text{principal square root is non-negative})\n\\end{aligned}$$",
        "pitfall": "**Negative radicands:** In the real number system, $\\sqrt{-4}$ is not a real number. Therefore $x$ cannot be negative!",
        "script": "[Prof. Park] In $y = \\sqrt{x}$, we cannot plug in negative numbers in real algebra. So the graph starts at the origin $(0, 0)$.\n\n[TA Sora] Domain is $[0, \\infty)$ and Range is $[0, \\infty)$! The curve rises gradually to the right.",
        "graph": {
            "xMin": -2, "xMax": 10, "yMin": -2, "yMax": 6,
            "title": "Square Root Curve: y = sqrt(x)",
            "points": [
                {"x": 0, "y": 0, "label": "(0, 0)", "color": "#10b981"},
                {"x": 1, "y": 1, "label": "(1, 1)", "color": "#38bdf8"},
                {"x": 4, "y": 2, "label": "(4, 2)", "color": "#f59e0b"}
            ]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Basic Equation E: Absolute Value y = |x|",
        "subtitle": "Unit 2 • Lecture 17 • Section 2.0 E (Workbook p. 32)",
        "detail": "Lecture 17: Elementary Functions & Domain/Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Equation E: $y = \\lvert x \\rvert$ (Workbook p. 32)\n- Create a table of values for $x = -3, -1, 0, 1, 3$.\n- Graph the equation on the Cartesian coordinate plane.\n- State the **Domain** and **Range** in interval notation.",
        "solution": "$$\\begin{aligned}\n\\text{Table of Values: } & (-3, 3), \\; (-1, 1), \\; (0, 0), \\; (1, 1), \\; (3, 3) \\\\[0.5em]\n\\text{Graph Shape: } & \\mathbf{\\text{V-shaped Graph with sharp vertex at } (0, 0)} \\\\[0.5em]\n\\mathbf{\\text{Domain: }} & \\mathbf{(-\\infty, \\infty)} \\\\\n\\mathbf{\\text{Range: }} & \\mathbf{[0, \\infty)}\n\\end{aligned}$$",
        "pitfall": "**V-shape vs U-shape:** Absolute value has straight linear rays forming a sharp 'V' with corner at $(0, 0)$, while $y = x^2$ is a smooth rounded 'U'!",
        "script": "[Prof. Park] Look at $y = |x|$. Because distance from zero is always positive or zero, negative inputs bounce back up.\n\n[TA Sora] This creates a sharp V-shape with vertex at $(0,0)$. Domain is $(-\\infty, \\infty)$ and range is $[0, \\infty)$!",
        "graph": {
            "xMin": -6, "xMax": 6, "yMin": -2, "yMax": 6,
            "title": "Absolute Value: y = |x| (V-Shaped Graph)",
            "points": [
                {"x": -3, "y": 3, "label": "(-3, 3)", "color": "#f59e0b"},
                {"x": -1, "y": 1, "label": "(-1, 1)", "color": "#38bdf8"},
                {"x": 0, "y": 0, "label": "(0, 0)", "color": "#10b981"},
                {"x": 1, "y": 1, "label": "(1, 1)", "color": "#38bdf8"},
                {"x": 3, "y": 3, "label": "(3, 3)", "color": "#f59e0b"}
            ],
            "lines": [
                {"p1": [-6, 6], "p2": [0, 0], "color": "#ec4899", "strokeWidth": 2.5},
                {"p1": [0, 0], "p2": [6, 6], "color": "#ec4899", "strokeWidth": 2.5}
            ]
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Basic Equation F: Cubic Function y = x^3",
        "subtitle": "Unit 2 • Lecture 17 • Section 2.0 F (Workbook p. 32)",
        "detail": "Lecture 17: Elementary Functions & Domain/Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Equation F: $y = x^3$ (Workbook p. 32)\n- Create a table of values for $x = -2, -1, 0, 1, 2$.\n- Graph the equation on the Cartesian coordinate plane.\n- State the **Domain** and **Range** in interval notation.",
        "solution": "$$\\begin{aligned}\n\\text{Table of Values: } & (-2, -8), \\; (-1, -1), \\; (0, 0), \\; (1, 1), \\; (2, 8) \\\\[0.5em]\n\\text{Graph Shape: } & \\mathbf{\\text{S-shaped Snake Curve passing through the origin}} \\\\[0.5em]\n\\mathbf{\\text{Domain: }} & \\mathbf{(-\\infty, \\infty)} \\\\\n\\mathbf{\\text{Range: }} & \\mathbf{(-\\infty, \\infty)}\n\\end{aligned}$$",
        "pitfall": "**Odd powers preserve signs:** $(-2)^3 = -8$, while $(+2)^3 = +8$. Unlike $x^2$, cubic graphs go down to $-\\infty$ on the left and up to $+\\infty$ on the right!",
        "script": "[Prof. Park] In $y = x^3$, odd powers keep the sign of the base. Negative numbers produce negative cubes.\n\n[TA Sora] This makes an S-curve that passes through the origin. Both domain and range are all real numbers $(-\\infty, \\infty)$!",
        "graph": {
            "xMin": -4, "xMax": 4, "yMin": -9, "yMax": 9,
            "title": "Cubic Function: y = x^3 (S-Curve)",
            "points": [
                {"x": -2, "y": -8, "label": "(-2, -8)", "color": "#ec4899"},
                {"x": -1, "y": -1, "label": "(-1, -1)", "color": "#f59e0b"},
                {"x": 0, "y": 0, "label": "(0, 0)", "color": "#10b981"},
                {"x": 1, "y": 1, "label": "(1, 1)", "color": "#38bdf8"},
                {"x": 2, "y": 8, "label": "(2, 8)", "color": "#38bdf8"}
            ]
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Basic Equation G: Cube Root y = cbrt(x)",
        "subtitle": "Unit 2 • Lecture 17 • Section 2.0 G (Workbook p. 32)",
        "detail": "Lecture 17: Elementary Functions & Domain/Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Equation G: $y = \\sqrt[3]{x}$ (Workbook p. 32)\n- Create a table of values for $x = -8, -1, 0, 1, 8$.\n- Graph the equation on the Cartesian coordinate plane.\n- State the **Domain** and **Range** in interval notation.",
        "solution": "$$\\begin{aligned}\n\\text{Table of Values: } & (-8, -2), \\; (-1, -1), \\; (0, 0), \\; (1, 1), \\; (8, 2) \\\\[0.5em]\n\\text{Graph Shape: } & \\mathbf{\\text{Sideways S-shaped Curve extending horizontally}} \\\\[0.5em]\n\\mathbf{\\text{Domain: }} & \\mathbf{(-\\infty, \\infty)} \\quad (\\text{odd roots are defined for negative numbers!}) \\\\\n\\mathbf{\\text{Range: }} & \\mathbf{(-\\infty, \\infty)}\n\\end{aligned}$$",
        "pitfall": "**Odd roots CAN take negative inputs:** Unlike $\\sqrt{-8}$ which is not real, $\\sqrt[3]{-8} = -2$ is completely valid and real!",
        "script": "[Prof. Park] Notice the critical distinction between even roots and odd roots: you can take the cube root of negative 8, which is negative 2!\n\n[TA Sora] Yes! So the domain of $\\sqrt[3]{x}$ is all real numbers $(-\\infty, \\infty)$, unlike square root which stopped at 0.",
        "graph": {
            "xMin": -9, "xMax": 9, "yMin": -4, "yMax": 4,
            "title": "Cube Root: y = cbrt(x) (Sideways S-Curve)",
            "points": [
                {"x": -8, "y": -2, "label": "(-8, -2)", "color": "#ec4899"},
                {"x": -1, "y": -1, "label": "(-1, -1)", "color": "#f59e0b"},
                {"x": 0, "y": 0, "label": "(0, 0)", "color": "#10b981"},
                {"x": 1, "y": 1, "label": "(1, 1)", "color": "#38bdf8"},
                {"x": 8, "y": 2, "label": "(8, 2)", "color": "#38bdf8"}
            ]
        }
    },
    {
        "num": 9,
        "type": "math_problem",
        "slideTypeLabel": "Grand Summary & Review",
        "title": "Section 2.0 Grand Summary: Parent Functions & Intervals",
        "subtitle": "Unit 2 • Lecture 17 • Section 2.0 Complete Summary",
        "detail": "Lecture 17: Elementary Functions & Domain/Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Parent Functions Comparison Table (Workbook pp. 31–32)\nReview the core characteristics of the 7 basic algebra equations:\n- Constant: $y = 3$ (Horizontal line, $R: \\{3\\}$)\n- Linear: $y = x$ (Diagonal line, $D, R: (-\\infty, \\infty)$)\n- Parabola: $y = x^2$ (U-shape, $R: [0, \\infty)$)\n- Square root: $y = \\sqrt{x}$ (Half curve, $D, R: [0, \\infty)$)\n- Absolute value: $y = \\lvert x \\rvert$ (V-shape, $R: [0, \\infty)$)\n- Cubic: $y = x^3$ (S-curve, $D, R: (-\\infty, \\infty)$)\n- Cube root: $y = \\sqrt[3]{x}$ (Sideways S-curve, $D, R: (-\\infty, \\infty)$)",
        "solution": "$$\\mathbf{\\text{Section 2.0 Mastered! Next Up: Section 2.1 — Graphing Linear Equations \\& Intercepts!}}$$",
        "pitfall": "**Remember bracket vs parenthesis:** A bracket $[$ means the point is included in the set; a parenthesis $($ means excluded or infinite!",
        "script": "[Prof. Park] Outstanding work! You have completed Section 2.0 and mapped out all 7 parent curves of mathematics.\n\n[TA Sora] In Lecture 18, we dive deep into linear equations, tables, and intercept methods!"
    }
]

# L18: Section 2.1 Part 1 (Workbook pp. 33 - 34) - 8 slides
data_16_20[18] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Section 2.1: Linear Equations in Two Variables",
        "subtitle": "Unit 2 • Lecture 18 • Section 2.1 (Workbook p. 33)",
        "detail": "Lecture 18: Linear Equations & Intercept Method",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Section 2.1 Overview (Workbook p. 33)\n- **Standard Form:** $Ax + By = C$\n- **Slope-Intercept Form:** $y = mx + b$\n  - $m$ is the **slope** (rate of change, $\\frac{\\text{Rise}}{\\text{Run}}$).\n  - $(0, b)$ is the **$y$-intercept**.\n- In this section, we master two core graphing methods:\n  1. **Table of Values Method**\n  2. **Intercept Method**",
        "solution": "$$\\begin{aligned}\n\\text{Standard Form: } & Ax + By = C \\\\\n\\text{Slope-Intercept: } & y = mx + b \\\\\n\\text{Slope } m: & \\frac{\\Delta y}{\\Delta x} = \\frac{\\text{Rise}}{\\text{Run}} \\\\\n\\text{Y-Intercept: } & (0, b)\n\\end{aligned}$$",
        "pitfall": "**Converting to $y = mx + b$:** When solving for $y$, always divide EVERY term on both sides by the coefficient of $y$!",
        "script": "[Prof. Park] Welcome to Section 2.1! Today we focus on straight lines: linear equations in two variables.\n\n[TA Sora] We will learn how to graph them using tables of values and the powerful intercept method!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.1 Example 1 (Part 1): Table for 2x + 3y = 6",
        "subtitle": "Unit 2 • Lecture 18 • Section 2.1 Example 1 (Workbook p. 33)",
        "detail": "Lecture 18: Linear Equations & Intercept Method",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 (Workbook p. 33)\nGraph the following linear equation using a table:\n$$\\mathbf{2x + 3y = 6}$$\nComplete the table by finding the corresponding $y$ when $x = 0$, and finding $x$ when $y = 0$, plus a third checkpoint at $x = 6$.",
        "solution": "$$\\begin{aligned}\n\\text{When } x = 0: & 2(0) + 3y = 6 \\implies 3y = 6 \\implies \\mathbf{y = 2} \\implies \\mathbf{(0, 2)} \\\\[0.5em]\n\\text{When } y = 0: & 2x + 3(0) = 6 \\implies 2x = 6 \\implies \\mathbf{x = 3} \\implies \\mathbf{(3, 0)} \\\\[0.5em]\n\\text{When } x = 6: & 2(6) + 3y = 6 \\implies 12 + 3y = 6 \\implies 3y = -6 \\implies \\mathbf{y = -2} \\implies \\mathbf{(6, -2)}\n\\end{aligned}$$",
        "pitfall": "**Always use 3 points:** 2 points determine a straight line, but the 3rd point serves as an essential error check!",
        "script": "[Prof. Park] In Example 1, setting $x=0$ gives the $y$-intercept $(0, 2)$, and setting $y=0$ gives the $x$-intercept $(3, 0)$.\n\n[TA Sora] And setting $x=6$ gives $(6, -2)$. All three points line up perfectly on our coordinate grid!",
        "graph": {
            "xMin": -2, "xMax": 8, "yMin": -4, "yMax": 6,
            "title": "Plotting Table Points for 2x + 3y = 6",
            "points": [
                {"x": 0, "y": 2, "label": "(0, 2)", "color": "#10b981"},
                {"x": 3, "y": 0, "label": "(3, 0)", "color": "#f59e0b"},
                {"x": 6, "y": -2, "label": "(6, -2)", "color": "#38bdf8"}
            ]
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.1 Example 1 (Part 2): Solving for y",
        "subtitle": "Unit 2 • Lecture 18 • Section 2.1 Example 1 (Workbook p. 33)",
        "detail": "Lecture 18: Linear Equations & Intercept Method",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 Algebraic Follow-up (Workbook p. 33)\nNow solve the equation for $y$:\n$$\\mathbf{2x + 3y = 6}$$\n- Isolate the $y$-term by subtracting $2x$ from both sides.\n- Divide each term by $3$ to put into slope-intercept form $y = mx + b$.",
        "solution": "$$\\begin{aligned}\n2x + 3y & = 6 \\\\[0.5em]\n3y & = -2x + 6 \\quad (\\text{subtract } 2x) \\\\[0.5em]\ny & = \\frac{-2x + 6}{3} \\quad (\\text{divide by } 3) \\\\[0.5em]\n\\mathbf{y} & = \\mathbf{-\\frac{2}{3}x + 2} \\\\[0.8em]\n\\text{Slope } m: & \\mathbf{-\\frac{2}{3}} \\quad (\\text{Down 2, Right 3}) \\\\\n\\text{Y-Intercept: } & \\mathbf{(0, 2)}\n\\end{aligned}$$",
        "pitfall": "**Dividing fractions:** Make sure both $-2x$ and $6$ get divided by $3$: $\\frac{6}{3} = 2$, not $6$!",
        "script": "[Prof. Park] Converting $2x + 3y = 6$ into slope-intercept form reveals the slope directly: $m = -\\frac{2}{3}$ and $b = 2$.\n\n[TA Sora] That means starting from $(0, 2)$, you go DOWN 2 units and RIGHT 3 units to hit $(3, 0)$!"
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.1 Example 1 (Part 3): Full Graph & Intercepts",
        "subtitle": "Unit 2 • Lecture 18 • Section 2.1 Example 1 (Workbook p. 33)",
        "detail": "Lecture 18: Linear Equations & Intercept Method",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 Full Visual Verification (Workbook p. 33)\nUse the graph to identify the following:\n- **$x$-intercept:** ____________\n- **$y$-intercept:** ____________\n- **Slope ($m$):** ____________",
        "solution": "$$\\begin{aligned}\n\\mathbf{x\\text{-intercept: }} & \\mathbf{(3, 0)} \\quad (\\text{where line crosses horizontal axis}) \\\\\n\\mathbf{y\\text{-intercept: }} & \\mathbf{(0, 2)} \\quad (\\text{where line crosses vertical axis}) \\\\\n\\mathbf{\\text{Slope } m: } & \\mathbf{-\\frac{2}{3}} = \\frac{\\text{Rise}}{\\text{Run}} = \\frac{-2}{+3}\n\\end{aligned}$$",
        "pitfall": "**Intercept coordinates format:** Always write intercepts as ordered pairs: $(3, 0)$ and $(0, 2)$, not just the single numbers $3$ and $2$!",
        "script": "[Prof. Park] Look at the full graph on the screen. The straight line connects $(0,2)$, $(3,0)$, and $(6,-2)$ smoothly.\n\n[TA Sora] Notice the slope triangle showing a rise of $-2$ and a run of $+3$!",
        "graph": {
            "xMin": -3, "xMax": 8, "yMin": -4, "yMax": 6,
            "title": "Complete Graph: 2x + 3y = 6 (y = -2/3x + 2)",
            "points": [
                {"x": 0, "y": 2, "label": "y-int (0, 2)", "color": "#10b981"},
                {"x": 3, "y": 0, "label": "x-int (3, 0)", "color": "#f59e0b"},
                {"x": 6, "y": -2, "label": "(6, -2)", "color": "#38bdf8"}
            ],
            "lines": [
                {"slope": -2/3, "yIntercept": 2, "color": "#38bdf8", "strokeWidth": 2.5, "label": "2x + 3y = 6"}
            ],
            "slopeTriangle": {"x1": 0, "y1": 2, "x2": 3, "y2": 0, "rise": -2, "run": 3}
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.1 Example 2A: Slope & Y-Intercept for y = 1/4x - 6",
        "subtitle": "Unit 2 • Lecture 18 • Section 2.1 Example 2A (Workbook p. 33)",
        "detail": "Lecture 18: Linear Equations & Intercept Method",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2A (Workbook p. 33)\nIdentify the slope and $y$-intercept for:\n$$\\mathbf{y = \\frac{1}{4}x - 6}$$\n- State the slope $m$ as a fraction.\n- State the $y$-intercept as an ordered pair $(0, b)$.",
        "solution": "$$\\begin{aligned}\n\\text{Compare with } y = mx + b: \\\\[0.5em]\n\\mathbf{\\text{Slope } m: } & \\mathbf{\\frac{1}{4}} \\quad (\\text{Up 1, Right 4}) \\\\[0.5em]\n\\mathbf{y\\text{-intercept: }} & \\mathbf{(0, -6)}\n\\end{aligned}$$",
        "pitfall": "**Sign of intercept:** The minus sign belongs to the intercept! $b = -6$, so the intercept is $(0, -6)$, NOT $(0, 6)$!",
        "script": "[Prof. Park] In Example 2A, the equation is already in slope-intercept form.\n\n[TA Sora] The coefficient of $x$ is $m = \\frac{1}{4}$, and the constant is $-6$, so the $y$-intercept is $(0, -6)$!",
        "graph": {
            "xMin": -2, "xMax": 10, "yMin": -8, "yMax": 2,
            "title": "Graph of y = 1/4x - 6",
            "points": [
                {"x": 0, "y": -6, "label": "y-int (0, -6)", "color": "#10b981"},
                {"x": 4, "y": -5, "label": "(4, -5)", "color": "#38bdf8"}
            ],
            "lines": [
                {"slope": 0.25, "yIntercept": -6, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = 1/4x - 6"}
            ]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.1 Example 2B: Slope & Y-Intercept for 2x - y = 7",
        "subtitle": "Unit 2 • Lecture 18 • Section 2.1 Example 2B (Workbook p. 33)",
        "detail": "Lecture 18: Linear Equations & Intercept Method",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2B (Workbook p. 33)\nIdentify the slope and $y$-intercept for:\n$$\\mathbf{2x - y = 7}$$\n- Solve for $y$ first by isolating the variable.\n- Identify $m$ and $(0, b)$.",
        "solution": "$$\\begin{aligned}\n2x - y & = 7 \\\\[0.5em]\n-y & = -2x + 7 \\quad (\\text{subtract } 2x) \\\\[0.5em]\ny & = 2x - 7 \\quad (\\text{multiply by } -1) \\\\[0.8em]\n\\mathbf{\\text{Slope } m: } & \\mathbf{2} = \\frac{2}{1} \\quad (\\text{Up 2, Right 1}) \\\\[0.5em]\n\\mathbf{y\\text{-intercept: }} & \\mathbf{(0, -7)}\n\\end{aligned}$$",
        "pitfall": "**The negative sign in front of y:** When subtracting $2x$, don't drop the negative sign on $-y$. Dividing by $-1$ flips both $-2x \\rightarrow +2x$ and $7 \\rightarrow -7$!",
        "script": "[Prof. Park] In Example 2B, we must solve for $y$ first. $-y = -2x + 7$, so dividing by $-1$ gives $y = 2x - 7$.\n\n[TA Sora] The slope is $2$ (or $\\frac{2}{1}$) and the $y$-intercept is $(0, -7)$!",
        "graph": {
            "xMin": -2, "xMax": 8, "yMin": -9, "yMax": 3,
            "title": "Graph of 2x - y = 7 (y = 2x - 7)",
            "points": [
                {"x": 0, "y": -7, "label": "y-int (0, -7)", "color": "#10b981"},
                {"x": 2, "y": -3, "label": "(2, -3)", "color": "#38bdf8"},
                {"x": 3.5, "y": 0, "label": "x-int (3.5, 0)", "color": "#f59e0b"}
            ],
            "lines": [
                {"slope": 2, "yIntercept": -7, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = 2x - 7"}
            ]
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Formal Definition",
        "title": "Definition of Intercepts on the Cartesian Plane",
        "subtitle": "Unit 2 • Lecture 18 • Section 2.1 (Workbook p. 34)",
        "detail": "Lecture 18: Linear Equations & Intercept Method",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Definition of Intercepts (Workbook p. 34)\n- **$x$-intercept:** Any point on a graph with a $y$-value of $0$.\n  $$\\mathbf{(x, 0)} \\implies \\text{Set } y = 0 \\text{ and solve for } x$$\n- **$y$-intercept:** Any point on a graph with an $x$-value of $0$.\n  $$\\mathbf{(0, y)} \\implies \\text{Set } x = 0 \\text{ and solve for } y$$",
        "solution": "$$\\begin{aligned}\n\\text{To find } x\\text{-intercept: } & \\text{Substitute } y = 0 \\text{ into the equation, then solve for } x. \\\\\n\\text{To find } y\\text{-intercept: } & \\text{Substitute } x = 0 \\text{ into the equation, then solve for } y.\n\\end{aligned}$$",
        "pitfall": "**Which coordinate is zero?** To find the $x$-intercept, $y=0$. To find the $y$-intercept, $x=0$. It's always the OPPOSITE variable that is set to zero!",
        "script": "[Prof. Park] Remember this golden rule: the $x$-intercept sits on the $x$-axis, so its height is 0 ($y=0$).\n\n[TA Sora] And the $y$-intercept sits on the $y$-axis, so its horizontal shift is 0 ($x=0$)!"
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.1 Example 3A: Intercepts for 5x + 2y = 6",
        "subtitle": "Unit 2 • Lecture 18 • Section 2.1 Example 3A (Workbook p. 34)",
        "detail": "Lecture 18: Linear Equations & Intercept Method",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3A (Workbook p. 34)\nFind the $x$- and $y$-intercepts algebraically for:\n$$\\mathbf{5x + 2y = 6}$$\nThen re-write the equation into slope-intercept form.",
        "solution": "$$\\begin{aligned}\n\\mathbf{x\\text{-intercept: }} & 5x + 2(0) = 6 \\implies 5x = 6 \\implies \\mathbf{x = \\frac{6}{5} = 1.2} \\implies \\mathbf{\\left(\\frac{6}{5}, 0\\right)} \\\\[0.6em]\n\\mathbf{y\\text{-intercept: }} & 5(0) + 2y = 6 \\implies 2y = 6 \\implies \\mathbf{y = 3} \\implies \\mathbf{(0, 3)} \\\\[0.8em]\n\\text{Slope-Intercept: } & 2y = -5x + 6 \\implies \\mathbf{y = -\\frac{5}{2}x + 3}\n\\end{aligned}$$",
        "pitfall": "**Fractional intercepts are valid!** $x = \\frac{6}{5}$ is $1.2$. Plot it just past $1$ on the $x$-axis. Fractions are common in algebra!",
        "script": "[Prof. Park] In Example 3A, the $x$-intercept is a fraction: $\\frac{6}{5}$, which is $1.2$.\n\n[TA Sora] Setting $x=0$ yields $y=3$. So our intercepts are $(\\frac{6}{5}, 0)$ and $(0, 3)$. Look at how neatly they graph!",
        "graph": {
            "xMin": -2, "xMax": 5, "yMin": -2, "yMax": 6,
            "title": "Intercepts of 5x + 2y = 6 (y = -5/2x + 3)",
            "points": [
                {"x": 1.2, "y": 0, "label": "x-int (6/5, 0)", "color": "#f59e0b"},
                {"x": 0, "y": 3, "label": "y-int (0, 3)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": -2.5, "yIntercept": 3, "color": "#38bdf8", "strokeWidth": 2.5, "label": "5x + 2y = 6"}
            ]
        }
    }
]

# L19: Section 2.1 Part 2 (Workbook pp. 35 - 37) - 8 slides
data_16_20[19] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.1 Example 3B: Intercepts for 4x - 5y = 10",
        "subtitle": "Unit 2 • Lecture 19 • Section 2.1 Example 3B (Workbook p. 35)",
        "detail": "Lecture 19: Advanced Intercepts & Special Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3B (Workbook p. 35)\nFind the $x$- and $y$-intercepts algebraically for:\n$$\\mathbf{4x - 5y = 10}$$\nThen re-write the equation into slope-intercept form and graph the line.",
        "solution": "$$\\begin{aligned}\n\\mathbf{x\\text{-intercept: }} & 4x - 5(0) = 10 \\implies 4x = 10 \\implies \\mathbf{x = \\frac{10}{4} = \\frac{5}{2} = 2.5} \\implies \\mathbf{\\left(\\frac{5}{2}, 0\\right)} \\\\[0.6em]\n\\mathbf{y\\text{-intercept: }} & 4(0) - 5y = 10 \\implies -5y = 10 \\implies \\mathbf{y = -2} \\implies \\mathbf{(0, -2)} \\\\[0.8em]\n\\text{Slope-Intercept: } & -5y = -4x + 10 \\implies \\mathbf{y = \\frac{4}{5}x - 2}\n\\end{aligned}$$",
        "pitfall": "**Division by negative number:** $-5y = -4x + 10 \\implies y = \\frac{-4}{-5}x + \\frac{10}{-5} = +\\frac{4}{5}x - 2$. Watch the signs carefully!",
        "script": "[Prof. Park] In Example 3B, setting $y=0$ gives $x = \\frac{5}{2} = 2.5$, and setting $x=0$ gives $y = -2$.\n\n[TA Sora] Solving for $y$ confirms $y = \\frac{4}{5}x - 2$. The slope is positive $\\frac{4}{5}$, rising from left to right!",
        "graph": {
            "xMin": -2, "xMax": 6, "yMin": -5, "yMax": 4,
            "title": "Graph of 4x - 5y = 10 (y = 4/5x - 2)",
            "points": [
                {"x": 2.5, "y": 0, "label": "x-int (5/2, 0)", "color": "#f59e0b"},
                {"x": 0, "y": -2, "label": "y-int (0, -2)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": 0.8, "yIntercept": -2, "color": "#38bdf8", "strokeWidth": 2.5, "label": "4x - 5y = 10"}
            ]
        }
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.1 Example 3C: Intercepts for y = -3/2x - 3",
        "subtitle": "Unit 2 • Lecture 19 • Section 2.1 Example 3C (Workbook p. 36)",
        "detail": "Lecture 19: Advanced Intercepts & Special Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3C (Workbook p. 36)\nFind the $x$- and $y$-intercepts algebraically for:\n$$\\mathbf{y = -\\frac{3}{2}x - 3}$$\nThen graph the equation on the Cartesian coordinate plane.",
        "solution": "$$\\begin{aligned}\n\\mathbf{y\\text{-intercept: }} & \\text{Directly from equation: } b = -3 \\implies \\mathbf{(0, -3)} \\\\[0.6em]\n\\mathbf{x\\text{-intercept: }} & 0 = -\\frac{3}{2}x - 3 \\implies \\frac{3}{2}x = -3 \\\\\n& x = -3 \\cdot \\frac{2}{3} = \\mathbf{-2} \\implies \\mathbf{(-2, 0)} \\\\[0.8em]\n\\mathbf{\\text{Slope } m: } & \\mathbf{-\\frac{3}{2}} \\quad (\\text{Down 3, Right 2})\n\\end{aligned}$$",
        "pitfall": "**Solving with fractions:** When $\\frac{3}{2}x = -3$, multiply both sides by the reciprocal $\\frac{2}{3}$: $x = -3 \\cdot \\frac{2}{3} = -2$.",
        "script": "[Prof. Park] In Example 3C, the $y$-intercept is right in front of us: $(0, -3)$. Setting $y=0$ gives $x = -2$.\n\n[TA Sora] We plot $(-2, 0)$ and $(0, -3)$ and connect them with a line with negative slope $-\\frac{3}{2}$!",
        "graph": {
            "xMin": -6, "xMax": 4, "yMin": -6, "yMax": 3,
            "title": "Graph of y = -3/2x - 3",
            "points": [
                {"x": -2, "y": 0, "label": "x-int (-2, 0)", "color": "#f59e0b"},
                {"x": 0, "y": -3, "label": "y-int (0, -3)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": -1.5, "yIntercept": -3, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = -3/2x - 3"}
            ]
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.1 Example 3D: Direct Variation y = 2x",
        "subtitle": "Unit 2 • Lecture 19 • Section 2.1 Example 3D (Workbook p. 36)",
        "detail": "Lecture 19: Advanced Intercepts & Special Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3D (Workbook p. 36)\nFind the $x$- and $y$-intercepts algebraically for:\n$$\\mathbf{y = 2x}$$\nWhat happens when both intercepts are $(0, 0)$? How do you graph the line?",
        "solution": "$$\\begin{aligned}\n\\mathbf{y\\text{-intercept: }} & x = 0 \\implies y = 2(0) = 0 \\implies \\mathbf{(0, 0)} \\\\[0.5em]\n\\mathbf{x\\text{-intercept: }} & y = 0 \\implies 2x = 0 \\implies x = 0 \\implies \\mathbf{(0, 0)} \\\\[0.8em]\n\\text{Second Point: } & \\text{Use slope } m = \\frac{2}{1} \\text{ from } (0, 0): \\\\\n& \\text{Rise } +2, \\text{ Run } +1 \\implies \\mathbf{(1, 2)} \\\\\n& \\text{Or choose } x = 2 \\implies y = 2(2) = 4 \\implies \\mathbf{(2, 4)}\n\\end{aligned}$$",
        "pitfall": "**When intercepts coincide:** If both intercepts are $(0, 0)$, the intercept method only gives ONE point. You MUST pick another $x$-value (or use slope) to get a second point!",
        "script": "[Prof. Park] When $b = 0$, the line passes directly through the origin $(0, 0)$. Both intercepts are the same point!\n\n[TA Sora] Exactly. So we use the slope $m = 2$: start at $(0, 0)$, go UP 2 and RIGHT 1 to find $(1, 2)$!",
        "graph": {
            "xMin": -4, "xMax": 6, "yMin": -4, "yMax": 8,
            "title": "Direct Variation: y = 2x (Passes through Origin)",
            "points": [
                {"x": 0, "y": 0, "label": "Origin (0, 0)", "color": "#10b981"},
                {"x": 1, "y": 2, "label": "(1, 2)", "color": "#38bdf8"},
                {"x": 2, "y": 4, "label": "(2, 4)", "color": "#f59e0b"}
            ],
            "lines": [
                {"slope": 2, "yIntercept": 0, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = 2x"}
            ]
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.1 Example 3E: Horizontal Line y = -2",
        "subtitle": "Unit 2 • Lecture 19 • Section 2.1 Example 3E (Workbook p. 37)",
        "detail": "Lecture 19: Advanced Intercepts & Special Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Horizontal Lines: Example 3E (Workbook p. 37)\nFind the intercepts and slope-intercept form for:\n$$\\mathbf{y = -2}$$\n- State the $x$-intercept (if any).\n- State the $y$-intercept.\n- Identify the slope.",
        "solution": "$$\\begin{aligned}\n\\mathbf{y\\text{-intercept: }} & x = 0 \\implies y = -2 \\implies \\mathbf{(0, -2)} \\\\[0.5em]\n\\mathbf{x\\text{-intercept: }} & \\text{Set } y = 0 \\implies 0 = -2 \\; (\\text{contradiction}) \\implies \\mathbf{\\text{None}} \\\\[0.5em]\n\\text{Slope-Intercept: } & y = 0x - 2 \\implies \\mathbf{m = 0} \\\\[0.5em]\n\\text{Orientation: } & \\mathbf{\\text{Horizontal Line at height } y = -2}\n\\end{aligned}$$",
        "pitfall": "**No x-intercept:** A horizontal line parallel to the $x$-axis never crosses the $x$-axis. It has NO $x$-intercept!",
        "script": "[Prof. Park] $y = -2$ has no $x$ variable. That means $y$ is $-2$ for every possible value of $x$.\n\n[TA Sora] The slope is $0$. It never touches the $x$-axis, so there is no $x$-intercept, but the $y$-intercept is $(0, -2)$!",
        "graph": {
            "xMin": -6, "xMax": 6, "yMin": -6, "yMax": 4,
            "title": "Horizontal Line: y = -2 (Slope m = 0)",
            "points": [
                {"x": 0, "y": -2, "label": "y-int (0, -2)", "color": "#10b981"},
                {"x": -3, "y": -2, "label": "(-3, -2)", "color": "#38bdf8"},
                {"x": 3, "y": -2, "label": "(3, -2)", "color": "#f59e0b"}
            ],
            "lines": [
                {"horizontal": -2, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = -2"}
            ]
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.1 Example 3F: Vertical Line x = 3",
        "subtitle": "Unit 2 • Lecture 19 • Section 2.1 Example 3F (Workbook p. 37)",
        "detail": "Lecture 19: Advanced Intercepts & Special Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Vertical Lines: Example 3F (Workbook p. 37)\nFind the intercepts and slope-intercept form for:\n$$\\mathbf{x = 3}$$\n- State the $x$-intercept.\n- State the $y$-intercept (if any).\n- Can this equation be written in slope-intercept form $y = mx + b$?",
        "solution": "$$\\begin{aligned}\n\\mathbf{x\\text{-intercept: }} & \\mathbf{(3, 0)} \\\\[0.5em]\n\\mathbf{y\\text{-intercept: }} & \\text{Set } x = 0 \\implies 0 = 3 \\; (\\text{contradiction}) \\implies \\mathbf{\\text{None}} \\\\[0.5em]\n\\mathbf{\\text{Slope: }} & \\mathbf{\\text{Undefined (Division by zero in run)}} \\\\[0.5em]\n\\mathbf{\\text{Note: }} & \\mathbf{\\text{Vertical lines CANNOT be written in } y = mx + b!}\n\\end{aligned}$$",
        "pitfall": "**Vertical lines are not functions:** Because slope is undefined, you CANNOT write $x = 3$ in $y = mx + b$ format!",
        "script": "[Prof. Park] In Example 3F, $x = 3$. This is a vertical line. Its slope is undefined because there is zero horizontal run.\n\n[TA Sora] It crosses the $x$-axis at $(3, 0)$ and never crosses the $y$-axis!",
        "graph": {
            "xMin": -2, "xMax": 8, "yMin": -6, "yMax": 6,
            "title": "Vertical Line: x = 3 (Slope Undefined)",
            "points": [
                {"x": 3, "y": 0, "label": "x-int (3, 0)", "color": "#f59e0b"},
                {"x": 3, "y": 4, "label": "(3, 4)", "color": "#38bdf8"},
                {"x": 3, "y": -4, "label": "(3, -4)", "color": "#ec4899"}
            ],
            "lines": [
                {"vertical": 3, "color": "#ec4899", "strokeWidth": 2.5, "label": "x = 3"}
            ]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Sora's Memory Anchor",
        "title": "The Famous 'HOY VUX' Mnemonic for Special Lines",
        "subtitle": "Unit 2 • Lecture 19 • Section 2.1 (Workbook p. 37)",
        "detail": "Lecture 19: Advanced Intercepts & Special Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### The 'HOY VUX' Rule (Workbook p. 37)\nHow can you permanently remember the equations and slopes of horizontal and vertical lines?\n- **H - O - Y:**\n  - **H:** Horizontal line\n  - **O:** Zero slope ($m = 0$)\n  - **Y:** Equation is $\\mathbf{y = c}$\n- **V - U - X:**\n  - **V:** Vertical line\n  - **U:** Undefined slope ($m = \\text{undefined}$)\n  - **X:** Equation is $\\mathbf{x = c}$",
        "solution": "$$\\begin{array}{|c|c|c|c|c|}\n\\hline\n\\textbf{Mnemonic} & \\textbf{Line Type} & \\textbf{Slope } (m) & \\textbf{Equation Form} & \\textbf{Intercepts} \\\\\n\\hline\n\\textbf{HOY} & \\text{Horizontal} & 0 & y = c & (0, c), \\text{ No } x\\text{-int} \\\\\n\\hline\n\\textbf{VUX} & \\text{Vertical} & \\text{Undefined} & x = c & (c, 0), \\text{ No } y\\text{-int} \\\\\n\\hline\n\\end{array}$$",
        "pitfall": "**Never say 'no slope':** Say 'Zero slope' for horizontal, and 'Undefined slope' for vertical. 'No slope' is ambiguous and loses exam points!",
        "script": "[Prof. Park] Sora, share the famous Bozeman student trick for horizontal and vertical lines!\n\n[TA Sora] HOY VUX! HOY: Horizontal, Zero slope, Y equals. VUX: Vertical, Undefined slope, X equals! Memorize HOY VUX and you will never miss these on the exam!"
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Synthesis",
        "title": "Intersecting Special Lines: y = -2 and x = 3",
        "subtitle": "Unit 2 • Lecture 19 • Section 2.1 Comparison",
        "detail": "Lecture 19: Advanced Intercepts & Special Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Intersection of Horizontal & Vertical Lines\nPlot both $y = -2$ (from Example 3E) and $x = 3$ (from Example 3F) on the same coordinate grid:\n- State the point where these two perpendicular lines intersect.\n- Explain how their coordinates relate to their equations.",
        "solution": "$$\\begin{aligned}\n\\text{Line 1: } & y = -2 \\quad (\\text{all points have } y = -2) \\\\\n\\text{Line 2: } & x = 3 \\quad (\\text{all points have } x = 3) \\\\[0.8em]\n\\mathbf{\\text{Intersection Point: }} & \\mathbf{(3, -2)} \\\\[0.5em]\n\\text{Angle of Intersection: } & \\mathbf{90^\\circ \\; (\\text{Perpendicular Lines})}\n\\end{aligned}$$",
        "pitfall": "**Direct coordinate match:** The intersection of $x = a$ and $y = b$ is ALWAYS the ordered pair $(a, b)$!",
        "script": "[Prof. Park] When horizontal line $y = -2$ meets vertical line $x = 3$, they cross at exactly $(3, -2)$ at a 90-degree angle.\n\n[TA Sora] Look at the grid: blue line horizontal, pink line vertical, meeting at the gold glowing intersection point $(3, -2)$!",
        "graph": {
            "xMin": -4, "xMax": 8, "yMin": -6, "yMax": 4,
            "title": "Intersection of y = -2 (HOY) and x = 3 (VUX) at (3, -2)",
            "points": [
                {"x": 3, "y": -2, "label": "Intersection (3, -2)", "color": "#f59e0b", "labelOffsetX": 8, "labelOffsetY": 14}
            ],
            "lines": [
                {"horizontal": -2, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = -2"},
                {"vertical": 3, "color": "#ec4899", "strokeWidth": 2.5, "label": "x = 3"}
            ]
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 2.1 Mastery Review",
        "subtitle": "Unit 2 • Lecture 19 • Section 2.1 Wrap-up",
        "detail": "Lecture 19: Advanced Intercepts & Special Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Section 2.1 Graphing Summary\n- **Table Method:** Pick $x=0$, $y=0$, and a third checkpoint.\n- **Intercept Method:** Plot $(a, 0)$ and $(0, b)$.\n- **Slope-Intercept:** $y = mx + b$, begin at $(0, b)$ and move by $\\frac{\\text{Rise}}{\\text{Run}}$.\n- **HOY:** $y = c$, Horizontal, Slope = 0.\n- **VUX:** $x = c$, Vertical, Slope = Undefined.",
        "solution": "$$\\mathbf{\\text{Section 2.1 Mastered! Next Up: Section 2.2 — The Slope of a Line!}}$$",
        "pitfall": "**Exam Checklist:** Always check if a problem specifies 'use the intercept method' or 'use slope-intercept form'!",
        "script": "[Prof. Park] Excellent job conquering Section 2.1! You can now graph any linear equation in two variables.\n\n[TA Sora] In Lecture 20, we explore the deep mathematics of slope $m = \\frac{\\text{Rise}}{\\text{Run}}$!"
    }
]

# L20: Section 2.2 Part 1 (Workbook pp. 38 - 39) - 9 slides
data_16_20[20] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "The Slope of a Line: Rise Over Run & Formula",
        "subtitle": "Unit 2 • Lecture 20 • Section 2.2 (Workbook p. 38)",
        "detail": "Lecture 20: Slope of a Line & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Section 2.2: Slope of a Line (Workbook p. 38)\nSlope measures the **steepness and direction** of a straight line:\n$$\\mathbf{\\text{Slope } = m = \\frac{\\text{Rise}}{\\text{Run}} = \\frac{\\text{Change in } y}{\\text{Change in } x} = \\frac{y_2 - y_1}{x_2 - x_1}}$$\n- **Positive Slope ($m > 0$):** Line rises from left to right.\n- **Negative Slope ($m < 0$):** Line falls from left to right.\n- **Zero Slope ($m = 0$):** Horizontal line.\n- **Undefined Slope:** Vertical line (division by zero).",
        "solution": "$$\\begin{aligned}\n\\text{Formula: } & m = \\frac{y_2 - y_1}{x_2 - x_1} \\\\[0.5em]\n\\text{Numerator: } & \\Delta y = y_2 - y_1 \\quad (\\text{vertical rise/fall}) \\\\\n\\text{Denominator: } & \\Delta x = x_2 - x_1 \\quad (\\text{horizontal run right})\n\\end{aligned}$$",
        "pitfall": "**Y over X:** Slope is ALWAYS change in $y$ over change in $x$. Never flip it to $\\frac{x_2 - x_1}{y_2 - y_1}$!",
        "script": "[Prof. Park] Welcome to Lecture 20! Today we master Slope: the single most important concept in developmental algebra.\n\n[TA Sora] Remember: Rise over Run! $y$ is the elevator on top, $x$ is the sidewalk on the bottom!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 1A: Slope between (2, 3) and (5, 7)",
        "subtitle": "Unit 2 • Lecture 20 • Section 2.2 Example 1A (Workbook p. 38)",
        "detail": "Lecture 20: Slope of a Line & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1A (Workbook p. 38)\nFind the slope of the line that passes through the two given points:\n$$\\mathbf{(2, 3) \\quad \\text{and} \\quad (5, 7)}$$\n- Label $(x_1, y_1)$ and $(x_2, y_2)$.\n- Apply the slope formula and simplify.\n- State the rise and run.",
        "solution": "$$\\begin{aligned}\n\\text{Let } & (x_1, y_1) = (2, 3) \\quad \\text{and} \\quad (x_2, y_2) = (5, 7) \\\\[0.5em]\nm & = \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{7 - 3}{5 - 2} \\\\[0.5em]\n& = \\frac{4}{3} \\\\[0.5em]\n\\mathbf{\\text{Slope } m: } & \\mathbf{\\frac{4}{3}} \\quad (\\text{Rise } = +4, \\; \\text{Run } = +3)\n\\end{aligned}$$",
        "pitfall": "**Order consistency:** If you start with $y_2$ in the numerator, you MUST start with $x_2$ in the denominator!",
        "script": "[Prof. Park] In Example 1A, we compute $\\frac{7 - 3}{5 - 2} = \\frac{4}{3}$.\n\n[TA Sora] Rise is 4, Run is 3! On the coordinate plane, the gold slope triangle shows exactly 4 units up and 3 units right!",
        "graph": {
            "xMin": 0, "xMax": 8, "yMin": 0, "yMax": 9,
            "title": "Slope Triangle: m = 4/3 between (2, 3) and (5, 7)",
            "points": [
                {"x": 2, "y": 3, "label": "(2, 3)", "color": "#f59e0b"},
                {"x": 5, "y": 7, "label": "(5, 7)", "color": "#38bdf8"}
            ],
            "lines": [
                {"p1": [2, 3], "p2": [5, 7], "color": "#38bdf8", "strokeWidth": 2.5, "label": "m = 4/3"}
            ],
            "slopeTriangle": {"x1": 2, "y1": 3, "x2": 5, "y2": 7, "rise": 4, "run": 3}
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 1B: Slope between (3, -4) and (-2, -8)",
        "subtitle": "Unit 2 • Lecture 20 • Section 2.2 Example 1B (Workbook p. 38)",
        "detail": "Lecture 20: Slope of a Line & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1B (Workbook p. 38)\nFind the slope of the line that passes through the two given points:\n$$\\mathbf{(3, -4) \\quad \\text{and} \\quad (-2, -8)}$$\n- Watch the double negatives carefully when subtracting!\n- Simplify the fraction to lowest terms.",
        "solution": "$$\\begin{aligned}\n\\text{Let } & (x_1, y_1) = (3, -4) \\quad \\text{and} \\quad (x_2, y_2) = (-2, -8) \\\\[0.5em]\nm & = \\frac{-8 - (-4)}{-2 - 3} \\\\[0.5em]\n& = \\frac{-8 + 4}{-5} = \\frac{-4}{-5} \\\\[0.5em]\n\\mathbf{\\text{Slope } m: } & \\mathbf{\\frac{4}{5}}\n\\end{aligned}$$",
        "pitfall": "**Double negative sign trap:** $-8 - (-4) = -8 + 4 = -4$. And $\\frac{-4}{-5} = +\\frac{4}{5}$. A negative divided by a negative is positive!",
        "script": "[Prof. Park] In Example 1B, double negatives appear in both numerator and denominator.\n\n[TA Sora] $-8 - (-4)$ becomes $-4$, and $-2 - 3$ becomes $-5$. Negative divided by negative is positive $\\frac{4}{5}$!",
        "graph": {
            "xMin": -5, "xMax": 6, "yMin": -10, "yMax": 2,
            "title": "Slope Triangle: m = 4/5 between (-2, -8) and (3, -4)",
            "points": [
                {"x": -2, "y": -8, "label": "(-2, -8)", "color": "#ec4899"},
                {"x": 3, "y": -4, "label": "(3, -4)", "color": "#38bdf8"}
            ],
            "lines": [
                {"p1": [-2, -8], "p2": [3, -4], "color": "#38bdf8", "strokeWidth": 2.5, "label": "m = 4/5"}
            ],
            "slopeTriangle": {"x1": -2, "y1": -8, "x2": 3, "y2": -4, "rise": 4, "run": 5}
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 1C: Slope between (3, 7) and (3, -10)",
        "subtitle": "Unit 2 • Lecture 20 • Section 2.2 Example 1C (Workbook p. 38)",
        "detail": "Lecture 20: Slope of a Line & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1C (Workbook p. 38)\nFind the slope of the line that passes through the two given points:\n$$\\mathbf{(3, 7) \\quad \\text{and} \\quad (3, -10)}$$\n- What happens to the denominator $x_2 - x_1$?\n- State the value of the slope.",
        "solution": "$$\\begin{aligned}\nm & = \\frac{-10 - 7}{3 - 3} \\\\[0.5em]\n& = \\frac{-17}{0} \\\\[0.5em]\n\\mathbf{\\text{Slope } m: } & \\mathbf{\\text{Undefined}} \\\\[0.5em]\n\\text{Line Type: } & \\mathbf{\\text{Vertical line } x = 3}\n\\end{aligned}$$",
        "pitfall": "**Division by zero is undefined:** When the denominator is $0$, the slope is UNDEFINED. It is NOT zero! (Think of VUX: Vertical = Undefined = X).",
        "script": "[Prof. Park] In Example 1C, both $x$-coordinates are 3. The denominator is $3 - 3 = 0$.\n\n[TA Sora] You can never divide by zero! The slope is undefined, which confirms this is a vertical line $x = 3$!",
        "graph": {
            "xMin": -2, "xMax": 8, "yMin": -12, "yMax": 10,
            "title": "Vertical Line x = 3: Undefined Slope",
            "points": [
                {"x": 3, "y": 7, "label": "(3, 7)", "color": "#10b981"},
                {"x": 3, "y": -10, "label": "(3, -10)", "color": "#ec4899"}
            ],
            "lines": [
                {"vertical": 3, "color": "#ec4899", "strokeWidth": 2.5, "label": "x = 3"}
            ]
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 1D: Slope between (-2, -5) and (3, -5)",
        "subtitle": "Unit 2 • Lecture 20 • Section 2.2 Example 1D (Workbook p. 38)",
        "detail": "Lecture 20: Slope of a Line & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1D (Workbook p. 38)\nFind the slope of the line that passes through the two given points:\n$$\\mathbf{(-2, -5) \\quad \\text{and} \\quad (3, -5)}$$\n- What happens to the numerator $y_2 - y_1$?\n- State the value of the slope.",
        "solution": "$$\\begin{aligned}\nm & = \\frac{-5 - (-5)}{3 - (-2)} \\\\[0.5em]\n& = \\frac{-5 + 5}{3 + 2} = \\frac{0}{5} \\\\[0.5em]\n\\mathbf{\\text{Slope } m: } & \\mathbf{0} \\\\[0.5em]\n\\text{Line Type: } & \\mathbf{\\text{Horizontal line } y = -5}\n\\end{aligned}$$",
        "pitfall": "**Zero in numerator vs denominator:** $\\frac{0}{5} = 0$ (perfectly fine, zero slope). $\\frac{5}{0} = \\text{Undefined}$ (division by zero error)!",
        "script": "[Prof. Park] In Example 1D, the $y$-coordinates are both $-5$. The numerator is $-5 - (-5) = 0$.\n\n[TA Sora] Zero divided by 5 is 0! A slope of 0 means a perfectly flat horizontal line $y = -5$ (HOY)!",
        "graph": {
            "xMin": -6, "xMax": 6, "yMin": -8, "yMax": 2,
            "title": "Horizontal Line y = -5: Slope m = 0",
            "points": [
                {"x": -2, "y": -5, "label": "(-2, -5)", "color": "#38bdf8"},
                {"x": 3, "y": -5, "label": "(3, -5)", "color": "#f59e0b"}
            ],
            "lines": [
                {"horizontal": -5, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = -5"}
            ]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 1E: Fraction Coordinates",
        "subtitle": "Unit 2 • Lecture 20 • Section 2.2 Example 1E (Workbook p. 38)",
        "detail": "Lecture 20: Slope of a Line & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1E: Fraction Coordinates (Workbook p. 38)\nFind the slope of the line passing through:\n$$\\mathbf{\\left(\\frac{4}{3}, \\frac{1}{3}\\right) \\quad \\text{and} \\quad \\left(-\\frac{3}{5}, \\frac{7}{5}\\right)}$$\n- Subtract the $y$-coordinates using a common denominator.\n- Subtract the $x$-coordinates using a common denominator.\n- Simplify the complex fraction.",
        "solution": "$$\\begin{aligned}\n\\Delta y & = \\frac{7}{5} - \\frac{1}{3} = \\frac{21}{15} - \\frac{5}{15} = \\frac{16}{15} \\\\[0.6em]\n\\Delta x & = -\\frac{3}{5} - \\frac{4}{3} = -\\frac{9}{15} - \\frac{20}{15} = -\\frac{29}{15} \\\\[0.6em]\nm & = \\frac{\\frac{16}{15}}{-\\frac{29}{15}} = \\frac{16}{15} \\cdot \\left(-\\frac{15}{29}\\right) = \\mathbf{-\\frac{16}{29}}\n\\end{aligned}$$",
        "pitfall": "**Simplifying complex fractions:** Multiply by the reciprocal of the denominator! Notice the LCD 15 cancels out beautifully.",
        "script": "[Prof. Park] In Example 1E, we use our Unit 1 fraction skills! Finding LCD 15 in both numerator and denominator makes the 15s cancel.\n\n[TA Sora] Leaving a final clean slope of $-\\frac{16}{29}$!",
        "graph": {
            "xMin": -2, "xMax": 3, "yMin": -1, "yMax": 3,
            "title": "Slope with Fractional Coordinates: m = -16/29",
            "points": [
                {"x": 4/3, "y": 1/3, "label": "(4/3, 1/3)", "color": "#f59e0b"},
                {"x": -3/5, "y": 7/5, "label": "(-3/5, 7/5)", "color": "#38bdf8"}
            ],
            "lines": [
                {"p1": [-3/5, 7/5], "p2": [4/3, 1/3], "color": "#38bdf8", "strokeWidth": 2}
            ]
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 2A: Counting Slope from a Graph",
        "subtitle": "Unit 2 • Lecture 20 • Section 2.2 Example 2A (Workbook p. 39)",
        "detail": "Lecture 20: Slope of a Line & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2A (Workbook p. 39)\nFind the slope of the line shown in the graph:\n- Identify two grid intersections: $(0, 1)$ and $(3, 3)$.\n- Count the vertical rise from the first point to the second.\n- Count the horizontal run to the right.\n- Write the slope $m = \\frac{\\text{Rise}}{\\text{Run}}$.",
        "solution": "$$\\begin{aligned}\n\\text{Point 1: } & (0, 1) \\\\\n\\text{Point 2: } & (3, 3) \\\\[0.5em]\n\\text{Rise: } & 3 - 1 = \\mathbf{+2 \\text{ units (UP)}} \\\\\n\\text{Run: } & 3 - 0 = \\mathbf{+3 \\text{ units (RIGHT)}} \\\\[0.8em]\n\\mathbf{\\text{Slope } m: } & \\mathbf{\\frac{2}{3}}\n\\end{aligned}$$",
        "pitfall": "**Finding clean grid points:** When reading a slope from a graph, always pick points where the line crosses the grid corners exactly, avoiding fractional estimates!",
        "script": "[Prof. Park] In Example 2, we find slope directly from the graph by counting grid squares.\n\n[TA Sora] From $(0, 1)$ to $(3, 3)$, count UP 2 squares, then RIGHT 3 squares. The slope is positive $\\frac{2}{3}$!",
        "graph": {
            "xMin": -3, "xMax": 6, "yMin": -2, "yMax": 5,
            "title": "Example 2A: Counting Rise = 2, Run = 3 (m = 2/3)",
            "points": [
                {"x": 0, "y": 1, "label": "(0, 1)", "color": "#10b981"},
                {"x": 3, "y": 3, "label": "(3, 3)", "color": "#38bdf8"}
            ],
            "lines": [
                {"slope": 2/3, "yIntercept": 1, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "slopeTriangle": {"x1": 0, "y1": 1, "x2": 3, "y2": 3, "rise": 2, "run": 3}
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 2B: Counting Negative Slope from Graph",
        "subtitle": "Unit 2 • Lecture 20 • Section 2.2 Example 2B (Workbook p. 39)",
        "detail": "Lecture 20: Slope of a Line & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2B (Workbook p. 39)\nFind the slope of the line shown in the graph:\n- Identify two grid intersections: $(0, 4)$ and $(2, 0)$.\n- Determine whether the line is rising or falling from left to right.\n- Count the rise and run to calculate $m$.",
        "solution": "$$\\begin{aligned}\n\\text{Point 1: } & (0, 4) \\\\\n\\text{Point 2: } & (2, 0) \\\\[0.5em]\n\\text{Rise: } & 0 - 4 = \\mathbf{-4 \\text{ units (DOWN 4)}} \\\\\n\\text{Run: } & 2 - 0 = \\mathbf{+2 \\text{ units (RIGHT 2)}} \\\\[0.8em]\nm & = \\frac{-4}{2} = \\mathbf{-2}\n\\end{aligned}$$",
        "pitfall": "**Downhill lines must have negative slope:** If the line goes downward as you read from left to right, your slope MUST be negative!",
        "script": "[Prof. Park] In Example 2B, the line heads downhill. We drop 4 units and move right 2 units.\n\n[TA Sora] $\\frac{-4}{2} = -2$. The negative sign is crucial!",
        "graph": {
            "xMin": -2, "xMax": 5, "yMin": -2, "yMax": 6,
            "title": "Example 2B: Counting Negative Slope (m = -2)",
            "points": [
                {"x": 0, "y": 4, "label": "(0, 4)", "color": "#10b981"},
                {"x": 2, "y": 0, "label": "(2, 0)", "color": "#f59e0b"}
            ],
            "lines": [
                {"slope": -2, "yIntercept": 4, "color": "#ec4899", "strokeWidth": 2.5}
            ],
            "slopeTriangle": {"x1": 0, "y1": 4, "x2": 2, "y2": 0, "rise": -4, "run": 2}
        }
    },
    {
        "num": 9,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 2.2 Part 1 Mastery Summary",
        "subtitle": "Unit 2 • Lecture 20 • Section 2.2 Wrap-up",
        "detail": "Lecture 20: Slope of a Line & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Four Types of Slope on the Coordinate Plane\n- **Positive ($m > 0$):** Slants uphill / rises to the right.\n- **Negative ($m < 0$):** Slants downhill / falls to the right.\n- **Zero ($m = 0$):** Horizontal line (flat ground).\n- **Undefined:** Vertical line (vertical cliff, division by zero).",
        "solution": "$$\\mathbf{\\text{Lecture 20 Complete! Next Up: Section 2.2 Part 2 — Parallel \\& Perpendicular Slopes!}}$$",
        "pitfall": "**Cross-check your algebra:** Always glance at your graph: if the line slants up, a negative algebraic answer means a sign error occurred!",
        "script": "[Prof. Park] Fantastic job! We have mastered calculating and counting slope.\n\n[TA Sora] Next in Lecture 21, we examine how slopes tell us if two lines are parallel, perpendicular, or neither!"
    }
]

print("Lectures 16 to 20 generated successfully!")
