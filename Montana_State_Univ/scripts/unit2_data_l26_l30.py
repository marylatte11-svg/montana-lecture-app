# Unit 2 Lectures 26 - 30 Data
# Faithful to M090 Workbook pp. 47 - 56

data_26_30 = {}

# L26: Section 2.5 Part 1 (Workbook pp. 47 - 48) - 8 slides
data_26_30[26] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Section 2.5: Function Notation f(x)",
        "subtitle": "Unit 2 • Lecture 26 • Section 2.5 (Workbook p. 47)",
        "detail": "Lecture 26: Function Notation & Algebraic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Decoding Function Notation (Workbook p. 47)\n$$\\mathbf{y = f(x)}$$\n- **$f$:** The **name** of the function (the rule or machine).\n- **$x$:** The **input** ($x$-coordinate of the ordered pair).\n- **$f(x)$:** The **output** value ($y$-coordinate of the ordered pair).\n- Read aloud as: **\"$f$ of $x$\"**.\n- Ordered Pair Representation: **$(x, f(x))$**",
        "solution": "$$\\begin{aligned}\n\\text{Equation notation: } & y = 4x - 5 \\\\\n\\text{Function notation: } & f(x) = 4x - 5 \\\\[0.5em]\n\\text{Input } x = 2: & f(2) = 4(2) - 5 = 8 - 5 = 3 \\\\\n\\text{Ordered pair: } & \\mathbf{(2, 3)} \\iff \\mathbf{(2, f(2))}\n\\end{aligned}$$",
        "pitfall": "**f(x) does NOT mean f times x!** The parentheses indicate the INPUT being fed into the function rule, NOT multiplication!",
        "script": "[Prof. Park] Welcome to Section 2.5! Today we master the universal language of modern mathematics: function notation $f(x)$.\n\n[TA Sora] $f(x)$ is simply a more informative replacement for $y$. It explicitly names the input inside the parentheses!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.5 Example 1 & 2: Comparing y and f(x)",
        "subtitle": "Unit 2 • Lecture 26 • Section 2.5 Examples 1 & 2 (Workbook p. 47)",
        "detail": "Lecture 26: Function Notation & Algebraic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Examples 1 & 2 (Workbook p. 47)\n- **Example 1:** Consider the linear equation $y = 4x - 5$. Find the value of $y$ when $x = 2$.\n- **Example 2:** Consider the linear function $f(x) = 4x - 5$. Find $f(2)$.\n- Plot the resulting point on the coordinate plane.",
        "solution": "$$\\begin{aligned}\n\\textbf{Example 1: } & y = 4(2) - 5 = 8 - 5 = \\mathbf{3} \\\\[0.5em]\n\\textbf{Example 2: } & f(2) = 4(2) - 5 = 8 - 5 = \\mathbf{3} \\\\[0.8em]\n\\mathbf{\\text{Result: }} & \\mathbf{(2, 3)} \\text{ on the graph of } y = 4x - 5.\n\\end{aligned}$$",
        "pitfall": "**Same math, better shorthand:** Notice how $f(2) = 3$ communicates both the input $2$ and output $3$ simultaneously!",
        "script": "[Prof. Park] Examples 1 and 2 perform the exact same mathematical substitution.\n\n[TA Sora] But $f(2) = 3$ is compact and tells us immediately that the point $(2, 3)$ is on the graph!",
        "graph": {
            "xMin": -2, "xMax": 5, "yMin": -6, "yMax": 6,
            "title": "Graph of f(x) = 4x - 5 with Point (2, f(2)) = (2, 3)",
            "points": [
                {"x": 2, "y": 3, "label": "(2, f(2)) = (2, 3)", "color": "#f59e0b"},
                {"x": 0, "y": -5, "label": "y-int (0, -5)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": 4, "yIntercept": -5, "color": "#38bdf8", "strokeWidth": 2.5, "label": "f(x) = 4x - 5"}
            ]
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Three Reasons Why Function Notation is Essential",
        "subtitle": "Unit 2 • Lecture 26 • Section 2.5 (Workbook p. 47)",
        "detail": "Lecture 26: Function Notation & Algebraic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Why We Use Function Notation (Workbook p. 47)\n1. **Guarantee of Single Output:** Writing $f(x)$ guarantees that the relation is indeed a function (passes the Vertical Line Test).\n2. **Naming Multiple Rules:** When working with several functions at once (cost $C(x)$, revenue $R(x)$, profit $P(x)$), distinct names prevent confusion.\n3. **Compact Input-Output Shorthand:** $f(2) = 3$ shows input and output in a single statement without saying 'when $x = 2$, $y = 3$'.",
        "solution": "$$\\begin{aligned}\n\\text{Instead of } y_1, y_2, y_3: & \\implies f(x), \\; g(x), \\; h(x) \\\\\n\\text{Instead of \"when } x=5, y=12\": & \\implies f(5) = 12 \\\\\n\\text{Corresponding point: } & (5, 12)\n\\end{aligned}$$",
        "pitfall": "**Don't divide by f:** If $f(x) = 10$, you CANNOT divide both sides by $f$. $f$ is a name, not a number!",
        "script": "[Prof. Park] In physics, economics, and business, you will encounter functions like $C(x)$ for cost and $R(x)$ for revenue.\n\n[TA Sora] Function notation lets us juggle multiple equations without ever mixing up our variables!"
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.5 Example 3A & 3B: Negative Inputs",
        "subtitle": "Unit 2 • Lecture 26 • Section 2.5 Example 3A, B (Workbook p. 48)",
        "detail": "Lecture 26: Function Notation & Algebraic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3A & 3B (Workbook p. 48)\nLet $\\mathbf{g(x) = -2x + 7}$ and $\\mathbf{h(x) = 3x - 5}$. Evaluate:\n- **A.** $g(-1)$\n- **B.** $h(-1)$\nUse proper notation with each step.",
        "solution": "$$\\begin{aligned}\n\\textbf{A. } g(-1) & = -2(-1) + 7 = 2 + 7 = \\mathbf{9} \\implies (-1, 9) \\\\[0.8em]\n\\textbf{B. } h(-1) & = 3(-1) - 5 = -3 - 5 = \\mathbf{-8} \\implies (-1, -8)\n\\end{aligned}$$",
        "pitfall": "**Parentheses on negative inputs:** Always wrap negative substitutions in parentheses: $-2(-1) = +2$, NOT $-2 - 1 = -3$!",
        "script": "[Prof. Park] In Example 3, notice which function is called: $g$ or $h$!\n\n[TA Sora] For $g(-1)$, plug $-1$ into $g$: $-2(-1) + 7 = 9$. For $h(-1)$, plug into $h$: $3(-1) - 5 = -8$!"
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.5 Example 3C & 3D: Evaluating at Zero & Y-Intercepts",
        "subtitle": "Unit 2 • Lecture 26 • Section 2.5 Example 3C, D (Workbook p. 48)",
        "detail": "Lecture 26: Function Notation & Algebraic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3C & 3D (Workbook p. 48)\nLet $\\mathbf{g(x) = -2x + 7}$ and $\\mathbf{h(x) = 3x - 5}$. Evaluate:\n- **C.** $h(0)$\n- **D.** $g(0)$\nWhat graphical feature do these outputs represent?",
        "solution": "$$\\begin{aligned}\n\\textbf{C. } h(0) & = 3(0) - 5 = 0 - 5 = \\mathbf{-5} \\implies \\mathbf{(0, -5) \\; [y\\text{-intercept of } h]} \\\\[0.8em]\n\\textbf{D. } g(0) & = -2(0) + 7 = 0 + 7 = \\mathbf{7} \\implies \\mathbf{(0, 7) \\; [y\\text{-intercept of } g]}\n\\end{aligned}$$",
        "pitfall": "**Evaluating at zero:** Evaluating any function at $x = 0$ ALWAYS gives the $y$-intercept of the graph!",
        "script": "[Prof. Park] Evaluating at $0$ reveals the $y$-intercept instantly. $h(0) = -5$ and $g(0) = 7$.\n\n[TA Sora] Both intercepts shine brightly on our coordinate grid!",
        "graph": {
            "xMin": -4, "xMax": 6, "yMin": -8, "yMax": 10,
            "title": "Intercepts: g(0) = 7 and h(0) = -5",
            "points": [
                {"x": 0, "y": 7, "label": "g(0) = (0, 7)", "color": "#38bdf8"},
                {"x": 0, "y": -5, "label": "h(0) = (0, -5)", "color": "#ec4899"}
            ],
            "lines": [
                {"slope": -2, "yIntercept": 7, "color": "#38bdf8", "strokeWidth": 2, "label": "g(x) = -2x + 7"},
                {"slope": 3, "yIntercept": -5, "color": "#ec4899", "strokeWidth": 2, "label": "h(x) = 3x - 5"}
            ]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.5 Example 3E & 3F: Fraction & Variable Inputs",
        "subtitle": "Unit 2 • Lecture 26 • Section 2.5 Example 3E, F (Workbook p. 48)",
        "detail": "Lecture 26: Function Notation & Algebraic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3E & 3F (Workbook p. 48)\nLet $\\mathbf{g(x) = -2x + 7}$ and $\\mathbf{h(x) = 3x - 5}$. Evaluate:\n- **E.** $g\\left(\\frac{5}{2}\\right)$\n- **F.** $h(a)$",
        "solution": "$$\\begin{aligned}\n\\textbf{E. } g\\left(\\frac{5}{2}\\right) & = -2\\left(\\frac{5}{2}\\right) + 7 = -5 + 7 = \\mathbf{2} \\implies \\left(\\frac{5}{2}, 2\\right) \\\\[0.8em]\n\\textbf{F. } h(a) & = 3(a) - 5 = \\mathbf{3a - 5}\n\\end{aligned}$$",
        "pitfall": "**Plugging in letters:** When the input is a variable like $a$, simply replace every $x$ with $a$. Do not try to solve for a number!",
        "script": "[Prof. Park] In 3E, $-2 \\cdot \\frac{5}{2}$ cancels the 2s, giving $-5 + 7 = 2$.\n\n[TA Sora] And in 3F, inputting $a$ into $h(x)$ simply gives $3a - 5$!"
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.5 Example 3G & 3H: Binomial Inputs",
        "subtitle": "Unit 2 • Lecture 26 • Section 2.5 Example 3G, H (Workbook p. 48)",
        "detail": "Lecture 26: Function Notation & Algebraic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3G & 3H (Workbook p. 48)\nLet $\\mathbf{g(x) = -2x + 7}$ and $\\mathbf{h(x) = 3x - 5}$. Evaluate:\n- **G.** $g(x - 7)$\n- **H.** $h(k + 1)$\nSubstitute the entire binomial expression into parentheses and distribute.",
        "solution": "$$\\begin{aligned}\n\\textbf{G. } g(x - 7) & = -2(x - 7) + 7 = -2x + 14 + 7 = \\mathbf{-2x + 21} \\\\[0.8em]\n\\textbf{H. } h(k + 1) & = 3(k + 1) - 5 = 3k + 3 - 5 = \\mathbf{3k - 2}\n\\end{aligned}$$",
        "pitfall": "**Distribute to BOTH terms:** $-2(x - 7) = -2x + 14$. A common mistake is forgetting to multiply the $-2$ by the $-7$!",
        "script": "[Prof. Park] In 3G and 3H, the inputs are expressions. Substitute with parentheses and distribute carefully.\n\n[TA Sora] $-2(x - 7) + 7 = -2x + 14 + 7 = -2x + 21$. Beautiful algebra!"
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.5 Example 4: Solving for x when f(x) = k",
        "subtitle": "Unit 2 • Lecture 26 • Section 2.5 Example 4 (Workbook p. 48)",
        "detail": "Lecture 26: Function Notation & Algebraic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4 (Workbook p. 48)\nLet $\\mathbf{f(x) = 5x + 3}$. Solve the following for $x$:\n- **A.** $f(x) = 18$\n- **B.** $f(x) = -8$\nNotice the difference: Here you are given the OUTPUT and must find the INPUT!",
        "solution": "$$\\begin{aligned}\n\\textbf{A. } f(x) = 18 \\implies 5x + 3 & = 18 \\\\\n5x & = 15 \\implies \\mathbf{x = 3} \\quad \\text{[Point: } (3, 18)] \\\\[0.8em]\n\\textbf{B. } f(x) = -8 \\implies 5x + 3 & = -8 \\\\\n5x & = -11 \\implies \\mathbf{x = -\\frac{11}{5} = -2.2} \\quad \\text{[Point: } (-2.2, -8)]\n\\end{aligned}$$",
        "pitfall": "**The Great Function Confusion:** 'Evaluate $f(3)$' means plug in $x = 3$ to find $y$. 'Solve $f(x) = 18$' means set the expression equal to $18$ and solve for $x$!",
        "script": "[Prof. Park] This is Sora's number one pitfall warning in all of algebra. Do not plug 18 into $x$!\n\n[TA Sora] Exactly! $f(x) = 18$ means the OUTPUT is 18. Set $5x + 3 = 18$ to solve for $x = 3$!"
    }
]

# L27: Section 2.5 Part 2 (Workbook pp. 49 - 50) - 8 slides
data_26_30[27] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Reading Function Values Directly from Graphs",
        "subtitle": "Unit 2 • Lecture 27 • Section 2.5 (Workbook p. 49)",
        "detail": "Lecture 27: Graph-Based Function Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Graph-to-Function Connections (Workbook p. 49)\nEvery point on the graph of $y = f(x)$ has the form:\n$$\\mathbf{(x, y) = (x, f(x))}$$\n- To find $\\mathbf{f(a)}$: Find $x = a$ on the horizontal axis, move vertically to the graph, and read the height $y$.\n- To solve $\\mathbf{f(x) = k}$: Find $y = k$ on the vertical axis, move horizontally to the graph, and read the $x$-position.",
        "solution": "$$\\begin{aligned}\n\\text{Given input } a: & \\text{Look on } x\\text{-axis} \\rightarrow \\text{find graph height } y = f(a) \\\\\n\\text{Given output } k: & \\text{Look on } y\\text{-axis} \\rightarrow \\text{find graph position } x \\text{ where } y = k\n\\end{aligned}$$",
        "pitfall": "**Horizontal vs Vertical Search:** Remember: Inputs are horizontal ($x$). Outputs are vertical ($y$)!",
        "script": "[Prof. Park] In Lecture 27, we learn how to read function notation directly from coordinate graphs without doing algebra on paper!\n\n[TA Sora] Let's look at Example 5 from page 49 of our Gallatin College MSU workbook."
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.5 Example 5 (Part 1): Finding h(2) and h(4)",
        "subtitle": "Unit 2 • Lecture 27 • Section 2.5 Example 5A, C (Workbook p. 49)",
        "detail": "Lecture 27: Graph-Based Function Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5A & 5C (Workbook p. 49)\nUse the graph of the function $y = h(x)$ shown below to answer:\n- **A.** $h(2) = \\underline{\hspace{2cm}}$\n- **C.** $h(4) = \\underline{\hspace{2cm}}$",
        "solution": "$$\\begin{aligned}\n\\textbf{A. } h(2): & \\text{Find } x = 2 \\text{ on } x\\text{-axis. Move up to the graph.} \\\\\n& \\text{The point is } (2, 1) \\implies \\mathbf{h(2) = 1} \\\\[0.8em]\n\\textbf{C. } h(4): & \\text{Find } x = 4 \\text{ on } x\\text{-axis. Move up to the graph.} \\\\\n& \\text{The point is } (4, 4) \\implies \\mathbf{h(4) = 4}\n\\end{aligned}$$",
        "pitfall": "**Ordered pair check:** $h(2) = 1$ corresponds to $(2, 1)$. $h(4) = 4$ corresponds to $(4, 4)$. Both points are highlighted on the grid!",
        "script": "[Prof. Park] On the graph of $h(x)$, when $x = 2$, the graph height is $1$. So $h(2) = 1$.\n\n[TA Sora] When $x = 4$, the graph height is $4$. So $h(4) = 4$!",
        "graph": {
            "xMin": -4, "xMax": 6, "yMin": -5, "yMax": 6,
            "title": "Graph of y = h(x): Evaluating h(2) = 1 and h(4) = 4",
            "points": [
                {"x": 2, "y": 1, "label": "h(2) = 1 -> (2, 1)", "color": "#f59e0b"},
                {"x": 4, "y": 4, "label": "h(4) = 4 -> (4, 4)", "color": "#38bdf8"}
            ],
            "lines": [
                {"slope": 1.5, "yIntercept": -2, "color": "#38bdf8", "strokeWidth": 2.5, "label": "h(x) = 1.5x - 2"}
            ]
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.5 Example 5 (Part 2): Solving h(x) = -3 and h(x) = -2",
        "subtitle": "Unit 2 • Lecture 27 • Section 2.5 Example 5B, D (Workbook p. 49)",
        "detail": "Lecture 27: Graph-Based Function Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5B & 5D (Workbook p. 49)\nUse the graph of $y = h(x)$ to solve:\n- **B.** $h(x) = -3$; find $x$.\n- **D.** $h(x) = -2$; find $x$.",
        "solution": "$$\\begin{aligned}\n\\textbf{B. } h(x) = -3: & \\text{Find } y = -3 \\text{ on } y\\text{-axis. Move horizontally to the line.} \\\\\n& \\text{At } y = -3, \\; x = -0.67 = -\\frac{2}{3} \\implies \\mathbf{x = -\\frac{2}{3}} \\\\[0.8em]\n\\textbf{D. } h(x) = -2: & \\text{Find } y = -2 \\text{ on } y\\text{-axis. The line crosses at } (0, -2). \\\\\n& \\text{Therefore, } \\mathbf{x = 0} \\quad (\\text{this is the } y\\text{-intercept!})\n\\end{aligned}$$",
        "pitfall": "**Finding x from y:** When $h(x) = -2$, look at height $-2$. The line hits the $y$-axis directly at $x = 0$!",
        "script": "[Prof. Park] In 5B and 5D, we start on the vertical axis and look horizontally for $x$.\n\n[TA Sora] At height $y = -2$, the graph is right on the $y$-axis, so $x = 0$!",
        "graph": {
            "xMin": -4, "xMax": 6, "yMin": -5, "yMax": 4,
            "title": "Solving h(x) = -2 at x = 0 (y-intercept)",
            "points": [
                {"x": 0, "y": -2, "label": "h(0) = -2", "color": "#10b981"},
                {"x": -2/3, "y": -3, "label": "h(-2/3) = -3", "color": "#ec4899"}
            ],
            "lines": [
                {"slope": 1.5, "yIntercept": -2, "color": "#38bdf8", "strokeWidth": 2.5, "label": "h(x)"},
                {"horizontal": -2, "color": "#10b981", "strokeWidth": 1.5, "dashed": True},
                {"horizontal": -3, "color": "#ec4899", "strokeWidth": 1.5, "dashed": True}
            ]
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.5 Example 5 (Part 3): Intercepts & Slope",
        "subtitle": "Unit 2 • Lecture 27 • Section 2.5 Example 5E, F, G (Workbook p. 49)",
        "detail": "Lecture 27: Graph-Based Function Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5E, F, G (Workbook p. 49)\nFrom the graph of $y = h(x)$:\n- **E. $x$-intercept:** ____________\n- **F. $y$-intercept:** ____________\n- **G. Slope ($m$):** ____________",
        "solution": "$$\\begin{aligned}\n\\mathbf{x\\text{-intercept: }} & \\mathbf{\\left(\\frac{4}{3}, 0\\right) \\approx (1.33, 0)} \\quad (\\text{where line crosses } x\\text{-axis}) \\\\[0.5em]\n\\mathbf{y\\text{-intercept: }} & \\mathbf{(0, -2)} \\quad (\\text{where line crosses } y\\text{-axis}) \\\\[0.5em]\n\\mathbf{\\text{Slope } m: } & \\text{From } (0, -2) \\text{ to } (2, 1): \\\\\n& m = \\frac{1 - (-2)}{2 - 0} = \\mathbf{\\frac{3}{2} = 1.5}\n\\end{aligned}$$",
        "pitfall": "**Slope triangle on graph:** Look at the slope triangle from $(0, -2)$ to $(2, 1)$: rise is $+3$, run is $+2$, giving $m = \\frac{3}{2}$!",
        "script": "[Prof. Park] In parts E, F, and G, we extract the complete formula of $h(x)$ from the graph: $y$-intercept $(0, -2)$, slope $\\frac{3}{2}$, giving $h(x) = \\frac{3}{2}x - 2$.\n\n[TA Sora] Everything connects seamlessly!",
        "graph": {
            "xMin": -3, "xMax": 5, "yMin": -4, "yMax": 4,
            "title": "h(x) Intercepts: (0, -2) and Slope m = 3/2",
            "points": [
                {"x": 0, "y": -2, "label": "y-int (0, -2)", "color": "#10b981"},
                {"x": 2, "y": 1, "label": "(2, 1)", "color": "#38bdf8"},
                {"x": 4/3, "y": 0, "label": "x-int (4/3, 0)", "color": "#f59e0b"}
            ],
            "lines": [
                {"slope": 1.5, "yIntercept": -2, "color": "#38bdf8", "strokeWidth": 2.5, "label": "h(x) = 3/2x - 2"}
            ],
            "slopeTriangle": {"x1": 0, "y1": -2, "x2": 2, "y2": 1, "rise": 3, "run": 2}
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.5 Practice #1 & #2: Multi-Function Practice",
        "subtitle": "Unit 2 • Lecture 27 • Section 2.5 Practice 1 & 2 (Workbook pp. 49-50)",
        "detail": "Lecture 27: Graph-Based Function Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Practice 1 & 2 (Workbook pp. 49–50)\nLet $\\mathbf{f(x) = 2x - 8}$ and $\\mathbf{g(x) = x - 9}$. Evaluate:\n- **1A.** $g(-2)$\n- **1B.** $f(4)$\n- **1C.** $g(0)$\n- **1D.** $g\\left(\\frac{1}{2}\\right)$\n- **2A.** $f\\left(-\\frac{1}{2}\\right)$",
        "solution": "$$\\begin{aligned}\n\\textbf{1A. } g(-2) & = -2 - 9 = \\mathbf{-11} \\\\[0.5em]\n\\textbf{1B. } f(4) & = 2(4) - 8 = 8 - 8 = \\mathbf{0} \\implies (4, 0) \\; [x\\text{-intercept of } f] \\\\[0.5em]\n\\textbf{1C. } g(0) & = 0 - 9 = \\mathbf{-9} \\implies (0, -9) \\; [y\\text{-intercept of } g] \\\\[0.5em]\n\\textbf{1D. } g\\left(\\frac{1}{2}\\right) & = \\frac{1}{2} - 9 = \\mathbf{-\\frac{17}{2} = -8.5} \\\\[0.5em]\n\\textbf{2A. } f\\left(-\\frac{1}{2}\\right) & = 2\\left(-\\frac{1}{2}\\right) - 8 = -1 - 8 = \\mathbf{-9}\n\\end{aligned}$$",
        "pitfall": "**Fraction operations:** $\\frac{1}{2} - 9 = \\frac{1}{2} - \\frac{18}{2} = -\\frac{17}{2}$. Always convert integers to common denominators!",
        "script": "[Prof. Park] In Practice 1 and 2, evaluate carefully. Notice $f(4) = 0$, which proves $(4, 0)$ is the $x$-intercept of $f(x)$!\n\n[TA Sora] And $g(0) = -9$ is the $y$-intercept of $g(x)$!"
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.5 Practice #3: Solving p(x) = 2x - 11",
        "subtitle": "Unit 2 • Lecture 27 • Section 2.5 Practice 3 (Workbook p. 50)",
        "detail": "Lecture 27: Graph-Based Function Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Practice 3 (Workbook p. 50)\nLet $\\mathbf{p(x) = 2x - 11}$. Solve the following for $x$:\n- **A.** $p(x) = -15$\n- **B.** $p(x) = 3$",
        "solution": "$$\\begin{aligned}\n\\textbf{A. } p(x) = -15 \\implies 2x - 11 & = -15 \\\\\n2x & = -4 \\implies \\mathbf{x = -2} \\quad [\\text{Point: } (-2, -15)] \\\\[0.8em]\n\\textbf{B. } p(x) = 3 \\implies 2x - 11 & = 3 \\\\\n2x & = 14 \\implies \\mathbf{x = 7} \\quad [\\text{Point: } (7, 3)]\n\\end{aligned}$$",
        "pitfall": "**Do not plug in for x:** $p(x) = 3$ means set the expression equal to $3$, add $11$, and divide by $2$!",
        "script": "[Prof. Park] Practice 3 asks us to solve for $x$. For part A, $2x - 11 = -15 \\implies 2x = -4 \\implies x = -2$.\n\n[TA Sora] And for part B, $2x - 11 = 3 \\implies 2x = 14 \\implies x = 7$!"
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.5 Practice #4: Reading Graph of f(x)",
        "subtitle": "Unit 2 • Lecture 27 • Section 2.5 Practice 4 (Workbook p. 50)",
        "detail": "Lecture 27: Graph-Based Function Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Practice 4 (Workbook p. 50)\nUse the graph of $y = f(x)$ below to answer:\n- **A.** $f(2) = \\underline{\hspace{2cm}}$\n- **B.** $f(x) = -3 \\implies x = \\underline{\hspace{2cm}}$\n- **C.** $f(1.5) = \\underline{\hspace{2cm}}$\n- **D.** $f(x) = -1 \\implies x = \\underline{\hspace{2cm}}$\n- **E, F, G.** Intercepts and Slope",
        "solution": "$$\\begin{aligned}\n\\textbf{A. } f(2) & = \\mathbf{1} \\implies (2, 1) \\\\[0.5em]\n\\textbf{B. } f(x) = -3 & \\implies \\mathbf{x = 0} \\implies (0, -3) \\; [y\\text{-intercept}] \\\\[0.5em]\n\\textbf{C. } f(1.5) & = \\mathbf{0} \\implies (1.5, 0) = \\left(\\frac{3}{2}, 0\\right) \\; [x\\text{-intercept}] \\\\[0.5em]\n\\textbf{D. } f(x) = -1 & \\implies \\mathbf{x = 1} \\implies (1, -1) \\\\[0.8em]\n\\mathbf{\\text{Slope } m: } & \\frac{1 - (-3)}{2 - 0} = \\frac{4}{2} = \\mathbf{2} \\implies \\mathbf{f(x) = 2x - 3}\n\\end{aligned}$$",
        "pitfall": "**Verification:** Notice that $f(x) = 2x - 3$ satisfies every single point: $f(2) = 2(2) - 3 = 1$; $f(1.5) = 2(1.5) - 3 = 0$!",
        "script": "[Prof. Park] In Practice 4, reading the graph confirms that $f(x) = 2x - 3$.\n\n[TA Sora] Look at how smoothly $(0, -3)$, $(1, -1)$, $(1.5, 0)$, and $(2, 1)$ all sit on the line!",
        "graph": {
            "xMin": -2, "xMax": 5, "yMin": -5, "yMax": 4,
            "title": "Practice 4: f(x) = 2x - 3 on Coordinate Grid",
            "points": [
                {"x": 0, "y": -3, "label": "y-int (0, -3)", "color": "#10b981"},
                {"x": 1.5, "y": 0, "label": "x-int (1.5, 0)", "color": "#f59e0b"},
                {"x": 2, "y": 1, "label": "f(2) = 1", "color": "#38bdf8"}
            ],
            "lines": [
                {"slope": 2, "yIntercept": -3, "color": "#38bdf8", "strokeWidth": 2.5, "label": "f(x) = 2x - 3"}
            ]
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 2.5 Mastery: Evaluation vs Solving",
        "subtitle": "Unit 2 • Lecture 27 • Section 2.5 Wrap-up",
        "detail": "Lecture 27: Graph-Based Function Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Golden Rule of Function Notation\n- **Evaluate $f(a)$:** $a$ is the input ($x$). Plug it into the formula to find output $y$.\n- **Solve $f(x) = b$:** $b$ is the output ($y$). Set the formula equal to $b$ and solve for input $x$.\n- On a coordinate graph, points are always **$(x, f(x))$**!",
        "solution": "$$\\mathbf{\\text{Section 2.5 Mastered! Next Up: Section 2.6 — Graphing Linear Functions!}}$$",
        "pitfall": "**Never confuse input and output:** Check the position: Inside parentheses = $x$. Outside after equals = $y$!",
        "script": "[Prof. Park] Outstanding work! You are now fluent in function notation.\n\n[TA Sora] In Lecture 28, we graph linear functions and connect them to real-world rates of change!"
    }
]

# L28: Section 2.6 (Workbook pp. 51 - 52) - 8 slides
data_26_30[28] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Section 2.6: Linear Functions f(x) = mx + b",
        "subtitle": "Unit 2 • Lecture 28 • Section 2.6 (Workbook p. 51)",
        "detail": "Lecture 28: Linear Functions & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Linear Functions (Workbook p. 51)\n$$\\mathbf{f(x) = mx + b}$$\n- $m$ is the **constant rate of change** (slope).\n- $(0, b)$ is the **vertical intercept** ($y$-intercept).\n- **Domain:** $(-\\infty, \\infty)$ for all non-vertical linear functions.\n- **Range:** $(-\\infty, \\infty)$ when $m \\neq 0$.\n  *(If $m = 0$, range is the single number $\\{b\\}$!)*",
        "solution": "$$\\begin{aligned}\n\\text{Formula: } & f(x) = mx + b \\\\\n\\text{Slope: } & m = \\frac{f(x_2) - f(x_1)}{x_2 - x_1} \\\\\n\\text{Intercept: } & (0, b)\n\\end{aligned}$$",
        "pitfall": "**Linear function range:** All linear functions with non-zero slope have range $(-\\infty, \\infty)$. Only constant functions $f(x) = c$ have range $\\{c\\}$!",
        "script": "[Prof. Park] Welcome to Section 2.6! Here we unite everything we know about lines and functions into $f(x) = mx + b$.\n\n[TA Sora] $m$ is the constant rate of change. It tells us how rapidly the function increases or decreases!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.6 Example 1: Graphing f(x) = 2x - 4",
        "subtitle": "Unit 2 • Lecture 28 • Section 2.6 Example 1 (Workbook p. 51)",
        "detail": "Lecture 28: Linear Functions & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 (Workbook p. 51)\nGraph the function $\\mathbf{f(x) = 2x - 4}$, and identify the following:\n- **Slope:** ____________\n- **$y$-intercept:** ____________\n- **$x$-intercept:** ____________\n- **Domain & Range** (in interval notation)",
        "solution": "$$\\begin{aligned}\n\\mathbf{\\text{Slope } m: } & \\mathbf{2} = \\frac{2}{1} \\\\[0.5em]\n\\mathbf{y\\text{-intercept: }} & \\mathbf{(0, -4)} \\\\[0.5em]\n\\mathbf{x\\text{-intercept: }} & 0 = 2x - 4 \\implies 2x = 4 \\implies \\mathbf{x = 2} \\implies \\mathbf{(2, 0)} \\\\[0.5em]\n\\mathbf{\\text{Domain: }} & \\mathbf{(-\\infty, \\infty)} \\\\\n\\mathbf{\\text{Range: }} & \\mathbf{(-\\infty, \\infty)}\n\\end{aligned}$$",
        "pitfall": "**Finding x-intercept in function notation:** Set $f(x) = 0$, NOT $x = 0$! Setting $f(x) = 0$ gives $2x - 4 = 0 \\implies x = 2$.",
        "script": "[Prof. Park] In Example 1, $f(x) = 2x - 4$. The $y$-intercept is $(0, -4)$ and the slope is $2$.\n\n[TA Sora] Setting $f(x) = 0$ yields $x = 2$. So the $x$-intercept is $(2, 0)$! Both intercepts are plotted on the grid.",
        "graph": {
            "xMin": -3, "xMax": 6, "yMin": -6, "yMax": 4,
            "title": "Example 1: f(x) = 2x - 4 (m = 2, b = -4)",
            "points": [
                {"x": 0, "y": -4, "label": "y-int (0, -4)", "color": "#10b981"},
                {"x": 2, "y": 0, "label": "x-int (2, 0)", "color": "#f59e0b"}
            ],
            "lines": [
                {"slope": 2, "yIntercept": -4, "color": "#38bdf8", "strokeWidth": 2.5, "label": "f(x) = 2x - 4"}
            ]
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.6 Example 2: Graphing g(x) = -x + 4",
        "subtitle": "Unit 2 • Lecture 28 • Section 2.6 Example 2 (Workbook p. 51)",
        "detail": "Lecture 28: Linear Functions & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2 (Workbook p. 51)\nGraph the function $\\mathbf{g(x) = -x + 4}$, and identify the following:\n- **Slope:** ____________\n- **$y$-intercept:** ____________\n- **$x$-intercept:** ____________\n- **Domain & Range** (in interval notation)",
        "solution": "$$\\begin{aligned}\n\\mathbf{\\text{Slope } m: } & \\mathbf{-1} = \\frac{-1}{1} \\\\[0.5em]\n\\mathbf{y\\text{-intercept: }} & \\mathbf{(0, 4)} \\\\[0.5em]\n\\mathbf{x\\text{-intercept: }} & 0 = -x + 4 \\implies x = 4 \\implies \\mathbf{(4, 0)} \\\\[0.5em]\n\\mathbf{\\text{Domain: }} & \\mathbf{(-\\infty, \\infty)} \\\\\n\\mathbf{\\text{Range: }} & \\mathbf{(-\\infty, \\infty)}\n\\end{aligned}$$",
        "pitfall": "**Negative slope:** In $g(x) = -x + 4$, the coefficient of $x$ is $-1$. The line falls at a 45-degree angle from left to right!",
        "script": "[Prof. Park] In Example 2, the slope is $-1$. It crosses the $y$-axis at $(0, 4)$ and the $x$-axis at $(4, 0)$.\n\n[TA Sora] Notice the symmetry! Both intercepts have a coordinate of 4.",
        "graph": {
            "xMin": -2, "xMax": 7, "yMin": -2, "yMax": 6,
            "title": "Example 2: g(x) = -x + 4 (m = -1)",
            "points": [
                {"x": 0, "y": 4, "label": "y-int (0, 4)", "color": "#10b981"},
                {"x": 4, "y": 0, "label": "x-int (4, 0)", "color": "#f59e0b"}
            ],
            "lines": [
                {"slope": -1, "yIntercept": 4, "color": "#38bdf8", "strokeWidth": 2.5, "label": "g(x) = -x + 4"}
            ]
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.6 Example 3: Domain, Range & Values from Graph",
        "subtitle": "Unit 2 • Lecture 28 • Section 2.6 Example 3 (Workbook p. 52)",
        "detail": "Lecture 28: Linear Functions & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3 (Workbook p. 52)\nUsing the graph at the right, answer:\n- **Domain:** (in interval notation)\n- **Range:** (in interval notation)\n- **$f(-2) = \\underline{\hspace{2cm}}$**\n- **When $f(x) = -4$, $x = \\underline{\hspace{2cm}}$**",
        "solution": "$$\\begin{aligned}\n\\mathbf{\\text{Domain: }} & \\mathbf{(-\\infty, \\infty)} \\\\\n\\mathbf{\\text{Range: }} & \\mathbf{(-\\infty, \\infty)} \\\\[0.5em]\n\\mathbf{f(-2): } & \\text{Find } x = -2 \\implies \\mathbf{f(-2) = 0} \\implies (-2, 0) \\\\[0.5em]\n\\mathbf{f(x) = -4: } & \\text{Find height } y = -4 \\implies \\mathbf{x = -4} \\implies (-4, -4)\n\\end{aligned}$$",
        "pitfall": "**Reading zero height:** When $x = -2$, the line sits directly on the horizontal axis, so $f(-2) = 0$!",
        "script": "[Prof. Park] Example 3 gives us a visual linear graph to interrogate.\n\n[TA Sora] At $x = -2$, the height is 0. And when height is $-4$, the $x$-value is $-4$!",
        "graph": {
            "xMin": -6, "xMax": 4, "yMin": -6, "yMax": 4,
            "title": "Example 3: Reading f(-2) = 0 and f(-4) = -4",
            "points": [
                {"x": -2, "y": 0, "label": "f(-2) = 0", "color": "#10b981"},
                {"x": -4, "y": -4, "label": "f(-4) = -4", "color": "#ec4899"}
            ],
            "lines": [
                {"slope": 2, "yIntercept": 4, "color": "#38bdf8", "strokeWidth": 2.5}
            ]
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.6 Example 4: Creating Function h(x)",
        "subtitle": "Unit 2 • Lecture 28 • Section 2.6 Example 4 (Workbook p. 52)",
        "detail": "Lecture 28: Linear Functions & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4 (Workbook p. 52)\nFind the equation of the linear function $h(x)$ that has a **slope of $\\frac{3}{4}$** and a **$y$-intercept at $(0, -5)$**.\n- Express the final answer in function notation $h(x) = mx + b$.",
        "solution": "$$\\begin{aligned}\n\\text{Given: } & m = \\frac{3}{4}, \\quad b = -5 \\\\[0.5em]\n\\text{Form: } & h(x) = mx + b \\\\[0.5em]\n\\mathbf{h(x)} & = \\mathbf{\\frac{3}{4}x - 5}\n\\end{aligned}$$",
        "pitfall": "**Use function name h(x):** The problem asked for $h(x)$, NOT $y$. Always write $h(x) = \\frac{3}{4}x - 5$ to receive full credit!",
        "script": "[Prof. Park] In Example 4, slope $m = \\frac{3}{4}$ and $y$-intercept $(0, -5)$ are given directly.\n\n[TA Sora] We write $h(x) = \\frac{3}{4}x - 5$. Look at how nicely it graphs on our coordinate grid!",
        "graph": {
            "xMin": -2, "xMax": 8, "yMin": -7, "yMax": 2,
            "title": "Example 4: h(x) = 3/4x - 5",
            "points": [
                {"x": 0, "y": -5, "label": "y-int (0, -5)", "color": "#10b981"},
                {"x": 4, "y": -2, "label": "(4, -2)", "color": "#38bdf8"}
            ],
            "lines": [
                {"slope": 0.75, "yIntercept": -5, "color": "#38bdf8", "strokeWidth": 2.5, "label": "h(x) = 3/4x - 5"}
            ]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.6 Example 5: Creating Function k(x)",
        "subtitle": "Unit 2 • Lecture 28 • Section 2.6 Example 5 (Workbook p. 52)",
        "detail": "Lecture 28: Linear Functions & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5 (Workbook p. 52)\nFind the equation of the linear function $k(x)$ that has a **slope of $\\frac{1}{5}$** and passes through the point **$(-5, 0)$**.\n- Use point-slope form with $k(x)$ replacing $y$.",
        "solution": "$$\\begin{aligned}\n\\text{Given: } & m = \\frac{1}{5}, \\quad (x_1, y_1) = (-5, 0) \\\\[0.5em]\ny - 0 & = \\frac{1}{5}(x - (-5)) \\\\[0.5em]\ny & = \\frac{1}{5}(x + 5) = \\frac{1}{5}x + 1 \\\\[0.5em]\n\\mathbf{k(x)} & = \\mathbf{\\frac{1}{5}x + 1}\n\\end{aligned}$$",
        "pitfall": "**Replace y with k(x):** In function problems, replace $y$ with $k(x)$ at the very end: $k(x) = \\frac{1}{5}x + 1$!",
        "script": "[Prof. Park] In Example 5, $(-5, 0)$ is an $x$-intercept. Distributing $\\frac{1}{5}(x + 5)$ gives $k(x) = \\frac{1}{5}x + 1$.\n\n[TA Sora] So the $y$-intercept is $(0, 1)$! Both points sit perfectly on our line.",
        "graph": {
            "xMin": -7, "xMax": 5, "yMin": -2, "yMax": 4,
            "title": "Example 5: k(x) = 1/5x + 1",
            "points": [
                {"x": -5, "y": 0, "label": "(-5, 0)", "color": "#f59e0b"},
                {"x": 0, "y": 1, "label": "(0, 1)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": 0.2, "yIntercept": 1, "color": "#38bdf8", "strokeWidth": 2.5, "label": "k(x) = 1/5x + 1"}
            ]
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.6 Example 6: Function through (2, 3) and (4, 9)",
        "subtitle": "Unit 2 • Lecture 28 • Section 2.6 Example 6 (Workbook p. 52)",
        "detail": "Lecture 28: Linear Functions & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 6 (Workbook p. 52)\nFind the equation of the linear function $f(x)$ that passes through the points **$(2, 3)$** and **$(4, 9)$**.\n- Calculate the slope $m$.\n- Use point-slope form to find $f(x)$.",
        "solution": "$$\\begin{aligned}\nm & = \\frac{9 - 3}{4 - 2} = \\frac{6}{2} = \\mathbf{3} \\\\[0.5em]\ny - 3 & = 3(x - 2) = 3x - 6 \\\\[0.5em]\ny & = 3x - 3 \\\\[0.5em]\n\\mathbf{f(x)} & = \\mathbf{3x - 3}\n\\end{aligned}$$",
        "pitfall": "**Check both points:** $f(2) = 3(2) - 3 = 3$ (works!). $f(4) = 3(4) - 3 = 9$ (works!). Verification takes only 5 seconds!",
        "script": "[Prof. Park] In Example 6, the rate of change is $\\frac{6}{2} = 3$. Point-slope gives $f(x) = 3x - 3$.\n\n[TA Sora] Both $(2, 3)$ and $(4, 9)$ line up with slope 3!",
        "graph": {
            "xMin": -1, "xMax": 6, "yMin": -4, "yMax": 11,
            "title": "Example 6: f(x) = 3x - 3 through (2, 3) and (4, 9)",
            "points": [
                {"x": 2, "y": 3, "label": "(2, 3)", "color": "#f59e0b"},
                {"x": 4, "y": 9, "label": "(4, 9)", "color": "#38bdf8"},
                {"x": 0, "y": -3, "label": "y-int (0, -3)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": 3, "yIntercept": -3, "color": "#38bdf8", "strokeWidth": 2.5, "label": "f(x) = 3x - 3"}
            ]
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.6 Example 7: Constant Function through (7, 9) and (-4, 9)",
        "subtitle": "Unit 2 • Lecture 28 • Section 2.6 Example 7 (Workbook p. 52)",
        "detail": "Lecture 28: Linear Functions & Rate of Change",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 7 (Workbook p. 52)\nFind the equation of the linear function $g(x)$ that contains the points **$(7, 9)$** and **$(-4, 9)$**.\n- Notice the shared coordinates!\n- State the equation in function notation.",
        "solution": "$$\\begin{aligned}\nm & = \\frac{9 - 9}{-4 - 7} = \\frac{0}{-11} = \\mathbf{0} \\\\[0.5em]\n\\text{Constant Function: } & g(x) = 0x + 9 \\\\[0.5em]\n\\mathbf{g(x)} & = \\mathbf{9} \\\\[0.5em]\n\\mathbf{\\text{Range: }} & \\mathbf{\\{9\\}}\n\\end{aligned}$$",
        "pitfall": "**Constant linear function:** When $m = 0$, $g(x) = 9$. It is a flat horizontal line with domain $(-\\infty, \\infty)$ and range $\\{9\\}$!",
        "script": "[Prof. Park] In Example 7, both outputs are 9. Slope is 0, so $g(x) = 9$.\n\n[TA Sora] A horizontal line at height 9! Notice that a constant function IS a function, unlike a vertical line!",
        "graph": {
            "xMin": -6, "xMax": 9, "yMin": 0, "yMax": 12,
            "title": "Example 7: Constant Function g(x) = 9",
            "points": [
                {"x": -4, "y": 9, "label": "(-4, 9)", "color": "#ec4899"},
                {"x": 7, "y": 9, "label": "(7, 9)", "color": "#38bdf8"}
            ],
            "lines": [
                {"horizontal": 9, "color": "#38bdf8", "strokeWidth": 2.5, "label": "g(x) = 9"}
            ]
        }
    }
]

# L29: Section 2.7 Part 1 (Workbook pp. 53 - 54) - 8 slides
data_26_30[29] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Section 2.7: Modeling with Linear Functions",
        "subtitle": "Unit 2 • Lecture 29 • Section 2.7 (Workbook p. 53)",
        "detail": "Lecture 29: Real-World Linear Modeling",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Modeling with Linear Functions (Workbook p. 53)\n$$\\mathbf{f(x) = mx + b}$$\nIn real-world applications:\n- **$m$ = Rate of Change:** (e.g. dollars per hour, miles per gallon, depreciation per year).\n- **$b$ = Initial Value / Fixed Cost:** (e.g. startup fee, purchase price, base charge at time $0$).\n- **Strategy:** Decide if you are directly given the rate $m$ and initial value $b$, or if you need to build two data points $(x_1, y_1)$ and $(x_2, y_2)$ from the story!",
        "solution": "$$\\begin{aligned}\n\\text{Case 1: } & \\text{Given rate } m \\text{ and initial value } b \\implies \\mathbf{f(x) = mx + b} \\\\\n\\text{Case 2: } & \\text{Given two scenarios } (x_1, y_1), \\; (x_2, y_2) \\implies m = \\frac{y_2 - y_1}{x_2 - x_1}, \\; \\text{then point-slope}\n\\end{aligned}$$",
        "pitfall": "**Units matter:** Always include units on the slope (e.g. 'dollars per hour') and the intercept (e.g. 'dollars')!",
        "script": "[Prof. Park] Welcome to Section 2.7! This is where algebra comes alive: modeling real Montana businesses, cars, and science.\n\n[TA Sora] $m$ is the rate of change, and $b$ is the starting point!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.7 Example 1 (Part 1): Kim's Bozeman Ski Rental Model",
        "subtitle": "Unit 2 • Lecture 29 • Section 2.7 Example 1 (Workbook p. 53)",
        "detail": "Lecture 29: Real-World Linear Modeling",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Kim's Bozeman Ski Rental (Workbook p. 53)\nKim owns a ski rental business in Bozeman. His monthly fixed costs are **$2450** (rent, utilities, supplies). Additionally, Kim pays his employee **$15 per hour**.\n- Write a linear function $C(h)$ that models Kim's monthly cost in terms of $h$, the number of hours his employee works.",
        "solution": "$$\\begin{aligned}\n\\text{Fixed cost (initial value } b): & 2450 \\text{ dollars} \\\\[0.5em]\n\\text{Hourly wage (rate } m): & 15 \\text{ dollars/hour} \\\\[0.5em]\n\\mathbf{C(h)} & = \\mathbf{15h + 2450}\n\\end{aligned}$$",
        "pitfall": "**Use variable h:** The prompt asks for $C(h)$, so use $h$ for hours, not $x$!",
        "script": "[Prof. Park] In Example 1, fixed costs are $2450 and hourly wage is $15.\n\n[TA Sora] The function is $C(h) = 15h + 2450$!"
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.7 Example 1 (Part 2): Monthly Cost for 25 Hours",
        "subtitle": "Unit 2 • Lecture 29 • Section 2.7 Example 1 Evaluation (Workbook p. 53)",
        "detail": "Lecture 29: Real-World Linear Modeling",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 Evaluation (Workbook p. 53)\nFind the monthly cost if Kim pays an employee to work **25 hours**.\n- Evaluate $C(25)$.\n- Plot the cost curve and highlight $(25, C(25))$.",
        "solution": "$$\\begin{aligned}\nC(25) & = 15(25) + 2450 \\\\[0.5em]\n& = 375 + 2450 \\\\[0.5em]\n\\mathbf{C(25)} & = \\mathbf{2825} \\\\[0.8em]\n\\mathbf{\\text{Sentence: }} & \\mathbf{\\text{The monthly cost for 25 employee hours is 2825 dollars.}}\n\\end{aligned}$$",
        "pitfall": "**Always state answers in context:** Don't just write $2825$. State what it means: Kim pays $2825 in total monthly costs!",
        "script": "[Prof. Park] Evaluating $C(25) = 15(25) + 2450 = 375 + 2450 = 2825 dollars.\n\n[TA Sora] Notice on the coordinate grid how the base cost starts at 2450 and rises linearly!",
        "graph": {
            "xMin": 0, "xMax": 40, "yMin": 2000, "yMax": 3200,
            "title": "Kim's Ski Rental Cost: C(h) = 15h + 2450",
            "points": [
                {"x": 0, "y": 2450, "label": "Fixed Cost (0, 2450)", "color": "#10b981"},
                {"x": 25, "y": 2825, "label": "C(25) = 2825", "color": "#f59e0b"}
            ],
            "lines": [
                {"slope": 15, "yIntercept": 2450, "color": "#38bdf8", "strokeWidth": 2.5, "label": "C(h) = 15h + 2450"}
            ]
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.7 Example 2 (Part 1): Car Depreciation Model",
        "subtitle": "Unit 2 • Lecture 29 • Section 2.7 Example 2 (Workbook p. 53)",
        "detail": "Lecture 29: Real-World Linear Modeling",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Car Depreciation (Workbook p. 53)\nYou purchased your car in 2023 for **$22,500**. You learned that the car would **depreciate linearly by $1500 per year**.\n- Write a function $V(t)$ that gives the value of the car $t$ years after 2023.",
        "solution": "$$\\begin{aligned}\n\\text{Initial purchase price } (b): & 22500 \\text{ dollars} \\\\[0.5em]\n\\text{Depreciation rate } (m): & \\mathbf{-1500} \\text{ dollars/year} \\quad (\\text{value decreases!}) \\\\[0.5em]\n\\mathbf{V(t)} & = \\mathbf{-1500t + 22500}\n\\end{aligned}$$",
        "pitfall": "**Depreciation means negative slope:** The car is LOSING value, so $m = -1500$, NOT $+1500$!",
        "script": "[Prof. Park] In Example 2, the car depreciates. Depreciation means decreasing value, so slope is negative $1500$.\n\n[TA Sora] Our function is $V(t) = -1500t + 22500$!"
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.7 Example 2 (Part 2): When is Car Value Zero?",
        "subtitle": "Unit 2 • Lecture 29 • Section 2.7 Example 2 Analysis (Workbook p. 53)",
        "detail": "Lecture 29: Real-World Linear Modeling",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2 Graph & Zero Value (Workbook p. 53)\nUsing $V(t) = -1500t + 22500$:\n- Find when the car's value reaches **$0** (the $t$-intercept).\n- What calendar year does this correspond to?",
        "solution": "$$\\begin{aligned}\n\\text{Set } V(t) = 0: & 0 = -1500t + 22500 \\\\[0.5em]\n1500t & = 22500 \\\\[0.5em]\nt & = \\frac{22500}{1500} = \\mathbf{15 \\text{ years}} \\\\[0.8em]\n\\text{Calendar Year: } & 2023 + 15 = \\mathbf{\\text{Year } 2038}\n\\end{aligned}$$",
        "pitfall": "**Calendar year interpretation:** $t = 15$ means 15 years after 2023, which is 2038!",
        "script": "[Prof. Park] Setting $V(t) = 0$ gives $t = 15$ years.\n\n[TA Sora] That means in the year 2038, the car's value will reach $0 on our coordinate graph!",
        "graph": {
            "xMin": 0, "xMax": 18, "yMin": 0, "yMax": 25000,
            "title": "Car Depreciation: V(t) = -1500t + 22500",
            "points": [
                {"x": 0, "y": 22500, "label": "Purchase (0, $22.5k)", "color": "#10b981"},
                {"x": 15, "y": 0, "label": "Zero Value (15, $0)", "color": "#ec4899"}
            ],
            "lines": [
                {"slope": -1500, "yIntercept": 22500, "color": "#38bdf8", "strokeWidth": 2.5, "label": "V(t)"}
            ]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.7 Example 3 (Part 1): Car Salesperson Commission Points",
        "subtitle": "Unit 2 • Lecture 29 • Section 2.7 Example 3 (Workbook p. 54)",
        "detail": "Lecture 29: Real-World Linear Modeling",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Car Salesperson Commission (Workbook p. 54)\nA salesperson earns commission on car sales:\n- Sold **3 cars**, earned **$760** for the week.\n- Sold **5 cars**, earned **$920** for the week.\nTranslate these two statements into ordered pairs $(x, E)$ where $x$ is cars sold and $E$ is weekly earnings.",
        "solution": "$$\\begin{aligned}\n\\text{Week 1: } & 3 \\text{ cars sold, } 760 \\text{ dollars earned} \\implies \\mathbf{(3, 760)} \\\\[0.5em]\n\\text{Week 2: } & 5 \\text{ cars sold, } 920 \\text{ dollars earned} \\implies \\mathbf{(5, 920)}\n\\end{aligned}$$",
        "pitfall": "**Identify variables correctly:** $x$ = number of cars (input), $E(x)$ = earnings in dollars (output).",
        "script": "[Prof. Park] In Example 3, we are not given the slope or intercept directly. We are given two data points!\n\n[TA Sora] $(3, 760)$ and $(5, 920)$. Now we can find the commission rate!"
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.7 Example 3 (Part 2): Commission Function E(x)",
        "subtitle": "Unit 2 • Lecture 29 • Section 2.7 Example 3 Solution (Workbook p. 54)",
        "detail": "Lecture 29: Real-World Linear Modeling",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3 Solution (Workbook p. 54)\nFind the linear function $E(x)$ that represents weekly earnings when $x$ cars are sold:\n- Calculate commission per car (slope $m$).\n- Use point-slope form to find base weekly salary (intercept $b$).",
        "solution": "$$\\begin{aligned}\nm & = \\frac{920 - 760}{5 - 3} = \\frac{160}{2} = \\mathbf{80 \\text{ dollars/car}} \\\\[0.5em]\nE - 760 & = 80(x - 3) \\\\[0.5em]\nE - 760 & = 80x - 240 \\\\[0.5em]\n\\mathbf{E(x)} & = \\mathbf{80x + 520} \\\\[0.8em]\n\\text{Interpretation: } & \\text{Base salary is } \\mathbf{520 \\text{ dollars/week}}, \\text{ plus } \\mathbf{80 \\text{ dollars per car sold}}.\n\\end{aligned}$$",
        "pitfall": "**Meaning of intercept:** $b = 520$ means if the salesperson sells 0 cars ($x = 0$), they still take home a base salary of $520!",
        "script": "[Prof. Park] The slope is 80 dollars per car. Point-slope reveals a base salary of 520 dollars.\n\n[TA Sora] So $E(x) = 80x + 520$. Both data points $(3, 760)$ and $(5, 920)$ sit right on the line!",
        "graph": {
            "xMin": 0, "xMax": 8, "yMin": 400, "yMax": 1100,
            "title": "Earnings Model: E(x) = 80x + 520",
            "points": [
                {"x": 0, "y": 520, "label": "Base Salary (0, $520)", "color": "#10b981"},
                {"x": 3, "y": 760, "label": "(3, $760)", "color": "#f59e0b"},
                {"x": 5, "y": 920, "label": "(5, $920)", "color": "#38bdf8"}
            ],
            "lines": [
                {"slope": 80, "yIntercept": 520, "color": "#38bdf8", "strokeWidth": 2.5, "label": "E(x) = 80x + 520"}
            ]
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 2.7 Part 1 Mastery Summary",
        "subtitle": "Unit 2 • Lecture 29 • Section 2.7 Wrap-up",
        "detail": "Lecture 29: Real-World Linear Modeling",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Real-World Modeling Takeaways\n- **Rate = Slope ($m$):** Watch for words like 'per', 'each', 'rate of', 'depreciates'.\n- **Initial Value = Intercept ($b$):** The value when input $x = 0$.\n- **Two Scenarios:** Build $(x_1, y_1)$ and $(x_2, y_2)$ and calculate $m = \\frac{y_2 - y_1}{x_2 - x_1}$.",
        "solution": "$$\\mathbf{\\text{Lecture 29 Complete! Next Up: Lecture 30 — Blood Pressure, Elevation \\& Unit 2 Grand Review!}}$$",
        "pitfall": "**Sentence answers:** Always conclude word problems with a complete English sentence describing the practical meaning of your solution!",
        "script": "[Prof. Park] You did a fantastic job modeling these real-world scenarios.\n\n[TA Sora] In Lecture 30, we hike up to the Bozeman 'M' and celebrate our mastery of Unit 2!"
    }
]

# L30: Section 2.7 Part 2 & Unit 2 Grand Review (Workbook pp. 54 - 56) - 8 slides
data_26_30[30] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.7 Example 4: Adult Systolic Blood Pressure Model",
        "subtitle": "Unit 2 • Lecture 30 • Section 2.7 Example 4 (Workbook p. 54)",
        "detail": "Lecture 30: Elevation, Grain Storage & Grand Review",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Adult Systolic Blood Pressure (Workbook p. 54)\nLet $x$ represent age in years and $P(x)$ represent systolic blood pressure in mmHg:\n- A **23-year-old** adult has a blood pressure of **120 mmHg** $\\implies (23, 120)$.\n- A **53-year-old** adult has a blood pressure of **132 mmHg** $\\implies (53, 132)$.\nFind the linear function $P(x)$.",
        "solution": "$$\\begin{aligned}\n\\text{Step 1: } & m = \\frac{132 - 120}{53 - 23} = \\frac{12}{30} = \\mathbf{0.4 \\text{ mmHg/year}} \\\\[0.5em]\n\\text{Step 2: } & P - 120 = 0.4(x - 23) \\\\[0.5em]\n& P - 120 = 0.4x - 9.2 \\\\[0.5em]\n\\mathbf{P(x)} & = \\mathbf{0.4x + 110.8}\n\\end{aligned}$$",
        "pitfall": "**Decimal slope:** $12/30 = 0.4$. That means on average, adult systolic blood pressure increases by $0.4$ mmHg every year of age!",
        "script": "[Prof. Park] In Example 4, we model medical data. Blood pressure rises at a rate of 0.4 mmHg per year of life.\n\n[TA Sora] The baseline model intercept at age 0 is 110.8 mmHg, giving $P(x) = 0.4x + 110.8$!",
        "graph": {
            "xMin": 10, "xMax": 70, "yMin": 110, "yMax": 140,
            "title": "Blood Pressure Model: P(x) = 0.4x + 110.8",
            "points": [
                {"x": 23, "y": 120, "label": "Age 23 (23, 120)", "color": "#10b981"},
                {"x": 53, "y": 132, "label": "Age 53 (53, 132)", "color": "#38bdf8"}
            ],
            "lines": [
                {"slope": 0.4, "yIntercept": 110.8, "color": "#38bdf8", "strokeWidth": 2.5, "label": "P(x)"}
            ]
        }
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.7 Example 5 (Part 1): Bozeman Elevation & Boiling Point",
        "subtitle": "Unit 2 • Lecture 30 • Section 2.7 Example 5 (Workbook p. 55)",
        "detail": "Lecture 30: Elevation, Grain Storage & Grand Review",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Bozeman Elevation vs Boiling Point (Workbook p. 55)\nThe relationship between elevation $x$ (in feet) and boiling point of water $B(x)$ (in $^\\circ$F):\n- At **0 ft elevation** (sea level camping), water boils at **$212^\\circ$F** $\\implies (0, 212)$.\n- Hiking up to the **Bozeman \"M\"** at **5700 ft elevation**, water boils at **$200^\\circ$F** $\\implies (5700, 200)$.\nIdentify the two ordered pairs and state the $y$-intercept.",
        "solution": "$$\\begin{aligned}\n\\text{Sea level point: } & (x_1, B_1) = \\mathbf{(0, 212)} \\quad (y\\text{-intercept } b = 212) \\\\[0.5em]\n\\text{Bozeman \"M\" point: } & (x_2, B_2) = \\mathbf{(5700, 200)}\n\\end{aligned}$$",
        "pitfall": "**Notice b is already given!** Because sea level is elevation $0$, $(0, 212)$ is our $y$-intercept directly!",
        "script": "[Prof. Park] In Example 5, we connect to Bozeman's famous 'M' trail on the Bridger foothills! Water boils at a lower temperature at higher elevations.\n\n[TA Sora] Because atmospheric pressure is lower! At 0 feet it boils at 212 degrees, but at 5700 feet it boils at 200 degrees."
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.7 Example 5 (Part 2): Boiling Point Function B(x)",
        "subtitle": "Unit 2 • Lecture 30 • Section 2.7 Example 5 Solution (Workbook p. 55)",
        "detail": "Lecture 30: Elevation, Grain Storage & Grand Review",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5 Solution (Workbook p. 55)\nWrite a linear function $B(x)$ that represents the boiling point of water in degrees Fahrenheit in terms of elevation $x$ in feet:\n- Calculate slope $m$.\n- Assemble the linear function.",
        "solution": "$$\\begin{aligned}\nm & = \\frac{200 - 212}{5700 - 0} = \\frac{-12}{5700} = \\mathbf{-\\frac{1}{475} \\; ^\\circ\\text{F/ft}} \\\\[0.6em]\n\\text{Since } b = 212: & \\\\\n\\mathbf{B(x)} & = \\mathbf{-\\frac{1}{475}x + 212}\n\\end{aligned}$$",
        "pitfall": "**Negative rate:** Boiling point drops as elevation increases, so the slope must be negative: $-\\frac{1}{475}$!",
        "script": "[Prof. Park] The slope simplifies to $-\\frac{1}{475}$ degrees per foot of elevation.\n\n[TA Sora] That means water boiling point drops by 1 degree Fahrenheit for every 475 feet you climb in Montana!",
        "graph": {
            "xMin": 0, "xMax": 7000, "yMin": 190, "yMax": 220,
            "title": "Boiling Point vs Elevation: B(x) = -1/475x + 212",
            "points": [
                {"x": 0, "y": 212, "label": "Sea Level (0, 212°F)", "color": "#10b981"},
                {"x": 5700, "y": 200, "label": "Bozeman 'M' (5700, 200°F)", "color": "#f59e0b"}
            ],
            "lines": [
                {"slope": -1/475, "yIntercept": 212, "color": "#38bdf8", "strokeWidth": 2.5, "label": "B(x)"}
            ]
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.7 Example 6 (Part 1): Montana Grain Bin Storage",
        "subtitle": "Unit 2 • Lecture 30 • Section 2.7 Example 6 (Workbook p. 55)",
        "detail": "Lecture 30: Elevation, Grain Storage & Grand Review",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Montana Grain Bin Depletion (Workbook p. 55)\nIn **2001**, the volume in a grain bin is **45 tons**. In **2025**, there were only **15 tons** remaining.\n- Create a linear model $V(t)$ that represents the volume of grain left in the bin, $t$ years after 2000.\n- State the data points in terms of $t$ (years after 2000).",
        "solution": "$$\\begin{aligned}\n2001 \\implies t_1 & = 2001 - 2000 = \\mathbf{1} \\implies \\mathbf{(1, 45)} \\\\[0.5em]\n2025 \\implies t_2 & = 2025 - 2000 = \\mathbf{25} \\implies \\mathbf{(25, 15)}\n\\end{aligned}$$",
        "pitfall": "**Base year offset:** Years are defined as $t$ years AFTER 2000! So 2001 is $t = 1$, NOT $t = 2001$!",
        "script": "[Prof. Park] In Montana agriculture, grain bins are vital for harvest storage. Here $t$ is measured from the year 2000.\n\n[TA Sora] So 2001 is $t=1$, and 2025 is $t=25$!"
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 2.7 Example 6 (Part 2): Grain Model & When Empty",
        "subtitle": "Unit 2 • Lecture 30 • Section 2.7 Example 6 Solution (Workbook p. 55)",
        "detail": "Lecture 30: Elevation, Grain Storage & Grand Review",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 6 Solution (Workbook p. 55)\n- Find the linear model $V(t)$.\n- **Determine when the grain bin will be completely empty.**",
        "solution": "$$\\begin{aligned}\n\\text{Step 1: } & m = \\frac{15 - 45}{25 - 1} = \\frac{-30}{24} = \\mathbf{-1.25 \\text{ tons/year}} \\\\[0.5em]\n\\text{Step 2: } & V - 45 = -1.25(t - 1) \\\\\n& V - 45 = -1.25t + 1.25 \\implies \\mathbf{V(t) = -1.25t + 46.25} \\\\[0.8em]\n\\text{Step 3: } & \\text{Set } V(t) = 0: \\\\\n& 0 = -1.25t + 46.25 \\implies 1.25t = 46.25 \\implies \\mathbf{t = 37} \\\\[0.5em]\n\\text{Calendar Year: } & 2000 + 37 = \\mathbf{\\text{Year } 2037}\n\\end{aligned}$$",
        "pitfall": "**Convert t back to calendar year:** $t = 37$ means 37 years after 2000, so the bin will empty in the year 2037!",
        "script": "[Prof. Park] Slope is $-1.25$ tons per year. The model is $V(t) = -1.25t + 46.25$.\n\n[TA Sora] Setting $V(t) = 0$ gives $t = 37$, so the grain bin will be completely empty in the year 2037!",
        "graph": {
            "xMin": 0, "xMax": 42, "yMin": 0, "yMax": 55,
            "title": "Grain Bin Depletion: V(t) = -1.25t + 46.25 (Empty at t = 37)",
            "points": [
                {"x": 1, "y": 45, "label": "2001 (1, 45)", "color": "#10b981"},
                {"x": 25, "y": 15, "label": "2025 (25, 15)", "color": "#38bdf8"},
                {"x": 37, "y": 0, "label": "Empty 2037 (37, 0)", "color": "#ec4899"}
            ],
            "lines": [
                {"slope": -1.25, "yIntercept": 46.25, "color": "#38bdf8", "strokeWidth": 2.5, "label": "V(t)"}
            ]
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Grand Synthesis & Review",
        "title": "Unit 2 Master Principles: The Linear Universe",
        "subtitle": "Unit 2 • Lecture 30 • Unit 2 Complete Synthesis",
        "detail": "Lecture 30: Elevation, Grain Storage & Grand Review",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Unit 2 Master Principles Recap (Sections 2.0 – 2.7)\n1. **Cartesian Coordinates:** $(x, y)$, Quadrants I–IV, Intercepts $(a, 0)$ and $(0, b)$.\n2. **Slope:** $m = \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{\\text{Rise}}{\\text{Run}}$.\n3. **Parallel & Perpendicular:** Parallel ($m_1 = m_2$), Perpendicular ($m_1 \\cdot m_2 = -1$).\n4. **Linear Forms:** Slope-intercept ($y = mx + b$), Point-slope ($y - y_1 = m(x - x_1)$).\n5. **Special Lines (HOY VUX):** Horizontal ($y = c, m = 0$), Vertical ($x = c, m = \\text{undefined}$).\n6. **Functions & VLT:** Every input has exactly one output. Passes Vertical Line Test.\n7. **Function Notation:** $y = f(x)$, evaluating $f(a)$ vs solving $f(x) = k$.\n8. **Linear Models:** $f(x) = mx + b$ where $m = \\text{rate}$ and $b = \\text{initial value}$.",
        "solution": "$$\\begin{array}{|c|c|c|}\n\\hline\n\\textbf{Topic} & \\textbf{Formula / Rule} & \\textbf{Key Application} \\\\\n\\hline\n\\text{Slope} & m = \\frac{y_2 - y_1}{x_2 - x_1} & \\text{Steepness \\& Direction} \\\\\n\\hline\n\\text{Point-Slope} & y - y_1 = m(x - x_1) & \\text{Writing any line} \\\\\n\\hline\n\\text{Parallel} & m_1 = m_2 & \\text{Same direction} \\\\\n\\hline\n\\text{Perpendicular} & m_1 \\cdot m_2 = -1 & 90^\\circ \\text{ intersection} \\\\\n\\hline\n\\text{Linear Function} & f(x) = mx + b & \\text{Real-world rates} \\\\\n\\hline\n\\end{array}$$",
        "pitfall": "**You have built a powerhouse algebraic foundation:** These 8 pillars will support everything you do in algebra and calculus!",
        "script": "[Prof. Park] Look at how much ground we have conquered together from page 29 to page 56 of the workbook!\n\n[TA Sora] You can graph any line, find any equation, test any function, and model any real-world problem!"
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Comprehensive Coordinate Grid",
        "title": "Unit 2 Master Coordinate Grid: All Line Types",
        "subtitle": "Unit 2 • Lecture 30 • Visual Comparison",
        "detail": "Lecture 30: Elevation, Grain Storage & Grand Review",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Visualizing Every Line Family on One Coordinate Plane\nObserve how all forms of lines coexist in the Cartesian coordinate system:\n- **Rising Line ($m > 0$):** $y = x + 1$ (Blue)\n- **Falling Line ($m < 0$):** $y = -x + 3$ (Pink)\n- **Horizontal Line (HOY):** $y = -2$ (Green)\n- **Vertical Line (VUX):** $x = 4$ (Gold)",
        "solution": "$$\\begin{aligned}\n\\text{Blue: } & y = x + 1 \\quad (m = +1 > 0) \\\\\n\\text{Pink: } & y = -x + 3 \\quad (m = -1 < 0) \\\\\n\\text{Green: } & y = -2 \\quad (m = 0, \\text{ HOY}) \\\\\n\\text{Gold: } & x = 4 \\quad (m = \\text{undefined}, \\text{ VUX})\n\\end{aligned}$$",
        "pitfall": "**Coordinate Plane Mastery:** The coordinate plane is a unified visual stage for every equation in algebra!",
        "script": "[Prof. Park] Here is the grand visual summary: positive slope, negative slope, zero slope, and undefined slope on one Cartesian plane.\n\n[TA Sora] A masterpiece of visual algebra!",
        "graph": {
            "xMin": -6, "xMax": 8, "yMin": -6, "yMax": 8,
            "title": "Master Coordinate Grid: All Line Types Coexisting",
            "points": [
                {"x": 1, "y": 2, "label": "Intersection (1, 2)", "color": "#f59e0b"},
                {"x": 4, "y": -2, "label": "(4, -2)", "color": "#10b981"}
            ],
            "lines": [
                {"slope": 1, "yIntercept": 1, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = x + 1 (m > 0)"},
                {"slope": -1, "yIntercept": 3, "color": "#ec4899", "strokeWidth": 2.5, "label": "y = -x + 3 (m < 0)"},
                {"horizontal": -2, "color": "#10b981", "strokeWidth": 2.5, "label": "y = -2 (m = 0)"},
                {"vertical": 4, "color": "#f59e0b", "strokeWidth": 2.5, "label": "x = 4 (m = undef)"}
            ]
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Course Milestone & Celebration",
        "title": "Unit 2 Mastered! Transition to Unit 3 (Quadratics)",
        "subtitle": "Unit 2 • Lecture 30 • Course Milestone",
        "detail": "Lecture 30: Elevation, Grain Storage & Grand Review",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Milestone Achieved: Two-Thirds of M090 Complete!\n- **Unit 1 Conquered:** Algebraic Expressions, Signed Numbers, Fractions, Equations, Inequalities.\n- **Unit 2 Conquered:** Cartesian Coordinates, Linear Equations, Slopes, Functions, Real-World Modeling.\n- **Coming Next in Unit 3:** Quadratic Functions, Factoring Polynomials, Solving Quadratic Equations, and Parabolas!",
        "solution": "$$\\mathbf{\\text{Unit 2 Complete! Onward to Unit 3: Quadratic Functions \\& Factoring!}}$$",
        "pitfall": "**Celebrate your achievement:** You have mastered two entire units of college developmental algebra!",
        "script": "[Prof. Park] Students, congratulations on mastering Unit 2 of M090 Introductory Algebra at Gallatin College MSU!\n\n[TA Sora] Every problem, every graph, every slope, and every real-world Montana model has been conquered!\n\n[Prof. Park] In Unit 3, we move from straight lines to curves: Quadratic Functions and Factoring!\n\n[TA Sora] Go Bobcats! See you in Unit 3!"
    }
]

print("Lectures 26 to 30 generated successfully!")
