import fs from 'fs';
import path from 'path';

const filePath = path.resolve('src/data/montanaSlidesData.js');
let fileContent = fs.readFileSync(filePath, 'utf8');

// Key: `${lecNum}_${slideNum}` -> new script text
const updates = {
  // L31
  '31_5': `[Prof. Park] Slide 5 brings us to Section 3.0 Example 3 on page 60: $f(x) = -2 - 3x + \\frac{x^2}{3}$. Sora, what trap must students avoid here immediately?

[TA Sora] Do NOT just read coefficients from left to right! The constant $-2$ is listed first, and the squared term $\\frac{x^2}{3}$ is waiting at the very end!

[Prof. Park] Exactly right. Standard general form requires descending order of powers: $ax^2 + bx + c$. Let's rewrite it: $f(x) = \\frac{1}{3}x^2 - 3x - 2$.

[TA Sora] Now everything is clear: $a = \\frac{1}{3}$, $b = -3$, and $c = -2$!

[Prof. Park] Next, does the parabola open upward or downward? Since $a = \\frac{1}{3}$, which is positive ($a > 0$), the parabola opens upward like a cup!

[TA Sora] And because it opens upward, the vertex sits at the lowest point, meaning the vertex represents a MINIMUM value!

[Prof. Park] Finally, what is the $y$-intercept? When $x = 0$, $f(0) = -2$, so the $y$-intercept is the coordinate point $(0, -2)$.

[TA Sora] Always reorder terms from highest power to lowest power first before extracting $a$, $b$, and $c$!`,

  '31_6': `[Prof. Park] On Slide 6, Example 4 asks us to classify two functions: $f(x) = 4x + 7$ and $g(x) = -x^2 + 5$. Sora, how do we distinguish linear from quadratic?

[TA Sora] Look at the highest exponent of $x$—that is the degree! If the degree is 1, it is linear. If the degree is 2, it is quadratic!

[Prof. Park] Exactly. In $f(x) = 4x + 7$, $x$ has an exponent of 1. That makes $f(x)$ a linear function, and its graph is a straight line with slope 4 and $y$-intercept $(0, 7)$.

[TA Sora] Now examine $g(x) = -x^2 + 5$. The highest power of $x$ is 2! That makes $g(x)$ a quadratic function!

[Prof. Park] Notice also that in $g(x) = -x^2 + 5$, there is no linear $x$ term, so $b = 0$. And $a = -1 < 0$, so its graph is a parabola opening downward with vertex at $(0, 5)$.

[TA Sora] Degree 1 produces a straight line, while degree 2 gives us the iconic curved parabola!`,

  // L32
  '32_2': `[Prof. Park] Slide 2 presents Section 3.0 Example 5 Part 1 on page 61: For $f(x) = x^2 - 6x + 5$, find the $y$-intercept and the $x$-intercepts. Sora, let's start with the $y$-intercept.

[TA Sora] The $y$-intercept is always effortless! Set $x = 0$: $f(0) = 0^2 - 6(0) + 5 = 5$. So the $y$-intercept is $(0, 5)$! It is simply the constant term $c$.

[Prof. Park] Now for Part B: to find the $x$-intercepts, we set the function value equal to zero: $x^2 - 6x + 5 = 0$. How should we solve this?

[TA Sora] Factoring! We need two numbers that multiply to $+5$ and add up to $-6$. Those numbers are $-1$ and $-5$!

[Prof. Park] That gives $(x - 1)(x - 5) = 0$. By the Zero-Product Property, $x - 1 = 0$ gives $x = 1$, and $x - 5 = 0$ gives $x = 5$.

[TA Sora] As complete coordinate pairs, our $x$-intercepts are $(1, 0)$ and $(5, 0)$!

[Prof. Park] We now have three critical points: $(0, 5)$, $(1, 0)$, and $(5, 0)$. Next, let's find the vertex on Slide 3!`,

  '32_3': `[Prof. Park] Continuing with $f(x) = x^2 - 6x + 5$ on Slide 3, Part 2 asks us for the Axis of Symmetry and the Vertex. Sora, how can we use our $x$-intercepts from Slide 2?

[TA Sora] Because a parabola is perfectly symmetrical, the axis of symmetry is always halfway between the $x$-intercepts $x = 1$ and $x = 5$! The midpoint is $\\frac{1 + 5}{2} = 3$!

[Prof. Park] And applying our formula $x = -\\frac{b}{2a} = -\\frac{-6}{2(1)} = 3$ confirms the Axis of Symmetry is the vertical line $x = 3$.

[TA Sora] Now substitute $x = 3$ into $f(x)$ to get the vertex height: $f(3) = 3^2 - 6(3) + 5 = 9 - 18 + 5 = -4$!

[Prof. Park] That gives the vertex $(3, -4)$. Since $a = 1 > 0$, the parabola opens upward, so the vertex is a minimum.

[TA Sora] The minimum value is $-4$, occurring at $x = 3$! Vertex at $(3, -4)$ and line of symmetry at $x = 3$.`,

  // L33
  '33_1': `[Prof. Park] Hello Bobcats, and welcome to Lecture 33! On Slide 1, Example 7 Parts A and B ask us to evaluate $g(-1)$ and $h(-1)$ for $g(x) = -x^2 + 2x + 7$ and $h(x) = 3(x - 2)^2 - 4$. Sora, watch out for negative signs!

[TA Sora] Part A is where so many students slip up! When evaluating $g(-1)$, write $-(-1)^2 + 2(-1) + 7$. Notice the negative is OUTSIDE the square: $(-1)^2 = 1$, then apply the negative to get $-1$!

[Prof. Park] Exactly. $-1 + (-2) + 7 = 4$. So $g(-1) = 4$.

[TA Sora] Now for Part B with $h(x) = 3(x - 2)^2 - 4$: plug in $-1$: $h(-1) = 3(-1 - 2)^2 - 4 = 3(-3)^2 - 4$.

[Prof. Park] Follow order of operations: square $-3$ first to get $+9$. Then $3(9) = 27$, and $27 - 4 = 23$. So $h(-1) = 23$!

[TA Sora] Clean execution: $g(-1) = 4$ and $h(-1) = 23$!`,

  '33_2': `[Prof. Park] Slide 2 brings us to Parts C and D: evaluating at zero, $g(0)$ and $h(0)$, which gives the $y$-intercept of each function!

[TA Sora] For $g(x) = -x^2 + 2x + 7$, setting $x = 0$ wipes out the first two terms: $g(0) = -(0)^2 + 2(0) + 7 = 7$. The $y$-intercept is $(0, 7)$!

[Prof. Park] Now look closely at Part D with $h(x) = 3(x - 2)^2 - 4$. Sora, why is $h(0)$ NOT simply $-4$?

[TA Sora] That is a huge trap! Because $h(x)$ is in vertex form, setting $x = 0$ leaves $(0 - 2)^2$, which is $(-2)^2 = 4$!

[Prof. Park] Yes: $h(0) = 3(4) - 4 = 12 - 4 = 8$. The $y$-intercept of $h$ is $(0, 8)$, not $(0, -4)$!

[TA Sora] Always compute $f(0)$ algebraically rather than guessing from vertex form!`,

  '33_3': `[Prof. Park] On Slide 3, Part E tests our fraction arithmetic skills: evaluating $h(5/2)$ for $h(x) = 3(x - 2)^2 - 4$. Sora, let's guide students through the common denominator.

[TA Sora] Step 1: Substitute $\\frac{5}{2}$ into the parentheses: $\\frac{5}{2} - 2 = \\frac{5}{2} - \\frac{4}{2} = \\frac{1}{2}$!

[Prof. Park] Step 2: Square that fraction: $(\\frac{1}{2})^2 = \\frac{1}{4}$.

[TA Sora] Step 3: Multiply by the coefficient 3: $3 \\cdot \\frac{1}{4} = \\frac{3}{4}$.

[Prof. Park] Step 4: Subtract 4: $\\frac{3}{4} - 4 = \\frac{3}{4} - \\frac{16}{4} = -\\frac{13}{4}$, which is $-3.25$.

[TA Sora] Keep your fractions intact until the very end: $h(5/2) = -\\frac{13}{4}$!`,

  '33_4': `[Prof. Park] Turning to Slide 4, Part F asks us to evaluate $g(a)$ for $g(x) = -x^2 + 2x + 7$. Sora, students often wonder what to compute when the input is a letter.

[TA Sora] Treat the variable $a$ just like a number! Everywhere you see $x$, replace it with $a$: $g(a) = -(a)^2 + 2(a) + 7 = -a^2 + 2a + 7$!

[Prof. Park] Exactly. You cannot combine terms because they have different powers, so $-a^2 + 2a + 7$ is the complete and final simplified answer.

[TA Sora] The function formula is a template—whatever is inside the parentheses replaces every $x$!`,

  '33_5': `[Prof. Park] Slide 5 presents Part G: evaluating $g(x - 6)$ for $g(x) = -x^2 + 2x + 7$. Now the input is a binomial!

[TA Sora] Substitute $(x - 6)$ everywhere: $g(x - 6) = -(x - 6)^2 + 2(x - 6) + 7$.

[Prof. Park] Careful with $(x - 6)^2$: expand it as $x^2 - 12x + 36$. Then distribute the outside negative sign: $-(x^2 - 12x + 36) = -x^2 + 12x - 36$.

[TA Sora] Next distribute the $+2$: $2(x - 6) = 2x - 12$. Now combine all like terms: $-x^2 + (12x + 2x) + (-36 - 12 + 7)$.

[Prof. Park] $12x + 2x = 14x$, and $-36 - 12 + 7 = -41$. So $g(x - 6) = -x^2 + 14x - 41$!

[TA Sora] Beautiful algebraic distribution and combining like terms!`,

  '33_6': `[Prof. Park] On Slide 6, Part H gives us our final challenge: evaluate $h(k + 1)$ for $h(x) = 3(x - 2)^2 - 4$.

[TA Sora] Substitute $(k + 1)$ for $x$: $h(k + 1) = 3((k + 1) - 2)^2 - 4$. Inside the parentheses, simplify first: $(k + 1) - 2 = k - 1$!

[Prof. Park] That simplifies the expression to $3(k - 1)^2 - 4$. Now expand $(k - 1)^2 = k^2 - 2k + 1$.

[TA Sora] Distribute the 3: $3(k^2 - 2k + 1) = 3k^2 - 6k + 3$. Finally, subtract 4: $3 - 4 = -1$.

[Prof. Park] Our final simplified result is $h(k + 1) = 3k^2 - 6k - 1$.

[TA Sora] Simplifying inside parentheses first saved us so much work! Section 3.0 evaluation mastered!`,

  // L35
  '35_5': `[Prof. Park] Slide 5 presents Section 3.1 Example 7 (Part 1) on page 66: a comprehensive analysis of $f(x) = -x^2 - 4x - 5$. Sora, let's determine the key features.

[TA Sora] Let's list our coefficients: $a = -1$, $b = -4$, and $c = -5$. First, the $y$-intercept is $(0, c)$, so it is $(0, -5)$!

[Prof. Park] Next, the vertex: $x_v = -\\frac{b}{2a} = -\\frac{-4}{2(-1)} = \\frac{4}{-2} = -2$. Now evaluate $f(-2)$: $-(-2)^2 - 4(-2) - 5 = -4 + 8 - 5 = -1$. So the vertex is $(-2, -1)$!

[TA Sora] Since $a = -1 < 0$, the parabola opens downward, and the axis of symmetry is the line $x = -2$. The maximum value of the function is $-1$!

[Prof. Park] Now what about the $x$-intercepts? If we set $-x^2 - 4x - 5 = 0$, the discriminant is $b^2 - 4ac = (-4)^2 - 4(-1)(-5) = 16 - 20 = -4 < 0$!

[TA Sora] Because the peak is at $y = -1$ and it opens downward, the curve NEVER reaches the $x$-axis! There are NO real $x$-intercepts!

[Prof. Park] An essential observation: not every parabola crosses the $x$-axis!`,

  '35_6': `[Prof. Park] On Slide 6, we evaluate specific function values for $f(x) = -x^2 - 4x - 5$ to interrogate its behavior on the coordinate plane.

[TA Sora] Part G: find $f(-4)$. Substitute $-4$: $f(-4) = -(-4)^2 - 4(-4) - 5 = -16 + 16 - 5 = -5$! Notice that $(-4, -5)$ is symmetric to our $y$-intercept $(0, -5)$ across $x = -2$!

[Prof. Park] Part H asks: if $f(x) = -2$, what is $x$? Set $-x^2 - 4x - 5 = -2$. Add 2 to both sides: $-x^2 - 4x - 3 = 0$, or $x^2 + 4x + 3 = 0$.

[TA Sora] Factor that into $(x + 1)(x + 3) = 0$, giving $x = -1$ and $x = -3$! Both points have a height of $-2$.

[Prof. Park] Part I: $f(0) = -5$, our $y$-intercept. And Part J: $f(x) = -5$ gives $-x^2 - 4x - 5 = -5 \\implies -x^2 - 4x = 0 \\implies -x(x + 4) = 0$, so $x = 0$ or $x = -4$!

[TA Sora] Everything connects through the axis of symmetry $x = -2$! Perfectly verified.`,

  // L36
  '36_5': `[Prof. Park] Turning to Slide 5, Section 3.2 Example 3 connects solving directly to graphing: For the function $f(x) = x^2 - 36$, find the $x$-intercepts and the vertex.

[TA Sora] To find the $x$-intercepts, set $f(x) = 0$: $x^2 - 36 = 0$. Using the Square Root Property: $x^2 = 36$, so $x = \\pm \\sqrt{36} = \\pm 6$!

[Prof. Park] So the two $x$-intercepts are $(6, 0)$ and $(-6, 0)$.

[TA Sora] Now for the vertex: notice there is no linear $x$ term, so $b = 0$. That means $x_v = -\\frac{0}{2(1)} = 0$!

[Prof. Park] Evaluating $f(0) = 0^2 - 36 = -36$. The vertex is located at $(0, -36)$, which is also the $y$-intercept!

[TA Sora] Because $a = 1 > 0$, the parabola opens upward from $(0, -36)$, crossing the horizontal axis at $-6$ and $+6$!`,

  '36_6': `[Prof. Park] Slide 6 presents Example 4: For $g(x) = 3x^2 - 27$, find the $x$-intercepts and the vertex. Sora, what is our first move?

[TA Sora] Set $g(x) = 0$: $3x^2 - 27 = 0$. Add 27 to both sides: $3x^2 = 27$. Remember to isolate $x^2$ before taking square roots—divide both sides by 3 to get $x^2 = 9$!

[Prof. Park] Now apply the Square Root Property: $x = \\pm \\sqrt{9} = \\pm 3$. That gives $x$-intercepts at $(3, 0)$ and $(-3, 0)$.

[TA Sora] And for the vertex, since $b = 0$, $x = 0$. $g(0) = 3(0)^2 - 27 = -27$. The vertex is $(0, -27)$!

[Prof. Park] The curve has its minimum at $(0, -27)$ and passes symmetrically through $(-3, 0)$ and $(3, 0)$. Clean, rapid execution!`,

  // L38
  '38_3': `[Prof. Park] On Slide 3, Section 3.3 Example 2 asks us to find the $x$-intercepts and vertex for $f(x) = x^2 + 7x + 12$.

[TA Sora] Let's find the $x$-intercepts first by setting $f(x) = 0$: $x^2 + 7x + 12 = 0$. We need two numbers that multiply to $+12$ and add up to $+7$. Those are $+3$ and $+4$!

[Prof. Park] So we factor it into $(x + 3)(x + 4) = 0$. By the Zero-Product Property, $x + 3 = 0 \\implies x = -3$, and $x + 4 = 0 \\implies x = -4$. The $x$-intercepts are $(-3, 0)$ and $(-4, 0)$.

[TA Sora] Now for the vertex: the axis of symmetry is halfway between $-3$ and $-4$, which is $x = -3.5$, or $-\\frac{7}{2}$!

[Prof. Park] Plugging $x = -3.5$ into $f(x)$: $(-3.5)^2 + 7(-3.5) + 12 = 12.25 - 24.5 + 12 = -0.25$. So the vertex is $(-3.5, -0.25)$.

[TA Sora] Both intercepts $(-3, 0)$ and $(-4, 0)$ and the vertex $(-3.5, -0.25)$ are verified!`,

  // L40
  '40_5': `[Prof. Park] On Slide 5, Example 4 raises the difficulty bar: Solve $2x^2 + 12x - 10 = 0$. Sora, look at the leading coefficient: $a = 2$. Can we complete the square while $a = 2$?

[TA Sora] Absolutely not! The #1 rule of Completing the Square is: 'The leading coefficient MUST be 1 before you take half of $b$!' If $a \\neq 1$, divide first!

[Prof. Park] So divide every term on both sides by 2: $\\frac{2x^2}{2} + \\frac{12x}{2} - \\frac{10}{2} = 0$, giving $x^2 + 6x - 5 = 0$.

[TA Sora] Step 2: Move the constant $-5$ to the right side: $x^2 + 6x = 5$.

[Prof. Park] Step 3: Find the magic number! $b = 6$. Half of 6 is 3. Square it: $3^2 = 9$. Add 9 to both sides: $x^2 + 6x + 9 = 5 + 9 = 14$!

[TA Sora] Step 4: Write the left side as a binomial square: $(x + 3)^2 = 14$!

[Prof. Park] Step 5: Take the square root of both sides: $x + 3 = \\pm \\sqrt{14}$. Subtract 3: $x = -3 \\pm \\sqrt{14}$!

[TA Sora] Exact radical solution set: $\\{-3 - \\sqrt{14}, -3 + \\sqrt{14}\\}$. Always divide by $a$ first!`,

  // L41
  '41_3': `[Prof. Park] Slide 3 brings us to Example 2: Find the intercepts and vertex for $h(x) = x^2 - 5x - 7$. Sora, let's identify $a$, $b$, and $c$.

[TA Sora] Coefficients: $a = 1$, $b = -5$, and $c = -7$. Be extra careful with the negative signs when plugging into the Quadratic Formula!

[Prof. Park] $x = \\frac{-(-5) \\pm \\sqrt{(-5)^2 - 4(1)(-7)}}{2(1)} = \\frac{5 \\pm \\sqrt{25 + 28}}{2} = \\frac{5 \\pm \\sqrt{53}}{2}$.

[TA Sora] Since 53 is a prime number, $\\frac{5 \\pm \\sqrt{53}}{2}$ is the exact radical answer! In decimals, $\\sqrt{53} \\approx 7.28$, so $x \\approx 6.14$ and $x \\approx -1.14$.

[Prof. Park] Now for the vertex: $x_v = -\\frac{b}{2a} = -\\frac{-5}{2(1)} = 2.5$. $h(2.5) = (2.5)^2 - 5(2.5) - 7 = 6.25 - 12.5 - 7 = -13.25$.

[TA Sora] Vertex is $(2.5, -13.25)$ and $y$-intercept is $(0, -7)$! Complete analysis accomplished.`,

  '41_4': `[Prof. Park] On Slide 4, Example 3 gives us: $h(x) = 13x - x^2 + 1$. Sora, what must we do before applying the formula?

[TA Sora] Rewrite it in standard descending form: $h(x) = -x^2 + 13x + 1$! So $a = -1$, $b = 13$, and $c = 1$.

[Prof. Park] Now set it equal to zero and apply the formula: $x = \\frac{-13 \\pm \\sqrt{13^2 - 4(-1)(1)}}{2(-1)} = \\frac{-13 \\pm \\sqrt{169 + 4}}{-2} = \\frac{-13 \\pm \\sqrt{173}}{-2}$.

[TA Sora] Divide top and bottom by $-1$: $x = \\frac{13 \\pm \\sqrt{173}}{2}$! Since $\\sqrt{173} \\approx 13.15$, our solutions are $x \\approx 13.08$ and $x \\approx -0.08$.

[Prof. Park] And the vertex: $x_v = -\\frac{13}{2(-1)} = 6.5$. $h(6.5) = 13(6.5) - (6.5)^2 + 1 = 84.5 - 42.25 + 1 = 43.25$.

[TA Sora] Vertex is $(6.5, 43.25)$, a high maximum since $a = -1 < 0$!`,

  '41_5': `[Prof. Park] Slide 5 presents Example 4: Find the intercepts and vertex for $f(x) = -x^2 - 5x + 7$. Sora, let's identify the parameters.

[TA Sora] Here $a = -1$, $b = -5$, and $c = 7$.

[Prof. Park] Set $f(x) = 0$: $x = \\frac{-(-5) \\pm \\sqrt{(-5)^2 - 4(-1)(7)}}{2(-1)} = \\frac{5 \\pm \\sqrt{25 + 28}}{-2} = \\frac{5 \\pm \\sqrt{53}}{-2}$.

[TA Sora] Using $\\sqrt{53} \\approx 7.28$, $\\frac{5 + 7.28}{-2} \\approx -6.14$, and $\\frac{5 - 7.28}{-2} \\approx 1.14$!

[Prof. Park] And the vertex: $x_v = -\\frac{-5}{2(-1)} = -2.5$. $f(-2.5) = -(-2.5)^2 - 5(-2.5) + 7 = -6.25 + 12.5 + 7 = 13.25$.

[TA Sora] The vertex is $(-2.5, 13.25)$ and the $y$-intercept is $(0, 7)$. Exact and decimal forms mastered!`,

  '41_6': `[Prof. Park] On Slide 6, Example 5 asks us to find intercepts and vertex for $f(x) = -1 + 2x^2 - 3x$. Sora, let's standardize this first.

[TA Sora] Standard form is $f(x) = 2x^2 - 3x - 1$. So $a = 2$, $b = -3$, and $c = -1$.

[Prof. Park] Set $f(x) = 0$: $x = \\frac{-(-3) \\pm \\sqrt{(-3)^2 - 4(2)(-1)}}{2(2)} = \\frac{3 \\pm \\sqrt{9 + 8}}{4} = \\frac{3 \\pm \\sqrt{17}}{4}$.

[TA Sora] With $\\sqrt{17} \\approx 4.12$, $x \\approx \\frac{3 + 4.12}{4} \\approx 1.78$ and $x \\approx \\frac{3 - 4.12}{4} \\approx -0.28$!

[Prof. Park] For the vertex: $x_v = -\\frac{-3}{2(2)} = 0.75$. $f(0.75) = 2(0.75)^2 - 3(0.75) - 1 = 1.125 - 2.25 - 1 = -2.125$.

[TA Sora] Vertex is $(0.75, -2.125)$ and $y$-intercept is $(0, -1)$!`,

  '41_7': `[Prof. Park] Slide 7 provides an evaluation and solving challenge with $f(x) = 3x^2 - 5x + 7$. Sora, let's walk through Parts A, B, C, and D.

[TA Sora] Part A: $f(4) = 3(4)^2 - 5(4) + 7 = 3(16) - 20 + 7 = 48 - 20 + 7 = 35$! Part B: $f(p) = 3p^2 - 5p + 7$.

[Prof. Park] Part C: $f(x + 3) = 3(x + 3)^2 - 5(x + 3) + 7 = 3(x^2 + 6x + 9) - 5x - 15 + 7 = 3x^2 + 18x + 27 - 5x - 8 = 3x^2 + 13x + 19$.

[TA Sora] And Part D: Solve $f(x) = 13$! Set $3x^2 - 5x + 7 = 13$. Subtract 13: $3x^2 - 5x - 6 = 0$!

[Prof. Park] Now apply the Quadratic Formula with $a = 3, b = -5, c = -6$: $x = \\frac{5 \\pm \\sqrt{25 - 4(3)(-6)}}{6} = \\frac{5 \\pm \\sqrt{25 + 72}}{6} = \\frac{5 \\pm \\sqrt{97}}{6} \\approx 2.47$ and $-0.81$.

[TA Sora] That covers all four parts with precision!`,

  // L42
  '42_4': `[Prof. Park] On Slide 4, Example 7 tests: $f(x) = x^2 + 2x + 5$. Sora, let's see what the discriminant reveals here!

[TA Sora] Step 1: Identify coefficients: $a = 1$, $b = 2$, and $c = 5$.

[Prof. Park] Step 2: Compute $\\Delta = b^2 - 4ac = 2^2 - 4(1)(5) = 4 - 20 = -16$!

[TA Sora] Look at that: $\\Delta = -16$, which is strictly negative ($\\Delta < 0$)!

[Prof. Park] Because you cannot take the square root of a negative number in the real number system, there are ZERO real solutions to $x^2 + 2x + 5 = 0$.

[TA Sora] That means there are NO real $x$-intercepts! On the coordinate plane, the vertex sits up at $(-1, 4)$, and since $a = 1 > 0$, the parabola opens upward! It floats entirely above the $x$-axis.

[Prof. Park] Negative discriminant: zero real $x$-intercepts. The graph never touches the horizontal axis!`,

  // L43 (PRIMARY ISSUE)
  '43_2': `[Prof. Park] Slide 2 presents Section 3.6 Example 1A on page 83: Find the $x$-intercepts of $g(x) = x^2 + 6x$. Sora, which tool should we grab from our toolbox?

[TA Sora] Look at the structure: there is no constant term ($c = 0$)! Both terms share a common factor of $x$. Factoring out the GCF is our fastest weapon!

[Prof. Park] Let's factor it: set $g(x) = 0$, so $x^2 + 6x = 0$. Factoring out $x$ gives $x(x + 6) = 0$.

[TA Sora] Now apply the Zero-Product Property: either $x = 0$ or $x + 6 = 0$, which gives $x = -6$! That took literally five seconds!

[Prof. Park] So the two $x$-intercepts are $(0, 0)$ and $(-6, 0)$. Notice that $(0, 0)$ is also the $y$-intercept.

[TA Sora] And for the vertex: the axis of symmetry is halfway between $0$ and $-6$, which is $x = -3$. Plug in $-3$: $g(-3) = (-3)^2 + 6(-3) = 9 - 18 = -9$. Vertex is $(-3, -9)$!

[Prof. Park] One crucial pitfall to warn students about: never divide both sides by $x$! Dividing by $x$ loses the solution $x = 0$! Always factor!

[TA Sora] Always factor the GCF when $c = 0$! Solution set: $\\{0, -6\\}$. Clean and effortless!`,

  '43_3': `[Prof. Park] Turning to Slide 3, Example 1B presents: $h(x) = -2x^2 + 5x + 6$. Sora, what is our tactical assessment?

[TA Sora] Let's scan: $a = -2$, $b = 5$, and $c = 6$. Can we factor? Factors of $a \\cdot c = -12$ that add to 5 are $12$ and $-1$, or $6$ and $-2$... none add to 5! So we deploy the Quadratic Formula!

[Prof. Park] Exactly. Set $h(x) = 0$: $x = \\frac{-5 \\pm \\sqrt{5^2 - 4(-2)(6)}}{2(-2)} = \\frac{-5 \\pm \\sqrt{25 + 48}}{-4} = \\frac{-5 \\pm \\sqrt{73}}{-4}$.

[TA Sora] Since 73 is not a perfect square, $\\frac{-5 \\pm \\sqrt{73}}{-4}$ is our exact radical form!

[Prof. Park] In decimals, $\\sqrt{73} \\approx 8.544$. That gives $x \\approx \\frac{-5 + 8.544}{-4} \\approx -0.89$ and $x \\approx \\frac{-5 - 8.544}{-4} \\approx 3.39$.

[TA Sora] And the vertex: $x_v = -\\frac{b}{2a} = -\\frac{5}{2(-2)} = 1.25$. Evaluate $h(1.25) = -2(1.25)^2 + 5(1.25) + 6 = -3.125 + 6.25 + 6 = 9.13$. Vertex is $(1.25, 9.13)$!

[Prof. Park] Downward-opening parabola with $y$-intercept at $(0, 6)$ and peak at $(1.25, 9.13)$.`,

  '43_4': `[Prof. Park] Slide 4 presents Example 1C: Find the $x$-intercepts of $f(x) = 4x^2 - 28$. Let's scan this equation tactically.

[TA Sora] Look at the structure: there is NO middle term $bx$ ($b = 0$)! When $b = 0$, the Square Root Property is our quickest weapon!

[Prof. Park] Let's execute: set $4x^2 - 28 = 0$. Add 28 to both sides: $4x^2 = 28$. Now isolate $x^2$ by dividing by 4: $x^2 = 7$.

[TA Sora] Now take the square root of both sides, remembering our mandatory plus-or-minus sign: $x = \\pm \\sqrt{7}$! That is approximately $\\pm 2.65$.

[Prof. Park] So the $x$-intercepts are $(\\sqrt{7}, 0)$ and $(-\\sqrt{7}, 0)$.

[TA Sora] And what about the vertex? Since $b = 0$, $x_v = 0$. $f(0) = -28$. The vertex is $(0, -28)$, which is also the $y$-intercept!

[Prof. Park] Fast, clean, and avoids the Quadratic Formula entirely!`,

  '43_5': `[Prof. Park] On Slide 5, Example 1D presents: $f(x) = x^2 - 15x + 50$. Sora, what is our tactical assessment here?

[TA Sora] All three terms exist, $a = 1$, and $50$ has obvious factors! Can we find two numbers that multiply to $+50$ and add up to $-15$?

[Prof. Park] Yes: $-5 \\times -10 = 50$, and $-5 + (-10) = -15$. It factors cleanly into $(x - 5)(x - 10) = 0$!

[TA Sora] Setting each factor to zero gives $x = 5$ and $x = 10$! The $x$-intercepts are $(5, 0)$ and $(10, 0)$.

[Prof. Park] The $y$-intercept is $(0, 50)$. And the vertex is halfway between 5 and 10: $x_v = 7.5$.

[TA Sora] Evaluate $f(7.5) = (7.5)^2 - 15(7.5) + 50 = 56.25 - 112.5 + 50 = -6.25$. So the vertex is $(7.5, -6.25)$!

[Prof. Park] When factoring works with integers, it is by far the most enjoyable method in algebra!`,

  '43_6': `[Prof. Park] Slide 6 presents Example 2 on page 84: $f(x) = -2(x - 15)^2 + 50$. Notice this function is already in Vertex Form $a(x - h)^2 + k$!

[TA Sora] We can read the vertex directly off the page with zero computation! $h = 15$ and $k = 50$. So the vertex is $(15, 50)$!

[Prof. Park] Since $a = -2 < 0$, the parabola opens downward, making $(15, 50)$ the absolute maximum. Now let's find the $x$-intercepts by setting $f(x) = 0$.

[TA Sora] Subtract 50 from both sides: $-2(x - 15)^2 = -50$. Divide both sides by $-2$: $(x - 15)^2 = 25$!

[Prof. Park] Take the square root of both sides: $x - 15 = \\pm 5$. Add 15: $x = 15 \\pm 5$. That gives $x = 20$ and $x = 10$!

[TA Sora] Intercepts are $(10, 0)$ and $(20, 0)$. And $f(20) = 0$, exactly matching Part D!

[Prof. Park] Finally, for the $y$-intercept: $f(0) = -2(-15)^2 + 50 = -2(225) + 50 = -400$, giving $(0, -400)$.`,

  // L44
  '44_2': `[Prof. Park] On Slide 2, we graph $g(x) = x^2 + 6x + 5$ using the Vertex and Table method from page 96. Let's execute our protocol!

[TA Sora] Step 1: The Vertex! $a = 1$, $b = 6$, and $c = 5$. $x_v = -\\frac{6}{2(1)} = -3$. Plug in $-3$: $g(-3) = (-3)^2 + 6(-3) + 5 = 9 - 18 + 5 = -4$. Vertex is $(-3, -4)$!

[Prof. Park] Step 2: Build a table centered at $x = -3$, picking two values to the left and two values to the right.

[TA Sora] At $x = -5$: $g(-5) = 25 - 30 + 5 = 0$. At $x = -4$: $g(-4) = 16 - 24 + 5 = -3$. At $x = -2$: $g(-2) = 4 - 12 + 5 = -3$. At $x = -1$: $g(-1) = 1 - 6 + 5 = 0$!

[Prof. Park] Notice the beautiful symmetry in the table: $y$-values are $0, -3, -4, -3, 0$.

[TA Sora] The points are $(-5, 0)$, $(-4, -3)$, $(-3, -4)$, $(-2, -3)$, and $(-1, 0)$. Connect them with a smooth U-shaped curve!`,

  '44_4': `[Prof. Park] On Slide 4, we examine $g(x) = 2x^2 - 8x$. Sora, let's identify the 5 key features!

[TA Sora] Point 1: The Vertex! $a = 2$, $b = -8$, and $c = 0$. $x_v = -\\frac{-8}{2(2)} = \\frac{8}{4} = 2$. Evaluate $g(2) = 2(4) - 8(2) = 8 - 16 = -8$. Vertex is $(2, -8)$!

[Prof. Park] Point 2: The $y$-intercept. Since $c = 0$, $g(0) = 0$, giving $(0, 0)$.

[TA Sora] Point 3: The $x$-intercepts! Set $2x^2 - 8x = 0$. Factor out the GCF $2x$: $2x(x - 4) = 0$. That gives $x = 0$ and $x = 4$! So $(0, 0)$ and $(4, 0)$!

[Prof. Park] Point 4: Notice that $(4, 0)$ is the symmetric partner of $(0, 0)$ across the axis of symmetry $x = 2$!

[TA Sora] Because $a = 2 > 0$, the parabola opens upward with a minimum at $(2, -8)$. Domain is $(-\\infty, \\infty)$ and Range is $[-8, \\infty)$!`,

  '44_5': `[Prof. Park] Slide 5 presents $f(x) = -\\frac{1}{2}(x + 1)^2 + 8$ in Vertex Form. Sora, how quickly can we harvest the key points?

[TA Sora] Instantly! The vertex is $(-1, 8)$! Because $a = -\\frac{1}{2} < 0$, it opens downward and is wider than standard parabolas.

[Prof. Park] Step 2: The $y$-intercept. Set $x = 0$: $f(0) = -\\frac{1}{2}(0 + 1)^2 + 8 = -0.5 + 8 = 7.5$, giving $(0, 7.5)$.

[TA Sora] By symmetry across $x = -1$, moving 1 unit left gives the partner point $(-2, 7.5)$!

[Prof. Park] Step 3: The $x$-intercepts. Set $-\\frac{1}{2}(x + 1)^2 + 8 = 0 \\implies -\\frac{1}{2}(x + 1)^2 = -8 \\implies (x + 1)^2 = 16$.

[TA Sora] Take square roots: $x + 1 = \\pm 4 \\implies x = 3$ and $x = -5$! Intercepts are $(3, 0)$ and $(-5, 0)$!

[Prof. Park] Domain is $(-\\infty, \\infty)$ and Range is $(-\\infty, 8]$ because the maximum peak is 8!`,

  '44_6': `[Prof. Park] Slide 6 compares quadratic and linear functions: evaluating $f(x) = x^2 - 6x + 4$ and $g(x) = -2x + 25$ at $x = -7$.

[TA Sora] Part A: Plug $-7$ into the quadratic $f(x)$: $f(-7) = (-7)^2 - 6(-7) + 4 = 49 + 42 + 4 = 95$!

[Prof. Park] Part B: Plug $-7$ into the linear function $g(x)$: $g(-7) = -2(-7) + 25 = 14 + 25 = 39$!

[TA Sora] Look at how much faster quadratic growth is compared to linear growth: at $x = -7$, $f$ has climbed to 95 while $g$ is at 39!

[Prof. Park] Exactly. Linear rate of change is constant, but quadratic acceleration multiplies rapidly.`,

  '44_7': `[Prof. Park] Slide 7 demonstrates function transformations with $f(x + 5)$ and $g(x + 5)$ for our two functions.

[TA Sora] For Part C: substitute $(x + 5)$ into $f(x) = x^2 - 6x + 4$: $f(x + 5) = (x + 5)^2 - 6(x + 5) + 4$.

[Prof. Park] Expand: $x^2 + 10x + 25 - 6x - 30 + 4$. Combining like terms gives $x^2 + 4x - 1$!

[TA Sora] Now Part D with $g(x) = -2x + 25$: $g(x + 5) = -2(x + 5) + 25 = -2x - 10 + 25 = -2x + 15$!

[Prof. Park] Geometrically, replacing $x$ with $x + 5$ shifts both the parabola and the straight line 5 units to the left on the coordinate plane.`,

  '44_8': `[Prof. Park] Slide 8 presents our final solving challenge: Part E solves $g(x) = 17$, and Part F solves the intersection system $f(x) = g(x)$!

[TA Sora] Part E is linear: $-2x + 25 = 17$. Subtract 25: $-2x = -8$, so $x = 4$!

[Prof. Park] Part F finds where the line intersects the parabola: set $x^2 - 6x + 4 = -2x + 25$.

[TA Sora] Add $2x$ and subtract 25 to set it to zero: $x^2 - 4x - 21 = 0$!

[Prof. Park] Factor the quadratic: two numbers that multiply to $-21$ and add to $-4$ are $-7$ and $+3$. So $(x - 7)(x + 3) = 0$.

[TA Sora] That gives $x = 7$ and $x = -3$! The line cuts through the parabola at two distinct points: $x = 7$ and $x = -3$!`,

  // L45
  '45_2': `[Prof. Park] Slide 2 reviews Domain and Range across all four Section 3.7 functions from our workbook.

[TA Sora] Function 1: $g(x) = x^2 + 6x + 5$. Vertex is $(-3, -4)$, and it opens upward. Domain is $(-\\infty, \\infty)$ and Range is $[-4, \\infty)$!

[Prof. Park] Function 2: $h(x) = -2x^2 + 4x + 6$. Vertex is $(1, 8)$, and it opens downward because $a = -2 < 0$. Range is $(-\\infty, 8]$!

[TA Sora] Function 3: $g(x) = 2x^2 - 8x$. Vertex is $(2, -8)$, opens upward. Range is $[-8, \\infty)$!

[Prof. Park] Function 4: $f(x) = -\\frac{1}{2}(x + 1)^2 + 8$. Vertex is $(-1, 8)$, opens downward. Range is $(-\\infty, 8]$!

[TA Sora] Notice the universal rule: Domain of EVERY quadratic function is $(-\\infty, \\infty)$. Range always starts or ends at the vertex $y$-value $k$!`
};

let modifiedCount = 0;

for (const [key, newScript] of Object.entries(updates)) {
  const [lecStr, slideStr] = key.split('_');
  const lecNum = parseInt(lecStr, 10);
  const slideNum = parseInt(slideStr, 10);

  const lecVarName = 'SLIDES_MONTANA_L' + (lecNum < 10 ? '0' + lecNum : lecNum);
  const lecIdx = fileContent.indexOf(lecVarName);
  if (lecIdx === -1) {
    console.error(`Could not find ${lecVarName}`);
    continue;
  }

  // Find "num": slideNum after lecIdx
  // Note: slide objects look like: "num": 2,
  const numRegex = new RegExp(`["']num["']\\s*:\\s*${slideNum}\\b`);
  const matchNum = fileContent.slice(lecIdx).match(numRegex);
  if (!matchNum) {
    console.error(`Could not find slide num ${slideNum} in ${lecVarName}`);
    continue;
  }
  const numIdx = lecIdx + matchNum.index;

  // Now find "script": "..." after numIdx
  const scriptKey = '"script":';
  const scriptIdx = fileContent.indexOf(scriptKey, numIdx);
  if (scriptIdx === -1) {
    console.error(`Could not find "script": in ${lecVarName} S${slideNum}`);
    continue;
  }

  // Find start of string
  const quoteStart = fileContent.indexOf('"', scriptIdx + scriptKey.length);
  if (quoteStart === -1) {
    console.error(`Could not find quoteStart in ${lecVarName} S${slideNum}`);
    continue;
  }

  // Scan until unescaped closing quote
  let quoteEnd = quoteStart + 1;
  while (quoteEnd < fileContent.length) {
    if (fileContent[quoteEnd] === '\\') {
      quoteEnd += 2; // skip escaped char
    } else if (fileContent[quoteEnd] === '"') {
      break;
    } else {
      quoteEnd++;
    }
  }

  if (quoteEnd >= fileContent.length) {
    console.error(`Could not find quoteEnd in ${lecVarName} S${slideNum}`);
    continue;
  }

  // Replace old string with JSON-serialized newScript
  const serializedNewScript = JSON.stringify(newScript);
  fileContent = fileContent.slice(0, quoteStart) + serializedNewScript + fileContent.slice(quoteEnd + 1);
  modifiedCount++;
  console.log(`Updated L${lecNum} S${slideNum}`);
}

console.log(`Total updated: ${modifiedCount} of ${Object.keys(updates).length}`);
fs.writeFileSync(filePath, fileContent, 'utf8');
console.log('Successfully written to', filePath);
