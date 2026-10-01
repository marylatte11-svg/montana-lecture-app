const fs = require('fs');

// Comprehensive generator for Montana State University M090 Unit 2 (Lectures 16 through 30)
// 100% exact match to M090 Student Workbook pages 29 to 56.

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
    script: "[Prof. Park] Welcome to Unit 2, everyone! We are stepping into the visual world of coordinate geometry on page 29 of your M090 Workbook.\n\n[TA Sora] Welcome back Bobcats! In Unit 1 we manipulated algebraic symbols; now in Unit 2, we bring those symbols to life as graphs and lines!\n\n[Prof. Park] Remember: $(x, y)$ always lists the horizontal $x$-value first, and the vertical $y$-value second. Let's plot our first points on Slide 2."
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

const L21 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Core Point-Slope Equation",
    title: "Section 2.3: Point-Slope Form of a Line",
    subtitle: "Unit 2 • Lecture 21 • Section 2.3 (Workbook p. 41)",
    detail: "Lecture 21: Finding the Equation of a Line (Point-Slope Form)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### The Point-Slope Formula (Workbook p. 41)\n$$y - y_1 = m(x - x_1)$$\n- Where $m$ is the slope and $(x_1, y_1)$ is any point on the line.\n- Can be used to find the equation of **any non-vertical line** in the universe!\n- Always solve for $y$ at the end to express in slope-intercept form $y = mx + b$.",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Identify or calculate slope } m. \\\\\n\\text{Step 2: } & \\text{Pick a point } (x_1, y_1) \\text{ and substitute into } y - y_1 = m(x - x_1). \\\\\n\\text{Step 3: } & \\text{Distribute } m \\text{ and isolate } y.\n\\end{aligned}$$",
    pitfall: "**Minus Signs in Formula:** Watch $y - (-3) = y + 3$ and $x - (-2) = x + 2$!",
    script: "[Prof. Park] Welcome to Lecture 21! Today we are on page 41: Finding the Equation of a Line.\n\n[TA Sora] Point-Slope form $y - y_1 = m(x - x_1)$ is your best friend! Give me any point and a slope, and I can give you the equation of the line!\n\n[Prof. Park] Let's solve Examples 1, 2, and 3 on Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1 & 2: Writing Line Equations from Intercepts",
    subtitle: "Unit 2 • Lecture 21 • Section 2.3 Example 1 & 2 (Workbook p. 41)",
    detail: "Lecture 21: Finding the Equation of a Line (Point-Slope Form)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Find the equation of each line (Workbook p. 41)\n$$\\mathbf{Example\\ 1:}\\quad y\\text{-intercept } (0, -3) \\text{ and slope } m = -\\frac{4}{3}$$\n$$\\mathbf{Example\\ 2:}\\quad x\\text{-intercept } (-3, 0) \\text{ and slope } m = -\\frac{4}{3}$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Example\\ 1:}\\quad & \\text{Since we are given the } y\\text{-intercept } (0, -3), \\quad b = -3: \\\\\n& \\mathbf{y = -\\frac{4}{3}x - 3} \\\\[1em]\n\\mathbf{Example\\ 2:}\\quad & \\text{Given point } (x_1, y_1) = (-3, 0) \\text{ and } m = -\\frac{4}{3}: \\\\\n& y - 0 = -\\frac{4}{3}(x - (-3)) \\\\\n& y = -\\frac{4}{3}(x + 3) = -\\frac{4}{3}x - \\left(\\frac{4}{3} \\cdot 3\\right) \\\\\n& \\mathbf{y = -\\frac{4}{3}x - 4}\n\\end{aligned}$$",
    pitfall: "**$x$-intercept is NOT $b$:** In Example 2, the point is $(-3, 0)$, so $b \\neq -3$! You must use point-slope form to find $b = -4$!",
    script: "[Prof. Park] Look at Example 1: $y$-intercept is $(0, -3)$, so $b = -3$ directly: $y = -\\frac{4}{3}x - 3$.\n\n[TA Sora] But in Example 2, $(-3, 0)$ is an $X$-intercept, not a $y$-intercept! We must use point-slope form: $y - 0 = -\\frac{4}{3}(x + 3) \\implies y = -\\frac{4}{3}x - 4$!"
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3: Line Containing (2, 3) and (-6, 1)",
    subtitle: "Unit 2 • Lecture 21 • Section 2.3 Example 3 (Workbook p. 41)",
    detail: "Lecture 21: Finding the Equation of a Line (Point-Slope Form)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Find the equation of the line containing the points (Workbook p. 41)\n$$(2, 3) \\quad \\text{and} \\quad (-6, 1)$$",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Find slope } m: \\\\\n& m = \\frac{1 - 3}{-6 - 2} = \\frac{-2}{-8} = \\mathbf{\\frac{1}{4}} \\\\[0.8em]\n\\text{Step 2: } & \\text{Use point-slope form with } (2, 3): \\\\\n& y - 3 = \\frac{1}{4}(x - 2) \\\\\n& y - 3 = \\frac{1}{4}x - \\frac{2}{4} = \\frac{1}{4}x - \\frac{1}{2} \\\\[0.8em]\n\\text{Step 3: } & \\text{Add } 3 = \\frac{6}{2} \\text{ to both sides:} \\\\\n& y = \\frac{1}{4}x - \\frac{1}{2} + \\frac{6}{2} \\implies \\mathbf{y = \\frac{1}{4}x + \\frac{5}{2}}\n\\end{aligned}$$",
    pitfall: "**Fraction Arithmetic:** $-\\frac{1}{2} + 3 = -\\frac{1}{2} + \\frac{6}{2} = \\frac{5}{2}$. Keep common denominators intact!",
    script: "[Prof. Park] In Example 3, we first find the slope between $(2, 3)$ and $(-6, 1)$: $m = \\frac{-2}{-8} = \\frac{1}{4}$.\n\n[TA Sora] Then plug into point-slope form: $y - 3 = \\frac{1}{4}(x - 2) \\implies y = \\frac{1}{4}x - \\frac{1}{2} + 3 \\implies y = \\frac{1}{4}x + \\frac{5}{2}$!\n\n[Prof. Park] Outstanding work! That completes page 41."
  }
];

const L22 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 4 & 5: Special Line Equations from Points",
    subtitle: "Unit 2 • Lecture 22 • Section 2.3 Example 4 & 5 (Workbook p. 42)",
    detail: "Lecture 22: Equations of Parallel, Perpendicular & Special Lines",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Find the equation of the line containing each pair of points (Workbook p. 42)\n$$\\mathbf{Example\\ 4:}\\quad (1, 7) \\text{ and } (-3, 7)$$\n$$\\mathbf{Example\\ 5:}\\quad (2, -8) \\text{ and } (2, 1)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Example\\ 4:}\\quad & m = \\frac{7 - 7}{-3 - 1} = \\frac{0}{-4} = 0 \\\\\n& \\text{Slope is } 0 \\implies \\text{Horizontal line!} \\\\\n& \\mathbf{y = 7} \\\\[1em]\n\\mathbf{Example\\ 5:}\\quad & m = \\frac{1 - (-8)}{2 - 2} = \\frac{9}{0} = \\text{Undefined} \\\\\n& \\text{Slope is Undefined} \\implies \\text{Vertical line!} \\\\\n& \\mathbf{x = 2}\n\\end{aligned}$$",
    pitfall: "**Spot Identical Coordinates:** In Ex 4, both $y$-values are 7 $\\implies y = 7$! In Ex 5, both $x$-values are 2 $\\implies x = 2$!",
    script: "[Prof. Park] Welcome to Lecture 22! Look at Example 4 on page 42: $(1, 7)$ and $(-3, 7)$.\n\n[TA Sora] Both $y$-coordinates are 7! The slope is 0, so the equation is simply $y = 7$!\n\n[Prof. Park] And in Example 5: $(2, -8)$ and $(2, 1)$. Both $x$-coordinates are 2, so the slope is undefined and the equation is $x = 2$!"
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 6 & 7: Parallel & Perpendicular Line Equations",
    subtitle: "Unit 2 • Lecture 22 • Section 2.3 Example 6 & 7 (Workbook p. 42)",
    detail: "Lecture 22: Equations of Parallel, Perpendicular & Special Lines",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Find the equation of the line satisfying the conditions (Workbook p. 42)\n$$\\mathbf{Example\\ 6:}\\quad \\text{Through } (-1, 3) \\text{ and parallel to } 2x + y = 10$$\n$$\\mathbf{Example\\ 7:}\\quad \\text{Through } (2, -3) \\text{ and perpendicular to } 4y - x = 20$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Example\\ 6:}\\quad & 2x + y = 10 \\implies y = -2x + 10 \\implies \\mathbf{m = -2} \\\\\n& \\text{Parallel means use the same slope: } m_\\parallel = -2 \\\\\n& y - 3 = -2(x - (-1)) = -2(x + 1) = -2x - 2 \\\\\n& \\mathbf{y = -2x + 1} \\\\[1em]\n\\mathbf{Example\\ 7:}\\quad & 4y - x = 20 \\implies 4y = x + 20 \\implies y = \\frac{1}{4}x + 5 \\implies m_1 = \\frac{1}{4} \\\\\n& \\text{Perpendicular slope is opposite reciprocal: } \\mathbf{m_\\perp = -4} \\\\\n& y - (-3) = -4(x - 2) \\implies y + 3 = -4x + 8 \\\\\n& \\mathbf{y = -4x + 5}\n\\end{aligned}$$",
    pitfall: "**Ignore the Original $y$-Intercept:** In Ex 6, throw away $+10$! In Ex 7, throw away $+5$! Only steal the slope!",
    script: "[Prof. Park] In Example 6, the given line has slope $-2$. For parallel, use $m = -2$ through $(-1, 3)$, giving $y = -2x + 1$.\n\n[TA Sora] In Example 7, the given line has slope $\\frac{1}{4}$. The perpendicular slope flips and negates to $-4$! Through $(2, -3)$, we get $y = -4x + 5$!"
  }
];

const L23 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Core Relation & Function Theory",
    title: "Section 2.4: Intro to Functions — Domain & Range",
    subtitle: "Unit 2 • Lecture 23 • Section 2.4 (Workbook p. 45)",
    detail: "Lecture 23: Intro to Functions, Domain & Range",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Key Definitions of Relations and Functions (Workbook p. 45)\n- **Relation:** Any set of ordered pairs $(x, y)$.\n- **Domain:** The set of all **input values** ($x$-coordinates).\n- **Range:** The set of all **output values** ($y$-coordinates).\n- **Function Rule:** A relation where **each input $x$ corresponds to EXACTLY ONE output $y$**.",
    solution: "$$\\begin{aligned}\n\\text{Input Set: } & \\text{Domain} = \\{x\\} \\\\\n\\text{Output Set: } & \\text{Range} = \\{y\\} \\\\\n\\text{Function Condition: } & \\text{No single } x \\text{ value can have two different } y \\text{ values!}\n\\end{aligned}$$",
    pitfall: "**Sora's Vending Machine Analogy:** Pressing button B4 (input $x$) must always dispense the same snack (output $y$)! If pressing B4 sometimes gives chips and sometimes soda, the machine is broken—NOT a function!",
    script: "[Prof. Park] Welcome to Lecture 23! Today we begin Section 2.4 on page 45: Intro to Functions.\n\n[TA Sora] Think of a function like a vending machine! Button B4 is your input, and a snack is your output. Each button must lead to exactly one predictable snack!\n\n[Prof. Park] Let's find Domain and Range for Example 1 on Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1: Domain & Range for a Discrete Relation",
    subtitle: "Unit 2 • Lecture 23 • Section 2.4 Example 1 (Workbook p. 45)",
    detail: "Lecture 23: Intro to Functions, Domain & Range",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### For the following relation, determine the domain and range (Workbook p. 45)\n$$\\{(1, 2), (3, 4), (5, 6), (1, 7)\\}$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Domain\\ (Inputs\\ x):}\\quad & \\text{Collect all } x\\text{-coordinates: } \\{1, 3, 5, 1\\} \\\\\n& \\text{List each unique value once: } \\mathbf{\\{1, 3, 5\\}} \\\\[1em]\n\\mathbf{Range\\ (Outputs\\ y):}\\quad & \\text{Collect all } y\\text{-coordinates: } \\{2, 4, 6, 7\\} \\\\\n& \\mathbf{\\{2, 4, 6, 7\\}}\n\\end{aligned}$$",
    pitfall: "**Do Not Repeat Elements:** When listing sets in curly braces $\\{ \\}$, never write duplicate numbers! Write $\\{1, 3, 5\\}$, NOT $\\{1, 1, 3, 5\\}$!",
    script: "[Prof. Park] In Example 1, our points are $(1, 2), (3, 4), (5, 6), (1, 7)$.\n\n[TA Sora] The inputs are 1, 3, 5, and 1. We don't write 1 twice, so Domain is $\\{1, 3, 5\\}$. The outputs are Range: $\\{2, 4, 6, 7\\}$!\n\n[Prof. Park] Notice that input 1 appears twice with different outputs. In Lecture 24, we'll see why that disqualifies it from being a function!"
  }
];

const L24 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Core Function Test",
    title: "Section 2.4: The Vertical Line Test (VLT)",
    subtitle: "Unit 2 • Lecture 24 • Section 2.4 (Workbook p. 46)",
    detail: "Lecture 24: Function Verification & The Vertical Line Test",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### The Vertical Line Test (Workbook p. 46)\nA graph represents a **function** if and only if **EVERY vertical line intersects the graph at most ONCE**.\n- If any vertical line passes through **2 or more points**, the graph is **NOT a function**.",
    solution: "$$\\begin{aligned}\n\\text{Passes VLT: } & \\text{Non-vertical lines, parabolas } (y = x^2) \\implies \\mathbf{\\text{FUNCTION}} \\\\\n\\text{Fails VLT: } & \\text{Circles, sideways parabolas } (x = y^2) \\implies \\mathbf{\\text{NOT A FUNCTION}}\n\\end{aligned}$$",
    pitfall: "**Vertical Lines Fail VLT:** A vertical line $x = c$ intersects itself at infinitely many points, so vertical lines are NEVER functions!",
    script: "[Prof. Park] Welcome to Lecture 24! Today on page 46, we learn the fastest graphical test in algebra: the Vertical Line Test.\n\n[TA Sora] Take an imaginary vertical ruler and sweep it across the graph. If it ever touches the graph at two points at the same time, it fails—NOT a function!\n\n[Prof. Park] Let's analyze Examples 3 and 4 on Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3 & 4: Determining Functions and VLT",
    subtitle: "Unit 2 • Lecture 24 • Section 2.4 Example 3 & 4 (Workbook p. 46)",
    detail: "Lecture 24: Function Verification & The Vertical Line Test",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Determine if each represents a function (Workbook p. 46)\n- **Example 3:** Is Example 1 $(\\{(1, 2), (3, 4), (5, 6), (1, 7)\\})$ a function?\n- **Example 4:** Determine if graphs (Parabola vs. Circle) represent functions.",
    solution: "$$\\begin{aligned}\n\\mathbf{Example\\ 3:}\\quad & \\text{Input } x = 1 \\text{ corresponds to TWO different outputs: } y = 2 \\text{ and } y = 7! \\\\\n& \\implies \\mathbf{\\text{NOT A FUNCTION}} \\\\[1em]\n\\mathbf{Example\\ 4A\\ (Parabola):}\\quad & \\text{Any vertical line intersects at most once } \\implies \\mathbf{\\text{FUNCTION}} \\\\[0.8em]\n\\mathbf{Example\\ 4B\\ (Circle):}\\quad & \\text{A vertical line intersects at top and bottom } \\implies \\mathbf{\\text{NOT A FUNCTION}}\n\\end{aligned}$$",
    pitfall: "**Multiple Inputs Sharing Output is OK:** $(2, 5)$ and $(3, 5)$ IS a function (horizontal line). But $(5, 2)$ and $(5, 3)$ is NOT a function!",
    script: "[Prof. Park] In Example 3, input 1 gives both 2 and 7. That breaks the single-output rule: Not a Function!\n\n[TA Sora] And in Example 4, a parabola passes the vertical line test, so it's a function. But a circle touches twice on a vertical line, so a circle is NOT a function!"
  }
];

const L25 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Core Notation Law",
    title: "Section 2.5: Function Notation — f(x) vs. y",
    subtitle: "Unit 2 • Lecture 25 • Section 2.5 (Workbook p. 47)",
    detail: "Lecture 25: Function Notation & Evaluating f(x)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Understanding Function Notation (Workbook p. 47)\n$$y = f(x)$$\n- $f$ is the **name** of the function.\n- $x$ is the **input**.\n- $f(x)$ (read \"$f$ of $x$\") is the **output value** ($y$-value).\n- **CRITICAL WARNING:** $f(x)$ DOES NOT MEAN $f$ multiplied by $x$!",
    solution: "$$\\begin{aligned}\n\\text{Equation Form: } & y = 4x - 5 \\\\\n\\text{Function Form: } & f(x) = 4x - 5 \\\\\n\\text{Evaluating at } x = 2: & f(2) = 4(2) - 5 = 8 - 5 = \\mathbf{3} \\implies \\text{Point: } (2, 3)\n\\end{aligned}$$",
    pitfall: "**Never Divide by f:** Since $f(x)$ is NOT multiplication, you cannot divide by $f$!",
    script: "[Prof. Park] Welcome to Lecture 25! Today on page 47 of your workbook, we introduce function notation: $f(x)$.\n\n[TA Sora] Please remember: $f(x)$ does NOT mean $f$ times $x$! It is a name tag that says: 'Feed me $x$, and I will output $y$!'\n\n[Prof. Park] In Example 1 and 2, $y = 4x - 5$ and $f(x) = 4x - 5$ are identical. When $x = 2$, $f(2) = 3$. Let's evaluate multi-functions on Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3: Evaluating Functions g(x) and h(x)",
    subtitle: "Unit 2 • Lecture 25 • Section 2.5 Example 3 (Workbook p. 48)",
    detail: "Lecture 25: Function Notation & Evaluating f(x)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Let g(x) = -2x + 7 and h(x) = 3x - 5. Evaluate each (Workbook p. 48)\n$$\\text{A. } g(-1) \\qquad \\text{B. } h(-1) \\qquad \\text{C. } h(0) \\qquad \\text{D. } g(0) \\qquad \\text{E. } g\\left(\\frac{5}{2}\\right)$$\n$$\\text{F. } h(a) \\qquad \\text{G. } g(x - 7) \\qquad \\text{H. } h(k + 1)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{A.\\ } g(-1):\\quad & -2(-1) + 7 = 2 + 7 = \\mathbf{9} \\\\[0.5em]\n\\mathbf{B.\\ } h(-1):\\quad & 3(-1) - 5 = -3 - 5 = \\mathbf{-8} \\\\[0.5em]\n\\mathbf{C.\\ } h(0):\\quad & 3(0) - 5 = \\mathbf{-5} \\\\[0.5em]\n\\mathbf{D.\\ } g(0):\\quad & -2(0) + 7 = \\mathbf{7} \\\\[0.5em]\n\\mathbf{E.\\ } g(5/2):\\quad & -2\\left(\\frac{5}{2}\\right) + 7 = -5 + 7 = \\mathbf{2} \\\\[0.5em]\n\\mathbf{F.\\ } h(a):\\quad & \\mathbf{3a - 5} \\\\[0.5em]\n\\mathbf{G.\\ } g(x - 7):\\quad & -2(x - 7) + 7 = -2x + 14 + 7 = \\mathbf{-2x + 21} \\\\[0.5em]\n\\mathbf{H.\\ } h(k + 1):\\quad & 3(k + 1) - 5 = 3k + 3 - 5 = \\mathbf{3k - 2}\n\\end{aligned}$$",
    pitfall: "**Algebraic Substitution Trap:** In Part G, replace the ENTIRE variable $x$ with $(x - 7)$ in parentheses: $-2(x - 7) + 7 = -2x + 21$!",
    script: "[Prof. Park] Example 3 on page 48 is fantastic. In 3A, $g(-1) = 9$. In 3E, $g(5/2) = 2$.\n\n[TA Sora] And look at 3G and 3H: you can plug expressions into functions! In $g(x - 7)$, replace $x$ with $(x - 7)$ to get $-2(x - 7) + 7 = -2x + 21$!\n\n[Prof. Park] In 3H, $h(k + 1) = 3(k + 1) - 5 = 3k - 2$. Clean, consistent substitution."
  }
];

const L26 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 4: Solving for x Given f(x) = k",
    subtitle: "Unit 2 • Lecture 26 • Section 2.5 Example 4 (Workbook p. 48)",
    detail: "Lecture 26: Solving Equations with Function Notation & Graph Reading",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Let f(x) = 5x + 3. Solve the following for x (Workbook p. 48)\n$$\\text{A. } f(x) = 18$$\n$$\\text{B. } f(x) = -8$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & \\text{Replace } f(x) \\text{ with } 18: \\\\\n& 18 = 5x + 3 \\implies 15 = 5x \\implies \\mathbf{x = 3} \\quad [\\text{Point: } (3, 18)] \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & \\text{Replace } f(x) \\text{ with } -8: \\\\\n& -8 = 5x + 3 \\implies -11 = 5x \\implies \\mathbf{x = -\\frac{11}{5}} \\quad \\left[\\text{Point: } \\left(-\\frac{11}{5}, -8\\right)\\right]\n\\end{aligned}$$",
    pitfall: "**Input vs. Output:** $f(18)$ means plug in $x = 18$. But $f(x) = 18$ means the OUTPUT is 18, so solve for $x$!",
    script: "[Prof. Park] Welcome to Lecture 26! Look carefully at Example 4: it does NOT say $f(18)$; it says $f(x) = 18$.\n\n[TA Sora] Big difference! $f(x) = 18$ means set $5x + 3 = 18$, so $x = 3$. And for $f(x) = -8$, set $5x + 3 = -8$, so $x = -\\frac{11}{5}$!"
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 5: Reading Function Values from a Graph",
    subtitle: "Unit 2 • Lecture 26 • Section 2.5 Example 5 (Workbook p. 49)",
    detail: "Lecture 26: Solving Equations with Function Notation & Graph Reading",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Use the graph of y = h(x) to answer each prompt (Workbook p. 49)\n$$\\text{A. } h(2) \\qquad \\text{B. } h(x) = -3; \\text{ find } x \\qquad \\text{C. } h(4) \\qquad \\text{D. } h(x) = -2; \\text{ find } x$$\n$$\\text{E. } x\\text{-intercept} \\qquad \\text{F. } y\\text{-intercept} \\qquad \\text{G. Slope } m$$",
    solution: "$$\\begin{aligned}\n\\mathbf{A.\\ } h(2):\\quad & \\text{Locate } x = 2 \\text{ on horizontal axis, find corresponding } y \\implies \\mathbf{h(2) = -1} \\\\[0.5em]\n\\mathbf{B.\\ } h(x) = -3:\\quad & \\text{Locate } y = -3 \\text{ on vertical axis, find corresponding } x \\implies \\mathbf{x = 0} \\\\[0.5em]\n\\mathbf{C.\\ } h(4):\\quad & \\text{At } x = 4, y = 1 \\implies \\mathbf{h(4) = 1} \\\\[0.5em]\n\\mathbf{D.\\ } h(x) = -2:\\quad & \\text{At } y = -2, x = 1 \\implies \\mathbf{x = 1} \\\\[0.5em]\n\\mathbf{E.\\ Intercepts:}\\quad & x\\text{-intercept: } \\mathbf{(3, 0)}, \\quad y\\text{-intercept: } \\mathbf{(0, -3)} \\\\[0.5em]\n\\mathbf{G.\\ Slope:}\\quad & m = \\frac{0 - (-3)}{3 - 0} = \\frac{3}{3} = \\mathbf{1}\n\\end{aligned}$$",
    pitfall: "**Which Axis to Start On:** For $h(2)$, start on the $x$-axis. For $h(x) = -3$, start on the $y$-axis!",
    script: "[Prof. Park] In Example 5 on page 49, reading graphs is all about knowing which axis is your starting point.\n\n[TA Sora] For $h(2)$, look at $x = 2$, go down to the line: $y = -1$. For $h(x) = -3$, look at $y = -3$, the line is right at $x = 0$!\n\n[Prof. Park] And the intercepts are $(3, 0)$ and $(0, -3)$, giving slope $m = 1$."
  }
];

const L27 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1: Graphing f(x) = 2x - 4 & Complete Analysis",
    subtitle: "Unit 2 • Lecture 27 • Section 2.6 Example 1 (Workbook p. 51)",
    detail: "Lecture 27: Graphing & Analyzing Linear Functions",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Graph the function f(x) = 2x - 4 and identify (Workbook p. 51)\n- Slope\n- $y$-intercept\n- $x$-intercept\n- Domain\n- Range",
    solution: "$$\\begin{aligned}\n\\mathbf{Slope:}\\quad & m = \\mathbf{2} = \\frac{2}{1} \\\\[0.6em]\n\\mathbf{y\\text{-intercept:}}\\quad & b = -4 \\implies \\mathbf{(0, -4)} \\\\[0.6em]\n\\mathbf{x\\text{-intercept:}}\\quad & 0 = 2x - 4 \\implies 2x = 4 \\implies \\mathbf{x = 2} \\implies \\mathbf{(2, 0)} \\\\[0.6em]\n\\mathbf{Domain:}\\quad & \\text{Every real number can be an input: } \\mathbf{(-\\infty, \\infty)} \\\\[0.6em]\n\\mathbf{Range:}\\quad & \\text{The line extends infinitely up and down: } \\mathbf{(-\\infty, \\infty)}\n\\end{aligned}$$",
    pitfall: "**Domain/Range of Non-Vertical Lines:** Every non-vertical straight line has Domain $(-\\infty, \\infty)$ and Range $(-\\infty, \\infty)$!",
    script: "[Prof. Park] Welcome to Lecture 27! Today on page 51, we study Linear Functions: $f(x) = mx + b$.\n\n[TA Sora] In Example 1, $f(x) = 2x - 4$. Slope is 2, $y$-intercept is $(0, -4)$, and setting $2x - 4 = 0$ gives $x$-intercept $(2, 0)$!\n\n[Prof. Park] And because the line goes forever left-to-right and bottom-to-top, both Domain and Range are $(-\\infty, \\infty)$."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2: Graphing g(x) = -x + 4 & Complete Analysis",
    subtitle: "Unit 2 • Lecture 27 • Section 2.6 Example 2 (Workbook p. 51)",
    detail: "Lecture 27: Graphing & Analyzing Linear Functions",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Graph the function g(x) = -x + 4 and identify (Workbook p. 51)\n- Slope\n- $y$-intercept\n- $x$-intercept\n- Domain\n- Range",
    solution: "$$\\begin{aligned}\n\\mathbf{Slope:}\\quad & m = \\mathbf{-1} = \\frac{-1}{1} \\\\[0.6em]\n\\mathbf{y\\text{-intercept:}}\\quad & b = 4 \\implies \\mathbf{(0, 4)} \\\\[0.6em]\n\\mathbf{x\\text{-intercept:}}\\quad & 0 = -x + 4 \\implies x = 4 \\implies \\mathbf{(4, 0)} \\\\[0.6em]\n\\mathbf{Domain:}\\quad & \\mathbf{(-\\infty, \\infty)} \\\\[0.6em]\n\\mathbf{Range:}\\quad & \\mathbf{(-\\infty, \\infty)}\n\\end{aligned}$$",
    pitfall: "**Negative Slope Direction:** $m = -1$ falls from left to right! Anchor at $(0, 4)$, down 1, right 1 to $(1, 3)$!",
    script: "[Prof. Park] In Example 2: $g(x) = -x + 4$. The coefficient of $x$ is $-1$, so slope is $-1$.\n\n[TA Sora] $y$-intercept is $(0, 4)$, $x$-intercept is $(4, 0)$, and Domain and Range are both $(-\\infty, \\infty)$!"
  }
];

const L28 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 4 & 5: Constructing Linear Function Models",
    subtitle: "Unit 2 • Lecture 28 • Section 2.6 Example 4 & 5 (Workbook p. 52)",
    detail: "Lecture 28: Constructing Linear Function Models",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Find the linear function equation for each (Workbook p. 52)\n$$\\mathbf{Example\\ 4:}\\quad h(x) \\text{ with slope } m = \\frac{3}{4} \\text{ and } y\\text{-intercept } (0, -5)$$\n$$\\mathbf{Example\\ 5:}\\quad k(x) \\text{ with slope } m = \\frac{1}{5} \\text{ passing through } (-5, 0)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Example\\ 4:}\\quad & \\text{Directly substitute } m = \\frac{3}{4} \\text{ and } b = -5 \\text{ into } h(x) = mx + b: \\\\\n& \\mathbf{h(x) = \\frac{3}{4}x - 5} \\\\[1em]\n\\mathbf{Example\\ 5:}\\quad & y - y_1 = m(x - x_1) \\implies y - 0 = \\frac{1}{5}(x - (-5)) \\\\\n& y = \\frac{1}{5}(x + 5) = \\frac{1}{5}x + 1 \\\\\n& \\text{Write in function notation: } \\mathbf{k(x) = \\frac{1}{5}x + 1}\n\\end{aligned}$$",
    pitfall: "**Use Function Names:** Use $h(x)$ or $k(x)$ as requested in the problem, NOT generic $y$!",
    script: "[Prof. Park] Welcome to Lecture 28! Today we are on page 52: Creating Linear Functions.\n\n[TA Sora] In Example 4, slope is $\\frac{3}{4}$ and $y$-intercept is $(0, -5)$, so $h(x) = \\frac{3}{4}x - 5$.\n\n[Prof. Park] In Example 5, through $(-5, 0)$ with slope $\\frac{1}{5}$: point-slope form gives $k(x) = \\frac{1}{5}x + 1$."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 6 & 7: Functions Through Two Points",
    subtitle: "Unit 2 • Lecture 28 • Section 2.6 Example 6 & 7 (Workbook p. 52)",
    detail: "Lecture 28: Constructing Linear Function Models",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Find the linear function equation for each (Workbook p. 52)\n$$\\mathbf{Example\\ 6:}\\quad f(x) \\text{ passing through } (2, 3) \\text{ and } (4, 9)$$\n$$\\mathbf{Example\\ 7:}\\quad g(x) \\text{ containing } (7, 9) \\text{ and } (-4, 9)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Example\\ 6:}\\quad & m = \\frac{9 - 3}{4 - 2} = \\frac{6}{2} = \\mathbf{3} \\\\\n& y - 3 = 3(x - 2) = 3x - 6 \\implies y = 3x - 3 \\\\\n& \\mathbf{f(x) = 3x - 3} \\\\[1em]\n\\mathbf{Example\\ 7:}\\quad & m = \\frac{9 - 9}{-4 - 7} = \\frac{0}{-11} = \\mathbf{0} \\\\\n& y - 9 = 0(x - 7) = 0 \\implies y = 9 \\\\\n& \\mathbf{g(x) = 9} \\quad [\\textbf{Constant Function}]\n\\end{aligned}$$",
    pitfall: "**Constant Function:** When $m = 0$, $g(x) = 0x + 9 = 9$. It outputs 9 for every input!",
    script: "[Prof. Park] In Example 6, points $(2, 3)$ and $(4, 9)$ give slope 3. Point-slope gives $f(x) = 3x - 3$.\n\n[TA Sora] In Example 7, both $y$-values are 9, so slope is 0. That's a horizontal constant function: $g(x) = 9$!"
  }
];

const L29 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Montana Applied Modeling",
    title: "Section 2.7: Applications — Kim's Bozeman Ski Rental",
    subtitle: "Unit 2 • Lecture 29 • Section 2.7 Example 1 (Workbook p. 53)",
    detail: "Lecture 29: Applications of Linear Functions: Bozeman Business & Depreciation",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Real-World Bozeman Business Modeling (Workbook p. 53)\nKim owns a ski rental business in Bozeman. His **monthly fixed costs are $2,450** (rent, utilities, supplies).\nAdditionally, Kim has one worker whom he pays **$15 per hour**.\n- Write a linear function $C(h)$ that models Kim's monthly cost in terms of $h$, the number of hours his employee works.\n- Find the monthly cost if Kim pays an employee to work **25 hours**.",
    solution: "$$\\begin{aligned}\n\\text{Model: } & C(h) = mh + b \\\\\n\\text{Rate of change (slope): } & m = 15\\text{ dollars/hour} \\\\\n\\text{Initial fixed cost (intercept): } & b = 2450\\text{ dollars} \\\\[0.8em]\n\\mathbf{\\text{Cost Function:}}\\quad & \\mathbf{C(h) = 15h + 2450} \\\\[1em]\n\\mathbf{\\text{For } h = 25\\text{ hours:}}\\quad & C(25) = 15(25) + 2450 \\\\\n& C(25) = 375 + 2450 = \\mathbf{2825\\text{ dollars}}\n\\end{aligned}$$",
    pitfall: "**Units in Real Life:** Always include units (dollars, hours) when answering applied word problems: Cost = $2,825 for 25 hours of work!",
    script: "[Prof. Park] Welcome to Lecture 29! Today we are on page 53: Applications of Linear Functions.\n\n[TA Sora] I love this problem! Kim runs a ski rental right here in Bozeman! Fixed cost is $2,450, and he pays $15 an hour. So $C(h) = 15h + 2450$!\n\n[Prof. Park] And for 25 hours of employee work: $15(25) + 2450 = 375 + 2450 = \\$2,825$ total cost."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2 & 3: Car Depreciation & Sales Commission",
    subtitle: "Unit 2 • Lecture 29 • Section 2.7 Example 2 & 3 (Workbook pp. 53–54)",
    detail: "Lecture 29: Applications of Linear Functions: Bozeman Business & Depreciation",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Vehicle Depreciation & Sales Commission (Workbook pp. 53–54)\n- **Example 2:** You purchased your car in 2023 for **$22,500**. It depreciates linearly by **$1,500 per year**. Write a function $V(t)$ for the value $t$ years after 2023.\n- **Example 3:** A salesperson sold **3 cars and earned $760**; the next week they sold **5 cars and earned $920**. Find linear function $E(x)$ for weekly earnings.",
    solution: "$$\\begin{aligned}\n\\mathbf{Example\\ 2\\ (Depreciation):}\\quad & \\text{Initial value: } b = 22500, \\quad \\text{Depreciation rate: } m = -1500 \\\\\n& \\mathbf{V(t) = -1500t + 22500} \\quad (\\text{or } V(t) = 22500 - 1500t) \\\\[1em]\n\\mathbf{Example\\ 3\\ (Commission):}\\quad & \\text{Points: } (3, 760) \\text{ and } (5, 920) \\\\\n& m = \\frac{920 - 760}{5 - 3} = \\frac{160}{2} = \\mathbf{80\\text{ dollars/car}} \\\\\n& E(x) - 760 = 80(x - 3) = 80x - 240 \\\\\n& \\mathbf{E(x) = 80x + 520} \\quad [\\text{Base salary: } 520\\text{ dollars}, \\text{ Commission: } 80\\text{ dollars/car}]\n\\end{aligned}$$",
    pitfall: "**Depreciation is Negative:** In Ex 2, value decreases, so slope MUST be negative: $-1500$!",
    script: "[Prof. Park] In Example 2, car value drops by $\$1,500$ each year: $V(t) = 22500 - 1500t$.\n\n[TA Sora] In Example 3, 3 cars earned $\$760$ and 5 cars earned $\$920$. The slope is $\\frac{160}{2} = \\$80$ per car. Point-slope gives $E(x) = 80x + 520$. The salesperson has a $\$520$ base salary plus $\$80$ per car sold!"
  }
];

const L30 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Montana Applied Modeling",
    title: "Section 2.7: Blood Pressure & Montana Elevation Modeling",
    subtitle: "Unit 2 • Lecture 30 • Section 2.7 Example 4 & 5 (Workbook pp. 54–55)",
    detail: "Lecture 30: Real-World Modeling (Elevation & Boiling Point) & Unit 2 Grand Review",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Real-World Modeling (Workbook pp. 54–55)\n- **Example 4 (Blood Pressure):** A 23-year-old has systolic pressure **120 mmHg**, while a 53-year-old has **132 mmHg**. Find $P(x)$ in terms of age $x$.\n- **Example 5 (Montana Elevation):** Water boils at **$212^\\circ\\text{F}$ at 0 ft** (sea level). Hiking to the **\"M\" in Bozeman (5,700 ft)**, water boils at **$200^\\circ\\text{F}$**. Find boiling point function $B(x)$.",
    solution: "$$\\begin{aligned}\n\\mathbf{Example\\ 4:}\\quad & \\text{Points: } (23, 120), (53, 132) \\\\\n& m = \\frac{132 - 120}{53 - 23} = \\frac{12}{30} = \\mathbf{0.4} \\\\\n& P(x) - 120 = 0.4(x - 23) = 0.4x - 9.2 \\implies \\mathbf{P(x) = 0.4x + 110.8} \\\\[1em]\n\\mathbf{Example\\ 5:}\\quad & \\text{Points: } (0, 212), (5700, 200) \\\\\n& m = \\frac{200 - 212}{5700 - 0} = \\frac{-12}{5700} = \\mathbf{-\\frac{1}{475}} \\approx -0.0021^\\circ\\text{F}/\\text{ft} \\\\\n& \\mathbf{B(x) = -\\frac{1}{475}x + 212} \\quad (\\text{or } B(x) = -0.0021x + 212)\n\\end{aligned}$$",
    pitfall: "**Bozeman Elevation Context:** Water boils at a lower temperature in Bozeman because atmospheric pressure is lower at 5,700 ft!",
    script: "[Prof. Park] Welcome to Lecture 30! Example 5 is a classic Montana State University problem: hiking up to the 'M' in the Bridger foothills at 5,700 feet!\n\n[TA Sora] At sea level, water boils at $212^\\circ\\text{F}$. But at the Bozeman 'M', it boils at $200^\\circ\\text{F}$! The slope is $-\\frac{12}{5700} = -\\frac{1}{475}$. So $B(x) = -\\frac{1}{475}x + 212$!"
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 6: Montana Grain Bin Depletion Model",
    subtitle: "Unit 2 • Lecture 30 • Section 2.7 Example 6 (Workbook p. 55)",
    detail: "Lecture 30: Real-World Modeling (Elevation & Boiling Point) & Unit 2 Grand Review",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Montana Agriculture Modeling (Workbook p. 55)\nIn 2001, the volume in a grain bin is **45 tons**. In 2025, there were only **15 tons remaining**.\n- Create a linear model $V(t)$ that represents the volume of grain left in the bin, $t$ years after 2000.\n- **Determine when the grain bin will be completely empty.**",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Convert years to } t \\text{ (years after 2000):} \\\\\n& 2001 \\implies t_1 = 1, \\quad V_1 = 45 \\implies (1, 45) \\\\\n& 2025 \\implies t_2 = 25, \\quad V_2 = 15 \\implies (25, 15) \\\\[0.8em]\n\\text{Step 2: } & \\text{Find slope } m = \\frac{15 - 45}{25 - 1} = \\frac{-30}{24} = \\mathbf{-1.25\\text{ tons/year}} \\\\[0.8em]\n\\text{Step 3: } & \\text{Point-slope equation: } V(t) - 45 = -1.25(t - 1) \\\\\n& V(t) = -1.25t + 1.25 + 45 \\implies \\mathbf{V(t) = -1.25t + 46.25} \\\\[0.8em]\n\\text{Step 4: } & \\text{Set } V(t) = 0 \\text{ to find when empty:} \\\\\n& 0 = -1.25t + 46.25 \\implies 1.25t = 46.25 \\implies \\mathbf{t = 37} \\\\\n& \\text{Year } 2000 + 37 = \\mathbf{\\text{Year } 2037}\n\\end{aligned}$$",
    pitfall: "**Convert t back to Calendar Year:** $t = 37$ means 37 years after 2000, which is the year 2037!",
    script: "[Prof. Park] In Example 6, grain depletion is measured from the base year 2000. $t = 1$ has 45 tons, and $t = 25$ has 15 tons.\n\n[TA Sora] Slope is $-1.25$ tons per year! The function is $V(t) = -1.25t + 46.25$. Setting volume to 0 gives $t = 37$—so the grain bin will be empty in 2037!"
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Course Milestone & Synthesis",
    title: "Unit 2 Grand Synthesis & Transition to Unit 3 (Quadratics)",
    subtitle: "Unit 2 • Lecture 30 • Unit 2 Complete Synthesis",
    detail: "Lecture 30: Real-World Modeling (Elevation & Boiling Point) & Unit 2 Grand Review",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Unit 2 Master Principles Recap (Sections 2.0 – 2.7)\n- **1. Cartesian Plane:** $(x, y)$, Quadrants I–IV, Axis points $(a, 0)$ and $(0, b)$.\n- **2. Slope:** $m = \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{\\text{Rise}}{\\text{Run}}$. Positive, negative, zero (horizontal), undefined (vertical).\n- **3. Parallel & Perpendicular:** Parallel ($m_1 = m_2$), Perpendicular ($m_1 \\cdot m_2 = -1$).\n- **4. Line Forms:** Slope-intercept ($y = mx + b$), Point-slope ($y - y_1 = m(x - x_1)$).\n- **5. Special Lines (HOY VUX):** Horizontal ($y = c, m = 0$), Vertical ($x = c, m = \\text{undefined}$).\n- **6. Functions:** Each input $x$ has exactly one output $y$. Passes Vertical Line Test.\n- **7. Function Notation:** $y = f(x)$, evaluating $f(a)$ vs solving $f(x) = k$.\n- **8. Linear Models:** $f(x) = mx + b$ where $m = \\text{rate}$ and $b = \\text{initial value}$.",
    solution: "$$\\mathbf{\\text{Unit 2 Mastered! Next Up: Unit 3 — Quadratic Functions, Factoring \\& Parabolas!}}$$",
    pitfall: "**Congratulations!** You have conquered two-thirds of M090 Introductory Algebra!",
    script: "[Prof. Park] Students, congratulations on mastering Unit 2 of M090 Introductory Algebra at Gallatin College MSU!\n\n[TA Sora] We have covered every graph, every slope, every function, and every real-world Montana word problem from page 29 to page 56!\n\n[Prof. Park] In Unit 3, we move from straight lines to curves: Quadratic Functions, Factoring, and Parabolas!\n\n[TA Sora] Go Bobcats! See you in Unit 3!"
  }
];

// Now load src/data/montanaSlidesData.js and append L16 to L30
let file = fs.readFileSync('src/data/montanaSlidesData.js', 'utf8');

// Update MONTANA_LECTURES array if not already present
const newLectures = [
  { id: 16, title: "Lecture 16: Intro to Graphing & The Cartesian Plane", active: true },
  { id: 17, title: "Lecture 17: Linear Equations in Two Variables & Intercepts", active: true },
  { id: 18, title: "Lecture 18: Slope-Intercept Form & Special Lines", active: true },
  { id: 19, title: "Lecture 19: The Slope of a Line & Rate of Change", active: true },
  { id: 20, title: "Lecture 20: Parallel & Perpendicular Lines", active: true },
  { id: 21, title: "Lecture 21: Finding the Equation of a Line (Point-Slope Form)", active: true },
  { id: 22, title: "Lecture 22: Equations of Parallel, Perpendicular & Special Lines", active: true },
  { id: 23, title: "Lecture 23: Intro to Functions, Domain & Range", active: true },
  { id: 24, title: "Lecture 24: Function Verification & The Vertical Line Test", active: true },
  { id: 25, title: "Lecture 25: Function Notation & Evaluating f(x)", active: true },
  { id: 26, title: "Lecture 26: Solving Equations with Function Notation & Graph Reading", active: true },
  { id: 27, title: "Lecture 27: Graphing & Analyzing Linear Functions", active: true },
  { id: 28, title: "Lecture 28: Constructing Linear Function Models", active: true },
  { id: 29, title: "Lecture 29: Applications of Linear Functions: Bozeman Business & Depreciation", active: true },
  { id: 30, title: "Lecture 30: Real-World Modeling (Elevation & Boiling Point) & Unit 2 Grand Review", active: true }
];

// Update MONTANA_LECTURES
const allLecturesMatch = file.match(/export const MONTANA_LECTURES = \[([\s\S]*?)\];/);
if (allLecturesMatch) {
  let existing = JSON.parse('[' + allLecturesMatch[1] + ']');
  // filter out existing 16-30 if any
  existing = existing.filter(l => l.id <= 15).concat(newLectures);
  const formattedLectures = JSON.stringify(existing, null, 2);
  file = file.replace(allLecturesMatch[0], `export const MONTANA_LECTURES = ${formattedLectures};`);
}

// Generate code for L16 to L30
const unit2Data = {
  16: L16,
  17: L17,
  18: L18,
  19: L19,
  20: L20,
  21: L21,
  22: L22,
  23: L23,
  24: L24,
  25: L25,
  26: L26,
  27: L27,
  28: L28,
  29: L29,
  30: L30
};

let exportStrings = '';
for (let num = 16; num <= 30; num++) {
  exportStrings += `export const SLIDES_MONTANA_L${num} = ${JSON.stringify(unit2Data[num], null, 2)};\n\n`;
}

// Cleanly slice from the end of L15
const l15Tag = 'export const SLIDES_MONTANA_L15 = [';
const l15Idx = file.indexOf(l15Tag);
const endOfL15 = file.indexOf('];', l15Idx) + 2;

file = file.slice(0, endOfL15) + '\n\n' + exportStrings + `export const MONTANA_ALL_SLIDES = {\n`;
for (let num = 1; num <= 30; num++) {
  const pad = num < 10 ? '0' + num : '' + num;
  file += `  ${num}: SLIDES_MONTANA_L${pad},\n`;
}
file += `};\n`;

fs.writeFileSync('src/data/montanaSlidesData.js', file, 'utf8');
console.log('Unit 2 (Lectures 16 to 30) cleanly written to src/data/montanaSlidesData.js!');
