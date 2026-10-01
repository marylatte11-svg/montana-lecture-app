# Unit 3 Lectures 36 - 40 Data
# Faithful to M090 Workbook pp. 67 - 79
# Focuses on Finding Intercepts: Square Root Property, Factoring, Completing the Square

data_36_40 = {}

# L36: Section 3.2 Part 1 (Workbook pp. 67 - 68) - 8 slides
data_36_40[36] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Finding x-Intercepts of Quadratic Functions",
        "subtitle": "Unit 3 • Lecture 36 • Section 3.2 (Workbook p. 67)",
        "detail": "Lecture 36: The Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### The Goal of Solving Quadratic Equations (Workbook p. 67)\nTo find the **$x$-intercepts** of any function $f(x)$, we set the output to zero:\n$$\\mathbf{f(x) = 0 \\implies ax^2 + bx + c = 0}$$\n- The real solutions to this equation are the **$x$-intercepts** $(x_1, 0)$ and $(x_2, 0)$ of the parabola.\n- When the linear term is missing ($b = 0$), the equation looks like **$x^2 = k$**.\n- This leads directly to our first algebraic method: **The Square Root Property**!",
        "solution": "$$\\begin{aligned}\n\\text{To find } y\\text{-intercept: } & \\text{Evaluate } f(0) = c \\implies (0, c) \\\\\n\\text{To find } x\\text{-intercepts: } & \\text{Solve } f(x) = 0 \\implies (x_1, 0), \\; (x_2, 0)\n\\end{aligned}$$",
        "pitfall": "**Never confuse the two intercepts:** $y$-intercept is found by plugging in $0$ for $x$. $x$-intercepts are found by setting $f(x) = 0$ and solving for $x$!",
        "script": "[Prof. Park] Welcome to Section 3.2! In this section, we transition from reading graphs to finding intercepts purely with algebra.\n\n[TA Sora] Finding $x$-intercepts means setting $f(x) = 0$. When there is no middle $x$ term, the Square Root Property is the fastest tool in the shed!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Formal Mathematical Rule",
        "title": "The Square Root Property (SRP)",
        "subtitle": "Unit 3 • Lecture 36 • Section 3.2 (Workbook p. 67)",
        "detail": "Lecture 36: The Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### The Square Root Property (Workbook p. 67)\n- **If $k > 0$ and $x^2 = k$, then:**\n  $$\\mathbf{x = \\pm \\sqrt{k}}$$\n  *(Two real solutions: $+\\sqrt{k}$ and $-\\sqrt{k}$)*\n- **If $x^2 = 0$, then:**\n  $$\\mathbf{x = 0}$$\n  *(One real solution)*\n- **If $k < 0$ and $x^2 = k$, then:**\n  $$\\mathbf{\\text{No Real Solutions}}$$\n  *(The parabola does not cross the $x$-axis!)*",
        "solution": "$$\\begin{aligned}\nx^2 = 9 & \\implies x = \\pm \\sqrt{9} = \\mathbf{\\pm 3} \\quad \\implies x = 3 \\text{ or } x = -3 \\\\\nx^2 = -9 & \\implies x = \\pm \\sqrt{-9} \\implies \\mathbf{\\text{No real number solution}}\n\\end{aligned}$$",
        "pitfall": "**The Plus-or-Minus Sign is MANDATORY:** When you take the square root of both sides to solve an equation, you MUST write $\\pm$! Writing only $x = 3$ misses half of the answers!",
        "script": "[Prof. Park] Look at $x^2 = 9$. Both $3^2 = 9$ AND $(-3)^2 = 9$. That's why the plus-or-minus sign is mandatory!\n\n[TA Sora] Sora's Rule: Whenever YOU introduce a square root to solve an equation, YOU must write the $\\pm$ sign!"
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.2 Example 1: Solving x^2 = 16",
        "subtitle": "Unit 3 • Lecture 36 • Section 3.2 Example 1 (Workbook p. 67)",
        "detail": "Lecture 36: The Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 (Workbook p. 67)\nSolve the equation for $x$:\n$$\\mathbf{x^2 = 16}$$\n- Apply the Square Root Property.\n- State both solutions and check them.",
        "solution": "$$\\begin{aligned}\nx^2 & = 16 \\\\[0.5em]\nx & = \\pm \\sqrt{16} \\\\[0.5em]\n\\mathbf{x} & = \\mathbf{\\pm 4} \\quad \\implies \\quad \\mathbf{x = 4 \\quad \\text{or} \\quad x = -4} \\\\[0.8em]\n\\text{Check: } & (4)^2 = 16 \\; (\\text{True}), \\quad (-4)^2 = 16 \\; (\\text{True})\n\\end{aligned}$$",
        "pitfall": "**Don't forget the negative root:** $-4$ is just as valid as $+4$. Both satisfy the equation perfectly.",
        "script": "[Prof. Park] In Example 1, $x^2 = 16 \\implies x = \\pm \\sqrt{16} = \\pm 4$.\n\n[TA Sora] Visually, the horizontal line $y = 16$ intersects the parabola $y = x^2$ at $x = -4$ and $x = +4$!",
        "graph": {
            "xMin": -6, "xMax": 6, "yMin": -2, "yMax": 20,
            "title": "Example 1: Intersections of y = x^2 and y = 16 at x = ±4",
            "points": [
                {"x": -4, "y": 16, "label": "(-4, 16)", "color": "#ec4899"},
                {"x": 4, "y": 16, "label": "(4, 16)", "color": "#38bdf8"}
            ],
            "curves": [
                {"a": 1, "b": 0, "c": 0, "color": "#38bdf8", "strokeWidth": 2.5, "label": "y = x^2"}
            ],
            "lines": [
                {"horizontal": 16, "color": "#f59e0b", "strokeWidth": 2, "dashed": True, "label": "y = 16"}
            ]
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.2 Example 2: Solving 2x^2 + 2 = 10",
        "subtitle": "Unit 3 • Lecture 36 • Section 3.2 Example 2 (Workbook p. 67)",
        "detail": "Lecture 36: The Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2 (Workbook p. 67)\nSolve the equation for $x$:\n$$\\mathbf{2x^2 + 2 = 10}$$\n- Isolate the $x^2$ term first.\n- Divide by the coefficient of $x^2$.\n- Apply the Square Root Property.",
        "solution": "$$\\begin{aligned}\n2x^2 + 2 & = 10 \\\\[0.5em]\n2x^2 & = 8 \\quad (\\text{subtract } 2) \\\\[0.5em]\nx^2 & = 4 \\quad (\\text{divide by } 2) \\\\[0.5em]\nx & = \\pm \\sqrt{4} \\\\[0.5em]\n\\mathbf{x} & = \\mathbf{\\pm 2} \\quad \\implies \\quad \\mathbf{x = 2 \\quad \\text{or} \\quad x = -2}\n\\end{aligned}$$",
        "pitfall": "**Isolate x^2 FIRST:** Do NOT take the square root of $2x^2 + 2$ directly! You must isolate $x^2$ alone before taking square roots!",
        "script": "[Prof. Park] In Example 2, isolate $x^2$ first. Subtract 2 to get $2x^2 = 8$, then divide by 2 to get $x^2 = 4$.\n\n[TA Sora] Now take square roots: $x = \\pm \\sqrt{4} = \\pm 2$!"
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.2 Example 3: Intercepts & Vertex for f(x) = x^2 - 36",
        "subtitle": "Unit 3 • Lecture 36 • Section 3.2 Example 3 (Workbook p. 67)",
        "detail": "Lecture 36: The Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3 (Workbook p. 67)\nFind the intercepts and vertex for the function:\n$$\\mathbf{f(x) = x^2 - 36}$$\n- **A. Find the $x$-intercept(s):** __________________________\n- **B. Find the $y$-intercept:** __________________________\n- **C. Find the vertex:** __________________________",
        "solution": "$$\\begin{aligned}\n\\textbf{A. x-intercepts: } & \\text{Set } f(x) = 0: x^2 - 36 = 0 \\implies x^2 = 36 \\\\\n& x = \\pm \\sqrt{36} = \\pm 6 \\implies \\mathbf{(6, 0) \\quad \\text{and} \\quad (-6, 0)} \\\\[0.8em]\n\\textbf{B. y-intercept: } & f(0) = 0^2 - 36 = -36 \\implies \\mathbf{(0, -36)} \\\\[0.8em]\n\\textbf{C. Vertex: } & x_v = -\\frac{0}{2(1)} = 0, \\; y_v = -36 \\implies \\mathbf{(0, -36)}\n\\end{aligned}$$",
        "pitfall": "**Intercept format:** Remember that intercepts are points on a plane: write $(6, 0)$ and $(-6, 0)$, not just $x = \\pm 6$!",
        "script": "[Prof. Park] Setting $x^2 - 36 = 0$ gives $x^2 = 36$, so $x = \\pm 6$. The $x$-intercepts are $(6, 0)$ and $(-6, 0)$.\n\n[TA Sora] And $f(0) = -36$, which means the vertex and $y$-intercept are the exact same point $(0, -36)$!",
        "graph": {
            "xMin": -9, "xMax": 9, "yMin": -42, "yMax": 10,
            "title": "Example 3: f(x) = x^2 - 36 (x-ints at ±6, Vertex at (0, -36))",
            "points": [
                {"x": -6, "y": 0, "label": "(-6, 0)", "color": "#f59e0b"},
                {"x": 6, "y": 0, "label": "(6, 0)", "color": "#f59e0b"},
                {"x": 0, "y": -36, "label": "Vertex & y-int (0, -36)", "color": "#38bdf8"}
            ],
            "curves": [
                {"a": 1, "b": 0, "c": -36, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 0
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.2 Example 4: Intercepts & Vertex for g(x) = 3x^2 - 27",
        "subtitle": "Unit 3 • Lecture 36 • Section 3.2 Example 4 (Workbook p. 68)",
        "detail": "Lecture 36: The Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4 (Workbook p. 68)\nFind the intercepts and vertex for the function:\n$$\\mathbf{g(x) = 3x^2 - 27}$$\n- **A. Find the $x$-intercept(s):** __________________________\n- **B. Find the $y$-intercept:** __________________________\n- **C. Find the vertex:** __________________________",
        "solution": "$$\\begin{aligned}\n\\textbf{A. x-intercepts: } & \\text{Set } g(x) = 0: 3x^2 - 27 = 0 \\implies 3x^2 = 27 \\\\\n& x^2 = 9 \\implies x = \\pm \\sqrt{9} = \\pm 3 \\\\\n& \\implies \\mathbf{(3, 0) \\quad \\text{and} \\quad (-3, 0)} \\\\[0.8em]\n\\textbf{B. y-intercept: } & g(0) = 3(0)^2 - 27 = -27 \\implies \\mathbf{(0, -27)} \\\\[0.8em]\n\\textbf{C. Vertex: } & \\mathbf{(0, -27)}\n\\end{aligned}$$",
        "pitfall": "**Divide before taking square root:** $3x^2 = 27 \\implies x^2 = 9$. Don't take square root until the coefficient 3 is cleared!",
        "script": "[Prof. Park] In Example 4, divide by 3 first: $x^2 = 9$, which gives $x = \\pm 3$.\n\n[TA Sora] The $x$-intercepts are $(3, 0)$ and $(-3, 0)$, and the vertex sits at $(0, -27)$!",
        "graph": {
            "xMin": -6, "xMax": 6, "yMin": -32, "yMax": 10,
            "title": "Example 4: g(x) = 3x^2 - 27 (x-ints at ±3)",
            "points": [
                {"x": -3, "y": 0, "label": "(-3, 0)", "color": "#f59e0b"},
                {"x": 3, "y": 0, "label": "(3, 0)", "color": "#f59e0b"},
                {"x": 0, "y": -27, "label": "Vertex (0, -27)", "color": "#38bdf8"}
            ],
            "curves": [
                {"a": 3, "b": 0, "c": -27, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 0
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "When x^2 = k Has No Real Solutions",
        "subtitle": "Unit 3 • Lecture 36 • Section 3.2 Negative Radicands",
        "detail": "Lecture 36: The Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### What Happens When $x^2 = -9$?\nSolve the equation $x^2 + 9 = 0$:\n- $x^2 = -9$\n- Can any real number squared equal a negative number?\n- What does this look like geometrically on the Cartesian coordinate plane?",
        "solution": "$$\\begin{aligned}\nx^2 & = -9 \\\\[0.5em]\nx & = \\pm \\sqrt{-9} \\\\[0.5em]\n\\mathbf{\\text{Conclusion: }} & \\mathbf{\\text{NO REAL NUMBER SOLUTION.}} \\\\[0.8em]\n\\text{Geometric Meaning: } & \\text{The parabola } f(x) = x^2 + 9 \\text{ has vertex at } (0, 9) \\\\\n& \\text{and opens UPWARD. It } \\mathbf{\\text{never crosses the }} x\\mathbf{\\text{-axis!}}\n\\end{aligned}$$",
        "pitfall": "**No real solution vs No solution:** In algebra of real numbers, $\\sqrt{-9}$ is not real, which means the graph has zero $x$-intercepts!",
        "script": "[Prof. Park] If you get $x^2 = -9$, stop! In real numbers, squares can never be negative.\n\n[TA Sora] Visually, the parabola sits entirely above the $x$-axis floating in space. It has no $x$-intercepts!",
        "graph": {
            "xMin": -5, "xMax": 5, "yMin": 0, "yMax": 20,
            "title": "Parabola f(x) = x^2 + 9 (Never Touches x-Axis)",
            "points": [
                {"x": 0, "y": 9, "label": "Vertex (0, 9)", "color": "#38bdf8"}
            ],
            "curves": [
                {"a": 1, "b": 0, "c": 9, "color": "#38bdf8", "strokeWidth": 2.5}
            ]
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 3.2 Part 1 Mastery Summary",
        "subtitle": "Unit 3 • Lecture 36 • Section 3.2 Wrap-up",
        "detail": "Lecture 36: The Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Lecture 36 Key Rules\n- **Square Root Property:** If $x^2 = k$ and $k > 0$, then $x = \\pm \\sqrt{k}$.\n- Always isolate $x^2$ before taking square roots.\n- $x$-intercepts are ordered pairs $(+\\sqrt{k}, 0)$ and $(-\\sqrt{k}, 0)$.\n- If $k < 0$, there are no real $x$-intercepts.",
        "solution": "$$\\mathbf{\\text{Lecture 36 Complete! Next Up: Lecture 37 — SRP with Binomial Squares } (x-h)^2 = k!}$$",
        "pitfall": "**Never forget the $\\pm$:** Write $\\pm$ the instant you write the square root radical!",
        "script": "[Prof. Park] Excellent job! In Lecture 37, we apply the Square Root Property to expressions with binomial squares like $(x - 3)^2 = 25$!"
    }
]

# L37: Section 3.2 Part 2 (Workbook pp. 69 - 70) - 8 slides
data_36_40[37] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Square Root Property with Binomial Squares: (x - h)^2 = k",
        "subtitle": "Unit 3 • Lecture 37 • Section 3.2 (Workbook p. 69)",
        "detail": "Lecture 37: Binomial Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### The Generalized Square Root Property (Workbook p. 69)\nWhen a binomial squared equals a constant:\n$$\\mathbf{(x - h)^2 = k}$$\n- Take the square root of both sides:\n  $$\\mathbf{x - h = \\pm \\sqrt{k}}$$\n- Add $h$ to both sides to isolate $x$:\n  $$\\mathbf{x = h \\pm \\sqrt{k}}$$\n- This produces two solutions: $x_1 = h + \\sqrt{k}$ and $x_2 = h - \\sqrt{k}$.",
        "solution": "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Ensure the squared term } (x - h)^2 \\text{ is isolated.} \\\\\n\\text{Step 2: } & \\text{Apply } \\pm \\sqrt{k}: \\quad x - h = \\pm \\sqrt{k}. \\\\\n\\text{Step 3: } & \\text{Add } h \\text{ in FRONT of the } \\pm: \\quad x = h \\pm \\sqrt{k}. \\\\\n\\text{Step 4: } & \\text{Calculate both numerical solutions if } k \\text{ is a perfect square.}\n\\end{aligned}$$",
        "pitfall": "**Put h in front of the $\\pm$ sign:** Writing $x = h \\pm \\sqrt{k}$ prevents you from accidentally putting $h$ inside the radical!",
        "script": "[Prof. Park] In Lecture 37, we solve equations where the entire left side is a binomial squared: $(x - h)^2 = k$.\n\n[TA Sora] Take the square root of both sides, drop the exponent 2, and add $h$ to both sides! It's that clean."
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.2 Example 5: Solving (x - 3)^2 = 25",
        "subtitle": "Unit 3 • Lecture 37 • Section 3.2 Example 5 (Workbook p. 69)",
        "detail": "Lecture 37: Binomial Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5 (Workbook p. 69)\nSolve the equation for $x$:\n$$\\mathbf{(x - 3)^2 = 25}$$\n- Apply the Square Root Property.\n- Separate into two arithmetic cases and simplify.",
        "solution": "$$\\begin{aligned}\n(x - 3)^2 & = 25 \\\\[0.5em]\nx - 3 & = \\pm \\sqrt{25} \\\\[0.5em]\nx - 3 & = \\pm 5 \\\\[0.5em]\nx & = 3 \\pm 5 \\\\[0.8em]\n\\text{Case 1: } & x = 3 + 5 = \\mathbf{8} \\\\\n\\text{Case 2: } & x = 3 - 5 = \\mathbf{-2} \\\\[0.8em]\n\\mathbf{\\text{Solutions: }} & \\mathbf{x = 8 \\quad \\text{and} \\quad x = -2}\n\\end{aligned}$$",
        "pitfall": "**Do not FOIL out $(x - 3)^2$!** Expanding $(x - 3)^2 = x^2 - 6x + 9 = 25$ wastes time and invites arithmetic errors. Take the square root directly!",
        "script": "[Prof. Park] In Example 5, take square roots immediately: $x - 3 = \\pm 5$. Adding 3 gives $3 \\pm 5$.\n\n[TA Sora] $3 + 5 = 8$, and $3 - 5 = -2$. Two integer solutions!"
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.2 Example 6: Intercepts & Vertex for f(x) = (x + 2)^2 - 9",
        "subtitle": "Unit 3 • Lecture 37 • Section 3.2 Example 6 (Workbook p. 69)",
        "detail": "Lecture 37: Binomial Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 6 (Workbook p. 69)\nFind the intercepts and vertex for the function:\n$$\\mathbf{f(x) = (x + 2)^2 - 9}$$\n- **A. Find the $x$-intercept(s):** __________________________\n- **B. Find the $y$-intercept:** __________________________\n- **C. Find the vertex:** __________________________",
        "solution": "$$\\begin{aligned}\n\\textbf{A. x-intercepts: } & \\text{Set } f(x) = 0: (x + 2)^2 - 9 = 0 \\implies (x + 2)^2 = 9 \\\\\n& x + 2 = \\pm \\sqrt{9} = \\pm 3 \\\\\n& x = -2 \\pm 3 \\implies x = -2 + 3 = \\mathbf{1}, \\quad x = -2 - 3 = \\mathbf{-5} \\\\\n& \\implies \\mathbf{(1, 0) \\quad \\text{and} \\quad (-5, 0)} \\\\[0.8em]\n\\textbf{B. y-intercept: } & f(0) = (0 + 2)^2 - 9 = 4 - 9 = \\mathbf{-5} \\implies \\mathbf{(0, -5)} \\\\[0.8em]\n\\textbf{C. Vertex: } & \\text{From vertex form: } \\mathbf{(-2, -9)}\n\\end{aligned}$$",
        "pitfall": "**Check vertex form:** Vertex is $(-2, -9)$. Notice the $x$-intercepts $1$ and $-5$ are spaced $\\pm 3$ units symmetrically around $x = -2$!",
        "script": "[Prof. Park] In Example 6, setting $(x + 2)^2 - 9 = 0$ gives $x + 2 = \\pm 3$.\n\n[TA Sora] So $x = -2 \\pm 3$, which gives $(1, 0)$ and $(-5, 0)$. And the vertex is $(-2, -9)$!",
        "graph": {
            "xMin": -7, "xMax": 3, "yMin": -11, "yMax": 5,
            "title": "Example 6: f(x) = (x + 2)^2 - 9 (Vertex (-2, -9), x-ints 1, -5)",
            "points": [
                {"x": -2, "y": -9, "label": "Vertex (-2, -9)", "color": "#38bdf8"},
                {"x": 0, "y": -5, "label": "y-int (0, -5)", "color": "#10b981"},
                {"x": 1, "y": 0, "label": "(1, 0)", "color": "#f59e0b"},
                {"x": -5, "y": 0, "label": "(-5, 0)", "color": "#f59e0b"}
            ],
            "curves": [
                {"a": 1, "b": 4, "c": -5, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": -2
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.2 Example 7: Solving 2(x - 4)^2 = 32",
        "subtitle": "Unit 3 • Lecture 37 • Section 3.2 Example 7 (Workbook p. 70)",
        "detail": "Lecture 37: Binomial Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 7 (Workbook p. 70)\nSolve the equation for $x$:\n$$\\mathbf{2(x - 4)^2 = 32}$$\n- Divide by 2 first to isolate $(x - 4)^2$.\n- Apply the Square Root Property.\n- Solve for both values of $x$.",
        "solution": "$$\\begin{aligned}\n2(x - 4)^2 & = 32 \\\\[0.5em]\n(x - 4)^2 & = 16 \\quad (\\text{divide by } 2) \\\\[0.5em]\nx - 4 & = \\pm \\sqrt{16} \\\\[0.5em]\nx - 4 & = \\pm 4 \\\\[0.5em]\nx & = 4 \\pm 4 \\\\[0.8em]\n\\text{Case 1: } & x = 4 + 4 = \\mathbf{8} \\\\\n\\text{Case 2: } & x = 4 - 4 = \\mathbf{0} \\\\[0.8em]\n\\mathbf{\\text{Solutions: }} & \\mathbf{x = 8 \\quad \\text{and} \\quad x = 0}\n\\end{aligned}$$",
        "pitfall": "**Do not distribute 2 into parentheses:** $(x - 4)$ is protected by the exponent 2! You CANNOT distribute 2 into $(x - 4)$! Divide by 2 instead!",
        "script": "[Prof. Park] In Example 7, divide both sides by 2 first to get $(x - 4)^2 = 16$.\n\n[TA Sora] Taking square roots gives $x - 4 = \\pm 4 \\implies x = 4 \\pm 4$, so $x = 8$ or $x = 0$!"
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.2 Example 8: Non-Perfect Squares and Radicals",
        "subtitle": "Unit 3 • Lecture 37 • Section 3.2 Example 8 (Workbook p. 70)",
        "detail": "Lecture 37: Binomial Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 8 (Workbook p. 70)\nSolve the equation for $x$:\n$$\\mathbf{(x - 1)^2 = 12}$$\n- Apply the Square Root Property.\n- Simplify the radical $\\sqrt{12} = \\sqrt{4 \\cdot 3} = 2\\sqrt{3}$.\n- Express the exact answers in simplified radical form.",
        "solution": "$$\\begin{aligned}\n(x - 1)^2 & = 12 \\\\[0.5em]\nx - 1 & = \\pm \\sqrt{12} \\\\[0.5em]\nx - 1 & = \\pm \\sqrt{4 \\cdot 3} = \\pm 2\\sqrt{3} \\\\[0.5em]\n\\mathbf{x} & = \\mathbf{1 \\pm 2\\sqrt{3}} \\\\[0.8em]\n\\text{Two exact roots: } & \\mathbf{x = 1 + 2\\sqrt{3}} \\quad \\text{and} \\quad \\mathbf{x = 1 - 2\\sqrt{3}}\n\\end{aligned}$$",
        "pitfall": "**Do not combine 1 and 2:** $1 \\pm 2\\sqrt{3}$ CANNOT be simplified to $3\\sqrt{3}$! $1$ is a rational number and $2\\sqrt{3}$ is irrational; they are not like terms!",
        "script": "[Prof. Park] In Example 8, 12 is not a perfect square. We simplify $\\sqrt{12} = 2\\sqrt{3}$.\n\n[TA Sora] Adding 1 gives $1 \\pm 2\\sqrt{3}$. Remember: do NOT add 1 and 2 together! $1$ and $2\\sqrt{3}$ are not like terms!"
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Application & Decimal Approximation",
        "title": "Exact Radical Form vs Decimal Approximations",
        "subtitle": "Unit 3 • Lecture 37 • Section 3.2 Approximations",
        "detail": "Lecture 37: Binomial Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Working with Irrational Roots\nFor $x = 1 \\pm 2\\sqrt{3}$:\n- Compute the decimal approximations using $\\sqrt{3} \\approx 1.732$.\n- Verify where these points lie on the $x$-axis of the coordinate plane.",
        "solution": "$$\\begin{aligned}\n\\sqrt{3} & \\approx 1.732 \\\\[0.5em]\n2\\sqrt{3} & \\approx 2(1.732) = 3.464 \\\\[0.5em]\n\\mathbf{x_1} & = 1 + 2\\sqrt{3} \\approx 1 + 3.464 = \\mathbf{4.46} \\implies \\mathbf{(4.46, 0)} \\\\[0.5em]\n\\mathbf{x_2} & = 1 - 2\\sqrt{3} \\approx 1 - 3.464 = \\mathbf{-2.46} \\implies \\mathbf{(-2.46, 0)}\n\\end{aligned}$$",
        "pitfall": "**Exam instruction awareness:** If the exam asks for 'exact form', write $1 \\pm 2\\sqrt{3}$. If it asks for 'round to nearest tenth', write $4.5$ and $-2.5$!",
        "script": "[Prof. Park] Exact form is $1 \\pm 2\\sqrt{3}$. On a graph, that corresponds to approximately $4.46$ and $-2.46$.\n\n[TA Sora] Notice on the coordinate grid how the parabola crosses the $x$-axis right around $-2.5$ and $4.5$!",
        "graph": {
            "xMin": -5, "xMax": 7, "yMin": -14, "yMax": 4,
            "title": "Irrational x-intercepts at approximately -2.46 and 4.46",
            "points": [
                {"x": 1, "y": -12, "label": "Vertex (1, -12)", "color": "#38bdf8"},
                {"x": 4.46, "y": 0, "label": "(4.46, 0)", "color": "#f59e0b"},
                {"x": -2.46, "y": 0, "label": "(-2.46, 0)", "color": "#f59e0b"}
            ],
            "curves": [
                {"a": 1, "b": -2, "c": -11, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 1
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Sora's Pro-Tip",
        "title": "Sora's Checklist for the Square Root Property",
        "subtitle": "Unit 3 • Lecture 37 • Section 3.2 Checklist",
        "detail": "Lecture 37: Binomial Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### When to Use the Square Root Property\n- **Use SRP when:**\n  - Equation has an isolated square: $x^2 = k$ or $(x - h)^2 = k$.\n  - There is NO separate linear $x$ term outside the parentheses.\n- **Do NOT use SRP directly if:**\n  - Equation has both $x^2$ and $x$ separated: e.g. $x^2 - 5x + 6 = 0$.\n  *(For that, we use Factoring or Completing the Square!)*",
        "solution": "$$\\begin{array}{|c|c|c|} \n\\hline\n\\textbf{Equation} & \\textbf{Use SRP?} & \\textbf{Reason} \\\\\n\\hline\n(x - 5)^2 = 16 & \\textbf{YES} & \\text{Isolated binomial square} \\\\\n\\hline\n3x^2 = 75 & \\textbf{YES} & \\text{Isolate } x^2 = 25 \\\\\n\\hline\nx^2 - 6x + 8 = 0 & \\textbf{NO} & \\text{Has linear term } -6x \\; (\\text{use Factoring}) \\\\\n\\hline\n\\end{array}$$",
        "pitfall": "**Pattern recognition:** Recognizing which tool fits which equation is what makes math easy!",
        "script": "[Prof. Park] This table teaches pattern recognition. If you see a complete square, use the Square Root Property!\n\n[TA Sora] If you see a full trinomial with a middle term, use Factoring—which is our next lecture!"
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 3.2 Complete Mastery Summary",
        "subtitle": "Unit 3 • Lecture 37 • Section 3.2 Wrap-up",
        "detail": "Lecture 37: Binomial Square Root Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Section 3.2 Master Summary\n- $(x - h)^2 = k \\implies x - h = \\pm\\sqrt{k} \\implies x = h \\pm \\sqrt{k}$.\n- Always simplify radicals to lowest terms ($\n\\sqrt{12} = 2\\sqrt{3}$).\n- If $k$ is not a perfect square, keep exact radical form unless decimals are requested.",
        "solution": "$$\\mathbf{\\text{Section 3.2 Mastered! Next Up: Section 3.3 — Finding Intercepts by Factoring!}}$$",
        "pitfall": "**Next Challenge:** What do we do when equations have both $x^2$ AND $x$? In Section 3.3, we master Factoring and the Zero Product Property!",
        "script": "[Prof. Park] Superb work on the Square Root Property! You have mastered solving pure squares.\n\n[TA Sora] In Lecture 38, we learn how to factor trinomials to find $x$-intercepts!"
    }
]

# L38: Section 3.3 Part 1 (Workbook pp. 71 - 72) - 8 slides
data_36_40[38] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Section 3.3: Finding Intercepts by Factoring",
        "subtitle": "Unit 3 • Lecture 38 • Section 3.3 (Workbook p. 71)",
        "detail": "Lecture 38: Factoring & Zero Product Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### The Power of Factoring (Workbook p. 71)\nWhen a quadratic function has all three terms ($ax^2 + bx + c$), we set $f(x) = 0$:\n$$\\mathbf{ax^2 + bx + c = 0}$$\n- If the trinomial can be factored into two binomials:\n  $$\\mathbf{(x - r_1)(x - r_2) = 0}$$\n- We apply the **Zero Product Property** to solve each factor separately!",
        "solution": "$$\\begin{aligned}\n\\text{Zero Product Property: } & \\text{If } A \\cdot B = 0, \\text{ then } \\mathbf{A = 0} \\text{ or } \\mathbf{B = 0}. \\\\[0.5em]\n(x - 2)(x - 3) = 0 & \\implies x - 2 = 0 \\implies \\mathbf{x = 2} \\\\\n& \\text{or } x - 3 = 0 \\implies \\mathbf{x = 3}\n\\end{aligned}$$",
        "pitfall": "**Must equal ZERO:** The Zero Product Property ONLY works if the other side equals $0$! If $(x - 2)(x - 3) = 12$, you CANNOT set $x - 2 = 12$!",
        "script": "[Prof. Park] Welcome to Section 3.3! The Zero Product Property is one of the most powerful theorems in algebra.\n\n[TA Sora] If two numbers multiply to 0, at least one of them MUST be 0! That lets us break a quadratic into two simple linear equations."
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.3 Example 1: Solving x^2 - 5x + 6 = 0",
        "subtitle": "Unit 3 • Lecture 38 • Section 3.3 Example 1 (Workbook p. 71)",
        "detail": "Lecture 38: Factoring & Zero Product Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 (Workbook p. 71)\nFind the $x$-intercepts for $\\mathbf{f(x) = x^2 - 5x + 6}$ by factoring:\n- Set $x^2 - 5x + 6 = 0$.\n- Find two numbers that multiply to $+6$ and add to $-5$.\n- Apply the Zero Product Property.",
        "solution": "$$\\begin{aligned}\nx^2 - 5x + 6 & = 0 \\\\[0.5em]\n\\text{Find factors of } 6 \\text{ adding to } -5: & \\quad (-2) \\cdot (-3) = +6, \\quad (-2) + (-3) = -5 \\\\[0.5em]\n(x - 2)(x - 3) & = 0 \\\\[0.5em]\nx - 2 = 0 & \\implies \\mathbf{x = 2} \\\\\nx - 3 = 0 & \\implies \\mathbf{x = 3} \\\\[0.8em]\n\\mathbf{x\\text{-intercepts: }} & \\mathbf{(2, 0) \\quad \\text{and} \\quad (3, 0)}\n\\end{aligned}$$",
        "pitfall": "**Signs flip when solving:** The factors are $(x - 2)$ and $(x - 3)$, but the solutions are $x = +2$ and $x = +3$! Setting each to zero flips the sign.",
        "script": "[Prof. Park] In Example 1, $-2$ and $-3$ multiply to $+6$ and add to $-5$. The factors are $(x - 2)(x - 3) = 0$.\n\n[TA Sora] Setting each to zero gives $x = 2$ and $x = 3$. The parabola hits the $x$-axis at $(2, 0)$ and $(3, 0)$!",
        "graph": {
            "xMin": 0, "xMax": 5, "yMin": -2, "yMax": 7,
            "title": "Example 1: f(x) = x^2 - 5x + 6 (x-ints at (2,0) and (3,0))",
            "points": [
                {"x": 2, "y": 0, "label": "(2, 0)", "color": "#f59e0b"},
                {"x": 3, "y": 0, "label": "(3, 0)", "color": "#f59e0b"},
                {"x": 0, "y": 6, "label": "y-int (0, 6)", "color": "#10b981"},
                {"x": 2.5, "y": -0.25, "label": "Vertex (2.5, -0.25)", "color": "#38bdf8"}
            ],
            "curves": [
                {"a": 1, "b": -5, "c": 6, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 2.5
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.3 Example 2: Intercepts & Vertex for f(x) = x^2 + 7x + 12",
        "subtitle": "Unit 3 • Lecture 38 • Section 3.3 Example 2 (Workbook p. 71)",
        "detail": "Lecture 38: Factoring & Zero Product Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2 (Workbook p. 71)\nFor $\\mathbf{f(x) = x^2 + 7x + 12}$:\n- **A. Find the $x$-intercept(s) by factoring:** __________________________\n- **B. Find the $y$-intercept:** __________________________\n- **C. Find the vertex:** __________________________",
        "solution": "$$\\begin{aligned}\n\\textbf{A. x-intercepts: } & x^2 + 7x + 12 = 0 \\\\\n& (x + 3)(x + 4) = 0 \\\\\n& x + 3 = 0 \\implies x = -3, \\quad x + 4 = 0 \\implies x = -4 \\\\\n& \\implies \\mathbf{(-3, 0) \\quad \\text{and} \\quad (-4, 0)} \\\\[0.8em]\n\\textbf{B. y-intercept: } & f(0) = 12 \\implies \\mathbf{(0, 12)} \\\\[0.8em]\n\\textbf{C. Vertex: } & x_v = -\\frac{7}{2(1)} = -3.5, \\\\\n& y_v = (-3.5)^2 + 7(-3.5) + 12 = 12.25 - 24.5 + 12 = \\mathbf{-0.25} \\\\\n& \\implies \\mathbf{(-3.5, -0.25)}\n\\end{aligned}$$",
        "pitfall": "**Midpoint check:** The vertex $x = -3.5$ is exactly halfway between $-3$ and $-4$! Symmetrical perfection.",
        "script": "[Prof. Park] In Example 2, $3$ and $4$ multiply to $12$ and add to $7$. So $(x + 3)(x + 4) = 0$.\n\n[TA Sora] The $x$-intercepts are $(-3, 0)$ and $(-4, 0)$. And the vertex sits at $(-3.5, -0.25)$!",
        "graph": {
            "xMin": -6, "xMax": 1, "yMin": -2, "yMax": 14,
            "title": "Example 2: f(x) = x^2 + 7x + 12",
            "points": [
                {"x": -4, "y": 0, "label": "(-4, 0)", "color": "#f59e0b"},
                {"x": -3, "y": 0, "label": "(-3, 0)", "color": "#f59e0b"},
                {"x": -3.5, "y": -0.25, "label": "Vertex (-3.5, -0.25)", "color": "#38bdf8"},
                {"x": 0, "y": 12, "label": "y-int (0, 12)", "color": "#10b981"}
            ],
            "curves": [
                {"a": 1, "b": 7, "c": 12, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": -3.5
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.3 Example 3: Factoring with GCF: 2x^2 - 8x = 0",
        "subtitle": "Unit 3 • Lecture 38 • Section 3.3 Example 3 (Workbook p. 72)",
        "detail": "Lecture 38: Factoring & Zero Product Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3 (Workbook p. 72)\nFind the $x$-intercepts for $\\mathbf{f(x) = 2x^2 - 8x}$:\n- Notice there is no constant term ($c = 0$).\n- Factor out the Greatest Common Factor (GCF).\n- Apply the Zero Product Property.",
        "solution": "$$\\begin{aligned}\n2x^2 - 8x & = 0 \\\\[0.5em]\n2x(x - 4) & = 0 \\quad (\\text{factor out GCF } 2x) \\\\[0.5em]\n2x = 0 & \\implies \\mathbf{x = 0} \\\\\nx - 4 = 0 & \\implies \\mathbf{x = 4} \\\\[0.8em]\n\\mathbf{x\\text{-intercepts: }} & \\mathbf{(0, 0) \\quad \\text{and} \\quad (4, 0)}\n\\end{aligned}$$",
        "pitfall": "**x = 0 IS A VALID SOLUTION:** When factoring out $2x$, setting $2x = 0$ gives $x = 0$. Never divide by $x$ and lose the root $x = 0$!",
        "script": "[Prof. Park] In Example 3, factor out the GCF $2x$. That leaves $2x(x - 4) = 0$.\n\n[TA Sora] Setting $2x = 0$ gives $x = 0$, and setting $x - 4 = 0$ gives $x = 4$. One intercept is right at the origin $(0, 0)$!",
        "graph": {
            "xMin": -2, "xMax": 6, "yMin": -10, "yMax": 4,
            "title": "Example 3: f(x) = 2x^2 - 8x (x-ints at (0, 0) and (4, 0))",
            "points": [
                {"x": 0, "y": 0, "label": "Origin (0, 0)", "color": "#10b981"},
                {"x": 4, "y": 0, "label": "(4, 0)", "color": "#f59e0b"},
                {"x": 2, "y": -8, "label": "Vertex (2, -8)", "color": "#38bdf8"}
            ],
            "curves": [
                {"a": 2, "b": -8, "c": 0, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 2
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.3 Example 4: Difference of Squares 4x^2 - 25 = 0",
        "subtitle": "Unit 3 • Lecture 38 • Section 3.3 Example 4 (Workbook p. 72)",
        "detail": "Lecture 38: Factoring & Zero Product Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4 (Workbook p. 72)\nFind the $x$-intercepts for $\\mathbf{f(x) = 4x^2 - 25}$:\n- Recognize the Difference of Two Squares pattern: $A^2 - B^2 = (A - B)(A + B)$.\n- Factor and solve for $x$.",
        "solution": "$$\\begin{aligned}\n4x^2 - 25 & = 0 \\\\[0.5em]\n(2x - 5)(2x + 5) & = 0 \\\\[0.5em]\n2x - 5 = 0 & \\implies 2x = 5 \\implies \\mathbf{x = \\frac{5}{2} = 2.5} \\\\\n2x + 5 = 0 & \\implies 2x = -5 \\implies \\mathbf{x = -\\frac{5}{2} = -2.5} \\\\[0.8em]\n\\mathbf{x\\text{-intercepts: }} & \\mathbf{\\left(\\frac{5}{2}, 0\\right) \\quad \\text{and} \\quad \\left(-\\frac{5}{2}, 0\\right)}\n\\end{aligned}$$",
        "pitfall": "**Two methods available:** Notice you could also use the Square Root Property here: $4x^2 = 25 \\implies x^2 = 25/4 \\implies x = \\pm 5/2$! Both methods give the exact same result!",
        "script": "[Prof. Park] In Example 4, $4x^2 - 25$ is a difference of squares: $(2x - 5)(2x + 5) = 0$.\n\n[TA Sora] That gives $x = \\pm \\frac{5}{2} = \\pm 2.5$. Symmetrical across the $y$-axis!",
        "graph": {
            "xMin": -5, "xMax": 5, "yMin": -28, "yMax": 6,
            "title": "Example 4: f(x) = 4x^2 - 25 (x-ints at ±2.5)",
            "points": [
                {"x": -2.5, "y": 0, "label": "(-2.5, 0)", "color": "#f59e0b"},
                {"x": 2.5, "y": 0, "label": "(2.5, 0)", "color": "#f59e0b"},
                {"x": 0, "y": -25, "label": "Vertex (0, -25)", "color": "#38bdf8"}
            ],
            "curves": [
                {"a": 4, "b": 0, "c": -25, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 0
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Sora's Pitfall Alert",
        "title": "The 'Must Equal Zero' Trap: x(x - 5) = 6",
        "subtitle": "Unit 3 • Lecture 38 • Section 3.3 Common Trap",
        "detail": "Lecture 38: Factoring & Zero Product Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Solve: $x(x - 5) = 6$\n- **Fatal Student Error:** Setting $x = 6$ or $x - 5 = 6$! Why is this completely false?\n- **Correct Procedure:** Multiply out, subtract 6 to set equation equal to ZERO, and then factor!",
        "solution": "$$\\begin{aligned}\nx(x - 5) & = 6 \\\\[0.5em]\nx^2 - 5x & = 6 \\quad (\\text{distribute}) \\\\[0.5em]\nx^2 - 5x - 6 & = 0 \\quad (\\text{MUST EQUAL ZERO!}) \\\\[0.5em]\n(x - 6)(x + 1) & = 0 \\quad (\\text{factor}) \\\\[0.5em]\n\\mathbf{x} & = \\mathbf{6 \\quad \\text{or} \\quad x = -1}\n\\end{aligned}$$",
        "pitfall": "**There is no 'Six Product Property':** If $A \\cdot B = 6$, $A$ could be $2$ and $B$ could be $3$. Neither has to be $6$! The product property ONLY works for ZERO!",
        "script": "[Prof. Park] Sora, warn them about this fatal trap.\n\n[TA Sora] There is NO Six Product Property! You must always distribute and bring everything to one side so it equals ZERO before factoring!"
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Summary & Step-by-Step",
        "title": "Sora's Protocol for Solving by Factoring",
        "subtitle": "Unit 3 • Lecture 38 • Section 3.3 Protocol",
        "detail": "Lecture 38: Factoring & Zero Product Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Factoring Protocol for Quadratic Equations\n1. **Set to zero:** Move all terms to one side: $ax^2 + bx + c = 0$.\n2. **Look for a GCF first:** Factor out any common monomial factor.\n3. **Count the terms:**\n   - **2 terms:** Check for difference of squares ($A^2 - B^2$).\n   - **3 terms ($a = 1$):** Find factors of $c$ that add to $b$.\n   - **3 terms ($a \\neq 1$):** Use the $ac$-method / grouping.\n4. **Apply Zero Product Property:** Set each factor equal to zero and solve.",
        "solution": "$$\\begin{array}{|c|c|c|} \n\\hline\n\\textbf{Structure} & \\textbf{Method} & \\textbf{Example} \\\\\n\\hline\n2x^2 - 8x = 0 & \\text{GCF} & 2x(x - 4) = 0 \\\\\n\\hline\nx^2 - 25 = 0 & \\text{Difference of Squares} & (x - 5)(x + 5) = 0 \\\\\n\\hline\nx^2 - 5x + 6 = 0 & \\text{Trinomial } a = 1 & (x - 2)(x - 3) = 0 \\\\\n\\hline\n\\end{array}$$",
        "pitfall": "**Check your factors:** Always FOIL your binomials back out to verify they match the original trinomial before solving!",
        "script": "[Prof. Park] Follow this 4-step protocol and factoring becomes effortless.\n\n[TA Sora] In Lecture 39, we tackle the tougher trinomials where the leading coefficient is not 1!"
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 3.3 Part 1 Mastery Summary",
        "subtitle": "Unit 3 • Lecture 38 • Section 3.3 Wrap-up",
        "detail": "Lecture 38: Factoring & Zero Product Property",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Lecture 38 Key Takeaways\n- $x$-intercepts correspond to roots of $ax^2 + bx + c = 0$.\n- Zero Product Property: $A \\cdot B = 0 \\implies A = 0$ or $B = 0$.\n- Always set to zero before factoring.\n- Write $x$-intercepts as $(x_1, 0)$ and $(x_2, 0)$.",
        "solution": "$$\\mathbf{\\text{Lecture 38 Complete! Next Up: Lecture 39 — Factoring when } a \\neq 1 \\text{ \\& Tangent Vertices!}}$$",
        "pitfall": "**Next Challenge:** What if the leading coefficient is $2x^2$ or $3x^2$? In Lecture 39, we master $ac$-factoring!",
        "script": "[Prof. Park] Great job! In Lecture 39, we expand our factoring toolkit to handle any factorable quadratic equation."
    }
]

# L39: Section 3.3 Part 2 (Workbook pp. 73 - 74) - 8 slides
data_36_40[39] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.3 Example 5: Factoring 2x^2 + 7x + 3 = 0",
        "subtitle": "Unit 3 • Lecture 39 • Section 3.3 Example 5 (Workbook p. 73)",
        "detail": "Lecture 39: Advanced Factoring & Root Types",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5: Leading Coefficient $a \\neq 1$ (Workbook p. 73)\nFind the $x$-intercepts for $\\mathbf{f(x) = 2x^2 + 7x + 3}$ by factoring:\n- Use the $ac$-method: $a \\cdot c = 2 \\cdot 3 = 6$.\n- Find factors of $6$ that add to $7$.\n- Factor by grouping and solve.",
        "solution": "$$\\begin{aligned}\n2x^2 + 7x + 3 & = 0 \\\\[0.5em]\nac & = 2 \\cdot 3 = 6 \\implies \\text{factors } 1 \\text{ and } 6 \\; (1 \\cdot 6 = 6, \\; 1 + 6 = 7) \\\\[0.5em]\n2x^2 + 6x + x + 3 & = 0 \\quad (\\text{split middle term}) \\\\[0.5em]\n2x(x + 3) + 1(x + 3) & = 0 \\\\[0.5em]\n(2x + 1)(x + 3) & = 0 \\\\[0.5em]\n2x + 1 = 0 & \\implies \\mathbf{x = -\\frac{1}{2} = -0.5} \\\\\nx + 3 = 0 & \\implies \\mathbf{x = -3} \\\\[0.8em]\n\\mathbf{x\\text{-intercepts: }} & \\mathbf{\\left(-\\frac{1}{2}, 0\\right) \\quad \\text{and} \\quad (-3, 0)}\n\\end{aligned}$$",
        "pitfall": "**Fraction root from 2x + 1:** $2x + 1 = 0 \\implies 2x = -1 \\implies x = -\\frac{1}{2}$. Don't forget to divide by 2!",
        "script": "[Prof. Park] In Example 5, $a = 2$. We split $7x$ into $6x + 1x$ and factor by grouping to get $(2x + 1)(x + 3) = 0$.\n\n[TA Sora] The intercepts are $\\left(-\\frac{1}{2}, 0\\right)$ and $(-3, 0)$! Look at them plotted on our coordinate grid.",
        "graph": {
            "xMin": -5, "xMax": 2, "yMin": -5, "yMax": 8,
            "title": "Example 5: f(x) = 2x^2 + 7x + 3 (x-ints at -3 and -0.5)",
            "points": [
                {"x": -3, "y": 0, "label": "(-3, 0)", "color": "#f59e0b"},
                {"x": -0.5, "y": 0, "label": "(-0.5, 0)", "color": "#f59e0b"},
                {"x": 0, "y": 3, "label": "y-int (0, 3)", "color": "#10b981"},
                {"x": -1.75, "y": -3.125, "label": "Vertex (-1.75, -3.125)", "color": "#38bdf8"}
            ],
            "curves": [
                {"a": 2, "b": 7, "c": 3, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": -1.75
        }
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.3 Example 6: Intercepts for g(x) = 3x^2 - 10x - 8",
        "subtitle": "Unit 3 • Lecture 39 • Section 3.3 Example 6 (Workbook p. 73)",
        "detail": "Lecture 39: Advanced Factoring & Root Types",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 6 (Workbook p. 73)\nFind the intercepts for $\\mathbf{g(x) = 3x^2 - 10x - 8}$:\n- $ac = 3 \\cdot (-8) = -24$.\n- Find factors of $-24$ that add to $-10$.\n- Factor and solve for $x$-intercepts and $y$-intercept.",
        "solution": "$$\\begin{aligned}\nac & = -24 \\implies \\text{factors: } -12 \\text{ and } +2 \\quad (-12 \\cdot 2 = -24, \\; -12 + 2 = -10) \\\\[0.5em]\n3x^2 - 12x + 2x - 8 & = 0 \\\\[0.5em]\n3x(x - 4) + 2(x - 4) & = 0 \\\\[0.5em]\n(3x + 2)(x - 4) & = 0 \\\\[0.5em]\n3x + 2 = 0 & \\implies \\mathbf{x = -\\frac{2}{3}} \\\\\nx - 4 = 0 & \\implies \\mathbf{x = 4} \\\\[0.8em]\n\\mathbf{x\\text{-intercepts: }} & \\mathbf{\\left(-\\frac{2}{3}, 0\\right) \\quad \\text{and} \\quad (4, 0)} \\\\[0.5em]\n\\mathbf{y\\text{-intercept: }} & \\mathbf{(0, -8)}\n\\end{aligned}$$",
        "pitfall": "**Check factors signs:** $-12$ and $+2$ gives $-10$. Using $-6$ and $-4$ gives $+24$, NOT $-24$! Always check the multiplication sign!",
        "script": "[Prof. Park] In Example 6, factors $-12$ and $+2$ give $(3x + 2)(x - 4) = 0$.\n\n[TA Sora] The $x$-intercepts are $(-\\frac{2}{3}, 0)$ and $(4, 0)$, and the $y$-intercept is $(0, -8)$!"
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.3 Example 7: Negative Leading Coefficient -x^2 + 4x + 5 = 0",
        "subtitle": "Unit 3 • Lecture 39 • Section 3.3 Example 7 (Workbook p. 74)",
        "detail": "Lecture 39: Advanced Factoring & Root Types",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 7 (Workbook p. 74)\nFind the $x$-intercepts for $\\mathbf{f(x) = -x^2 + 4x + 5}$:\n- Set $-x^2 + 4x + 5 = 0$.\n- Multiply or factor out $-1$ from all terms first.\n- Factor the resulting trinomial and solve.",
        "solution": "$$\\begin{aligned}\n-x^2 + 4x + 5 & = 0 \\\\[0.5em]\n-(x^2 - 4x - 5) & = 0 \\quad (\\text{factor out } -1) \\\\[0.5em]\n-(x - 5)(x + 1) & = 0 \\\\[0.5em]\nx - 5 = 0 & \\implies \\mathbf{x = 5} \\\\\nx + 1 = 0 & \\implies \\mathbf{x = -1} \\\\[0.8em]\n\\mathbf{x\\text{-intercepts: }} & \\mathbf{(5, 0) \\quad \\text{and} \\quad (-1, 0)}\n\\end{aligned}$$",
        "pitfall": "**Factoring with negative a:** Factoring is 10 times easier if you factor out $-1$ first: $x^2 - 4x - 5 = 0$ is simple to factor into $(x - 5)(x + 1)$!",
        "script": "[Prof. Park] Never struggle with a negative leading coefficient. Multiply both sides by $-1$ or factor out $-1$.\n\n[TA Sora] Then $x^2 - 4x - 5 = 0$ factors easily into $(x - 5)(x + 1) = 0$, giving $x = 5$ and $x = -1$!",
        "graph": {
            "xMin": -3, "xMax": 7, "yMin": -4, "yMax": 11,
            "title": "Example 7: f(x) = -x^2 + 4x + 5 (Opens Down, x-ints -1, 5)",
            "points": [
                {"x": -1, "y": 0, "label": "(-1, 0)", "color": "#f59e0b"},
                {"x": 5, "y": 0, "label": "(5, 0)", "color": "#f59e0b"},
                {"x": 2, "y": 9, "label": "Vertex (2, 9)", "color": "#ec4899"},
                {"x": 0, "y": 5, "label": "y-int (0, 5)", "color": "#10b981"}
            ],
            "curves": [
                {"a": -1, "b": 4, "c": 5, "color": "#ec4899", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 2
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Special Case & Tangent Vertex",
        "title": "Special Case: Exactly One x-Intercept (Tangent Vertex)",
        "subtitle": "Unit 3 • Lecture 39 • Section 3.3 Perfect Square Trinomials",
        "detail": "Lecture 39: Advanced Factoring & Root Types",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Perfect Square Trinomial: $f(x) = x^2 - 6x + 9$\n- Factor the equation $x^2 - 6x + 9 = 0$.\n- How many distinct roots are there?\n- What does this mean geometrically for the parabola on the Cartesian plane?",
        "solution": "$$\\begin{aligned}\nx^2 - 6x + 9 & = 0 \\\\[0.5em]\n(x - 3)(x - 3) & = 0 \\implies (x - 3)^2 = 0 \\\\[0.5em]\nx - 3 = 0 & \\implies \\mathbf{x = 3} \\; (\\text{Multiplicity 2}) \\\\[0.8em]\n\\mathbf{x\\text{-intercept: }} & \\mathbf{(3, 0) \\; [\\text{Exactly ONE } x\\text{-intercept!}]} \\\\[0.5em]\n\\text{Geometric Meaning: } & \\mathbf{\\text{The vertex sits directly ON the }} x\\mathbf{\\text{-axis (Tangent!)}}.\n\\end{aligned}$$",
        "pitfall": "**Single intercept = Vertex on axis:** When a quadratic has only ONE $x$-intercept, that intercept IS the vertex $(3, 0)$! The parabola bounces off the axis without crossing.",
        "script": "[Prof. Park] In this special case, the factors are identical: $(x - 3)^2 = 0$. There is only ONE $x$-intercept: $(3, 0)$.\n\n[TA Sora] That means the vertex touches the $x$-axis and bounces off! It is tangent to the axis.",
        "graph": {
            "xMin": 0, "xMax": 6, "yMin": -2, "yMax": 10,
            "title": "Tangent Vertex at (3, 0): f(x) = (x - 3)^2",
            "points": [
                {"x": 3, "y": 0, "label": "Tangent Vertex (3, 0)", "color": "#38bdf8"},
                {"x": 0, "y": 9, "label": "y-int (0, 9)", "color": "#10b981"}
            ],
            "curves": [
                {"a": 1, "b": -6, "c": 9, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 3
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "The Three Possibilities for x-Intercepts of a Parabola",
        "subtitle": "Unit 3 • Lecture 39 • Section 3.3 Geometric Classification",
        "detail": "Lecture 39: Advanced Factoring & Root Types",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### How Many x-Intercepts Can a Parabola Have?\nA parabola can intersect the horizontal axis in three distinct ways:\n1. **Two $x$-intercepts:** The parabola crosses through the axis twice (e.g. $x^2 - 5x + 6 = 0$).\n2. **One $x$-intercept:** The vertex touches the axis (tangent) once (e.g. $(x - 3)^2 = 0$).\n3. **Zero $x$-intercepts:** The parabola never touches the axis (e.g. $x^2 + 9 = 0$).",
        "solution": "$$\\begin{array}{|c|c|c|} \n\\hline\n\\textbf{Case} & \\textbf{Number of } x\\text{-ints} & \\textbf{Graphical Behavior} \\\\\n\\hline\n\\text{Case 1} & \\mathbf{2} & \\text{Crosses axis twice} \\\\\n\\hline\n\\text{Case 2} & \\mathbf{1} & \\text{Vertex touches axis (tangent)} \\\\\n\\hline\n\\text{Case 3} & \\mathbf{0} & \\text{Floats entirely above or below axis} \\\\\n\\hline\n\\end{array}$$",
        "pitfall": "**At most 2:** A quadratic equation can NEVER have 3 or more $x$-intercepts! The degree is 2, so the maximum number of real roots is 2.",
        "script": "[Prof. Park] Always visualize these three possibilities: 2 hits, 1 hit, or 0 hits.\n\n[TA Sora] This is the geometric heart of the Fundamental Theorem of Algebra!"
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Connection to Factored Form",
        "title": "Factored Form to Graph: f(x) = a(x - r_1)(x - r_2)",
        "subtitle": "Unit 3 • Lecture 39 • Section 3.3 Root Form",
        "detail": "Lecture 39: Advanced Factoring & Root Types",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Factored Form of a Quadratic Function\nIf the $x$-intercepts are $r_1$ and $r_2$, the function can be written:\n$$\\mathbf{f(x) = a(x - r_1)(x - r_2)}$$\n- The roots $r_1$ and $r_2$ appear directly in the factors.\n- The vertex $x$-coordinate is always the exact average of the roots:\n  $$\\mathbf{x_v = \\frac{r_1 + r_2}{2}}$$",
        "solution": "$$\\begin{aligned}\n\\text{If roots are } 2 \\text{ and } 6: & \\implies f(x) = a(x - 2)(x - 6) \\\\\n\\text{Vertex } x\\text{-coordinate: } & x_v = \\frac{2 + 6}{2} = \\mathbf{4}\n\\end{aligned}$$",
        "pitfall": "**Finding the vertex from roots:** When you factor and find roots $r_1$ and $r_2$, average them to get the vertex $x$-value! You don't even need $-b/(2a)$!",
        "script": "[Prof. Park] If you factor and find the roots, average them! That gives the vertex $x$-coordinate instantly.\n\n[TA Sora] That's a huge time-saver on multiple-choice exam questions!"
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Practice Problem",
        "title": "Check Your Understanding: Factoring 3x^2 - 12 = 0",
        "subtitle": "Unit 3 • Lecture 39 • Section 3.3 Practice",
        "detail": "Lecture 39: Advanced Factoring & Root Types",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Checkpoint Practice\nFind the $x$-intercepts for $\\mathbf{f(x) = 3x^2 - 12}$ using factoring:\n- Factor out the GCF first.\n- Factor the remaining difference of squares.\n- State both $x$-intercepts.",
        "solution": "$$\\begin{aligned}\n3x^2 - 12 & = 0 \\\\[0.5em]\n3(x^2 - 4) & = 0 \\quad (\\text{factor out GCF } 3) \\\\[0.5em]\n3(x - 2)(x + 2) & = 0 \\\\[0.5em]\nx - 2 = 0 & \\implies \\mathbf{x = 2} \\\\\nx + 2 = 0 & \\implies \\mathbf{x = -2} \\\\[0.8em]\n\\mathbf{x\\text{-intercepts: }} & \\mathbf{(2, 0) \\quad \\text{and} \\quad (-2, 0)}\n\\end{aligned}$$",
        "pitfall": "**The GCF 3 doesn't yield a root:** Setting $3 = 0$ is impossible! Only factors with variables produce solutions.",
        "script": "[Prof. Park] Factor out 3 first: $3(x^2 - 4) = 3(x - 2)(x + 2) = 0$.\n\n[TA Sora] The intercepts are $(2, 0)$ and $(-2, 0)$!"
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 3.3 Complete Mastery Summary",
        "subtitle": "Unit 3 • Lecture 39 • Section 3.3 Wrap-up",
        "detail": "Lecture 39: Advanced Factoring & Root Types",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Section 3.3 Master Checklist\n- Factored quadratic equations using GCF, grouping ($ac$-method), and difference of squares.\n- Handled negative leading coefficients by factoring out $-1$.\n- Discovered tangent vertices when roots repeat.\n- Connected roots $(r_1, 0)$ and $(r_2, 0)$ to the vertex midpoint $x_v = \\frac{r_1 + r_2}{2}$.",
        "solution": "$$\\mathbf{\\text{Section 3.3 Mastered! Next Up: Section 3.4 — Completing the Square!}}$$",
        "pitfall": "**The Big Question:** What if a trinomial DOES NOT FACTOR? (e.g. $x^2 + 6x - 7 = 0$ factors, but what about $x^2 + 6x - 2 = 0$?) In Section 3.4, Completing the Square solves ANY quadratic equation!",
        "script": "[Prof. Park] What if a trinomial won't factor? Do we give up?\n\n[TA Sora] Never! In Lecture 40, we learn Completing the Square, which can solve every quadratic equation in the universe!"
    }
]

# L40: Section 3.4 (Workbook pp. 75 - 79) - 8 slides
data_36_40[40] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Section 3.4: Completing the Square",
        "subtitle": "Unit 3 • Lecture 40 • Section 3.4 (Workbook p. 75)",
        "detail": "Lecture 40: Completing the Square",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Why Complete the Square? (Workbook p. 75)\nMany quadratic equations cannot be factored using whole numbers.\n**Completing the Square** is an algebraic technique that turns ANY quadratic expression into a **perfect square binomial**:\n$$x^2 + bx + \\mathbf{\\left(\\frac{b}{2}\\right)^2} = \\mathbf{\\left(x + \\frac{b}{2}\\right)^2}$$\n- Then we can solve it using the **Square Root Property** from Section 3.2!\n- The 'magic number' you must add to both sides is **$\\left(\\frac{b}{2}\\right)^2$**.",
        "solution": "$$\\begin{aligned}\n\\text{Magic Number: } & \\mathbf{\\left(\\frac{b}{2}\\right)^2} \\\\[0.5em]\n\\text{Take half of } b: & \\frac{b}{2} \\\\\n\\text{Square it: } & \\left(\\frac{b}{2}\\right)^2 \\\\\n\\text{Factor result: } & \\left(x + \\frac{b}{2}\\right)^2\n\\end{aligned}$$",
        "pitfall": "**Add to BOTH sides:** When solving an equation, if you add $(\\frac{b}{2})^2$ to the left side, you MUST add it to the right side to keep the balance!",
        "script": "[Prof. Park] Welcome to Section 3.4! Completing the Square is one of the greatest triumphs of classical algebra.\n\n[TA Sora] It forces a stubborn expression into a perfect square $(x + \\frac{b}{2})^2$ so we can use our trusty Square Root Property!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.4 Example 1: Finding the 'Magic Number'",
        "subtitle": "Unit 3 • Lecture 40 • Section 3.4 Example 1 (Workbook p. 75)",
        "detail": "Lecture 40: Completing the Square",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 (Workbook p. 75)\nFind the constant term that must be added to each binomial to make it a perfect square trinomial, then write the factored form:\n- **A.** $x^2 + 6x + \\underline{\\quad}$\n- **B.** $x^2 - 10x + \\underline{\\quad}$\n- **C.** $x^2 + 5x + \\underline{\\quad}$",
        "solution": "$$\\begin{aligned}\n\\textbf{A. } b = 6: & \\quad \\left(\\frac{6}{2}\\right)^2 = (3)^2 = \\mathbf{9} \\implies x^2 + 6x + 9 = \\mathbf{(x + 3)^2} \\\\[0.8em]\n\\textbf{B. } b = -10: & \\quad \\left(\\frac{-10}{2}\\right)^2 = (-5)^2 = \\mathbf{25} \\implies x^2 - 10x + 25 = \\mathbf{(x - 5)^2} \\\\[0.8em]\n\\textbf{C. } b = 5: & \\quad \\left(\\frac{5}{2}\\right)^2 = \\mathbf{\\frac{25}{4}} \\implies x^2 + 5x + \\frac{25}{4} = \\mathbf{\\left(x + \\frac{5}{2}\\right)^2}\n\\end{aligned}$$",
        "pitfall": "**The number inside the factored binomial:** The number inside the parentheses is ALWAYS half of $b$ ($\frac{b}{2}$)! Look at $x+3$ (half of 6) and $x-5$ (half of $-10$)!",
        "script": "[Prof. Park] In Example 1, take half of $b$ and square it. Half of 6 is 3, squared is 9. Factor is $(x + 3)^2$.\n\n[TA Sora] Half of $-10$ is $-5$, squared is 25. Factor is $(x - 5)^2$!"
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.4 Example 2: Solving x^2 + 6x = 7",
        "subtitle": "Unit 3 • Lecture 40 • Section 3.4 Example 2 (Workbook p. 75)",
        "detail": "Lecture 40: Completing the Square",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2 (Workbook p. 75)\nSolve the equation by completing the square:\n$$\\mathbf{x^2 + 6x = 7}$$\n- Add $(\\frac{6}{2})^2 = 9$ to both sides.\n- Factor the left side as a perfect square.\n- Apply the Square Root Property and solve.",
        "solution": "$$\\begin{aligned}\nx^2 + 6x & = 7 \\\\[0.5em]\nx^2 + 6x + \\mathbf{9} & = 7 + \\mathbf{9} \\quad (\\text{add } 9 \\text{ to BOTH sides!}) \\\\[0.5em]\n(x + 3)^2 & = 16 \\\\[0.5em]\nx + 3 & = \\pm \\sqrt{16} \\\\[0.5em]\nx + 3 & = \\pm 4 \\\\[0.5em]\nx & = -3 \\pm 4 \\\\[0.8em]\n\\text{Case 1: } & x = -3 + 4 = \\mathbf{1} \\\\\n\\text{Case 2: } & x = -3 - 4 = \\mathbf{-7} \\\\[0.8em]\n\\mathbf{\\text{Solutions: }} & \\mathbf{x = 1 \\quad \\text{and} \\quad x = -7}\n\\end{aligned}$$",
        "pitfall": "**Subtract 3 in front:** $x + 3 = \\pm 4 \\implies x = -3 \\pm 4$. Subtract 3 from both sides!",
        "script": "[Prof. Park] In Example 2, add 9 to both sides: $(x + 3)^2 = 16$. Square root gives $x + 3 = \\pm 4$.\n\n[TA Sora] Subtract 3: $-3 + 4 = 1$, and $-3 - 4 = -7$. Two clean integer roots!",
        "graph": {
            "xMin": -9, "xMax": 3, "yMin": -18, "yMax": 10,
            "title": "Example 2: f(x) = (x + 3)^2 - 16 = x^2 + 6x - 7",
            "points": [
                {"x": 1, "y": 0, "label": "(1, 0)", "color": "#f59e0b"},
                {"x": -7, "y": 0, "label": "(-7, 0)", "color": "#f59e0b"},
                {"x": -3, "y": -16, "label": "Vertex (-3, -16)", "color": "#38bdf8"}
            ],
            "curves": [
                {"a": 1, "b": 6, "c": -7, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": -3
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.4 Example 3: Solving x^2 - 8x - 5 = 0",
        "subtitle": "Unit 3 • Lecture 40 • Section 3.4 Example 3 (Workbook p. 76)",
        "detail": "Lecture 40: Completing the Square",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3 (Workbook p. 76)\nSolve the equation by completing the square:\n$$\\mathbf{x^2 - 8x - 5 = 0}$$\n- Move the constant $-5$ to the right side first.\n- Add $(\\frac{-8}{2})^2 = 16$ to both sides.\n- Solve for exact radical answers.",
        "solution": "$$\\begin{aligned}\nx^2 - 8x & = 5 \\quad (\\text{move constant to right side}) \\\\[0.5em]\nx^2 - 8x + \\mathbf{16} & = 5 + \\mathbf{16} \\quad \\left(\\text{add } \\left(\\frac{-8}{2}\\right)^2 = 16\\right) \\\\[0.5em]\n(x - 4)^2 & = 21 \\\\[0.5em]\nx - 4 & = \\pm \\sqrt{21} \\\\[0.5em]\n\\mathbf{x} & = \\mathbf{4 \\pm \\sqrt{21}} \\\\[0.8em]\n\\text{Two exact roots: } & \\mathbf{x = 4 + \\sqrt{21} \\approx 8.58} \\quad \\text{and} \\quad \\mathbf{x = 4 - \\sqrt{21} \\approx -0.58}\n\\end{aligned}$$",
        "pitfall": "**Notice this equation COULD NOT be factored:** There are no whole numbers multiplying to $-5$ and adding to $-8$. Completing the square solved it smoothly!",
        "script": "[Prof. Park] In Example 3, $x^2 - 8x - 5 = 0$ is unfactorable with integers. But completing the square handles it with ease.\n\n[TA Sora] We get $x = 4 \\pm \\sqrt{21}$. That is the exact mathematical truth!",
        "graph": {
            "xMin": -3, "xMax": 10, "yMin": -24, "yMax": 6,
            "title": "Example 3: f(x) = x^2 - 8x - 5 (x-ints at 4 ± sqrt(21))",
            "points": [
                {"x": 4, "y": -21, "label": "Vertex (4, -21)", "color": "#38bdf8"},
                {"x": 8.58, "y": 0, "label": "4 + sqrt(21)", "color": "#f59e0b"},
                {"x": -0.58, "y": 0, "label": "4 - sqrt(21)", "color": "#f59e0b"}
            ],
            "curves": [
                {"a": 1, "b": -8, "c": -5, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 4
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.4 Example 4: Leading Coefficient a != 1",
        "subtitle": "Unit 3 • Lecture 40 • Section 3.4 Example 4 (Workbook p. 77)",
        "detail": "Lecture 40: Completing the Square",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4: When $a \\neq 1$ (Workbook p. 77)\nSolve by completing the square:\n$$\\mathbf{2x^2 + 12x - 10 = 0}$$\n- **Golden Rule:** Completing the square requires the leading coefficient to be **$1$**!\n- Divide EVERY term on both sides by $2$ first.",
        "solution": "$$\\begin{aligned}\n\\frac{2x^2 + 12x - 10}{2} & = \\frac{0}{2} \\\\[0.5em]\nx^2 + 6x - 5 & = 0 \\\\[0.5em]\nx^2 + 6x & = 5 \\\\[0.5em]\nx^2 + 6x + \\mathbf{9} & = 5 + \\mathbf{9} \\quad \\left(\\text{add } \\left(\\frac{6}{2}\\right)^2 = 9\\right) \\\\[0.5em]\n(x + 3)^2 & = 14 \\\\[0.5em]\nx + 3 & = \\pm \\sqrt{14} \\\\[0.5em]\n\\mathbf{x} & = \\mathbf{-3 \\pm \\sqrt{14}}\n\\end{aligned}$$",
        "pitfall": "**Divide by a FIRST:** You CANNOT find the magic number while the coefficient of $x^2$ is 2! Always divide everything by $a$ first!",
        "script": "[Prof. Park] In Example 4, $a = 2$. Divide every single term by 2 before doing anything else!\n\n[TA Sora] $x^2 + 6x - 5 = 0$. Now complete the square by adding 9: $(x + 3)^2 = 14 \\implies x = -3 \\pm \\sqrt{14}$!"
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Connection to Vertex Form",
        "title": "Converting General Form to Vertex Form via CTS",
        "subtitle": "Unit 3 • Lecture 40 • Section 3.4 Application",
        "detail": "Lecture 40: Completing the Square",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Transforming $f(x) = x^2 - 6x + 5$ into Vertex Form\nWatch how completing the square transforms General Form into Vertex Form:\n- Group the $x$-terms: $(x^2 - 6x) + 5$.\n- Complete the square inside: add $9$ and subtract $9$ to keep balance!\n- State the vertex $(h, k)$.",
        "solution": "$$\\begin{aligned}\nf(x) & = (x^2 - 6x) + 5 \\\\[0.5em]\n& = (x^2 - 6x + \\mathbf{9}) + 5 - \\mathbf{9} \\quad (\\text{add and subtract } 9) \\\\[0.5em]\n& = \\mathbf{(x - 3)^2 - 4} \\\\[0.8em]\n\\mathbf{\\text{Vertex: }} & \\mathbf{(3, -4)} \\quad \\implies \\quad \\text{Vertex Form matches Section 3.0 Example 5!}\n\\end{aligned}$$",
        "pitfall": "**Add and subtract on the same side:** If you work on one side of an expression, adding $9$ and subtracting $9$ adds zero overall, preserving the equation!",
        "script": "[Prof. Park] This is how mathematicians convert general form into vertex form!\n\n[TA Sora] $(x - 3)^2 - 4$ gives the vertex $(3, -4)$ immediately without memorizing the vertex formula!"
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Step-by-Step Summary",
        "title": "Sora's Complete CTS Protocol",
        "subtitle": "Unit 3 • Lecture 40 • Section 3.4 Protocol",
        "detail": "Lecture 40: Completing the Square",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Master 5-Step CTS Protocol\n1. **Ensure $a = 1$:** If $a \\neq 1$, divide all terms on both sides by $a$.\n2. **Isolate variable terms:** Move constant $c$ to the right side: $x^2 + bx = -c$.\n3. **Compute magic number:** Calculate $(\\frac{b}{2})^2$.\n4. **Add to BOTH sides:** $x^2 + bx + (\\frac{b}{2})^2 = -c + (\\frac{b}{2})^2$.\n5. **Factor and solve:** $(x + \\frac{b}{2})^2 = k \\implies x = -\\frac{b}{2} \\pm \\sqrt{k}$.",
        "solution": "$$\\mathbf{\\text{Result: Solves EVERY quadratic equation, factorable or unfactorable!}}$$",
        "pitfall": "**Fraction b values:** If $b$ is odd (like $b = 5$), $(\\frac{5}{2})^2 = \\frac{25}{4}$. Don't fear fractions; just find common denominators!",
        "script": "[Prof. Park] This 5-step method is foolproof. It works for every single quadratic equation in existence.\n\n[TA Sora] And even more amazingly, if you apply this exact protocol to the general equation $ax^2 + bx + c = 0$, you derive the Quadratic Formula!"
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 3.4 Mastery Summary & The Gateway to the Formula",
        "subtitle": "Unit 3 • Lecture 40 • Section 3.4 Wrap-up",
        "detail": "Lecture 40: Completing the Square",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### The Gateway to Section 3.5\n- Completing the square proved that ANY quadratic equation can be solved.\n- In Section 3.5, we complete the square on the abstract symbols $ax^2 + bx + c = 0$ once and for all.\n- That yields the crown jewel of algebra: **The Quadratic Formula**!",
        "solution": "$$\\mathbf{\\text{Section 3.4 Mastered! Next Up: Section 3.5 — The Quadratic Formula!}}$$",
        "pitfall": "**Celebrate your progress:** You have conquered Square Root Property, Factoring, and Completing the Square!",
        "script": "[Prof. Park] You have conquered three major methods. Now get ready for the grand master key.\n\n[TA Sora] In Lecture 41, we unlock the legendary Quadratic Formula!"
    }
]

print("Unit 3 Lectures 36 to 40 generated successfully!")
