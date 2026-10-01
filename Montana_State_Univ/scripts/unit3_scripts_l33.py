# -*- coding: utf-8 -*-
"""
unit3_scripts_l33.py
Full 20-25 Minute Broadcast Tiki-Taka Dialogue for Lecture 33
Prof. Eunju Park & TA Sora (Gallatin College Montana State University)
Covers all 8 slides with ~310-380 words per slide (~2,600-2,900 words total).
"""

SCRIPTS_L33 = {
    1: """[Prof. Park] Hello Bobcats, and welcome to Lecture 33 of M090 Introductory Algebra! I'm Professor Eunju Park, and joining me is our teaching assistant, Sora. Today we tackle Section 3.0 Example 7 on page 63 of your workbook—evaluating functions at various inputs.

[TA Sora] Welcome back everyone! Function evaluation is like running a precise calculation program: whatever number or expression is fed into the function machine as the input $x$, it replaces every single instance of $x$ throughout the algebraic formula!

[Prof. Park] On Slide 1, we start with Parts A and B: evaluating two different functions at $x = -1$. The functions given in the workbook are $f(x) = -x^2 + 3x + 8$ and $g(x) = 2x^2 - 7$. Sora, what is our non-negotiable protocol whenever we substitute a negative number?

[TA Sora] The Golden Rule of Sora's Tutoring Desk: 'Protective Parentheses!' Whenever you substitute a negative number like $-1$, wrap it in parentheses before squaring or multiplying! If you don't use parentheses, your signs will collapse like a cheap tent in a Montana blizzard!

[Prof. Park] Let's look at $f(-1)$: $f(-1) = -(-1)^2 + 3(-1) + 8$. Look at the first term: $-(-1)^2$. The negative sign on the outside stays outside! First, square the inside: $(-1)^2 = +1$. Then apply the outside negative sign: $-(1) = -1$.

[TA Sora] Exactly! Then the linear term is $3(-1) = -3$. Adding them up: $-1 - 3 + 8 = -4 + 8 = 4$. So $f(-1) = 4$, which corresponds to the point $(-1, 4)$ on the graph!

[Prof. Park] Now let's calculate $g(-1)$ for $g(x) = 2x^2 - 7$: $g(-1) = 2(-1)^2 - 7$. Order of operations says exponents before multiplication! Square $-1$ first to get $+1$. Then multiply by 2: $2(1) = 2$. Finally, subtract 7: $2 - 7 = -5$!

[TA Sora] So $g(-1) = -5$, giving the point $(-1, -5)$. Notice how protective parentheses kept our signs completely under control in both calculations.

[Prof. Park] Master this habit now, and you will save yourself countless headaches on midterms and finals!""",

    2: """[Prof. Park] Slide 2 brings us to Parts C and D: evaluating at zero, $g(0)$ and $h(0)$, for $g(x) = 2x^2 - 7$ and $h(x) = 4x^2 - 2x + 5$. Sora, why is zero such a beloved number in algebra?

[TA Sora] Because multiplying by zero is the ultimate algebraic shortcut! Any term containing $x$ multiplied by zero simply vanishes into thin air: $a(0)^2 = 0$ and $b(0) = 0$.

[Prof. Park] Let's calculate $g(0)$: $g(0) = 2(0)^2 - 7 = 2(0) - 7 = 0 - 7 = -7$. And look at what that represents geometrically: it is the $y$-intercept of the graph, $(0, -7)$!

[TA Sora] Now let's look at $h(0)$ for $h(x) = 4x^2 - 2x + 5$: $h(0) = 4(0)^2 - 2(0) + 5 = 0 - 0 + 5 = 5$. Again, the output matches the constant term $c = 5$ exactly!

[Prof. Park] This gives us a universal principle: for any polynomial in general form $ax^2 + bx + c$, evaluating at $x = 0$ always yields the constant term $c$. The $y$-intercept is always $(0, c)$!

[TA Sora] Think of this like the baseline calibration of an instrument in a laboratory or agricultural moisture sensor. When all inputs are set to zero, whatever reading remains is your baseline constant.

[Prof. Park] In economics, this is your fixed overhead cost. If you produce zero units ($x = 0$), your variable production costs vanish, and you are left paying your fixed rent and equipment depreciation.

[TA Sora] So write down both answers: $g(0) = -7$ corresponding to $(0, -7)$, and $h(0) = 5$ corresponding to $(0, 5)$. Zero is your fastest path to the vertical intercept!""",

    3: """[Prof. Park] On Slide 3, Part E tests our fraction arithmetic skills: evaluating $h(5/2)$ for $h(x) = 4x^2 - 2x + 5$. Sora, fractions tend to make developmental algebra students anxious. How do we break this down into friendly steps?

[TA Sora] Fractions are just division waiting to happen, and when you follow the order of operations, the numbers actually cooperate beautifully! Let's substitute $5/2$ inside protective parentheses: $h(5/2) = 4(5/2)^2 - 2(5/2) + 5$.

[Prof. Park] Step 1: Exponents first! What is $(5/2)^2$? Square both the numerator and the denominator: $5^2 / 2^2 = 25/4$. So our first term becomes $4 \\cdot (25/4)$.

[TA Sora] And look at the magic right there! The 4 in front cancels with the 4 in the denominator: $4 \\cdot (25/4) = 25$! The fraction completely disappeared!

[Prof. Park] Now look at the second term: $-2 \\cdot (5/2)$. The 2 in front cancels with the 2 in the denominator, leaving $-5$!

[TA Sora] And the constant at the end is $+5$. Look at our entire simplified expression: $25 - 5 + 5$! The $-5$ and $+5$ cancel out to zero, leaving us with a clean integer: $25$!

[Prof. Park] What started out looking like an intimidating fraction calculation simplified down to the integer 25. That gives us the point $(5/2, 25)$ on the parabola.

[TA Sora] This teaches us a crucial lesson: never panic when you see fractions in algebra. The workbook authors often design these problems so that factors cancel cleanly if you follow the correct order of operations!

[Prof. Park] So $h(5/2) = 25$. Write every intermediate step in your workbook: $4(25/4) - 2(5/2) + 5 = 25 - 5 + 5 = 25$!""",

    4: """[Prof. Park] Turning to Slide 4, Part F asks us to evaluate $g(a)$ for the function $g(x) = 2x^2 - 7$. Sora, students often ask: 'Why are we replacing the letter $x$ with another letter $a$? Isn't that just moving letters around?'

[TA Sora] That is such a common question! But in advanced mathematics, physics, and computer programming, we constantly change variable names to represent specific parameters. In coding, you pass an argument to a function; in physics, you might switch from position $x$ to time $t$ or mass $m$.

[Prof. Park] Exactly. The function $g$ is fundamentally a machine that takes whatever is inside the parentheses, squares it, multiplies by 2, and subtracts 7: $g(\\text{input}) = 2(\\text{input})^2 - 7$.

[TA Sora] So when the input is the letter $a$, we simply erase $x$ and replace it with $a$: $g(a) = 2(a)^2 - 7 = 2a^2 - 7$. There is nothing more to calculate or simplify because $a$ is an unknown variable.

[Prof. Park] Think about a CNC milling machine in a manufacturing shop in Kalispell or Billings. The machine follows a set code path: take dimension $x$, square it, double it, cut down by 7. If the customer changes the raw material stock parameter to $a$, the machine simply runs the same code on parameter $a$.

[TA Sora] That's a great analogy. Don't overthink variable substitution: $g(a) = 2a^2 - 7$. It simply recasts the relationship using a new symbol.

[Prof. Park] Make a note on page 63: $g(a) = 2a^2 - 7$. Now let's see what happens when our input is an entire binomial on Slide 5!""",

    5: """[Prof. Park] Slide 5 presents Part G: evaluating $g(x - 6)$ for $g(x) = 2x^2 - 7$. Now the input is not just a single number or letter—it is a two-term binomial, $x - 6$!

[TA Sora] This is where algebraic discipline really counts. We replace the input variable with $(x - 6)$: $g(x - 6) = 2(x - 6)^2 - 7$. And remember our rule from earlier: expand the binomial square BEFORE multiplying by 2!

[Prof. Park] Let's expand $(x - 6)^2$: that means $(x - 6)(x - 6)$. Using FOIL: $x^2 - 6x - 6x + 36 = x^2 - 12x + 36$. Notice that middle term of $-12x$! Never write $x^2 - 36$ or $x^2 + 36$; the middle term is essential.

[TA Sora] Now substitute that back into our expression: $g(x - 6) = 2(x^2 - 12x + 36) - 7$. Distribute the 2 through all three terms: $2x^2 - 24x + 72 - 7$.

[Prof. Park] Finally, combine the constant terms: $72 - 7 = 65$. So our final simplified function is $g(x - 6) = 2x^2 - 24x + 65$!

[TA Sora] What does this transformation mean geometrically? In precalculus and calculus, replacing $x$ with $x - 6$ shifts the entire parabola horizontally 6 units to the right! 

[Prof. Park] That's right. The original vertex was at $(0, -7)$. In our new function $g(x - 6)$, the vertex has shifted 6 units to the right to $(6, -7)$. You can verify that by checking $x_v = -b/(2a) = -(-24)/(2 \\cdot 2) = 24/4 = 6$!

[TA Sora] Wow, that is so beautiful how the algebra and geometry confirm each other. Write it down carefully: $g(x - 6) = 2x^2 - 24x + 65$.""",

    6: """[Prof. Park] On Slide 6, Part H gives us our final evaluation challenge: evaluate $h(k + 1)$ for $h(x) = 4x^2 - 2x + 5$. This problem brings together every skill we have practiced today.

[TA Sora] Let's substitute $(k + 1)$ into every single spot where $x$ appears: $h(k + 1) = 4(k + 1)^2 - 2(k + 1) + 5$. Notice we wrapped $(k + 1)$ in parentheses in both the quadratic term and the linear term!

[Prof. Park] Step 1: Expand $(k + 1)^2$: that is $k^2 + 2k + 1$. Step 2: Distribute 4 across that trinomial: $4(k^2 + 2k + 1) = 4k^2 + 8k + 4$.

[TA Sora] Step 3: Distribute the $-2$ through the linear term: $-2(k + 1) = -2k - 2$. Watch that negative sign carefully! It must distribute to both the $k$ and the $+1$.

[Prof. Park] Now let's assemble all the pieces in a single line: $4k^2 + 8k + 4 - 2k - 2 + 5$. Step 4 is to combine like terms: the quadratic term is $4k^2$. For the linear terms: $8k - 2k = +6k$.

[TA Sora] And for the constants: $4 - 2 + 5 = 2 + 5 = +7$! Putting it all together: $h(k + 1) = 4k^2 + 6k + 7$!

[Prof. Park] Look at how tidy and organized that result is. In engineering, this process is known as a Taylor shift or coordinate re-parameterization. When you shift your origin of measurement by 1 unit, the quadratic equation rebalances itself smoothly.

[TA Sora] If you followed along and got $4k^2 + 6k + 7$, give yourself a high five! You have mastered binomial substitution into quadratic polynomials.""",

    7: """[Prof. Park] Slide 7 addresses what is arguably the #1 sign trap in all of developmental algebra: the difference between $-x^2$ and $(-x)^2$. Sora, how many thousands of times have we seen students trip over this distinction?

[TA Sora] Oh, countless times! Every single semester, on every homework and quiz. Students often think: 'A negative squared is always positive, right?' But without parentheses, the negative is NOT being squared!

[Prof. Park] Let's state the rule in crystal clear terms: $(-x)^2$ means the base is $(-x)$. You multiply $(-x) \\cdot (-x)$, which equals $+x^2$ (positive). The negative is inside the parentheses, so it gets squared.

[TA Sora] But $-x^2$ means $-(x^2)$! According to PEMDAS, exponentiation comes BEFORE negation! So you square $x$ first, and THEN apply the negative sign at the very end. The result is always negative or zero for any real number $x$!

[Prof. Park] Let's test this with a real number: let $x = 3$. $(-3)^2 = (-3) \\cdot (-3) = +9$. But $-3^2 = -(3 \\cdot 3) = -9$! They are opposite numbers!

[TA Sora] And what about a negative input, like $x = -4$? If you calculate $(-x)^2$, you get $(-(-4))^2 = (4)^2 = 16$. But if you calculate $-x^2$, you get $-(-4)^2 = -(16) = -16$!

[Prof. Park] If you plug $-3^2$ into most scientific calculators or Google without parentheses, it will give you $-9$ because the calculator strictly follows the order of operations: exponents first, negation second!

[TA Sora] Write this on a sticky note and put it on your bathroom mirror: $(-x)^2 = +x^2$, but $-x^2 = -x^2$. Protect your base with parentheses every single time!""",

    8: """[Prof. Park] We have reached Slide 8, our Section 3.0 Complete Mastery Summary! This concludes our foundational study of Section 3.0. Sora, what are the core takeaways every M090 student should carry forward?

[TA Sora] First, the General Quadratic Form $f(x) = ax^2 + bx + c$ ($a \\neq 0$) graphs as a parabola. Second, the sign of $a$ controls the direction: $a > 0$ opens upward with a minimum; $a < 0$ opens downward with a maximum.

[Prof. Park] Third, in vertex form $f(x) = a(x - h)^2 + k$, the vertex is $(h, k)$ with the opposite sign on $h$, and the Axis of Symmetry is the vertical line $x = h$. Fourth, the $y$-intercept is always found by evaluating $f(0)$, and $x$-intercepts are found by solving $f(x) = 0$.

[TA Sora] Fifth, the Domain of any quadratic function is always $(-\\infty, \\infty)$, while the Range is bounded by the vertex output $k$. And sixth, when evaluating functions with negative numbers or binomials, ALWAYS use protective parentheses!

[Prof. Park] In mathematics, just like in building a career or personal discipline, small daily habits compound over time. Double-checking your signs, writing clean steps, and organizing terms creates excellence that extends far beyond the classroom.

[TA Sora] You have built a rock-solid foundation in Section 3.0. Tonight, complete all remaining exercises on pages 63 through 66 of your workbook.

[Prof. Park] In Lecture 34, we will introduce Section 3.1 and derive the famous Vertex Formula $x = -b / (2a)$. Congratulations on completing Section 3.0!

[TA Sora] Fantastic work today, Bobcats! See you in Lecture 34!"""
}
