# -*- coding: utf-8 -*-
"""
unit3_scripts_l39_l40.py
Full 20-25 Minute Broadcast Tiki-Taka Dialogue for Lectures 39 and 40
Prof. Eunju Park & TA Sora (Gallatin College Montana State University)
Each lecture contains 8 slides with ~300-380 words per slide (~2,500-2,800 words per lecture).
"""

SCRIPTS_L39 = {
    1: """[Prof. Park] Hello everyone, and welcome to Lecture 39 of M090 Introductory Algebra! I'm Professor Eunju Park, and joining me is our teaching assistant, Sora. Today we advance to Section 3.3 Part 2 on page 82 of your workbook—factoring when the leading coefficient $a$ is not 1.

[TA Sora] Welcome back, Bobcats! When $a = 1$, finding factors that add to $b$ and multiply to $c$ is relatively straightforward. But when $a \\neq 1$, such as in $2x^2 + 7x + 3 = 0$, that leading number 2 influences the middle term!

[Prof. Park] Let's look at Slide 1, Section 3.3 Example 5: Solve $2x^2 + 7x + 3 = 0$. Sora, what factoring method do you recommend for trinomials with $a \\neq 1$?

[TA Sora] I teach the 'ac-Method' (factoring by grouping)! Step 1: Multiply $a$ and $c$ together. Here $a = 2$ and $c = 3$, so $a \\times c = 2 \\times 3 = 6$. Now, we need two numbers that multiply to $+6$ and add to the middle coefficient $+7$!

[Prof. Park] What two numbers multiply to 6 and add to 7? That's 1 and 6! $1 \\times 6 = 6$, and $1 + 6 = 7$.

[TA Sora] Step 2: Split the middle term $7x$ using those two numbers: write $7x$ as $1x + 6x$ (or $6x + 1x$). Our equation becomes: $2x^2 + 6x + 1x + 3 = 0$!

[Prof. Park] Step 3: Now factor by grouping! Group the first two terms and the last two terms: from $2x^2 + 6x$, factor out $2x$, leaving $2x(x + 3)$. From $1x + 3$, factor out $+1$, leaving $+1(x + 3)$.

[TA Sora] Look at that common binomial factor: $(x + 3)$ appears in both groups! Factor out $(x + 3)$, and what remains is $(2x + 1)$. So our equation is $(2x + 1)(x + 3) = 0$!

[Prof. Park] Step 4: Apply the Zero Product Property: $2x + 1 = 0 \\implies 2x = -1 \\implies x = -1/2$. And $x + 3 = 0 \\implies x = -3$!

[TA Sora] Our two solutions are $x = -1/2$ and $x = -3$. Two clean roots found by structured grouping!""",

    2: """[Prof. Park] Turning to Slide 2, Example 6 asks us to find the $x$-intercepts for $g(x) = 3x^2 - 10x - 8$. Sora, let's guide our students through the ac-method with negative numbers!

[TA Sora] First, set $g(x) = 0$: $3x^2 - 10x - 8 = 0$. Step 1: Calculate $a \\times c$. Here $a = 3$ and $c = -8$, so $a \\times c = 3 \\times (-8) = -24$! We need two numbers that multiply to $-24$ and add to the middle coefficient $-10$.

[Prof. Park] Let's test pairs of factors of $-24$: how about $-12$ and $+2$? $-12 \\times 2 = -24$, and $-12 + 2 = -10$! They match the middle term perfectly!

[TA Sora] Step 2: Split the middle term $-10x$ into $-12x + 2x$: $3x^2 - 12x + 2x - 8 = 0$.

[Prof. Park] Step 3: Factor by grouping: from the first pair $3x^2 - 12x$, factor out $3x$: $3x(x - 4)$. From the second pair $2x - 8$, factor out $+2$: $+2(x - 4)$.

[TA Sora] The shared binomial is $(x - 4)$! Grouping gives: $(3x + 2)(x - 4) = 0$!

[Prof. Park] Step 4: Set each factor equal to zero: $3x + 2 = 0 \\implies 3x = -2 \\implies x = -2/3$. And $x - 4 = 0 \\implies x = 4$!

[TA Sora] So our $x$-intercepts as ordered pairs on the coordinate plane are $(-2/3, 0)$ and $(4, 0)$.

[Prof. Park] Look at how dependable the ac-method is: it eliminates all guessing. Solution set: $\\{-2/3, 4\\}$!""",

    3: """[Prof. Park] Slide 3 brings us to Example 7: $-x^2 + 4x + 5 = 0$. Sora, look at that leading coefficient: it is negative ($-1$). What is our immediate tactical move?

[TA Sora] Never factor a quadratic equation when the leading coefficient is negative! Factoring with a negative $a$ creates a nightmare of double negatives. Instead, multiply the ENTIRE equation on both sides by $-1$!

[Prof. Park] Let's multiply both sides by $-1$: $-1 \\cdot (-x^2 + 4x + 5) = -1 \\cdot 0$. Every single sign on the left flips: $x^2 - 4x - 5 = 0$!

[TA Sora] Look at how friendly that looks now! Now $a = +1$. We just need two numbers that multiply to $-5$ and add to $-4$. That's $-5$ and $+1$!

[Prof. Park] So it factors instantly into: $(x - 5)(x + 1) = 0$. Set each factor equal to zero: $x - 5 = 0 \\implies x = 5$, and $x + 1 = 0 \\implies x = -1$!

[TA Sora] The two roots are $x = 5$ and $x = -1$. 

[Prof. Park] Notice that multiplying by $-1$ does NOT change the roots! It flips the parabola upside down (from opening down to opening up), but both parabolas cross the ground at the exact same two points: $(-1, 0)$ and $(5, 0)$!

[TA Sora] Multiplying by $-1$ clears the fog. Always make $a$ positive before factoring!""",

    4: """[Prof. Park] On Slide 4, we examine a fascinating Special Case: When a Quadratic Has Exactly One $x$-Intercept. Look at $x^2 - 6x + 9 = 0$.

[TA Sora] Let's factor it: we need two numbers that multiply to $+9$ and add to $-6$. That is $-3$ and $-3$! So it factors into $(x - 3)(x - 3) = 0$, or $(x - 3)^2 = 0$!

[Prof. Park] When we apply the Zero Product Property, both factors yield the exact same solution: $x - 3 = 0 \\implies x = 3$. This is called a repeated root or a root of multiplicity 2!

[TA Sora] What does this look like geometrically on the coordinate grid? The parabola does NOT pass through the $x$-axis into negative territory! Instead, it sweeps down from above, touches the $x$-axis at the single point $(3, 0)$, and immediately turns around and bounces back up!

[Prof. Park] That single touch point is tangent to the axis! That means the $x$-intercept $(3, 0)$ IS the vertex of the parabola!

[TA Sora] Think of a basketball bouncing on the hardwood floor at the MSU Brick Breeden Fieldhouse. The ball touches the floor at one single instantaneous point and reverses direction.

[Prof. Park] Whenever you see a Perfect Square Trinomial like $(x - 3)^2 = 0$, the parabola has exactly one $x$-intercept, and that intercept is the vertex!""",

    5: """[Prof. Park] Slide 5 synthesizes 'The Three Possibilities for $x$-Intercepts of a Parabola.' Every quadratic function in the universe falls into one of these three geometric categories.

[TA Sora] Case 1: Exactly TWO Real $x$-Intercepts. This happens when the vertex lies on one side of the $x$-axis and the parabola opens towards the axis! The curve slices through the axis twice, like $f(x) = x^2 - 5x + 6$ with roots at $(2, 0)$ and $(3, 0)$.

[Prof. Park] Case 2: Exactly ONE Real $x$-Intercept. This happens when the vertex sits directly ON the $x$-axis ($y_v = 0$), like $f(x) = (x - 3)^2$. The vertex kisses the axis and turns around.

[TA Sora] Case 3: ZERO Real $x$-Intercepts. This happens when the vertex sits above the axis and opens upward (like $f(x) = x^2 + 4$), or sits below the axis and opens downward! The parabola never touches ground level!

[Prof. Park] In physics, if you model the trajectory of a spacecraft trying to enter planetary orbit: Case 1 means it crashes into the surface; Case 2 means it grazes the upper atmosphere at one point; Case 3 means it passes harmlessly above the planet!

[TA Sora] Looking at your vertex and direction of opening tells you immediately whether you will find 2 roots, 1 root, or 0 roots!""",

    6: """[Prof. Park] On Slide 6, we introduce Factored Form: $f(x) = a(x - r_1)(x - r_2)$. Sora, this is our third representation of a quadratic function, alongside General Form and Vertex Form!

[TA Sora] In Factored Form, the numbers $r_1$ and $r_2$ are the roots or $x$-intercepts! If a function is written as $f(x) = 2(x - 1)(x - 5)$, you know immediately that the $x$-intercepts are at $(1, 0)$ and $(5, 0)$!

[Prof. Park] And where is the Axis of Symmetry? It is always the average of the two roots: $x = (r_1 + r_2) / 2 = (1 + 5) / 2 = 6 / 2 = 3$!

[TA Sora] And to find the vertex height, just plug in $x = 3$: $f(3) = 2(3 - 1)(3 - 5) = 2(2)(-2) = -8$! The vertex is $(3, -8)$!

[Prof. Park] And what about the $y$-intercept? Plug in $x = 0$: $f(0) = 2(0 - 1)(0 - 5) = 2(-1)(-5) = +10$! The $y$-intercept is $(0, 10)$.

[TA Sora] Look at how fast you can graph an entire parabola when it is in factored form: you plot the two roots $(1, 0)$ and $(5, 0)$, the vertex $(3, -8)$, and the $y$-intercept $(0, 10)$, and your sketch is complete in under a minute!

[Prof. Park] Factored form is beloved by engineers because it directly reveals the operational thresholds where output is zero.""",

    7: """[Prof. Park] Slide 7 presents a 'Check Your Understanding' problem: Solve $3x^2 - 12 = 0$ by factoring.

[TA Sora] Step 1: Follow Sora's checklist—always look for a Greatest Common Factor (GCF) first! Both $3x^2$ and $12$ are divisible by 3. Factor out 3: $3(x^2 - 4) = 0$!

[Prof. Park] Step 2: Now look inside the parentheses: $x^2 - 4$ is a Difference of Squares! $x^2 - 2^2 = (x - 2)(x + 2)$. So our fully factored equation is: $3(x - 2)(x + 2) = 0$!

[TA Sora] Step 3: Apply the Zero Product Property! Can the number 3 equal zero? No, $3 \\neq 0$. So we set the variable factors equal to zero: $x - 2 = 0 \\implies x = 2$, and $x + 2 = 0 \\implies x = -2$!

[Prof. Park] Our two solutions are $x = 2$ and $x = -2$. Notice that factoring out the GCF made the Difference of Squares effortless!

[TA Sora] If someone forgot the GCF and tried to factor $3x^2 - 12$ directly, they would get confused. The GCF simplifies the numbers immediately.

[Prof. Park] Solution set: $\\{-2, 2\\}$. Clean, fast, and verified!""",

    8: """[Prof. Park] We have reached Slide 8, our Section 3.3 Complete Mastery Summary! 

[TA Sora] In Lecture 39, we mastered the ac-method for factoring when $a \\neq 1$, learned to flip signs by multiplying by $-1$, explored the tangent vertex special case with 1 root, analyzed the three possibilities for parabola intercepts, and used factored form $a(x - r_1)(x - r_2)$ to sketch graphs rapidly.

[Prof. Park] Remember: algebra is a toolkit of multiple strategies. When factoring is easy, use it! But what happens when an equation CANNOT be factored, like $x^2 + 6x - 7 = 0$ or $x^2 - 8x - 5 = 0$?

[TA Sora] That brings us to our next grand topic: Completing the Square in Lecture 40! Completing the square is the engine that proves the Quadratic Formula!

[Prof. Park] Complete the Section 3.3 practice exercises on pages 82 through 85 of your workbook tonight.

[TA Sora] Keep up the incredible momentum, Bobcats! We will see you all in Lecture 40!"""
}

SCRIPTS_L40 = {
    1: """[Prof. Park] Welcome back to M090, Bobcats! I am Professor Eunju Park, and with me is our course teaching assistant, Sora. Today we enter Lecture 40 and Section 3.4 on page 86 of your workbook: Completing the Square.

[TA Sora] Hello everyone! Section 3.4 is one of the most intellectually rewarding topics in all of algebra. So far, we've solved quadratics using the Square Root Property (when $b = 0$) and Factoring (when numbers factor nicely). But what if a quadratic doesn't factor, and $b \\neq 0$?

[Prof. Park] That's where Completing the Square comes in. It is a brilliant mathematical technique that allows us to take ANY quadratic expression, no matter how stubborn or messy, and physically reshape it into a perfect binomial square of the form $(x + d)^2$!

[TA Sora] And once it is packaged as a binomial square $(x + d)^2 = k$, we can solve it instantly using the Square Root Property from Section 3.2! Completing the Square is the bridge that turns an impossible factoring problem into a simple square root problem!

[Prof. Park] Think about carpentry and tile work in Bozeman homes. If you have an L-shaped room of tiles measuring $x^2 + bx$, it is almost a complete square, but it has a missing corner! Completing the square literally calculates the exact missing tile piece needed to complete the square!

[TA Sora] Turn to page 86 in your workbook. Let's find that missing corner piece—the 'Magic Number'—on Slide 2!""",

    2: """[Prof. Park] Slide 2 introduces the heart of this section: Finding the 'Magic Number' that completes the square for $x^2 + bx$.

[TA Sora] Here is the universal formula: to complete the square for $x^2 + bx$, you take half of the linear coefficient $b$, and square it! The magic number is $(b/2)^2$!

[Prof. Park] Let's say that together: 'Half of $b$, squared!' Once you add $(b/2)^2$, the expression $x^2 + bx + (b/2)^2$ factors automatically into $(x + b/2)^2$!

[TA Sora] Let's practice with three quick examples: Example A: $x^2 + 8x$. What is half of 8? It's 4. What is $4^2$? 16! Add 16, and you get $x^2 + 8x + 16 = (x + 4)^2$!

[Prof. Park] Example B: $x^2 - 10x$. What is half of $-10$? It's $-5$. What is $(-5)^2$? $+25$! Notice the added number is ALWAYS positive because squaring any real number produces a positive! So $x^2 - 10x + 25 = (x - 5)^2$!

[TA Sora] Example C: $x^2 + 5x$. What is half of 5? It's $5/2$. What is $(5/2)^2$? $25/4$! So $x^2 + 5x + 25/4 = (x + 5/2)^2$!

[Prof. Park] Notice the pattern: inside the binomial square, the number is always $b/2$, including its sign! If $b$ is positive, it's $(x + b/2)^2$; if $b$ is negative, it's $(x - |b/2|)^2$.

[TA Sora] Master that phrase: 'Half of $b$, squared!' That magic number unlocks everything!""",

    3: """[Prof. Park] On Slide 3, Section 3.4 Example 2 puts this to work on a full equation: Solve $x^2 + 6x = 7$ by completing the square.

[TA Sora] Step 1: The variable terms $x^2 + 6x$ are already isolated on the left side, and the constant 7 is on the right side. That is our ideal starting position!

[Prof. Park] Step 2: Find the magic number! Here $b = 6$. Take half of 6: $6 / 2 = 3$. Square it: $3^2 = 9$!

[TA Sora] Step 3: The Golden Equation Rule! Whatever you add to the left side, you MUST add to the right side to keep the equation balanced! Add 9 to both sides: $x^2 + 6x + 9 = 7 + 9$!

[Prof. Park] Step 4: The left side factors automatically into $(x + 3)^2$, and the right side is $7 + 9 = 16$! Look at our equation now: $(x + 3)^2 = 16$!

[TA Sora] Look at that transformation! It is now an isolated binomial square equal to 16, exactly like our problems from Section 3.2!

[Prof. Park] Step 5: Apply the Square Root Property: $x + 3 = \\pm \\sqrt{16} = \\pm 4$. Subtract 3: $x = -3 \\pm 4$!

[TA Sora] Step 6: Branch out! $x = -3 + 4 = 1$, and $x = -3 - 4 = -7$!

[Prof. Park] Our two solutions are $x = 1$ and $x = -7$. Let's check $x = 1$: $1^2 + 6(1) = 1 + 6 = 7$ (True!). For $x = -7$: $(-7)^2 + 6(-7) = 49 - 42 = 7$ (True!).

[TA Sora] Completing the square took a general equation and converted it into a square root problem. Solution set: $\\{-7, 1\\}$!""",

    4: """[Prof. Park] Slide 4 presents Example 3: Solve $x^2 - 8x - 5 = 0$. Sora, notice that this equation cannot be factored over integers because no factors of $-5$ add to $-8$!

[TA Sora] This is where Completing the Square proves its true worth! It doesn't care if numbers factor or not; it works every single time!

[Prof. Park] Step 1: Move the constant term to the right side by adding 5 to both sides: $x^2 - 8x = 5$.

[TA Sora] Step 2: Find the magic number! $b = -8$. Half of $-8$ is $-4$. Square it: $(-4)^2 = +16$!

[Prof. Park] Step 3: Add 16 to BOTH sides of the equation: $x^2 - 8x + 16 = 5 + 16$!

[TA Sora] Step 4: Package the left side as a square: $(x - 4)^2$. Simplify the right side: $5 + 16 = 21$! Our equation is $(x - 4)^2 = 21$!

[Prof. Park] Step 5: Apply the Square Root Property: $x - 4 = \\pm \\sqrt{21}$. Add 4 to both sides: $x = 4 \\pm \\sqrt{21}$!

[TA Sora] Since 21 has no perfect square factors ($21 = 3 \\times 7$), $\\sqrt{21}$ cannot be simplified. Our exact solutions are $x = 4 + \\sqrt{21}$ and $x = 4 - \\sqrt{21}$!

[Prof. Park] And in decimal form: $\\sqrt{21} \\approx 4.58$, so $x \\approx 4 + 4.58 = 8.58$, and $x \\approx 4 - 4.58 = -0.58$.

[TA Sora] Factoring was completely helpless on this problem, but Completing the Square solved it without breaking a sweat! Solution set: $\\{4 - \\sqrt{21}, 4 + \\sqrt{21}\\}$. Total victory!""",

    5: """[Prof. Park] On Slide 5, Example 4 raises the difficulty bar: Solve $2x^2 - 12x + 10 = 0$. Sora, look at the leading coefficient: $a = 2$. Can we complete the square while $a = 2$?

[TA Sora] Absolutely not! This is the #1 rule of Completing the Square: 'The leading coefficient MUST be 1 before you take half of $b$!' If $a$ is not 1, your magic number formula will fail!

[Prof. Park] So what is our mandatory first move? Divide every single term on both sides of the equation by 2! Let's do that: $2x^2 / 2 - 12x / 2 + 10 / 2 = 0 / 2$, which gives $x^2 - 6x + 5 = 0$!

[TA Sora] Look at how clean that is now: $a = 1$! Step 2: Move the constant $+5$ to the right side by subtracting 5: $x^2 - 6x = -5$.

[Prof. Park] Step 3: Find the magic number! $b = -6$. Half of $-6$ is $-3$. Square it: $(-3)^2 = 9$. Add 9 to both sides: $x^2 - 6x + 9 = -5 + 9$!

[TA Sora] Step 4: Package the left side as a square: $(x - 3)^2 = 4$!

[Prof. Park] Step 5: Apply the Square Root Property: $x - 3 = \\pm \\sqrt{4} = \\pm 2$. Add 3: $x = 3 \\pm 2$!

[TA Sora] Step 6: Branch out! $x = 3 + 2 = 5$, and $x = 3 - 2 = 1$!

[Prof. Park] Our two solutions are $x = 5$ and $x = 1$. Let's check $x = 1$: $2(1)^2 - 12(1) + 10 = 2 - 12 + 10 = 0$ (True!).

[TA Sora] Always divide by $a$ first if $a \\neq 1$. That keeps your path clear and your calculations accurate! Solution set: $\\{1, 5\\}$.""",

    6: """[Prof. Park] Slide 6 reveals a magnificent application of Completing the Square: Converting General Form $f(x) = ax^2 + bx + c$ into Vertex Form $f(x) = a(x - h)^2 + k$!

[TA Sora] In Section 3.1, we loved vertex form because the vertex $(h, k)$ was obvious. Now, Completing the Square gives us the exact tool to create vertex form whenever we want!

[Prof. Park] Let's convert $f(x) = x^2 - 6x + 13$ into vertex form: Step 1: Group the $x$ terms together and leave a space for the magic number: $f(x) = (x^2 - 6x + \\underline{\\quad}) + 13$.

[TA Sora] Step 2: Find the magic number! Half of $-6$ is $-3$, and $(-3)^2 = 9$. We add 9 inside the parentheses. But wait! Since this is an expression on one side of a function, if we add 9, we must simultaneously SUBTRACT 9 to keep the function equal!

[Prof. Park] Exactly! Add 9 and subtract 9: $f(x) = (x^2 - 6x + 9) + 13 - 9$.

[TA Sora] Step 3: Package the trinomial into a square: $(x - 3)^2$. Combine the numbers outside: $13 - 9 = +4$!

[Prof. Park] Look at our result: $f(x) = (x - 3)^2 + 4$! We have converted the general form into pristine vertex form!

[TA Sora] And what can we read immediately from $(x - 3)^2 + 4$? The vertex is $(3, 4)$, the axis of symmetry is $x = 3$, and the minimum value is 4!

[Prof. Park] Completing the square is not just a solving method; it is a structural transformation tool.""",

    7: """[Prof. Park] Slide 7 presents 'Sora's Complete CTS Protocol.' Here is the master 5-step checklist for Completing the Square.

[TA Sora] Step 1: 'Make $a = 1$.' If there is a leading coefficient $a \\neq 1$, divide every term in the equation by $a$.

[Prof. Park] Step 2: 'Isolate Variables.' Move the constant term to the right side of the equals sign: $x^2 + bx = \\text{constant}$.

[TA Sora] Step 3: 'The Magic Number.' Calculate $(b/2)^2$. Add this magic number to BOTH sides of the equation without fail!

[Prof. Park] Step 4: 'Package the Square.' Rewrite the left side as $(x + b/2)^2$, and simplify the numerical sum on the right side.

[TA Sora] Step 5: 'Square Root & Solve.' Apply the Square Root Property: $x + b/2 = \\pm \\sqrt{k}$. Subtract $b/2$ to find your final exact solutions: $x = -b/2 \\pm \\sqrt{k}$!

[Prof. Park] Look at that final formula: $x = -b/2 \\pm \\sqrt{k}$. Notice that $-b/2$! It is the exact same structure as the Quadratic Formula!

[TA Sora] Practice this 5-step checklist until you can write it in your sleep!""",

    8: """[Prof. Park] We have arrived at Slide 8, our Section 3.4 Mastery Summary and the Gateway to the Quadratic Formula!

[TA Sora] What a milestone today was! Completing the Square gives us universal power: it solves any quadratic equation, regardless of whether it factors.

[Prof. Park] We learned that adding $(b/2)^2$ to both sides transforms $x^2 + bx$ into $(x + b/2)^2$. We used it to solve equations with irrational roots like $4 \\pm \\sqrt{21}$, and we used it to convert general form into vertex form.

[TA Sora] And here is the grand historical reveal: If you take the literal general quadratic equation $ax^2 + bx + c = 0$ with unknown letters $a$, $b$, and $c$, and you apply our 5-step Completing the Square protocol to it...

[Prof. Park] Out pops the most famous formula in the history of mathematics: $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$—The Quadratic Formula!

[TA Sora] That's right! In Lecture 41, we will unleash the Quadratic Formula, knowing that its beating heart was born right here in Completing the Square.

[Prof. Park] Complete your Section 3.4 homework on pages 86 through 89 tonight. Be proud of the immense mathematical strength you are developing.

[TA Sora] Keep shining, Bobcats! We will see you in Lecture 41 for the Quadratic Formula!"""
}
