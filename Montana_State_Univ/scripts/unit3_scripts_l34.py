# -*- coding: utf-8 -*-
"""
unit3_scripts_l34.py
Full 20-25 Minute Broadcast Tiki-Taka Dialogue for Lecture 34
Prof. Eunju Park & TA Sora (Gallatin College Montana State University)
Covers all 8 slides with ~320-380 words per slide (~2,600-2,900 words total).
"""

SCRIPTS_L34 = {
    1: """[Prof. Park] Hello everyone, and welcome to Lecture 34 of M090 Introductory Algebra! I'm Professor Eunju Park, and with me is our course teaching assistant, Sora. Today we step into Section 3.1 on page 67 of your workbook—a true turning point in our study of quadratics.

[TA Sora] Welcome back, Bobcats! In Section 3.0, whenever we needed the vertex from general form, we had to find the $x$-intercepts first and take their average. But what happens if a parabola doesn't have nice $x$-intercepts, or what if it floats completely above the $x$-axis and never touches the ground at all?

[Prof. Park] That is the exact dilemma that mathematicians faced centuries ago. We needed a universal, foolproof formula that extracts the vertex directly from the coefficients $a$, $b$, and $c$, without needing any intercepts! And that formula is the celebrated Vertex Formula: $x_v = -\\frac{b}{2a}$.

[TA Sora] Memorize this formula, tattoo it on your mental chalkboard, write it in gold ink: $x = -b / (2a)$! That tiny fraction gives you the horizontal coordinate of the vertex every single time, guaranteed!

[Prof. Park] And once you have that $x$-value, finding the corresponding vertical height $y_v$ is as simple as plugging $x_v$ right back into the function: $y_v = f(x_v) = f(-b/(2a))$. Together, the ordered pair is $(x_v, y_v)$.

[TA Sora] Think about real-world optimization in Montana. If you are an agricultural manager monitoring a center-pivot irrigation system, or an architect calculating the optimal crown slope of a highway to prevent rainwater pooling, the highest or lowest point is where efficiency happens. The vertex formula takes you straight to that critical point in two lines of math!

[Prof. Park] Look at Slide 1: General Form $f(x) = ax^2 + bx + c$. The $x$-coordinate of the vertex is $x = -b/(2a)$. The vertical Axis of Symmetry is the equation $x = -b/(2a)$. 

[TA Sora] Keep your workbook open to page 67. Let's apply this power on our first official workbook problem on Slide 2!""",

    2: """[Prof. Park] Slide 2 presents Section 3.1 Example 1 from page 67: For the quadratic function $f(x) = x^2 + 6x - 7$, find the vertex, the axis of symmetry, determine whether it has a minimum or maximum, and state the domain and range.

[TA Sora] Let's follow our step-by-step protocol. Step 1: Identify the coefficients $a$, $b$, and $c$. Here, $a = 1$, $b = 6$, and $c = -7$. Make sure you write those three numbers down explicitly!

[Prof. Park] Step 2: Apply the Vertex Formula for $x$: $x_v = -\\frac{b}{2a} = -\\frac{6}{2(1)} = -\\frac{6}{2} = -3$. Look at how clean that calculation was: $x_v = -3$!

[TA Sora] Step 3: Find the $y$-value by evaluating $f(-3)$. Remember Sora's rule from Lecture 33: protective parentheses around $-3$! $f(-3) = (-3)^2 + 6(-3) - 7$.

[Prof. Park] Let's calculate carefully: $(-3)^2 = +9$. Then $6(-3) = -18$. Finally, $-7$. So we have $9 - 18 - 7 = -9 - 7 = -16$! So the vertical coordinate is $y_v = -16$.

[TA Sora] That gives us the complete vertex: $(-3, -16)$! And immediately, the Axis of Symmetry is the vertical line passing through $x = -3$: the equation is $x = -3$.

[Prof. Park] Now let's examine min/max and range. The leading coefficient is $a = 1 > 0$, so the parabola opens upward like a cup. That means the vertex sits at the bottom—it is a Minimum value! And that minimum value is $-16$.

[TA Sora] For the Domain, it is always all real numbers: $(-\\infty, \\infty)$. For the Range, the outputs start at the minimum $-16$ and go up to infinity: $[-16, \\infty)$, with a solid square bracket on $-16$!

[Prof. Park] Look at how seamlessly everything locked into place: Vertex $(-3, -16)$, Axis of Symmetry $x = -3$, Minimum value $-16$, Domain $(-\\infty, \\infty)$, Range $[-16, \\infty)$. Complete mastery!""",

    3: """[Prof. Park] Turning to Slide 3, Section 3.1 Example 2 gives us a function with a fraction coefficient: $f(x) = -\\frac{1}{2}x^2 + 2x + 3$. Sora, students see that fraction $-\\frac{1}{2}$ and immediately brace for impact. How do we guide them through this?

[TA Sora] Take a deep breath! When you multiply a fraction by 2 in the denominator, something wonderful often happens. Let's write out our coefficients first: $a = -\\frac{1}{2}$, $b = 2$, and $c = 3$.

[Prof. Park] Now apply the Vertex Formula: $x_v = -\\frac{b}{2a} = -\\frac{2}{2(-1/2)}$. Look at that denominator: $2 \\cdot (-1/2) = -1$! The fraction completely vanished!

[TA Sora] Wow! So we have $x_v = -\\frac{2}{-1} = -(-2) = +2$! Look at that: $x_v$ turned out to be a positive integer, $+2$!

[Prof. Park] That is why you should never run from fractions. Now Step 3: find $y_v$ by calculating $f(2)$: $f(2) = -\\frac{1}{2}(2)^2 + 2(2) + 3$. Square the 2 first: $2^2 = 4$. Half of 4 is 2, with the negative sign outside: $-\\frac{1}{2}(4) = -2$.

[TA Sora] Then $2(2) = 4$, and the constant is $+3$. Combine them: $-2 + 4 + 3 = 2 + 3 = 5$! So $y_v = 5$, giving us a vertex at $(2, 5)$!

[Prof. Park] And what about the direction? The leading coefficient $a = -\\frac{1}{2}$ is negative ($a < 0$), so the parabola opens downward! That means our vertex $(2, 5)$ is the peak—a Maximum value of 5!

[TA Sora] Axis of Symmetry is the vertical line $x = 2$. Domain is $(-\\infty, \\infty)$. And because it opens downward, the Range comes from negative infinity up to 5: $(-\\infty, 5]$!

[Prof. Park] If you are modeling projectile motion—say, launching a flare into the night sky in Yellowstone—the flare reaches a maximum height of 5 units at time 2. 

[TA Sora] Everything worked out to clean integers. Vertex $(2, 5)$, Axis of Symmetry $x = 2$, Max value 5, Range $(-\\infty, 5]$. Beautiful!""",

    4: """[Prof. Park] On Slide 4, we pause to ask a deeper question: Why does $x = -b / (2a)$ work? In mathematics, we don't just memorize formulas like magical incantations; we understand their architectural origin!

[TA Sora] I love this derivation so much. Think back to Section 3.0: we proved that because of symmetry, the vertex is always the exact midpoint between the two roots or $x$-intercepts!

[Prof. Park] Exactly. Now, consider the celebrated Quadratic Formula, which gives the two roots: $x = \\frac{-b + \\sqrt{b^2 - 4ac}}{2a}$ and $x = \\frac{-b - \\sqrt{b^2 - 4ac}}{2a}$. Notice how both roots share the common base $-\\frac{b}{2a}$, and then add or subtract that radical deviation $\\frac{\\sqrt{b^2 - 4ac}}{2a}$!

[TA Sora] Look at that! The two roots are located at $-\\frac{b}{2a} + \\text{distance}$ and $-\\frac{b}{2a} - \\text{distance}$! If you take the average of those two numbers—adding them together and dividing by 2—the positive and negative square root parts cancel out completely!

[Prof. Park] What is left behind? Exactly $-\\frac{b}{2a}$! The vertex formula is literally the center anchor around which the two symmetric roots branch outward!

[TA Sora] And here is the profound beauty: even when a parabola floats above the $x$-axis and has NO real roots—meaning $b^2 - 4ac < 0$—that center anchor $-\\frac{b}{2a}$ still exists in the real numbers! The roots might become imaginary, but the physical vertex and its axis of symmetry remain 100% real and visible on your graph!

[Prof. Park] That is why $x = -b / (2a)$ works for every single quadratic function in existence. It is the geometric heartbeat of the parabola.

[TA Sora] Understanding the 'why' transforms math from a burden into an art form. Keep that midpoint image in your mind whenever you write $-b / (2a)$!""",

    5: """[Prof. Park] Slide 5 brings us to 'Sora's Protocol for Finding the Vertex & Max/Min.' When you sit down for an exam or work through difficult engineering problems, having a checklist eliminates anxiety.

[TA Sora] Here is my four-step protocol: Step 1 is the 'Sign & Coefficient Scan.' Write down $a$, $b$, and $c$. Immediately check the sign of $a$: if $a > 0$, draw a little smiling U (opens up, minimum). If $a < 0$, draw an upside-down U (opens down, maximum).

[Prof. Park] That two-second scan instantly anchors your expectations. Step 2 is the 'Vertex Formula Execution': write $x_v = -b / (2a)$. Substitute carefully with parentheses, simplify the denominator first, and reduce the fraction.

[TA Sora] Step 3 is the 'Plug-In Evaluation': calculate $y_v = f(x_v)$. Use protective parentheses around $x_v$, especially if $x_v$ is negative! Compute powers first, then multiplications, then additions and subtractions. Write down your vertex as an ordered pair $(x_v, y_v)$.

[Prof. Park] And Step 4 is the 'Summary Packaging': write the Axis of Symmetry as the line equation $x = x_v$. State the max or min value as $y_v$. Write the Domain as $(-\\infty, \\infty)$, and assemble the Range: $[y_v, \\infty)$ if opening up, or $(-\\infty, y_v]$ if opening down.

[TA Sora] Think of this protocol like a pre-flight checklist for an aviation mechanic at Gallatin College. You don't skip steps or rely on memory; you follow the checklist, and you land safely every single time!

[Prof. Park] Let's put this protocol to the test on Slide 6 with a comprehensive challenge problem!""",

    6: """[Prof. Park] On Slide 6, we have a 'Check Your Understanding' problem: Find the vertex, axis of symmetry, max/min value, and range for $f(x) = -2x^2 + 8x - 3$. Sora, let's walk through our four-step protocol together!

[TA Sora] Step 1: Sign & Coefficient Scan! $a = -2$, $b = 8$, and $c = -3$. Because $a = -2 < 0$, the parabola opens downward! I immediately draw an upside-down U: we are dealing with a Maximum!

[Prof. Park] Step 2: The Vertex Formula! $x_v = -\\frac{b}{2a} = -\\frac{8}{2(-2)} = -\\frac{8}{-4} = +2$. The horizontal coordinate is $+2$!

[TA Sora] Step 3: Plug-In Evaluation for $y_v$! $f(2) = -2(2)^2 + 8(2) - 3$. Order of operations: $2^2 = 4$. Then $-2(4) = -8$. For the linear term: $8(2) = +16$. And constant: $-3$.

[Prof. Park] Adding them up: $-8 + 16 - 3 = 8 - 3 = 5$! So $y_v = 5$, and our vertex is $(2, 5)$!

[TA Sora] Step 4: Summary Packaging! Axis of symmetry: the vertical line $x = 2$. Maximum value: 5 (reached at $x = 2$). Domain: $(-\\infty, \\infty)$. Range: since it opens downward, $(-\\infty, 5]$!

[Prof. Park] Now let's connect this to real-world business economics. Imagine $f(x)$ models the net profit in thousands of dollars for a local Bozeman bakery producing $x$ hundred specialty artisan sourdough loaves per week.

[TA Sora] Yes! The vertex $(2, 5)$ tells the bakery owner: 'If you bake 200 loaves per week ($x = 2$), you achieve your absolute maximum profit of $5,000 ($y = 5$)!' If you bake fewer loaves, you leave profit on the table; if you bake more, excess flour costs and unsold bread drag your profits down!

[Prof. Park] The vertex is the optimal sweet spot. That's the real power of algebra in decision-making!""",

    7: """[Prof. Park] Let's look at Slide 7: Visualizing the Vertex & Symmetry on the Coordinate Grid. Take a look at the graph plotted on your screen. The vertex $(2, 5)$ sits at the highest peak, glowing with a golden marker.

[TA Sora] Notice that vertical dashed line running through $x = 2$. That is our Axis of Symmetry. Look at the two points on either side at height $y = 3$: to the left, when $x = 1$, $f(1) = -2(1)^2 + 8(1) - 3 = 3$, giving $(1, 3)$. To the right, when $x = 3$, $f(3) = -2(9) + 24 - 3 = 3$, giving $(3, 3)$!

[Prof. Park] Both points are exactly 1 unit away from the axis of symmetry ($2 - 1 = 1$ and $2 + 1 = 3$), and both sit at the exact same height of $y = 3$! That balance is the defining feature of a parabola.

[TA Sora] Now look 2 units away from the axis of symmetry: to the left at $x = 0$, the $y$-intercept is $(0, -3)$. If you travel 2 units to the right of the symmetry line to $x = 4$, $f(4)$ also equals $-3$, giving the symmetric point $(4, -3)$!

[Prof. Park] This gives you a fast and elegant way to graph parabolas without a calculator: once you find the vertex and the $y$-intercept on the left, you can reflect that point across the axis of symmetry to get a free third point on the right!

[TA Sora] I love free points in math! If $(0, -3)$ is 2 units to the left of $x = 2$, then 2 units to the right at $x = 4$ must also have $y = -3$. You connect those points with a smooth curve, and your graph is complete.

[Prof. Park] Never sketch a parabola with sharp, V-shaped corners. A parabola is smooth and rounded at its vertex, like the bottom of a canoe floating on Flathead Lake.

[TA Sora] Symmetry is your best friend when graphing. Use it to check your calculations and save time!""",

    8: """[Prof. Park] We have reached the final slide of Lecture 34—our Section 3.1 Part 1 Mastery Summary! Sora, let's summarize the key breakthroughs from today's session.

[TA Sora] The #1 star of today's lecture was the Vertex Formula: $x_v = -b / (2a)$. It works on every single quadratic function in general form, regardless of whether the intercepts are pretty, messy, or nonexistent!

[Prof. Park] We learned that the vertical line $x = -b / (2a)$ is the Axis of Symmetry. We learned that substituting $x_v$ back into the function gives the vertical coordinate $y_v = f(x_v)$, producing the complete vertex $(x_v, y_v)$.

[TA Sora] We reinforced that the sign of $a$ dictates the curve: if $a > 0$, the parabola smiles upward with a minimum value of $y_v$, and Range $[y_v, \\infty)$. If $a < 0$, it opens downward with a maximum value of $y_v$, and Range $(-\\infty, y_v]$.

[Prof. Park] We discovered that the vertex formula is fundamentally the center midpoint of the quadratic formula's roots, explaining why symmetry is embedded in the very DNA of quadratic algebra.

[TA Sora] And we applied this to real-world economics and optimization: finding the maximum profit for a business, the optimal launch height for a projectile, or the lowest point of sag in an electrical transmission cable across the Montana plains.

[Prof. Park] To all our students: you are mastering tools that empower you to think logically, systematically, and analytically. Tonight, complete the Section 3.1 practice problems on pages 67 through 69 of your workbook.

[TA Sora] In Lecture 35, we will explore Vertex Form $f(x) = a(x - h)^2 + k$ in full depth and compare it side-by-side with General Form. 

[Prof. Park] Thank you for your wonderful energy and focus today. 

[TA Sora] Keep shining, Bobcats! We will see you in Lecture 35!"""
}
