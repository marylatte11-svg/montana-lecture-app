# -*- coding: utf-8 -*-
"""
unit3_scripts_l32_l35.py
Full 20-25 Minute Broadcast Tiki-Taka Dialogue for Lectures 32, 33, 34, 35
Prof. Eunju Park & TA Sora (Gallatin College Montana State University)
Each lecture contains 8-9 slides with ~300-380 words per slide (~2,500-2,900 words per lecture).
"""

SCRIPTS_L32 = {
    1: """[Prof. Park] Welcome back to M090, Bobcats! I am Professor Eunju Park, and with me is our stellar teaching assistant, Sora. Today in Lecture 32, we transition from the algebraic formulas of Section 3.0 into the visual architecture of the parabola.

[TA Sora] Hello everyone! Slide 1 is what I call the 'Blueprint Slide.' When an architect designs a bridge in Bozeman or a roof truss for heavy mountain snow, they identify specific anchor points before drawing anything else. A parabola has four critical anatomical features!

[Prof. Park] Let's list those four landmarks together: First, the Vertex—the turning point and single most important point on the entire curve. Second, the Axis of Symmetry—the vertical mirror line passing straight through the vertex. Third, the $y$-intercept—where the curve crosses the vertical axis. And fourth, the $x$-intercepts—where the curve touches the horizontal ground level.

[TA Sora] Notice on the coordinate plane how symmetrical the parabola is! If you fold the paper along that golden dashed line—the Axis of Symmetry—the left wing lands perfectly on top of the right wing. Every point on the left has an identical twin on the right at the exact same height!

[Prof. Park] Think of casting a fly-fishing line across the Gallatin River. As your weighted fly travels forward and arcs through the air, it reaches a peak height—that's your vertex. The left side where it rises and the right side where it descends are mirror images dictated by gravity.

[TA Sora] And students, look at the equation for that mirror line: it is always written as a vertical line equation, $x = h$, NOT just a single number! If you write 'axis of symmetry = 1' on a quiz, that's just a number. You must write $x = 1$ because it is a physical line across the plane!

[Prof. Park] Excellent warning, Sora. Today we will explore two complete examples—Example 5 in general form and Example 6 in vertex form—and extract all four features step-by-step.

[TA Sora] Turn to page 61 in your workbook, and let's dissect Example 5 together!""",

    2: """[Prof. Park] Slide 2 brings us to Section 3.0 Example 5 on page 61: $f(x) = x^2 - 9$. Part 1 asks us to find both the $y$-intercept and the $x$-intercepts. Sora, where should a student always begin?

[TA Sora] I always recommend starting with the $y$-intercept because it requires almost zero heavy lifting! To find where any graph crosses the $y$-axis, you simply evaluate the function at $x = 0$.

[Prof. Park] Let's do that arithmetic right now: $f(0) = (0)^2 - 9 = 0 - 9 = -9$. So the graph crosses the vertical axis at the point $(0, -9)$. Notice that as an ordered pair, the $x$-coordinate is strictly 0.

[TA Sora] Now for the $x$-intercepts! This is where the output $y$ or $f(x)$ equals 0. So we set the entire function equal to zero: $x^2 - 9 = 0$. Professor Park, we have two different ways to solve this equation, don't we?

[Prof. Park] We do! You can factor it as a difference of squares: $(x - 3)(x + 3) = 0$, giving $x = 3$ and $x = -3$. Or you can add 9 to both sides to get $x^2 = 9$, and apply the Square Root Property: $x = \\pm \\sqrt{9} = \\pm 3$.

[TA Sora] Both methods yield the exact same two points: $(-3, 0)$ and $(3, 0)$! Notice how symmetrical they are relative to the $y$-axis—one is 3 units to the left of the origin, and the other is 3 units to the right.

[Prof. Park] Look at the graph on your screen. The points $(-3, 0)$ and $(3, 0)$ anchor the curve at the horizontal axis, and $(0, -9)$ anchors the curve down below. 

[TA Sora] Always write intercepts as complete ordered pairs: write $(0, -9)$, $(-3, 0)$, and $(3, 0)$. In college algebra, an intercept is a geometric point on the plane!""",

    3: """[Prof. Park] Continuing with $f(x) = x^2 - 9$ on Slide 3, Part 2 asks us to determine the Vertex and the Axis of Symmetry. Sora, how can we use our intercepts from the previous slide to find the vertex without complicated formulas?

[TA Sora] This is one of the most elegant geometric insights in algebra! Because a parabola is completely symmetrical, the $x$-coordinate of the vertex must sit at the exact midpoint between the two $x$-intercepts!

[Prof. Park] What a great insight. The two intercepts are at $x = -3$ and $x = 3$. What is the average or midpoint between $-3$ and $+3$? It is $(-3 + 3) / 2 = 0 / 2 = 0$. That immediately tells us $x_v = 0$!

[TA Sora] And to find the matching $y$-value, we plug $x = 0$ back into our function: $f(0) = 0^2 - 9 = -9$. So our vertex is at $(0, -9)$! In this special case, the vertex and the $y$-intercept are the exact same point!

[Prof. Park] Now what about the Axis of Symmetry? Remember, the mirror line cuts vertically right through the vertex. Since the $x$-coordinate of the vertex is 0, the equation of the axis of symmetry is simply $x = 0$.

[TA Sora] Which is the equation of the $y$-axis itself! Look at the coordinate grid: that vertical yellow dashed line splits the parabola into two identical halves.

[Prof. Park] Think about hanging a heavy pendulum or hammock in your backyard. The lowest point hangs right in the center, and both sides rise equally. That center plumb line is your axis of symmetry.

[TA Sora] Confirm your notes on page 61: Vertex is $(0, -9)$, and the Axis of Symmetry is the vertical line $x = 0$. Let's analyze the domain and range on Slide 4!""",

    4: """[Prof. Park] Slide 4 covers Part 3 of Example 5: determining whether $f(x) = x^2 - 9$ has a minimum or maximum value, and finding its Domain and Range in interval notation.

[TA Sora] First, let's determine minimum versus maximum. We look at the leading coefficient $a$. For $f(x) = x^2 - 9$, the coefficient in front of $x^2$ is an invisible positive 1 ($a = 1 > 0$). Since $a$ is positive, the parabola opens upward!

[Prof. Park] And when a parabola opens upward like a cup, the vertex sits at the very bottom. That means the function has a Minimum value. But students, be careful: when a problem asks 'what is the minimum value?', it is asking for the lowest $y$-output, not the $x$-location!

[TA Sora] Exactly! The minimum value is $-9$. It occurs at $x = 0$, but the value itself is $-9$. If you run a refrigeration truck carrying fresh Montana beef, your minimum operating temperature is the $y$-value, $-9^\\circ$, not the time of day.

[Prof. Park] Now let's discuss Domain. For any standard polynomial or quadratic function with no square roots or fractions, you can substitute any real number you want for $x$. So the Domain is always all real numbers: $(-\\infty, \\infty)$.

[TA Sora] But Range is restricted! Range is the set of all possible vertical outputs ($y$-values). Look at the graph: the curve never drops below $y = -9$. It starts at $-9$ and climbs upward to infinity without bound!

[Prof. Park] Therefore, the Range in interval notation is $[-9, \\infty)$. Notice the square bracket on $-9$ because the point $(0, -9)$ is actually reached by the function.

[TA Sora] Never put a parenthesis on a reached minimum: write $[-9, \\infty)$ with a bracket! Domain is $(-\\infty, \\infty)$, Range is $[-9, \\infty)$, and the minimum value is $-9$.""",

    5: """[Prof. Park] On Slide 5, we turn to Section 3.0 Example 6 on page 62: $f(x) = -2(x + 1)^2 + 8$. Sora, this equation looks completely different from Example 5. It is written in what we call Vertex Form!

[TA Sora] Yes! Standard Vertex Form is written as $f(x) = a(x - h)^2 + k$. Many students prefer vertex form over general form because the coordinates of the vertex $(h, k)$ are practically handed to you on a silver platter!

[Prof. Park] But there is a huge psychological trap with the signs inside the parentheses! Notice the formula has a minus sign: $(x - h)$. That means the horizontal coordinate $h$ always has the OPPOSITE sign of what you see inside the parentheses!

[TA Sora] Let's look closely at our function: we have $(x + 1)^2$. Because it says $+1$, $h$ is actually $-1$! Think of it as $(x - (-1))^2$. Outside the parentheses, we have $+8$, so $k = +8$. That gives us a vertex of $(-1, 8)$!

[Prof. Park] Now let's find the $y$-intercept. Never assume the number at the end is the $y$-intercept when you are in vertex form! To find the $y$-intercept, you MUST substitute $x = 0$ into the function.

[TA Sora] Let's do the arithmetic carefully: $f(0) = -2(0 + 1)^2 + 8$. Inside the parentheses, $0 + 1 = 1$. Square that: $1^2 = 1$. Multiply by $-2$: $-2(1) = -2$. Finally, add 8: $-2 + 8 = 6$!

[Prof. Park] So the $y$-intercept is at $(0, 6)$! Notice that 6 is NOT the number 8 sitting at the end of the equation. In vertex form, the number at the end is $k$, not the $y$-intercept.

[TA Sora] That is such a vital distinction. In general form, the constant $c$ was the $y$-intercept. In vertex form, $k$ is the vertex height, and you must calculate $f(0)$ to find the $y$-intercept. Here it is $(0, 6)$!""",

    6: """[Prof. Park] Let's continue with Example 6 on Slide 6: identifying the Vertex and Axis of Symmetry for $f(x) = -2(x + 1)^2 + 8$. As Sora pointed out, reading vertex form $a(x - h)^2 + k$ reveals the vertex $(h, k)$ directly.

[TA Sora] Here is my personal mental trick: 'Inside the parentheses, think opposite; outside the parentheses, keep it normal.' Inside, we see $+1$, so we flip the sign to $-1$. Outside, we see $+8$, so we keep $+8$. That gives us the vertex $(-1, 8)$!

[Prof. Park] And once you have the vertex $(-1, 8)$, what is the equation of the Axis of Symmetry? The vertical mirror line must slice right through the $x$-coordinate of the vertex. So the Axis of Symmetry is simply $x = -1$.

[TA Sora] Look at the graph on your right: the vertical dashed golden line is positioned at $x = -1$. Notice that our leading coefficient is $a = -2$. Because $a$ is negative, the parabola opens downward!

[Prof. Park] And look at the factor of 2! The graph is narrower and steeper than a standard parabola because the factor of 2 stretches the curve vertically away from the horizontal axis. 

[TA Sora] If you are in civil engineering designing a storm water drainage culvert or an arched tunnel through the Rocky Mountains, you need to know the highest clearance point so tall trucks can pass safely. The vertex $(-1, 8)$ tells you the absolute highest clearance inside that arch!

[Prof. Park] Exactly. The highest point is at 8 feet (or meters), located 1 unit to the left of your center reference line. 

[TA Sora] Write down both items: Vertex is $(-1, 8)$, and Axis of Symmetry is the vertical line $x = -1$. Now let's examine the maximum value and range on Slide 7!""",

    7: """[Prof. Park] Slide 7 covers Part 3 of Example 6: finding the maximum or minimum value and writing the Domain and Range for $f(x) = -2(x + 1)^2 + 8$. 

[TA Sora] Since the leading coefficient is $a = -2 < 0$, our parabola opens downward. That means the vertex $(-1, 8)$ is the mountain peak—the absolute Maximum value of the function!

[Prof. Park] And what is that maximum value? It is the $y$-value of the vertex: the maximum value is 8. The function reaches a height of 8 when $x = -1$, but it can never produce any output higher than 8.

[TA Sora] Now let's write the Domain. Professor Park, does the domain ever change for a standard quadratic function?

[Prof. Park] Never! A parabola extends infinitely to the left and infinitely to the right without any holes, vertical asymptotes, or breaks. So the Domain is always all real numbers: $(-\\infty, \\infty)$.

[TA Sora] But look at the Range! Because the parabola opens downward, its vertical outputs come from deep down in the negative abyss, climb all the way up to the peak of 8, and stop right there!

[Prof. Park] When writing interval notation, always list from smallest to largest—bottom to top! So the Range begins at $-\\infty$ and goes up to 8, with a solid bracket on 8: $(-\\infty, 8]$.

[TA Sora] Common student mistake alert: Never write $[8, -\\infty)$! Interval notation must always read from left to right, lowest number first. So $-\\infty$ comes first: $(-\\infty, 8]$.

[Prof. Park] Maximum value is 8, Domain is $(-\\infty, \\infty)$, and Range is $(-\\infty, 8]$. You have completely mastered the functional behavior!""",

    8: """[Prof. Park] On Slide 8, Part 4 of Example 6 asks us to do something very practical: convert our vertex form $f(x) = -2(x + 1)^2 + 8$ into General Form $f(x) = ax^2 + bx + c$. Sora, why would anyone want to convert between these two forms?

[TA Sora] Because each form gives you different superpowers! Vertex form gives you the vertex instantly. But general form lets you see the $y$-intercept immediately and allows you to use the Quadratic Formula, which we will learn later in Section 3.5.

[Prof. Park] To convert, we must follow the strict Order of Operations (PEMDAS). Step 1 is to expand the binomial square: $(x + 1)^2$. Sora, warn our students about the dangerous temptation here!

[TA Sora] Oh, the 'Freshman's Dream' trap! Students often want to just square both terms and write $x^2 + 1$. That misses the entire middle term! Remember that $(x + 1)^2$ means $(x + 1)(x + 1) = x^2 + 2x + 1$. Never forget that middle term of $2x$!

[Prof. Park] Now Step 2: substitute that expanded trinomial back into the function: $f(x) = -2(x^2 + 2x + 1) + 8$. Now distribute the $-2$ through every single term inside the parentheses: $-2 \\cdot x^2 = -2x^2$, $-2 \\cdot 2x = -4x$, and $-2 \\cdot 1 = -2$.

[TA Sora] That gives us $f(x) = -2x^2 - 4x - 2 + 8$. And Step 3 is to combine the constant numbers at the end: $-2 + 8 = +6$!

[Prof. Park] Bringing it all together: $f(x) = -2x^2 - 4x + 6$. Look at that: $a = -2$, $b = -4$, and $c = 6$. And notice our constant $c = 6$ matches the $y$-intercept $(0, 6)$ that we found on Slide 5!

[TA Sora] Everything in algebra connects like clockwork. Converting forms confirms our calculations and proves that both equations describe the exact same curve!""",

    9: """[Prof. Park] We have arrived at Slide 9, our Section 3.0 Part 2 Mastery Summary! Sora, we have covered an incredible amount of rich mathematics in Lecture 32.

[TA Sora] We truly have! Let's review the big milestones: We explored the anatomy of parabolas in both General Form ($ax^2 + bx + c$) and Vertex Form ($a(x - h)^2 + k$). We found that the vertex $(h, k)$ is the turning point, and the vertical line $x = h$ is the Axis of Symmetry.

[Prof. Park] We learned how to find the $y$-intercept by evaluating $f(0)$, and $x$-intercepts by solving $f(x) = 0$. We proved that the Domain of every quadratic is $(-\\infty, \\infty)$, while the Range is bounded by the vertex: $[k, \\infty)$ if the parabola opens up ($a > 0$), and $(-\\infty, k]$ if the parabola opens down ($a < 0$).

[TA Sora] And we practiced algebraic discipline: expanding binomial squares carefully without dropping the middle term, distributing negative coefficients, and translating between vertex form and general form.

[Prof. Park] In everyday life, whether you are managing personal debt, optimizing crop yields on a Montana farm, or tracking physical trajectories in sports, understanding peaks, valleys, and symmetry gives you a profound analytical edge.

[TA Sora] Tonight, review pages 61 and 62 in your workbook. Practice finding the vertex, intercepts, and range for the exercise problems.

[Prof. Park] In Lecture 33, we will tackle function evaluations with negative numbers, fractions, and binomial inputs. Great job today, everyone!

[TA Sora] Keep your confidence high, Bobcats. We'll see you in Lecture 33!"""
}
