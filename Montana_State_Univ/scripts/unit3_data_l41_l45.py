# Unit 3 Lectures 41-45 slide data
# Workbook: M090 Full Student Workbook, Unit 3, pp. 79-91
# Section 3.5 (Quadratic Formula), 3.6 (Mixed Methods), 3.7 (Graphing)
# "One Problem = One Slide" rule | 100% English | All graphing problems use CoordinateGrid

import json

SLIDES_MONTANA_L41 = [
  {
    "num": 1,
    "type": "math_problem",
    "slideTypeLabel": "Lesson Introduction",
    "title": "Section 3.5: The Quadratic Formula",
    "subtitle": "Unit 3 \u2022 Lecture 41 \u2022 Section 3.5 (Workbook p. 79)",
    "detail": "Lecture 41: Finding Intercepts via the Quadratic Formula",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**The Quadratic Formula** can solve ANY quadratic equation once it is set equal to zero in general form.\n\n$$\\text{If } ax^2 + bx + c = 0 \\text{ then:}$$\n\n$$\\boxed{x = \\dfrac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}}$$\n\n**Why do we need this?**\n- Square Root Property works when there is no middle \\(bx\\) term.\n- Factoring works when nice integer roots exist.\n- The **Quadratic Formula** always works, no matter what!",
    "solution": "**Formula Components:**\n- \\(a\\) = leading coefficient\n- \\(b\\) = middle coefficient\n- \\(c\\) = constant term\n- \\(b^2 - 4ac\\) = **discriminant** (determines the number of solutions)\n\n**Three possible outcomes:**\n$$b^2 - 4ac > 0 \\Rightarrow \\text{2 real x-intercepts}$$\n$$b^2 - 4ac = 0 \\Rightarrow \\text{1 real x-intercept (vertex on x-axis)}$$\n$$b^2 - 4ac < 0 \\Rightarrow \\text{No real x-intercepts (parabola doesn\u2019t cross x-axis)}$$",
    "pitfall": "**Sora\u2019s Warning:** The \\(\\pm\\) sign means you compute TWO values: one with \\(+\\) and one with \\(-\\). Never skip one!",
    "script": "[Prof. Park] Welcome to Lecture 41! We\u2019ve mastered the Square Root Property and Factoring. Today we unlock the most powerful tool of all: the Quadratic Formula.\n\n[TA Sora] I remember when I first saw this formula I thought it looked scary. But honestly, it\u2019s just a recipe\u2014plug in a, b, and c, and out come the x-intercepts!\n\n[Prof. Park] Exactly. And unlike factoring, this formula ALWAYS works. Let\u2019s see it in action."
  },
  {
    "num": 2,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 1A",
    "title": "Quadratic Formula: \\( g(x) = x^2 - 17x + 72 \\)",
    "subtitle": "Unit 3 \u2022 Lecture 41 \u2022 Section 3.5 Example 1A (Workbook p. 79)",
    "detail": "Find the x-intercepts, y-intercept, and vertex.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find the intercepts and vertex for:** \\(g(x) = x^2 - 17x + 72\\)\n\n**Step 1 \u2014 Identify x-intercepts:** Set \\(g(x) = 0\\)\n$$x^2 - 17x + 72 = 0$$\n\nIdentify: \\(a = 1,\\; b = -17,\\; c = 72\\)\n\nApply the Quadratic Formula:\n$$x = \\dfrac{-(-17) \\pm \\sqrt{(-17)^2 - 4(1)(72)}}{2(1)}$$",
    "solution": "$$x = \\dfrac{17 \\pm \\sqrt{289 - 288}}{2} = \\dfrac{17 \\pm \\sqrt{1}}{2} = \\dfrac{17 \\pm 1}{2}$$\n\n$$x = \\dfrac{17+1}{2} = \\dfrac{18}{2} = \\mathbf{9} \\qquad x = \\dfrac{17-1}{2} = \\dfrac{16}{2} = \\mathbf{8}$$\n\n**x-intercepts:** \\((9,0)\\) and \\((8,0)\\)\n\n**y-intercept:** \\(g(0) = 0 - 0 + 72 = \\mathbf{72}\\) \u2192 \\((0, 72)\\)\n\n**Vertex:** \\(x = \\dfrac{-(-17)}{2(1)} = \\dfrac{17}{2} = 8.5\\)\n$$g(8.5) = (8.5)^2 - 17(8.5) + 72 = 72.25 - 144.5 + 72 = -0.25$$\n\n**Vertex:** \\((8.5,\\; -0.25)\\)",
    "pitfall": "**Sora\u2019s Note:** \\(\\sqrt{1} = 1\\), not 0! The discriminant being 1 (very close to 0) means the two roots are almost equal but still distinct: \\(x = 8\\) and \\(x = 9\\).",
    "script": "[Prof. Park] Example 1A has a=1, b=-17, c=72. Let\u2019s plug in carefully.\n\n[TA Sora] The discriminant is 289 minus 288 which equals 1. So we get two roots very close together, x=8 and x=9!\n\n[Prof. Park] Perfect. The parabola barely dips below the x-axis between x=8 and x=9 before going back up.",
    "coordinate": {
      "xMin": -1, "xMax": 15, "yMin": -5, "yMax": 80,
      "xTicks": 2, "yTicks": 10,
      "curves": [{"a": 1, "b": -17, "c": 72, "color": "#00d4ff", "strokeWidth": 3}],
      "points": [
        {"x": 8, "y": 0, "color": "#ff6b6b", "label": "(8,0)"},
        {"x": 9, "y": 0, "color": "#ff6b6b", "label": "(9,0)"},
        {"x": 8.5, "y": -0.25, "color": "#ffd700", "label": "V(8.5,-0.25)"}
      ],
      "axisOfSymmetry": 8.5
    }
  },
  {
    "num": 3,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 1B",
    "title": "Quadratic Formula: \\( h(x) = x^2 - 5x - 7 \\)",
    "subtitle": "Unit 3 \u2022 Lecture 41 \u2022 Section 3.5 Example 1B (Workbook p. 80)",
    "detail": "Find the x-intercepts, y-intercept, and vertex.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find the intercepts and vertex for:** \\(h(x) = x^2 - 5x - 7\\)\n\nSet \\(h(x) = 0\\): \\(x^2 - 5x - 7 = 0\\)\n\nIdentify: \\(a = 1,\\; b = -5,\\; c = -7\\)\n\n$$x = \\dfrac{-(-5) \\pm \\sqrt{(-5)^2 - 4(1)(-7)}}{2(1)} = \\dfrac{5 \\pm \\sqrt{25 + 28}}{2}$$",
    "solution": "$$x = \\dfrac{5 \\pm \\sqrt{53}}{2}$$\n\n$$\\sqrt{53} \\approx 7.28$$\n\n$$x = \\dfrac{5 + 7.28}{2} = \\dfrac{12.28}{2} \\approx \\mathbf{6.14} \\qquad x = \\dfrac{5 - 7.28}{2} = \\dfrac{-2.28}{2} \\approx \\mathbf{-1.14}$$\n\n**x-intercepts:** \\(\\approx (6.14,\\,0)\\) and \\(\\approx (-1.14,\\,0)\\)\n\n**y-intercept:** \\(h(0) = -7\\) \u2192 \\((0,\\,-7)\\)\n\n**Vertex:** \\(x = \\dfrac{5}{2} = 2.5\\),\\quad \\(h(2.5) = 6.25 - 12.5 - 7 = -13.25\\)\n\n**Vertex:** \\((2.5,\\,-13.25)\\)",
    "pitfall": "**Sora\u2019s Note:** When \\(c\\) is negative, \\(-4ac\\) becomes positive (negative times negative). Always double-check: \\(-4(1)(-7) = +28\\).",
    "script": "[Prof. Park] In Example 1B, c is -7 which makes the discriminant larger: 25+28=53. A positive discriminant means two real roots.\n\n[TA Sora] And since 53 is not a perfect square, our answers are irrational. We leave them as fractions with the radical or use a decimal approximation.\n\n[Prof. Park] Great observation, Sora. Both forms are correct, but irrational exact form is preferred in math.",
    "coordinate": {
      "xMin": -3, "xMax": 8, "yMin": -16, "yMax": 10,
      "xTicks": 1, "yTicks": 2,
      "curves": [{"a": 1, "b": -5, "c": -7, "color": "#00d4ff", "strokeWidth": 3}],
      "points": [
        {"x": 6.14, "y": 0, "color": "#ff6b6b", "label": "(6.14,0)"},
        {"x": -1.14, "y": 0, "color": "#ff6b6b", "label": "(-1.14,0)"},
        {"x": 2.5, "y": -13.25, "color": "#ffd700", "label": "V(2.5,-13.25)"}
      ],
      "axisOfSymmetry": 2.5
    }
  },
  {
    "num": 4,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 1C",
    "title": "Quadratic Formula: \\( h(x) = 13x - x^2 + 1 \\)",
    "subtitle": "Unit 3 \u2022 Lecture 41 \u2022 Section 3.5 Example 1C (Workbook p. 80)",
    "detail": "Rewrite in standard form first, then find intercepts and vertex.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find the intercepts and vertex for:** \\(h(x) = 13x - x^2 + 1\\)\n\n**Step 1 \u2014 Rewrite in standard form** \\(ax^2 + bx + c\\):\n$$h(x) = -x^2 + 13x + 1$$\n\nSet \\(h(x) = 0\\): \\(-x^2 + 13x + 1 = 0\\)\n\nIdentify: \\(a = -1,\\; b = 13,\\; c = 1\\)\n\n$$x = \\dfrac{-13 \\pm \\sqrt{13^2 - 4(-1)(1)}}{2(-1)} = \\dfrac{-13 \\pm \\sqrt{169+4}}{-2}$$",
    "solution": "$$x = \\dfrac{-13 \\pm \\sqrt{173}}{-2}$$\n\n$$\\sqrt{173} \\approx 13.15$$\n\n$$x = \\dfrac{-13 + 13.15}{-2} = \\dfrac{0.15}{-2} \\approx \\mathbf{-0.08}$$\n\n$$x = \\dfrac{-13 - 13.15}{-2} = \\dfrac{-26.15}{-2} \\approx \\mathbf{13.08}$$\n\n**x-intercepts:** \\(\\approx (-0.08,\\,0)\\) and \\(\\approx (13.08,\\,0)\\)\n\n**y-intercept:** \\(h(0) = 1\\) \u2192 \\((0,\\,1)\\)\n\n**Vertex:** \\(x = \\dfrac{-13}{2(-1)} = \\dfrac{13}{2} = 6.5\\)\n$$h(6.5) = -(6.5)^2 + 13(6.5) + 1 = -42.25 + 84.5 + 1 = 43.25$$\n\n**Vertex:** \\((6.5,\\;43.25)\\)",
    "pitfall": "**Sora\u2019s Warning:** Always rearrange to \\(ax^2 + bx + c = 0\\) FIRST! And with \\(a = -1\\), remember dividing by \\(-2\\) flips sign.",
    "script": "[Prof. Park] Example 1C is written out of standard order: 13x minus x squared plus 1. Our first job is to reorder it.\n\n[TA Sora] So we get -x\u00b2+13x+1. Now a=-1. That means the parabola opens downward, and the vertex is at the TOP!\n\n[Prof. Park] Exactly. The parabola opens down with a maximum at (6.5, 43.25).",
    "coordinate": {
      "xMin": -2, "xMax": 15, "yMin": -10, "yMax": 50,
      "xTicks": 2, "yTicks": 5,
      "curves": [{"a": -1, "b": 13, "c": 1, "color": "#ff9500", "strokeWidth": 3}],
      "points": [
        {"x": -0.08, "y": 0, "color": "#ff6b6b", "label": "(-0.08,0)"},
        {"x": 13.08, "y": 0, "color": "#ff6b6b", "label": "(13.08,0)"},
        {"x": 6.5, "y": 43.25, "color": "#ffd700", "label": "V(6.5,43.25)"}
      ],
      "axisOfSymmetry": 6.5
    }
  },
  {
    "num": 5,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 1D",
    "title": "Quadratic Formula: \\( f(x) = -x^2 - 5x + 7 \\)",
    "subtitle": "Unit 3 \u2022 Lecture 41 \u2022 Section 3.5 Example 1D (Workbook p. 81)",
    "detail": "Find the x-intercepts, y-intercept, and vertex.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find the intercepts and vertex for:** \\(f(x) = -x^2 - 5x + 7\\)\n\nSet \\(f(x) = 0\\): \\(-x^2 - 5x + 7 = 0\\)\n\nIdentify: \\(a = -1,\\; b = -5,\\; c = 7\\)\n\n$$x = \\dfrac{-(-5) \\pm \\sqrt{(-5)^2 - 4(-1)(7)}}{2(-1)} = \\dfrac{5 \\pm \\sqrt{25 + 28}}{-2}$$",
    "solution": "$$x = \\dfrac{5 \\pm \\sqrt{53}}{-2}$$\n\n$$\\sqrt{53} \\approx 7.28$$\n\n$$x = \\dfrac{5 + 7.28}{-2} = \\dfrac{12.28}{-2} \\approx \\mathbf{-6.14}$$\n\n$$x = \\dfrac{5 - 7.28}{-2} = \\dfrac{-2.28}{-2} \\approx \\mathbf{1.14}$$\n\n**x-intercepts:** \\(\\approx (-6.14,\\,0)\\) and \\(\\approx (1.14,\\,0)\\)\n\n**y-intercept:** \\(f(0) = 7\\) \u2192 \\((0,\\,7)\\)\n\n**Vertex:** \\(x = \\dfrac{-(-5)}{2(-1)} = \\dfrac{5}{-2} = -2.5\\)\n$$f(-2.5) = -(-2.5)^2 - 5(-2.5) + 7 = -6.25 + 12.5 + 7 = 13.25$$\n\n**Vertex:** \\((-2.5,\\;13.25)\\)",
    "pitfall": "**Sora\u2019s Note:** Two negatives in a=-1, b=-5. Be extra careful. \\(-b = -(-5) = +5\\) and \\(-4(-1)(7) = +28\\).",
    "script": "[Prof. Park] Example 1D has two negative signs for a and b. These are the problems where students make sign errors.\n\n[TA Sora] I always write out every step slowly when I see negative a. It\u2019s so easy to flip the wrong sign!\n\n[Prof. Park] Wise advice, Sora. Slow down, write every step, and check your signs twice.",
    "coordinate": {
      "xMin": -8, "xMax": 4, "yMin": -5, "yMax": 16,
      "xTicks": 1, "yTicks": 2,
      "curves": [{"a": -1, "b": -5, "c": 7, "color": "#ff9500", "strokeWidth": 3}],
      "points": [
        {"x": -6.14, "y": 0, "color": "#ff6b6b", "label": "(-6.14,0)"},
        {"x": 1.14, "y": 0, "color": "#ff6b6b", "label": "(1.14,0)"},
        {"x": -2.5, "y": 13.25, "color": "#ffd700", "label": "V(-2.5,13.25)"}
      ],
      "axisOfSymmetry": -2.5
    }
  },
  {
    "num": 6,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 1E",
    "title": "Quadratic Formula: \\( f(x) = -1 + 2x^2 - 3x \\)",
    "subtitle": "Unit 3 \u2022 Lecture 41 \u2022 Section 3.5 Example 1E (Workbook p. 81)",
    "detail": "Rewrite in standard form, then find intercepts and vertex.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find the intercepts and vertex for:** \\(f(x) = -1 + 2x^2 - 3x\\)\n\n**Step 1 \u2014 Rewrite in standard form:**\n$$f(x) = 2x^2 - 3x - 1$$\n\nSet \\(f(x) = 0\\): \\(2x^2 - 3x - 1 = 0\\)\n\nIdentify: \\(a = 2,\\; b = -3,\\; c = -1\\)\n\n$$x = \\dfrac{-(-3) \\pm \\sqrt{(-3)^2 - 4(2)(-1)}}{2(2)} = \\dfrac{3 \\pm \\sqrt{9 + 8}}{4}$$",
    "solution": "$$x = \\dfrac{3 \\pm \\sqrt{17}}{4}$$\n\n$$\\sqrt{17} \\approx 4.12$$\n\n$$x = \\dfrac{3 + 4.12}{4} = \\dfrac{7.12}{4} \\approx \\mathbf{1.78}$$\n\n$$x = \\dfrac{3 - 4.12}{4} = \\dfrac{-1.12}{4} \\approx \\mathbf{-0.28}$$\n\n**x-intercepts:** \\(\\approx (1.78,\\,0)\\) and \\(\\approx (-0.28,\\,0)\\)\n\n**y-intercept:** \\(f(0) = -1\\) \u2192 \\((0,\\,-1)\\)\n\n**Vertex:** \\(x = \\dfrac{-(-3)}{2(2)} = \\dfrac{3}{4} = 0.75\\)\n$$f(0.75) = 2(0.75)^2 - 3(0.75) - 1 = 1.125 - 2.25 - 1 = -2.125$$\n\n**Vertex:** \\((0.75,\\;-2.125)\\)",
    "pitfall": "**Sora\u2019s Tip:** \\(-4(2)(-1) = +8\\). Two negatives make a positive! The discriminant 9+8=17 is positive, so two real roots exist.",
    "script": "[Prof. Park] Our last example in Section 3.5 Part 1 has a=2. Notice how 2a=4 appears in the denominator.\n\n[TA Sora] And the terms are written out of order! I had to rearrange to 2x\u00b2-3x-1 to see a, b, and c clearly.\n\n[Prof. Park] Always rewrite first. Standard form ax\u00b2+bx+c is essential before applying any formula.",
    "coordinate": {
      "xMin": -2, "xMax": 3, "yMin": -4, "yMax": 6,
      "xTicks": 1, "yTicks": 1,
      "curves": [{"a": 2, "b": -3, "c": -1, "color": "#00d4ff", "strokeWidth": 3}],
      "points": [
        {"x": 1.78, "y": 0, "color": "#ff6b6b", "label": "(1.78,0)"},
        {"x": -0.28, "y": 0, "color": "#ff6b6b", "label": "(-0.28,0)"},
        {"x": 0.75, "y": -2.125, "color": "#ffd700", "label": "V(0.75,-2.13)"}
      ],
      "axisOfSymmetry": 0.75
    }
  },
  {
    "num": 7,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 2 \u2014 Function Evaluation",
    "title": "Function Evaluation: \\( f(x) = 3x^2 - 5x + 7 \\)",
    "subtitle": "Unit 3 \u2022 Lecture 41 \u2022 Section 3.5 Example 2 (Workbook p. 82)",
    "detail": "Evaluate f(4), f(p), f(x+3), and solve f(x) = 13.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Use \\(f(x) = 3x^2 - 5x + 7\\) to find:**\n\n**A.** \\(f(4)\\)\n\n**B.** \\(f(p)\\)\n\n**C.** \\(f(x+3)\\)\n\n**D.** Solve \\(f(x) = 13\\) for \\(x\\)",
    "solution": "**A.** \\(f(4) = 3(4)^2 - 5(4) + 7 = 48 - 20 + 7 = \\mathbf{35}\\)\n\n**B.** \\(f(p) = 3p^2 - 5p + 7\\)\n\n**C.** \\(f(x+3) = 3(x+3)^2 - 5(x+3) + 7\\)\n$$= 3(x^2+6x+9) - 5x - 15 + 7 = 3x^2+18x+27-5x-15+7$$\n$$= \\mathbf{3x^2 + 13x + 19}$$\n\n**D.** Set \\(f(x) = 13\\):\n$$3x^2 - 5x + 7 = 13 \\Rightarrow 3x^2 - 5x - 6 = 0$$\n$$x = \\dfrac{5 \\pm \\sqrt{25+72}}{6} = \\dfrac{5 \\pm \\sqrt{97}}{6} \\approx \\dfrac{5 \\pm 9.85}{6}$$\n$$x \\approx \\mathbf{2.47} \\quad \\text{or} \\quad x \\approx \\mathbf{-0.81}$$",
    "pitfall": "**Sora\u2019s Note for Part C:** Use FOIL or the perfect-square pattern for \\((x+3)^2 = x^2 + 6x + 9\\). Then distribute the 3!",
    "script": "[Prof. Park] Section 3.5 Example 2 tests ALL our function notation skills together. Evaluation, expression substitution, and solving.\n\n[TA Sora] Part D is so interesting! We set f(x) equal to 13, move 13 to the left, and then we HAVE to use the Quadratic Formula because the result doesn\u2019t factor nicely.\n\n[Prof. Park] Perfect connection, Sora. The Quadratic Formula saves us when factoring fails."
  },
  {
    "num": 8,
    "type": "math_problem",
    "slideTypeLabel": "Lecture 41 Review",
    "title": "Quadratic Formula \u2014 Key Takeaways",
    "subtitle": "Unit 3 \u2022 Lecture 41 Summary",
    "detail": "Review of the Quadratic Formula and its applications.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Quadratic Formula Summary:**\n\n| Step | Action |\n|------|--------|\n| 1 | Write in standard form: \\(ax^2+bx+c=0\\) |\n| 2 | Identify \\(a\\), \\(b\\), \\(c\\) |\n| 3 | Compute discriminant: \\(b^2 - 4ac\\) |\n| 4 | Apply: \\(x = \\dfrac{-b \\pm \\sqrt{b^2-4ac}}{2a}\\) |\n| 5 | Simplify both \\(+\\) and \\(-\\) solutions |",
    "solution": "**Examples covered today:**\n- \\(g(x) = x^2-17x+72\\) \u2192 \\(x = 8, 9\\)\n- \\(h(x) = x^2-5x-7\\) \u2192 \\(x \\approx 6.14,\\,-1.14\\)\n- \\(h(x) = 13x-x^2+1\\) \u2192 \\(x \\approx -0.08,\\,13.08\\)\n- \\(f(x) = -x^2-5x+7\\) \u2192 \\(x \\approx -6.14,\\,1.14\\)\n- \\(f(x) = -1+2x^2-3x\\) \u2192 \\(x \\approx 1.78,\\,-0.28\\)\n\n**Next Lecture:** The Discriminant \u2014 predicting solutions before solving!",
    "pitfall": "**Sora\u2019s Final Reminder:** Always check that your equation equals ZERO before applying the Quadratic Formula. If it equals a non-zero constant, move it first!",
    "script": "[TA Sora] Five examples in one lecture! You\u2019re all Quadratic Formula champions now!\n\n[Prof. Park] In Lecture 42 we\u2019ll study the discriminant, which lets us predict how many solutions exist WITHOUT fully solving the equation. See you then!"
  }
]

SLIDES_MONTANA_L42 = [
  {
    "num": 1,
    "type": "math_problem",
    "slideTypeLabel": "Lesson Introduction",
    "title": "Section 3.5 Part 2: The Discriminant",
    "subtitle": "Unit 3 \u2022 Lecture 42 \u2022 Section 3.5 (Workbook p. 79\u201382)",
    "detail": "Lecture 42: Using the Discriminant to Classify Solutions",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**The Discriminant** is the expression inside the square root of the Quadratic Formula:\n\n$$\\Delta = b^2 - 4ac$$\n\n**It tells us the number of x-intercepts WITHOUT solving:**\n\n| Discriminant | Solutions | Graph |\n|---|---|---|\n| \\(\\Delta > 0\\) | 2 real x-intercepts | Crosses x-axis twice |\n| \\(\\Delta = 0\\) | 1 real x-intercept | Touches x-axis at vertex |\n| \\(\\Delta < 0\\) | No real x-intercepts | Parabola floats above or below x-axis |",
    "solution": "**Why does this matter?**\n- Saves time! If \\(\\Delta < 0\\), you know immediately there are no real x-intercepts.\n- Tells you the shape of your parabola\u2019s relationship with the x-axis.\n- Discriminant zero means vertex is ON the x-axis (special case!).",
    "pitfall": "**Sora\u2019s Warning:** The discriminant is \\(b^2 - 4ac\\), NOT \\(\\sqrt{b^2-4ac}\\). Compute it BEFORE taking the square root.",
    "script": "[Prof. Park] Welcome to Lecture 42! Today we study the discriminant, the gatekeeper of quadratic solutions.\n\n[TA Sora] I love this concept because just computing b\u00b2-4ac tells you everything about how many answers you\u2019ll get. It\u2019s like a spoiler for the answer!\n\n[Prof. Park] Exactly, Sora. Three outcomes: cross twice, touch once, or miss entirely."
  },
  {
    "num": 2,
    "type": "math_problem",
    "slideTypeLabel": "Discriminant \u2014 Two Solutions",
    "title": "Discriminant \\(\\Delta > 0\\): Two Real x-Intercepts",
    "subtitle": "Unit 3 \u2022 Lecture 42 \u2022 Discriminant Case 1",
    "detail": "When the discriminant is positive, the parabola crosses the x-axis twice.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find and classify solutions for:** \\(f(x) = x^2 - 5x + 4\\)\n\n**Step 1 \u2014 Compute discriminant:** \\(a=1, b=-5, c=4\\)\n$$\\Delta = (-5)^2 - 4(1)(4) = 25 - 16 = 9 > 0$$\n\n**Conclusion:** The parabola crosses the x-axis at **2 distinct points**.",
    "solution": "**Apply the formula:**\n$$x = \\dfrac{5 \\pm \\sqrt{9}}{2} = \\dfrac{5 \\pm 3}{2}$$\n\n$$x = \\dfrac{5+3}{2} = 4 \\qquad x = \\dfrac{5-3}{2} = 1$$\n\n**x-intercepts:** \\((1,\\,0)\\) and \\((4,\\,0)\\)\n\n**Vertex:** \\(x = 2.5\\), \\(f(2.5) = 6.25-12.5+4 = -2.25\\)\n\n**Vertex:** \\((2.5,\\,-2.25)\\)",
    "pitfall": "**Sora\u2019s Note:** \\(\\sqrt{9} = 3\\) (a perfect square!). When \\(\\Delta\\) is a perfect square, solutions are rational numbers.",
    "script": "[Prof. Park] When delta equals 9, a perfect square, we get the cleanest possible answer: two rational roots.\n\n[TA Sora] x=1 and x=4. The parabola clearly crosses the x-axis at both points. I can see it on the graph!",
    "coordinate": {
      "xMin": -1, "xMax": 6, "yMin": -4, "yMax": 8,
      "xTicks": 1, "yTicks": 1,
      "curves": [{"a": 1, "b": -5, "c": 4, "color": "#00d4ff", "strokeWidth": 3}],
      "points": [
        {"x": 1, "y": 0, "color": "#ff6b6b", "label": "(1,0)"},
        {"x": 4, "y": 0, "color": "#ff6b6b", "label": "(4,0)"},
        {"x": 2.5, "y": -2.25, "color": "#ffd700", "label": "V(2.5,-2.25)"}
      ],
      "axisOfSymmetry": 2.5
    }
  },
  {
    "num": 3,
    "type": "math_problem",
    "slideTypeLabel": "Discriminant \u2014 One Solution",
    "title": "Discriminant \\(\\Delta = 0\\): Exactly One Real x-Intercept",
    "subtitle": "Unit 3 \u2022 Lecture 42 \u2022 Discriminant Case 2",
    "detail": "When the discriminant is zero, the vertex sits exactly on the x-axis.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find and classify solutions for:** \\(f(x) = x^2 - 6x + 9\\)\n\n**Step 1 \u2014 Compute discriminant:** \\(a=1, b=-6, c=9\\)\n$$\\Delta = (-6)^2 - 4(1)(9) = 36 - 36 = 0$$\n\n**Conclusion:** The parabola **touches** the x-axis at exactly **one point** (the vertex).",
    "solution": "**Apply the formula:**\n$$x = \\dfrac{6 \\pm \\sqrt{0}}{2} = \\dfrac{6 \\pm 0}{2} = \\dfrac{6}{2} = 3$$\n\n**One x-intercept:** \\((3,\\,0)\\)\n\n**Vertex = x-intercept:** \\((3,\\,0)\\)\n\n**Note:** \\(f(x) = x^2-6x+9 = (x-3)^2\\). The vertex form confirms vertex is at \\((3,0)\\), sitting ON the x-axis.",
    "pitfall": "**Sora\u2019s Insight:** \\(\\Delta = 0\\) means it\u2019s a perfect square trinomial! \\(x^2-6x+9 = (x-3)^2\\). So the answer is a double root: \\(x=3\\) repeated twice.",
    "script": "[TA Sora] When the discriminant is exactly zero, there\u2019s only one solution. The parabola just barely touches the x-axis at its lowest point.\n\n[Prof. Park] This is called a double root or a repeated root. x=3 is the answer, and visually the parabola is tangent to the x-axis.",
    "coordinate": {
      "xMin": 0, "xMax": 6, "yMin": -1, "yMax": 10,
      "xTicks": 1, "yTicks": 1,
      "curves": [{"a": 1, "b": -6, "c": 9, "color": "#00ff88", "strokeWidth": 3}],
      "points": [
        {"x": 3, "y": 0, "color": "#ffd700", "label": "V(3,0)"}
      ],
      "axisOfSymmetry": 3
    }
  },
  {
    "num": 4,
    "type": "math_problem",
    "slideTypeLabel": "Discriminant \u2014 No Real Solutions",
    "title": "Discriminant \\(\\Delta < 0\\): No Real x-Intercepts",
    "subtitle": "Unit 3 \u2022 Lecture 42 \u2022 Discriminant Case 3",
    "detail": "When the discriminant is negative, the parabola floats above or below the x-axis.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find and classify solutions for:** \\(f(x) = x^2 + 2x + 5\\)\n\n**Step 1 \u2014 Compute discriminant:** \\(a=1, b=2, c=5\\)\n$$\\Delta = (2)^2 - 4(1)(5) = 4 - 20 = -16 < 0$$\n\n**Conclusion:** There are **no real x-intercepts**. The parabola floats entirely above the x-axis.",
    "solution": "**Why no real solutions?**\n$$x = \\dfrac{-2 \\pm \\sqrt{-16}}{2}$$\n\n$$\\sqrt{-16} \\text{ is not a real number!}$$\n\nWe cannot take the square root of a negative number in the real number system.\n\n**Vertex:** \\(x = \\dfrac{-2}{2} = -1\\), \\(f(-1) = 1-2+5 = 4\\)\n\n**Vertex:** \\((-1,\\,4)\\) \u2014 The parabola opens upward with minimum at \\(y=4 > 0\\). Never crosses the x-axis!",
    "pitfall": "**Sora\u2019s Note:** You will encounter imaginary numbers (\\(\\sqrt{-16} = 4i\\)) in future math courses. For M090, we just state: NO REAL SOLUTIONS.",
    "script": "[Prof. Park] When the discriminant is negative, the square root doesn\u2019t exist in real numbers. The parabola simply floats above the x-axis entirely.\n\n[TA Sora] I can see on the graph that the vertex is at y=4, which is above the x-axis. So the parabola never crosses it. That makes perfect sense!",
    "coordinate": {
      "xMin": -4, "xMax": 2, "yMin": -1, "yMax": 12,
      "xTicks": 1, "yTicks": 1,
      "curves": [{"a": 1, "b": 2, "c": 5, "color": "#ff9500", "strokeWidth": 3}],
      "points": [
        {"x": -1, "y": 4, "color": "#ffd700", "label": "V(-1,4)"}
      ],
      "axisOfSymmetry": -1
    }
  },
  {
    "num": 5,
    "type": "math_problem",
    "slideTypeLabel": "Discriminant Practice \u2014 Classify Only",
    "title": "Classify Without Solving: \\(h(x) = -2x^2 + 3x - 5\\)",
    "subtitle": "Unit 3 \u2022 Lecture 42 \u2022 Discriminant Application",
    "detail": "Use the discriminant to classify the number of x-intercepts.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Without fully solving, determine the number of x-intercepts for:**\n$$h(x) = -2x^2 + 3x - 5$$\n\nIdentify: \\(a = -2,\\; b = 3,\\; c = -5\\)\n\nCompute the discriminant:\n$$\\Delta = b^2 - 4ac = (3)^2 - 4(-2)(-5)$$",
    "solution": "$$\\Delta = 9 - 40 = -31 < 0$$\n\n**Conclusion: No real x-intercepts.**\n\nThe parabola opens **downward** (a=-2<0) and sits entirely **below** the x-axis.\n\n**Vertex:** \\(x = \\dfrac{-3}{2(-2)} = \\dfrac{3}{4} = 0.75\\)\n$$h(0.75) = -2(0.5625)+3(0.75)-5 = -1.125+2.25-5 = -3.875$$\n\n**Vertex:** \\((0.75,\\,-3.875)\\) \u2014 Maximum is negative, parabola entirely below x-axis.",
    "pitfall": "**Sora\u2019s Check:** \\(-4(-2)(-5) = -4 \\times 10 = -40\\). Two negatives in a=-2 and c=-5 give a negative product! Don\u2019t accidentally make it positive.",
    "script": "[TA Sora] Wait, a is negative AND c is negative. So -4ac = -4(-2)(-5). Let me compute: negative four times negative two is positive eight, times negative five is negative forty!\n\n[Prof. Park] Precisely! So delta = 9-40 = -31. Negative discriminant. No real x-intercepts confirmed.",
    "coordinate": {
      "xMin": -1, "xMax": 3, "yMin": -8, "yMax": 2,
      "xTicks": 1, "yTicks": 1,
      "curves": [{"a": -2, "b": 3, "c": -5, "color": "#ff9500", "strokeWidth": 3}],
      "points": [
        {"x": 0.75, "y": -3.875, "color": "#ffd700", "label": "V(0.75,-3.88)"}
      ],
      "axisOfSymmetry": 0.75
    }
  },
  {
    "num": 6,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 2A & 2B",
    "title": "Function Evaluation: \\( f(x) = 3x^2 - 5x + 7 \\) (Parts A & B)",
    "subtitle": "Unit 3 \u2022 Lecture 42 \u2022 Section 3.5 Example 2 (Workbook p. 82)",
    "detail": "Evaluate f(4) and f(p).",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Use \\(f(x) = 3x^2 - 5x + 7\\) to find:**\n\n**A.** \\(f(4)\\)\n\n**B.** \\(f(p)\\)\n\n**Recall:** To evaluate \\(f(\\text{input})\\), replace every \\(x\\) in the formula with the input.",
    "solution": "**A.** \\(f(4)\\): Replace \\(x\\) with \\(4\\)\n$$f(4) = 3(4)^2 - 5(4) + 7 = 3(16) - 20 + 7 = 48 - 20 + 7 = \\mathbf{35}$$\n\n**B.** \\(f(p)\\): Replace \\(x\\) with \\(p\\)\n$$f(p) = 3p^2 - 5p + 7$$\n\nThis stays as an **algebraic expression** \u2014 we substitute the variable \\(p\\) directly.",
    "pitfall": "**Sora\u2019s Note on Part B:** When the input is a variable (like \\(p\\)), the output is a new expression, not a number. Just replace every \\(x\\) with \\(p\\)!",
    "script": "[Prof. Park] Example 2A gives a numeric answer. Example 2B gives an algebraic expression. Both are valid evaluations of function notation.\n\n[TA Sora] So f of 4 equals 35 (a number), but f of p equals 3p\u00b2-5p+7 (still an expression). Got it!"
  },
  {
    "num": 7,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 2C & 2D",
    "title": "Function Composition & Solving: \\( f(x) = 3x^2 - 5x + 7 \\) (Parts C & D)",
    "subtitle": "Unit 3 \u2022 Lecture 42 \u2022 Section 3.5 Example 2 (Workbook p. 82)",
    "detail": "Find f(x+3) and solve f(x)=13.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Use \\(f(x) = 3x^2 - 5x + 7\\) to find:**\n\n**C.** \\(f(x+3)\\)\n\n**D.** Solve \\(f(x) = 13\\) for \\(x\\)",
    "solution": "**C.** \\(f(x+3)\\): Replace every \\(x\\) with \\((x+3)\\)\n$$f(x+3) = 3(x+3)^2 - 5(x+3) + 7$$\n$$= 3(x^2+6x+9) - 5x - 15 + 7$$\n$$= 3x^2 + 18x + 27 - 5x - 8$$\n$$= \\mathbf{3x^2 + 13x + 19}$$\n\n**D.** Set \\(f(x) = 13\\):\n$$3x^2 - 5x + 7 = 13$$\n$$3x^2 - 5x - 6 = 0$$\n$$x = \\dfrac{5 \\pm \\sqrt{25+72}}{6} = \\dfrac{5 \\pm \\sqrt{97}}{6} \\approx \\dfrac{5 \\pm 9.85}{6}$$\n$$x \\approx \\mathbf{2.47} \\quad \\text{or} \\quad x \\approx \\mathbf{-0.81}$$",
    "pitfall": "**Sora\u2019s FOIL Reminder for Part C:** \\((x+3)^2 = x^2+6x+9\\), NOT \\(x^2+9\\)! Always expand fully.",
    "script": "[TA Sora] Part C is so interesting! We\u2019re substituting an expression x+3 instead of a number. We just replace every x with the whole thing in parentheses.\n\n[Prof. Park] And Part D requires moving 13 to the left to get standard form equal to zero, then the Quadratic Formula gives two solutions."
  },
  {
    "num": 8,
    "type": "math_problem",
    "slideTypeLabel": "Lecture 42 Review",
    "title": "Discriminant Summary \u2014 Three Cases Visualized",
    "subtitle": "Unit 3 \u2022 Lecture 42 Summary",
    "detail": "Visual summary of all three discriminant cases.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Discriminant Decision Chart:**\n\n| Compute \\(\\Delta = b^2-4ac\\) | Result | Parabola |\n|---|---|---|\n| \\(\\Delta > 0\\) | **2** real solutions | Crosses x-axis at 2 points |\n| \\(\\Delta = 0\\) | **1** real solution | Vertex touches x-axis |\n| \\(\\Delta < 0\\) | **0** real solutions | No x-intercepts exist |\n\n**Remember:** This works for ANY quadratic, regardless of the value of \\(a\\)!",
    "solution": "**Lecture 42 examples covered:**\n- \\(f(x)=x^2-5x+4\\): \\(\\Delta=9>0\\) \u2192 \\(x=1,4\\)\n- \\(f(x)=x^2-6x+9\\): \\(\\Delta=0\\) \u2192 \\(x=3\\) (double root)\n- \\(f(x)=x^2+2x+5\\): \\(\\Delta=-16<0\\) \u2192 No real solutions\n- \\(h(x)=-2x^2+3x-5\\): \\(\\Delta=-31<0\\) \u2192 No real solutions\n\n**Next Lecture:** Master decision strategy \u2014 which method to use and when!",
    "pitfall": "**Sora\u2019s Final Tip:** Before solving ANY quadratic, compute the discriminant first. It tells you what to expect and saves time if there are no real solutions.",
    "script": "[TA Sora] Three cases, perfectly memorized!\n\n[Prof. Park] In Lecture 43, we bring everything together: Square Root Property, Factoring, Completing the Square, and the Quadratic Formula. You\u2019ll learn exactly when to use each method."
  }
]

SLIDES_MONTANA_L43 = [
  {
    "num": 1,
    "type": "math_problem",
    "slideTypeLabel": "Lesson Introduction",
    "title": "Section 3.6: Mixed Methods \u2014 Intercepts and Vertex",
    "subtitle": "Unit 3 \u2022 Lecture 43 \u2022 Section 3.6 (Workbook p. 83)",
    "detail": "Lecture 43: Finding Intercepts Using the Best Method",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Section 3.6 Strategy: Choose the Best Method**\n\n| Equation Form | Best Method |\n|---|---|\n| \\(ax^2 + c = 0\\) (no \\(bx\\)) | **Square Root Property** |\n| \\(ax^2 + bx = 0\\) (no constant) | **Factor out GCF** |\n| \\(ax^2 + bx + c = 0\\) (nice factors) | **Factor (FOIL-reverse)** |\n| Any quadratic | **Quadratic Formula** |\n\nIn Section 3.6, we practice ALL methods and find x-intercepts, y-intercepts, AND vertex for each function.",
    "solution": "**Today\u2019s four functions:**\n- \\(g(x) = x^2+6x\\)\n- \\(h(x) = -2x^2+5x+6\\)\n- \\(f(x) = 4x^2-28\\)\n- \\(f(x) = x^2-15x+50\\)\n\nFor each: find x-intercepts, y-intercept, and vertex. Then use them to graph!",
    "pitfall": "**Sora\u2019s Tip:** Always find the y-intercept by substituting \\(x=0\\). Always find the vertex using \\(x = \\dfrac{-b}{2a}\\), then plug back in.",
    "script": "[Prof. Park] Welcome to Lecture 43, Section 3.6! This is our master practice section. We apply every method we\u2019ve learned to find all key features of four different quadratic functions.\n\n[TA Sora] This is like the final boss before graphing! Let\u2019s conquer all four."
  },
  {
    "num": 2,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Section 3.6, Example 1A",
    "title": "x-Intercepts: \\( g(x) = x^2 + 6x \\) (Factor GCF)",
    "subtitle": "Unit 3 \u2022 Lecture 43 \u2022 Section 3.6 Example 1A (Workbook p. 83)",
    "detail": "Find the x-intercepts by factoring out the GCF.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find the x-intercepts of \\(g(x) = x^2 + 6x\\)**\n\nSet \\(g(x) = 0\\):\n$$x^2 + 6x = 0$$\n\n**Method: Factor out the GCF**\n- Both terms share a factor of \\(x\\)\n$$x(x + 6) = 0$$\n\n**Zero-Product Property:**\n$$x = 0 \\quad \\text{or} \\quad x+6 = 0$$",
    "solution": "$$x = 0 \\qquad \\text{or} \\qquad x = -6$$\n\n**x-intercepts:** \\((0,\\,0)\\) and \\((-6,\\,0)\\)\n\n**Note:** The x-intercept \\((0,0)\\) is also the y-intercept!\n\n**y-intercept:** \\(g(0) = 0 + 0 = 0\\) \u2192 \\((0,\\,0)\\)\n\n**Vertex:** \\(x = \\dfrac{-6}{2(1)} = -3\\),\\quad \\(g(-3) = 9-18 = -9\\)\n\n**Vertex:** \\((-3,\\,-9)\\)",
    "pitfall": "**Sora\u2019s Note:** Never divide both sides by \\(x\\)! That would make you lose the solution \\(x=0\\). Always FACTOR instead.",
    "script": "[TA Sora] g(x) = x\u00b2+6x has no constant term, so we factor out x. This gives x(x+6)=0.\n\n[Prof. Park] And by the Zero-Product Property, either x=0 or x+6=0. Two x-intercepts: the origin and (-6,0).",
    "coordinate": {
      "xMin": -8, "xMax": 3, "yMin": -12, "yMax": 8,
      "xTicks": 1, "yTicks": 2,
      "curves": [{"a": 1, "b": 6, "c": 0, "color": "#00d4ff", "strokeWidth": 3}],
      "points": [
        {"x": 0, "y": 0, "color": "#ff6b6b", "label": "(0,0)"},
        {"x": -6, "y": 0, "color": "#ff6b6b", "label": "(-6,0)"},
        {"x": -3, "y": -9, "color": "#ffd700", "label": "V(-3,-9)"}
      ],
      "axisOfSymmetry": -3
    }
  },
  {
    "num": 3,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Section 3.6, Example 1B",
    "title": "x-Intercepts: \\( h(x) = -2x^2 + 5x + 6 \\) (Quadratic Formula)",
    "subtitle": "Unit 3 \u2022 Lecture 43 \u2022 Section 3.6 Example 1B (Workbook p. 83)",
    "detail": "Find the x-intercepts using the Quadratic Formula.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find the x-intercepts of \\(h(x) = -2x^2 + 5x + 6\\)**\n\nSet \\(h(x) = 0\\): \\(-2x^2 + 5x + 6 = 0\\)\n\nIdentify: \\(a = -2,\\; b = 5,\\; c = 6\\)\n\n$$x = \\dfrac{-5 \\pm \\sqrt{5^2 - 4(-2)(6)}}{2(-2)} = \\dfrac{-5 \\pm \\sqrt{25+48}}{-4}$$",
    "solution": "$$x = \\dfrac{-5 \\pm \\sqrt{73}}{-4}$$\n\n$$\\sqrt{73} \\approx 8.54$$\n\n$$x = \\dfrac{-5+8.54}{-4} = \\dfrac{3.54}{-4} \\approx \\mathbf{-0.89}$$\n\n$$x = \\dfrac{-5-8.54}{-4} = \\dfrac{-13.54}{-4} \\approx \\mathbf{3.39}$$\n\n**x-intercepts:** \\(\\approx (-0.89,\\,0)\\) and \\(\\approx (3.39,\\,0)\\)\n\n**y-intercept:** \\(h(0) = 6\\) \u2192 \\((0,\\,6)\\)\n\n**Vertex:** \\(x = \\dfrac{-5}{2(-2)} = \\dfrac{5}{4} = 1.25\\)\n$$h(1.25) = -2(1.5625)+5(1.25)+6 = -3.125+6.25+6 = 9.125$$\n\n**Vertex:** \\((1.25,\\;9.125)\\)",
    "pitfall": "**Sora\u2019s Warning:** With \\(a=-2\\), dividing by \\(-4\\) FLIPS the sign direction. \\(\\dfrac{\\text{positive}}{-4}\\) gives a negative result!",
    "script": "[Prof. Park] With a=-2, factoring is difficult. The Quadratic Formula is our best friend here.\n\n[TA Sora] And careful: we\u2019re dividing by -4, which is negative. So positive numerator gives negative answer, and negative numerator gives positive answer. Interesting!",
    "coordinate": {
      "xMin": -2, "xMax": 5, "yMin": -5, "yMax": 12,
      "xTicks": 1, "yTicks": 2,
      "curves": [{"a": -2, "b": 5, "c": 6, "color": "#ff9500", "strokeWidth": 3}],
      "points": [
        {"x": -0.89, "y": 0, "color": "#ff6b6b", "label": "(-0.89,0)"},
        {"x": 3.39, "y": 0, "color": "#ff6b6b", "label": "(3.39,0)"},
        {"x": 1.25, "y": 9.125, "color": "#ffd700", "label": "V(1.25,9.13)"}
      ],
      "axisOfSymmetry": 1.25
    }
  },
  {
    "num": 4,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Section 3.6, Example 1C",
    "title": "x-Intercepts: \\( f(x) = 4x^2 - 28 \\) (Square Root Property)",
    "subtitle": "Unit 3 \u2022 Lecture 43 \u2022 Section 3.6 Example 1C (Workbook p. 83)",
    "detail": "Find the x-intercepts using the Square Root Property.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find the x-intercepts of \\(f(x) = 4x^2 - 28\\)**\n\nSet \\(f(x) = 0\\):\n$$4x^2 - 28 = 0$$\n\n**Method: Square Root Property** (no \\(bx\\) term!)\n\n**Step 1:** Isolate \\(x^2\\):\n$$4x^2 = 28 \\Rightarrow x^2 = 7$$\n\n**Step 2:** Take square root of both sides:",
    "solution": "$$x = \\pm\\sqrt{7} \\approx \\pm 2.646$$\n\n**x-intercepts:** \\((-\\sqrt{7},\\,0)\\approx(-2.65,\\,0)\\) and \\((\\sqrt{7},\\,0)\\approx(2.65,\\,0)\\)\n\n**y-intercept:** \\(f(0) = 0-28 = -28\\) \u2192 \\((0,\\,-28)\\)\n\n**Vertex:** No \\(b\\) term, so \\(x = 0\\)\n$$f(0) = -28$$\n\n**Vertex:** \\((0,\\,-28)\\) \u2014 The vertex is the y-intercept here!",
    "pitfall": "**Sora\u2019s Tip:** No middle term \\(bx\\)? Use the Square Root Property! It\u2019s much faster than the Quadratic Formula for this form.",
    "script": "[TA Sora] 4x\u00b2-28=0. There\u2019s no x term, just x squared! This is perfect for the Square Root Property.\n\n[Prof. Park] Isolate x\u00b2 to get x\u00b2=7, then x=\u00b1\u221a7. Quick and clean.",
    "coordinate": {
      "xMin": -4, "xMax": 4, "yMin": -32, "yMax": 10,
      "xTicks": 1, "yTicks": 5,
      "curves": [{"a": 4, "b": 0, "c": -28, "color": "#00d4ff", "strokeWidth": 3}],
      "points": [
        {"x": -2.646, "y": 0, "color": "#ff6b6b", "label": "(-\u221a7,0)"},
        {"x": 2.646, "y": 0, "color": "#ff6b6b", "label": "(\u221a7,0)"},
        {"x": 0, "y": -28, "color": "#ffd700", "label": "V(0,-28)"}
      ],
      "axisOfSymmetry": 0
    }
  },
  {
    "num": 5,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Section 3.6, Example 1D",
    "title": "x-Intercepts: \\( f(x) = x^2 - 15x + 50 \\) (Factoring)",
    "subtitle": "Unit 3 \u2022 Lecture 43 \u2022 Section 3.6 Example 1D (Workbook p. 83)",
    "detail": "Find the x-intercepts by factoring.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find the x-intercepts of \\(f(x) = x^2 - 15x + 50\\)**\n\nSet \\(f(x) = 0\\):\n$$x^2 - 15x + 50 = 0$$\n\n**Method: Factoring** \u2014 Find two numbers that:\n- **Multiply** to \\(+50\\)\n- **Add** to \\(-15\\)\n\nSearch: \\(-5 \\times -10 = 50\\) and \\(-5 + (-10) = -15\\) \u2713",
    "solution": "$$(x-5)(x-10) = 0$$\n\n**Zero-Product Property:**\n$$x-5 = 0 \\Rightarrow x = 5$$\n$$x-10 = 0 \\Rightarrow x = 10$$\n\n**x-intercepts:** \\((5,\\,0)\\) and \\((10,\\,0)\\)\n\n**y-intercept:** \\(f(0) = 50\\) \u2192 \\((0,\\,50)\\)\n\n**Vertex:** \\(x = \\dfrac{15}{2} = 7.5\\)\n$$f(7.5) = 56.25-112.5+50 = -6.25$$\n\n**Vertex:** \\((7.5,\\,-6.25)\\)",
    "pitfall": "**Sora\u2019s Factoring Check:** Always verify: \\((x-5)(x-10) = x^2-10x-5x+50 = x^2-15x+50\\) \u2713",
    "script": "[Prof. Park] For Example 1D, we look for factors of 50 that add to -15. That\u2019s -5 and -10, giving us (x-5)(x-10).\n\n[TA Sora] And factoring is so clean here! No decimals, no radicals. x=5 and x=10.",
    "coordinate": {
      "xMin": -1, "xMax": 12, "yMin": -10, "yMax": 20,
      "xTicks": 1, "yTicks": 5,
      "curves": [{"a": 1, "b": -15, "c": 50, "color": "#00d4ff", "strokeWidth": 3}],
      "points": [
        {"x": 5, "y": 0, "color": "#ff6b6b", "label": "(5,0)"},
        {"x": 10, "y": 0, "color": "#ff6b6b", "label": "(10,0)"},
        {"x": 7.5, "y": -6.25, "color": "#ffd700", "label": "V(7.5,-6.25)"}
      ],
      "axisOfSymmetry": 7.5
    }
  },
  {
    "num": 6,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Section 3.6, Example 4",
    "title": "All Features: \\( f(x) = -2(x-15)^2 + 50 \\)",
    "subtitle": "Unit 3 \u2022 Lecture 43 \u2022 Section 3.6 Example 4 (Workbook p. 85)",
    "detail": "Find x-intercepts, y-intercept, vertex, and f(20). Function is in vertex form.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Use \\(f(x) = -2(x-15)^2 + 50\\) to find:**\n\n**A.** x-intercept(s)\n\n**B.** y-intercept\n\n**C.** Vertex\n\n**D.** \\(f(20)\\)\n\n**Note:** This function is already in **vertex form** \\(f(x) = a(x-h)^2 + k\\)!",
    "solution": "**C. Vertex (read directly from vertex form):**\n$$h = 15,\\; k = 50 \\Rightarrow \\text{Vertex: } (15,\\,50)$$\n\n**B. y-intercept:** \\(f(0) = -2(0-15)^2+50 = -2(225)+50 = -450+50 = -400\\)\ny-intercept: \\((0,\\,-400)\\)\n\n**A. x-intercepts:** Set \\(f(x)=0\\):\n$$-2(x-15)^2+50=0 \\Rightarrow (x-15)^2=25 \\Rightarrow x-15=\\pm 5$$\n$$x = 20 \\quad \\text{or} \\quad x = 10$$\nx-intercepts: \\((10,\\,0)\\) and \\((20,\\,0)\\)\n\n**D.** \\(f(20) = -2(20-15)^2+50 = -2(25)+50 = -50+50 = \\mathbf{0}\\)\nConfirmed: \\((20,0)\\) is an x-intercept!",
    "pitfall": "**Sora\u2019s Note:** The y-intercept at (0,-400) is FAR below the vertex at (15,50). The parabola is very wide and tall.",
    "script": "[Prof. Park] Vertex form makes reading the vertex trivial. Just look: h=15, k=50. Vertex at (15,50)!\n\n[TA Sora] And for x-intercepts, we use the Square Root Property on vertex form. (x-15)\u00b2=25 gives x-15=\u00b15, so x=20 or x=10. Beautiful!",
    "coordinate": {
      "xMin": 5, "xMax": 25, "yMin": -10, "yMax": 60,
      "xTicks": 2, "yTicks": 10,
      "curves": [{"a": -2, "b": 60, "c": -400, "color": "#ff9500", "strokeWidth": 3}],
      "points": [
        {"x": 10, "y": 0, "color": "#ff6b6b", "label": "(10,0)"},
        {"x": 20, "y": 0, "color": "#ff6b6b", "label": "(20,0)"},
        {"x": 15, "y": 50, "color": "#ffd700", "label": "V(15,50)"}
      ],
      "axisOfSymmetry": 15
    }
  },
  {
    "num": 7,
    "type": "math_problem",
    "slideTypeLabel": "Section 3.6 Method Summary",
    "title": "Intercept Summary Chart \u2014 All Four Methods",
    "subtitle": "Unit 3 \u2022 Lecture 43 \u2022 Section 3.6 Summary (Workbook p. 84\u201385)",
    "detail": "Summary of when to use each method to find intercepts.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Summary of Finding Intercepts:**\n\n| Method | When to Use | Example |\n|---|---|---|\n| **Factor GCF** | No constant term \\(c\\) | \\(x^2+6x=0\\) |\n| **Square Root Property** | No middle term \\(b\\) | \\(4x^2=28\\) |\n| **Factoring** | Integer roots exist | \\(x^2-15x+50=0\\) |\n| **Quadratic Formula** | Always works! | \\(-2x^2+5x+6=0\\) |\n| **Vertex Form** | Already in \\(a(x-h)^2+k\\) | \\(-2(x-15)^2+50=0\\) |",
    "solution": "**Finding ALL Key Features:**\n\n| Feature | Method |\n|---|---|\n| **x-intercept(s)** | Set \\(f(x)=0\\), solve |\n| **y-intercept** | Set \\(x=0\\), evaluate \\(f(0)\\) |\n| **Vertex** | \\(x = \\dfrac{-b}{2a}\\), then plug in OR read from vertex form |",
    "pitfall": "**Sora\u2019s Final Tip:** ALWAYS check the discriminant before solving! If \\(\\Delta < 0\\), skip solving for x-intercepts and write: \\textit{No real x-intercepts}.",
    "script": "[TA Sora] This summary chart is my new best friend! Five methods, each for a different situation.\n\n[Prof. Park] Excellent, Sora. In Lecture 44 we put it all together and actually GRAPH these quadratics with the complete 5-point method!"
  },
  {
    "num": 8,
    "type": "math_problem",
    "slideTypeLabel": "Lecture 43 Review",
    "title": "Section 3.6 Complete \u2014 Lecture 43 Recap",
    "subtitle": "Unit 3 \u2022 Lecture 43 Summary",
    "detail": "Review of all four quadratic functions and their features.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Lecture 43 Complete Summary:**\n\n| Function | x-intercepts | y-intercept | Vertex |\n|---|---|---|---|\n| \\(g(x)=x^2+6x\\) | \\(0\\) and \\(-6\\) | \\(0\\) | \\((-3,-9)\\) |\n| \\(h(x)=-2x^2+5x+6\\) | \\(-0.89\\) and \\(3.39\\) | \\(6\\) | \\((1.25,9.13)\\) |\n| \\(f(x)=4x^2-28\\) | \\(\\pm\\sqrt{7}\\) | \\(-28\\) | \\((0,-28)\\) |\n| \\(f(x)=x^2-15x+50\\) | \\(5\\) and \\(10\\) | \\(50\\) | \\((7.5,-6.25)\\) |",
    "solution": "**Key Rules Confirmed:**\n1. x-intercepts: Set \\(f(x) = 0\\), solve\n2. y-intercept: Set \\(x = 0\\), compute \\(f(0) = c\\)\n3. Vertex x-coordinate: \\(x = \\dfrac{-b}{2a}\\)\n4. Vertex y-coordinate: Plug vertex x back into \\(f(x)\\)\n\n**Next Lecture:** Section 3.7 \u2014 Graphing Quadratic Functions with the 5-point method!",
    "pitfall": "**Sora\u2019s Observation:** For every quadratic, the y-intercept is just \\(c\\) (the constant term). No calculation needed!",
    "script": "[Prof. Park] Outstanding work in Lecture 43! You can now find all key features of any quadratic function.\n\n[TA Sora] In Lecture 44 we draw the actual graph using all these points. This is where everything comes together visually!"
  }
]

SLIDES_MONTANA_L44 = [
  {
    "num": 1,
    "type": "math_problem",
    "slideTypeLabel": "Lesson Introduction",
    "title": "Section 3.7: Graphing Quadratic Functions",
    "subtitle": "Unit 3 \u2022 Lecture 44 \u2022 Section 3.7 (Workbook p. 87)",
    "detail": "Lecture 44: The Complete 5-Point Method for Graphing Parabolas",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**5-Point Graphing Method for \\(f(x) = ax^2 + bx + c\\):**\n\n1. **Find the Vertex** \u2014 \\(x = \\dfrac{-b}{2a}\\), then compute \\(y\\)\n2. **Find the y-intercept** \u2014 \\((0, c)\\)\n3. **Find the x-intercept(s)** \u2014 Set \\(f(x)=0\\), solve\n4. **Symmetric Point** \u2014 Mirror the y-intercept across axis of symmetry\n5. **Connect** \u2014 Draw a smooth U-shaped curve through all points\n\n**State Domain and Range:**\n- Domain: Always \\((-\\infty, \\infty)\\)\n- Range: \\([k, \\infty)\\) if \\(a>0\\) or \\((-\\infty, k]\\) if \\(a<0\\) (\\(k\\) = vertex y-value)",
    "solution": "**Remember:**\n- \\(a > 0\\) \u2192 Parabola opens **upward** (minimum at vertex)\n- \\(a < 0\\) \u2192 Parabola opens **downward** (maximum at vertex)\n- Axis of symmetry: \\(x = \\dfrac{-b}{2a}\\) (always passes through vertex)",
    "pitfall": "**Sora\u2019s Tip:** The symmetric point of the y-intercept \\((0,c)\\) is at \\\\(\\left(\\dfrac{-b}{a},\\,c\\right)\\\\). Just double the x-distance from the axis!",
    "script": "[Prof. Park] Welcome to Lecture 44, Section 3.7! This is the culminating lesson of Unit 3. We take all our calculated values and produce a beautiful, accurate graph.\n\n[TA Sora] Five steps! And after five steps we have a perfect parabola. Let\u2019s practice on four examples from the workbook."
  },
  {
    "num": 2,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 1",
    "title": "Graph \\( g(x) = x^2 + 6x + 5 \\) Using Vertex and Table",
    "subtitle": "Unit 3 \u2022 Lecture 44 \u2022 Section 3.7 Example 1 (Workbook p. 87)",
    "detail": "Graph by finding the vertex and completing a table of values.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Graph \\(g(x) = x^2 + 6x + 5\\)**\n\n**Step 1 \u2014 Vertex:** \\(x = \\dfrac{-6}{2(1)} = -3\\),\\quad \\(g(-3) = 9-18+5 = -4\\)\n\n**Vertex:** \\((-3,\\,-4)\\)\n\n**Step 2 \u2014 Table** (centered at vertex x=-3):\n\n| \\(x\\) | \\(g(x)\\) |\n|---|---|\n| \\(-5\\) | \\(25-30+5=0\\) |\n| \\(-4\\) | \\(16-24+5=-3\\) |\n| \\(-3\\) | \\(-4\\) (vertex) |\n| \\(-2\\) | \\(4-12+5=-3\\) |\n| \\(-1\\) | \\(1-6+5=0\\) |",
    "solution": "**x-intercepts:** \\((-5,0)\\) and \\((-1,0)\\)\n\n**Verification by factoring:** \\(x^2+6x+5 = (x+5)(x+1)\\) \u2192 \\(x=-5\\) or \\(x=-1\\) \u2713\n\n**y-intercept:** \\(g(0) = 5\\) \u2192 \\((0,\\,5)\\)\n\n**Domain:** \\((-\\infty, \\infty)\\)\n**Range:** \\([-4, \\infty)\\) since \\(a=1>0\\) (minimum is \\(-4\\))",
    "pitfall": "**Sora\u2019s Note:** The table is symmetric around x=-3. Notice g(-4)=g(-2)=-3 and g(-5)=g(-1)=0. This confirms symmetry!",
    "script": "[Prof. Park] Example 1: g(x) = x\u00b2+6x+5. Vertex at (-3,-4). Build the table with two points on each side.\n\n[TA Sora] I love how the table is perfectly symmetric! Both sides mirror each other. That\u2019s how you know the parabola is graphed correctly.",
    "coordinate": {
      "xMin": -7, "xMax": 2, "yMin": -6, "yMax": 8,
      "xTicks": 1, "yTicks": 2,
      "curves": [{"a": 1, "b": 6, "c": 5, "color": "#00d4ff", "strokeWidth": 3}],
      "points": [
        {"x": -5, "y": 0, "color": "#ff6b6b", "label": "(-5,0)"},
        {"x": -1, "y": 0, "color": "#ff6b6b", "label": "(-1,0)"},
        {"x": -3, "y": -4, "color": "#ffd700", "label": "V(-3,-4)"},
        {"x": 0, "y": 5, "color": "#00ff88", "label": "(0,5)"}
      ],
      "axisOfSymmetry": -3
    }
  },
  {
    "num": 3,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 2",
    "title": "Graph \\( h(x) = -2x^2 + 4x + 6 \\) Using All Key Points",
    "subtitle": "Unit 3 \u2022 Lecture 44 \u2022 Section 3.7 Example 2 (Workbook p. 87)",
    "detail": "Graph by finding vertex, x-intercepts, and y-intercept.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Graph \\(h(x) = -2x^2 + 4x + 6\\)**\n\n**Step 1 \u2014 Vertex:** \\(a=-2,\\;b=4,\\;c=6\\)\n$$x = \\dfrac{-4}{2(-2)} = \\dfrac{-4}{-4} = 1,\\quad h(1) = -2+4+6 = 8$$\n\n**Vertex:** \\((1,\\,8)\\) \u2014 Maximum!\n\n**Step 2 \u2014 y-intercept:** \\(h(0) = 6\\) \u2192 \\((0,\\,6)\\)\n\n**Step 3 \u2014 x-intercepts:** Set \\(h(x)=0\\)\n$$-2x^2+4x+6=0 \\Rightarrow x^2-2x-3=0 \\Rightarrow (x-3)(x+1)=0$$",
    "solution": "$$x = 3 \\quad \\text{or} \\quad x = -1$$\n\n**x-intercepts:** \\((-1,\\,0)\\) and \\((3,\\,0)\\)\n\n**Symmetric point** of y-intercept: Mirror \\((0,6)\\) across \\(x=1\\) \u2192 \\((2,\\,6)\\)\n\n**Five key points:**\n\\((-1,0)\\), \\((0,6)\\), \\((1,8)\\), \\((2,6)\\), \\((3,0)\\)\n\n**Domain:** \\((-\\infty, \\infty)\\)\n\n**Range:** \\((-\\infty, 8]\\) since \\(a=-2<0\\) (maximum is \\(8\\))",
    "pitfall": "**Sora\u2019s Step:** Divide by -2 first: \\(-2x^2+4x+6=0 \\Rightarrow x^2-2x-3=0\\). This makes factoring much easier!",
    "script": "[Prof. Park] h(x) opens downward since a=-2. The vertex (1,8) is the MAXIMUM. Range is all y-values less than or equal to 8.\n\n[TA Sora] And dividing by -2 before factoring is so smart! We get x\u00b2-2x-3=0 which factors to (x-3)(x+1). Clean roots!",
    "coordinate": {
      "xMin": -3, "xMax": 5, "yMin": -5, "yMax": 12,
      "xTicks": 1, "yTicks": 2,
      "curves": [{"a": -2, "b": 4, "c": 6, "color": "#ff9500", "strokeWidth": 3}],
      "points": [
        {"x": -1, "y": 0, "color": "#ff6b6b", "label": "(-1,0)"},
        {"x": 3, "y": 0, "color": "#ff6b6b", "label": "(3,0)"},
        {"x": 1, "y": 8, "color": "#ffd700", "label": "V(1,8)"},
        {"x": 0, "y": 6, "color": "#00ff88", "label": "(0,6)"},
        {"x": 2, "y": 6, "color": "#00ff88", "label": "(2,6)"}
      ],
      "axisOfSymmetry": 1
    }
  },
  {
    "num": 4,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 3",
    "title": "Graph \\( g(x) = 2x^2 - 8x \\)",
    "subtitle": "Unit 3 \u2022 Lecture 44 \u2022 Section 3.7 Example 3 (Workbook p. 88)",
    "detail": "Graph by finding vertex, x-intercepts (GCF factoring), and key points.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Graph \\(g(x) = 2x^2 - 8x\\)**\n\n**Step 1 \u2014 Vertex:** \\(a=2,\\;b=-8,\\;c=0\\)\n$$x = \\dfrac{-(-8)}{2(2)} = \\dfrac{8}{4} = 2,\\quad g(2) = 2(4)-8(2) = 8-16 = -8$$\n\n**Vertex:** \\((2,\\,-8)\\) \u2014 Minimum!\n\n**Step 2 \u2014 x-intercepts:** Factor GCF (no constant term!)\n$$2x^2-8x=0 \\Rightarrow 2x(x-4)=0 \\Rightarrow x=0 \\text{ or } x=4$$",
    "solution": "**x-intercepts:** \\((0,\\,0)\\) and \\((4,\\,0)\\)\n\n**y-intercept:** \\(g(0)=0\\) \u2192 \\((0,\\,0)\\) \u2014 Same as one x-intercept!\n\n**Additional point** using table:\n$$g(1) = 2-8 = -6 \\rightarrow (1,-6)$$\n$$g(3) = 18-24 = -6 \\rightarrow (3,-6) \\text{ (symmetric)}$$\n\n**Five key points:** \\((0,0)\\), \\((1,-6)\\), \\((2,-8)\\), \\((3,-6)\\), \\((4,0)\\)\n\n**Domain:** \\((-\\infty, \\infty)\\)\n\n**Range:** \\([-8, \\infty)\\)",
    "pitfall": "**Sora\u2019s Note:** The origin \\((0,0)\\) is BOTH an x-intercept and the y-intercept. Use extra table points like \\((1,-6)\\) to plot the curve accurately.",
    "script": "[Prof. Park] g(x)=2x\u00b2-8x has no constant term, so GCF factoring gives us 2x(x-4)=0. Quick and easy!\n\n[TA Sora] The vertex is at (2,-8), the minimum. The parabola goes down to -8 and then back up. Domain is all real numbers, range is [-8, infinity).",
    "coordinate": {
      "xMin": -1, "xMax": 6, "yMin": -10, "yMax": 6,
      "xTicks": 1, "yTicks": 2,
      "curves": [{"a": 2, "b": -8, "c": 0, "color": "#00d4ff", "strokeWidth": 3}],
      "points": [
        {"x": 0, "y": 0, "color": "#ff6b6b", "label": "(0,0)"},
        {"x": 4, "y": 0, "color": "#ff6b6b", "label": "(4,0)"},
        {"x": 2, "y": -8, "color": "#ffd700", "label": "V(2,-8)"},
        {"x": 1, "y": -6, "color": "#00ff88", "label": "(1,-6)"},
        {"x": 3, "y": -6, "color": "#00ff88", "label": "(3,-6)"}
      ],
      "axisOfSymmetry": 2
    }
  },
  {
    "num": 5,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 4",
    "title": "Graph \\( f(x) = -\\frac{1}{2}(x+1)^2 + 8 \\) (Vertex Form)",
    "subtitle": "Unit 3 \u2022 Lecture 44 \u2022 Section 3.7 Example 4 (Workbook p. 88)",
    "detail": "Graph a quadratic in vertex form directly.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Graph \\(f(x) = -\\dfrac{1}{2}(x+1)^2 + 8\\)**\n\n**Vertex form:** \\(f(x) = a(x-h)^2 + k\\)\n\n**Read directly:**\n- \\(a = -\\dfrac{1}{2}\\) (opens downward, wide)\n- \\(h = -1\\) (vertex x-coordinate)\n- \\(k = 8\\) (vertex y-coordinate)\n\n**Vertex:** \\((-1,\\,8)\\) \u2014 Maximum!\n\n**Step 2 \u2014 y-intercept:** \\(f(0) = -\\dfrac{1}{2}(1)+8 = -0.5+8 = 7.5\\)",
    "solution": "**x-intercepts:** Set \\(f(x)=0\\):\n$$-\\dfrac{1}{2}(x+1)^2 + 8 = 0$$\n$$(x+1)^2 = 16 \\Rightarrow x+1 = \\pm 4$$\n$$x = 3 \\quad \\text{or} \\quad x = -5$$\n\n**x-intercepts:** \\((-5,\\,0)\\) and \\((3,\\,0)\\)\n\n**Symmetric point** of \\((0,7.5)\\) across \\(x=-1\\): \\((-2,\\,7.5)\\)\n\n**Five key points:** \\((-5,0)\\), \\((-2,7.5)\\), \\((-1,8)\\), \\((0,7.5)\\), \\((3,0)\\)\n\n**Domain:** \\((-\\infty, \\infty)\\)\n\n**Range:** \\((-\\infty, 8]\\)",
    "pitfall": "**Sora\u2019s Tip:** Multiply both sides by \\(-2\\) to isolate \\((x+1)^2\\): \\(-\\frac{1}{2}(x+1)^2 = -8 \\Rightarrow (x+1)^2 = 16\\).",
    "script": "[Prof. Park] Vertex form is the most elegant way to graph. Just read h, k directly, and the vertex is instantly known.\n\n[TA Sora] And with a=-1/2, the parabola opens down and is wider than usual! The coefficient magnitude being less than 1 means it spreads out more.",
    "coordinate": {
      "xMin": -7, "xMax": 5, "yMin": -5, "yMax": 12,
      "xTicks": 1, "yTicks": 2,
      "curves": [{"a": -0.5, "b": -1, "c": 7.5, "color": "#ff9500", "strokeWidth": 3}],
      "points": [
        {"x": -5, "y": 0, "color": "#ff6b6b", "label": "(-5,0)"},
        {"x": 3, "y": 0, "color": "#ff6b6b", "label": "(3,0)"},
        {"x": -1, "y": 8, "color": "#ffd700", "label": "V(-1,8)"},
        {"x": 0, "y": 7.5, "color": "#00ff88", "label": "(0,7.5)"},
        {"x": -2, "y": 7.5, "color": "#00ff88", "label": "(-2,7.5)"}
      ],
      "axisOfSymmetry": -1
    }
  },
  {
    "num": 6,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 5A & 5B",
    "title": "Evaluating Two Functions: \\( f(x) = x^2-6x+4 \\) and \\( g(x) = -2x+25 \\)",
    "subtitle": "Unit 3 \u2022 Lecture 44 \u2022 Section 3.7 Example 5 (Workbook p. 89)",
    "detail": "Evaluate f(-7) and g(-7).",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Given \\(f(x) = x^2 - 6x + 4\\) and \\(g(x) = -2x + 25\\), find:**\n\n**A.** \\(f(-7)\\)\n\n**B.** \\(g(-7)\\)",
    "solution": "**A.** \\(f(-7) = (-7)^2 - 6(-7) + 4 = 49 + 42 + 4 = \\mathbf{95}\\)\n\n**B.** \\(g(-7) = -2(-7) + 25 = 14 + 25 = \\mathbf{39}\\)\n\n**Observation:** Both functions take the input \\(-7\\).\n- \\(f\\) is quadratic: its value \\(95\\) is much larger due to the \\(x^2\\) term.\n- \\(g\\) is linear: its value \\(39\\) grows more slowly.",
    "pitfall": "**Sora\u2019s Sign Check:** \\((-7)^2 = 49\\) (positive!) and \\(-6(-7) = +42\\) (two negatives!). Be careful with signs when input is negative.",
    "script": "[Prof. Park] Example 5 introduces TWO functions simultaneously. We evaluate each at the same x-value and compare.\n\n[TA Sora] f(-7) = 49+42+4 = 95 and g(-7) = 14+25 = 39. The quadratic grows so much faster than the linear function!"
  },
  {
    "num": 7,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 5C & 5D",
    "title": "Function Composition: \\( f(x+5) \\) and \\( g(x+5) \\)",
    "subtitle": "Unit 3 \u2022 Lecture 44 \u2022 Section 3.7 Example 5 (Workbook p. 89)",
    "detail": "Find f(x+5) and g(x+5) by substitution.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Given \\(f(x) = x^2-6x+4\\) and \\(g(x) = -2x+25\\), find:**\n\n**C.** \\(f(x+5)\\)\n\n**D.** \\(g(x+5)\\)",
    "solution": "**C.** \\(f(x+5)\\): Replace every \\(x\\) with \\((x+5)\\)\n$$f(x+5) = (x+5)^2 - 6(x+5) + 4$$\n$$= x^2+10x+25 - 6x-30 + 4$$\n$$= \\mathbf{x^2 + 4x - 1}$$\n\n**D.** \\(g(x+5)\\): Replace every \\(x\\) with \\((x+5)\\)\n$$g(x+5) = -2(x+5) + 25 = -2x-10+25 = \\mathbf{-2x + 15}$$",
    "pitfall": "**Sora\u2019s FOIL Reminder:** \\((x+5)^2 = x^2 + 10x + 25\\), NOT \\(x^2+25\\)! Always expand the binomial squared fully.",
    "script": "[Prof. Park] Parts C and D test function composition. Replace every x with the expression (x+5).\n\n[TA Sora] For g(x+5) it\u2019s simple: just replace x with x+5 in the linear function. For f(x+5) we need FOIL for the squared binomial."
  },
  {
    "num": 8,
    "type": "math_problem",
    "slideTypeLabel": "Workbook Example 5E & 5F",
    "title": "Solving: \\( g(x) = 17 \\) and \\( f(x) = g(x) \\)",
    "subtitle": "Unit 3 \u2022 Lecture 44 \u2022 Section 3.7 Example 5 (Workbook p. 89)",
    "detail": "Solve g(x)=17 and f(x)=g(x) for x.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Given \\(f(x) = x^2-6x+4\\) and \\(g(x) = -2x+25\\), find:**\n\n**E.** Solve for \\(x\\) if \\(g(x) = 17\\)\n\n**F.** Solve for \\(x\\) if \\(f(x) = g(x)\\)",
    "solution": "**E.** \\(g(x) = 17\\):\n$$-2x+25 = 17 \\Rightarrow -2x = -8 \\Rightarrow x = \\mathbf{4}$$\n\n**F.** \\(f(x) = g(x)\\): Set the two functions equal\n$$x^2-6x+4 = -2x+25$$\n$$x^2-6x+2x+4-25 = 0$$\n$$x^2-4x-21 = 0$$\n$$(x-7)(x+3) = 0$$\n$$x = \\mathbf{7} \\quad \\text{or} \\quad x = \\mathbf{-3}$$\n\n**Intersection points:** At \\(x=7\\): \\(g(7)=-14+25=11\\) \u2192 \\((7,11)\\)\nAt \\(x=-3\\): \\(g(-3)=6+25=31\\) \u2192 \\((-3,31)\\)",
    "pitfall": "**Sora\u2019s Note for Part F:** Setting f(x)=g(x) finds where the parabola and line INTERSECT. Rearrange to one side = 0, then factor or use the Quadratic Formula.",
    "script": "[Prof. Park] Part F is a beautiful application: where do the parabola and the line cross? Setting f(x)=g(x) and solving gives the intersection points.\n\n[TA Sora] x\u00b2-6x+4 = -2x+25 becomes x\u00b2-4x-21=0. Factoring gives (x-7)(x+3)=0. Two intersection points at x=7 and x=-3!"
  }
]

SLIDES_MONTANA_L45 = [
  {
    "num": 1,
    "type": "math_problem",
    "slideTypeLabel": "Lesson Introduction",
    "title": "Section 3.7 Part 2: Comprehensive Graphing Review",
    "subtitle": "Unit 3 \u2022 Lecture 45 \u2022 Section 3.7 (Workbook pp. 87\u201390)",
    "detail": "Lecture 45: Complete Quadratic Graphing and Unit 3 Capstone",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Lecture 45 Agenda:**\n\n1. **Domain and Range Review** \u2014 for all four graphed functions\n2. **Graphing from Scratch Practice** \u2014 complete 5-point method\n3. **Graph Comparison** \u2014 parabola vs. linear function on same axes\n4. **Unit 3 Grand Summary** \u2014 all methods, all concepts\n5. **Graduation Celebration** \u2014 You have completed M090 Unit 3!\n\n**Unit 3 Topics Mastered:**\n- Vertex form, standard form, transformations\n- Square Root Property, factoring, completing the square\n- Quadratic Formula and discriminant\n- Graphing with 5-point method",
    "solution": "**The Big Picture of Unit 3:**\n$$f(x) = ax^2 + bx + c \\qquad \\text{(Standard Form)}$$\n$$f(x) = a(x-h)^2 + k \\qquad \\text{(Vertex Form)}$$\n\nBoth represent the same parabola. Vertex form makes graphing instant; standard form makes formula applications easy.",
    "pitfall": "**Sora\u2019s Motivation:** You\u2019ve gone from x\u00b2 all the way to the Quadratic Formula and full graphing! This is the most advanced math in M090. Be proud!",
    "script": "[Prof. Park] Welcome to the final lecture of Unit 3 and of the entire M090 course! Lecture 45 is our grand capstone.\n\n[TA Sora] We\u2019ve come so far! From simple variables in Unit 1, to lines in Unit 2, to full parabola graphing in Unit 3. Let\u2019s celebrate and review!"
  },
  {
    "num": 2,
    "type": "math_problem",
    "slideTypeLabel": "Domain and Range Review",
    "title": "Domain and Range for All Four Section 3.7 Functions",
    "subtitle": "Unit 3 \u2022 Lecture 45 \u2022 Section 3.7 Domain & Range",
    "detail": "State domain and range for all four graphed parabolas.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**State Domain and Range for each function:**\n\n| Function | Opens | Vertex | Domain | Range |\n|---|---|---|---|---|\n| \\(g(x)=x^2+6x+5\\) | Up | \\((-3,-4)\\) | | |\n| \\(h(x)=-2x^2+4x+6\\) | Down | \\((1,8)\\) | | |\n| \\(g(x)=2x^2-8x\\) | Up | \\((2,-8)\\) | | |\n| \\(f(x)=-\\frac{1}{2}(x+1)^2+8\\) | Down | \\((-1,8)\\) | | |",
    "solution": "| Function | Domain | Range |\n|---|---|---|\n| \\(g(x)=x^2+6x+5\\) | \\((-\\infty,\\infty)\\) | \\([-4,\\infty)\\) |\n| \\(h(x)=-2x^2+4x+6\\) | \\((-\\infty,\\infty)\\) | \\((-\\infty,8]\\) |\n| \\(g(x)=2x^2-8x\\) | \\((-\\infty,\\infty)\\) | \\([-8,\\infty)\\) |\n| \\(f(x)=-\\frac{1}{2}(x+1)^2+8\\) | \\((-\\infty,\\infty)\\) | \\((-\\infty,8]\\) |\n\n**Rule:** Domain is ALWAYS \\((-\\infty,\\infty)\\) for quadratic functions. Range depends on direction (up/down) and vertex y-value.",
    "pitfall": "**Sora\u2019s Memory Trick:** Opens UP \u2192 Range has a minimum \\([k, \\infty)\\). Opens DOWN \u2192 Range has a maximum \\((-\\infty, k]\\).",
    "script": "[Prof. Park] Domain for all quadratics is the entire real number line. No restrictions!\n\n[TA Sora] And range depends on whether the parabola opens up or down. Up means minimum at vertex, down means maximum at vertex."
  },
  {
    "num": 3,
    "type": "math_problem",
    "slideTypeLabel": "Complete Graphing Practice",
    "title": "Full Graph: \\( p(x) = x^2 - 4x - 5 \\) \u2014 5-Point Method",
    "subtitle": "Unit 3 \u2022 Lecture 45 \u2022 Comprehensive Graphing Practice",
    "detail": "Apply the complete 5-point method from scratch.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Graph \\(p(x) = x^2 - 4x - 5\\) using the 5-point method:**\n\n**Step 1 \u2014 Vertex:**\n$$x = \\dfrac{-(-4)}{2(1)} = \\dfrac{4}{2} = 2$$\n$$p(2) = 4-8-5 = -9$$\n**Vertex:** \\((2,\\,-9)\\) \u2014 Minimum\n\n**Step 2 \u2014 y-intercept:**\n$$p(0) = -5 \\Rightarrow (0,\\,-5)$$",
    "solution": "**Step 3 \u2014 x-intercepts:** Set \\(p(x)=0\\)\n$$x^2-4x-5=0 \\Rightarrow (x-5)(x+1)=0$$\n$$x = 5 \\quad \\text{or} \\quad x=-1$$\n**x-intercepts:** \\((-1,0)\\) and \\((5,0)\\)\n\n**Step 4 \u2014 Symmetric point** of \\((0,-5)\\):\nAxis of symmetry: \\(x=2\\). Distance from 0 to 2 is 2. Mirror: \\(x=4\\)\n$$p(4) = 16-16-5 = -5 \\Rightarrow (4,\\,-5)\\text{ \u2713}$$\n\n**Step 5 \u2014 Five key points:**\n\\((-1,0)\\), \\((0,-5)\\), \\((2,-9)\\), \\((4,-5)\\), \\((5,0)\\)\n\n**Domain:** \\((-\\infty,\\infty)\\) \\qquad **Range:** \\([-9,\\infty)\\)",
    "pitfall": "**Sora\u2019s Check:** Verify the symmetric point by computing \\(p(4)\\) directly. It should equal \\(p(0) = -5\\). \u2713 Symmetry confirmed!",
    "script": "[TA Sora] Five clean steps: vertex, y-intercept, x-intercepts, symmetric point, and done! I have five perfect points to plot.\n\n[Prof. Park] And the symmetric point is a great self-check. If it matches, your axis of symmetry is correct.",
    "coordinate": {
      "xMin": -3, "xMax": 7, "yMin": -12, "yMax": 6,
      "xTicks": 1, "yTicks": 2,
      "curves": [{"a": 1, "b": -4, "c": -5, "color": "#00d4ff", "strokeWidth": 3}],
      "points": [
        {"x": -1, "y": 0, "color": "#ff6b6b", "label": "(-1,0)"},
        {"x": 5, "y": 0, "color": "#ff6b6b", "label": "(5,0)"},
        {"x": 2, "y": -9, "color": "#ffd700", "label": "V(2,-9)"},
        {"x": 0, "y": -5, "color": "#00ff88", "label": "(0,-5)"},
        {"x": 4, "y": -5, "color": "#00ff88", "label": "(4,-5)"}
      ],
      "axisOfSymmetry": 2
    }
  },
  {
    "num": 4,
    "type": "math_problem",
    "slideTypeLabel": "Parabola vs. Line on Same Graph",
    "title": "Intersection of \\( f(x) = x^2-6x+4 \\) and \\( g(x) = -2x+25 \\)",
    "subtitle": "Unit 3 \u2022 Lecture 45 \u2022 Section 3.7 Example 5F Visual (Workbook p. 89)",
    "detail": "Graph both functions and identify their intersection points.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Graph both \\(f(x) = x^2-6x+4\\) (parabola) and \\(g(x) = -2x+25\\) (line) on the same axes.**\n\n**Parabola \\(f(x)\\):**\n- Vertex: \\(x=3\\), \\(f(3)=9-18+4=-5\\) \u2192 \\((3,-5)\\)\n- y-intercept: \\((0,4)\\)\n- x-intercepts: \\(x^2-6x+4=0\\) \u2192 \\(x=3\\pm\\sqrt{5}\\approx(5.24,0)\\) and \\((0.76,0)\\)\n\n**Line \\(g(x)\\):**\n- y-intercept: \\((0,25)\\)\n- x-intercept: \\(-2x+25=0\\) \u2192 \\(x=12.5\\)",
    "solution": "**Intersection (from Lecture 44, Part F):**\n$$f(x) = g(x) \\Rightarrow x^2-4x-21=0 \\Rightarrow (x-7)(x+3)=0$$\n$$x = 7 \\quad \\text{or} \\quad x=-3$$\n\n**Intersection points:**\n- At \\(x=7\\): \\(g(7) = -14+25 = 11\\) \u2192 \\((7,\\,11)\\)\n- At \\(x=-3\\): \\(g(-3) = 6+25 = 31\\) \u2192 \\((-3,\\,31)\\)\n\n**Visual:** The line \\(g\\) crosses the parabola \\(f\\) at \\((-3,31)\\) and \\((7,11)\\). Between these points, the line is above the parabola.",
    "pitfall": "**Sora\u2019s Observation:** Where \\(g(x) > f(x)\\), the line is above the parabola. Where \\(g(x) < f(x)\\), the parabola is above the line. The intersection points are the switchover!",
    "script": "[Prof. Park] When we graph a parabola and a line together, the intersection points are found by setting them equal and solving.\n\n[TA Sora] Two intersection points at (-3,31) and (7,11). This is the graphical meaning of solving f(x)=g(x)!",
    "coordinate": {
      "xMin": -5, "xMax": 14, "yMin": -10, "yMax": 35,
      "xTicks": 2, "yTicks": 5,
      "curves": [
        {"a": 1, "b": -6, "c": 4, "color": "#00d4ff", "strokeWidth": 3, "label": "f(x)"},
        {"a": 0, "b": -2, "c": 25, "color": "#ff9500", "strokeWidth": 2, "dashed": True, "label": "g(x)"}
      ],
      "points": [
        {"x": 3, "y": -5, "color": "#ffd700", "label": "V(3,-5)"},
        {"x": -3, "y": 31, "color": "#ff6b6b", "label": "(-3,31)"},
        {"x": 7, "y": 11, "color": "#ff6b6b", "label": "(7,11)"}
      ]
    }
  },
  {
    "num": 5,
    "type": "math_problem",
    "slideTypeLabel": "Unit 3 Complete Summary",
    "title": "Unit 3 Grand Review: All Methods for Quadratic Functions",
    "subtitle": "Unit 3 \u2022 Lecture 45 \u2022 Complete Unit Summary",
    "detail": "Comprehensive review of all Unit 3 concepts.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Unit 3 \u2014 All Methods Mastered:**\n\n| Section | Topic | Method |\n|---|---|---|\n| 3.0 | Quadratic Functions intro | Identify vertex, direction |\n| 3.1 | Vertex & y-intercept | \\(x=-b/2a\\), plug in |\n| 3.2 | x-intercepts | Square Root Property |\n| 3.3 | x-intercepts | Factoring |\n| 3.4 | x-intercepts | Completing the Square |\n| 3.5 | x-intercepts | Quadratic Formula \\(\\pm\\sqrt{\\Delta}\\) |\n| 3.6 | Mixed methods | Choose best approach |\n| 3.7 | Full graph | 5-point method + Domain/Range |",
    "solution": "**The Master Decision Tree:**\n1. Is it in vertex form \\(a(x-h)^2+k\\)? \u2192 Read vertex directly\n2. No \\(b\\) term? \u2192 Square Root Property\n3. No \\(c\\) term? \u2192 Factor out GCF\n4. Factors nicely? \u2192 Factor\n5. Otherwise \u2192 **Quadratic Formula** (always works!)\n\n**5-Point Graph Checklist:**\n\\(\\square\\) Vertex \\(\\square\\) y-intercept \\(\\square\\) x-intercept(s) \\(\\square\\) Symmetric point \\(\\square\\) Smooth curve",
    "pitfall": "**Sora\u2019s Final Wisdom:** When in doubt, use the Quadratic Formula. It ALWAYS works and never fails. But always set the equation to zero first!",
    "script": "[Prof. Park] This is the complete roadmap of Unit 3. Eight sections, eight skills, all building toward one goal: graphing quadratic functions completely and accurately.\n\n[TA Sora] Every section added one more tool to our toolkit. Now we have the complete set. I feel like a math superhero!"
  },
  {
    "num": 6,
    "type": "math_problem",
    "slideTypeLabel": "Key Formulas Reference Card",
    "title": "M090 Unit 3 Formula Card \u2014 Keep This Forever!",
    "subtitle": "Unit 3 \u2022 Lecture 45 \u2022 Formula Reference",
    "detail": "All essential formulas from Unit 3 in one place.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Essential Unit 3 Formulas:**\n\n$$\\textbf{Standard Form: } f(x) = ax^2 + bx + c$$\n\n$$\\textbf{Vertex Form: } f(x) = a(x-h)^2 + k$$\n\n$$\\textbf{Axis of Symmetry: } x = \\dfrac{-b}{2a}$$\n\n$$\\textbf{Quadratic Formula: } x = \\dfrac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$\n\n$$\\textbf{Discriminant: } \\Delta = b^2 - 4ac$$",
    "solution": "**Quick Reference:**\n\n| Feature | Formula |\n|---|---|\n| Vertex x | \\(\\dfrac{-b}{2a}\\) |\n| Vertex y | \\(f\\left(\\dfrac{-b}{2a}\\right)\\) |\n| y-intercept | \\((0, c)\\) |\n| x-intercept | Solve \\(f(x)=0\\) |\n| Discriminant | \\(b^2-4ac\\) |\n| Domain | \\((-\\infty,\\infty)\\) always |\n| Range (up) | \\([k,\\infty)\\) |\n| Range (down) | \\((-\\infty,k]\\) |",
    "pitfall": "**Sora\u2019s Study Tip:** Write these formulas on an index card and put it on your desk. By the end of this semester, you\u2019ll have them memorized without even trying!",
    "script": "[TA Sora] This formula card is pure gold! Every formula from Unit 3 in one place.\n\n[Prof. Park] Memorize the Quadratic Formula first. With that one formula and the vertex formula, you can solve virtually any quadratic problem."
  },
  {
    "num": 7,
    "type": "math_problem",
    "slideTypeLabel": "Final Challenge Problem",
    "title": "Challenge: Complete Analysis of \\( q(x) = -3x^2 + 12x - 9 \\)",
    "subtitle": "Unit 3 \u2022 Lecture 45 \u2022 Final Challenge",
    "detail": "Find all features and graph this quadratic completely.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**Find all features and graph \\(q(x) = -3x^2 + 12x - 9\\):**\n\n1. Direction of opening\n2. Vertex\n3. Axis of symmetry\n4. y-intercept\n5. x-intercept(s) \u2014 use best method\n6. Domain and Range",
    "solution": "**1. Direction:** \\(a=-3<0\\) \u2192 Opens **downward** (maximum)\n\n**2. Vertex:** \\(x=\\dfrac{-12}{2(-3)}=\\dfrac{-12}{-6}=2\\)\n$$q(2)=-3(4)+12(2)-9=-12+24-9=\\mathbf{3}$$\n**Vertex: \\((2,3)\\)**\n\n**3. Axis of Symmetry:** \\(x=2\\)\n\n**4. y-intercept:** \\(q(0)=-9\\) \u2192 \\((0,-9)\\)\n\n**5. x-intercepts:** Factor out \\(-3\\):\n$$-3x^2+12x-9=0 \\Rightarrow x^2-4x+3=0 \\Rightarrow (x-1)(x-3)=0$$\n$$x=1 \\text{ or } x=3$$\n**x-intercepts: \\((1,0)\\) and \\((3,0)\\)**\n\n**6. Domain:** \\((-\\infty,\\infty)\\) \\quad **Range:** \\((-\\infty,3]\\)",
    "pitfall": "**Sora\u2019s Shortcut:** Divide by \\(-3\\) first: \\(x^2-4x+3=0\\) is much easier to factor than \\(-3x^2+12x-9=0\\)!",
    "script": "[Prof. Park] Our final challenge! Everything at once: direction, vertex, intercepts, domain, range.\n\n[TA Sora] Divide by -3 first to simplify. Then x\u00b2-4x+3=0 factors to (x-1)(x-3)=0 instantly. This is Unit 3 mastery!",
    "coordinate": {
      "xMin": -1, "xMax": 5, "yMin": -12, "yMax": 6,
      "xTicks": 1, "yTicks": 2,
      "curves": [{"a": -3, "b": 12, "c": -9, "color": "#ff9500", "strokeWidth": 3}],
      "points": [
        {"x": 1, "y": 0, "color": "#ff6b6b", "label": "(1,0)"},
        {"x": 3, "y": 0, "color": "#ff6b6b", "label": "(3,0)"},
        {"x": 2, "y": 3, "color": "#ffd700", "label": "V(2,3)"},
        {"x": 0, "y": -9, "color": "#00ff88", "label": "(0,-9)"}
      ],
      "axisOfSymmetry": 2
    }
  },
  {
    "num": 8,
    "type": "math_problem",
    "slideTypeLabel": "Unit 3 Graduation Celebration",
    "title": "Congratulations! You Have Completed M090 Unit 3!",
    "subtitle": "Unit 3 \u2022 Lecture 45 \u2022 Course Milestone",
    "detail": "Celebration of completing Unit 3 and the entire M090 course.",
    "instructor": "Prof. Eunju Park \u2022 TA Sora (Gallatin College MSU)",
    "problem": "**You have successfully completed Unit 3: Quadratic Functions!**\n\n**What you have mastered:**\n- \\(\\checkmark\\) Identifying and graphing quadratic functions\n- \\(\\checkmark\\) Finding vertices using \\(x = -b/2a\\)\n- \\(\\checkmark\\) Square Root Property for x-intercepts\n- \\(\\checkmark\\) Factoring quadratic equations\n- \\(\\checkmark\\) Completing the Square\n- \\(\\checkmark\\) The Quadratic Formula\n- \\(\\checkmark\\) The Discriminant\n- \\(\\checkmark\\) Mixed methods and the decision strategy\n- \\(\\checkmark\\) Full 5-point graphing with domain and range",
    "solution": "**M090 Introductory Algebra \u2014 All Units Complete:**\n\n| Unit | Topic | Status |\n|---|---|---|\n| Unit 1 | The Language of Algebra | \\(\\checkmark\\) Complete |\n| Unit 2 | Linear Functions & Graphing | \\(\\checkmark\\) Complete |\n| Unit 3 | Quadratic Functions | \\(\\checkmark\\) Complete |\n\n**Next Steps:** MTH 103 (College Algebra) at Gallatin College MSU!\n\n**Well done, Bobcats! Go MSU!**",
    "pitfall": "**Sora\u2019s Farewell:** Math is not a talent\u2014it\u2019s a skill. And you\u2019ve proven that with dedication and practice, ANY student can master Introductory Algebra. See you in MTH 103!",
    "script": "[Prof. Park] Students of M090 at Gallatin College Montana State University, I am incredibly proud of each and every one of you. You have worked hard through three full units of algebra.\n\n[TA Sora] From day one when we learned what a variable is, to today when we\u2019re graphing full parabolas with discriminants and vertex forms\u2014what a journey!\n\n[Prof. Park] Unit 1 gave you the language of algebra. Unit 2 gave you the power of linear functions. And Unit 3 showed you the beauty of curves.\n\n[TA Sora] Whether you\u2019re heading to College Algebra next, or simply needed this math skill for your career, I hope you feel confident and capable in your mathematical abilities.\n\n[Prof. Park] Study hard for your final exam, review all three units systematically, and remember: algebra is just pattern recognition with symbols. You\u2019ve got this!\n\n[TA Sora] Go Bobcats! Go MSU! And thank you for being such wonderful students. We\u2019ll see you in the next course!"
  }
]

if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.dirname(__file__))
    
    print("L41 slides:", len(SLIDES_MONTANA_L41))
    print("L42 slides:", len(SLIDES_MONTANA_L42))
    print("L43 slides:", len(SLIDES_MONTANA_L43))
    print("L44 slides:", len(SLIDES_MONTANA_L44))
    print("L45 slides:", len(SLIDES_MONTANA_L45))
    
    total = len(SLIDES_MONTANA_L41) + len(SLIDES_MONTANA_L42) + len(SLIDES_MONTANA_L43) + len(SLIDES_MONTANA_L44) + len(SLIDES_MONTANA_L45)
    print(f"Total L41-L45: {total} slides")
    
    # Validate no Korean
    all_slides = SLIDES_MONTANA_L41 + SLIDES_MONTANA_L42 + SLIDES_MONTANA_L43 + SLIDES_MONTANA_L44 + SLIDES_MONTANA_L45
    import unicodedata
    korean_count = 0
    for slide in all_slides:
        for key, val in slide.items():
            if isinstance(val, str):
                for ch in val:
                    if '\uAC00' <= ch <= '\uD7A3':
                        korean_count += 1
    print(f"Korean characters found: {korean_count}")
    
    print("OK - unit3_data_l41_l45.py ready")
