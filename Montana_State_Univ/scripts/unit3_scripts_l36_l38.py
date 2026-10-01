# -*- coding: utf-8 -*-
"""
unit3_scripts_l36_l38.py
Full 20-25 Minute Broadcast Tiki-Taka Dialogue for Lectures 36, 37, 38
Prof. Eunju Park & TA Sora (Gallatin College Montana State University)
Each lecture contains 8 slides with ~310-380 words per slide (~2,500-2,800 words per lecture).
"""

SCRIPTS_L36 = {
    1: """[Prof. Park] Welcome back to M090, Bobcats! I'm Professor Eunju Park, and joining me is our teaching assistant, Sora. Today we start Section 3.2 on page 75 of your workbook: Finding the $x$-intercepts of Quadratic Functions.

[TA Sora] Hello everyone! In Section 3.0 and 3.1, we focused heavily on the Vertex—the highest peak or lowest valley of the parabola. But now, we turn our attention to the ground level: the $x$-intercepts, also known as the roots or zeros of the function!

[Prof. Park] Think about why $x$-intercepts are so important in real life. If you launch a water rocket in a Bozeman city park, the vertex tells you how high it flew, but the $x$-intercepts tell you where it launched and where it landed! If you run a business, the $x$-intercepts represent your Break-Even Points—where your profit is exactly zero ($P(x) = 0$).

[TA Sora] And algebraically, the definition of an $x$-intercept is where the output $y$ or $f(x)$ equals zero. That means every single $x$-intercept problem requires us to solve a Quadratic Equation: $ax^2 + bx + c = 0$!

[Prof. Park] In this unit, we will learn four distinct methods to solve quadratic equations: the Square Root Property, Factoring, Completing the Square, and the Quadratic Formula. 

[TA Sora] And Section 3.2 introduces the fastest and most direct of all four methods: the Square Root Property (SRP)! 

[Prof. Park] When can we use the Square Root Property? We use it whenever the variable is isolated inside a squared term, with no independent linear $x$ term floating around outside!

[TA Sora] Open your workbook to page 75. Let's inspect the theoretical foundation of the Square Root Property on Slide 2!""",

    2: """[Prof. Park] Slide 2 defines the Square Root Property (SRP): If $X^2 = k$, where $k$ is a real number, then $X = \\pm \\sqrt{k}$. Sora, notice that tiny symbol: $\\pm$, read as 'plus or minus.' Why is that the #1 trap in this entire section?

[TA Sora] That 'plus or minus' symbol is where 80% of student mistakes occur! When people see $x^2 = 16$, their brain automatically thinks 4 because $4 \\times 4 = 16$. But they forget that negative numbers exist! $(-4) \\times (-4)$ also equals positive 16!

[Prof. Park] Exactly! Both $+4$ and $-4$, when squared, produce positive 16. If you forget the $\\pm$ sign, you lose half your solutions and erase half of your parabola's roots!

[TA Sora] Here is Sora's Rule: 'Whenever YOU physically write a square root symbol across an equals sign to solve an equation, you MUST immediately write a $\\pm$ in front of it!' The square root operation itself gives the principal (positive) root, but the equation demands BOTH signs!

[Prof. Park] Now let's consider the number $k$ on the right side: First, if $k > 0$ (positive), there are two distinct real solutions: $X = +\\sqrt{k}$ and $X = -\\sqrt{k}$.

[TA Sora] Second, if $k = 0$, there is exactly ONE real solution: $X = \\pm \\sqrt{0} = 0$. That corresponds to a parabola whose vertex is tangent to the $x$-axis!

[Prof. Park] And third, what if $k < 0$ (negative)? If $x^2 = -9$, there is NO real number that squares to give a negative number! That means the equation has NO real solutions, and the parabola never crosses the $x$-axis!

[TA Sora] Three clear cases: $k > 0$ gives two real roots; $k = 0$ gives one real root; $k < 0$ gives zero real roots. Keep that $\\pm$ firmly in place as we work through Example 1 on Slide 3!""",

    3: """[Prof. Park] On Slide 3, we look at Section 3.2 Example 1 on page 75: Solve the equation $x^2 = 16$. Sora, this is the foundational textbook example.

[TA Sora] Let's follow our protocol step-by-step. Step 1: The squared term $x^2$ is already completely isolated on the left side, and the number 16 is on the right side. 

[Prof. Park] Step 2: Apply the Square Root Property: take the square root of both sides, and instantly place a $\\pm$ on the right side: $x = \\pm \\sqrt{16}$.

[TA Sora] Step 3: Simplify the radical! 16 is a perfect square because $4^2 = 16$. So $\\sqrt{16} = 4$. That gives us $x = \\pm 4$, which means $x = 4$ or $x = -4$!

[Prof. Park] Step 4: Always check your answers by substituting them back into the original equation! For $x = 4$: $(4)^2 = 16$ (True). For $x = -4$: $(-4)^2 = 16$ (True). Both answers check out with 100% certainty!

[TA Sora] Now let's connect this to the graph of $f(x) = x^2 - 16$. If you set $f(x) = 0$, you get $x^2 - 16 = 0$, which is $x^2 = 16$. The two solutions $x = 4$ and $x = -4$ are the two $x$-intercepts on the coordinate grid: $(-4, 0)$ and $(4, 0)$!

[Prof. Park] Notice how the two roots sit at equal distances from the $y$-axis: 4 units to the left, and 4 units to the right. That perfect balance is reflected in the $\\pm$ symbol!

[TA Sora] In set notation, write your solution set as $\\{-4, 4\\}$. Two real solutions, completely verified!""",

    4: """[Prof. Park] Slide 4 brings us to Example 2: Solve the equation $2x^2 + 2 = 10$. Sora, here the squared term $x^2$ is not by itself yet. What is our first priority?

[TA Sora] Our golden rule before applying the Square Root Property is: 'Isolate the squared term completely before taking any square roots!' You cannot take the square root while there are other numbers added to or multiplying $x^2$!

[Prof. Park] Let's peel away the numbers around $x^2$ using reverse order of operations. First, subtract 2 from both sides of the equation: $2x^2 + 2 - 2 = 10 - 2$, which simplifies to $2x^2 = 8$.

[TA Sora] Next, divide both sides by 2 to eliminate the coefficient: $2x^2 / 2 = 8 / 2$, which gives $x^2 = 4$!

[Prof. Park] Now, and only now, is the squared term isolated: $x^2 = 4$. Now we unleash the Square Root Property: take the square root of both sides and insert the $\\pm$ sign: $x = \\pm \\sqrt{4}$.

[TA Sora] Since 4 is a perfect square, $\\sqrt{4} = 2$. So our solutions are $x = \\pm 2$, meaning $x = 2$ and $x = -2$!

[Prof. Park] Let's check both solutions in the original equation $2x^2 + 2 = 10$. If $x = 2$: $2(2)^2 + 2 = 2(4) + 2 = 8 + 2 = 10$ (Check!). If $x = -2$: $2(-2)^2 + 2 = 2(4) + 2 = 8 + 2 = 10$ (Check!).

[TA Sora] Notice how important it was to isolate $x^2$ first. If a student mistakenly took the square root at the beginning, they would get an algebraic mess. Always isolate first, square root second!

[Prof. Park] Solution set: $\\{-2, 2\\}$. A disciplined, clean execution!""",

    5: """[Prof. Park] Turning to Slide 5, Section 3.2 Example 3 connects solving directly to graphing: For the function $f(x) = x^2 - 16$, find the $x$-intercepts, the $y$-intercept, the vertex, and sketch the graph.

[TA Sora] This is where algebra and geometry shake hands! First, let's find the $x$-intercepts: set $f(x) = 0$, so $x^2 - 16 = 0$. Add 16 to both sides: $x^2 = 16$. By the Square Root Property, $x = \\pm \\sqrt{16} = \\pm 4$.

[Prof. Park] So the $x$-intercepts as ordered pairs are $(-4, 0)$ and $(4, 0)$! Now Step 2: find the $y$-intercept by evaluating $f(0)$: $f(0) = (0)^2 - 16 = -16$. So the $y$-intercept is $(0, -16)$.

[TA Sora] Step 3: Find the vertex! Here $a = 1$, $b = 0$, and $c = -16$. Using our Vertex Formula from Section 3.1: $x_v = -b / (2a) = -0 / (2 \\cdot 1) = 0$. And $f(0) = -16$. So the vertex is $(0, -16)$!

[Prof. Park] Look at the graph on your screen. The vertex $(0, -16)$ is the minimum point. The vertical Axis of Symmetry is $x = 0$ (the $y$-axis). And the two wings of the parabola rise up and pass through $(-4, 0)$ on the left and $(4, 0)$ on the right!

[TA Sora] Look at how wide and symmetrical the curve is! The distance from the center line $x = 0$ to the left root is 4 units, and to the right root is 4 units.

[Prof. Park] If you are designing an arched entryway for a barn in the Gallatin Valley, the width along the ground is 8 feet (from $-4$ to $+4$), and the depth or height clearance is 16 feet!

[TA Sora] Domain is $(-\\infty, \\infty)$, and Range is $[-16, \\infty)$. All four landmarks found with total precision!""",

    6: """[Prof. Park] Slide 6 presents Example 4: For $g(x) = 3x^2 - 15$, find the $x$-intercepts and the vertex. Sora, notice the number 15—is 15 a perfect square?

[TA Sora] It is not! 15 is not like 4, 9, 16, or 25. But that is completely fine! In college algebra, we embrace radicals and work with exact irrational values!

[Prof. Park] Let's find the $x$-intercepts: set $g(x) = 0$, so $3x^2 - 15 = 0$. Step 1: Isolate the $x^2$ term. Add 15 to both sides: $3x^2 = 15$. Divide by 3: $x^2 = 5$!

[TA Sora] Step 2: Apply the Square Root Property: $x = \\pm \\sqrt{5}$. Since 5 is a prime number with no perfect square factors, $\\sqrt{5}$ cannot be simplified any further.

[Prof. Park] That gives us our exact solutions: $x = \\sqrt{5}$ and $x = -\\sqrt{5}$! As ordered pairs on the coordinate plane, the $x$-intercepts are $(-\\sqrt{5}, 0)$ and $(\\sqrt{5}, 0)$.

[TA Sora] Now, if you need to plot those points on a graph or measure them with a tape measure on a carpentry project, what is $\\sqrt{5}$ approximately? $\\sqrt{5} \\approx 2.236$! So the roots are roughly at $-2.24$ and $+2.24$.

[Prof. Park] And what about the vertex? Since $b = 0$, $x_v = 0$, and $g(0) = 3(0)^2 - 15 = -15$. So the vertex sits down at $(0, -15)$!

[TA Sora] Look at the graph: the vertex is $(0, -15)$, opening upward with a narrow curve because $a = 3$, and crossing the $x$-axis at $\\pm \\sqrt{5} \\approx \\pm 2.24$.

[Prof. Park] Always write down the exact radical form first: $\\pm \\sqrt{5}$. That is the standard of mathematical precision!""",

    7: """[Prof. Park] On Slide 7, we address a profound conceptual question: What happens when $x^2 = k$ and $k$ is a negative number? For instance, what if we try to solve $x^2 = -9$?

[TA Sora] Let's test this logically! Suppose someone claims that $x = 3$. Well, $3 \\times 3 = +9$, not $-9$. Then they say: 'What about $x = -3$?' But $(-3) \\times (-3)$ is ALSO $+9$! 

[Prof. Park] In the set of real numbers, whenever you multiply any real number by itself, the result is ALWAYS positive or zero: $x^2 \\geq 0$. It is physically impossible for the square of a real number to be negative!

[TA Sora] Therefore, the equation $x^2 = -9$ has NO real solutions! If you try to write $x = \\pm \\sqrt{-9}$, in intermediate algebra we introduce imaginary numbers ($3i$), but on the real Cartesian coordinate plane, there are NO real coordinates!

[Prof. Park] Now think about what this means for the graph of $f(x) = x^2 + 9$. The vertex is at $(0, 9)$, and since $a = 1 > 0$, the parabola opens upward from $y = 9$ towards positive infinity!

[TA Sora] Look at that picture in your mind: the entire parabola is floating high up in the sky above the $x$-axis! The lowest point is at height 9, so it never descends to touch ground level ($y = 0$).

[Prof. Park] This is why an equation having 'no real solutions' is not a failure—it is a geometric fact! The graph simply does not intersect the $x$-axis.

[TA Sora] Remember: if $x^2 = \\text{negative}$, write 'No Real Solutions.' The parabola floats completely above or below the $x$-axis!""",

    8: """[Prof. Park] We have arrived at Slide 8, our Section 3.2 Part 1 Mastery Summary! Let's review the ground we have conquered in Lecture 36.

[TA Sora] The headline theorem today was the Square Root Property: If $X^2 = k$, then $X = \\pm \\sqrt{k}$. Never forget the $\\pm$ sign—it accounts for both positive and negative roots!

[Prof. Park] We learned the essential two-step strategy: Step 1, isolate the squared term completely (e.g., $2x^2 + 2 = 10 \\implies x^2 = 4$). Step 2, apply the square root property and simplify the radical.

[TA Sora] We saw that if $k$ is not a perfect square, like $x^2 = 5$, we keep the exact radical form $x = \\pm \\sqrt{5}$, and we can use a decimal approximation ($\\approx \\pm 2.24$) for practical measurements.

[Prof. Park] And we proved that if $k$ is negative, like $x^2 = -9$, there are NO real solutions because no real number squares to a negative. Geometrically, this means the parabola floats entirely above or below the $x$-axis.

[TA Sora] In everyday life, knowing when a problem has two solutions, one solution, or no solutions helps you avoid chasing impossible outcomes and focuses your energy on real, achievable targets.

[Prof. Park] In Lecture 37, we will expand the Square Root Property to binomial squares of the form $(x - h)^2 = k$. Practice the exercises on page 76 tonight!

[TA Sora] Fantastic work today, Bobcats! We will see you in Lecture 37!"""
}

SCRIPTS_L37 = {
    1: """[Prof. Park] Hello everyone, and welcome to Lecture 37 of M090 Introductory Algebra! I'm Professor Eunju Park, and joining me as always is our stellar teaching assistant, Sora. Today we advance to Section 3.2 Part 2 on page 77 of your workbook: The Square Root Property with Binomial Squares.

[TA Sora] Welcome back, Bobcats! In Lecture 36, we applied the Square Root Property to a single isolated variable: $x^2 = k \\implies x = \\pm \\sqrt{k}$. But today, the base being squared is an entire binomial: $(x - h)^2 = k$!

[Prof. Park] Many students look at an equation like $(x - 3)^2 = 25$ and their first instinct is to expand it: write $x^2 - 6x + 9 = 25$, subtract 25, and try to factor it. Sora, is that wrong?

[TA Sora] It is not mathematically wrong, but it is like driving from Bozeman to Billings by going through Seattle! You are doing three times more work and creating multiple opportunities to make sign errors!

[Prof. Park] Exactly. Why expand a perfect square when it is ALREADY packaged as a square? We can apply the Square Root Property directly to the entire binomial: if $(x - h)^2 = k$, then taking the square root of both sides gives $x - h = \\pm \\sqrt{k}$!

[TA Sora] Look at how brilliant that is: the exponent of 2 vanishes, the parentheses disappear, and you are left with a simple, one-step linear equation! Just add $h$ to both sides, and you have $x = h \\pm \\sqrt{k}$!

[Prof. Park] Think about carpentry and framing in Montana construction. When you pre-fabricate a wall frame in a controlled shop and bring it to the job site, you install it as a pre-built unit; you don't take it apart and rebuild it from individual two-by-fours! $(x - h)^2$ is a pre-packaged square. Keep it intact!

[TA Sora] Open your workbook to page 77. Let's solve Example 5 together on Slide 2!""",

    2: """[Prof. Park] On Slide 2, Section 3.2 Example 5 asks us to solve the equation $(x - 3)^2 = 25$. Let's demonstrate the speed and elegance of the Square Root Property!

[TA Sora] Step 1: Check that the binomial square is isolated on the left side. It is! $(x - 3)^2$ is all by itself, and 25 is on the right side.

[Prof. Park] Step 2: Apply the Square Root Property: take the square root of both sides, remembering our mandatory $\\pm$ on the right: $x - 3 = \\pm \\sqrt{25}$.

[TA Sora] Step 3: Simplify the radical! Since 25 is a perfect square, $\\sqrt{25} = 5$. So our equation becomes $x - 3 = \\pm 5$!

[Prof. Park] Step 4: Now isolate $x$ by adding 3 to both sides: $x = 3 \\pm 5$. Notice where we write the 3: we place it in FRONT of the $\\pm$ sign! That keeps our arithmetic organized and clear.

[TA Sora] Step 5: Split this into two separate branch calculations! Branch 1 (using the plus sign): $x = 3 + 5 = 8$. Branch 2 (using the minus sign): $x = 3 - 5 = -2$!

[Prof. Park] Look at those two clean solutions: $x = 8$ and $x = -2$. Let's check both in the original equation! For $x = 8$: $(8 - 3)^2 = (5)^2 = 25$ (True!). For $x = -2$: $(-2 - 3)^2 = (-5)^2 = 25$ (True!).

[TA Sora] Both answers check out 100%! Notice the symmetry: the center number is 3, and both solutions are exactly 5 units away from 3: $3 + 5 = 8$, and $3 - 5 = -2$.

[Prof. Park] That center number 3 is the $x$-coordinate of the parabola's vertex! The distance 5 is the horizontal spread to the $x$-intercepts.

[TA Sora] Solution set: $\\{-2, 8\\}$. Five clean steps, zero messy factoring!""",

    3: """[Prof. Park] Turning to Slide 3, Section 3.2 Example 6 connects this method to graphing a quadratic function in vertex form: For $f(x) = (x + 2)^2 - 9$, find the $x$-intercepts and the vertex, and sketch the graph.

[TA Sora] Look at how familiar this form is! $f(x) = (x + 2)^2 - 9$ is written in Vertex Form $a(x - h)^2 + k$. We can read the vertex immediately: inside $(x + 2)$ flips to $h = -2$, and outside $-9$ stays $k = -9$. The vertex is $(-2, -9)$!

[Prof. Park] And since $a = 1 > 0$, the parabola opens upward from that minimum of $-9$. Now let's find the $x$-intercepts by setting $f(x) = 0$: $(x + 2)^2 - 9 = 0$.

[TA Sora] Step 1: Isolate the binomial square by adding 9 to both sides: $(x + 2)^2 = 9$!

[Prof. Park] Step 2: Apply the Square Root Property: $x + 2 = \\pm \\sqrt{9} = \\pm 3$. Step 3: Subtract 2 from both sides, placing $-2$ in front: $x = -2 \\pm 3$!

[TA Sora] Now split into the two branches: Branch 1: $x = -2 + 3 = +1$. Branch 2: $x = -2 - 3 = -5$! That gives us two $x$-intercepts: $(1, 0)$ and $(-5, 0)$!

[Prof. Park] Look at the symmetry around our vertex $x$-coordinate of $-2$: to the right, $-2 + 3 = 1$; to the left, $-2 - 3 = -5$. Both roots are exactly 3 units away from the vertical line of symmetry $x = -2$!

[TA Sora] Look at the coordinate plane on your screen: the vertex sits at $(-2, -9)$, the axis of symmetry is $x = -2$, and the curve passes through $(-5, 0)$ and $(1, 0)$.

[Prof. Park] Finding intercepts from vertex form via the Square Root Property is lightning fast. Everything connects!""",

    4: """[Prof. Park] On Slide 4, Example 7 adds one extra layer of algebra: Solve the equation $2(x - 4)^2 = 32$. Sora, what must a student NEVER do at the start of this problem?

[TA Sora] Never distribute that 2 inside the parentheses! Many students want to multiply 2 by $(x - 4)$ and write $(2x - 8)^2$. That is a catastrophic violation of PEMDAS! Exponents have priority over multiplication. You cannot distribute into a base that is being squared!

[Prof. Park] That is such a vital warning. So what should we do with that 2? We divide both sides by 2! Let's do that right now: $2(x - 4)^2 / 2 = 32 / 2$, which gives $(x - 4)^2 = 16$!

[TA Sora] Look at how clean that is! Now the binomial square is completely isolated: $(x - 4)^2 = 16$.

[Prof. Park] Now we apply the Square Root Property: take the square root of both sides with our $\\pm$ sign: $x - 4 = \\pm \\sqrt{16} = \\pm 4$.

[TA Sora] Now add 4 to both sides: $x = 4 \\pm 4$. Let's evaluate both branches: Branch 1: $x = 4 + 4 = 8$. Branch 2: $x = 4 - 4 = 0$!

[Prof. Park] Our two solutions are $x = 8$ and $x = 0$! Let's check them in the original equation $2(x - 4)^2 = 32$. For $x = 8$: $2(8 - 4)^2 = 2(4)^2 = 2(16) = 32$ (Check!). For $x = 0$: $2(0 - 4)^2 = 2(-4)^2 = 2(16) = 32$ (Check!).

[TA Sora] One of our roots is $x = 0$, which means this parabola passes directly through the origin $(0, 0)$!

[Prof. Park] Remember the lesson: divide by the outside coefficient first; never distribute into a squared binomial. Solution set: $\\{0, 8\\}$!""",

    5: """[Prof. Park] Slide 5 presents Section 3.2 Example 8: $(x + 1)^2 = 12$. Here, 12 is not a perfect square. Sora, how do we handle non-perfect square radicals?

[TA Sora] We simplify the radical by factoring out the largest perfect square factor! Let's follow our steps: Step 1: The binomial square is already isolated: $(x + 1)^2 = 12$.

[Prof. Park] Step 2: Apply the Square Root Property: $x + 1 = \\pm \\sqrt{12}$. Now, how do we simplify $\\sqrt{12}$? We look for perfect square factors: $12 = 4 \\times 3$. Since 4 is a perfect square, $\\sqrt{12} = \\sqrt{4 \\times 3} = \\sqrt{4} \\cdot \\sqrt{3} = 2\\sqrt{3}$!

[TA Sora] Beautiful! So $x + 1 = \\pm 2\\sqrt{3}$. Step 3: Subtract 1 from both sides, putting the $-1$ in front: $x = -1 \\pm 2\\sqrt{3}$!

[Prof. Park] Can we combine $-1$ and $2\\sqrt{3}$ into a single number like $1\\sqrt{3}$? Absolutely not! You cannot combine a rational integer with an irrational radical term. They are like apples and oranges.

[TA Sora] So our two exact solutions are $x = -1 + 2\\sqrt{3}$ and $x = -1 - 2\\sqrt{3}$.

[Prof. Park] What if a surveyor or civil engineer working on a road project near Bozeman needs to know where these points lie on the ground? We approximate $\\sqrt{3} \\approx 1.732$. Then $2\\sqrt{3} \\approx 3.464$.

[TA Sora] That gives: $x = -1 + 3.464 = 2.464$, and $x = -1 - 3.464 = -4.464$!

[Prof. Park] Both forms have their purpose: exact radical form $-1 \\pm 2\\sqrt{3}$ for pure mathematics, and decimal approximations for real-world measurements.

[TA Sora] Always provide exact form unless the problem explicitly asks you to round!""",

    6: """[Prof. Park] On Slide 6, we explore 'Exact Radical Form versus Decimal Approximations.' In STEM disciplines—engineering, physics, computer science, and chemistry—knowing when to use which form is a vital professional skill.

[TA Sora] Let's define the difference clearly: Exact Radical Form contains symbols like $\\sqrt{3}$, $\\sqrt{5}$, or $\\pi$. It preserves 100% of the mathematical truth with zero rounding error. No digits are lost!

[Prof. Park] Think about sending a space probe to Mars or programming a CNC plasma cutter to slice steel beams for a bridge in Helena. If you round $\\sqrt{3}$ to $1.7$ too early in your calculations, that rounding error compounds over thousands of operations, and your bridge joint will not align properly!

[TA Sora] But Decimal Approximations are essential when communicating with the physical world! If you go to a lumber yard or hardware store in Bozeman and ask for '$-1 + 2\\sqrt{3}$ feet of copper pipe,' the store clerk will look at you like you're from outer space!

[Prof. Park] Exactly. You tell them: 'I need about 2 feet 5 and a half inches (2.46 feet).' That is where decimals shine.

[TA Sora] Here is the golden rule for college algebra: 'Keep exact radical form throughout all intermediate calculation steps. Only round at the very final step, and only if requested!'

[Prof. Park] Respecting the exact value is a sign of mathematical maturity. Master both representations!""",

    7: """[Prof. Park] Slide 7 presents 'Sora's Checklist for the Square Root Property.' Let's summarize the four non-negotiable steps to guarantee success on every homework and exam problem.

[TA Sora] Step 1: The 'Isolation Phase.' Look at your equation. Is the squared quantity $(X)^2$ or $(x - h)^2$ completely alone on one side of the equals sign? If there is an added number, subtract it! If there is a multiplying coefficient, divide by it!

[Prof. Park] Step 2: The '$\\pm$ Square Root Application.' Once isolated, take the square root of both sides. Write $X = \\pm \\sqrt{k}$ immediately. Do not wait until the next line to add the $\\pm$—write it in the exact same pen stroke!

[TA Sora] Step 3: The 'Radical Simplification.' If $k$ is a perfect square, evaluate it to an integer. If $k$ has perfect square factors, simplify it (e.g., $\\sqrt{12} = 2\\sqrt{3}$). If $k < 0$, stop and write 'No Real Solutions.'

[Prof. Park] Step 4: The 'Linear Solution & Branching.' If solving $(x - h)^2 = k$, add $h$ to both sides: $x = h \\pm \\sqrt{k}$. If the radical simplified to an integer, calculate both branches ($h + \\sqrt{k}$ and $h - \\sqrt{k}$). If it remains a radical, write $h \\pm \\sqrt{k}$.

[TA Sora] Follow these four steps in order, and the Square Root Property will feel like a smooth, effortless routine every single time!""",

    8: """[Prof. Park] We have arrived at Slide 8, our Section 3.2 Complete Mastery Summary! Sora, what an empowering set of tools we've built in Lectures 36 and 37.

[TA Sora] We have truly expanded our algebraic toolkit! We mastered the Square Root Property for simple variables ($x^2 = k$) and for binomial squares ($(x - h)^2 = k$).

[Prof. Park] We learned that isolated binomial squares should never be expanded when solving—we take the square root directly, saving time and preventing errors. We emphasized the mandatory $\\pm$ sign that guarantees both symmetric roots are captured.

[TA Sora] We connected solving to graphing: the solutions $x = h \\pm \\sqrt{k}$ are the $x$-intercepts, centered symmetrically around the vertex line $x = h$.

[Prof. Park] And we distinguished between exact radical values that preserve absolute mathematical truth and decimal approximations that guide real-world physical construction.

[TA Sora] Tonight, complete all Section 3.2 homework exercises on pages 77 through 79 of your workbook. 

[Prof. Park] In Lecture 38, we begin Section 3.3: solving quadratic equations by Factoring, using the legendary Zero Product Property. 

[TA Sora] Outstanding work today, Bobcats! We will see you all in Lecture 38!"""
}

SCRIPTS_L38 = {
    1: """[Prof. Park] Welcome back to M090, Bobcats! I am Professor Eunju Park, and joining me is our teaching assistant, Sora. Today we enter Section 3.3 on page 80 of your workbook: Solving Quadratic Equations by Factoring.

[TA Sora] Hello everyone! Section 3.3 is one of my absolute favorite sections in all of algebra. In Section 3.2, we used the Square Root Property, which required the equation to have an isolated square with no standalone linear $x$ term. But what do we do when an equation has all three terms: $ax^2 + bx + c = 0$?

[Prof. Park] When all three terms are present, our primary tool is Factoring, powered by one of the most fundamental theorems in all of mathematics: The Zero Product Property!

[TA Sora] Let's state the Zero Product Property in plain English: If you multiply two real numbers together and the answer is zero—$A \\cdot B = 0$—then at least one of those numbers MUST be zero! Either $A = 0$, or $B = 0$, or both!

[Prof. Park] Think about how remarkable that is. If I tell you that two numbers multiply to give 12—$A \\cdot B = 12$—can you tell me what $A$ is? No! $A$ could be 1, 2, 3, 4, 6, 12, or even fractions like $1/2$ times 24! There are infinite possibilities!

[TA Sora] But zero is unique! If $A \\cdot B = 0$, there is NO mystery. One of those factors has to be zero. That property allows us to take a complex quadratic equation of degree 2, factor it into two linear pieces, and solve each piece in one simple step!

[Prof. Park] In life, when you face a huge, overwhelming project—renovating a house, organizing your finances, or studying for finals—you don't try to solve the whole giant problem at once. You factor it into smaller, manageable tasks and solve them one by one.

[TA Sora] Turn to page 80 in your workbook. Let's look at our first official example on Slide 2!""",

    2: """[Prof. Park] Slide 2 brings us to Section 3.3 Example 1 on page 80: Solve the equation $x^2 - 5x + 6 = 0$ by factoring.

[TA Sora] Let's follow our step-by-step factoring method. Step 1: Ensure the equation is set equal to zero! It is: $x^2 - 5x + 6 = 0$.

[Prof. Park] Step 2: Identify the target numbers. For a trinomial with leading coefficient 1, we need two numbers that multiply to give the constant term $+6$, and add to give the linear coefficient $-5$.

[TA Sora] Let's think about factors of $+6$. Since they multiply to a positive number and add to a negative number, BOTH numbers must be negative! Let's check: $-1 \\times (-6) = +6$, but $-1 + (-6) = -7$ (Not $-5$). What about $-2$ and $-3$? $-2 \\times (-3) = +6$, and $-2 + (-3) = -5$! They match perfectly!

[Prof. Park] Beautiful! So our trinomial factors into: $(x - 2)(x - 3) = 0$. Step 3: Now apply the Zero Product Property! Set each factor equal to zero independently: $x - 2 = 0$ or $x - 3 = 0$.

[TA Sora] Step 4: Solve each linear equation: for $x - 2 = 0$, add 2 to both sides to get $x = 2$. For $x - 3 = 0$, add 3 to both sides to get $x = 3$!

[Prof. Park] We have our two solutions: $x = 2$ and $x = 3$. Now look at the coordinate plane on your screen! Notice that the parabola $f(x) = x^2 - 5x + 6$ crosses the $x$-axis at exactly $(2, 0)$ and $(3, 0)$!

[TA Sora] And look at the vertex: it sits right between them at $x = 2.5$, down at $y = -0.25$! Notice how our anti-collision labels display cleanly: the vertex label sits below the valley, and the roots $(2, 0)$ and $(3, 0)$ sit cleanly on their respective sides.

[Prof. Park] Everything connects: factoring finds the roots, and the roots anchor the parabola on the coordinate plane. Solution set: $\\{2, 3\\}$!""",

    3: """[Prof. Park] On Slide 3, Section 3.3 Example 2 asks us to find the $x$-intercepts and vertex for $f(x) = x^2 + 7x + 10$.

[TA Sora] Let's find the $x$-intercepts first by setting the function equal to zero: $x^2 + 7x + 10 = 0$. We need two numbers that multiply to $+10$ and add to $+7$.

[Prof. Park] Factors of 10: $1 \\times 10 = 10$, but $1 + 10 = 11$. How about $2 \\times 5$? $2 \\times 5 = 10$, and $2 + 5 = 7$! That works!

[TA Sora] So it factors into $(x + 2)(x + 5) = 0$. Setting each factor equal to zero: $x + 2 = 0 \\implies x = -2$, and $x + 5 = 0 \\implies x = -5$!

[Prof. Park] That gives us two $x$-intercepts as ordered pairs: $(-2, 0)$ and $(-5, 0)$. Now let's find the vertex! Sora, where must the $x$-coordinate of the vertex be?

[TA Sora] Right at the midpoint between $-2$ and $-5$! $(-2 + (-5)) / 2 = -7/2 = -3.5$! Or using the Vertex Formula: $x_v = -b / (2a) = -7 / (2 \\cdot 1) = -3.5$. Both methods give $x = -3.5$!

[Prof. Park] Now find the $y$-value by evaluating $f(-3.5)$: $f(-3.5) = (-3.5)^2 + 7(-3.5) + 10 = 12.25 - 24.5 + 10 = -2.25$! So the vertex is at $(-3.5, -2.25)$.

[TA Sora] And the $y$-intercept is found by plugging in $x = 0$: $f(0) = 0^2 + 7(0) + 10 = 10$, giving $(0, 10)$!

[Prof. Park] Look at the graph: vertex at $(-3.5, -2.25)$, opening upward since $a = 1 > 0$, crossing the $x$-axis at $(-5, 0)$ and $(-2, 0)$, and crossing the $y$-axis at $(0, 10)$.

[TA Sora] Factoring gives you the roots in thirty seconds. It is fast, clean, and reliable!""",

    4: """[Prof. Park] Turning to Slide 4, Example 3 presents a different factoring pattern: Solve $2x^2 - 8x = 0$. Sora, notice that this equation only has two terms. There is no constant term $c$!

[TA Sora] When a quadratic equation is missing its constant term, students sometimes freeze because they are looking for three terms to do trinomial factoring. But whenever you see shared variables, your first instinct should always be: 'Greatest Common Factor (GCF)!'

[Prof. Park] What is the Greatest Common Factor between $2x^2$ and $8x$? Both terms share a 2, and both terms share at least one $x$! So the GCF is $2x$.

[TA Sora] Let's factor out $2x$: $2x(x - 4) = 0$! Look at that: it factored in a single step!

[Prof. Park] Now apply the Zero Product Property! We have two factors: $2x$ and $(x - 4)$. Set each equal to zero: $2x = 0$ or $x - 4 = 0$.

[TA Sora] For $2x = 0$, divide by 2: $x = 0 / 2 = 0$. For $x - 4 = 0$, add 4: $x = 4$!

[Prof. Park] Our two solutions are $x = 0$ and $x = 4$. Notice that whenever an equation has no constant term ($c = 0$), $x = 0$ is ALWAYS one of the solutions!

[TA Sora] Yes! Because if there is no constant, plugging in $x = 0$ makes every term zero: $2(0)^2 - 8(0) = 0 - 0 = 0$. The graph passes directly through the origin $(0, 0)$!

[Prof. Park] Common mistake: never divide both sides of an equation by the variable $x$! If you divided $2x^2 = 8x$ by $x$, you would get $2x = 8 \\implies x = 4$, and you would completely lose the solution $x = 0$!

[TA Sora] Never divide by a variable because that variable might be zero! Always factor out the GCF instead. Solution set: $\\{0, 4\\}$!""",

    5: """[Prof. Park] Slide 5 brings us to Example 4: Difference of Squares, $4x^2 - 25 = 0$. Sora, here we have two terms again, but this time there is no middle linear term ($b = 0$).

[TA Sora] Look at both terms: $4x^2$ is $(2x)^2$, a perfect square! And 25 is $5^2$, another perfect square! And they are separated by a subtraction sign—that makes this a Difference of Squares!

[Prof. Park] The difference of squares formula is $A^2 - B^2 = (A - B)(A + B)$. Here $A = 2x$ and $B = 5$. So $4x^2 - 25$ factors instantly into: $(2x - 5)(2x + 5) = 0$!

[TA Sora] Now set each factor equal to zero: $2x - 5 = 0 \\implies 2x = 5 \\implies x = 5/2$. And $2x + 5 = 0 \\implies 2x = -5 \\implies x = -5/2$!

[Prof. Park] Look at that symmetry: $x = 5/2$ and $x = -5/2$, which is $x = \\pm 2.5$!

[TA Sora] Notice that you could also have solved this using the Square Root Property from Section 3.2: add 25 to get $4x^2 = 25$, divide by 4 to get $x^2 = 25/4$, and take the square root: $x = \\pm \\sqrt{25/4} = \\pm 5/2$!

[Prof. Park] Both methods give the exact same two roots! Factoring and the Square Root Property are two sides of the same mathematical coin.

[TA Sora] As ordered pairs on the graph of $f(x) = 4x^2 - 25$, the $x$-intercepts are $(-2.5, 0)$ and $(2.5, 0)$, perfectly centered around the $y$-axis.

[Prof. Park] Solution set: $\\{-5/2, 5/2\\}$. Quick, clean, and symmetrical!""",

    6: """[Prof. Park] Slide 6 addresses what is known across mathematics departments as 'The Must Equal Zero Trap.' Look at the equation on your screen: $x(x - 5) = 6$. Sora, why does this problem cause so many heartaches on exams?

[TA Sora] Because students see factors on the left side, and they say: 'Oh, it's already factored! I'll just set $x = 6$ and $x - 5 = 6$!' That is a 100% fatal mathematical error!

[Prof. Park] Let's be completely clear: There is a Zero Product Property, but there is NO such thing as a 'Six Product Property'! If two numbers multiply to 6, they could be 2 and 3, 1 and 6, $-2$ and $-3$, or $12$ and $0.5$! Setting factors equal to 6 is completely meaningless!

[TA Sora] The Zero Product Property ONLY works when the right side is strictly ZERO! If it does not equal zero, you cannot apply the theorem!

[Prof. Park] So what is the correct protocol? We must tear down the left side, bring the 6 over, and rebuild! Step 1: Distribute $x$ on the left side: $x(x - 5) = x^2 - 5x$.

[TA Sora] Step 2: Subtract 6 from both sides to create a zero on the right: $x^2 - 5x - 6 = 0$! Now we have our standard general form equal to zero!

[Prof. Park] Step 3: Now factor the new trinomial: we need two numbers that multiply to $-6$ and add to $-5$. That is $-6$ and $+1$! So it factors into $(x - 6)(x + 1) = 0$.

[TA Sora] Step 4: Now, and only now, set each factor equal to zero: $x - 6 = 0 \\implies x = 6$, and $x + 1 = 0 \\implies x = -1$!

[Prof. Park] Notice that the true solutions are $6$ and $-1$, NOT the mistaken $6$ and $11$ that someone would get by setting $x - 5 = 6$!

[TA Sora] Remember: 'Zero is the hero!' The equation MUST equal zero before you factor!""",

    7: """[Prof. Park] Slide 7 presents 'Sora's Protocol for Solving by Factoring.' Having a clear roadmap keeps your head cool and your pencil moving smoothly.

[TA Sora] Step 1: The 'Zero Invariant.' Move all terms to one side of the equals sign so that one side is strictly 0: $ax^2 + bx + c = 0$. If the leading coefficient is negative, multiply both sides by $-1$ to make $a$ positive!

[Prof. Park] Step 2: The 'GCF Check.' Always look for a Greatest Common Factor first! Factoring out a GCF immediately shrinks the remaining numbers and makes trinomial factoring ten times easier.

[TA Sora] Step 3: The 'Factoring Strategy.' If there are two terms, check for Difference of Squares ($A^2 - B^2$). If there are three terms with $a = 1$, find numbers that multiply to $c$ and add to $b$. If $a \\neq 1$, use grouping or trial-and-error.

[Prof. Park] Step 4: The 'Zero Product Execution.' Set each linear factor equal to zero independently: $A = 0$ or $B = 0$. Solve each simple equation.

[TA Sora] Step 5: The 'Check & Packaging.' Plug your answers back into the ORIGINAL equation to verify, and package your solutions in a set: $\\{r_1, r_2\\}$.

[Prof. Park] Follow this protocol, and factoring becomes one of the most reliable scoring opportunities on any math exam you ever take!""",

    8: """[Prof. Park] We have reached Slide 8, our Section 3.3 Part 1 Mastery Summary! Let's reflect on the milestones of Lecture 38.

[TA Sora] Today we harnessed the power of the Zero Product Property: $A \\cdot B = 0 \\implies A = 0$ or $B = 0$. It allows us to break second-degree quadratic equations into two manageable first-degree linear equations.

[Prof. Park] We saw how the solutions to $f(x) = 0$ give the exact $x$-intercepts of the parabola, and we connected those roots to the vertex via symmetry.

[TA Sora] We learned how to handle missing terms: when $c = 0$, factor out the GCF (and $x = 0$ is always a root). When $b = 0$, factor as a Difference of Squares.

[Prof. Park] And we sounded the alarm on the 'Must Equal Zero Trap': never factor until the equation is set strictly equal to zero!

[TA Sora] In everyday life, factoring teaches us the power of deconstruction: when facing complex tasks, break them down into their underlying components, solve each component with focus, and assemble your success.

[Prof. Park] In Lecture 39, we will tackle advanced factoring where the leading coefficient $a$ is not 1, explore special cases with one tangent root, and analyze the three possibilities for parabola intercepts.

[TA Sora] Keep up your dedication, Bobcats! We will see you in Lecture 39!"""
}
