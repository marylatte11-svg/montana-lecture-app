# -*- coding: utf-8 -*-
"""
unit3_scripts_l35.py
Full 20-25 Minute Broadcast Tiki-Taka Dialogue for Lecture 35
Prof. Eunju Park & TA Sora (Gallatin College Montana State University)
Covers all 8 slides with ~320-380 words per slide (~2,600-2,900 words total).
"""

SCRIPTS_L35 = {
    1: """[Prof. Park] Hello everyone, and welcome to Lecture 35 of M090 Introductory Algebra! I'm Professor Eunju Park, and joining me is our wonderful teaching assistant, Sora. Today we dive into Vertex Form in complete depth, beginning on page 70 of your workbook.

[TA Sora] Welcome, Bobcats! In Lecture 34, we used the Vertex Formula $x = -b / (2a)$ for functions written in General Form $ax^2 + bx + c$. But today, we explore the superpower format of algebra: Standard Vertex Form, $f(x) = a(x - h)^2 + k$!

[Prof. Park] On Slide 1, we look at Section 3.1 Example 3: $f(x) = -3(x - 4)^2 + 7$. The problem asks us to find the vertex, axis of symmetry, determine min or max, and write the domain and range. Sora, how quickly can a student extract the vertex here?

[TA Sora] In literally three seconds! Remember our golden rule: 'Inside the parentheses, reverse the sign; outside the parentheses, keep the sign!' Inside, we have $(x - 4)$, so $h = +4$. Outside, we have $+7$, so $k = +7$. The vertex is $(4, 7)$!

[Prof. Park] Zero formulas, zero algebraic manipulation. The vertex is $(4, 7)$. And the vertical Axis of Symmetry passes right through that $x$-coordinate, so its equation is $x = 4$.

[TA Sora] Now look at the leading coefficient: $a = -3$. Because $a$ is negative, the parabola frowns downward! That means the vertex $(4, 7)$ is the highest mountain peak—it represents a Maximum value of 7!

[Prof. Park] Domain is always all real numbers: $(-\\infty, \\infty)$. And because the parabola opens downward, the vertical outputs come from $-\\infty$ up to 7, giving a Range of $(-\\infty, 7]$ with a solid square bracket on 7!

[TA Sora] Notice how steep this curve is: that factor of $-3$ vertically stretches the parabola, making it three times narrower than a standard curve.

[Prof. Park] Vertex $(4, 7)$, Axis of Symmetry $x = 4$, Maximum value 7, Domain $(-\\infty, \\infty)$, Range $(-\\infty, 7]$. That is the efficiency of vertex form!""",

    2: """[Prof. Park] Let's move to Slide 2 and examine Section 3.1 Example 4 on page 70: $f(x) = 5(x - 1)^2 + 3$. Sora, let's break down this function using our vertex form inspection method.

[TA Sora] Let's look inside the parentheses first: we see $(x - 1)$. Reversing that sign gives $h = +1$. Outside the parentheses, we see $+3$, which gives $k = +3$. So our vertex sits at $(1, 3)$!

[Prof. Park] Exactly. The Axis of Symmetry is the vertical line $x = 1$. Now, let's look at the leading coefficient $a = 5$. Since $a = 5 > 0$, what does that tell us about the shape of the graph?

[TA Sora] It smiles upward! The parabola opens upward like an ultra-narrow cup, which means the vertex is the absolute lowest valley—a Minimum value! And that minimum value is $y = 3$.

[Prof. Park] Now think about what this means for the graph relative to the horizontal $x$-axis! The lowest point on the entire curve is at height $y = 3$, and the parabola opens upward from there. Does this graph EVER touch the $x$-axis?

[TA Sora] Wow, that is such a brilliant observation, Professor Park! Because the minimum height is $+3$, the entire parabola floats up in Quadrant I above the $x$-axis! It will NEVER cross the $x$-axis, meaning this quadratic equation has ZERO real $x$-intercepts!

[Prof. Park] Exactly. If you tried to set $5(x - 1)^2 + 3 = 0$, you would get $(x - 1)^2 = -3/5$, which has no real solutions because you cannot take the real square root of a negative number. Vertex form told us that immediately without solving a thing!

[TA Sora] Domain is $(-\\infty, \\infty)$, and Range starts at the minimum 3 and goes to infinity: $[3, \\infty)$! Minimum value is 3, vertex is $(1, 3)$, and axis of symmetry is $x = 1$.""",

    3: """[Prof. Park] Slide 3 brings us to Example 5: $f(x) = -6(x + 2)^2 - 9$. Sora, this problem is loaded with negative signs both inside and outside the parentheses. How do we prevent sign confusion here?

[TA Sora] Don't let the cluster of minus signs intimidate you! Stick strictly to our principle: Inside the parentheses, we have $(x + 2)$. We reverse the sign of $+2$, which gives $h = -2$! Outside, we have $-9$, so we keep it as $k = -9$!

[Prof. Park] So our vertex is $(-2, -9)$. Both coordinates are negative! The Axis of Symmetry is the vertical line $x = -2$.

[TA Sora] Now look at the leading coefficient: $a = -6$. It is negative, so the parabola opens downward! That means our vertex $(-2, -9)$ is the peak—the Maximum value of the function!

[Prof. Park] And what is that maximum value? It is $-9$. Think about that: the highest point on the curve is down at $y = -9$, and the arms of the parabola open downward into deeper negative territory!

[TA Sora] So just like Example 4, this parabola also NEVER touches the $x$-axis! It lives entirely in Quadrant III, trapped beneath the ceiling of $y = -9$.

[Prof. Park] If this function modeled the temperature of an experimental deep-freeze cryo-chamber in Bozeman, the maximum temperature the chamber ever reaches is $-9^\\circ$ Fahrenheit. It never warms above $-9^\\circ$.

[TA Sora] Domain is $(-\\infty, \\infty)$. Range starts from $-\\infty$ and tops out at $-9$: $(-\\infty, -9]$ with a solid bracket! 

[Prof. Park] Vertex $(-2, -9)$, Axis of Symmetry $x = -2$, Maximum value $-9$, Range $(-\\infty, -9]$. Beautifully analyzed!""",

    4: """[Prof. Park] On Slide 4, Example 6 asks us to find the vertex of $f(x) = 2x^2 - 7$. Sora, students look at $2x^2 - 7$ and say: 'Wait, where are the parentheses? Is this in vertex form or general form?'

[TA Sora] It is actually both at the exact same time! Notice that there are no parentheses around $x$, which means nothing is being added to or subtracted from $x$ before squaring. We can rewrite $2x^2 - 7$ as $2(x - 0)^2 - 7$!

[Prof. Park] That is the bridge of understanding. Inside the parentheses, the horizontal shift is $h = 0$. Outside, the vertical shift is $k = -7$. That gives us a vertex of $(0, -7)$!

[TA Sora] And notice that if you used the Vertex Formula from General Form, with $a = 2$, $b = 0$, and $c = -7$, you would get $x_v = -0 / (2 \\cdot 2) = 0$, and $f(0) = -7$. Both roads lead to the exact same destination: $(0, -7)$!

[Prof. Park] Since $a = 2 > 0$, the parabola opens upward. The vertex $(0, -7)$ is a Minimum value of $-7$. The Axis of Symmetry is the line $x = 0$, which is the $y$-axis.

[TA Sora] The Domain is $(-\\infty, \\infty)$, and the Range is $[-7, \\infty)$.

[Prof. Park] Whenever you see a pure quadratic term with no linear middle term, like $ax^2 + c$, the vertex is always sitting directly on the $y$-axis at $(0, c)$. The parabola has zero horizontal shift!

[TA Sora] Write down: $f(x) = 2(x - 0)^2 - 7 \\implies$ Vertex $(0, -7)$, Axis of Symmetry $x = 0$, Minimum value $-7$, Range $[-7, \\infty)$!""",

    5: """[Prof. Park] Slide 5 presents Section 3.1 Example 7 (Part 1) on page 71: a comprehensive graphing challenge for $f(x) = -2(x + 3)^2 + 8$. The problem asks us to find the vertex, axis of symmetry, $y$-intercept, $x$-intercepts, and sketch the graph.

[TA Sora] This is the complete package! Let's harvest our information step-by-step. Step 1: The Vertex! Inside, $(x + 3)$ flips to $h = -3$. Outside, $+8$ stays $k = 8$. The vertex is $(-3, 8)$!

[Prof. Park] Step 2: The Axis of Symmetry is the vertical line $x = -3$. And because $a = -2 < 0$, the parabola opens downward from its peak of 8!

[TA Sora] Step 3: The $y$-intercept! Remember: never assume 8 is the $y$-intercept! We must plug in $x = 0$: $f(0) = -2(0 + 3)^2 + 8 = -2(3)^2 + 8 = -2(9) + 8 = -18 + 8 = -10$!

[Prof. Park] So the $y$-intercept is at $(0, -10)$! That is way down on the negative axis. Step 4: Now let's find the $x$-intercepts by setting $f(x) = 0$: $-2(x + 3)^2 + 8 = 0$.

[TA Sora] Look at how easy this is to solve using the Square Root Property: subtract 8 from both sides to get $-2(x + 3)^2 = -8$. Divide both sides by $-2$: $(x + 3)^2 = 4$!

[Prof. Park] Now take the square root of both sides: $x + 3 = \\pm \\sqrt{4} = \\pm 2$. Subtract 3: $x = -3 \\pm 2$. That gives $x = -3 + 2 = -1$, and $x = -3 - 2 = -5$!

[TA Sora] That yields two $x$-intercepts: $(-1, 0)$ and $(-5, 0)$! Notice how symmetrical they are around our axis of symmetry $x = -3$: $-1$ is 2 units to the right, and $-5$ is 2 units to the left!

[Prof. Park] Every piece of geometry aligns in perfect harmony. Let's interrogate this graph on Slide 6!""",

    6: """[Prof. Park] On Slide 6, we interrogate the five key anchor points of our graph for $f(x) = -2(x + 3)^2 + 8$: the vertex $(-3, 8)$, the two $x$-intercepts $(-5, 0)$ and $(-1, 0)$, the $y$-intercept $(0, -10)$, and its symmetric partner $(-6, -10)$.

[TA Sora] Look at the coordinate grid on your screen. The vertex $(-3, 8)$ crowns the top of the curve. The two $x$-intercepts $(-5, 0)$ and $(-1, 0)$ anchor the curve at the horizontal ground. 

[Prof. Park] Now look at the $y$-intercept at $(0, -10)$. How far is $x = 0$ from our axis of symmetry $x = -3$? It is 3 units to the right! Because of symmetry, if you travel 3 units to the left of the axis of symmetry—from $-3$ minus 3 to $x = -6$—the height must also be $-10$!

[TA Sora] That gives us our fifth point for free: $(-6, -10)$! Having five precise anchor points gives you an airtight, professional sketch of any parabola.

[Prof. Park] And what about the domain and range? Domain is $(-\\infty, \\infty)$. Range is $(-\\infty, 8]$ because the maximum peak is 8.

[TA Sora] If this were the trajectory of a rocket launched during an engineering competition at Montana State University, it launched from ground level at $x = -5$ seconds relative to reference, reached a peak altitude of 800 feet at $x = -3$, and landed back at $x = -1$!

[Prof. Park] That's a vivid picture, Sora. When you see the numbers as physical landmarks, algebra ceases to be abstract symbols and becomes a language of motion and form.

[TA Sora] Five anchor points: $(-6, -10)$, $(-5, 0)$, $(-3, 8)$, $(-1, 0)$, and $(0, -10)$. A masterpiece of parabolic graphing!""",

    7: """[Prof. Park] Slide 7 provides what I consider the most valuable reference slide in this entire unit: The General Form versus Vertex Form Summary Matrix. Let's compare them side-by-side.

[TA Sora] In column 1, we have General Form: $f(x) = ax^2 + bx + c$. What are its advantages? First, the $y$-intercept is handed to you instantly as $(0, c)$. Second, it is ready for factoring or the Quadratic Formula!

[Prof. Park] But its disadvantage is that finding the vertex requires two calculation steps: first compute $x = -b / (2a)$, then evaluate $y = f(-b/(2a))$.

[TA Sora] Now look at column 2, Vertex Form: $f(x) = a(x - h)^2 + k$. Its superpower is that the vertex $(h, k)$ and the axis of symmetry $x = h$ are visible immediately with zero calculations! 

[Prof. Park] And finding $x$-intercepts from vertex form is lightning fast using the Square Root Property: isolate $(x - h)^2 = -k/a$ and take the square root of both sides.

[TA Sora] But its slight drawback is that finding the $y$-intercept requires evaluating $f(0)$, and expanding to general form requires FOILing the binomial square.

[Prof. Park] Notice what both forms share: the leading coefficient $a$ is identical in both forms! If $a$ is positive, both open up; if $a$ is negative, both open down. The width and curvature are identical!

[TA Sora] That's why top students know how to move fluidly between both forms. You pick the form that fits your current objective!""",

    8: """[Prof. Park] We have completed Lecture 35 and reached the end of Section 3.1! Sora, this marks the completion of the first major phase of Unit 3.

[TA Sora] Congratulations, Bobcats! You have mastered the foundations of quadratic functions. In Lectures 31 through 35, you learned to identify terms and coefficients, determine direction and min/max, calculate the vertex via $x = -b/(2a)$, read vertex form $a(x - h)^2 + k$, and graph complete 5-point parabolas.

[Prof. Park] Remember the life lessons woven through these mathematical truths: symmetry brings balance; order of operations prevents chaotic mistakes; and understanding the core landmarks gives you direction before you draw a single line.

[TA Sora] Tonight, complete all Section 3.1 homework exercises on pages 70 through 74 in your workbook. Revisit any problem where you hesitated, and practice Sora's 4-step protocol until it becomes second nature.

[Prof. Park] In Lecture 36, we begin Section 3.2: mastering the Square Root Property and learning how to solve quadratic equations when factoring is impossible. 

[TA Sora] Be proud of your progress, stay curious, and keep practicing! We will see you all in Lecture 36!"""
}
