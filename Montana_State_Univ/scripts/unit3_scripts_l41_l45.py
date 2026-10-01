# -*- coding: utf-8 -*-
"""
unit3_scripts_l43_l45.py
Full 20-25 Minute Broadcast Tiki-Taka Dialogue for Lectures 43, 44, 45
Prof. Eunju Park & TA Sora (Gallatin College Montana State University)
Grand Finale of Unit 3: ~300-360 words per slide (~2,400-2,700 words per lecture).
"""

SCRIPTS_L43 = {
    1: """[Prof. Park] Welcome back to M090, Bobcats! I am Professor Eunju Park, and joining me is our teaching assistant, Sora. Today we reach Section 3.6 on page 94 of your workbook: Mixed Methods for Intercepts and Vertex.

[TA Sora] Hello everyone! Over the past two weeks, we have learned four distinct mathematical weapons to solve quadratic equations: 1. The Square Root Property, 2. Factoring, 3. Completing the Square, and 4. The Quadratic Formula. But on an exam or in real-world engineering, nobody tells you which method to use!

[Prof. Park] Exactly. That is the transition from being a student who just follows steps to becoming a master craftsman who chooses the right tool for the job. You wouldn't use a massive chainsaw to sharpen a pencil, and you wouldn't use a tiny hand drill to bore through granite in the Rocky Mountains!

[TA Sora] Each method has its sweet spot. Today, we are going to train our tactical decision-making instincts. When you see an equation, you will know within five seconds which path is the fastest and least prone to mistakes!

[Prof. Park] Let's outline our tactical hierarchy: If there is no middle $x$ term ($b = 0$), the Square Root Property is fastest. If the trinomial factors in your head in ten seconds, Factoring is fastest. If $a = 1$ and $b$ is an even number, Completing the Square is wonderful. And if numbers are ugly, fractions loom, or factoring fails, the Quadratic Formula is your unstoppable tank!

[TA Sora] Keep your workbook open to page 94. Let's test our tactical instincts on Problem 1 on Slide 2!""",

    2: """[Prof. Park] Slide 2 presents Problem 1: Solve the equation $x^2 - 36 = 0$. Sora, which tool should we grab from our toolbox?

[TA Sora] Look at the structure: there is an $x^2$ term, but there is NO linear $x$ term ($b = 0$)! When $b = 0$, our fastest weapon is the Square Root Property!

[Prof. Park] Let's execute it: add 36 to both sides to isolate the square: $x^2 = 36$. Now take the square root of both sides, remembering our mandatory $\\pm$ sign: $x = \\pm \\sqrt{36}$!

[TA Sora] Since 36 is a perfect square, $\\sqrt{36} = 6$. So $x = \\pm 6$, which means $x = 6$ and $x = -6$! That took literally ten seconds!

[Prof. Park] Now, could you have solved this by Factoring as a Difference of Squares: $(x - 6)(x + 6) = 0$? Yes! And could you have used the Quadratic Formula with $a = 1$, $b = 0$, and $c = -36$? Yes, but it would have taken ten times longer!

[TA Sora] That's the power of tactical choice. Pick the path of least resistance. The two $x$-intercepts on the graph are $(-6, 0)$ and $(6, 0)$, perfectly balanced around the $y$-axis.

[Prof. Park] Solution set: $\\{-6, 6\\}$. Clean, fast, and effortless!""",

    3: """[Prof. Park] Turning to Slide 3, Problem 2 asks us to solve: $x^2 - 7x + 10 = 0$. Sora, what is our tactical assessment?

[TA Sora] Let's scan the equation: $a = 1$, $b = -7$, and $c = 10$. Can we find two numbers that multiply to $+10$ and add to $-7$?

[Prof. Park] Factors of 10: $-2$ and $-5$! $-2 \\times (-5) = +10$, and $-2 + (-5) = -7$! That took five seconds of mental arithmetic!

[TA Sora] Since it factors cleanly in our head, Factoring is by far our best choice! Factor into: $(x - 2)(x - 5) = 0$.

[Prof. Park] Apply the Zero Product Property: $x - 2 = 0 \\implies x = 2$, and $x - 5 = 0 \\implies x = 5$!

[TA Sora] Our two roots are $x = 2$ and $x = 5$. Could we have used the Quadratic Formula here? Sure! But setting up $-(-7) \\pm \\sqrt{49 - 40}$ over 2 requires much more writing and increases the chance of arithmetic slip-ups.

[Prof. Park] When factoring is obvious, take the gift and solve it by factoring! Solution set: $\\{2, 5\\}$.""",

    4: """[Prof. Park] Slide 4 presents Problem 3: Solve $x^2 + 6x - 2 = 0$. Let's scan this equation tactically.

[TA Sora] Let's check factoring first: factors of $-2$ are only $1$ and $-2$, or $-1$ and $2$. Neither pair adds to $+6$! So factoring is completely impossible.

[Prof. Park] Factoring is off the table. Now look at the coefficients: $a = 1$, and $b = +6$, which is an EVEN number! When $a = 1$ and $b$ is even, Completing the Square is exceptionally smooth!

[TA Sora] Let's execute Completing the Square: add 2 to both sides: $x^2 + 6x = 2$. Half of 6 is 3, and $3^2 = 9$. Add 9 to both sides: $x^2 + 6x + 9 = 2 + 9$!

[Prof. Park] Package the square: $(x + 3)^2 = 11$. Apply the Square Root Property: $x + 3 = \\pm \\sqrt{11}$. Subtract 3: $x = -3 \\pm \\sqrt{11}$!

[TA Sora] Look at how fast that was! Only four lines of clean algebra, with zero large fractions. If you used the Quadratic Formula, you would get $(-6 \\pm \\sqrt{44}) / 2$, and you would have to simplify $\\sqrt{44} = 2\\sqrt{11}$ and cancel the 2. Completing the square avoided that entire reduction!

[Prof. Park] Knowing when $b$ is even gives you a massive shortcut. Solution set: $\\{-3 - \\sqrt{11}, -3 + \\sqrt{11}\\}$!""",

    5: """[Prof. Park] On Slide 5, Problem 4 presents: $3x^2 - 5x - 4 = 0$. Sora, what is our tactical assessment here?

[TA Sora] Let's scan: $a = 3$, $b = -5$, and $c = -4$. First, $a \\neq 1$, and $b = -5$ is an odd number. If we tried Completing the Square, we would have to divide by 3 and get messy fractions like $-5/3$ and squaring to $25/36$! We don't want that!

[Prof. Park] And if we try the ac-method: $a \\times c = 3 \\times (-4) = -12$. Factors of $-12$ that add to $-5$? $-12$ and $1$ ($-11$), $-6$ and $2$ ($-4$), $-4$ and $3$ ($-1$). None of them equal $-5$! So it does NOT factor!

[TA Sora] Factoring is impossible, and Completing the Square has fraction bloat. That means it is time to bring out the big tank: The Quadratic Formula!

[Prof. Park] Let's deploy the formula: $x = \\frac{-(-5) \\pm \\sqrt{(-5)^2 - 4(3)(-4)}}{2(3)}$. 

[TA Sora] Under the radical: $(-5)^2 = 25$. And $-4(3)(-4) = +48$! So $25 + 48 = 73$! In the denominator: $2(3) = 6$.

[Prof. Park] So our exact solutions are: $x = \\frac{5 \\pm \\sqrt{73}}{6}$! Since 73 is a prime number, it cannot be simplified any further.

[TA Sora] The Quadratic Formula handled an otherwise impossible problem with calm certainty. Solution set: $\\{\\frac{5 - \\sqrt{73}}{6}, \\frac{5 + \\sqrt{73}}{6}\\}$!""",

    6: """[Prof. Park] Slide 6 compares our two methods for finding the Vertex: using the Vertex Formula $x_v = -b / (2a)$ versus converting to Vertex Form via Completing the Square.

[TA Sora] Let's test both on $f(x) = 2x^2 - 8x + 3$: Method 1, Vertex Formula: $a = 2$, $b = -8$. $x_v = -(-8) / (2 \\cdot 2) = 8 / 4 = 2$! Then evaluate $f(2) = 2(2)^2 - 8(2) + 3 = 8 - 16 + 3 = -5$! Vertex is $(2, -5)$!

[Prof. Park] Method 2, Completing the Square: Factor 2 from variable terms: $2(x^2 - 4x) + 3$. Half of $-4$ is $-2$, squared is 4. Add 4 inside: $2(x^2 - 4x + 4) + 3 - 2(4) = 2(x - 2)^2 + 3 - 8 = 2(x - 2)^2 - 5$! The vertex is $(2, -5)$!

[TA Sora] Both methods yield the exact same vertex $(2, -5)$. The formula is usually faster, but vertex form reveals the complete geometric transformations!""",

    7: """[Prof. Park] Slide 7 presents our Intercept Summary Chart—the master strategy guide to keep in your notes forever.

[TA Sora] Let's summarize the decision tree: 1. Is $b = 0$? Use the Square Root Property ($x^2 = k$). 2. Does it factor easily? Use Factoring ($A \\cdot B = 0$). 3. Is $a = 1$ and $b$ even? Use Completing the Square. 4. Is it non-factorable or messy? Use the Quadratic Formula!

[Prof. Park] Knowing when to use which tool gives you total mastery over any quadratic problem.""",

    8: """[Prof. Park] Section 3.6 is complete! You now possess tactical maturity in college algebra.

[TA Sora] In Lecture 44, we bring all these skills together into the 5-Point Graphing Method. Great job today, Bobcats!"""
}

SCRIPTS_L44 = {
    1: """[Prof. Park] Welcome to Lecture 44 of M090! Today we enter Section 3.7 on page 96: Graphing Quadratic Functions with the 5-Point Method.

[TA Sora] Hello everyone! Up until now, we have calculated individual features of parabolas in isolation—the vertex, the intercepts, the axis of symmetry. Today, we assemble all of them into a unified, 5-point blueprint for graphing!

[Prof. Park] Why five points? Two points make a straight line, but a curve requires at least three points to show curvature. And five points give you an airtight, professional sketch that accurately captures the width, vertex, and ground-level intercepts without any guessing!

[TA Sora] Here are our five anchor points: Point 1: The Vertex $(h, k)$—the master anchor. Point 2: The $y$-intercept $(0, c)$. Point 3: The Symmetric Partner of the $y$-intercept, reflected across the axis of symmetry! Points 4 & 5: The two $x$-intercepts $(r_1, 0)$ and $(r_2, 0)$!

[Prof. Park] Open your workbook to page 96. Let's graph our first complete 5-point parabola on Slide 2!""",

    2: """[Prof. Park] On Slide 2, we graph $f(x) = x^2 - 6x + 5$. Let's execute our 5-point protocol!

[TA Sora] Point 1: The Vertex! $a = 1$, $b = -6$, $c = 5$. $x_v = -(-6) / (2 \\cdot 1) = 3$. Plug in $x = 3$: $f(3) = 3^2 - 6(3) + 5 = 9 - 18 + 5 = -4$. Vertex is $(3, -4)$!

[Prof. Park] Point 2: The $y$-intercept! Plug in $x = 0$: $f(0) = 5$, giving $(0, 5)$.

[TA Sora] Point 3: The Symmetric Partner! The axis of symmetry is $x = 3$. The $y$-intercept is 3 units to the left ($0$). So 3 units to the right ($3 + 3 = 6$) must have the exact same height of 5! That gives $(6, 5)$ for free!

[Prof. Park] Points 4 & 5: The $x$-intercepts! Factor $x^2 - 6x + 5 = 0 \\implies (x - 1)(x - 5) = 0 \\implies x = 1$ and $x = 5$. That gives $(1, 0)$ and $(5, 0)$!

[TA Sora] Look at the five points: $(0, 5)$, $(1, 0)$, $(3, -4)$, $(5, 0)$, and $(6, 5)$. Connect them with a smooth U-shaped curve, and your graph is complete!""",

    3: """[Prof. Park] Slide 3 brings us to a downward-opening parabola: $h(x) = -2x^2 + 4x + 6$.

[TA Sora] Point 1: The Vertex! $x_v = -4 / (2(-2)) = -4 / -4 = 1$. Evaluate $h(1) = -2(1)^2 + 4(1) + 6 = -2 + 4 + 6 = 8$. Vertex is $(1, 8)$! Because $a = -2 < 0$, it opens downward.

[Prof. Park] Point 2: The $y$-intercept is $(0, 6)$. Point 3: The axis of symmetry is $x = 1$. The partner point 1 unit to the right is $(2, 6)$!

[TA Sora] Points 4 & 5: $x$-intercepts! Set $-2x^2 + 4x + 6 = 0$. Divide by $-2$: $x^2 - 2x - 3 = 0 \\implies (x - 3)(x + 1) = 0 \\implies x = 3, -1$. Roots are $(-1, 0)$ and $(3, 0)$!

[Prof. Park] Look at that majestic arch on your coordinate grid: $(-1, 0)$, $(0, 6)$, $(1, 8)$, $(2, 6)$, and $(3, 0)$! Perfect five-point symmetry!""",

    4: """[Prof. Park] On Slide 4, we examine $g(x) = x^2 + 2x + 2$. What happens when a parabola has NO $x$-intercepts?

[TA Sora] Let's check the discriminant: $\\Delta = 2^2 - 4(1)(2) = 4 - 8 = -4 < 0$! It has zero real $x$-intercepts! But we still need five points!

[Prof. Park] When there are no $x$-intercepts, we choose smart test points! Point 1: Vertex: $x_v = -2 / 2 = -1$. $g(-1) = (-1)^2 + 2(-1) + 2 = 1$. Vertex is $(-1, 1)$.

[TA Sora] Point 2: $y$-intercept is $(0, 2)$. Point 3: Symmetric partner across $x = -1$ is $(-2, 2)$!

[Prof. Park] Points 4 & 5: Test $x = 1$: $g(1) = 1 + 2 + 2 = 5$, giving $(1, 5)$. Reflect across $x = -1$ (2 units left) to get $(-3, 5)$!

[TA Sora] Five anchor points: $(-3, 5)$, $(-2, 2)$, $(-1, 1)$, $(0, 2)$, and $(1, 5)$! Even without $x$-intercepts, the 5-point method delivers a complete graph!""",

    5: """[Prof. Park] Slide 5 presents $k(x) = -x^2 + 4x - 4$. Here the discriminant is $16 - 16 = 0$. The vertex is $(2, 0)$—a tangent vertex touching the axis at one single point!""",

    6: """[Prof. Park] Slide 6 compares quadratic and linear functions: evaluating $f(x) = x^2 - 6x + 4$ versus $g(x) = 2x - 3$. Linear growth is constant; quadratic growth accelerates!""",

    7: """[Prof. Park] Slide 7 demonstrates function transformations: $f(x + 5)$ shifts the parabola 5 units to the left on the coordinate plane!""",

    8: """[Prof. Park] Slide 8 solves the system $f(x) = g(x)$: finding the two exact intersection points where the straight line cuts through the curved parabola! Complete synthesis!"""
}

SCRIPTS_L45 = {
    1: """[Prof. Park] Welcome to Lecture 45—the final lecture of Unit 3 and the grand capstone of our entire M090 journey!

[TA Sora] Congratulations Bobcats! Today we celebrate everything you have accomplished across 45 lectures of introductory algebra!

[Prof. Park] From the basic grammar of signed numbers in Unit 1, to straight lines in Unit 2, to the curved world of parabolas in Unit 3, you have built genuine mathematical fluency!""",

    2: """[Prof. Park] Slide 2 reviews Domain and Range across all four Section 3.7 functions. The Domain is always $(-\\infty, \\infty)$. The Range is bounded by the vertex $k$: $[k, \\infty)$ if opening upward, or $(-\\infty, k]$ if opening downward!""",

    3: """[Prof. Park] Slide 3 summarizes our 5-Point Graphing Masterclass: Vertex, $y$-intercept, symmetric reflection, and two $x$-intercepts. Always verify symmetry!""",

    4: """[Prof. Park] Slide 4 connects quadratics to real-world physics: projectile motion $h(t) = -16t^2 + v_0 t + h_0$. The vertex gives maximum altitude, and the positive root gives splashdown time!""",

    5: """[Prof. Park] Slide 5 presents the Grand Review of all four solving methods: Square Root Property, Factoring, Completing the Square, and Quadratic Formula. You now command them all!""",

    6: """[Prof. Park] Slide 6 is your M090 Formula Card—keep this forever in your academic career: $x = -b / (2a)$, $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$, and $\\Delta = b^2 - 4ac$!""",

    7: """[Prof. Park] Slide 7 provides final mastery problem solving and reflection on personal growth, persistence, and logical reasoning.""",

    8: """[Prof. Park] Congratulations! You have officially completed M090 Introductory Algebra at Gallatin College Montana State University!

[TA Sora] We are so immensely proud of your hard work, your curiosity, and your resilience. You are ready for College Algebra and beyond. Go Bobcats! 🏔️"""
}
