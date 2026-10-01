# -*- coding: utf-8 -*-
"""
unit2_scripts_l21_l23.py
High-density broadcast tiki-taka scripts for Lectures 21, 22, and 23.
Target: ~250-350 words per slide (~2,000-2,600 words per lecture).
"""

SCRIPTS_L21 = {
    1: r"""[Prof. Park] Welcome to Lecture 21 of M090 Introductory Algebra! Today on page 40 of your workbook, we explore the geometric and algebraic relationships between two distinct lines on the Cartesian plane: Parallel Lines and Perpendicular Lines.

[TA Sora] In everyday life, we see parallel lines everywhere in Montana—the dual rails of the Montana Rail Link passing through Bozeman, the parallel boundary fences of Gallatin Valley ranches, or the rungs of a ladder. Geometrically, parallel lines lie in the exact same plane and never, ever intersect, no matter how far you extend them into infinity!

[Prof. Park] And algebraically, what guarantees that two non-vertical lines will maintain the exact same separation forever? Their steepness must be identical! That gives us our first foundational theorem:
Two non-vertical lines are **parallel** if and only if they have the **exact same slope**:
$$m_1 = m_2 \quad \text{and} \quad b_1 \neq b_2$$
Notice that condition $b_1 \neq b_2$: if they had the same slope and the same $y$-intercept, they wouldn't just be parallel; they would be the exact same line sitting on top of itself!

[TA Sora] Now, what about **perpendicular lines**? Perpendicular lines intersect at a crisp, perfect 90-degree right angle—like the intersection of Main Street and Willson Avenue in downtown Bozeman, or the framing studs meeting the base plate in home construction.

[Prof. Park] And algebraically, their slopes have an extraordinary relationship: their slopes are **negative reciprocals** of each other!
$$m_1 \cdot m_2 = -1 \quad \iff \quad m_2 = -\frac{1}{m_1}$$
If one line climbs uphill with a positive slope of $\frac{2}{3}$, the perpendicular line must plunge downhill with a negative flipped slope of $-\frac{3}{2}$!

[TA Sora] To find a perpendicular slope: Flip the fraction upside down, and flip the sign! Two flips: flip the numbers, flip the sign!""",

    2: r"""[Prof. Park] Let us test that two-flip rule on Example 3 on page 40 of your workbook: Determine if the lines with the given slopes are parallel, perpendicular, or neither.

[TA Sora] Pair A gives us: $m_1 = 2$ and $m_2 = 2$.
Compare them directly: $m_1 = m_2$. Both slopes are positive 2.
Because their slopes are completely identical, these two lines are **Parallel**! They climb uphill at the exact same rate.

[Prof. Park] Now examine Pair B: $m_1 = -\frac{3}{4}$ and $m_2 = \frac{4}{3}$.
Let us check: Is $m_1 = m_2$? No, one is negative, one is positive.
Let us test the perpendicular condition by multiplying them:
$$m_1 \cdot m_2 = \left(-\frac{3}{4}\right) \cdot \left(\frac{4}{3}\right) = -\frac{12}{12} = -1!$$
The product is $-1$! Or think of Sora's two flips: start with $-\frac{3}{4}$. Flip the fraction to $\frac{4}{3}$, and flip negative to positive. It gives $+\frac{4}{3}$! Therefore, Pair B is **Perpendicular**!

[TA Sora] Now look at Pair C: $m_1 = 2$ and $m_2 = -2$.
This is the number one trap question on the entire chapter! Many students see the negative sign and shout: 'Perpendicular!' Why is that completely false, Professor?

[Prof. Park] Because they only flipped the sign, but forgot to flip the fraction! The reciprocal of $2$ (which is $\frac{2}{1}$) is $\frac{1}{2}$. For perpendicularity, we needed $-\frac{1}{2}$!
Let us multiply: $2 \cdot (-2) = -4 \neq -1$.
Are they equal? $2 \neq -2$, so not parallel.
Is their product $-1$? $-4 \neq -1$, so not perpendicular.
Therefore, Pair C is **Neither**!

[TA Sora] Never forget: Perpendicular requires BOTH flips—flip the fraction, flip the sign!""",

    3: r"""[Prof. Park] Now turn to Example 4 on page 40: Determine if the two lines $x + y = 5$ and $-2x - 2y = 7$ are parallel, perpendicular, or neither. In Step 1 on this slide, we analyze Line 1: $x + y = 5$.

[TA Sora] To compare two lines, you cannot just look at the raw numbers when the equations are in Standard Form $Ax + By = C$. You must put them into the universal comparison format: Slope-Intercept Form $y = mx + b$!

[Prof. Park] Let us isolate $y$ in Line 1:
$$x + y = 5$$
Subtract $x$ from both sides:
$$y = -x + 5$$
What is the slope of Line 1, Sora?

[TA Sora] Look in front of $x$: there is a minus sign, which means there is an invisible $-1$ multiplying $x$!
So the slope is:
$$m_1 = -1$$
And the $y$-intercept is:
$$b_1 = 5 \implies (0, 5)$$

[Prof. Park] Exactly. For every 1 unit you run to the right, Line 1 drops 1 unit downward. It starts at elevation 5 on the vertical axis and cuts diagonally downhill across Quadrant I into Quadrant IV.

[TA Sora] Now keep $m_1 = -1$ and $b_1 = 5$ firmly in your memory. On Slide 4, we will solve Line 2 and compare!""",

    4: r"""[Prof. Park] On Slide 4, we perform Step 2 of Example 4: Solving Line 2, which is $-2x - 2y = 7$.

[TA Sora] Our goal is to isolate $y$.
Step 1: Add $2x$ to both sides to move the $x$-term to the right:
$$-2y = 2x + 7$$
Notice how we keep $2x$ in front of $+7$ to match $mx + b$.

[Prof. Park] Step 2: Now divide every single term on both sides by the coefficient of $y$, which is $-2$:
$$y = \frac{2x}{-2} + \frac{7}{-2}$$
Simplify each term carefully:
$$\frac{2x}{-2} = -1x = -x$$
$$\frac{7}{-2} = -\frac{7}{2} = -3.5$$
So Line 2 in slope-intercept form is:
$$y = -x - \frac{7}{2}$$

[TA Sora] Let us read off the parameters for Line 2:
The slope is $m_2 = -1$.
The $y$-intercept is $b_2 = -\frac{7}{2} = -3.5$, which gives the point $(0, -3.5)$.

[Prof. Park] Look at that slope: $m_2 = -1$.
Compare it with Line 1 from Slide 3: $m_1 = -1$!
Both slopes are identical! On Slide 5, let us verify their graph and state our conclusion.""",

    5: r"""[Prof. Park] On Slide 5, we present the visual proof and final conclusion for Example 4.

[TA Sora] Let us compare the two sets of parameters:
Line 1: $m_1 = -1$ and $y$-intercept $(0, 5)$.
Line 2: $m_2 = -1$ and $y$-intercept $(0, -3.5)$.

[Prof. Park] Step 1: Check the slopes:
$$m_1 = -1 \quad \text{and} \quad m_2 = -1 \implies m_1 = m_2$$
Step 2: Check the $y$-intercepts:
$$b_1 = 5 \quad \text{and} \quad b_2 = -3.5 \implies b_1 \neq b_2$$
Because their slopes are equal and their intercepts are different, these two lines are **PARALLEL**!

[TA Sora] Look at the graph on your screen! Both lines plunge downhill at a 45-degree angle with a slope of $-1$. Line 1 rides higher, crossing at $(0, 5)$, while Line 2 rides lower, crossing at $(0, -3.5)$. They maintain the exact same diagonal distance between them across the entire coordinate plane!

[Prof. Park] If this were a system of linear equations, because these parallel lines never intersect, there would be zero common points—no solution!

[TA Sora] Notice how easy it was once both equations were converted to $y = mx + b$. Slope-intercept form is the great equalizer of linear algebra!""",

    6: r"""[Prof. Park] Now turn to Example 5 on page 40: Determine if the two lines $-x + 2y = 6$ and $2x + y = 4$ are parallel, perpendicular, or neither. In Step 1, let us solve Line 1: $-x + 2y = 6$.

[TA Sora] Let us isolate $y$:
$$-x + 2y = 6$$
Add $x$ to both sides:
$$2y = x + 6$$
Divide every single term by 2:
$$y = \frac{x}{2} + \frac{6}{2}$$
Rewrite the fraction $\frac{x}{2}$ as $\frac{1}{2}x$, and simplify $6/2 = 3$:
$$y = \frac{1}{2}x + 3$$

[Prof. Park] Excellent. What are the key parameters of Line 1?
Slope: $m_1 = \frac{1}{2}$.
$y$-intercept: $b_1 = 3$, which corresponds to $(0, 3)$.

[TA Sora] Line 1 has a gentle uphill rise: for every 2 units you move to the right, you rise 1 unit upward.
Now let us record $m_1 = \frac{1}{2}$, and on Slide 7, we solve Line 2 and test for perpendicularity!""",

    7: r"""[Prof. Park] On Slide 7, we solve Line 2 of Example 5: $2x + y = 4$.

[TA Sora] This one is fast and sweet!
$$2x + y = 4$$
Subtract $2x$ from both sides:
$$y = -2x + 4$$
Look at how cleanly that fell into place:
The slope is $m_2 = -2$ (or $-\frac{2}{1}$).
The $y$-intercept is $b_2 = 4$, which corresponds to $(0, 4)$.

[Prof. Park] Now let us compare the two slopes:
Line 1 had slope $m_1 = \frac{1}{2}$.
Line 2 has slope $m_2 = -2$.
Let us multiply them:
$$m_1 \cdot m_2 = \left(\frac{1}{2}\right) \cdot (-2) = -1!$$

[TA Sora] Their product is $-1$! And look at Sora's two-flip test: $\frac{1}{2}$ flipped upside down is $\frac{2}{1} = 2$. Flipped to the opposite sign gives $-2$. It matches perfectly! Therefore, these two lines are **PERPENDICULAR**!

[Prof. Park] Look at the graph on your screen. Line 1 climbs gently with slope $\frac{1}{2}$, while Line 2 drops steeply with slope $-2$. Where they intersect, they form a perfect 90-degree square right angle!

[TA Sora] In construction framing, carpenters call this 'square.' If your walls meet with slopes that multiply to $-1$, your house is structurally sound and true!""",

    8: r"""[Prof. Park] On Slide 8, we present the Section 2.2 Parallel & Perpendicular Master Decision Checklist. Keep this mental flowchart handy for all upcoming exams.

[TA Sora] Step 1: Always put both equations into Slope-Intercept Form $y = mx + b$.

[Prof. Park] Step 2: Compare the slopes $m_1$ and $m_2$:
- **Test for Parallel:** Are the slopes identical ($m_1 = m_2$) with different intercepts ($b_1 \neq b_2$)? If yes, the lines are **Parallel**!
- **Test for Perpendicular:** Are the slopes negative reciprocals ($m_1 \cdot m_2 = -1$)? If yes, the lines are **Perpendicular**!
- **Neither:** If the slopes are neither identical nor negative reciprocals, the lines are **Neither**!

[TA Sora] And don't forget the special cases:
- Any horizontal line ($m = 0$) is perpendicular to any vertical line ($m = \text{undefined}$)!
- Any two horizontal lines ($y = c_1$ and $y = c_2$) are parallel!
- Any two vertical lines ($x = k_1$ and $x = k_2$) are parallel!

[Prof. Park] In Lecture 22, we move to Section 2.3: Writing the Equations of Lines given points, slopes, and intercepts using the mighty Point-Slope formula! Outstanding work today, everyone!"""
}

SCRIPTS_L22 = {
    1: r"""[Prof. Park] Welcome to Lecture 22 of M090! Today on page 41 of your workbook, we begin Section 2.3: Writing Equations of Lines.

[TA Sora] In Section 2.1 and 2.2, we were given an equation and had to find its slope, its intercepts, and draw its graph. Today, we run the machine in reverse: we are given geometric clues—a point, a slope, or two coordinates—and our mission is to construct the equation of the line!

[Prof. Park] To do this, algebra gives us three major formulas:
1. **Slope-Intercept Form:** $y = mx + b$. Perfect when you already know the slope $m$ and the specific $y$-intercept $(0, b)$.
2. **Point-Slope Form:**
$$y - y_1 = m(x - x_1)$$
This is the single most powerful, versatile formula in linear algebra!
3. **Standard Form:** $Ax + By = C$.

[TA Sora] Why is Point-Slope Form so legendary? Because in real life—in science labs, carpentry, and business—you almost NEVER start with the $y$-intercept! You usually observe some random data point in the field, like $(x_1, y_1) = (4, 15)$, and you know the rate of change $m$. Point-Slope form lets you plug in ANY point on the entire line and construct the exact equation without guessing!

[Prof. Park] Where does the formula come from? Look at the slope definition: $m = \frac{y - y_1}{x - x_1}$. Multiply both sides by $(x - x_1)$, and you get:
$$y - y_1 = m(x - x_1)$$
It is literally the slope formula wearing a different jacket!

[TA Sora] Let us put this mighty tool to work on Example 1 on page 41!""",

    2: r"""[Prof. Park] Example 1 on page 41: Find the equation of the line with a slope of $\frac{3}{2}$ that contains the point $(-4, 1)$. Write the final equation in Slope-Intercept Form $y = mx + b$.

[TA Sora] Step 1: Identify your given pieces!
We are given:
Slope: $m = \frac{3}{2}$.
Given point: $(x_1, y_1) = (-4, 1)$.
Notice that this given point is NOT a $y$-intercept because $x_1 = -4 \neq 0$! So we cannot use $y = mx + b$ directly. We must deploy Point-Slope Form!

[Prof. Park] Step 2: Write down the point-slope formula before substituting:
$$y - y_1 = m(x - x_1)$$
Now substitute with protective parentheses around negative numbers:
$$y - 1 = \frac{3}{2}(x - (-4))$$
Inside the parentheses, $x - (-4)$ becomes $x + 4$:
$$y - 1 = \frac{3}{2}(x + 4)$$

[TA Sora] Step 3: Distribute the slope $\frac{3}{2}$ to both terms inside the parentheses:
$$\frac{3}{2} \cdot x = \frac{3}{2}x$$
$$\frac{3}{2} \cdot 4 = \frac{12}{2} = 6$$
So our equation becomes:
$$y - 1 = \frac{3}{2}x + 6$$

[Prof. Park] Step 4: Now isolate $y$ to finish in slope-intercept form. Add 1 to both sides:
$$y = \frac{3}{2}x + 6 + 1 \implies y = \frac{3}{2}x + 7$$

[TA Sora] Look at that finished equation: $y = \frac{3}{2}x + 7$. The slope is $\frac{3}{2}$, and the $y$-intercept is $(0, 7)$. Let us test our original point $(-4, 1)$: $\frac{3}{2}(-4) + 7 = -6 + 7 = 1$! It checks out with 100% precision!""",

    3: r"""[Prof. Park] Now turn to Example 2 on page 41: Find the equation of the line with an $x$-intercept of $(-3, 0)$ and a slope of $-\frac{4}{3}$.

[TA Sora] Notice how the problem statement says 'an $x$-intercept of $(-3, 0)$.' A very common student blunder here is seeing $(-3, 0)$ and plugging in $b = -3$ into $y = mx + b$! Why is that a catastrophe, Professor?

[Prof. Park] Because $b$ is the **$y$-intercept**, which must have $x = 0$! An $x$-intercept has $y = 0$. You cannot plug an $x$-intercept into the $b$ slot of $y = mx + b$!
Instead, treat $(-3, 0)$ as a standard point $(x_1, y_1) = (-3, 0)$ and use Point-Slope Form!

[TA Sora] Let us plug in:
$$m = -\frac{4}{3} \quad \text{and} \quad (x_1, y_1) = (-3, 0)$$
$$y - y_1 = m(x - x_1)$$
$$y - 0 = -\frac{4}{3}(x - (-3))$$

[Prof. Park] Look at how smooth this simplifies:
On the left side: $y - 0 = y$.
On the right side: $x - (-3) = x + 3$.
$$y = -\frac{4}{3}(x + 3)$$

[TA Sora] Now distribute $-\frac{4}{3}$:
$$-\frac{4}{3} \cdot x = -\frac{4}{3}x$$
$$-\frac{4}{3} \cdot 3 = -4$$
So our final equation is:
$$y = -\frac{4}{3}x - 4$$

[Prof. Park] Notice that the true $y$-intercept is $(0, -4)$, which is completely different from $-3$! The point-slope formula protected us from a fatal shortcut error. Always respect the distinction between an $x$-intercept and a $y$-intercept!""",

    4: r"""[Prof. Park] On Slide 4, we examine Example 3 Step 1 on page 41: Find the equation of the line that contains the two points $(2, 3)$ and $(-6, 1)$.

[TA Sora] Look at this problem carefully: we are given TWO points, but we are NOT given the slope $m$! What do we do when the slope is missing?

[Prof. Park] We calculate it ourselves! Remember Lecture 20: whenever you have two points, you can always compute the slope using the slope formula:
$$m = \frac{y_2 - y_1}{x_2 - x_1}$$
Let $(x_1, y_1) = (2, 3)$ and $(x_2, y_2) = (-6, 1)$.

[TA Sora] Let us substitute with protective parentheses:
$$m = \frac{1 - 3}{-6 - 2}$$
In the numerator: $1 - 3 = -2$.
In the denominator: $-6 - 2 = -8$.
$$m = \frac{-2}{-8}$$
Simplify the fraction: negative divided by negative is positive, and $\frac{2}{8} = \frac{1}{4}$!
$$m = \frac{1}{4}$$

[Prof. Park] Now we have our slope: $m = \frac{1}{4}$.
And we have two points to choose from: $(2, 3)$ or $(-6, 1)$.
On Slide 5, we will plug into Point-Slope form and complete the equation!""",

    5: r"""[Prof. Park] On Slide 5, we complete Example 3 Step 2: Use $m = \frac{1}{4}$ and the point $(2, 3)$ to find the equation in Slope-Intercept Form.

[TA Sora] Students often ask: 'Sora, does it matter which of the two points I plug into point-slope form?' Not at all! Both points lie on the exact same line, so both points will lead to the exact same final equation. Pick the point with smaller, positive numbers to make your arithmetic effortless!

[Prof. Park] Let us use $(x_1, y_1) = (2, 3)$ and $m = \frac{1}{4}$:
$$y - y_1 = m(x - x_1)$$
$$y - 3 = \frac{1}{4}(x - 2)$$
Distribute $\frac{1}{4}$ to both terms:
$$y - 3 = \frac{1}{4}x - \frac{2}{4} = \frac{1}{4}x - \frac{1}{2}$$

[TA Sora] Now isolate $y$ by adding 3 to both sides:
$$y = \frac{1}{4}x - \frac{1}{2} + 3$$
Convert 3 into a fraction with denominator 2: $3 = \frac{6}{2}$:
$$y = \frac{1}{4}x - \frac{1}{2} + \frac{6}{2} \implies y = \frac{1}{4}x + \frac{5}{2}$$

[Prof. Park] Look at the graph on your screen. The line passes through $(-6, 1)$ and $(2, 3)$, climbing gently with a slope of $\frac{1}{4}$, and it crosses the vertical axis at exactly $2.5$, which is $\frac{5}{2}$! Everything connects with 100% mathematical harmony!""",

    6: r"""[Prof. Park] Turn to Example 4 on page 42: Find the equation of the line containing the points $(1, 7)$ and $(-3, 7)$.

[TA Sora] Before you jump into formulas, pause for three seconds and inspect the coordinates!
Look at the points: $(1, 7)$ and $(-3, 7)$.
What jumps out immediately? Both points have the exact same $y$-coordinate: $y = 7$!

[Prof. Park] If both points share the same vertical elevation of 7, what kind of line must this be? Let us check the slope formula:
$$m = \frac{7 - 7}{-3 - 1} = \frac{0}{-4} = 0$$
The slope is zero!

[TA Sora] And what does our famous HOY VUX rule tell us?
H - O - Y!
Horizontal line, 0 slope, $y = \text{number}$!
Because $y$ is permanently locked at 7, the equation of the line is simply:
$$y = 7$$

[Prof. Park] You do not need point-slope form, you do not need fractions, you do not need algebra gymnastics. The equation is literally staring at you from the points: $y = 7$!

[TA Sora] Whenever you notice identical $y$-coordinates, smile and write $y = c$!""",

    7: r"""[Prof. Park] Now look at Example 5 on page 42: Find the equation of the line containing the points $(2, -8)$ and $(2, 1)$.

[TA Sora] Again, apply Sora's three-second inspection rule! Look at the coordinates:
Point 1: $(2, -8)$.
Point 2: $(2, 1)$.
Now the $x$-coordinates are identical: $x_1 = 2$ and $x_2 = 2$!

[Prof. Park] Let us compute the slope and observe what happens:
$$m = \frac{1 - (-8)}{2 - 2} = \frac{1 + 8}{0} = \frac{9}{0}$$
Division by zero! The slope is **Undefined**!

[TA Sora] And what does HOY VUX tell us?
V - U - X!
Vertical line, Undefined slope, $x = \text{number}$!
Because the $x$-coordinate is permanently locked at 2, you CANNOT write this line in $y = mx + b$ form. The equation of the line is simply:
$$x = 2$$

[Prof. Park] Notice the beauty of Examples 4 and 5 side by side:
When $y$-coordinates are identical, it is a horizontal line: $y = c$.
When $x$-coordinates are identical, it is a vertical line: $x = c$.
Recognizing these patterns instantly saves you minutes on exams!""",

    8: r"""[Prof. Park] On Slide 8, we present the Section 2.3 Part 1 Master Strategy Flowchart for Writing Equations of Lines.

[TA Sora] Case 1: **Given Slope $m$ and $y$-intercept $(0, b)$:**
Plug directly into Slope-Intercept Form: $y = mx + b$. Done in five seconds!

[Prof. Park] Case 2: **Given Slope $m$ and ANY point $(x_1, y_1)$:**
Use Point-Slope Form:
$$y - y_1 = m(x - x_1)$$
Distribute $m$, isolate $y$, and finish in $y = mx + b$.

[TA Sora] Case 3: **Given TWO points $(x_1, y_1)$ and $(x_2, y_2)$:**
Step A: Find slope $m = \frac{y_2 - y_1}{x_2 - x_1}$.
Step B: Pick either point and use Point-Slope Form: $y - y_1 = m(x - x_1)$.
Step C: Solve for $y$.

[Prof. Park] Case 4: **Special Lines (HOY VUX):**
If $y_1 = y_2$, horizontal line: $y = c$.
If $x_1 = x_2$, vertical line: $x = c$.

[TA Sora] In Lecture 23, we put these tools into high-gear action with parallel and perpendicular lines through given points and comprehensive in-class practice exercises!"""
}

SCRIPTS_L23 = {
    1: r"""[Prof. Park] Welcome to Lecture 23 of M090! Today on pages 42 through 44 of your workbook, we combine everything from the last two lectures: finding equations of lines that pass through specific points and are Parallel or Perpendicular to existing lines, followed by comprehensive in-class practice!

[TA Sora] Let us begin on page 42 with Example 6: Find the equation of the line containing the point $(-1, 3)$ and **parallel** to the line $y = 4x - 5$. Write the final answer in slope-intercept form.

[Prof. Park] Let us extract our clues methodically:
Clue 1: We are given a target point: $(x_1, y_1) = (-1, 3)$.
Clue 2: Our new line must be **parallel** to the reference line $y = 4x - 5$.

[TA Sora] What does 'parallel' mean for slopes? Parallel lines have the **exact same slope**!
Look at the reference line: $y = 4x - 5$. Its slope is $m = 4$.
Therefore, our new line must also have slope:
$$m = 4$$

[Prof. Park] Now we have our slope $m = 4$, and we have our point $(x_1, y_1) = (-1, 3)$. We plug directly into Point-Slope Form:
$$y - y_1 = m(x - x_1)$$
$$y - 3 = 4(x - (-1))$$
Inside the parentheses, $x - (-1)$ becomes $x + 1$:
$$y - 3 = 4(x + 1)$$

[TA Sora] Distribute the 4:
$$y - 3 = 4x + 4$$
Add 3 to both sides to isolate $y$:
$$y = 4x + 4 + 3 \implies y = 4x + 7$$

[Prof. Park] Look at how clean that is: $y = 4x + 7$.
It has slope 4 (so it is parallel to $y = 4x - 5$), and if you plug in $x = -1$: $4(-1) + 7 = 3$, it passes right through $(-1, 3)$! Perfectly verified!""",

    2: r"""[Prof. Park] Now turn to Example 7 on page 42: Find the equation of the line containing the point $(2, -3)$ and **perpendicular** to the line $y = -\frac{1}{3}x + 2$.

[TA Sora] Notice that magical word: **PERPENDICULAR**!
Let us find our slope using Sora's two-flip rule:
The reference line is $y = -\frac{1}{3}x + 2$, so its slope is $m_1 = -\frac{1}{3}$.
To find the perpendicular slope $m_{\perp}$:
Flip the fraction $\frac{1}{3} \implies \frac{3}{1} = 3$.
Flip the sign from negative to positive $\implies +3$!
Therefore:
$$m_{\perp} = 3$$

[Prof. Park] Now we assemble our pieces:
Slope: $m = 3$.
Given point: $(x_1, y_1) = (2, -3)$.
Plug into Point-Slope Form:
$$y - y_1 = m(x - x_1)$$
$$y - (-3) = 3(x - 2)$$
On the left side: $y - (-3)$ becomes $y + 3$:
$$y + 3 = 3(x - 2)$$

[TA Sora] Distribute the 3 on the right side:
$$y + 3 = 3x - 6$$
Subtract 3 from both sides:
$$y = 3x - 6 - 3 \implies y = 3x - 9$$

[Prof. Park] Outstanding! $y = 3x - 9$.
Let us check: The slope is $3$, which multiplies by $-\frac{1}{3}$ to give $-1$ (perpendicular!). And if $x = 2$, $y = 3(2) - 9 = 6 - 9 = -3$, confirming the point $(2, -3)$!""",

    3: r"""[Prof. Park] On Slide 3, we dive into In-Class Practice Problem #1 from page 43: Find the equation of the line with a $y$-intercept of $(0, 5)$ and a slope of $-\frac{3}{5}$.

[TA Sora] This is the best kind of problem you can ever receive on an exam! Look at what is given:
Slope: $m = -\frac{3}{5}$.
Given point: $(0, 5)$.
Notice that $x = 0$, which means $(0, 5)$ is literally the **$y$-intercept** $b = 5$!

[Prof. Park] Because we have the slope $m$ and the $y$-intercept $b$, we do not need to do any algebraic manipulations at all. We write down Slope-Intercept Form:
$$y = mx + b$$
And substitute directly:
$$y = -\frac{3}{5}x + 5$$

[TA Sora] Done in five seconds! Students often ask: 'Can I use point-slope form here too?' You certainly can: $y - 5 = -\frac{3}{5}(x - 0) \implies y = -\frac{3}{5}x + 5$. It gives the exact same result! But recognizing that $(0, 5)$ is $b$ saves precious time. Always look for the $y$-intercept first!""",

    4: r"""[Prof. Park] Now examine In-Class Practice Problem #2 on page 43: Find the equation of the line with an $x$-intercept of $(5, 0)$ and a slope of $\frac{3}{5}$.

[TA Sora] Compare this with Problem #1 on Slide 3! Problem #1 had a $y$-intercept of $(0, 5)$. Problem #2 has an **$x$-intercept** of $(5, 0)$!
Remember: You cannot plug an $x$-intercept into the $b$ spot of $y = mx + b$! $b$ is the $y$-intercept, not the $x$-intercept!

[Prof. Park] Exactly. We must treat $(5, 0)$ as our point $(x_1, y_1) = (5, 0)$ with slope $m = \frac{3}{5}$, and deploy Point-Slope Form:
$$y - y_1 = m(x - x_1)$$
$$y - 0 = \frac{3}{5}(x - 5)$$

[TA Sora] Look at how smoothly this works out:
$y - 0$ is simply $y$:
$$y = \frac{3}{5}(x - 5)$$
Now distribute $\frac{3}{5}$:
$$\frac{3}{5} \cdot x = \frac{3}{5}x$$
$$\frac{3}{5} \cdot (-5) = -3$$
So our equation is:
$$y = \frac{3}{5}x - 3$$

[Prof. Park] Look at that: the true $y$-intercept is $(0, -3)$! If a student had mistakenly written $y = \frac{3}{5}x + 5$, their line would have been completely wrong. Never mix up $(0, 5)$ and $(5, 0)$!""",

    5: r"""[Prof. Park] Turn to In-Class Practice Problem #3 on page 43: Find the equation of the line containing the points $(-2, -3)$ and $(6, 1)$.

[TA Sora] Step 1: Find the slope $m$ between the two points:
$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{1 - (-3)}{6 - (-2)}$$
Use protective parentheses:
In the numerator: $1 - (-3) = 1 + 3 = 4$.
In the denominator: $6 - (-2) = 6 + 2 = 8$.
$$m = \frac{4}{8} = \frac{1}{2}$$

[Prof. Park] Step 2: Now pick one point to plug into Point-Slope Form. Let us choose $(6, 1)$ because both numbers are positive:
$$y - y_1 = m(x - x_1)$$
$$y - 1 = \frac{1}{2}(x - 6)$$

[TA Sora] Distribute the $\frac{1}{2}$:
$$y - 1 = \frac{1}{2}x - 3$$
Add 1 to both sides:
$$y = \frac{1}{2}x - 3 + 1 \implies y = \frac{1}{2}x - 2$$

[Prof. Park] Let us verify with our other point $(-2, -3)$:
$$\frac{1}{2}(-2) - 2 = -1 - 2 = -3!$$
It works perfectly! The line has slope $\frac{1}{2}$ and $y$-intercept $(0, -2)$.""",

    6: r"""[Prof. Park] On Slide 6, we examine In-Class Practice Problems #4 and #5 from pages 43 and 44: The Special Lines.

[TA Sora] Problem #4 asks for the line through $(4, 2)$ and $(4, -1)$.
Look at those coordinates! Both points share $x = 4$.
If the $x$-coordinates are identical:
$$m = \frac{-1 - 2}{4 - 4} = \frac{-3}{0} \implies \text{Undefined!}$$
By HOY VUX: V - U - X!
Vertical line, Undefined slope, equation $x = \text{number}$.
Therefore, the equation is:
$$x = 4$$

[Prof. Park] Now examine Problem #5: Find the equation through $(-1, 6)$ and $(5, 6)$.
Look at the coordinates: both points share $y = 6$!
$$m = \frac{6 - 6}{5 - (-1)} = \frac{0}{6} = 0$$
The slope is zero!
By HOY VUX: H - O - Y!
Horizontal line, 0 slope, equation $y = \text{number}$.
Therefore, the equation is:
$$y = 6$$

[TA Sora] Look at how effortless these problems become when you train your eyes to scan for identical coordinates before touching any algebra! Problem #4 is $x = 4$; Problem #5 is $y = 6$!""",

    7: r"""[Prof. Park] In-Class Practice Problem #6 on page 44: Find the equation of the line containing $(2, 1)$ and **parallel** to $3x - y = 7$.

[TA Sora] Step 1: Find the slope of the reference line by solving for $y$:
$$3x - y = 7$$
Subtract $3x$:
$$-y = -3x + 7$$
Divide by $-1$:
$$y = 3x - 7$$
The slope of the reference line is $m = 3$.

[Prof. Park] Step 2: Since our line is **parallel**, it must have the exact same slope:
$$m = 3$$
Step 3: Now use Point-Slope Form with point $(2, 1)$:
$$y - 1 = 3(x - 2)$$
Distribute the 3:
$$y - 1 = 3x - 6$$
Add 1 to both sides:
$$y = 3x - 5$$

[TA Sora] Verify: Slope is 3 (parallel to $3x - y = 7$), and when $x = 2$, $y = 3(2) - 5 = 1$, matching point $(2, 1)$! Clean, precise, and fast!""",

    8: r"""[Prof. Park] In-Class Practice Problem #7 on page 44: Find the equation of the line containing $(6, 3)$ and **perpendicular** to $2y - x = 20$.

[TA Sora] Step 1: Solve the reference line for $y$:
$$2y - x = 20$$
Add $x$:
$$2y = x + 20$$
Divide by 2:
$$y = \frac{1}{2}x + 10$$
The reference slope is $m_{\text{ref}} = \frac{1}{2}$.

[Prof. Park] Step 2: Because our line is **perpendicular**, we find the negative reciprocal:
Flip $\frac{1}{2} \implies 2$.
Flip the sign $\implies -2$.
So our perpendicular slope is:
$$m_{\perp} = -2$$

[TA Sora] Step 3: Use Point-Slope Form with point $(6, 3)$:
$$y - 3 = -2(x - 6)$$
Distribute $-2$:
$$y - 3 = -2x + 12$$
Add 3 to both sides:
$$y = -2x + 15$$

[Prof. Park] Outstanding! Verify: $(-2) \cdot (1/2) = -1$ (perpendicular!). At $x = 6$, $y = -2(6) + 15 = -12 + 15 = 3$, passing through $(6, 3)$!

[TA Sora] You have completely mastered Section 2.3! In Lecture 24, we enter Section 2.4: Relations, Domain, Range, and the foundation of Functions!"""
}
