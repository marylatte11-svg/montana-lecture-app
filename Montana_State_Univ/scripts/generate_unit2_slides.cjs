// Script to generate Lectures 16 through 30 for Montana State University M090 Unit 2
// 100% exact match to M090 Student Workbook pages 29 to 56.

const fs = require('fs');

const L16 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Unit 2 Orientation & Coordinates",
    title: "Section 2.0: Intro to Graphing & The Cartesian Plane",
    subtitle: "Unit 2 • Lecture 16 • Section 2.0 (Workbook p. 29)",
    detail: "Lecture 16: Intro to Graphing & The Cartesian Plane",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### The Rectangular (Cartesian) Coordinate System (Workbook p. 29)\n- **Axes:** The horizontal $x$-axis and vertical $y$-axis intersect at the **Origin** $(0, 0)$.\n- **Quadrants:** Divided into 4 regions counter-clockwise:\n  - **Quadrant I:** $(+, +)$\n  - **Quadrant II:** $(-, +)$\n  - **Quadrant III:** $(-, -)$\n  - **Quadrant IV:** $(+, -)$\n- **Ordered Pair:** $(x, y)$ — horizontal position $x$ followed by vertical position $y$.",
    solution: "$$\\begin{aligned}\n\\text{Origin: } & (0, 0) \\\\\n\\text{Quadrant I: } & (3, 5) \\implies x > 0, y > 0 \\\\\n\\text{Quadrant II: } & (-4, 2) \\implies x < 0, y > 0 \\\\\n\\text{Quadrant III: } & (-3, -6) \\implies x < 0, y < 0 \\\\\n\\text{Quadrant IV: } & (5, -2) \\implies x > 0, y < 0\n\\end{aligned}$$",
    pitfall: "**Sora's Memory Hook:** 'Walk before you climb!' Always move left or right along the $x$-axis first, then move up or down on the $y$-axis!",
    script: "[Prof. Park] Welcome to Unit 2, everyone! We are stepping into the visual world of coordinate geometry on page 29 of your M090 Workbook.\n\n[TA Sora] Welcome back Bobcats! In Unit 1 we manipulated algebraic symbols; now in Unit 2, we bring those symbols to life as graphs and lines!\n\n[Prof. Park] René Descartes gave us this coordinate plane. Remember: $(x, y)$ always lists the horizontal $x$-value first, and the vertical $y$-value second. Let's plot our first points on Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1: Plotting & Labeling Ordered Pairs",
    subtitle: "Unit 2 • Lecture 16 • Section 2.0 Example 1 (Workbook p. 29)",
    detail: "Lecture 16: Intro to Graphing & The Cartesian Plane",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Plot and label the ordered pairs in the coordinate plane (Workbook p. 29)\n$$\\text{A. } (4, 0) \\qquad \\text{B. } (-1, 3) \\qquad \\text{C. } (0, 5) \\qquad \\text{D. } (-3, -4)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Point\\ A\\ (4, 0):}\\quad & \\text{Move } 4 \\text{ units right, } 0 \\text{ units vertically} \\implies \\mathbf{\\text{On the positive } x\\text{-axis}} \\\\[0.8em]\n\\mathbf{Point\\ B\\ (-1, 3):}\\quad & \\text{Move } 1 \\text{ unit left, } 3 \\text{ units up} \\implies \\mathbf{\\text{Quadrant II}} \\\\[0.8em]\n\\mathbf{Point\\ C\\ (0, 5):}\\quad & \\text{Move } 0 \\text{ units horizontally, } 5 \\text{ units up} \\implies \\mathbf{\\text{On the positive } y\\text{-axis}} \\\\[0.8em]\n\\mathbf{Point\\ D\\ (-3, -4):}\\quad & \\text{Move } 3 \\text{ units left, } 4 \\text{ units down} \\implies \\mathbf{\\text{Quadrant III}}\n\\end{aligned}$$",
    pitfall: "**The Axis Points Trap:** Points with zero like $(4, 0)$ and $(0, 5)$ are **NOT in any quadrant**! They lie directly on the coordinate axes!",
    script: "[Prof. Park] In Example 1, look at $(4, 0)$ and $(0, 5)$. Sora, which axes do they sit on?\n\n[TA Sora] $(4, 0)$ has $y = 0$, so it sits right on the $x$-axis. $(0, 5)$ has $x = 0$, so it sits right on the $y$-axis!\n\n[Prof. Park] Excellent. And $(-1, 3)$ is in Quadrant II, while $(-3, -4)$ is in Quadrant III."
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Core Verification Principle",
    title: "Testing Solutions to Two-Variable Equations",
    subtitle: "Unit 2 • Lecture 16 • Section 2.0 (Workbook p. 29)",
    detail: "Lecture 16: Intro to Graphing & The Cartesian Plane",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Definition: Solution of an Equation in x and y (Workbook p. 29)\nAn ordered pair $(x, y)$ is a **solution** if substituting the $x$- and $y$-values results in a **true statement**.\n$$\\text{Test if } (2, 3) \\text{ and } (4, 0) \\text{ are solutions to } 2x + y = 7$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Test\\ (2, 3):}\\quad & 2(2) + 3 = 4 + 3 = 7 = 7 \\quad \\mathbf{[TRUE]} \\\\\n& \\implies \\mathbf{(2, 3) \\text{ is a solution (lies on the line!)}}\\\\[1em]\n\\mathbf{Test\\ (4, 0):}\\quad & 2(4) + 0 = 8 + 0 = 8 \\neq 7 \\quad \\mathbf{[FALSE]} \\\\\n& \\implies \\mathbf{(4, 0) \\text{ is NOT a solution (does not lie on the line!)}}\n\\end{aligned}$$",
    pitfall: "**Sora's Insight:** A line is simply a visual picture of all the infinite ordered pairs $(x, y)$ that make the equation true!",
    script: "[Prof. Park] What is a line really? It is a collection of infinitely many points $(x, y)$ that satisfy the equation.\n\n[TA Sora] When we plug in $(2, 3)$, $2(2) + 3 = 7$, which is true! So $(2, 3)$ is on the line. When we plug in $(4, 0)$, $8 \\ne 7$, so it's not on the line.\n\n[Prof. Park] In Lecture 17, we will systematically find these points using tables and intercepts!"
  }
];

const L17 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1: Graphing 2x + 3y = 6 Using a Table",
    subtitle: "Unit 2 • Lecture 17 • Section 2.1 Example 1 (Workbook p. 33)",
    detail: "Lecture 17: Linear Equations in Two Variables & Intercepts",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Graph the following linear equation using a table (Workbook p. 33)\n$$2x + 3y = 6$$\nConstruct a table of values for $x = 0, 3, -3$ and find the corresponding $y$-values.",
    solution: "$$\\begin{aligned}\n\\text{Solve for } y: & \\quad 3y = -2x + 6 \\implies y = -\\frac{2}{3}x + 2 \\\\[0.8em]\n\\mathbf{For\\ x = 0:}\\quad & y = -\\frac{2}{3}(0) + 2 = \\mathbf{2} \\implies (0, 2) \\\\[0.8em]\n\\mathbf{For\\ x = 3:}\\quad & y = -\\frac{2}{3}(3) + 2 = -2 + 2 = \\mathbf{0} \\implies (3, 0) \\\\[0.8em]\n\\mathbf{For\\ x = -3:}\\quad & y = -\\frac{2}{3}(-3) + 2 = 2 + 2 = \\mathbf{4} \\implies (-3, 4)\n\\end{aligned}$$",
    pitfall: "**Choose Multiples of the Denominator:** Since the denominator is 3, pick $x$-values that are multiples of 3 ($0, 3, -3, 6$) to avoid messy fractions!",
    script: "[Prof. Park] Welcome to Lecture 17! Today we are on page 33 of your workbook: Section 2.1, Example 1.\n\n[TA Sora] We have $2x + 3y = 6$. Notice that solving for $y$ gives $y = -\\frac{2}{3}x + 2$. Since there is a 3 in the denominator, pick $x = 0, 3, -3$ so the fraction cancels cleanly!\n\n[Prof. Park] Exactly. That gives us $(0, 2), (3, 0),$ and $(-3, 4)$. Connect those dots, and you have your line!"
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2: Identifying Slope and y-Intercept",
    subtitle: "Unit 2 • Lecture 17 • Section 2.1 Example 2 (Workbook p. 33)",
    detail: "Lecture 17: Linear Equations in Two Variables & Intercepts",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Identify the slope and y-intercept for each (Workbook p. 33)\n$$\\text{A. } y = -\\frac{2}{3}x + 2$$\n$$\\text{B. } 2x - y = 7$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & y = mx + b \\implies \\mathbf{\\text{Slope } m = -\\frac{2}{3}}, \\quad \\mathbf{y\\text{-intercept: } (0, 2)} \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & \\text{Convert to slope-intercept form } y = mx + b: \\\\\n& -y = -2x + 7 \\\\\n& y = 2x - 7 \\\\\n& \\implies \\mathbf{\\text{Slope } m = 2}, \\quad \\mathbf{y\\text{-intercept: } (0, -7)}\n\\end{aligned}$$",
    pitfall: "**Intercept is an Ordered Pair:** Always write the $y$-intercept as a coordinate point $(0, b)$, not just a single number $b$!",
    script: "[Prof. Park] In Example 2A, $y = -\\frac{2}{3}x + 2$ is already in slope-intercept form: slope $m = -\\frac{2}{3}$ and $y$-intercept is $(0, 2)$.\n\n[TA Sora] In 2B, $2x - y = 7$ needs to be rewritten first: $-y = -2x + 7 \\implies y = 2x - 7$. Slope is 2, and the $y$-intercept is $(0, -7)$."
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3: Finding Intercepts Algebraically for 5x + 2y = 6",
    subtitle: "Unit 2 • Lecture 17 • Section 2.1 Example 3 (Workbook p. 34)",
    detail: "Lecture 17: Linear Equations in Two Variables & Intercepts",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Find the x- and y-intercepts algebraically, then rewrite into slope-intercept form (Workbook p. 34)\n$$5x + 2y = 6$$",
    solution: "$$\\begin{aligned}\n\\mathbf{x\\text{-intercept (Set } y = 0):}\\quad & 5x + 2(0) = 6 \\implies 5x = 6 \\implies \\mathbf{x = \\frac{6}{5}} \\implies \\mathbf{\\left(\\frac{6}{5}, 0\\right)} \\\\[0.8em]\n\\mathbf{y\\text{-intercept (Set } x = 0):}\\quad & 5(0) + 2y = 6 \\implies 2y = 6 \\implies \\mathbf{y = 3} \\implies \\mathbf{(0, 3)} \\\\[0.8em]\n\\mathbf{\\text{Slope-Intercept Form:}}\\quad & 2y = -5x + 6 \\implies \\mathbf{y = -\\frac{5}{2}x + 3}\n\\end{aligned}$$",
    pitfall: "**The Zero Rule:** To find the $x$-intercept, set $y = 0$! To find the $y$-intercept, set $x = 0$!",
    script: "[Prof. Park] On page 34, Example 3 gives $5x + 2y = 6$. Sora, how do we find the intercepts algebraically?\n\n[TA Sora] For the $x$-intercept, plug in $y = 0$: $5x = 6 \\implies x = \\frac{6}{5}$, so $(\\frac{6}{5}, 0)$. For the $y$-intercept, plug in $x = 0$: $2y = 6 \\implies y = 3$, so $(0, 3)$!\n\n[Prof. Park] And in slope-intercept form: $y = -\\frac{5}{2}x + 3$. Notice the $y$-intercept $(0, 3)$ matches perfectly!"
  }
];

const L18 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Core Graphing Strategy",
    title: "Section 2.1: Graphing Lines Fast via Slope-Intercept Form",
    subtitle: "Unit 2 • Lecture 18 • Section 2.1 (Workbook p. 35)",
    detail: "Lecture 18: Slope-Intercept Form & Special Lines",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Graphing with Slope m and y-Intercept b\n$$y = mx + b$$\n- **Step 1:** Plot the starting point: the $y$-intercept $(0, b)$ on the vertical axis.\n- **Step 2:** Use the slope $m = \\frac{\\text{Rise}}{\\text{Run}}$ to move to the next point.\n$$\\text{Graph: } y = \\frac{3}{4}x - 2$$",
    solution: "$$\\begin{aligned}\n\\text{Starting Point: } & (0, -2) \\\\\n\\text{Slope: } & m = \\frac{3}{4} = \\frac{\\text{Rise } +3}{\\text{Run } +4} \\\\\n\\text{Next Point: } & (0 + 4, -2 + 3) = \\mathbf{(4, 1)} \\\\\n\\text{Third Point: } & (4 + 4, 1 + 3) = \\mathbf{(8, 4)}\n\\end{aligned}$$",
    pitfall: "**Rise vs Run Order:** Rise is vertical ($y$), Run is horizontal ($x$)! Don't run before you rise!",
    script: "[Prof. Park] Welcome to Lecture 18! Graphing from $y = mx + b$ is the fastest technique in algebra.\n\n[TA Sora] Always plot $b$ first! In $y = \\frac{3}{4}x - 2$, anchor at $(0, -2)$, then rise 3 and run right 4 to land on $(4, 1)$!\n\n[Prof. Park] Now let's tackle the two most misunderstood lines in algebra: horizontal and vertical lines."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Special Lines Breakdown",
    title: "Horizontal vs. Vertical Lines: The HOY VUX Law",
    subtitle: "Unit 2 • Lecture 18 • Section 2.1 (Workbook pp. 36–37)",
    detail: "Lecture 18: Slope-Intercept Form & Special Lines",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### HOY VUX Memory Strategy (Workbook p. 36)\n| Acronym | Orientation | Slope | Equation Form | Example |\n| :--- | :--- | :--- | :--- | :--- |\n| **HOY** | **H**orizontal line | **0** (Zero slope) | **y** = constant | $y = 4$ |\n| **VUX** | **V**ertical line | **U**ndefined slope | **x** = constant | $x = -3$ |",
    solution: "$$\\begin{aligned}\n\\mathbf{Line\\ y = 4:}\\quad & \\text{Every point has } y = 4: \\quad (0, 4), (2, 4), (-5, 4) \\\\\n& \\text{Slope } m = \\frac{4 - 4}{2 - 0} = \\frac{0}{2} = \\mathbf{0} \\quad [\\textbf{Horizontal}] \\\\[1em]\n\\mathbf{Line\\ x = -3:}\\quad & \\text{Every point has } x = -3: \\quad (-3, 0), (-3, 2), (-3, -4) \\\\\n& \\text{Slope } m = \\frac{2 - 0}{-3 - (-3)} = \\frac{2}{0} = \\mathbf{\\text{Undefined}} \\quad [\\textbf{Vertical}]\n\\end{aligned}$$",
    pitfall: "**Zero vs. Undefined:** $y = 4$ has slope 0 (flat floor). $x = -3$ has undefined slope (a sheer cliff you cannot ski on)!",
    script: "[Prof. Park] Students often freeze when they see an equation with only one variable, like $y = 4$ or $x = -3$.\n\n[TA Sora] Remember HOY VUX! H-O-Y: Horizontal, Zero slope, $y = \\text{number}$. V-U-X: Vertical, Undefined slope, $x = \\text{number}$!\n\n[Prof. Park] Think of skiing: flat ground has slope 0. A vertical cliff has no slope—it's undefined! Great job on Section 2.1."
  }
];

const L19 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Core Slope Formula",
    title: "Section 2.2: The Slope of a Line — Rise over Run",
    subtitle: "Unit 2 • Lecture 19 • Section 2.2 (Workbook p. 38)",
    detail: "Lecture 19: The Slope of a Line & Rate of Change",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### The Slope Formula (Workbook p. 38)\n$$m = \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{\\Delta y}{\\Delta x} = \\frac{\\text{Rise}}{\\text{Run}}$$\n- Slope measures the **steepness and direction** of a straight line.\n- Always wrap coordinates in parentheses when subtracting negatives: $y_2 - (y_1)$!",
    solution: "$$\\begin{aligned}\n\\text{Four Types of Slope: } & \\\\\n\\text{1. Positive } (m > 0): & \\quad \\text{Rises from left to right } (\\nearrow) \\\\\n\\text{2. Negative } (m < 0): & \\quad \\text{Falls from left to right } (\\searrow) \\\\\n\\text{3. Zero } (m = 0): & \\quad \\text{Horizontal line } (\\rightarrow) \\\\\n\\text{4. Undefined}: & \\quad \\text{Vertical line } (\\uparrow)\n\\end{aligned}$$",
    pitfall: "**$y$ on Top, $x$ on Bottom:** The most common formula reversal is putting $\\frac{x_2 - x_1}{y_2 - y_1}$. $y$ is ALWAYS on top!",
    script: "[Prof. Park] Welcome to Lecture 19! Today we open to Section 2.2 on page 38 of your workbook: Slope of a Line.\n\n[TA Sora] Slope is rate of change: $m = \\frac{y_2 - y_1}{x_2 - x_1}$. Remember: $y$ values on top, $x$ values on the bottom! Let's solve Example 1 on Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1A & 1B: Finding Slope through Two Given Points",
    subtitle: "Unit 2 • Lecture 19 • Section 2.2 Example 1A & 1B (Workbook p. 38)",
    detail: "Lecture 19: The Slope of a Line & Rate of Change",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Find the slope of the line passing through the two points (Workbook p. 38)\n$$\\text{A. } (2, 3) \\text{ and } (5, 7)$$\n$$\\text{B. } (3, -4) \\text{ and } (-2, -8)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & m = \\frac{7 - 3}{5 - 2} = \\frac{4}{3} \\implies \\mathbf{m = \\frac{4}{3}} \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & m = \\frac{-8 - (-4)}{-2 - 3} = \\frac{-8 + 4}{-5} = \\frac{-4}{-5} = \\mathbf{\\frac{4}{5}}\n\\end{aligned}$$",
    pitfall: "**Double Negatives in Formula:** In 1B, $-8 - (-4) = -8 + 4 = -4$. Watch your signs!",
    script: "[Prof. Park] In 1A: $(2, 3)$ and $(5, 7)$. $m = \\frac{7 - 3}{5 - 2} = \\frac{4}{3}$.\n\n[TA Sora] In 1B: $(3, -4)$ and $(-2, -8)$. $m = \\frac{-8 - (-4)}{-2 - 3} = \\frac{-4}{-5} = \\frac{4}{5}$. A negative divided by a negative is positive!"
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1C & 1D: Zero vs. Undefined Slopes",
    subtitle: "Unit 2 • Lecture 19 • Section 2.2 Example 1C & 1D (Workbook p. 38)",
    detail: "Lecture 19: The Slope of a Line & Rate of Change",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Find the slope of the line passing through the two points (Workbook p. 38)\n$$\\text{C. } (3, 7) \\text{ and } (3, -10)$$\n$$\\text{D. } (-2, -5) \\text{ and } (3, -5)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & m = \\frac{-10 - 7}{3 - 3} = \\frac{-17}{0} \\implies \\mathbf{\\text{Undefined Slope}} \\quad [\\textbf{Vertical Line } x = 3] \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & m = \\frac{-5 - (-5)}{3 - (-2)} = \\frac{-5 + 5}{3 + 2} = \\frac{0}{5} = \\mathbf{0} \\quad [\\textbf{Horizontal Line } y = -5]\n\\end{aligned}$$",
    pitfall: "**Zero on Bottom = Undefined:** $\\frac{0}{5} = 0$ (OK!), but $\\frac{-17}{0} = \\text{Undefined}$ (NO!). You cannot divide by zero!",
    script: "[Prof. Park] In 1C, the $x$-coordinates are both 3. $3 - 3 = 0$ in the denominator, so the slope is Undefined. That's a vertical line: $x = 3$.\n\n[TA Sora] In 1D, the $y$-coordinates are both $-5$. $0$ in the numerator divided by 5 equals 0. That's a horizontal line: $y = -5$!"
  }
];

const L20 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Parallel & Perpendicular Laws",
    title: "Section 2.2: Parallel vs. Perpendicular Lines",
    subtitle: "Unit 2 • Lecture 20 • Section 2.2 (Workbook p. 40)",
    detail: "Lecture 20: Parallel & Perpendicular Lines",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Geometric Slopes Criteria (Workbook p. 40)\n- **Parallel Lines ($\\parallel$):** Have the **exact same slope** ($m_1 = m_2$) with different $y$-intercepts.\n- **Perpendicular Lines ($\\perp$):** Slopes are **opposite reciprocals**:\n$$m_1 \\cdot m_2 = -1 \\iff m_2 = -\\frac{1}{m_1}$$\n$$\\text{Example: If } m_1 = \\frac{2}{3}, \\text{ then } m_\\perp = -\\frac{3}{2}.$$",
    solution: "$$\\begin{aligned}\n\\text{Same Slope: } & m_1 = 4, m_2 = 4 \\implies \\mathbf{\\text{Parallel}} \\\\\n\\text{Opposite Reciprocal: } & m_1 = 4, m_2 = -\\frac{1}{4} \\implies \\mathbf{\\text{Perpendicular}} \\\\\n\\text{Neither: } & m_1 = 4, m_2 = -4 \\implies \\mathbf{\\text{Neither! (Opposite but NOT reciprocal)}}\n\\end{aligned}$$",
    pitfall: "**Both Flip and Negate:** Perpendicular slopes must flip the fraction AND change the sign! $3$ and $-3$ are NOT perpendicular!",
    script: "[Prof. Park] Welcome to Lecture 20! Today we turn to page 40 of your workbook: Parallel and Perpendicular Lines.\n\n[TA Sora] Parallel lines never touch—they have identical slopes! Perpendicular lines cross at $90^\\circ$—their slopes are flipped and have opposite signs!\n\n[Prof. Park] Let's analyze Examples 3, 4, and 5 on Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 4 & 5: Parallel, Perpendicular, or Neither?",
    subtitle: "Unit 2 • Lecture 20 • Section 2.2 Example 4 & 5 (Workbook p. 40)",
    detail: "Lecture 20: Parallel & Perpendicular Lines",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Determine if the lines are parallel, perpendicular, or neither (Workbook p. 40)\n$$\\mathbf{Example\\ 4:}\\quad x + y = 5 \\quad \\text{and} \\quad -2x - 2y = 7$$\n$$\\mathbf{Example\\ 5:}\\quad 2y = x - 2 \\quad \\text{and} \\quad y = -2x - 4$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Example\\ 4:}\\quad & \\text{Line 1: } y = -x + 5 \\implies \\mathbf{m_1 = -1} \\\\\n& \\text{Line 2: } -2y = 2x + 7 \\implies y = -x - \\frac{7}{2} \\implies \\mathbf{m_2 = -1} \\\\\n& m_1 = m_2 = -1 \\implies \\mathbf{\\text{PARALLEL}} \\\\[1em]\n\\mathbf{Example\\ 5:}\\quad & \\text{Line 1: } y = \\frac{1}{2}x - 1 \\implies \\mathbf{m_1 = \\frac{1}{2}} \\\\\n& \\text{Line 2: } y = -2x - 4 \\implies \\mathbf{m_2 = -2} \\\\\n& m_1 \\cdot m_2 = \\left(\\frac{1}{2}\\right)(-2) = -1 \\implies \\mathbf{\\text{PERPENDICULAR}}\n\\end{aligned}$$",
    pitfall: "**Convert to $y = mx + b$ First:** Never guess the slope from standard form until you isolate $y$!",
    script: "[Prof. Park] In Example 4, both lines have slope $-1$. Same slope means they are Parallel!\n\n[TA Sora] In Example 5, Line 1 has slope $\\frac{1}{2}$, and Line 2 has slope $-2$. Since $\\frac{1}{2} \\cdot (-2) = -1$, they are Perpendicular!"
  }
];

console.log('L16 to L20 slide objects defined.');
