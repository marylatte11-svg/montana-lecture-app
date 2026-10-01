# Unit 3 Lectures 31 - 35 Data
# Faithful to M090 Workbook pp. 60 - 66
# Introduces Parabolas, Vertex, Axis of Symmetry & Quadratic Evaluation

data_31_35 = {}

# L31: Section 3.0 Part 1 (Workbook p. 60) - 8 slides
data_31_35[31] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Course Orientation & Welcome to Unit 3",
        "title": "Welcome to Unit 3: Quadratic Functions & The Parabola World",
        "subtitle": "Unit 3 • Lecture 31 • Section 3.0 (Workbook p. 60)",
        "detail": "Lecture 31: Intro to Quadratic Functions",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Welcome to Unit 3 of M090! (Workbook p. 60)\nIn Unit 1, we learned the grammar of algebra (expressions, equations).\nIn Unit 2, we mastered straight lines ($y = mx + b$).\n\nNow in **Unit 3**, we enter the curved world of **Quadratic Functions & Parabolas**:\n- **General Form:** $\\mathbf{f(x) = ax^2 + bx + c}$ where $a \\neq 0$.\n- **Standard / Vertex Form:** $\\mathbf{f(x) = a(x - h)^2 + k}$.\n- **Graph:** A smooth, symmetric U-shaped curve called a **Parabola**!",
        "solution": "$$\\begin{aligned}\n\\text{General Form: } & f(x) = ax^2 + bx + c \\quad (a \\neq 0) \\\\\n\\text{Degree: } & 2 \\quad (\\text{highest exponent is } 2) \\\\\n\\text{Shape: } & \\text{Parabola (opens upward if } a > 0, \\text{ downward if } a < 0)\n\\end{aligned}$$",
        "pitfall": "**Quadratic requirement:** The coefficient $a$ CANNOT be zero! If $a = 0$, the $x^2$ term disappears and it becomes a linear function $bx + c$!",
        "script": "[Prof. Park] Welcome to Unit 3 of M090 Introductory Algebra! In this unit, lines begin to curve. We enter the world of quadratics.\n\n[TA Sora] Parabolas describe so many things in Montana: the flight of a ski jumper at Bridger Bowl, the arch of water in a fountain, and the trajectory of a basketball!\n\n[Prof. Park] Grab your workbook and open to Section 3.0 on page 60. Let's analyze the anatomy of quadratic equations!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Anatomy of a Quadratic Function: Terms & Coefficients",
        "subtitle": "Unit 3 • Lecture 31 • Section 3.0 (Workbook p. 60)",
        "detail": "Lecture 31: Intro to Quadratic Functions",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Anatomy of General Form (Workbook p. 60)\n$$\\mathbf{f(x) = ax^2 + bx + c}$$\n- **Quadratic Term:** The term with $x^2$ $\\rightarrow$ **$ax^2$** (Coefficient is **$a$**).\n- **Linear Term:** The term with $x$ $\\rightarrow$ **$bx$** (Coefficient is **$b$**).\n- **Constant Term:** The numerical term without variables $\\rightarrow$ **$c$**.",
        "solution": "$$\\begin{array}{|c|c|c|}\n\\hline\n\\textbf{Term Type} & \\textbf{Algebraic Expression} & \\textbf{Coefficient} \\\\\n\\hline\n\\text{Quadratic Term} & ax^2 & a \\\\\n\\hline\n\\text{Linear Term} & bx & b \\\\\n\\hline\n\\text{Constant Term} & c & c \\\\\n\\hline\n\\end{array}$$",
        "pitfall": "**Coefficient vs Term:** The term includes the variable ($ax^2$). The coefficient is strictly the number in front ($a$)!",
        "script": "[Prof. Park] In Section 3.0, the authors ask us to identify the quadratic term, linear term, and constant term.\n\n[TA Sora] Make sure to keep the sign with the coefficient: if it says $-5x$, the linear term is $-5x$ and its coefficient is $-5$!"
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 1: Terms in f(x) = -x^2 + 3x + 8",
        "subtitle": "Unit 3 • Lecture 31 • Section 3.0 Example 1 (Workbook p. 60)",
        "detail": "Lecture 31: Intro to Quadratic Functions",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 (Workbook p. 60)\nFor the function $\\mathbf{f(x) = -x^2 + 3x + 8}$, identify:\n- **Quadratic term:** ____________ \\quad **Coefficient:** ____________\n- **Linear term:** ____________ \\quad **Coefficient:** ____________\n- **Constant term:** ____________",
        "solution": "$$\\begin{aligned}\n\\textbf{Quadratic term: } & \\mathbf{-x^2} \\quad \\implies \\quad \\textbf{Coefficient: } \\mathbf{-1} \\\\[0.5em]\n\\textbf{Linear term: } & \\mathbf{3x} \\quad \\implies \\quad \\textbf{Coefficient: } \\mathbf{3} \\\\[0.5em]\n\\textbf{Constant term: } & \\mathbf{8}\n\\end{aligned}$$",
        "pitfall": "**The invisible 1:** When you see $-x^2$, the coefficient is $-1$, NOT $0$ or just a minus sign!",
        "script": "[Prof. Park] In Example 1, $f(x) = -x^2 + 3x + 8$. The quadratic term is $-x^2$ with coefficient $-1$.\n\n[TA Sora] Linear term is $3x$ with coefficient 3, and the constant is 8. Notice $a = -1 < 0$, which means this parabola opens downward!"
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 2: Terms in f(x) = 2x^2 - 7",
        "subtitle": "Unit 3 • Lecture 31 • Section 3.0 Example 2 (Workbook p. 60)",
        "detail": "Lecture 31: Intro to Quadratic Functions",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2 (Workbook p. 60)\nFor the function $\\mathbf{f(x) = 2x^2 - 7}$, identify:\n- **Quadratic term:** ____________ \\quad **Coefficient:** ____________\n- **Linear term:** ____________ \\quad **Coefficient:** ____________\n- **Constant term:** ____________",
        "solution": "$$\\begin{aligned}\n\\textbf{Quadratic term: } & \\mathbf{2x^2} \\quad \\implies \\quad \\textbf{Coefficient: } \\mathbf{2} \\\\[0.5em]\n\\textbf{Linear term: } & \\mathbf{0x \\; (\\text{None})} \\quad \\implies \\quad \\textbf{Coefficient: } \\mathbf{0} \\\\[0.5em]\n\\textbf{Constant term: } & \\mathbf{-7}\n\\end{aligned}$$",
        "pitfall": "**Missing terms have coefficient 0:** Because there is no $x$ term, the linear coefficient is $b = 0$. Do not write 'none'—mathematically, $b = 0$!",
        "script": "[Prof. Park] In Example 2, there is no middle term with $x$. What is its coefficient, Sora?\n\n[TA Sora] It is 0! We can think of it as $2x^2 + 0x - 7$. The quadratic coefficient is 2, and the constant is $-7$."
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 3: Descending Order First",
        "subtitle": "Unit 3 • Lecture 31 • Section 3.0 Example 3 (Workbook p. 60)",
        "detail": "Lecture 31: Intro to Quadratic Functions",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3 (Workbook p. 60)\nConsider $\\mathbf{f(x) = -2 - 3x + \\frac{x^2}{3}}$.\n- **Put in descending order first:** __________________________\n- **Quadratic term & coefficient:** __________________________\n- **Linear term & coefficient:** __________________________\n- **Constant term:** __________________________",
        "solution": "$$\\begin{aligned}\n\\textbf{Descending Order: } & \\mathbf{f(x) = \\frac{1}{3}x^2 - 3x - 2} \\\\[0.8em]\n\\textbf{Quadratic term: } & \\mathbf{\\frac{x^2}{3} = \\frac{1}{3}x^2} \\quad \\implies \\quad \\textbf{Coefficient: } \\mathbf{\\frac{1}{3}} \\\\[0.5em]\n\\textbf{Linear term: } & \\mathbf{-3x} \\quad \\implies \\quad \\textbf{Coefficient: } \\mathbf{-3} \\\\[0.5em]\n\\textbf{Constant term: } & \\mathbf{-2}\n\\end{aligned}$$",
        "pitfall": "**Rearrange before identifying:** Don't assume the first term is quadratic! Always rearrange from highest exponent to lowest: $x^2$, then $x$, then constant!",
        "script": "[Prof. Park] In Example 3, the terms are scrambled. Write the $x^2$ term first, then the $x$ term, then the constant.\n\n[TA Sora] $\\frac{x^2}{3} - 3x - 2$. The quadratic coefficient is $\\frac{1}{3}$, the linear coefficient is $-3$, and the constant is $-2$!"
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 4: Linear vs Quadratic",
        "subtitle": "Unit 3 • Lecture 31 • Section 3.0 Example 4 (Workbook p. 60)",
        "detail": "Lecture 31: Intro to Quadratic Functions",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4 (Workbook p. 60)\nWhat type of function is $\\mathbf{f(x) = 4x + 7}$?\n- **Quadratic term & coefficient:** __________________________\n- **Linear term & coefficient:** __________________________\n- **Constant term:** __________________________\n- Is this function quadratic?",
        "solution": "$$\\begin{aligned}\n\\textbf{Quadratic term: } & \\mathbf{0x^2 \\; (\\text{None})} \\quad \\implies \\quad \\textbf{Coefficient: } \\mathbf{0} \\\\[0.5em]\n\\textbf{Linear term: } & \\mathbf{4x} \\quad \\implies \\quad \\textbf{Coefficient: } \\mathbf{4} \\\\[0.5em]\n\\textbf{Constant term: } & \\mathbf{7} \\\\[0.8em]\n\\mathbf{\\text{Function Type: }} & \\mathbf{\\text{LINEAR FUNCTION, NOT Quadratic!}}\n\\end{aligned}$$",
        "pitfall": "**A quadratic function MUST have an x^2 term:** Since $a = 0$, the degree is 1, so this is a straight line, not a parabola!",
        "script": "[Prof. Park] Example 4 tests our definition. $f(x) = 4x + 7$ has no $x^2$ term at all.\n\n[TA Sora] It is a linear function with slope 4 and $y$-intercept 7. Quadratics strictly require degree 2!"
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept & Parabola Orientation",
        "title": "Parabola Direction: Opening Upward vs Opening Downward",
        "subtitle": "Unit 3 • Lecture 31 • Section 3.0 Direction Rules",
        "detail": "Lecture 31: Intro to Quadratic Functions",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Parabola Orientation Rules\nThe sign of the leading coefficient $a$ determines which way the parabola opens:\n- **$a > 0$ (Positive):** Parabola opens **UPWARD** $\\cup$.\n  - The vertex is the **lowest point (Minimum)**.\n- **$a < 0$ (Negative):** Parabola opens **DOWNWARD** $\\cap$.\n  - The vertex is the **highest point (Maximum)**.",
        "solution": "$$\\begin{array}{|c|c|c|c|}\n\\hline\n\\textbf{Sign of } a & \\textbf{Shape} & \\textbf{Orientation} & \\textbf{Vertex Type} \\\\\n\\hline\na > 0 & \\cup & \\text{Opens UP} & \\textbf{Minimum (Lowest Point)} \\\\\n\\hline\na < 0 & \\cap & \\text{Opens DOWN} & \\textbf{Maximum (Highest Point)} \\\\\n\\hline\n\\end{array}$$",
        "pitfall": "**Happy face vs Sad face:** Positive $a > 0$ makes a smile (minimum valley). Negative $a < 0$ makes a frown (maximum peak)!",
        "script": "[Prof. Park] Look at the two parabolas on your screen. The blue curve opens upward because $a > 0$, while the pink curve opens downward because $a < 0$.\n\n[TA Sora] This is so visual: positive means a minimum valley, negative means a maximum peak!",
        "graph": {
            "xMin": -5, "xMax": 5, "yMin": -5, "yMax": 6,
            "title": "Parabolas: Upward (Blue, min) vs Downward (Pink, max)",
            "points": [
                {"x": 0, "y": -3, "label": "Min Vertex (0, -3)", "color": "#38bdf8"},
                {"x": 0, "y": 4, "label": "Max Vertex (0, 4)", "color": "#ec4899"}
            ],
            "curves": [
                {"a": 1, "b": 0, "c": -3, "color": "#38bdf8", "strokeWidth": 2.5, "label": "a > 0 (Up)"},
                {"a": -1, "b": 0, "c": 4, "color": "#ec4899", "strokeWidth": 2.5, "label": "a < 0 (Down)"}
            ]
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 3.0 Part 1 Mastery Summary",
        "subtitle": "Unit 3 • Lecture 31 • Section 3.0 Wrap-up",
        "detail": "Lecture 31: Intro to Quadratic Functions",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Lecture 31 Key Takeaways\n- General form: $f(x) = ax^2 + bx + c$ with $a \\neq 0$.\n- Vertex form: $f(x) = a(x - h)^2 + k$.\n- Always rearrange into descending order before identifying coefficients.\n- Leading coefficient $a$ controls whether the parabola opens up or down.",
        "solution": "$$\\mathbf{\\text{Lecture 31 Complete! Next Up: Lecture 32 — Reading Parabola Graphs (Vertex, Axis, Intercepts)!}}$$",
        "pitfall": "**Never skip descending order:** Always write $ax^2 + bx + c$ so you never mix up $a, b,$ and $c$!",
        "script": "[Prof. Park] Excellent start to Unit 3! In Lecture 32, we learn how to read every key feature of a parabola directly from its graph."
    }
]

# L32: Section 3.0 Part 2 (Workbook p. 61) - 9 slides
data_31_35[32] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "The Anatomy of a Parabola Graph",
        "subtitle": "Unit 3 • Lecture 32 • Section 3.0 (Workbook p. 61)",
        "detail": "Lecture 32: Reading Parabola Graphs",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Key Features of Every Parabola (Workbook p. 61)\nWhen analyzing any quadratic graph, identify:\n1. **$y$-intercept:** Where the graph crosses the vertical axis $(0, c)$.\n2. **$x$-intercepts:** Where the graph crosses the horizontal axis (at most 2).\n3. **Vertex $(h, k)$:** The turning point (maximum or minimum).\n4. **Axis of Symmetry:** The vertical line cutting through the vertex: $\\mathbf{x = h}$.\n5. **Domain:** Always $(-\\infty, \\infty)$.\n6. **Range:** Bounded by the vertex: $[k, \\infty)$ if opens up, or $(-\\infty, k]$ if opens down.",
        "solution": "$$\\begin{aligned}\n\\text{Vertex: } & (h, k) \\\\\n\\text{Axis of Symmetry: } & x = h \\quad (\\text{vertical line}) \\\\\n\\text{Domain: } & (-\\infty, \\infty) \\\\\n\\text{Range: } & [k, \\infty) \\text{ if } a > 0, \\quad (-\\infty, k] \\text{ if } a < 0\n\\end{aligned}$$",
        "pitfall": "**Axis of symmetry is an EQUATION:** The axis of symmetry is a line, so you MUST write $\\mathbf{x = h}$. Writing just the number $h$ will lose credit on exams!",
        "script": "[Prof. Park] In Lecture 32, we explore Example 5 and Example 6 from page 61 of the workbook.\n\n[TA Sora] These examples teach us how to extract the vertex, axis of symmetry, intercepts, and range directly from a parabola graph!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 5 (Part 1): Intercepts for f(x) = x^2 - 6x + 5",
        "subtitle": "Unit 3 • Lecture 32 • Section 3.0 Example 5A, B (Workbook p. 61)",
        "detail": "Lecture 32: Reading Parabola Graphs",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5 (Workbook p. 61)\nUsing the graph of the function $\\mathbf{f(x) = x^2 - 6x + 5}$:\n- **A. $y$-intercept:** ____________\n- **B. $x$-intercepts:** ____________",
        "solution": "$$\\begin{aligned}\n\\mathbf{y\\text{-intercept: }} & \\text{Set } x = 0: f(0) = 0^2 - 6(0) + 5 = 5 \\implies \\mathbf{(0, 5)} \\\\[0.8em]\n\\mathbf{x\\text{-intercepts: }} & \\text{Set } f(x) = 0: x^2 - 6x + 5 = 0 \\\\\n& (x - 1)(x - 5) = 0 \\\\\n& \\mathbf{x = 1 \\quad \\text{and} \\quad x = 5} \\implies \\mathbf{(1, 0) \\quad \\text{and} \\quad (5, 0)}\n\\end{aligned}$$",
        "pitfall": "**List both x-intercepts:** Notice the parabola crosses the $x$-axis twice! List both points: $(1, 0)$ and $(5, 0)$.",
        "script": "[Prof. Park] Looking at the graph of $f(x) = x^2 - 6x + 5$, the curve hits the vertical axis at $(0, 5)$.\n\n[TA Sora] And it crosses the horizontal axis at two spots: $(1, 0)$ and $(5, 0)$!"
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 5 (Part 2): Vertex & Axis of Symmetry",
        "subtitle": "Unit 3 • Lecture 32 • Section 3.0 Example 5C, D (Workbook p. 61)",
        "detail": "Lecture 32: Reading Parabola Graphs",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5 Continued (Workbook p. 61)\nFrom the graph of $\\mathbf{f(x) = x^2 - 6x + 5}$:\n- **C. Vertex:** ____________\n- **D. Axis of Symmetry:** ____________",
        "solution": "$$\\begin{aligned}\n\\mathbf{\\text{Vertex: }} & \\text{Lowest point at } x = 3, y = -4 \\implies \\mathbf{(3, -4)} \\\\[0.8em]\n\\mathbf{\\text{Axis of Symmetry: }} & \\text{Vertical line through vertex: } \\mathbf{x = 3}\n\\end{aligned}$$",
        "pitfall": "**Notice the symmetry:** $x = 3$ is exactly halfway between the two $x$-intercepts $1$ and $5$: $\\frac{1 + 5}{2} = 3$!",
        "script": "[Prof. Park] The vertex is the turning point at $(3, -4)$.\n\n[TA Sora] The gold dashed line cuts right through the vertex at $x = 3$. That is our Axis of Symmetry!",
        "graph": {
            "xMin": -1, "xMax": 7, "yMin": -5, "yMax": 7,
            "title": "Example 5: f(x) = x^2 - 6x + 5 (Vertex at (3, -4))",
            "points": [
                {"x": 0, "y": 5, "label": "y-int (0, 5)", "color": "#10b981"},
                {"x": 1, "y": 0, "label": "x-int (1, 0)", "color": "#f59e0b"},
                {"x": 5, "y": 0, "label": "x-int (5, 0)", "color": "#f59e0b"},
                {"x": 3, "y": -4, "label": "Vertex (3, -4)", "color": "#38bdf8"}
            ],
            "curves": [
                {"a": 1, "b": -6, "c": 5, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 3
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 5 (Part 3): Min/Max & Domain/Range",
        "subtitle": "Unit 3 • Lecture 32 • Section 3.0 Example 5E, F, G (Workbook p. 61)",
        "detail": "Lecture 32: Reading Parabola Graphs",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5 Min/Max & Intervals (Workbook p. 61)\n- **E. What is the minimum value of $f(x)$?** ___________\n- **F. At what $x$-value does the minimum occur?** ___________\n- **G. Domain:** (in interval notation) \\quad **Range:** (in interval notation)",
        "solution": "$$\\begin{aligned}\n\\textbf{E. Minimum Value: } & \\mathbf{-4} \\quad (\\text{the } y\\text{-coordinate of the vertex}) \\\\[0.5em]\n\\textbf{F. Occurs at: } & \\mathbf{x = 3} \\quad (\\text{the } x\\text{-coordinate of the vertex}) \\\\[0.8em]\n\\mathbf{\\text{Domain: }} & \\mathbf{(-\\infty, \\infty)} \\\\\n\\mathbf{\\text{Range: }} & \\mathbf{[-4, \\infty)} \\quad (\\text{starts at } -4 \\text{ and goes up to } +\\infty)\n\\end{aligned}$$",
        "pitfall": "**Value vs Location:** The MINIMUM VALUE is the $y$-value ($-4$). The LOCATION where it occurs is the $x$-value ($3$)!",
        "script": "[Prof. Park] In math, when we ask 'What is the maximum or minimum value?', we always mean the $y$-value: $-4$.\n\n[TA Sora] And 'at what $x$-value' means the input: $x = 3$. The range starts with a bracket at $-4$: $[-4, \\infty)$!"
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 6 (Part 1): Vertex Form f(x) = -2(x + 1)^2 + 8",
        "subtitle": "Unit 3 • Lecture 32 • Section 3.0 Example 6A, B (Workbook p. 61)",
        "detail": "Lecture 32: Reading Parabola Graphs",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 6 (Workbook p. 61)\nUsing the graph of the function $\\mathbf{f(x) = -2(x + 1)^2 + 8}$:\n- **A. $y$-intercept:** ____________\n- **B. $x$-intercepts:** ____________\nNotice $a = -2 < 0$, so this parabola opens **downward**!",
        "solution": "$$\\begin{aligned}\n\\mathbf{y\\text{-intercept: }} & f(0) = -2(0 + 1)^2 + 8 = -2(1) + 8 = \\mathbf{6} \\implies \\mathbf{(0, 6)} \\\\[0.8em]\n\\mathbf{x\\text{-intercepts: }} & 0 = -2(x + 1)^2 + 8 \\\\\n& 2(x + 1)^2 = 8 \\implies (x + 1)^2 = 4 \\\\\n& x + 1 = \\pm 2 \\implies \\mathbf{x = 1 \\quad \\text{and} \\quad x = -3} \\\\\n& \\implies \\mathbf{(1, 0) \\quad \\text{and} \\quad (-3, 0)}\n\\end{aligned}$$",
        "pitfall": "**Don't assume y-intercept is 8:** In vertex form, the constant $8$ is $k$, NOT the $y$-intercept! Plug in $x = 0$ to get $y = 6$!",
        "script": "[Prof. Park] In Example 6, the parabola opens downward. Setting $x=0$ gives $y = -2(1) + 8 = 6$.\n\n[TA Sora] And setting $f(x)=0$ gives $x = 1$ and $x = -3$. Both intercepts are marked on the graph!"
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 6 (Part 2): Vertex & Axis of Symmetry",
        "subtitle": "Unit 3 • Lecture 32 • Section 3.0 Example 6C, D (Workbook p. 61)",
        "detail": "Lecture 32: Reading Parabola Graphs",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 6 Vertex from Formula (Workbook p. 61)\nCompare $\\mathbf{f(x) = -2(x + 1)^2 + 8}$ to Vertex Form $\\mathbf{f(x) = a(x - h)^2 + k}$:\n- **C. Vertex:** ____________ *(Do you see the connection to the function?)*\n- **D. Axis of Symmetry:** ____________",
        "solution": "$$\\begin{aligned}\n\\text{Formula: } & f(x) = a(x - h)^2 + k \\\\[0.5em]\n\\text{Identify: } & x + 1 = x - (-1) \\implies \\mathbf{h = -1} \\\\\n& \\mathbf{k = 8} \\\\[0.8em]\n\\mathbf{\\text{Vertex: }} & \\mathbf{(-1, 8)} \\\\[0.5em]\n\\mathbf{\\text{Axis of Symmetry: }} & \\mathbf{x = -1}\n\\end{aligned}$$",
        "pitfall": "**The sign inside the parentheses flips!** In $(x + 1)^2$, $h = -1$, NOT $+1$! It's always the opposite sign of what's inside!",
        "script": "[Prof. Park] Look at the vertex: $(-1, 8)$. Notice the function had $(x + 1)^2 + 8$.\n\n[TA Sora] The $x$-coordinate flips sign to $-1$, while the $y$-coordinate keeps its sign as $+8$! That is the secret of vertex form.",
        "graph": {
            "xMin": -5, "xMax": 3, "yMin": -2, "yMax": 10,
            "title": "Example 6: f(x) = -2(x + 1)^2 + 8 (Vertex (-1, 8))",
            "points": [
                {"x": -1, "y": 8, "label": "Max Vertex (-1, 8)", "color": "#ec4899"},
                {"x": 0, "y": 6, "label": "y-int (0, 6)", "color": "#10b981"},
                {"x": -3, "y": 0, "label": "x-int (-3, 0)", "color": "#f59e0b"},
                {"x": 1, "y": 0, "label": "x-int (1, 0)", "color": "#f59e0b"}
            ],
            "curves": [
                {"a": -2, "b": -4, "c": 6, "color": "#ec4899", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": -1
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 6 (Part 3): Max Value & Range",
        "subtitle": "Unit 3 • Lecture 32 • Section 3.0 Example 6E, F, G (Workbook p. 61)",
        "detail": "Lecture 32: Reading Parabola Graphs",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 6 Max & Range (Workbook p. 61)\n- **E. What is the maximum value of $f(x)$?** ___________\n- **F. At what $x$-value does the maximum occur?** ___________\n- **G. Domain:** (in interval notation) \\quad **Range:** (in interval notation)",
        "solution": "$$\\begin{aligned}\n\\textbf{E. Maximum Value: } & \\mathbf{8} \\quad (\\text{peak height of the parabola}) \\\\[0.5em]\n\\textbf{F. Occurs at: } & \\mathbf{x = -1} \\\\[0.8em]\n\\mathbf{\\text{Domain: }} & \\mathbf{(-\\infty, \\infty)} \\\\\n\\mathbf{\\text{Range: }} & \\mathbf{(-\\infty, 8]} \\quad (\\text{goes down to } -\\infty, \\text{ capped at peak } 8)\n\\end{aligned}$$",
        "pitfall": "**Range direction for downward parabolas:** The curve extends downward, so range is $(-\\infty, 8]$, NOT $[8, -\\infty)$ or $[8, \\infty)$!",
        "script": "[Prof. Park] Because $a = -2$, the parabola curves downward. The peak is at height 8.\n\n[TA Sora] So the maximum value is 8 occurring at $x = -1$. The range is $(-\\infty, 8]$!"
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 6 (Part 4): Converting to General Form",
        "subtitle": "Unit 3 • Lecture 32 • Section 3.0 Example 6H (Workbook p. 61)",
        "detail": "Lecture 32: Reading Parabola Graphs",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 6H: Algebraic Expansion (Workbook p. 61)\nSimplify the function $\\mathbf{f(x) = -2(x + 1)^2 + 8}$ into **General Form** ($ax^2 + bx + c$):\n- FOIL $(x + 1)^2$ first.\n- Distribute $-2$.\n- Combine like terms.",
        "solution": "$$\\begin{aligned}\nf(x) & = -2(x + 1)^2 + 8 \\\\[0.5em]\n& = -2(x^2 + 2x + 1) + 8 \\quad (\\text{FOIL first!}) \\\\[0.5em]\n& = -2x^2 - 4x - 2 + 8 \\quad (\\text{distribute } -2) \\\\[0.5em]\n\\mathbf{f(x)} & = \\mathbf{-2x^2 - 4x + 6}\n\\end{aligned}$$",
        "pitfall": "**Order of operations:** Square $(x + 1)$ FIRST! Do NOT multiply $-2$ into $(x + 1)$ before squaring!",
        "script": "[Prof. Park] In 6H, expand $(x + 1)^2 = x^2 + 2x + 1$. Then distribute $-2$: $-2x^2 - 4x - 2 + 8 = -2x^2 - 4x + 6$.\n\n[TA Sora] Notice the constant $+6$ matches our $y$-intercept $(0, 6)$! Both forms confirm each other."
    },
    {
        "num": 9,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 3.0 Part 2 Mastery Summary",
        "subtitle": "Unit 3 • Lecture 32 • Section 3.0 Wrap-up",
        "detail": "Lecture 32: Reading Parabola Graphs",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Parabola Graphing Comparison\n- **General Form:** $f(x) = ax^2 + bx + c \\implies y$-intercept is $(0, c)$.\n- **Vertex Form:** $f(x) = a(x - h)^2 + k \\implies$ Vertex is $(h, k)$.\n- **Axis of Symmetry:** Always $x = h$.\n- **If $a > 0$:** Minimum $= k$, Range $= [k, \\infty)$.\n- **If $a < 0$:** Maximum $= k$, Range $= (-\\infty, k]$.",
        "solution": "$$\\mathbf{\\text{Lecture 32 Mastered! Next Up: Lecture 33 — Advanced Quadratic Evaluation \\& Shifts!}}$$",
        "pitfall": "**Remember:** The axis of symmetry always passes directly through the vertex!",
        "script": "[Prof. Park] What a great lecture! You now know how to read any parabola graph.\n\n[TA Sora] In Lecture 33, we practice advanced evaluations and transformations before deriving the vertex formula!"
    }
]

# L33: Section 3.0 Part 3 (Workbook p. 62) - 8 slides
data_31_35[33] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 7A & 7B: Evaluating at -1",
        "subtitle": "Unit 3 • Lecture 33 • Section 3.0 Example 7A, B (Workbook p. 62)",
        "detail": "Lecture 33: Advanced Quadratic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 7A & 7B (Workbook p. 62)\nLet $\\mathbf{g(x) = -x^2 + 2x + 7}$ and $\\mathbf{h(x) = 3(x - 2)^2 - 5}$. Evaluate:\n- **A.** $g(-1)$\n- **B.** $h(-1)$\nUse proper notation and simplify completely.",
        "solution": "$$\\begin{aligned}\n\\textbf{A. } g(-1) & = -(-1)^2 + 2(-1) + 7 \\\\\n& = -(1) - 2 + 7 = -1 - 2 + 7 = \\mathbf{4} \\implies (-1, 4) \\\\[0.8em]\n\\textbf{B. } h(-1) & = 3(-1 - 2)^2 - 5 = 3(-3)^2 - 5 \\\\\n& = 3(9) - 5 = 27 - 5 = \\mathbf{22} \\implies (-1, 22)\n\\end{aligned}$$",
        "pitfall": "**The minus sign outside the square:** $-(-1)^2 = -(1) = -1$. The negative sign is OUTSIDE the base, so it stays negative!",
        "script": "[Prof. Park] In Example 7A, watch $-(-1)^2$. Square $-1$ first to get $+1$, then apply the negative sign to get $-1$.\n\n[TA Sora] So $-1 - 2 + 7 = 4$! And for $h(-1)$, $(-3)^2 = 9$, times 3 is 27, minus 5 is 22!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 7C & 7D: Evaluating at Zero & Y-Intercepts",
        "subtitle": "Unit 3 • Lecture 33 • Section 3.0 Example 7C, D (Workbook p. 62)",
        "detail": "Lecture 33: Advanced Quadratic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 7C & 7D (Workbook p. 62)\nLet $\\mathbf{g(x) = -x^2 + 2x + 7}$ and $\\mathbf{h(x) = 3(x - 2)^2 - 5}$. Evaluate:\n- **C.** $h(0)$\n- **D.** $g(0)$\nNotice what both functions have in common!",
        "solution": "$$\\begin{aligned}\n\\textbf{C. } h(0) & = 3(0 - 2)^2 - 5 = 3(-2)^2 - 5 = 3(4) - 5 = 12 - 5 = \\mathbf{7} \\implies \\mathbf{(0, 7)} \\\\[0.8em]\n\\textbf{D. } g(0) & = -(0)^2 + 2(0) + 7 = 0 + 0 + 7 = \\mathbf{7} \\implies \\mathbf{(0, 7)} \\\\[0.8em]\n\\mathbf{\\text{Insight: }} & \\mathbf{\\text{Both parabolas cross the } y\\text{-axis at the EXACT SAME point } (0, 7)!}\n\\end{aligned}$$",
        "pitfall": "**Zero in vertex form:** In $h(x)$, plugging in $0$ gives $(-2)^2 = 4$, times 3 is 12, minus 5 is 7. Do not assume the answer is $-5$!",
        "script": "[Prof. Park] Look at that fascinating result! Both $g(0)$ and $h(0)$ equal 7.\n\n[TA Sora] Both parabolas pass through the exact same $y$-intercept $(0, 7)$! Look at them intersecting on the coordinate plane.",
        "graph": {
            "xMin": -3, "xMax": 5, "yMin": -6, "yMax": 12,
            "title": "g(x) and h(x) Intersecting at y-intercept (0, 7)",
            "points": [
                {"x": 0, "y": 7, "label": "Shared y-int (0, 7)", "color": "#10b981"},
                {"x": 2, "y": -5, "label": "Vertex h(2, -5)", "color": "#38bdf8"},
                {"x": 1, "y": 8, "label": "Vertex g(1, 8)", "color": "#ec4899"}
            ],
            "curves": [
                {"a": -1, "b": 2, "c": 7, "color": "#ec4899", "strokeWidth": 2.5, "label": "g(x)"},
                {"a": 3, "b": -12, "c": 7, "color": "#38bdf8", "strokeWidth": 2.5, "label": "h(x)"}
            ]
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 7E: Fractional Input h(5/2)",
        "subtitle": "Unit 3 • Lecture 33 • Section 3.0 Example 7E (Workbook p. 62)",
        "detail": "Lecture 33: Advanced Quadratic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 7E (Workbook p. 62)\nLet $\\mathbf{h(x) = 3(x - 2)^2 - 5}$. Evaluate:\n$$\\mathbf{h\\left(\\frac{5}{2}\\right)}$$\n- Subtract $\\frac{5}{2} - 2$ using a common denominator.\n- Square the fraction.\n- Multiply by 3 and subtract 5.",
        "solution": "$$\\begin{aligned}\nh\\left(\\frac{5}{2}\\right) & = 3\\left(\\frac{5}{2} - 2\\right)^2 - 5 = 3\\left(\\frac{5}{2} - \\frac{4}{2}\\right)^2 - 5 \\\\[0.5em]\n& = 3\\left(\\frac{1}{2}\\right)^2 - 5 = 3\\left(\\frac{1}{4}\\right) - 5 \\\\[0.5em]\n& = \\frac{3}{4} - 5 = \\frac{3}{4} - \\frac{20}{4} \\\\[0.5em]\n\\mathbf{h\\left(\\frac{5}{2}\\right)} & = \\mathbf{-\\frac{17}{4} = -4.25}\n\\end{aligned}$$",
        "pitfall": "**Squaring fractions:** $(\\frac{1}{2})^2 = \\frac{1}{4}$. Square both numerator and denominator!",
        "script": "[Prof. Park] In 7E, $\\frac{5}{2} - 2 = \\frac{1}{2}$. Squared gives $\\frac{1}{4}$. Times 3 gives $\\frac{3}{4}$.\n\n[TA Sora] And $\\frac{3}{4} - 5 = -\\frac{17}{4} = -4.25$! Solid fraction arithmetic."
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 7F: Variable Input g(a)",
        "subtitle": "Unit 3 • Lecture 33 • Section 3.0 Example 7F (Workbook p. 62)",
        "detail": "Lecture 33: Advanced Quadratic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 7F (Workbook p. 62)\nLet $\\mathbf{g(x) = -x^2 + 2x + 7}$. Evaluate:\n$$\\mathbf{g(a)}$$",
        "solution": "$$\\begin{aligned}\ng(x) & = -x^2 + 2x + 7 \\\\[0.5em]\n\\mathbf{g(a)} & = \\mathbf{-a^2 + 2a + 7}\n\\end{aligned}$$",
        "pitfall": "**Don't overcomplicate:** Replace every occurrence of $x$ with $a$. You're done!",
        "script": "[Prof. Park] When evaluating at $a$, simply replace $x$ with $a$.\n\n[TA Sora] $g(a) = -a^2 + 2a + 7$. Straightforward and clean!"
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 7G: Binomial Input g(x - 6)",
        "subtitle": "Unit 3 • Lecture 33 • Section 3.0 Example 7G (Workbook p. 62)",
        "detail": "Lecture 33: Advanced Quadratic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 7G (Workbook p. 62)\nLet $\\mathbf{g(x) = -x^2 + 2x + 7}$. Evaluate and simplify:\n$$\\mathbf{g(x - 6)}$$\n- Replace $x$ with $(x - 6)$.\n- Expand $(x - 6)^2 = x^2 - 12x + 36$.\n- Distribute the negative sign and combine like terms.",
        "solution": "$$\\begin{aligned}\ng(x - 6) & = -(x - 6)^2 + 2(x - 6) + 7 \\\\[0.5em]\n& = -(x^2 - 12x + 36) + 2x - 12 + 7 \\\\[0.5em]\n& = -x^2 + 12x - 36 + 2x - 12 + 7 \\\\[0.5em]\n\\mathbf{g(x - 6)} & = \\mathbf{-x^2 + 14x - 41}\n\\end{aligned}$$",
        "pitfall": "**Distribute negative to all 3 terms:** $-(x^2 - 12x + 36) = -x^2 + 12x - 36$. Watch the middle sign flip to $+12x$!",
        "script": "[Prof. Park] In 7G, expand $(x - 6)^2$ first, then negate all three terms: $-x^2 + 12x - 36$.\n\n[TA Sora] Then add $2x - 12 + 7$. Combining like terms gives $-x^2 + 14x - 41$!"
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.0 Example 7H: Binomial Input h(k + 1)",
        "subtitle": "Unit 3 • Lecture 33 • Section 3.0 Example 7H (Workbook p. 62)",
        "detail": "Lecture 33: Advanced Quadratic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 7H (Workbook p. 62)\nLet $\\mathbf{h(x) = 3(x - 2)^2 - 5}$. Evaluate and simplify:\n$$\\mathbf{h(k + 1)}$$\n- Simplify inside the parentheses first: $(k + 1 - 2)$.\n- Square the simplified binomial.\n- Distribute 3 and subtract 5.",
        "solution": "$$\\begin{aligned}\nh(k + 1) & = 3((k + 1) - 2)^2 - 5 \\\\[0.5em]\n& = 3(k - 1)^2 - 5 \\quad (\\text{combine inside first!}) \\\\[0.5em]\n& = 3(k^2 - 2k + 1) - 5 \\\\[0.5em]\n& = 3k^2 - 6k + 3 - 5 \\\\[0.5em]\n\\mathbf{h(k + 1)} & = \\mathbf{3k^2 - 6k - 2}\n\\end{aligned}$$",
        "pitfall": "**Simplify inside parentheses first:** Notice how $(k + 1 - 2)$ simplifies to $(k - 1)$ immediately, saving you from a much messier expansion!",
        "script": "[Prof. Park] Smart algebraists simplify inside parentheses first: $k + 1 - 2 = k - 1$.\n\n[TA Sora] Squaring $(k - 1)$ gives $k^2 - 2k + 1$. Multiply by 3 to get $3k^2 - 6k + 3$, then minus 5 gives $3k^2 - 6k - 2$!"
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Sora's Pitfall Alert",
        "title": "The Negative Base Trap: -x^2 vs (-x)^2",
        "subtitle": "Unit 3 • Lecture 33 • Section 3.0 Pitfall Alert",
        "detail": "Lecture 33: Advanced Quadratic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Why Students Lose Points on Negative Squares\nEvaluate both expressions when $x = 3$ and when $x = -3$:\n- **Case 1:** $-x^2$\n- **Case 2:** $(-x)^2$\nExplain the difference using order of operations.",
        "solution": "$$\\begin{array}{|c|c|c|} \n\\hline\n\\textbf{Expression} & x = 3 & x = -3 \\\\\n\\hline\n-x^2 & -(3^2) = -(9) = \\mathbf{-9} & -((-3)^2) = -(9) = \\mathbf{-9} \\\\\n\\hline\n(-x)^2 & (-3)^2 = \\mathbf{+9} & (-(-3))^2 = (3)^2 = \\mathbf{+9} \\\\\n\\hline\n\\end{array}$$",
        "pitfall": "**Order of operations rule:** Exponents come BEFORE negation! In $-x^2$, you square $x$ first, then apply the negative sign. It is ALWAYS negative (or zero)!",
        "script": "[Prof. Park] Sora, this is the single most common error on Unit 3 quizzes.\n\n[TA Sora] Yes! In $-x^2$, the negative sign sits outside the square. No matter what real number you plug in, $-x^2$ is ALWAYS negative!"
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 3.0 Complete Mastery Summary",
        "subtitle": "Unit 3 • Lecture 33 • Section 3.0 Wrap-up",
        "detail": "Lecture 33: Advanced Quadratic Evaluation",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Section 3.0 Complete Mastery Checklist\n- Identified terms and coefficients in general form $ax^2 + bx + c$.\n- Analyzed parabolas: vertex, axis of symmetry, intercepts, min/max.\n- Converted vertex form $a(x - h)^2 + k$ to general form.\n- Evaluated quadratic functions with negative, fractional, and binomial inputs.",
        "solution": "$$\\mathbf{\\text{Section 3.0 Mastered! Next Up: Section 3.1 — The Vertex Formula } x = -\\frac{b}{2a}!}$$",
        "pitfall": "**Ready for Section 3.1:** What if we have general form $ax^2 + bx + c$ without a graph? In Section 3.1, we derive the formula to find the vertex instantly!",
        "script": "[Prof. Park] Congratulations on completing Section 3.0! You have mastered the foundations of quadratic functions.\n\n[TA Sora] In Lecture 34, we learn the famous formula $x = -\\frac{b}{2a}$ to find the vertex without graphing!"
    }
]

# L34: Section 3.1 Part 1 (Workbook pp. 63 - 65) - 8 slides
data_31_35[34] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Section 3.1: The Vertex Formula x_v = -b / (2a)",
        "subtitle": "Unit 3 • Lecture 34 • Section 3.1 (Workbook p. 63)",
        "detail": "Lecture 34: The Vertex Formula",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### The Vertex Formula (Workbook p. 63)\nFor any quadratic function in General Form $\\mathbf{f(x) = ax^2 + bx + c}$:\n- **$x$-coordinate of the vertex:**\n  $$\\mathbf{x_v = -\\frac{b}{2a}}$$\n- **$y$-coordinate of the vertex:**\n  $$\\mathbf{y_v = f(x_v)} = f\\left(-\\frac{b}{2a}\\right)$$\n- **Axis of Symmetry:** The vertical line $\\mathbf{x = -\\frac{b}{2a}}$.\n- **$y$-intercept:** Always $\\mathbf{(0, c)}$ since $f(0) = c$.",
        "solution": "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Identify } a, b, c \\text{ from } ax^2 + bx + c. \\\\\n\\text{Step 2: } & \\text{Compute } x_v = -\\frac{b}{2a}. \\\\\n\\text{Step 3: } & \\text{Substitute } x_v \\text{ into } f(x) \\text{ to find } y_v. \\\\\n\\text{Step 4: } & \\text{Vertex is } (x_v, y_v). \\text{ Axis of symmetry is } x = x_v.\n\\end{aligned}$$",
        "pitfall": "**Division by 2a:** Make sure to multiply $2 \\cdot a$ in the denominator before dividing! Use protective parentheses: $-b / (2a)$.",
        "script": "[Prof. Park] Welcome to Section 3.1! This formula $x = -\\frac{b}{2a}$ is your superpower. It finds the exact turning point of any parabola in seconds.\n\n[TA Sora] Once you have $x$, just plug it back into the function to get $y$!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.1 Example 1: Finding Vertex for f(x) = x^2 + 6x - 8",
        "subtitle": "Unit 3 • Lecture 34 • Section 3.1 Example 1 (Workbook p. 63)",
        "detail": "Lecture 34: The Vertex Formula",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 1 (Workbook p. 63)\nFor $\\mathbf{f(x) = x^2 + 6x - 8}$:\n- **A. Find the vertex:** __________________________\n- **B. Find the $y$-intercept:** __________________________\n- **C. Axis of Symmetry:** __________________________\n- **D. Maximum or Minimum Value:** __________________________",
        "solution": "$$\\begin{aligned}\n\\text{Identify: } & a = 1, \\quad b = 6, \\quad c = -8 \\\\[0.5em]\n\\mathbf{x_v} & = -\\frac{b}{2a} = -\\frac{6}{2(1)} = \\mathbf{-3} \\\\[0.5em]\n\\mathbf{y_v} & = f(-3) = (-3)^2 + 6(-3) - 8 = 9 - 18 - 8 = \\mathbf{-17} \\\\[0.8em]\n\\textbf{A. Vertex: } & \\mathbf{(-3, -17)} \\\\\n\\textbf{B. y-intercept: } & \\mathbf{(0, -8)} \\quad (c = -8) \\\\\n\\textbf{C. Axis of Symmetry: } & \\mathbf{x = -3} \\\\\n\\textbf{D. Minimum Value: } & \\mathbf{-17} \\quad (a = 1 > 0 \\implies \\text{opens up})\n\\end{aligned}$$",
        "pitfall": "**Squaring negative 3:** $(-3)^2 = +9$. Then $9 - 18 = -9$, and $-9 - 8 = -17$!",
        "script": "[Prof. Park] In Example 1, $a = 1, b = 6$. So $x_v = -\\frac{6}{2} = -3$. Plugging $-3$ in gives $y_v = -17$.\n\n[TA Sora] The vertex is $(-3, -17)$. Since $a > 0$, the parabola opens up, making $-17$ a MINIMUM value!",
        "graph": {
            "xMin": -8, "xMax": 2, "yMin": -20, "yMax": 4,
            "title": "Example 1: f(x) = x^2 + 6x - 8 (Vertex (-3, -17))",
            "points": [
                {"x": -3, "y": -17, "label": "Min Vertex (-3, -17)", "color": "#38bdf8"},
                {"x": 0, "y": -8, "label": "y-int (0, -8)", "color": "#10b981"}
            ],
            "curves": [
                {"a": 1, "b": 6, "c": -8, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": -3
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.1 Example 2: Fraction Leading Coefficient",
        "subtitle": "Unit 3 • Lecture 34 • Section 3.1 Example 2 (Workbook p. 63)",
        "detail": "Lecture 34: The Vertex Formula",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 2 (Workbook p. 63)\nFor $\\mathbf{f(x) = -\\frac{1}{4}x^2 - 3x + 9}$:\n- **A. Find the vertex:** __________________________\n- **B. Find the $y$-intercept:** __________________________\n- **C. Axis of Symmetry:** __________________________\n- **D. Maximum or Minimum Value:** __________________________",
        "solution": "$$\\begin{aligned}\n\\text{Identify: } & a = -\\frac{1}{4}, \\quad b = -3, \\quad c = 9 \\\\[0.5em]\n\\mathbf{x_v} & = -\\frac{b}{2a} = -\\frac{-3}{2\\left(-\\frac{1}{4}\\right)} = -\\frac{-3}{-\\frac{1}{2}} = -\\left(3 \\cdot 2\\right) = \\mathbf{-6} \\\\[0.8em]\n\\mathbf{y_v} & = f(-6) = -\\frac{1}{4}(-6)^2 - 3(-6) + 9 \\\\\n& = -\\frac{1}{4}(36) + 18 + 9 = -9 + 18 + 9 = \\mathbf{18} \\\\[0.8em]\n\\textbf{A. Vertex: } & \\mathbf{(-6, 18)} \\\\\n\\textbf{B. y-intercept: } & \\mathbf{(0, 9)} \\\\\n\\textbf{C. Axis of Symmetry: } & \\mathbf{x = -6} \\\\\n\\textbf{D. Maximum Value: } & \\mathbf{18} \\quad (a < 0 \\implies \\text{opens down})\n\\end{aligned}$$",
        "pitfall": "**Watch triple negatives:** In $x_v = -\\frac{-3}{2(-1/4)}$, three minus signs equal a negative: $-6$!",
        "script": "[Prof. Park] In Example 2, the denominator is $2(-\\frac{1}{4}) = -\\frac{1}{2}$. Dividing $-3$ by $-\\frac{1}{2}$ is $+6$, then negated gives $-6$.\n\n[TA Sora] Then $f(-6) = -\\frac{1}{4}(36) + 18 + 9 = 18$. The vertex is $(-6, 18)$ and it's a MAXIMUM value of 18!",
        "graph": {
            "xMin": -12, "xMax": 2, "yMin": 0, "yMax": 22,
            "title": "Example 2: f(x) = -1/4x^2 - 3x + 9 (Vertex (-6, 18))",
            "points": [
                {"x": -6, "y": 18, "label": "Max Vertex (-6, 18)", "color": "#ec4899"},
                {"x": 0, "y": 9, "label": "y-int (0, 9)", "color": "#10b981"}
            ],
            "curves": [
                {"a": -0.25, "b": -3, "c": 9, "color": "#ec4899", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": -6
        }
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Core Concept",
        "title": "Why Does x = -b / (2a) Work? The Midpoint of Roots",
        "subtitle": "Unit 3 • Lecture 34 • Section 3.1 Geometric Derivation",
        "detail": "Lecture 34: The Vertex Formula",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### The Origin of the Vertex Formula\nRecall the Quadratic Formula for finding roots:\n$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a} = \\mathbf{-\\frac{b}{2a}} \\pm \\frac{\\sqrt{b^2 - 4ac}}{2a}$$\n- Notice the central starting value: **$-\\frac{b}{2a}$**!\n- The two $x$-intercepts spread out symmetrically to the left and right by $\\pm \\frac{\\sqrt{b^2 - 4ac}}{2a}$.\n- Therefore, the exact middle (axis of symmetry) is always at **$x = -\\frac{b}{2a}$**!",
        "solution": "$$\\begin{aligned}\n\\text{Root 1: } & x_1 = -\\frac{b}{2a} - \\frac{\\sqrt{D}}{2a} \\\\\n\\text{Root 2: } & x_2 = -\\frac{b}{2a} + \\frac{\\sqrt{D}}{2a} \\\\[0.5em]\n\\text{Midpoint: } & \\frac{x_1 + x_2}{2} = \\frac{-2b / (2a)}{2} = \\mathbf{-\\frac{b}{2a}}\n\\end{aligned}$$",
        "pitfall": "**Even when there are no real x-intercepts:** Even if a parabola never touches the $x$-axis, $-\\frac{b}{2a}$ STILL gives the exact vertex!",
        "script": "[Prof. Park] Look at how beautifully mathematics connects. The vertex formula is simply the center point of the quadratic formula!\n\n[TA Sora] That's why the axis of symmetry is always exactly in the middle of any two symmetric points!"
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Step-by-Step Guide",
        "title": "Sora's Protocol for Finding the Vertex & Max/Min",
        "subtitle": "Unit 3 • Lecture 34 • Section 3.1 Protocol",
        "detail": "Lecture 34: The Vertex Formula",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Sora's 4-Step Vertex Checklist\n1. **Identify $a, b, c$:** Make sure the equation is in standard descending order $ax^2 + bx + c$.\n2. **Calculate $x_v$:** $x_v = -\\frac{b}{2a}$. Write out $-b$ and $(2a)$ with parentheses.\n3. **Calculate $y_v$:** Substitute $x_v$ back into the original function: $y_v = f(x_v)$.\n4. **Classify Max vs Min:**\n   - If $a > 0$: **Minimum value is $y_v$ at $x = x_v$.\n   - If $a < 0$: **Maximum value is $y_v$ at $x = x_v$.",
        "solution": "$$\\begin{array}{|c|c|} \n\\hline\n\\textbf{Feature} & \\textbf{How to Report} \\\\\n\\hline\n\\text{Vertex} & (x_v, y_v) \\\\\n\\hline\n\\text{Axis of Symmetry} & \\mathbf{x = x_v} \\; (\\text{include 'x ='}) \\\\\n\\hline\n\\text{Max or Min Value} & y_v \\; (\\text{just the number}) \\\\\n\\hline\n\\text{Where it occurs} & \\text{at } x = x_v \\\\\n\\hline\n\\end{array}$$",
        "pitfall": "**Reporting Max/Min:** Exam question: 'Find the maximum value of $f(x)$'. Correct answer: $18$. Incorrect answer: $(-6, 18)$. The value is strictly the $y$-coordinate!",
        "script": "[Prof. Park] Sora's table will save you from common test pitfalls. Pay attention to how the question is phrased!\n\n[TA Sora] 'Maximum value' means $y$. 'Where it occurs' means $x$!"
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Practice Problem",
        "title": "Check Your Understanding: Vertex of f(x) = -2x^2 + 8x - 3",
        "subtitle": "Unit 3 • Lecture 34 • Section 3.1 Checkpoint",
        "detail": "Lecture 34: The Vertex Formula",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Checkpoint Practice\nFind the vertex, axis of symmetry, and state whether it is a maximum or minimum for:\n$$\\mathbf{f(x) = -2x^2 + 8x - 3}$$",
        "solution": "$$\\begin{aligned}\n\\text{Identify: } & a = -2, \\quad b = 8, \\quad c = -3 \\\\[0.5em]\nx_v & = -\\frac{8}{2(-2)} = -\\frac{8}{-4} = \\mathbf{2} \\\\[0.5em]\ny_v & = f(2) = -2(2)^2 + 8(2) - 3 = -2(4) + 16 - 3 = -8 + 16 - 3 = \\mathbf{5} \\\\[0.8em]\n\\mathbf{\\text{Vertex: }} & \\mathbf{(2, 5)} \\\\\n\\mathbf{\\text{Axis of Symmetry: }} & \\mathbf{x = 2} \\\\\n\\mathbf{\\text{Maximum Value: }} & \\mathbf{5} \\quad (a = -2 < 0 \\implies \\text{opens down})\n\\end{aligned}$$",
        "pitfall": "**Negative leading coefficient:** $-2(2)^2 = -2(4) = -8$. Don't make it $+8$!",
        "script": "[Prof. Park] In this checkpoint, $x_v = -\\frac{8}{-4} = 2$. $f(2) = -8 + 16 - 3 = 5$.\n\n[TA Sora] Vertex is $(2, 5)$, and the maximum value is 5 occurring at $x = 2$!",
        "graph": {
            "xMin": -2, "xMax": 6, "yMin": -5, "yMax": 7,
            "title": "Checkpoint: f(x) = -2x^2 + 8x - 3 (Vertex (2, 5))",
            "points": [
                {"x": 2, "y": 5, "label": "Max Vertex (2, 5)", "color": "#ec4899"},
                {"x": 0, "y": -3, "label": "y-int (0, -3)", "color": "#10b981"}
            ],
            "curves": [
                {"a": -2, "b": 8, "c": -3, "color": "#ec4899", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 2
        }
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Visual & Coordinate Grid",
        "title": "Visualizing Vertex & Symmetry on the Grid",
        "subtitle": "Unit 3 • Lecture 34 • Section 3.1 Visual Analysis",
        "detail": "Lecture 34: The Vertex Formula",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### The Mirror Property of Parabolas\nEvery point on a parabola has a reflection across the axis of symmetry $x = h$:\n- Point $(0, -3)$ is $2$ units left of $x = 2$.\n- Its reflection is $(4, -3)$, exactly $2$ units right of $x = 2$!\nVerify: $f(4) = -2(4)^2 + 8(4) - 3 = -32 + 32 - 3 = -3$.",
        "solution": "$$\\begin{aligned}\n\\text{Left Point: } & (0, -3) \\quad [\\text{distance to } x=2 \\text{ is } 2] \\\\\n\\text{Right Point: } & (4, -3) \\quad [\\text{distance to } x=2 \\text{ is } 2] \\\\[0.5em]\n\\text{Symmetric Heights: } & f(0) = f(4) = -3\n\\end{aligned}$$",
        "pitfall": "**Use symmetry to graph quickly:** If you know the $y$-intercept $(0, c)$, reflect it across the axis of symmetry to instantly get a free second point!",
        "script": "[Prof. Park] Notice how $(0, -3)$ and $(4, -3)$ sit at the exact same height on opposite sides of the gold axis of symmetry line.\n\n[TA Sora] Parabolas are perfectly bilateral! This mirror symmetry makes graphing fast and accurate.",
        "graph": {
            "xMin": -2, "xMax": 6, "yMin": -5, "yMax": 7,
            "title": "Bilateral Symmetry: Reflection across x = 2",
            "points": [
                {"x": 0, "y": -3, "label": "(0, -3)", "color": "#10b981"},
                {"x": 4, "y": -3, "label": "Mirror (4, -3)", "color": "#38bdf8"},
                {"x": 2, "y": 5, "label": "Vertex (2, 5)", "color": "#ec4899"}
            ],
            "curves": [
                {"a": -2, "b": 8, "c": -3, "color": "#ec4899", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 2
        }
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 3.1 Part 1 Mastery Summary",
        "subtitle": "Unit 3 • Lecture 34 • Section 3.1 Wrap-up",
        "detail": "Lecture 34: The Vertex Formula",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Section 3.1 Part 1 Master Summary\n- **Formula:** $x_v = -\\frac{b}{2a}$, $y_v = f(x_v)$.\n- **Axis of Symmetry:** $x = x_v$.\n- **$y$-intercept:** $(0, c)$.\n- **Optimization:** If $a > 0$, vertex is minimum; if $a < 0$, vertex is maximum.",
        "solution": "$$\\mathbf{\\text{Lecture 34 Complete! Next Up: Lecture 35 — Vertex from Vertex Form } a(x-h)^2 + k!}$$",
        "pitfall": "**Double check signs:** A sign error in $x = -b/(2a)$ ruins both the vertex and axis of symmetry!",
        "script": "[Prof. Park] Great job! In Lecture 35, we examine how Vertex Form lets us read the vertex without doing any calculation at all!"
    }
]

# L35: Section 3.1 Part 2 (Workbook pp. 65 - 66) - 8 slides
data_31_35[35] = [
    {
        "num": 1,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.1 Example 3: f(x) = -3(x - 4)^2 + 7",
        "subtitle": "Unit 3 • Lecture 35 • Section 3.1 Example 3 (Workbook p. 64)",
        "detail": "Lecture 35: Vertex Form & Min/Max Analysis",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 3 (Workbook p. 64)\nFor $\\mathbf{f(x) = -3(x - 4)^2 + 7}$:\n- **A. Find the vertex:** __________________________\n- **B. Find the $y$-intercept:** __________________________\n- **C. Axis of Symmetry:** __________________________\n- **D. Maximum or Minimum Value:** __________________________",
        "solution": "$$\\begin{aligned}\n\\text{Compare with } a(x - h)^2 + k: & a = -3, \\quad h = 4, \\quad k = 7 \\\\[0.5em]\n\\textbf{A. Vertex: } & \\mathbf{(4, 7)} \\\\[0.5em]\n\\textbf{B. y-intercept: } & f(0) = -3(0 - 4)^2 + 7 = -3(16) + 7 = -48 + 7 = \\mathbf{-41} \\implies \\mathbf{(0, -41)} \\\\[0.5em]\n\\textbf{C. Axis of Symmetry: } & \\mathbf{x = 4} \\\\[0.5em]\n\\textbf{D. Maximum Value: } & \\mathbf{7} \\quad (a = -3 < 0 \\implies \\text{opens down})\n\\end{aligned}$$",
        "pitfall": "**Inside vs Outside:** $(x - 4)$ means $h = +4$! It flips sign! The outside constant $+7$ keeps its sign: $k = 7$!",
        "script": "[Prof. Park] In Example 3, we read the vertex directly from vertex form: $(4, 7)$.\n\n[TA Sora] Since $a = -3$ is negative, it opens downward, so the maximum value is 7 at $x = 4$!"
    },
    {
        "num": 2,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.1 Example 4: f(x) = 5(x - 1)^2 + 3",
        "subtitle": "Unit 3 • Lecture 35 • Section 3.1 Example 4 (Workbook p. 64)",
        "detail": "Lecture 35: Vertex Form & Min/Max Analysis",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 4 (Workbook p. 64)\nFor $\\mathbf{f(x) = 5(x - 1)^2 + 3}$:\n- **A. Find the vertex:** __________________________\n- **B. Find the $y$-intercept:** __________________________\n- **C. Axis of Symmetry:** __________________________\n- **D. Maximum or Minimum Value:** __________________________",
        "solution": "$$\\begin{aligned}\n\\text{Compare with } a(x - h)^2 + k: & a = 5, \\quad h = 1, \\quad k = 3 \\\\[0.5em]\n\\textbf{A. Vertex: } & \\mathbf{(1, 3)} \\\\[0.5em]\n\\textbf{B. y-intercept: } & f(0) = 5(0 - 1)^2 + 3 = 5(1) + 3 = \\mathbf{8} \\implies \\mathbf{(0, 8)} \\\\[0.5em]\n\\textbf{C. Axis of Symmetry: } & \\mathbf{x = 1} \\\\[0.5em]\n\\textbf{D. Minimum Value: } & \\mathbf{3} \\quad (a = 5 > 0 \\implies \\text{opens up})\n\\end{aligned}$$",
        "pitfall": "**Finding y-intercept in vertex form:** You must calculate $f(0)$! Do not guess that $b$ is 3!",
        "script": "[Prof. Park] In Example 4, $h = 1$ and $k = 3$, so the vertex is $(1, 3)$.\n\n[TA Sora] Since $a = 5 > 0$, the parabola opens up, making 3 a MINIMUM value at $x = 1$!",
        "graph": {
            "xMin": -2, "xMax": 4, "yMin": 0, "yMax": 14,
            "title": "Example 4: f(x) = 5(x - 1)^2 + 3 (Min at (1, 3))",
            "points": [
                {"x": 1, "y": 3, "label": "Min Vertex (1, 3)", "color": "#38bdf8"},
                {"x": 0, "y": 8, "label": "y-int (0, 8)", "color": "#10b981"}
            ],
            "curves": [
                {"a": 5, "b": -10, "c": 8, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 1
        }
    },
    {
        "num": 3,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.1 Example 5: f(x) = -6(x + 2)^2 - 9",
        "subtitle": "Unit 3 • Lecture 35 • Section 3.1 Example 5 (Workbook p. 64)",
        "detail": "Lecture 35: Vertex Form & Min/Max Analysis",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 5 (Workbook p. 64)\nFor $\\mathbf{f(x) = -6(x + 2)^2 - 9}$:\n- **A. Find the vertex:** __________________________\n- **B. Find the $y$-intercept:** __________________________\n- **C. Axis of Symmetry:** __________________________\n- **D. Maximum or Minimum Value:** __________________________",
        "solution": "$$\\begin{aligned}\n\\text{Notice: } & x + 2 = x - (-2) \\implies h = -2, \\quad k = -9 \\\\[0.5em]\n\\textbf{A. Vertex: } & \\mathbf{(-2, -9)} \\\\[0.5em]\n\\textbf{B. y-intercept: } & f(0) = -6(0 + 2)^2 - 9 = -6(4) - 9 = -24 - 9 = \\mathbf{-33} \\implies \\mathbf{(0, -33)} \\\\[0.5em]\n\\textbf{C. Axis of Symmetry: } & \\mathbf{x = -2} \\\\[0.5em]\n\\textbf{D. Maximum Value: } & \\mathbf{-9} \\quad (a = -6 < 0 \\implies \\text{opens down})\n\\end{aligned}$$",
        "pitfall": "**Plus sign inside:** $(x + 2)$ means $h = -2$! Remember, the formula has a minus sign: $(x - h)$.",
        "script": "[Prof. Park] In Example 5, $(x + 2)$ means $h = -2$. The vertex is $(-2, -9)$.\n\n[TA Sora] Opening downward with $a = -6$, so the maximum value is $-9$ occurring at $x = -2$!"
    },
    {
        "num": 4,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.1 Example 6: Vertex of f(x) = 2x^2 - 7",
        "subtitle": "Unit 3 • Lecture 35 • Section 3.1 Example 6 (Workbook p. 66)",
        "detail": "Lecture 35: Vertex Form & Min/Max Analysis",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 6 (Workbook p. 66)\nFor $\\mathbf{f(x) = 2x^2 - 7}$:\n- **A. Find the vertex:** __________________________\n- **B. Find the $y$-intercept:** __________________________\n- **C. Axis of Symmetry:** __________________________\n- **D. Maximum or Minimum Value:** __________________________",
        "solution": "$$\\begin{aligned}\n\\text{Rewrite as vertex form: } & f(x) = 2(x - 0)^2 - 7 \\implies h = 0, \\; k = -7 \\\\[0.5em]\n\\text{Or use formula: } & x_v = -\\frac{0}{2(2)} = 0, \\quad y_v = 2(0)^2 - 7 = -7 \\\\[0.8em]\n\\textbf{A. Vertex: } & \\mathbf{(0, -7)} \\\\[0.5em]\n\\textbf{B. y-intercept: } & \\mathbf{(0, -7)} \\quad (\\text{Vertex IS the } y\\text{-intercept!}) \\\\[0.5em]\n\\textbf{C. Axis of Symmetry: } & \\mathbf{x = 0} \\quad (\\text{the } y\\text{-axis}) \\\\[0.5em]\n\\textbf{D. Minimum Value: } & \\mathbf{-7} \\quad (a = 2 > 0 \\implies \\text{opens up})\n\\end{aligned}$$",
        "pitfall": "**When b = 0:** The vertex sits directly ON the $y$-axis at $(0, c)$, and the axis of symmetry is the $y$-axis itself ($x = 0$)!",
        "script": "[Prof. Park] In Example 6, $b = 0$. That means the vertex and the $y$-intercept are the exact same point: $(0, -7)$!\n\n[TA Sora] And the axis of symmetry is the $y$-axis itself: $x = 0$.",
        "graph": {
            "xMin": -4, "xMax": 4, "yMin": -9, "yMax": 5,
            "title": "Example 6: f(x) = 2x^2 - 7 (Symmetric on y-axis)",
            "points": [
                {"x": 0, "y": -7, "label": "Vertex & y-int (0, -7)", "color": "#38bdf8"},
                {"x": 2, "y": 1, "label": "(2, 1)", "color": "#f59e0b"},
                {"x": -2, "y": 1, "label": "(-2, 1)", "color": "#f59e0b"}
            ],
            "curves": [
                {"a": 2, "b": 0, "c": -7, "color": "#38bdf8", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": 0
        }
    },
    {
        "num": 5,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.1 Example 7 (Part 1): Comprehensive Graph f(x) = -x^2 - 4x - 5",
        "subtitle": "Unit 3 • Lecture 35 • Section 3.1 Example 7A-E (Workbook p. 66)",
        "detail": "Lecture 35: Vertex Form & Min/Max Analysis",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 7 (Workbook p. 66)\nUsing the graph of the function $\\mathbf{f(x) = -x^2 - 4x - 5}$, find:\n- **A. $y$-intercept:** ____________\n- **B. $x$-intercepts:** ____________\n- **C. Vertex:** ____________\n- **D. Axis of Symmetry:** ____________\n- **E. Maximum value:** ____________",
        "solution": "$$\\begin{aligned}\n\\textbf{A. y-intercept: } & (0, -5) \\\\[0.5em]\n\\textbf{B. x-intercepts: } & \\mathbf{\\text{None (the graph never crosses the } x\\text{-axis!)}} \\\\[0.5em]\n\\textbf{C. Vertex: } & x_v = -\\frac{-4}{2(-1)} = -2, \\; y_v = -(-2)^2 - 4(-2) - 5 = -4 + 8 - 5 = \\mathbf{-1} \\\\\n& \\implies \\mathbf{(-2, -1)} \\\\[0.5em]\n\\textbf{D. Axis of Symmetry: } & \\mathbf{x = -2} \\\\[0.5em]\n\\textbf{E. Maximum Value: } & \\mathbf{-1} \\quad (\\text{at } x = -2)\n\\end{aligned}$$",
        "pitfall": "**No x-intercepts is common:** When a downward parabola has its vertex below the $x$-axis (here at $y = -1$), it can never touch the $x$-axis! There are NO real $x$-intercepts.",
        "script": "[Prof. Park] In Example 7, look at the graph. The peak vertex is at $(-2, -1)$, which is already below the $x$-axis, and it opens downward!\n\n[TA Sora] So it NEVER touches the $x$-axis! That means zero real $x$-intercepts.",
        "graph": {
            "xMin": -6, "xMax": 2, "yMin": -10, "yMax": 2,
            "title": "Example 7: f(x) = -x^2 - 4x - 5 (No Real x-intercepts)",
            "points": [
                {"x": -2, "y": -1, "label": "Max Vertex (-2, -1)", "color": "#ec4899"},
                {"x": 0, "y": -5, "label": "y-int (0, -5)", "color": "#10b981"},
                {"x": -4, "y": -5, "label": "Mirror (-4, -5)", "color": "#38bdf8"}
            ],
            "curves": [
                {"a": -1, "b": -4, "c": -5, "color": "#ec4899", "strokeWidth": 2.5}
            ],
            "axisOfSymmetry": -2
        }
    },
    {
        "num": 6,
        "type": "math_problem",
        "slideTypeLabel": "Official Workbook Problem",
        "title": "Section 3.1 Example 7 (Part 2): Graph Interrogation",
        "subtitle": "Unit 3 • Lecture 35 • Section 3.1 Example 7G-J (Workbook p. 66)",
        "detail": "Lecture 35: Vertex Form & Min/Max Analysis",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Example 7 Function Values (Workbook p. 66)\nUsing the graph of $f(x) = -x^2 - 4x - 5$:\n- **G.** $f(-4) = \\text{_____________}$\n- **H.** $f(x) = -2 \\implies x = \\text{_____________}$\n- **I.** $f(0) = \\text{_____________}$\n- **J.** $f(x) = -5 \\implies x = \\text{_____________}$",
        "solution": "$$\\begin{aligned}\n\\textbf{G. } f(-4) & = -(-4)^2 - 4(-4) - 5 = -16 + 16 - 5 = \\mathbf{-5} \\implies (-4, -5) \\\\[0.5em]\n\\textbf{H. } f(x) = -2 & \\implies \\mathbf{x = -1 \\quad \\text{and} \\quad x = -3} \\\\[0.5em]\n\\textbf{I. } f(0) & = \\mathbf{-5} \\implies (0, -5) \\\\[0.5em]\n\\textbf{J. } f(x) = -5 & \\implies \\mathbf{x = 0 \\quad \\text{and} \\quad x = -4} \\quad (\\text{symmetric pairs!})\n\\end{aligned}$$",
        "pitfall": "**Two answers for quadratic outputs:** Because of symmetry, solving $f(x) = -5$ gives TWO inputs: $x = 0$ and $x = -4$!",
        "script": "[Prof. Park] Notice how $f(0) = -5$ and $f(-4) = -5$. Both are at the same height of $-5$.\n\n[TA Sora] That's why solving $f(x) = -5$ gives both $x = 0$ and $x = -4$!"
    },
    {
        "num": 7,
        "type": "math_problem",
        "slideTypeLabel": "Comparison Matrix",
        "title": "General Form vs Vertex Form: Summary Matrix",
        "subtitle": "Unit 3 • Lecture 35 • Section 3.1 Master Comparison",
        "detail": "Lecture 35: Vertex Form & Min/Max Analysis",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Choosing Your Method\nCompare the two primary forms of quadratic functions:\n- **General Form:** $f(x) = ax^2 + bx + c$\n  - Best for: $y$-intercept $(0, c)$, factoring, and quadratic formula.\n  - Vertex requires calculation: $x = -\\frac{b}{2a}$.\n- **Vertex Form:** $f(x) = a(x - h)^2 + k$\n  - Best for: Reading vertex $(h, k)$ and axis $x = h$ instantly.\n  - $y$-intercept requires calculating $f(0)$.",
        "solution": "$$\\begin{array}{|c|c|c|} \n\\hline\n\\textbf{Feature} & \\textbf{General: } ax^2 + bx + c & \\textbf{Vertex: } a(x-h)^2 + k \\\\\n\\hline\n\\text{Vertex} & \\left(-\\frac{b}{2a}, \\; f\\left(-\\frac{b}{2a}\\right)\\right) & \\mathbf{(h, k)} \\; [\\text{Immediate!}] \\\\\n\\hline\n\\text{Axis of Symmetry} & x = -\\frac{b}{2a} & \\mathbf{x = h} \\\\\n\\hline\ny\\text{-intercept} & \\mathbf{(0, c)} \\; [\\text{Immediate!}] & (0, f(0)) \\\\\n\\hline\n\\text{Direction} & a > 0 \\text{ (up)}, \\; a < 0 \\text{ (down)} & \\text{Same } a \\\\\n\\hline\n\\end{array}$$",
        "pitfall": "**Both forms share the exact same 'a':** The coefficient $a$ is identical in both forms! If $a = -2$ in vertex form, $a = -2$ in general form.",
        "script": "[Prof. Park] This matrix summarizes Section 3.1 completely.\n\n[TA Sora] Keep this cheat sheet handy for every homework problem and exam!"
    },
    {
        "num": 8,
        "type": "math_problem",
        "slideTypeLabel": "Section Mastery",
        "title": "Section 3.1 Complete Mastery Summary",
        "subtitle": "Unit 3 • Lecture 35 • Section 3.1 Wrap-up",
        "detail": "Lecture 35: Vertex Form & Min/Max Analysis",
        "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
        "problem": "### Section 3.1 Master Checklist\n- Conquered the Vertex Formula: $x_v = -\\frac{b}{2a}$.\n- Mastered reading Vertex Form: $f(x) = a(x - h)^2 + k \\implies (h, k)$.\n- Identified Axis of Symmetry as the equation $x = h$.\n- Evaluated quadratic functions graphically and algebraically.",
        "solution": "$$\\mathbf{\\text{Section 3.1 Mastered! Next Up: Section 3.2 — The Square Root Property!}}$$",
        "pitfall": "**Next Challenge:** How do we find $x$-intercepts algebraically without a graph? In Section 3.2, we learn the Square Root Property!",
        "script": "[Prof. Park] Outstanding work mastering Section 3.1! You can now find the vertex of any quadratic function.\n\n[TA Sora] In Lecture 36, we begin solving for $x$-intercepts using the Square Root Property!"
    }
]

print("Unit 3 Lectures 31 to 35 generated successfully!")
