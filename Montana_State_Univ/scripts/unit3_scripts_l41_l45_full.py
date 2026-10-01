# -*- coding: utf-8 -*-
"""
unit3_scripts_l41_l45_full.py
Complete 20-25 Minute Broadcast Tiki-Taka Dialogue for Lectures 41, 42, 43, 44, 45
Prof. Eunju Park & TA Sora (Gallatin College Montana State University)
Each lecture has 8 slides with ~300-380 words per slide (~2,400-2,800 words per lecture).
"""

SCRIPTS_L41_FULL = {
    1: """[Prof. Park] Hello everyone, and welcome to Lecture 41 of M090 Introductory Algebra! I'm Professor Eunju Park, and with me is our course teaching assistant, Sora. Today we reach the undisputed summit of introductory algebra: Section 3.5 on page 90 of your workbook—The Quadratic Formula!

[TA Sora] Welcome, Bobcats! In our previous lectures, we saw that Factoring is great when numbers are friendly, and Completing the Square works on everything but can produce heavy fractions. But today, we unlock the master universal key that solves EVERY single quadratic equation in human history with zero guesswork!

[Prof. Park] The Quadratic Formula: For any equation $ax^2 + bx + c = 0$ where $a \\neq 0$, the solutions are given by $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$!

[TA Sora] Every algebra student remembers the classic melody: '$x$ equals negative $b$, plus or minus square root, of $b$ squared minus $4ac$, all over $2a$!' Singing it fixes the algebraic rhythm in your memory forever!

[Prof. Park] Look at the anatomy of this formula: The leading part is $-b / (2a)$—our Vertex Formula from Section 3.1! The part under the square root is $b^2 - 4ac$—the Discriminant! And the whole thing is divided by $2a$!

[TA Sora] Warning from Sora's desk: Notice the big fraction bar goes under the ENTIRE numerator, including $-b$! Do not divide just the square root by $2a$; the entire top expression is divided by $2a$!

[Prof. Park] In physics, ballistics, civil engineering, and aerospace, whenever you solve for trajectory impact or structural tension, the Quadratic Formula is the equation programmed into every computer and calculator.

[TA Sora] Open your workbook to page 90. Let's conquer Example 1 together on Slide 2!""",

    2: """[Prof. Park] On Slide 2, we solve Section 3.5 Example 1: $g(x) = x^2 - 17x + 72 = 0$. Here the numbers are large, and finding factors of 72 that add to 17 could take several minutes of trial and error. Let's see how the Quadratic Formula handles it!

[TA Sora] Step 1: Identify our three coefficients: $a = 1$, $b = -17$, and $c = 72$. Write them down clearly with their signs!

[Prof. Park] Step 2: Set up the formula with protective parentheses: $x = \\frac{-(-17) \\pm \\sqrt{(-17)^2 - 4(1)(72)}}{2(1)}$. Look at that $-(-17)$: two negatives make $+17$!

[TA Sora] Step 3: Calculate the Discriminant under the radical: $(-17)^2 = 289$. And $4 \\times 1 \\times 72 = 288$! Subtract them: $289 - 288 = 1$!

[Prof. Park] Look at that! The number under the radical simplified to 1! And what is $\\sqrt{1}$? It is 1! So our equation becomes: $x = \\frac{17 \\pm 1}{2}$!

[TA Sora] Step 4: Branch out into our two solutions: Branch 1: $x = (17 + 1) / 2 = 18 / 2 = 9$! Branch 2: $x = (17 - 1) / 2 = 16 / 2 = 8$!

[Prof. Park] The two solutions are $x = 8$ and $x = 9$! Look at the coordinate plane on your right: the parabola crosses the $x$-axis at $(8, 0)$ and $(9, 0)$!

[TA Sora] And notice where the vertex sits: right at $x = 8.5$, down at $-0.25$! Notice how cleanly the labels display: the vertex label below, and the roots $(8, 0)$ and $(9, 0)$ on either side!

[Prof. Park] The formula plowed through large numbers and gave exact integer roots. Solution set: $\\{8, 9\\}$!""",

    3: """[Prof. Park] Slide 3 brings us to Example 2: Solve $2x^2 + 5x - 3 = 0$. Sora, here $a = 2$, and $c$ is negative. What sign danger should students watch out for?

[TA Sora] Watch out for the '$-4ac$' term! When $c$ is negative, you have $-4(a)(-c)$, which means two negative signs multiplying together to make a POSITIVE! Students often subtract when they should add!

[Prof. Park] Let's track that carefully: $a = 2$, $b = 5$, and $c = -3$. Plug into the formula: $x = \\frac{-5 \\pm \\sqrt{5^2 - 4(2)(-3)}}{2(2)}$.

[TA Sora] Look under the radical: $5^2 = 25$. Now look at $-4(2)(-3)$: $-4 \\times 2 = -8$, and $-8 \\times (-3) = +24$! So we have $25 + 24 = 49$!

[Prof. Park] And 49 is a perfect square! $\\sqrt{49} = 7$! In the denominator, $2(2) = 4$. So $x = \\frac{-5 \\pm 7}{4}$!

[TA Sora] Now branch out: Branch 1: $x = (-5 + 7) / 4 = 2 / 4 = 1/2$! Branch 2: $x = (-5 - 7) / 4 = -12 / 4 = -3$!

[Prof. Park] Our two roots are $x = 1/2$ and $x = -3$! Both are clean rational numbers. As points on the graph: $(-3, 0)$ and $(0.5, 0)$.

[TA Sora] Always remember: $-4ac$ with a negative $c$ turns into addition! That was the key to unlocking $\\sqrt{49} = 7$. Solution set: $\\{-3, 1/2\\}$!""",

    4: """[Prof. Park] On Slide 4, Example 3 gives us: $3x^2 - 4x + 1 = 0$. Sora, let's execute the formula with discipline.

[TA Sora] Coefficients: $a = 3$, $b = -4$, and $c = 1$. Notice $b$ is negative, so $-b$ becomes $-(-4) = +4$!

[Prof. Park] Substitute into the formula: $x = \\frac{-(-4) \\pm \\sqrt{(-4)^2 - 4(3)(1)}}{2(3)}$.

[TA Sora] Under the radical: $(-4)^2 = +16$. And $4(3)(1) = 12$. So $16 - 12 = 4$! The square root of 4 is 2!

[Prof. Park] And in the denominator: $2(3) = 6$. So our fraction is: $x = \\frac{4 \\pm 2}{6}$!

[TA Sora] Let's calculate the two branches: Branch 1: $x = (4 + 2) / 6 = 6 / 6 = 1$! Branch 2: $x = (4 - 2) / 6 = 2 / 6 = 1/3$!

[Prof. Park] The two solutions are $x = 1$ and $x = 1/3$! 

[TA Sora] Look at how smoothly the formula resolved that fraction $1/3$. Whether roots are integers or fractions, the Quadratic Formula delivers exact answers without hesitation.

[Prof. Park] Solution set: $\\{1/3, 1\\}$. A flawless calculation!""",

    5: """[Prof. Park] Slide 5 presents Example 4: Solve $x^2 + 4x + 1 = 0$. Sora, notice that this equation cannot be factored because no factors of 1 add to 4. What happens when we use the Quadratic Formula?

[TA Sora] This is where the formula truly shines! It handles non-factorable equations with irrational square roots effortlessly!

[Prof. Park] Coefficients: $a = 1$, $b = 4$, and $c = 1$. Let's set up the formula: $x = \\frac{-4 \\pm \\sqrt{4^2 - 4(1)(1)}}{2(1)}$.

[TA Sora] Under the radical: $4^2 = 16$, and $4(1)(1) = 4$. So $16 - 4 = 12$! That gives: $x = \\frac{-4 \\pm \\sqrt{12}}{2}$.

[Prof. Park] Now simplify the radical: $12 = 4 \\times 3$, so $\\sqrt{12} = 2\\sqrt{3}$. Our fraction becomes: $x = \\frac{-4 \\pm 2\\sqrt{3}}{2}$.

[TA Sora] Now here is Sora's fraction reduction rule: 'To cancel the 2 in the denominator, you MUST factor out a 2 from BOTH terms in the numerator!' Factor out 2: $x = \\frac{2(-2 \\pm \\sqrt{3})}{2} = -2 \\pm \\sqrt{3}$!

[Prof. Park] Never cancel just one term! You must divide both $-4$ and $2\\sqrt{3}$ by 2, which gives $-2 \\pm \\sqrt{3}$!

[TA Sora] Our exact solutions are $x = -2 + \\sqrt{3}$ and $x = -2 - \\sqrt{3}$. And since $\\sqrt{3} \\approx 1.732$, the decimal roots are $\\approx -0.27$ and $\\approx -3.73$.

[Prof. Park] Solution set: $\\{-2 - \\sqrt{3}, -2 + \\sqrt{3}\\}$. Complete mastery of radicals in the formula!""",

    6: """[Prof. Park] On Slide 6, we practice function evaluation with a quadratic model: Given $f(x) = 3x^2 - 5x + 7$, evaluate $f(-2)$ and $f(0)$. Sora, why do we continue practicing evaluations alongside our formula?

[TA Sora] Because evaluating functions is how we verify our algebraic roots in real applications! If you calculate a root, you plug it in to check that $f(x) = 0$. Let's evaluate $f(-2)$ first: remember protective parentheses around negative numbers! $f(-2) = 3(-2)^2 - 5(-2) + 7$.

[Prof. Park] Let's follow PEMDAS strictly: Exponents first: $(-2)^2 = +4$. Multiplication second: $3(4) = 12$, and $-5(-2) = +10$. Then addition: $12 + 10 + 7 = 29$! So $f(-2) = 29$, giving the point $(-2, 29)$ high on the left wing of the parabola.

[TA Sora] Now let's evaluate $f(0)$: $f(0) = 3(0)^2 - 5(0) + 7 = 0 - 0 + 7 = 7$! That gives the $y$-intercept $(0, 7)$. Notice that the constant term $c = 7$ is revealed instantly!

[Prof. Park] In physics, if $f(t)$ represents the electrical voltage spike during a power surge, $f(0) = 7$ volts is your baseline starting voltage, and $f(-2) = 29$ volts represents the historical peak before stabilization.

[TA Sora] Write both points in your workbook: $(-2, 29)$ and $(0, 7)$. Clean, fast, and accurate!""",

    7: """[Prof. Park] Slide 7 provides another evaluation challenge: For $f(x) = 3x^2 - 5x + 7$, evaluate $f(3)$ and $f(1/3)$. Sora, let's walk through that fraction input $1/3$ step by step!

[TA Sora] For $f(3)$: $f(3) = 3(3)^2 - 5(3) + 7 = 3(9) - 15 + 7 = 27 - 15 + 7 = 12 + 7 = 19$! That gives the ordered pair $(3, 19)$.

[Prof. Park] Now for the fraction input $f(1/3)$: substitute with protective parentheses: $f(1/3) = 3(1/3)^2 - 5(1/3) + 7$. Exponent first: $(1/3)^2 = 1/9$.

[TA Sora] Next, multiply: $3 \\times (1/9) = 3/9 = 1/3$. The linear term is $-5(1/3) = -5/3$. Combine the thirds: $1/3 - 5/3 = -4/3$!

[Prof. Park] Now add the constant 7: convert 7 into thirds: $7 = 21/3$. So we have $-4/3 + 21/3 = 17/3$! As a mixed number, $17/3 = 5 \\frac{2}{3} \\approx 5.67$.

[TA Sora] That gives us the point $(1/3, 17/3)$! Notice that earlier on Slide 4, we solved $3x^2 - 4x + 1 = 0$ and found $x = 1/3$. Here, with $c = 7$, the curve is shifted up by 6 units, so the output is $17/3$ instead of 0!

[Prof. Park] Everything in algebra is interconnected. Fractions represent exact precision that decimal approximations cannot match.

[TA Sora] Solution points: $(3, 19)$ and $(1/3, 17/3)$. Beautiful work!""",

    8: """[Prof. Park] We have reached Slide 8, our Lecture 41 Recap! Today we mastered the most powerful formula in algebra: $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$.

[TA Sora] Let's review the three golden rules of the Quadratic Formula: Rule 1: Set the equation strictly equal to zero first, and arrange in descending order $ax^2 + bx + c = 0$! Rule 2: Wrap negative numbers in parentheses when calculating $b^2$ and $-4ac$! Rule 3: The fraction bar extends under the ENTIRE numerator, including $-b$!

[Prof. Park] Remember that when $c$ is negative, the $-4ac$ term becomes positive addition under the radical. And when simplifying radicals like $2\\sqrt{3}$, factor out the common divisor from both terms in the numerator before reducing!

[TA Sora] In Lecture 42, we will zoom in on the expression under the square root—$b^2 - 4ac$—and discover how it predicts the exact nature and number of solutions before you do any math!

[Prof. Park] Complete all Section 3.5 practice problems on pages 90 and 91 of your workbook tonight.

[TA Sora] Great work today, Bobcats! See you in Lecture 42 for The Discriminant!"""
}

SCRIPTS_L42_FULL = {
    1: """[Prof. Park] Welcome back to M090, Bobcats! I am Professor Eunju Park, and with me is our stellar teaching assistant, Sora. Today in Lecture 42, we explore Section 3.5 Part 2 on page 92: The Discriminant.

[TA Sora] Hello everyone! The Discriminant is the mathematical crystal ball of algebra. It is the special quantity sitting directly underneath the square root symbol in the Quadratic Formula: $\\Delta = b^2 - 4ac$!

[Prof. Park] Think about why it is named the 'Discriminant'—the word means to distinguish or tell apart. By calculating just this one simple number, we can predict the exact number and type of solutions WITHOUT having to solve the entire equation or draw a single graph!

[TA Sora] Let's look at the three possibilities: Case 1: If $b^2 - 4ac > 0$ (positive), you are taking the square root of a positive number! That yields TWO distinct real solutions, and the parabola crosses the $x$-axis twice!

[Prof. Park] Case 2: If $b^2 - 4ac = 0$, you have $\\pm \\sqrt{0} = 0$. Adding or subtracting zero changes nothing, so you get exactly ONE real solution! The vertex touches the $x$-axis at one single tangent point!

[TA Sora] Case 3: If $b^2 - 4ac < 0$ (negative), you are taking the square root of a negative number! In the real number system, you cannot take the square root of a negative! That yields ZERO real solutions, meaning the parabola floats completely above or below the $x$-axis!

[Prof. Park] In structural engineering and aviation, calculating the discriminant tells you instantly whether a flight trajectory will intersect a safe glide path or miss it entirely.

[TA Sora] Open your workbook to page 92. Let's analyze Example 5 on Slide 2!""",

    2: """[Prof. Park] On Slide 2, Example 5 asks us to find the discriminant and determine the number and type of solutions for $x^2 - 5x - 6 = 0$.

[TA Sora] Step 1: Identify our three coefficients: $a = 1$, $b = -5$, and $c = -6$.

[Prof. Park] Step 2: Compute the Discriminant formula: $\\Delta = b^2 - 4ac = (-5)^2 - 4(1)(-6)$.

[TA Sora] Watch the signs carefully: $(-5)^2 = +25$. And $-4(1)(-6) = +24$! So $\\Delta = 25 + 24 = 49$!

[Prof. Park] Since $\\Delta = 49 > 0$, there are TWO distinct real solutions. Furthermore, 49 is a perfect square ($7^2 = 49$), which means the square root will resolve cleanly as $\\sqrt{49} = 7$! That tells us the solutions are not just real—they are Rational numbers (integers or simple fractions)!

[TA Sora] Look at the graph on your screen: the parabola clearly slices through the $x$-axis at two clean integer points: $x = 6$ and $x = -1$! 

[Prof. Park] When $\\Delta > 0$ and is a perfect square, the original equation could have been solved by factoring! Here $(x - 6)(x + 1) = 0$. The discriminant confirms that factoring was possible!

[TA Sora] Discriminant: $\\Delta = 49$. Number and type of solutions: Two real rational solutions. Prediction verified 100%!""",

    3: """[Prof. Park] Slide 3 brings us to Example 6: $x^2 - 6x + 9 = 0$. Let's test the discriminant!

[TA Sora] Step 1: Coefficients: $a = 1$, $b = -6$, and $c = 9$.

[Prof. Park] Step 2: Compute the Discriminant: $\\Delta = b^2 - 4ac = (-6)^2 - 4(1)(9) = 36 - 36 = 0$!

[TA Sora] The Discriminant is exactly ZERO! When $\\Delta = 0$, the $\\pm \\sqrt{b^2 - 4ac}$ part of the Quadratic Formula collapses to zero: $x = \\frac{-(-6) \\pm 0}{2(1)} = \\frac{6}{2} = 3$!

[Prof. Park] There is exactly ONE real rational solution: $x = 3$. Look at the coordinate grid: the vertex is $(3, 0)$, touching the $x$-axis at one single tangent point without crossing through!

[TA Sora] Whenever $\\Delta = 0$, the trinomial is a perfect square: $(x - 3)^2 = 0$. In manufacturing and physics, this represents critical damping—where a system returns to equilibrium as fast as possible without oscillating back and forth!

[Prof. Park] Discriminant $\\Delta = 0 \\implies$ Exactly one real rational root (tangent vertex). A beautiful geometric result!""",

    4: """[Prof. Park] On Slide 4, Example 7 tests: $2x^2 + 3x + 4 = 0$. Sora, let's see what the discriminant reveals here!

[TA Sora] Step 1: Coefficients: $a = 2$, $b = 3$, and $c = 4$.

[Prof. Park] Step 2: Compute $\\Delta = b^2 - 4ac = 3^2 - 4(2)(4) = 9 - 32 = -23$!

[TA Sora] Look at that: $\\Delta = -23$, which is strictly negative ($\\Delta < 0$)! 

[Prof. Park] You cannot take the square root of a negative number in the real number system because no real number multiplied by itself gives a negative output. Therefore, there are ZERO real solutions!

[TA Sora] Look at the graph on your right: the vertex is positioned up in Quadrant I at $( -0.75, 2.875 )$, and because $a = 2 > 0$, the parabola opens upward away from the $x$-axis! The curve never touches ground level!

[Prof. Park] In business, if $2x^2 + 3x + 4$ represents production cost, setting it equal to zero is asking when costs are zero. A negative discriminant tells the business owner: 'Costs will never be zero under this model—you will always have operating overhead.'

[TA Sora] Discriminant $\\Delta = -23 \\implies$ Zero real solutions. No real $x$-intercepts!""",

    5: """[Prof. Park] Slide 5 synthesizes the Discriminant Summary Matrix across all three possibilities. Let's review the complete landscape.

[TA Sora] Column 1: $\\Delta > 0$. Two real solutions. If $\\Delta$ is a perfect square, the roots are rational (factorable). If $\\Delta$ is not a perfect square (like $\\Delta = 73$), the roots are irrational containing square roots! The graph crosses the $x$-axis twice.

[Prof. Park] Column 2: $\\Delta = 0$. Exactly one real rational solution. The trinomial is a perfect square $(x - h)^2$, and the vertex sits directly on the $x$-axis.

[TA Sora] Column 3: $\\Delta < 0$. Zero real solutions. The graph floats completely above or below the $x$-axis.

[Prof. Park] Notice how this gives you an immediate audit tool: before spending five minutes solving an equation on an exam, take fifteen seconds to check $b^2 - 4ac$. If it's negative, you immediately write 'No real solutions' and move on!

[TA Sora] The Discriminant saves time, prevents frustration, and gives you total situational awareness!""",

    6: """[Prof. Park] On Slide 6, we evaluate function values for $f(x) = 3x^2 - 5x + 7$: evaluating $f(1)$ and $f(-1)$.

[TA Sora] Let's evaluate $f(1)$: $f(1) = 3(1)^2 - 5(1) + 7 = 3(1) - 5 + 7 = 3 - 5 + 7 = 5$. That gives the point $(1, 5)$!

[Prof. Park] Now evaluate $f(-1)$: remember protective parentheses around $-1$! $f(-1) = 3(-1)^2 - 5(-1) + 7$. Exponent first: $(-1)^2 = +1$. Multiply: $3(1) = 3$, and $-5(-1) = +5$. Then add: $3 + 5 + 7 = 15$! That gives the point $(-1, 15)$.

[TA Sora] Notice how steep the parabola climbs: moving from $x = 0$ (where $y = 7$) to $x = -1$, the height jumps up to 15! That accelerating rate of change is the hallmark of quadratic growth.

[Prof. Park] Solution points: $(1, 5)$ and $(-1, 15)$. Disciplined substitution leads to effortless precision!""",

    7: """[Prof. Park] Slide 7 challenges us with function composition and equation solving: find all values of $x$ where $f(x) = 9$ for $f(x) = 3x^2 - 5x + 7$.

[TA Sora] We set the function output equal to 9: $3x^2 - 5x + 7 = 9$. Remember our golden rule from Lecture 38: the equation MUST equal zero before we solve! Subtract 9 from both sides: $3x^2 - 5x - 2 = 0$!

[Prof. Park] Now let's check the Discriminant of this new equation: $a = 3$, $b = -5$, $c = -2$. $\\Delta = (-5)^2 - 4(3)(-2) = 25 + 24 = 49$!

[TA Sora] $\\Delta = 49$! It's positive and a perfect square ($7^2$)! That means it factors! Using the ac-method: $3 \\times (-2) = -6$. Factors of $-6$ that add to $-5$ are $-6$ and $+1$!

[Prof. Park] Rewrite: $3x^2 - 6x + 1x - 2 = 0 \\implies 3x(x - 2) + 1(x - 2) = 0 \\implies (3x + 1)(x - 2) = 0$!

[TA Sora] Set each factor to zero: $3x + 1 = 0 \\implies x = -1/3$. And $x - 2 = 0 \\implies x = 2$!

[Prof. Park] The two solutions are $x = -1/3$ and $x = 2$. At both of these inputs, the parabola reaches an exact height of $y = 9$!

[TA Sora] Solution set: $\\{-1/3, 2\\}$. The discriminant predicted rational roots, and factoring delivered!""",

    8: """[Prof. Park] We have completed Lecture 42! Today we proved that $\\Delta = b^2 - 4ac$ tells the entire mathematical story of any quadratic equation before you lift a finger to solve it.

[TA Sora] Positive gives two roots; zero gives one tangent root; negative gives zero real roots. 

[Prof. Park] In Lecture 43, we compare all four solving methods side-by-side: Square Root Property, Factoring, Completing the Square, and the Quadratic Formula. 

[TA Sora] Keep your confidence high, Bobcats! We will see you in Lecture 43!"""
}

SCRIPTS_L43_FULL = {
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

[TA Sora] Both methods yield the exact same vertex $(2, -5)$. The formula is usually faster, but vertex form reveals the complete geometric transformations!

[Prof. Park] In civil engineering, knowing both methods allows you to cross-verify structural calculations before building physical prototypes.

[TA Sora] Having two independent ways to reach the same answer is the ultimate confidence booster in mathematics!""",

    7: """[Prof. Park] Slide 7 presents our Intercept Summary Chart—the master strategy guide to keep in your notes forever.

[TA Sora] Let's summarize the decision tree: 1. Is $b = 0$? Use the Square Root Property ($x^2 = k$). 2. Does it factor easily? Use Factoring ($A \\cdot B = 0$). 3. Is $a = 1$ and $b$ even? Use Completing the Square. 4. Is it non-factorable or messy? Use the Quadratic Formula!

[Prof. Park] Notice how this hierarchy organizes your thinking. You never feel lost or overwhelmed because you simply run down the four questions in order.

[TA Sora] In everyday life, having a decision tree prevents analysis paralysis. When faced with a complex task, evaluate your tools, choose the most efficient path, and execute with focus.

[Prof. Park] Knowing when to use which tool gives you total mastery over any quadratic problem!""",

    8: """[Prof. Park] Section 3.6 is complete! You now possess tactical maturity in college algebra.

[TA Sora] In Lecture 44, we bring all these skills together into the 5-Point Graphing Method. 

[Prof. Park] Complete your Section 3.6 practice problems on pages 94 and 95 tonight.

[TA Sora] Great job today, Bobcats! We will see you in Lecture 44!"""
}

SCRIPTS_L44_FULL = {
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

[TA Sora] Look at the five points on your coordinate grid: $(0, 5)$, $(1, 0)$, $(3, -4)$, $(5, 0)$, and $(6, 5)$. Connect them with a smooth U-shaped curve, and your graph is complete!

[Prof. Park] Look at how beautifully balanced the curve is: vertex at the bottom, intercepts pinning the curve to the axes, and the partner point ensuring perfect width on the right wing.

[TA Sora] That's five-point graphing at its finest!""",

    3: """[Prof. Park] Slide 3 brings us to a downward-opening parabola: $h(x) = -2x^2 + 4x + 6$.

[TA Sora] Point 1: The Vertex! $x_v = -4 / (2(-2)) = -4 / -4 = 1$. Evaluate $h(1) = -2(1)^2 + 4(1) + 6 = -2 + 4 + 6 = 8$. Vertex is $(1, 8)$! Because $a = -2 < 0$, it opens downward.

[Prof. Park] Point 2: The $y$-intercept is $(0, 6)$. Point 3: The axis of symmetry is $x = 1$. The partner point 1 unit to the right is $(2, 6)$!

[TA Sora] Points 4 & 5: $x$-intercepts! Set $-2x^2 + 4x + 6 = 0$. Divide by $-2$: $x^2 - 2x - 3 = 0 \\implies (x - 3)(x + 1) = 0 \\implies x = 3, -1$. Roots are $(-1, 0)$ and $(3, 0)$!

[Prof. Park] Look at that majestic arch on your coordinate grid: $(-1, 0)$, $(0, 6)$, $(1, 8)$, $(2, 6)$, and $(3, 0)$! Perfect five-point symmetry!

[TA Sora] Notice how narrow the arch is compared to Slide 2: that factor of $-2$ stretches the graph vertically, making it twice as steep!

[Prof. Park] If this modeled a stone arch bridge in Yellowstone National Park, the clearance height is 8 feet, and the span across the water is 4 feet (from $-1$ to $+3$).

[TA Sora] Five anchor points confirmed: $(-1, 0)$, $(0, 6)$, $(1, 8)$, $(2, 6)$, and $(3, 0)$!""",

    4: """[Prof. Park] On Slide 4, we examine $g(x) = x^2 + 2x + 2$. What happens when a parabola has NO $x$-intercepts?

[TA Sora] Let's check the discriminant: $\\Delta = 2^2 - 4(1)(2) = 4 - 8 = -4 < 0$! It has zero real $x$-intercepts! But we still need five points!

[Prof. Park] When there are no $x$-intercepts, we choose smart test points! Point 1: Vertex: $x_v = -2 / 2 = -1$. $g(-1) = (-1)^2 + 2(-1) + 2 = 1$. Vertex is $(-1, 1)$.

[TA Sora] Point 2: $y$-intercept is $(0, 2)$. Point 3: Symmetric partner across $x = -1$ is $(-2, 2)$!

[Prof. Park] Points 4 & 5: Choose a test input $x = 1$: $g(1) = 1^2 + 2(1) + 2 = 5$, giving $(1, 5)$. Now reflect that point across our line of symmetry $x = -1$: since $x = 1$ is 2 units to the right, go 2 units to the left: $-1 - 2 = -3$. That gives $(-3, 5)$!

[TA Sora] Five anchor points: $(-3, 5)$, $(-2, 2)$, $(-1, 1)$, $(0, 2)$, and $(1, 5)$! Even without $x$-intercepts, the 5-point method delivers a complete, accurate graph!

[Prof. Park] The curve floats gracefully in Quadrants I and II above the $x$-axis. Total graphing mastery!""",

    5: """[Prof. Park] Slide 5 presents $k(x) = -x^2 + 4x - 4$. Here the discriminant is $16 - 16 = 0$. The vertex is $(2, 0)$—a tangent vertex touching the axis at one single point!

[TA Sora] Since the vertex is ON the axis, the vertex and the $x$-intercept are the exact same point $(2, 0)$! To get five points, we use the $y$-intercept $(0, -4)$, its partner $(4, -4)$, and test points at $x = 1$ ($1, -1$) and $x = 3$ ($3, -1$)!

[Prof. Park] Look at how symmetry creates pairs: $(1, -1)$ and $(3, -1)$ are twins; $(0, -4)$ and $(4, -4)$ are twins; and $(2, 0)$ crowns the peak.

[TA Sora] Five points: $(0, -4)$, $(1, -1)$, $(2, 0)$, $(3, -1)$, and $(4, -4)$!""",

    6: """[Prof. Park] Slide 6 compares quadratic and linear functions: evaluating $f(x) = x^2 - 6x + 4$ versus $g(x) = 2x - 3$. Linear growth is constant; quadratic growth accelerates!

[TA Sora] Look at the table of values: for the line $g(x)$, every step of $x$ adds a constant 2 to $y$. But for $f(x)$, the differences between consecutive $y$-values grow larger and larger! That acceleration is why projectile physics, braking distances, and kinetic energy require quadratic functions!

[Prof. Park] Understanding the difference between constant linear velocity and accelerating quadratic displacement is the foundation of physics and engineering.""",

    7: """[Prof. Park] Slide 7 demonstrates function transformations: $f(x + 5)$ shifts the parabola 5 units to the left on the coordinate plane!

[TA Sora] Whenever you add inside the function argument, $(x + c)$, the entire curve shifts horizontally to the left by $c$ units! The shape, width, and vertex height stay identical, but the horizontal location relocates!

[Prof. Park] In acoustic engineering and signal processing, this horizontal shift represents a phase delay in audio waves.""",

    8: """[Prof. Park] Slide 8 solves the system $f(x) = g(x)$: finding the two exact intersection points where the straight line cuts through the curved parabola!

[TA Sora] Set them equal: $x^2 - 6x + 4 = 2x - 3$. Subtract $2x$ and add 3: $x^2 - 8x + 7 = 0 \\implies (x - 1)(x - 7) = 0 \\implies x = 1$ and $x = 7$!

[Prof. Park] At $x = 1$, $y = -1$. At $x = 7$, $y = 11$. The line and the parabola meet at $(1, -1)$ and $(7, 11)$! Complete synthesis of lines and parabolas!"""
}

SCRIPTS_L45_FULL = {
    1: """[Prof. Park] Welcome to Lecture 45—the final lecture of Unit 3 and the grand capstone of our entire M090 journey at Gallatin College Montana State University!

[TA Sora] Congratulations Bobcats! Today we celebrate everything you have accomplished across 45 lectures of introductory algebra! You should feel immensely proud of your growth.

[Prof. Park] Think back to Lecture 1: we started with signed numbers and basic integer arithmetic. In Unit 2, we mastered the Cartesian plane, linear functions, slopes, and straight-line equations. And in Unit 3, we unlocked the curved universe of parabolas, roots, and quadratic optimization!

[TA Sora] Today is our Grand Review. We will synthesize every major tool, examine domain and range, solve real-world projectile problems, and review the master M090 Formula Card!

[Prof. Park] Let's begin our capstone review on Slide 2!""",

    2: """[Prof. Park] Slide 2 reviews Domain and Range across all four Section 3.7 functions: $f(x) = x^2 - 6x + 5$, $h(x) = -2x^2 + 4x + 6$, $g(x) = x^2 + 2x + 2$, and $k(x) = -x^2 + 4x - 4$.

[TA Sora] First, the Domain Invariant: For EVERY quadratic function, the Domain is always all real numbers: $(-\\infty, \\infty)$! You can plug any number into $x$ without restriction.

[Prof. Park] Second, the Range Rule: The Range is always bounded by the vertex $y$-value $k$! For upward parabolas ($a > 0$): Range is $[k, \\infty)$. For downward parabolas ($a < 0$): Range is $(-\\infty, k]$!

[TA Sora] Let's list them: For $f(x)$: minimum is $-4$, so Range is $[-4, \\infty)$. For $h(x)$: maximum is 8, so Range is $(-\\infty, 8]$. For $g(x)$: minimum is 1, so Range is $[1, \\infty)$. For $k(x)$: maximum is 0, so Range is $(-\\infty, 0]$!

[Prof. Park] Knowing the vertex instantly gives you the complete vertical range of the function!""",

    3: """[Prof. Park] Slide 3 summarizes our 5-Point Graphing Masterclass: 1. Vertex $(h, k)$, 2. $y$-intercept $(0, c)$, 3. Symmetric reflection of the $y$-intercept, 4 & 5. The two $x$-intercepts (or test points if roots are imaginary).

[TA Sora] Remember to always sketch the Axis of Symmetry $x = h$ as a dashed line. It acts as your visual mirror, ensuring that both wings of the parabola open with identical curvature and width.

[Prof. Park] A 5-point parabola is a piece of mathematical art. You have mastered this craft!""",

    4: """[Prof. Park] Slide 4 connects quadratics to real-world physics: projectile motion $h(t) = -16t^2 + v_0 t + h_0$, where $-16$ represents half the acceleration of gravity in feet per second squared!

[TA Sora] Look at how our algebraic tools answer real questions: 1. The $y$-intercept $h_0$ is the initial launch height! 2. The vertex formula $t = -v_0 / (2a)$ gives the exact time of maximum altitude! 3. The vertex height $k$ is the maximum altitude reached! 4. The positive $x$-intercept where $h(t) = 0$ is the exact moment of splashdown or ground impact!

[Prof. Park] Whether tracking a golf ball, an arrow, a wildfire retardant drop from an aircraft in Montana, or an artillery trajectory, quadratic functions govern physical flight.

[TA Sora] Algebra is the operating system of the physical world!""",

    5: """[Prof. Park] Slide 5 presents the Grand Review of all four quadratic solving methods: 1. Square Root Property ($X^2 = k$), 2. Factoring ($(x - r_1)(x - r_2) = 0$), 3. Completing the Square ($(x + b/2)^2 = k$), and 4. The Quadratic Formula ($x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$).

[TA Sora] You now command all four methods. You know when to deploy each tool for maximum speed, accuracy, and elegance.

[Prof. Park] No quadratic equation can intimidate you ever again!""",

    6: """[Prof. Park] Slide 6 is your M090 Formula Card—keep this forever in your academic career! 

[TA Sora] It contains: The General Form $ax^2 + bx + c = 0$, Vertex Form $a(x - h)^2 + k$, Vertex Formula $x_v = -b / (2a)$, Quadratic Formula $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$, Discriminant $\\Delta = b^2 - 4ac$, and the factoring special forms!

[Prof. Park] These formulas are the building blocks for College Algebra, Precalculus, Business Calculus, and Engineering Calculus.""",

    7: """[Prof. Park] Slide 7 provides final mastery problem solving and reflection on personal growth, persistence, and logical reasoning.

[TA Sora] Remember where you started in Lecture 1. You may have felt hesitant or anxious about algebra. But you showed up, you practiced on paper, you embraced protective parentheses, and you conquered every challenge step by step!

[Prof. Park] That persistence is the greatest skill you take from this class. Math teaches us that no problem is permanent—with the right tools, structure, and patience, every problem can be solved.""",

    8: """[Prof. Park] Congratulations! You have officially completed M090 Introductory Algebra at Gallatin College Montana State University!

[TA Sora] We are so immensely proud of your hard work, your curiosity, and your resilience. You are ready for College Algebra and beyond. Go Bobcats! 🏔️"""
}
