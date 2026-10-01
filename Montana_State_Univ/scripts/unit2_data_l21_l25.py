# Unit 2 Lectures 21 - 25 Data
# Faithful to M090 Workbook pp. 40 - 46

data_21_25 = {}

# L21: Section 2.2 Part 2 (Workbook p. 40) - 8 slides
data_21_25[21] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Parallel & Perpendicular Lines: Definitions & Slopes",
        "subtitle": "Unit 2 • Lecture 21 • Section 2.2 (Workbook p. 40)",
        "detail": "Lecture 21: Parallel & Perpendicular Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Parallel & Perpendicular Lines (Workbook p. 40)\n- **Parallel Lines:** Two lines that never intersect in a plane.\n  $$\\mathbf{m_1 = m_2 \\quad \\text{and} \\quad b_1 \\neq b_2}$$\n  *(Same slope, different $y$-intercepts)*\n- **Perpendicular Lines:** Two lines that intersect at a $90^\\circ$ right angle.\n  $$\\mathbf{m_1 \\cdot m_2 = -1 \\iff m_2 = -\\frac{1}{m_1}}$$\n  *(Slopes are opposite reciprocals)*",
        "solution": "$$\\begin{aligned}\n\\text{Parallel: } & m_1 = \\frac{2}{3} \\implies m_2 = \\frac{2}{3} \\\\[0.5em]\n\\text{Perpendicular: } & m_1 = \\frac{2}{3} \\implies m_2 = -\\frac{3}{2} \\quad (\\text{flip fraction and negate sign})\n\\end{aligned}$$",
        "pitfall": "**Both conditions for perpendicular:** Opposite reciprocal means TWO changes: change the sign (positive $\\leftrightarrow$ negative) AND flip the fraction upside-down!",
        "script": "[Prof. Park] Welcome to Lecture 21. How do we test if two lines are parallel or perpendicular without graphing them first?\n\n[TA Sora] By comparing their slopes! Parallel lines have identical slopes. Perpendicular lines have opposite reciprocal slopes whose product is $-1$!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 3: Comparing Slopes",
        "subtitle": "Unit 2 • Lecture 21 • Section 2.2 Example 3 (Workbook p. 40)",
        "detail": "Lecture 21: Parallel & Perpendicular Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3 (Workbook p. 40)\nDetermine if the two lines with the given slopes are **parallel, perpendicular, or neither**:\n$$\\mathbf{m_1 = \\frac{2}{5} \\quad \\text{and} \\quad m_2 = -\\frac{5}{2}}$$",
        "solution": "$$\\begin{aligned}\n\\text{Compare slopes: } & m_1 = \\frac{2}{5}, \\quad m_2 = -\\frac{5}{2} \\\\[0.5em]\n\\text{Check parallel: } & \\frac{2}{5} \\neq -\\frac{5}{2} \\implies \\text{Not parallel} \\\\[0.5em]\n\\text{Check product: } & m_1 \\cdot m_2 = \\left(\\frac{2}{5}\\right) \\left(-\\frac{5}{2}\\right) = -\\frac{10}{10} = \\mathbf{-1} \\\\[0.8em]\n\\mathbf{\\text{Conclusion: }} & \\mathbf{\\text{The lines are Perpendicular.}}\n\\end{aligned}$$",
        "pitfall": "**Neither case:** If $m_1 = \\frac{2}{5}$ and $m_2 = \\frac{5}{2}$ (same sign), they are NEITHER, because the product is $+1$, not $-1$!",
        "script": "[Prof. Park] In Example 3, $\\frac{2}{5}$ and $-\\frac{5}{2}$ are opposite reciprocals. When multiplied, they give $-1$.\n\n[TA Sora] Therefore, the two lines meet at a perfect 90-degree right angle and are perpendicular!"
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 4 (Step 1): Solving Line 1",
        "subtitle": "Unit 2 • Lecture 21 • Section 2.2 Example 4 (Workbook p. 40)",
        "detail": "Lecture 21: Parallel & Perpendicular Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4 (Workbook p. 40)\nDetermine if the two lines are parallel, perpendicular, or neither:\n$$\\text{Line 1: } \\mathbf{x + y = 5}$$\n$$\\text{Line 2: } \\mathbf{-2x - 2y = 7}$$\nSolve Line 1 for $y$ to determine its slope $m_1$ and $y$-intercept $b_1$.",
        "solution": "$$\\begin{aligned}\nx + y & = 5 \\\\[0.5em]\ny & = -x + 5 \\\\[0.8em]\n\\mathbf{\\text{Slope } m_1: } & \\mathbf{-1} \\\\\n\\mathbf{y\\text{-intercept } b_1: } & \\mathbf{(0, 5)}\n\\end{aligned}$$",
        "pitfall": "**Implicit coefficient of 1:** In $y = -x + 5$, the slope is $m = -1$, NOT $0$ or just the minus sign!",
        "script": "[Prof. Park] In Example 4, we must convert both standard equations into slope-intercept form.\n\n[TA Sora] Line 1 solves immediately to $y = -x + 5$. The slope is $m_1 = -1$."
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 4 (Step 2): Solving Line 2",
        "subtitle": "Unit 2 • Lecture 21 • Section 2.2 Example 4 (Workbook p. 40)",
        "detail": "Lecture 21: Parallel & Perpendicular Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4 Step 2 (Workbook p. 40)\nNow solve Line 2 for $y$:\n$$\\mathbf{-2x - 2y = 7}$$\n- Add $2x$ to both sides.\n- Divide each term by $-2$.\n- Identify slope $m_2$ and $y$-intercept $b_2$.",
        "solution": "$$\\begin{aligned}\n-2x - 2y & = 7 \\\\[0.5em]\n-2y & = 2x + 7 \\quad (\\text{add } 2x) \\\\[0.5em]\ny & = \\frac{2x + 7}{-2} = \\frac{2}{-2}x + \\frac{7}{-2} \\\\[0.5em]\n\\mathbf{y} & = \\mathbf{-x - \\frac{7}{2} = -x - 3.5} \\\\[0.8em]\n\\mathbf{\\text{Slope } m_2: } & \\mathbf{-1} \\\\\n\\mathbf{y\\text{-intercept } b_2: } & \\mathbf{\\left(0, -\\frac{7}{2}\\right) = (0, -3.5)}\n\\end{aligned}$$",
        "pitfall": "**Watch signs during division:** $2x / (-2) = -1x$, and $7 / (-2) = -3.5$.",
        "script": "[Prof. Park] For Line 2, dividing by $-2$ gives $y = -x - 3.5$. Its slope is also $-1$!\n\n[TA Sora] Both lines have slope $-1$, but Line 1 has intercept $(0, 5)$ and Line 2 has intercept $(0, -3.5)$."
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 4 (Conclusion & Graph): Parallel Lines",
        "subtitle": "Unit 2 • Lecture 21 • Section 2.2 Example 4 Graph (Workbook p. 40)",
        "detail": "Lecture 21: Parallel & Perpendicular Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4 Conclusion & Graph\nCompare slopes $m_1 = -1$ and $m_2 = -1$ with intercepts $b_1 = 5$ and $b_2 = -3.5$:\n- State the final relationship.\n- Visualize both lines on the Cartesian plane.",
        "solution": "$$\\begin{aligned}\nm_1 = -1 & = m_2 = -1 \\quad (\\text{slopes are identical}) \\\\\nb_1 = 5 & \\neq b_2 = -3.5 \\quad (\\text{different } y\\text{-intercepts}) \\\\[0.8em]\n\\mathbf{\\text{Conclusion: }} & \\mathbf{\\text{The two lines are strictly PARALLEL.}}\n\\end{aligned}$$",
        "pitfall": "**What if both slopes and intercepts were identical?** If $m_1 = m_2$ AND $b_1 = b_2$, the lines would be the SAME line (coincident), not parallel!",
        "script": "[Prof. Park] Look at the graph. Both lines slant downward at the exact same rate. They will never touch.\n\n[TA Sora] The blue line is $x+y=5$, and the pink line is $-2x-2y=7$. A classic pair of parallel lines!",
        "graph": {
            "xMin": -6, "xMax": 8, "yMin": -6, "yMax": 8,
            "title": "Parallel Lines: x + y = 5 and -2x - 2y = 7 (m = -1)",
            "points": [
                {"x": 0, "y": 5, "label": "(0, 5)", "color": "#38bdf8"},
                {"x": 0, "y": -3.5, "label": "(0, -3.5)", "color": "#ec4899"}
            ],
            "lines": [
                {"slope": -1, "yIntercept": 5, "color": "#38bdf8", "strokeWidth": 2.5, "label": "x + y = 5"},
                {"slope": -1, "yIntercept": -3.5, "color": "#ec4899", "strokeWidth": 2.5, "label": "-2x - 2y = 7"}
            ]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 5 (Step 1): Solving Line 1",
        "subtitle": "Unit 2 • Lecture 21 • Section 2.2 Example 5 (Workbook p. 40)",
        "detail": "Lecture 21: Parallel & Perpendicular Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5 (Workbook p. 40)\nDetermine if the two lines are parallel, perpendicular, or neither:\n$$\\text{Line 1: } \\mathbf{2y = x - 2}$$\n$$\\text{Line 2: } \\mathbf{y = -2x - 4}$$\nSolve Line 1 for $y$ and determine its slope $m_1$.",
        "solution": "$$\\begin{aligned}\n2y & = x - 2 \\\\[0.5em]\ny & = \\frac{1}{2}x - \\frac{2}{2} \\\\[0.5em]\n\\mathbf{y} & = \\mathbf{\\frac{1}{2}x - 1} \\\\[0.8em]\n\\mathbf{\\text{Slope } m_1: } & \\mathbf{\\frac{1}{2}} \\\\\n\\mathbf{y\\text{-intercept } b_1: } & \\mathbf{(0, -1)}\n\\end{aligned}$$",
        "pitfall": "**Coefficient in front of x:** When dividing $x$ by $2$, the coefficient is $\\frac{1}{2}$, NOT $2$!",
        "script": "[Prof. Park] In Example 5, Line 1 is $2y = x - 2$. Dividing by 2 yields $y = \\frac{1}{2}x - 1$.\n\n[TA Sora] Slope $m_1 = \\frac{1}{2}$. Now let's look at Line 2!"
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.2 Example 5 (Step 2 & Graph): Perpendicular Lines",
        "subtitle": "Unit 2 • Lecture 21 • Section 2.2 Example 5 Graph (Workbook p. 40)",
        "detail": "Lecture 21: Parallel & Perpendicular Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5 Conclusion & Graph (Workbook p. 40)\nCompare the slopes:\n$$\\mathbf{m_1 = \\frac{1}{2} \\quad \\text{and} \\quad m_2 = -2}$$\n- Calculate the product $m_1 \\cdot m_2$.\n- Graph both lines on the Cartesian plane to verify the $90^\\circ$ intersection.",
        "solution": "$$\\begin{aligned}\nm_1 \\cdot m_2 & = \\left(\\frac{1}{2}\\right) (-2) = -\\frac{2}{2} = \\mathbf{-1} \\\\[0.8em]\n\\mathbf{\\text{Conclusion: }} & \\mathbf{\\text{The lines are strictly PERPENDICULAR.}} \\\\[0.5em]\n\\text{Intersection Point: } & \\frac{1}{2}x - 1 = -2x - 4 \\implies 2.5x = -3 \\implies \\mathbf{(-1.2, -1.6)}\n\\end{aligned}$$",
        "pitfall": "**Opposite reciprocals product:** Two non-vertical lines are perpendicular if and only if their slopes multiply to $-1$!",
        "script": "[Prof. Park] Look at the Cartesian grid. The blue line has slope $\\frac{1}{2}$, and the pink line has slope $-2$.\n\n[TA Sora] They cross at a crisp right angle ($90^\\circ$)! That is the visual hallmark of perpendicular lines.",
        "graph": {
            "xMin": -6, "xMax": 6, "yMin": -6, "yMax": 6,
            "title": "Perpendicular Lines: y = 1/2x - 1 and y = -2x - 4",
            "points": [
                {"x": 0, "y": -1, "label": "y-int (0, -1)", "color": "#38bdf8"},
                {"x": 0, "y": -4, "label": "y-int (0, -4)", "color": "#ec4899"},
                {"x": -1.2, "y": -1.6, "label": "90° Intersection", "color": "#f59e0b"}
            ],
            "lines": [
                {"slope": 0.5, "yIntercept": -1, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = 1/2x - 1"},
                {"slope": -2, "yIntercept": -4, "color": "#ec4899", "strokeWidth": 2.5, "label": "y = -2x - 4"}
            ]
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 2.2 Mastery: Parallel & Perpendicular Tests",
        "subtitle": "Unit 2 • Lecture 21 • Section 2.2 Wrap-up",
        "detail": "Lecture 21: Parallel & Perpendicular Lines",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Master Slope Comparison Rules\n- **Parallel:** $m_1 = m_2$ (Same slope, different intercepts)\n- **Perpendicular:** $m_1 \\cdot m_2 = -1$ (Opposite reciprocals)\n- **Special case:** Any horizontal line ($m=0$) is perpendicular to any vertical line ($m=\\text{undefined}$)\n- **Neither:** Any lines that fail both parallel and perpendicular criteria.",
        "solution": "$$\\mathbf{\\text{Section 2.2 Mastered! Next Up: Section 2.3 — Finding Equations of Lines!}}$$",
        "pitfall": "**Beware of identical signs:** $\\frac{3}{4}$ and $\\frac{4}{3}$ are reciprocals, but NOT opposite reciprocals! Their product is $+1$, so they are NEITHER!",
        "script": "[Prof. Park] Congratulations! You have conquered Section 2.2 and the theory of slopes.\n\n[TA Sora] In Lecture 22, we learn the Point-Slope formula to create our own line equations!"
    }
]

# L22: Section 2.3 Part 1 (Workbook pp. 41 - 42) - 8 slides
data_21_25[22] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Section 2.3: Point-Slope Form of a Line",
        "subtitle": "Unit 2 • Lecture 22 • Section 2.3 (Workbook p. 41)",
        "detail": "Lecture 22: Finding Linear Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Point-Slope Form (Workbook p. 41)\n$$\\mathbf{y - y_1 = m(x - x_1)}$$\n- $m$ is the slope.\n- $(x_1, y_1)$ is **any point** on the line.\n- Can be used to find the equation of **any non-vertical line**!\n- Once substituted, distribute $m$ and solve for $y$ to get slope-intercept form $y = mx + b$.",
        "solution": "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Identify slope } m \\text{ and given point } (x_1, y_1). \\\\\n\\text{Step 2: } & \\text{Substitute into } y - y_1 = m(x - x_1). \\\\\n\\text{Step 3: } & \\text{Distribute } m \\text{ across the parentheses.} \\\\\n\\text{Step 4: } & \\text{Add } y_1 \\text{ to both sides to isolate } y = mx + b.\n\\end{aligned}$$",
        "pitfall": "**Minus sign in formula:** $y - y_1$ and $x - x_1$ contain subtraction signs. If $x_1$ is negative, $x - (-3)$ becomes $x + 3$!",
        "script": "[Prof. Park] Welcome to Section 2.3! If you know the slope and just one point on a line, Point-Slope Form builds the equation every single time.\n\n[TA Sora] It is derived directly from the slope formula by multiplying both sides by $(x - x_1)$!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.3 Example 1: Slope -4/3 and Y-Intercept (0, -3)",
        "subtitle": "Unit 2 • Lecture 22 • Section 2.3 Example 1 (Workbook p. 41)",
        "detail": "Lecture 22: Finding Linear Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 (Workbook p. 41)\nFind the equation of the line with a $y$-intercept of $(0, -3)$ and a slope of $m = -\\frac{4}{3}$.\n- Write the equation in slope-intercept form.\n- Graph the line on the Cartesian coordinate plane.",
        "solution": "$$\\begin{aligned}\n\\text{Given: } & m = -\\frac{4}{3}, \\quad b = -3 \\\\[0.5em]\n\\text{Direct substitution: } & y = mx + b \\\\[0.5em]\n\\mathbf{\\text{Equation: }} & \\mathbf{y = -\\frac{4}{3}x - 3}\n\\end{aligned}$$",
        "pitfall": "**Immediate answer when given y-intercept:** If the point is $(0, b)$, you don't even need point-slope! Just drop $m$ and $b$ directly into $y = mx + b$!",
        "script": "[Prof. Park] In Example 1, we are given the $y$-intercept $(0, -3)$ directly. We can plug $m = -\\frac{4}{3}$ and $b = -3$ straight into $y = mx + b$.\n\n[TA Sora] That gives $y = -\\frac{4}{3}x - 3$ instantly!",
        "graph": {
            "xMin": -6, "xMax": 4, "yMin": -8, "yMax": 3,
            "title": "Example 1: y = -4/3x - 3",
            "points": [
                {"x": 0, "y": -3, "label": "y-int (0, -3)", "color": "#10b981"},
                {"x": -3, "y": 1, "label": "(-3, 1)", "color": "#38bdf8"}
            ],
            "lines": [
                {"slope": -4/3, "yIntercept": -3, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = -4/3x - 3"}
            ]
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.3 Example 2: Slope -4/3 and X-Intercept (-3, 0)",
        "subtitle": "Unit 2 • Lecture 22 • Section 2.3 Example 2 (Workbook p. 41)",
        "detail": "Lecture 22: Finding Linear Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2 (Workbook p. 41)\nFind the equation of the line with $x$-intercept of $(-3, 0)$ and a slope of $m = -\\frac{4}{3}$.\n- Can you plug $-3$ in for $b$?\n- Use point-slope form $y - y_1 = m(x - x_1)$ to find the correct equation.",
        "solution": "$$\\begin{aligned}\n\\text{Given: } & (x_1, y_1) = (-3, 0), \\quad m = -\\frac{4}{3} \\\\[0.5em]\ny - y_1 & = m(x - x_1) \\\\[0.5em]\ny - 0 & = -\\frac{4}{3}(x - (-3)) \\\\[0.5em]\ny & = -\\frac{4}{3}(x + 3) = -\\frac{4}{3}x - \\left(\\frac{4}{3} \\cdot 3\\right) \\\\[0.5em]\n\\mathbf{y} & = \\mathbf{-\\frac{4}{3}x - 4}\n\\end{aligned}$$",
        "pitfall": "**DO NOT confuse x-intercept with y-intercept!** $(-3, 0)$ is an $x$-intercept. The $y$-intercept is $(0, -4)$, NOT $(0, -3)$!",
        "script": "[Prof. Park] Example 2 is a classic exam question. Students see $-3$ and write $y = -\\frac{4}{3}x - 3$. Why is that wrong, Sora?\n\n[TA Sora] Because $(-3, 0)$ is on the $x$-axis, not the $y$-axis! Using point-slope reveals that the true $y$-intercept is $-4$, giving $y = -\\frac{4}{3}x - 4$!",
        "graph": {
            "xMin": -6, "xMax": 4, "yMin": -8, "yMax": 3,
            "title": "Example 2: y = -4/3x - 4 with x-int (-3, 0)",
            "points": [
                {"x": -3, "y": 0, "label": "x-int (-3, 0)", "color": "#f59e0b"},
                {"x": 0, "y": -4, "label": "y-int (0, -4)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": -4/3, "yIntercept": -4, "color": "#ec4899", "strokeWidth": 2.5, "label": "y = -4/3x - 4"}
            ]
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.3 Example 3 (Step 1): Finding Slope between (2, 3) and (-6, 1)",
        "subtitle": "Unit 2 • Lecture 22 • Section 2.3 Example 3 (Workbook p. 41)",
        "detail": "Lecture 22: Finding Linear Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3 Step 1 (Workbook p. 41)\nFind the equation of the line that contains the points:\n$$\\mathbf{(2, 3) \\quad \\text{and} \\quad (-6, 1)}$$\nFirst, calculate the slope $m$ using the two points.",
        "solution": "$$\\begin{aligned}\n\\text{Let } & (x_1, y_1) = (2, 3) \\quad \\text{and} \\quad (x_2, y_2) = (-6, 1) \\\\[0.5em]\nm & = \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{1 - 3}{-6 - 2} \\\\[0.5em]\n& = \\frac{-2}{-8} \\\\[0.5em]\n\\mathbf{m} & = \\mathbf{\\frac{1}{4}}\n\\end{aligned}$$",
        "pitfall": "**Simplifying fractions:** $\\frac{-2}{-8}$ simplifies to positive $\\frac{1}{4}$. Always reduce slopes before writing equations!",
        "script": "[Prof. Park] In Example 3, we are given two points but no slope. What is our first mission?\n\n[TA Sora] Calculate slope first: $\\frac{1 - 3}{-6 - 2} = \\frac{-2}{-8} = \\frac{1}{4}$!"
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.3 Example 3 (Step 2 & Graph): Point-Slope to Slope-Intercept",
        "subtitle": "Unit 2 • Lecture 22 • Section 2.3 Example 3 Graph (Workbook p. 41)",
        "detail": "Lecture 22: Finding Linear Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3 Step 2 (Workbook p. 41)\nNow use $m = \\frac{1}{4}$ and point $(2, 3)$ to find the equation in slope-intercept form:\n- Apply $y - y_1 = m(x - x_1)$.\n- Graph the line passing through both $(2, 3)$ and $(-6, 1)$.",
        "solution": "$$\\begin{aligned}\ny - 3 & = \\frac{1}{4}(x - 2) \\\\[0.5em]\ny - 3 & = \\frac{1}{4}x - \\frac{2}{4} = \\frac{1}{4}x - \\frac{1}{2} \\\\[0.5em]\ny & = \\frac{1}{4}x - \\frac{1}{2} + 3 \\quad \\left(\\text{note: } 3 = \\frac{6}{2}\\right) \\\\[0.5em]\n\\mathbf{y} & = \\mathbf{\\frac{1}{4}x + \\frac{5}{2} = \\frac{1}{4}x + 2.5}\n\\end{aligned}$$",
        "pitfall": "**Either point works:** You could also plug in $(-6, 1)$: $y - 1 = \\frac{1}{4}(x + 6) \\implies y = \\frac{1}{4}x + 2.5$. You get the exact same answer!",
        "script": "[Prof. Park] Distributing $\\frac{1}{4}$ and adding 3 gives $y = \\frac{1}{4}x + 2.5$.\n\n[TA Sora] On our coordinate plane, both $(2, 3)$ and $(-6, 1)$ sit squarely on the line, with $y$-intercept at $(0, 2.5)$!",
        "graph": {
            "xMin": -8, "xMax": 5, "yMin": -2, "yMax": 6,
            "title": "Example 3: Line through (2, 3) and (-6, 1)",
            "points": [
                {"x": 2, "y": 3, "label": "(2, 3)", "color": "#f59e0b"},
                {"x": -6, "y": 1, "label": "(-6, 1)", "color": "#38bdf8"},
                {"x": 0, "y": 2.5, "label": "y-int (0, 2.5)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": 0.25, "yIntercept": 2.5, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = 1/4x + 2.5"}
            ]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.3 Example 4: Points (1, 7) and (-3, 7)",
        "subtitle": "Unit 2 • Lecture 22 • Section 2.3 Example 4 (Workbook p. 42)",
        "detail": "Lecture 22: Finding Linear Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4 (Workbook p. 42)\nFind the equation of the line that contains the points:\n$$\\mathbf{(1, 7) \\quad \\text{and} \\quad (-3, 7)}$$\n- Notice the coordinates that match!\n- Calculate slope $m$ and state the equation directly.",
        "solution": "$$\\begin{aligned}\nm & = \\frac{7 - 7}{-3 - 1} = \\frac{0}{-4} = \\mathbf{0} \\\\[0.5em]\n\\text{Since } m = 0: & \\text{This is a } \\mathbf{\\text{Horizontal Line (HOY)}}. \\\\\n\\mathbf{\\text{Equation: }} & \\mathbf{y = 7}\n\\end{aligned}$$",
        "pitfall": "**Spot identical coordinates:** Whenever both points share the same $y$-value (here $y = 7$), the line is simply $y = 7$!",
        "script": "[Prof. Park] In Example 4, both $y$-coordinates are 7. The slope is 0.\n\n[TA Sora] By HOY, the equation is simply $y = 7$! A flat horizontal line at height 7.",
        "graph": {
            "xMin": -6, "xMax": 4, "yMin": 0, "yMax": 10,
            "title": "Example 4: Horizontal Line y = 7",
            "points": [
                {"x": 1, "y": 7, "label": "(1, 7)", "color": "#f59e0b"},
                {"x": -3, "y": 7, "label": "(-3, 7)", "color": "#38bdf8"}
            ],
            "lines": [
                {"horizontal": 7, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = 7"}
            ]
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.3 Example 5: Points (2, -8) and (2, 1)",
        "subtitle": "Unit 2 • Lecture 22 • Section 2.3 Example 5 (Workbook p. 42)",
        "detail": "Lecture 22: Finding Linear Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5 (Workbook p. 42)\nFind the equation of the line that contains the points:\n$$\\mathbf{(2, -8) \\quad \\text{and} \\quad (2, 1)}$$\n- Notice the coordinates that match!\n- Calculate slope $m$ and state the equation.",
        "solution": "$$\\begin{aligned}\nm & = \\frac{1 - (-8)}{2 - 2} = \\frac{9}{0} = \\mathbf{\\text{Undefined}} \\\\[0.5em]\n\\text{Since slope is undefined: } & \\text{This is a } \\mathbf{\\text{Vertical Line (VUX)}}. \\\\\n\\mathbf{\\text{Equation: }} & \\mathbf{x = 2}\n\\end{aligned}$$",
        "pitfall": "**Do not use point-slope for vertical lines!** Because $m$ is undefined, you cannot multiply by $m$. Simply write $x = 2$!",
        "script": "[Prof. Park] In Example 5, both $x$-coordinates are 2. The slope is undefined.\n\n[TA Sora] By VUX, this is a vertical line with equation $x = 2$!",
        "graph": {
            "xMin": -2, "xMax": 6, "yMin": -10, "yMax": 4,
            "title": "Example 5: Vertical Line x = 2",
            "points": [
                {"x": 2, "y": -8, "label": "(2, -8)", "color": "#ec4899"},
                {"x": 2, "y": 1, "label": "(2, 1)", "color": "#10b981"}
            ],
            "lines": [
                {"vertical": 2, "color": "#ec4899", "strokeWidth": 2.5, "label": "x = 2"}
            ]
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 2.3 Part 1 Mastery Summary",
        "subtitle": "Unit 2 • Lecture 22 • Section 2.3 Wrap-up",
        "detail": "Lecture 22: Finding Linear Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Line Equation Strategies\n1. **Given $m$ and $y$-intercept $(0, b)$:** Use $y = mx + b$.\n2. **Given $m$ and any point $(x_1, y_1)$:** Use $y - y_1 = m(x - x_1)$.\n3. **Given two points:** Find $m = \\frac{y_2 - y_1}{x_2 - x_1}$ first, then use point-slope.\n4. **Same $y$-values:** Horizontal line $y = c$.\n5. **Same $x$-values:** Vertical line $x = c$.",
        "solution": "$$\\mathbf{\\text{Lecture 22 Complete! Next Up: Section 2.3 Part 2 — Parallel \\& Perpendicular Lines!}}$$",
        "pitfall": "**Double check signs:** $y - (-4)$ is $y + 4$, and $x - (-2)$ is $x + 2$!",
        "script": "[Prof. Park] Superb work! In Lecture 23, we use point-slope to construct lines parallel and perpendicular to other lines!"
    }
]

# L23: Section 2.3 Part 2 (Workbook pp. 42 - 44) - 8 slides
data_21_25[23] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.3 Example 6: Parallel Line through (-1, 3)",
        "subtitle": "Unit 2 • Lecture 23 • Section 2.3 Example 6 (Workbook p. 42)",
        "detail": "Lecture 23: Parallel & Perpendicular Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 6 (Workbook p. 42)\nFind the equation of the line containing the point $(-1, 3)$ and **parallel** to the line:\n$$\\mathbf{2x + y = 10}$$\n- Find the slope of the given line.\n- Use the same slope for the parallel line.\n- Write the new equation in slope-intercept form.",
        "solution": "$$\\begin{aligned}\n\\text{Given line: } & 2x + y = 10 \\implies y = -2x + 10 \\implies \\mathbf{m = -2} \\\\[0.5em]\n\\text{Parallel line has: } & m = -2, \\quad \\text{point } (-1, 3) \\\\[0.5em]\ny - y_1 & = m(x - x_1) \\\\[0.5em]\ny - 3 & = -2(x - (-1)) = -2(x + 1) \\\\[0.5em]\ny - 3 & = -2x - 2 \\\\[0.5em]\n\\mathbf{y} & = \\mathbf{-2x + 1}\n\\end{aligned}$$",
        "pitfall": "**Throw away the old intercept:** Only steal the SLOPE ($m = -2$) from the given line! Discard the $+10$ intercept!",
        "script": "[Prof. Park] In Example 6, the given line has slope $-2$. Our parallel line also needs slope $-2$.\n\n[TA Sora] Plugging $(-1, 3)$ and $m = -2$ into point-slope gives $y = -2x + 1$. Look at both lines running parallel on the grid!",
        "graph": {
            "xMin": -5, "xMax": 6, "yMin": -4, "yMax": 12,
            "title": "Example 6: Parallel Lines y = -2x + 10 and y = -2x + 1",
            "points": [
                {"x": -1, "y": 3, "label": "(-1, 3)", "color": "#f59e0b"},
                {"x": 0, "y": 1, "label": "(0, 1)", "color": "#38bdf8"}
            ],
            "lines": [
                {"slope": -2, "yIntercept": 10, "color": "#64748b", "strokeWidth": 2, "dashed": True, "label": "2x + y = 10"},
                {"slope": -2, "yIntercept": 1, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = -2x + 1"}
            ]
        }
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.3 Example 7: Perpendicular Line through (2, -3)",
        "subtitle": "Unit 2 • Lecture 23 • Section 2.3 Example 7 (Workbook p. 42)",
        "detail": "Lecture 23: Parallel & Perpendicular Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 7 (Workbook p. 42)\nFind the equation of the line containing the point $(2, -3)$ and **perpendicular** to the line:\n$$\\mathbf{4y - x = 20}$$\n- Solve for $y$ to find the slope of the given line.\n- Take the opposite reciprocal for $m_\\perp$.\n- Write the equation in slope-intercept form.",
        "solution": "$$\\begin{aligned}\n\\text{Given line: } & 4y = x + 20 \\implies y = \\frac{1}{4}x + 5 \\implies \\mathbf{m_1 = \\frac{1}{4}} \\\\[0.5em]\n\\text{Perpendicular slope: } & \\mathbf{m_\\perp = -4} \\quad (\\text{opposite reciprocal}) \\\\[0.5em]\ny - (-3) & = -4(x - 2) \\\\[0.5em]\ny + 3 & = -4x + 8 \\\\[0.5em]\n\\mathbf{y} & = \\mathbf{-4x + 5}\n\\end{aligned}$$",
        "pitfall": "**Opposite AND Reciprocal:** The reciprocal of $\\frac{1}{4}$ is $4$, and making it opposite gives $-4$!",
        "script": "[Prof. Park] In Example 7, the original slope is $\\frac{1}{4}$. The perpendicular slope must be $-4$.\n\n[TA Sora] Using point $(2, -3)$ with $m = -4$, we get $y = -4x + 5$. They meet at a 90-degree right angle!",
        "graph": {
            "xMin": -6, "xMax": 8, "yMin": -6, "yMax": 8,
            "title": "Example 7: Perpendicular Lines y = 1/4x + 5 and y = -4x + 5",
            "points": [
                {"x": 2, "y": -3, "label": "(2, -3)", "color": "#f59e0b"},
                {"x": 0, "y": 5, "label": "Shared y-int (0, 5)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": 0.25, "yIntercept": 5, "color": "#38bdf8", "strokeWidth": 2, "label": "y = 1/4x + 5"},
                {"slope": -4, "yIntercept": 5, "color": "#ec4899", "strokeWidth": 2.5, "label": "y = -4x + 5"}
            ]
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "In-Class Practice #1: Y-intercept (0, 5) and m = -3/5",
        "subtitle": "Unit 2 • Lecture 23 • Section 2.3 Practice #1 (Workbook p. 43)",
        "detail": "Lecture 23: Parallel & Perpendicular Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### In-Class Practice 1 (Workbook p. 43)\nFind the equation of the line with a $y$-intercept of $(0, 5)$ and a slope of $m = -\\frac{3}{5}$.\n- Write the equation in slope-intercept form.\n- Graph the line on the Cartesian coordinate plane.",
        "solution": "$$\\begin{aligned}\n\\text{Given: } & m = -\\frac{3}{5}, \\quad b = 5 \\\\[0.5em]\n\\mathbf{y} & = \\mathbf{-\\frac{3}{5}x + 5}\n\\end{aligned}$$",
        "pitfall": "**Direct form:** When $y$-intercept $(0, 5)$ is given, $b = 5$ immediately!",
        "script": "[Prof. Park] In Practice 1, we drop $m = -\\frac{3}{5}$ and $b = 5$ into $y = mx + b$.\n\n[TA Sora] We get $y = -\\frac{3}{5}x + 5$!",
        "graph": {
            "xMin": -2, "xMax": 10, "yMin": -2, "yMax": 8,
            "title": "Practice 1: y = -3/5x + 5",
            "points": [
                {"x": 0, "y": 5, "label": "(0, 5)", "color": "#10b981"},
                {"x": 5, "y": 2, "label": "(5, 2)", "color": "#38bdf8"}
            ],
            "lines": [
                {"slope": -0.6, "yIntercept": 5, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = -3/5x + 5"}
            ]
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "In-Class Practice #2: X-intercept (5, 0) and m = 3/5",
        "subtitle": "Unit 2 • Lecture 23 • Section 2.3 Practice #2 (Workbook p. 43)",
        "detail": "Lecture 23: Parallel & Perpendicular Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### In-Class Practice 2 (Workbook p. 43)\nFind the equation of the line with $x$-intercept of $(5, 0)$ and a slope of $m = \\frac{3}{5}$.\n- Use point-slope form $y - y_1 = m(x - x_1)$.\n- Graph the line on the Cartesian coordinate plane.",
        "solution": "$$\\begin{aligned}\n\\text{Point: } & (x_1, y_1) = (5, 0), \\quad m = \\frac{3}{5} \\\\[0.5em]\ny - 0 & = \\frac{3}{5}(x - 5) \\\\[0.5em]\ny & = \\frac{3}{5}x - \\left(\\frac{3}{5} \\cdot 5\\right) \\\\[0.5em]\n\\mathbf{y} & = \\mathbf{\\frac{3}{5}x - 3}\n\\end{aligned}$$",
        "pitfall": "**Don't assume b = 5:** $(5, 0)$ is an $x$-intercept! The $y$-intercept solves to $(0, -3)$!",
        "script": "[Prof. Park] In Practice 2, $(5, 0)$ is an $x$-intercept. Point-slope reveals $y = \\frac{3}{5}x - 3$.\n\n[TA Sora] Notice how the line crosses at $(5, 0)$ on the $x$-axis and $(0, -3)$ on the $y$-axis!",
        "graph": {
            "xMin": -2, "xMax": 8, "yMin": -5, "yMax": 4,
            "title": "Practice 2: y = 3/5x - 3 with x-int (5, 0)",
            "points": [
                {"x": 5, "y": 0, "label": "x-int (5, 0)", "color": "#f59e0b"},
                {"x": 0, "y": -3, "label": "y-int (0, -3)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": 0.6, "yIntercept": -3, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = 3/5x - 3"}
            ]
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "In-Class Practice #3: Through (-2, -3) and (6, 1)",
        "subtitle": "Unit 2 • Lecture 23 • Section 2.3 Practice #3 (Workbook p. 43)",
        "detail": "Lecture 23: Parallel & Perpendicular Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### In-Class Practice 3 (Workbook p. 43)\nFind the equation of the line that contains the points:\n$$\\mathbf{(-2, -3) \\quad \\text{and} \\quad (6, 1)}$$\n- Calculate the slope $m$.\n- Use point-slope form to find the equation.",
        "solution": "$$\\begin{aligned}\nm & = \\frac{1 - (-3)}{6 - (-2)} = \\frac{1 + 3}{6 + 2} = \\frac{4}{8} = \\mathbf{\\frac{1}{2}} \\\\[0.5em]\ny - 1 & = \\frac{1}{2}(x - 6) \\\\[0.5em]\ny - 1 & = \\frac{1}{2}x - 3 \\\\[0.5em]\n\\mathbf{y} & = \\mathbf{\\frac{1}{2}x - 2}\n\\end{aligned}$$",
        "pitfall": "**Double negatives:** In the slope calculation, $-(-3) = +3$ and $-(-2) = +2$, giving $\\frac{4}{8} = \\frac{1}{2}$!",
        "script": "[Prof. Park] In Practice 3, the slope is $\\frac{4}{8} = \\frac{1}{2}$. Using point $(6, 1)$ gives $y = \\frac{1}{2}x - 2$.\n\n[TA Sora] Let's verify: does $(-2, -3)$ work? $\\frac{1}{2}(-2) - 2 = -1 - 2 = -3$. It checks out perfectly!",
        "graph": {
            "xMin": -4, "xMax": 8, "yMin": -5, "yMax": 4,
            "title": "Practice 3: y = 1/2x - 2 through (-2, -3) and (6, 1)",
            "points": [
                {"x": -2, "y": -3, "label": "(-2, -3)", "color": "#f59e0b"},
                {"x": 6, "y": 1, "label": "(6, 1)", "color": "#38bdf8"},
                {"x": 0, "y": -2, "label": "y-int (0, -2)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": 0.5, "yIntercept": -2, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = 1/2x - 2"}
            ]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "In-Class Practice #4 & #5: Special Lines",
        "subtitle": "Unit 2 • Lecture 23 • Section 2.3 Practice #4 & #5 (Workbook pp. 43-44)",
        "detail": "Lecture 23: Parallel & Perpendicular Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### In-Class Practice 4 & 5 (Workbook pp. 43–44)\nFind the equations of the lines:\n- **#4:** Points $(2, -9)$ and $(2, -3)$\n- **#5:** Points $(5, -2)$ and $(4, -2)$",
        "solution": "$$\\begin{aligned}\n\\mathbf{\\#4: } & \\text{Both points have } x = 2 \\implies \\mathbf{x = 2} \\quad (\\text{Vertical line, } m = \\text{undefined}) \\\\[0.8em]\n\\mathbf{\\#5: } & \\text{Both points have } y = -2 \\implies \\mathbf{y = -2} \\quad (\\text{Horizontal line, } m = 0)\n\\end{aligned}$$",
        "pitfall": "**Instant inspection:** When $x$-coordinates are the same, $x = c$. When $y$-coordinates are the same, $y = c$!",
        "script": "[Prof. Park] In Practice 4 and 5, always inspect the coordinates first. Matching $x$ means vertical $x=2$; matching $y$ means horizontal $y=-2$.\n\n[TA Sora] HOY and VUX in action once again!",
        "graph": {
            "xMin": -2, "xMax": 8, "yMin": -10, "yMax": 2,
            "title": "Practice 4 & 5: x = 2 (Vertical) and y = -2 (Horizontal)",
            "points": [
                {"x": 2, "y": -3, "label": "(2, -3)", "color": "#ec4899"},
                {"x": 5, "y": -2, "label": "(5, -2)", "color": "#38bdf8"}
            ],
            "lines": [
                {"vertical": 2, "color": "#ec4899", "strokeWidth": 2.5, "label": "x = 2"},
                {"horizontal": -2, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = -2"}
            ]
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "In-Class Practice #6: Parallel to 3x - y = 7 through (2, 1)",
        "subtitle": "Unit 2 • Lecture 23 • Section 2.3 Practice #6 (Workbook p. 44)",
        "detail": "Lecture 23: Parallel & Perpendicular Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### In-Class Practice 6 (Workbook p. 44)\nFind the equation of the line containing the point $(2, 1)$ and **parallel** to the line:\n$$\\mathbf{3x - y = 7}$$",
        "solution": "$$\\begin{aligned}\n\\text{Given line: } & -y = -3x + 7 \\implies y = 3x - 7 \\implies \\mathbf{m = 3} \\\\[0.5em]\n\\text{Parallel line: } & m = 3, \\quad \\text{point } (2, 1) \\\\[0.5em]\ny - 1 & = 3(x - 2) = 3x - 6 \\\\[0.5em]\n\\mathbf{y} & = \\mathbf{3x - 5}\n\\end{aligned}$$",
        "pitfall": "**Solving for y:** Don't forget $-y = -3x + 7$ means $y = +3x - 7$. The slope is $+3$!",
        "script": "[Prof. Park] In Practice 6, the slope is $+3$. Using point $(2, 1)$ with $m = 3$ gives $y = 3x - 5$.\n\n[TA Sora] Both lines have slope 3 and run parallel forever!",
        "graph": {
            "xMin": -2, "xMax": 5, "yMin": -8, "yMax": 6,
            "title": "Practice 6: Parallel Lines y = 3x - 7 and y = 3x - 5",
            "points": [
                {"x": 2, "y": 1, "label": "(2, 1)", "color": "#f59e0b"}
            ],
            "lines": [
                {"slope": 3, "yIntercept": -7, "color": "#64748b", "strokeWidth": 2, "dashed": True, "label": "3x - y = 7"},
                {"slope": 3, "yIntercept": -5, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = 3x - 5"}
            ]
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "In-Class Practice #7: Perpendicular to 2y - x = 20 through (6, 3)",
        "subtitle": "Unit 2 • Lecture 23 • Section 2.3 Practice #7 (Workbook p. 44)",
        "detail": "Lecture 23: Parallel & Perpendicular Equations",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### In-Class Practice 7 (Workbook p. 44)\nFind the equation of the line containing the point $(6, 3)$ and **perpendicular** to the line:\n$$\\mathbf{2y - x = 20}$$",
        "solution": "$$\\begin{aligned}\n\\text{Given line: } & 2y = x + 20 \\implies y = \\frac{1}{2}x + 10 \\implies \\mathbf{m_1 = \\frac{1}{2}} \\\\[0.5em]\n\\text{Perpendicular slope: } & \\mathbf{m_\\perp = -2} \\\\[0.5em]\ny - 3 & = -2(x - 6) = -2x + 12 \\\\[0.5em]\n\\mathbf{y} & = \\mathbf{-2x + 15}\n\\end{aligned}$$",
        "pitfall": "**Reciprocal sign check:** Opposite reciprocal of $\\frac{1}{2}$ is $-2$. Then $-2 \\cdot (-6) = +12$!",
        "script": "[Prof. Park] In Practice 7, the original slope is $\\frac{1}{2}$, making the perpendicular slope $-2$. With point $(6, 3)$, we get $y = -2x + 15$.\n\n[TA Sora] Outstanding work completing Section 2.3! In Lecture 24, we enter the world of Functions!"
    }
]

# L24: Section 2.4 Part 1 (Workbook p. 45) - 8 slides
data_21_25[24] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Section 2.4: Relations, Domain & Range",
        "subtitle": "Unit 2 • Lecture 24 • Section 2.4 (Workbook p. 45)",
        "detail": "Lecture 24: Relations, Domain & Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Fundamentals of Relations (Workbook p. 45)\n- **Relation:** Any set of ordered pairs $(x, y)$.\n- **Input:** The first value in the ordered pair ($x$).\n- **Output:** The second value in the ordered pair ($y$).\n- **Domain:** The set of **all input values** ($x$-coordinates).\n- **Range:** The set of **all output values** ($y$-coordinates).",
        "solution": "$$\\begin{aligned}\n\\text{Relation } R & = \\{(x_1, y_1), (x_2, y_2), \\dots\\} \\\\[0.5em]\n\\text{Domain} & = \\{x \\mid (x, y) \\in R\\} \\quad (\\text{all } x\\text{-values}) \\\\\n\\text{Range} & = \\{y \\mid (x, y) \\in R\\} \\quad (\\text{all } y\\text{-values})\n\\end{aligned}$$",
        "pitfall": "**No duplicates in sets:** When writing domain or range in set notation, list repeating numbers only ONCE!",
        "script": "[Prof. Park] Welcome to Section 2.4! A relation is simply any pairing between inputs and outputs.\n\n[TA Sora] Think of a vending machine: you press a button (input $x$) and get a snack (output $y$)!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.4 Example 1: Domain & Range of a Discrete Relation",
        "subtitle": "Unit 2 • Lecture 24 • Section 2.4 Example 1 (Workbook p. 45)",
        "detail": "Lecture 24: Relations, Domain & Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 (Workbook p. 45)\nFor the following relation, determine the domain and range:\n$$\\mathbf{\\{(1, -1), (2, 5), (3, 10), (4, 16), (2, -3)\\}}$$\n- List all $x$-values in braces $\\{\\}$.\n- List all $y$-values in order from least to greatest.",
        "solution": "$$\\begin{aligned}\n\\text{Inputs } (x): & 1, 2, 3, 4, 2 \\\\[0.5em]\n\\mathbf{\\text{Domain: }} & \\mathbf{\\{1, 2, 3, 4\\}} \\quad (\\text{do not repeat } 2!) \\\\[0.8em]\n\\text{Outputs } (y): & -1, 5, 10, 16, -3 \\\\[0.5em]\n\\mathbf{\\text{Range: }} & \\mathbf{\\{-3, -1, 5, 10, 16\\}} \\quad (\\text{written in numerical order})\n\\end{aligned}$$",
        "pitfall": "**The repeated input:** Notice that the input $2$ appears twice: $(2, 5)$ and $(2, -3)$! In the domain set, we write $2$ once.",
        "script": "[Prof. Park] In Example 1, we collect all inputs into the domain: $\\{1, 2, 3, 4\\}$.\n\n[TA Sora] And for the range, list them in increasing order: $\\{-3, -1, 5, 10, 16\\}$!"
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.4 Example 1: Coordinate Grid of Discrete Points",
        "subtitle": "Unit 2 • Lecture 24 • Section 2.4 Example 1 Visual",
        "detail": "Lecture 24: Relations, Domain & Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Visualizing Example 1 on the Coordinate Plane\nPlot all five points of the relation:\n$$(1, -1), \\; (2, 5), \\; (3, 10), \\; (4, 16), \\; (2, -3)$$\nWhat do you notice vertically about the points $(2, 5)$ and $(2, -3)$?",
        "solution": "$$\\begin{aligned}\n\\text{Notice: } & (2, 5) \\text{ and } (2, -3) \\text{ share the EXACT same } x\\text{-coordinate } x = 2. \\\\[0.5em]\n\\text{Visual: } & \\mathbf{\\text{They stack directly above and below each other vertically!}} \\\\[0.5em]\n\\text{Significance: } & \\text{A single vertical line } x = 2 \\text{ passes through BOTH points.}\n\\end{aligned}$$",
        "pitfall": "**Vertical stacking:** When two points have the same $x$, they lie on the same vertical line. This will be the key to the Vertical Line Test!",
        "script": "[Prof. Park] Look at your screen. Point $(2, 5)$ and Point $(2, -3)$ stack vertically at $x = 2$.\n\n[TA Sora] They lie on the same vertical line $x = 2$! Remember this image for when we discuss functions!",
        "graph": {
            "xMin": -1, "xMax": 6, "yMin": -5, "yMax": 18,
            "title": "Example 1 Points: Stacking at x = 2",
            "points": [
                {"x": 1, "y": -1, "label": "(1, -1)", "color": "#38bdf8"},
                {"x": 2, "y": 5, "label": "(2, 5)", "color": "#ec4899"},
                {"x": 2, "y": -3, "label": "(2, -3)", "color": "#ec4899"},
                {"x": 3, "y": 10, "label": "(3, 10)", "color": "#38bdf8"},
                {"x": 4, "y": 16, "label": "(4, 16)", "color": "#10b981"}
            ],
            "vltLine": 2
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Mapping Diagrams: Visualizing Relations",
        "subtitle": "Unit 2 • Lecture 24 • Section 2.4 Mapping Diagrams",
        "detail": "Lecture 24: Relations, Domain & Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Mapping Diagrams (Domain $\\rightarrow$ Range)\nIn a mapping diagram:\n- The left oval contains the **Domain** elements.\n- The right oval contains the **Range** elements.\n- Arrows point from each input to its corresponding output.\n\nIn Example 1:\n- $1 \\rightarrow -1$\n- $\\mathbf{2 \\rightarrow 5}$ and $\\mathbf{2 \\rightarrow -3}$ *(One input branches to TWO outputs!)*\n- $3 \\rightarrow 10$\n- $4 \\rightarrow 16$",
        "solution": "$$\\begin{aligned}\n\\text{Domain Oval: } & \\{1, 2, 3, 4\\} \\\\\n\\text{Range Oval: } & \\{-3, -1, 5, 10, 16\\} \\\\[0.5em]\n\\text{Branching at } 2: & 2 \\text{ sends out two arrows: } 2 \\rightarrow 5 \\text{ and } 2 \\rightarrow -3.\n\\end{aligned}$$",
        "pitfall": "**Branching arrows:** If any input has more than one arrow leaving it, that relation CANNOT be a function!",
        "script": "[Prof. Park] Mapping diagrams show the flow of information. Look at input 2: it shoots out two arrows.\n\n[TA Sora] If you press button 2 on a vending machine, you don't know whether you will get chips or soda! That uncertainty is what prevents it from being a function!"
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.4 Example 2 (Graph A): Continuous Domain & Range",
        "subtitle": "Unit 2 • Lecture 24 • Section 2.4 Example 2A (Workbook p. 45)",
        "detail": "Lecture 24: Relations, Domain & Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2 Graph A (Workbook p. 45)\nFor the line segment shown on the graph extending from $(-4, -2)$ to $(4, 2)$:\n- Determine the **Domain** in interval notation.\n- Determine the **Range** in interval notation.",
        "solution": "$$\\begin{aligned}\n\\text{Leftmost } x: & -4 \\quad (\\text{closed dot} \\implies [) \\\\\n\\text{Rightmost } x: & +4 \\quad (\\text{closed dot} \\implies ]) \\\\[0.5em]\n\\mathbf{\\text{Domain: }} & \\mathbf{[-4, 4]} \\\\[0.8em]\n\\text{Lowest } y: & -2 \\quad (\\text{closed dot} \\implies [) \\\\\n\\text{Highest } y: & +2 \\quad (\\text{closed dot} \\implies ]) \\\\[0.5em]\n\\mathbf{\\text{Range: }} & \\mathbf{[-2, 2]}\n\\end{aligned}$$",
        "pitfall": "**Continuous uses intervals, not braces:** A solid curve contains infinitely many points, so we write intervals $[-4, 4]$, NOT discrete lists $\\{-4, 4\\}$!",
        "script": "[Prof. Park] In Example 2 Graph A, we have a continuous line segment. Look left-to-right for domain, and bottom-to-top for range.\n\n[TA Sora] The $x$-values stretch from $-4$ to $4$, so Domain is $[-4, 4]$. The $y$-values stretch from $-2$ to $2$, so Range is $[-2, 2]$!",
        "graph": {
            "xMin": -6, "xMax": 6, "yMin": -4, "yMax": 4,
            "title": "Example 2A: Segment from (-4, -2) to (4, 2)",
            "points": [
                {"x": -4, "y": -2, "label": "(-4, -2)", "color": "#10b981"},
                {"x": 4, "y": 2, "label": "(4, 2)", "color": "#38bdf8"}
            ],
            "lines": [
                {"p1": [-4, -2], "p2": [4, 2], "color": "#38bdf8", "strokeWidth": 3}
            ]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.4 Example 2 (Graph B): Bounded Curve",
        "subtitle": "Unit 2 • Lecture 24 • Section 2.4 Example 2B (Workbook p. 45)",
        "detail": "Lecture 24: Relations, Domain & Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2 Graph B (Workbook p. 45)\nFor the graph shown extending from $x = -3$ to $x = 5$ with minimum $y = -2$ and peak $y = 4$:\n- State the **Domain** in interval notation.\n- State the **Range** in interval notation.",
        "solution": "$$\\begin{aligned}\n\\text{Leftmost } x: & -3, \\quad \\text{Rightmost } x: 5 \\\\[0.5em]\n\\mathbf{\\text{Domain: }} & \\mathbf{[-3, 5]} \\\\[0.8em]\n\\text{Lowest } y: & -2, \\quad \\text{Highest } y: 4 \\\\[0.5em]\n\\mathbf{\\text{Range: }} & \\mathbf{[-2, 4]}\n\\end{aligned}$$",
        "pitfall": "**Peak vs Endpoint:** For range, do not just look at the endpoints! Look for the absolute lowest valley and absolute highest peak on the graph!",
        "script": "[Prof. Park] In Example 2 Graph B, the curve dips down to $-2$ and peaks at $+4$.\n\n[TA Sora] So while the domain is $[-3, 5]$ horizontally, the range reaches from $-2$ up to $4$, giving $[-2, 4]$!",
        "graph": {
            "xMin": -5, "xMax": 7, "yMin": -4, "yMax": 6,
            "title": "Example 2B: Domain [-3, 5], Range [-2, 4]",
            "points": [
                {"x": -3, "y": 0, "label": "Start (-3, 0)", "color": "#10b981"},
                {"x": 1, "y": 4, "label": "Peak (1, 4)", "color": "#f59e0b"},
                {"x": 3, "y": -2, "label": "Valley (3, -2)", "color": "#ec4899"},
                {"x": 5, "y": 2, "label": "End (5, 2)", "color": "#38bdf8"}
            ]
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Interval Notation vs Set-Builder Notation",
        "subtitle": "Unit 2 • Lecture 24 • Section 2.4 Notation Guide",
        "detail": "Lecture 24: Relations, Domain & Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### How to Report Domain and Range (Workbook p. 45)\n- **Discrete Relations (individual points):**\n  Use set braces listing numbers: $\\{1, 2, 3, 4\\}$.\n- **Continuous Relations (connected lines/curves):**\n  Use interval notation: $[a, b]$ or $(-\\infty, \\infty)$.\n- **Interval Symbols:**\n  - $[$ or $]$: Bracket includes the number (solid dot $\\bullet$).\n  - $($ or $)$: Parenthesis excludes the number (open circle $\\circ$) or for $\\pm\\infty$.",
        "solution": "$$\\begin{array}{|c|c|c|}\n\\hline\n\\textbf{Type of Graph} & \\textbf{Format} & \\textbf{Example} \\\\\n\\hline\n\\text{Discrete Points} & \\text{Set Braces } \\{\\} & D = \\{1, 2, 3\\}, \\; R = \\{4, 5\\} \\\\\n\\hline\n\\text{Segment with solid dots} & \\text{Closed Interval } [a, b] & D = [-4, 4], \\; R = [-2, 2] \\\\\n\\hline\n\\text{Line with arrows both ways} & \\text{All Real Numbers} & D = (-\\infty, \\infty), \\; R = (-\\infty, \\infty) \\\\\n\\hline\n\\end{array}$$",
        "pitfall": "**Never use braces for intervals:** $\\{ -4, 4 \\}$ only means two numbers: $-4$ and $4$. $[-4, 4]$ includes all infinite numbers in between!",
        "script": "[Prof. Park] Always choose the right notation: curly braces for discrete points, square brackets and parentheses for continuous intervals.\n\n[TA Sora] That distinction is essential on quizzes and exams!"
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 2.4 Part 1 Mastery Summary",
        "subtitle": "Unit 2 • Lecture 24 • Section 2.4 Wrap-up",
        "detail": "Lecture 24: Relations, Domain & Range",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Section 2.4 Part 1 Master Checklist\n- **Input = $x$-coordinate**\n- **Output = $y$-coordinate**\n- **Domain = set of all inputs** (look left to right on graph)\n- **Range = set of all outputs** (look bottom to top on graph)",
        "solution": "$$\\mathbf{\\text{Lecture 24 Complete! Next Up: Section 2.4 Part 2 — Functions \\& The Vertical Line Test!}}$$",
        "pitfall": "**Left-to-Right, Bottom-to-Top:** Always read domain from left to right, and range from bottom to top!",
        "script": "[Prof. Park] Excellent job! In Lecture 25, we find out which relations earn the special title of FUNCTION!"
    }
]

# L25: Section 2.4 Part 2 (Workbook p. 46) - 8 slides
data_21_25[25] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "The Formal Definition of a Function",
        "subtitle": "Unit 2 • Lecture 25 • Section 2.4 (Workbook p. 46)",
        "detail": "Lecture 25: Functions & The Vertical Line Test",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Definition: What is a Function? (Workbook p. 46)\nA **function** is a relation that assigns **each element in its domain to exactly one element in its range**.\n- **Crucial Rule:** One input value cannot correspond to two different output values!\n- **Allowed:** Multiple different inputs can produce the same output value (e.g. $2^2 = 4$ and $(-2)^2 = 4$).\n- **Forbidden:** A single input cannot split into two different outputs!",
        "solution": "$$\\begin{aligned}\n\\text{Function: } & \\text{Every } x \\text{ has ONE AND ONLY ONE } y. \\\\\n\\text{NOT a function: } & \\text{An } x \\text{ gives two or more different } y\\text{'s}.\n\\end{aligned}$$",
        "pitfall": "**One-to-many is NOT allowed:** Think of a person's birthday: one person can only have ONE birthday (function). But two different people can share the same birthday (allowed)!",
        "script": "[Prof. Park] Welcome to Lecture 25! A function is predictable: give it an input $x$, and it returns exactly one output $y$.\n\n[TA Sora] If an input gives you multiple different answers, it's not a function!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.4 Example 3: Testing Example 1 for Function Status",
        "subtitle": "Unit 2 • Lecture 25 • Section 2.4 Example 3 (Workbook p. 46)",
        "detail": "Lecture 25: Functions & The Vertical Line Test",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3 (Workbook p. 46)\nBased off the definition of a function, determine if Example 1 is a function:\n$$\\mathbf{\\{(1, -1), (2, 5), (3, 10), (4, 16), (2, -3)\\}}$$",
        "solution": "$$\\begin{aligned}\n\\text{Examine input } x = 2: & \\\\\n& 2 \\implies 5 \\quad \\text{from } (2, 5) \\\\\n& 2 \\implies -3 \\quad \\text{from } (2, -3) \\\\[0.8em]\n\\text{Analysis: } & \\text{The input } x = 2 \\text{ is assigned to TWO different outputs: } 5 \\text{ and } -3. \\\\[0.8em]\n\\mathbf{\\text{Conclusion: }} & \\mathbf{\\text{NOT A FUNCTION.}}\n\\end{aligned}$$",
        "pitfall": "**Look for repeated x-values:** In a set of ordered pairs, if any $x$-value repeats with a different $y$-value, it immediately FAILS to be a function!",
        "script": "[Prof. Park] In Example 3, input $x=2$ pairs with 5 and with $-3$.\n\n[TA Sora] That violates the rule of a function! Therefore, Example 1 is NOT a function."
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "The Vertical Line Test (VLT)",
        "subtitle": "Unit 2 • Lecture 25 • Section 2.4 (Workbook p. 46)",
        "detail": "Lecture 25: Functions & The Vertical Line Test",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### The Vertical Line Test (Workbook p. 46)\nA set of points in a rectangular coordinate system is the **graph of a function** if **every vertical line intersects the graph in at most one point**.\n- If **any** vertical line intersects the graph in **more than one point**, the graph **does not represent a function**.\n- Why? Because intersecting twice means that single $x$-value has two different $y$-values!",
        "solution": "$$\\begin{aligned}\n\\text{At most 1 intersection everywhere} & \\implies \\mathbf{\\text{IS A FUNCTION}} \\\\\n\\text{2 or more intersections anywhere} & \\implies \\mathbf{\\text{NOT A FUNCTION}}\n\\end{aligned}$$",
        "pitfall": "**It only takes ONE failure:** Even if 99% of vertical lines hit once, if a SINGLE vertical line hits twice, the entire graph is NOT a function!",
        "script": "[Prof. Park] The Vertical Line Test is the visual equivalent of the function definition.\n\n[TA Sora] Imagine scanning a vertical ruler across the screen from left to right. If the curve touches the ruler twice at any moment, it fails!"
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.4 Example 4A: Parabola y = x^2 - 2 (Passes VLT)",
        "subtitle": "Unit 2 • Lecture 25 • Section 2.4 Example 4A (Workbook p. 46)",
        "detail": "Lecture 25: Functions & The Vertical Line Test",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4A (Workbook p. 46)\nDetermine if the parabola $y = x^2 - 2$ represents a function:\n- Apply the Vertical Line Test.\n- State whether it is a function.",
        "solution": "$$\\begin{aligned}\n\\text{Vertical Line Test: } & \\text{Any vertical line } x = c \\text{ intersects the parabola } \\mathbf{\\text{at exactly ONE point}}. \\\\[0.8em]\n\\mathbf{\\text{Conclusion: }} & \\mathbf{\\text{YES, it is a FUNCTION.}}\n\\end{aligned}$$",
        "pitfall": "**U-shape is fine:** It's okay that $(-2, 2)$ and $(2, 2)$ share the same $y$-height. That is a horizontal test, not a vertical test!",
        "script": "[Prof. Park] Look at the parabola on your screen. Any vertical line hits it in at most one point.\n\n[TA Sora] It passes the Vertical Line Test with flying colors! Parabolas opening upward are functions.",
        "graph": {
            "xMin": -5, "xMax": 5, "yMin": -4, "yMax": 8,
            "title": "Example 4A: Parabola y = x^2 - 2 (PASSES VLT -> Function)",
            "points": [
                {"x": 0, "y": -2, "label": "Vertex (0, -2)", "color": "#10b981"},
                {"x": 2, "y": 2, "label": "(2, 2)", "color": "#38bdf8"},
                {"x": -2, "y": 2, "label": "(-2, 2)", "color": "#38bdf8"}
            ],
            "vltLine": 2
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.4 Example 4B: Circle x^2 + y^2 = 16 (Fails VLT)",
        "subtitle": "Unit 2 • Lecture 25 • Section 2.4 Example 4B (Workbook p. 46)",
        "detail": "Lecture 25: Functions & The Vertical Line Test",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4B (Workbook p. 46)\nDetermine if the circle $x^2 + y^2 = 16$ represents a function:\n- Apply the Vertical Line Test.\n- Identify a specific vertical line that intersects the circle more than once.",
        "solution": "$$\\begin{aligned}\n\\text{Test line } x = 0: & 0^2 + y^2 = 16 \\implies y^2 = 16 \\implies y = \\pm 4 \\\\[0.5em]\n\\text{Intersections: } & \\mathbf{(0, 4) \\quad \\text{and} \\quad (0, -4)} \\\\[0.8em]\n\\text{Vertical Line Test: } & \\text{The vertical line } x = 0 \\text{ intersects the circle in } \\mathbf{\\text{TWO points}}! \\\\[0.8em]\n\\mathbf{\\text{Conclusion: }} & \\mathbf{\\text{NOT A FUNCTION.}}\n\\end{aligned}$$",
        "pitfall": "**Circles, ellipses, and sideways parabolas are NOT functions:** Any closed loop curve fails the vertical line test!",
        "script": "[Prof. Park] In Example 4B, the red dashed line $x = 0$ cuts right through the circle, hitting $(0, 4)$ at the top and $(0, -4)$ at the bottom!\n\n[TA Sora] Two outputs for a single input $x = 0$. Circles fail the VLT and are NOT functions!",
        "graph": {
            "xMin": -6, "xMax": 6, "yMin": -6, "yMax": 6,
            "title": "Example 4B: Circle x^2 + y^2 = 16 (FAILS VLT -> Not a Function)",
            "points": [
                {"x": 0, "y": 4, "label": "(0, 4) [Top Hit]", "color": "#ef4444"},
                {"x": 0, "y": -4, "label": "(0, -4) [Bottom Hit]", "color": "#ef4444"}
            ],
            "vltLine": 0
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.4 Example 4C: Non-Vertical Line y = 2x - 1 (Passes VLT)",
        "subtitle": "Unit 2 • Lecture 25 • Section 2.4 Example 4C (Workbook p. 46)",
        "detail": "Lecture 25: Functions & The Vertical Line Test",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4C (Workbook p. 46)\nDetermine if the linear equation $y = 2x - 1$ represents a function:\n- Apply the Vertical Line Test.\n- State whether all non-vertical lines are functions.",
        "solution": "$$\\begin{aligned}\n\\text{Vertical Line Test: } & \\text{Every vertical line intersects } y = 2x - 1 \\text{ exactly ONCE.} \\\\[0.8em]\n\\mathbf{\\text{Conclusion: }} & \\mathbf{\\text{YES, it is a FUNCTION.}} \\\\[0.5em]\n\\text{Universal Rule: } & \\mathbf{\\text{ALL non-vertical lines are linear functions!}}\n\\end{aligned}$$",
        "pitfall": "**Horizontal lines are functions:** A horizontal line $y = 3$ passes the VLT (every vertical line hits it once). But a vertical line $x = 3$ fails completely!",
        "script": "[Prof. Park] All non-vertical straight lines pass the VLT everywhere.\n\n[TA Sora] Every non-vertical line is a linear function!",
        "graph": {
            "xMin": -4, "xMax": 5, "yMin": -5, "yMax": 7,
            "title": "Example 4C: Linear Function y = 2x - 1 (Passes VLT)",
            "points": [
                {"x": 0, "y": -1, "label": "y-int (0, -1)", "color": "#10b981"},
                {"x": 2, "y": 3, "label": "(2, 3)", "color": "#38bdf8"}
            ],
            "lines": [
                {"slope": 2, "yIntercept": -1, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = 2x - 1"}
            ],
            "vltLine": 2
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.4 Example 4D: Vertical Line x = 3 (Fails VLT Infinitely)",
        "subtitle": "Unit 2 • Lecture 25 • Section 2.4 Example 4D (Workbook p. 46)",
        "detail": "Lecture 25: Functions & The Vertical Line Test",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4D (Workbook p. 46)\nDetermine if the vertical line $x = 3$ represents a function:\n- Apply the Vertical Line Test at $x = 3$.\n- How many times does the vertical line $x = 3$ intersect itself?",
        "solution": "$$\\begin{aligned}\n\\text{Test line at } x = 3: & \\text{The test line lies directly ON TOP of } x = 3! \\\\[0.5em]\n\\text{Intersections: } & \\mathbf{\\text{INFINITELY MANY intersection points!}} \\\\[0.8em]\n\\mathbf{\\text{Conclusion: }} & \\mathbf{\\text{NOT A FUNCTION.}}\n\\end{aligned}$$",
        "pitfall": "**Vertical lines are NEVER functions:** A vertical line has an input of 3 with every conceivable $y$-value simultaneously!",
        "script": "[Prof. Park] In Example 4D, $x = 3$ fails the Vertical Line Test in the most catastrophic way possible: infinitely many intersections!\n\n[TA Sora] Vertical lines are relations, but they can NEVER be functions!",
        "graph": {
            "xMin": -2, "xMax": 8, "yMin": -6, "yMax": 6,
            "title": "Example 4D: Vertical Line x = 3 (FAILS VLT Infinitely)",
            "points": [
                {"x": 3, "y": 0, "label": "(3, 0)", "color": "#ef4444"},
                {"x": 3, "y": 3, "label": "(3, 3)", "color": "#ef4444"},
                {"x": 3, "y": -3, "label": "(3, -3)", "color": "#ef4444"}
            ],
            "lines": [
                {"vertical": 3, "color": "#ef4444", "strokeWidth": 3, "label": "x = 3"}
            ],
            "vltLine": 3
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 2.4 Complete Mastery Summary",
        "subtitle": "Unit 2 • Lecture 25 • Section 2.4 Wrap-up",
        "detail": "Lecture 25: Functions & The Vertical Line Test",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Summary of Section 2.4 Functions\n- **Definition:** Every input $x$ has exactly one output $y$.\n- **Ordered Pairs:** No $x$-value can repeat with different $y$'s.\n- **Graphs (VLT):** No vertical line can hit more than once.\n- **Linear Functions:** All lines are functions EXCEPT vertical lines ($x = c$).",
        "solution": "$$\\mathbf{\\text{Section 2.4 Mastered! Next Up: Section 2.5 — Function Notation f(x)!}}$$",
        "pitfall": "**Remember:** Functions are the bedrock of all advanced mathematics and calculus!",
        "script": "[Prof. Park] Fantastic work mastering Section 2.4! You can now identify functions algebraically and graphically.\n\n[TA Sora] In Lecture 26, we introduce the famous notation $f(x)$!"
    }
]

print("Lectures 21 to 25 generated successfully!")
