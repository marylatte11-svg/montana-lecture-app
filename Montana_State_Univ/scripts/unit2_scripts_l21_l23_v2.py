# -*- coding: utf-8 -*-
"""
unit2_scripts_l21_l23_v2.py
True 20-25 minute broadcast scripts for Lectures 21, 22, and 23.
Target: 2,400 - 2,800+ words per lecture (~300-380 words per slide across 8 slides).
Rich with Montana life examples, construction, agriculture, outdoor navigation, and student mindset.
"""

SCRIPTS_L21 = {
    1: r"""[Prof. Park] Welcome back, students, to Lecture 21 of M090 Introductory Algebra! Today on page 40 of your workbook, we step into one of the most practically vital topics in all of geometry and algebra: The Relationship Between Parallel and Perpendicular Lines.

[TA Sora] Whether you are driving down Interstate 90 through the Gallatin Valley, framing a custom timber home in Big Sky, or watching the dual steel rails of the Montana Rail Link roll through Bozeman, you are looking directly at parallel lines. In pure geometry, two lines in the same plane are parallel if they never meet, no matter how far they stretch into infinity. 

[Prof. Park] But algebra demands a numerical explanation! What mathematical property guarantees that two lines will never touch, even if you follow them across the entire continent? The answer is their **slope**! If two non-vertical lines are to maintain the exact same distance between them forever, they must rise and run at the exact same rate. That gives us our primary algebraic theorem:
Two non-vertical lines are **parallel** if and only if they have the **identical slope**:
$$m_1 = m_2 \quad \text{and} \quad b_1 \neq b_2$$
Notice that second condition: $b_1 \neq b_2$. If two lines had the same slope AND the same $y$-intercept, they wouldn't be parallel lines; they would be the exact same line drawn on top of itself!

[TA Sora] Now let us talk about the opposite extreme: **Perpendicular Lines**! In construction, carpentry, and architecture, perpendicular lines are the foundation of structural stability. When carpenters frame a house in Montana to withstand 80-mile-per-hour winds and heavy winter snow loads, the wall studs must stand perfectly perpendicular—at a true 90-degree right angle—to the floor plates and foundation.

[Prof. Park] And algebraically, perpendicular slopes do not match; they are **negative reciprocals** of each other!
$$m_1 \cdot m_2 = -1 \quad \iff \quad m_2 = -\frac{1}{m_1}$$
Think about the geometry: If Line 1 is climbing uphill from southwest to northeast with a positive slope, Line 2 MUST plunge downhill from northwest to southeast with a negative slope! And their steepness must invert: if one line rises 2 feet for every 3 feet of run ($m = 2/3$), the perpendicular line must drop 3 feet for every 2 feet of run ($m = -3/2$).

[TA Sora] Here is my golden paper-and-pencil rule that I teach every student at Gallatin College: **The Two-Flip Rule!** To find a perpendicular slope, you must perform two separate flips:
1. **Flip the fraction** upside down (take the reciprocal).
2. **Flip the sign** (positive becomes negative, or negative becomes positive).
If you only do one flip, your roof framing will be crooked and collapse under the first winter blizzard! Always do both flips!""",

    2: r"""[Prof. Park] Let us immediately apply Sora's Two-Flip Rule to Example 3 on page 40 of your workbook: Determine if the lines with the given pairs of slopes are parallel, perpendicular, or neither.

[TA Sora] Let us analyze Pair A first: $m_1 = 2$ and $m_2 = 2$.
Look at the numbers directly: $m_1$ is $+2$, and $m_2$ is $+2$.
Are they identical? Yes, $m_1 = m_2 = 2$!
Because both lines rise 2 vertical feet for every 1 horizontal foot, they climb uphill at the exact same pitch—like two parallel cross-country ski tracks groomed through the snow at Bohart Ranch.
Therefore, Pair A represents **PARALLEL LINES**!

[Prof. Park] Now let us examine Pair B: $m_1 = -\frac{3}{4}$ and $m_2 = \frac{4}{3}$.
Let us run our checks methodically:
Check 1: Are they equal? No, one is negative and one is positive, so they are definitely not parallel.
Check 2: Test for perpendicularity using the product formula:
$$m_1 \cdot m_2 = \left(-\frac{3}{4}\right) \cdot \left(\frac{4}{3}\right) = -\frac{12}{12} = -1!$$
The product is exactly $-1$!

[TA Sora] Now test it using my Two-Flip Rule:
Start with $m_1 = -\frac{3}{4}$.
Flip 1 (the fraction): $-\frac{3}{4}$ flips upside down to $-\frac{4}{3}$.
Flip 2 (the sign): change negative to positive, giving $+\frac{4}{3}$!
That matches $m_2$ perfectly! Therefore, Pair B represents **PERPENDICULAR LINES** meeting at a crisp 90-degree right angle!

[Prof. Park] Now look at Pair C very carefully: $m_1 = 2$ and $m_2 = -2$.
This is the single most common trap question on Midterm Exam 2 across all of Gallatin College! A hurried student looks at $+2$ and $-2$, sees the minus sign, and instantly circles 'Perpendicular.' Sora, why is that completely wrong?

[TA Sora] Because that student only did ONE flip! They flipped the sign from positive to negative, but they completely forgot to flip the fraction upside down! The reciprocal of $2$ (which is $\frac{2}{1}$) is $\frac{1}{2}$. For perpendicularity, we needed $-\frac{1}{2}$!
Think of an A-frame cabin roof: one side rises with slope $+2$, and the other side falls with slope $-2$. They meet at the roof peak, but they meet at an acute angle, NOT a 90-degree perpendicular angle!
Let us test the product:
$$m_1 \cdot m_2 = (2) \cdot (-2) = -4 \neq -1$$
Are they equal? $2 \neq -2$, so not parallel.
Is their product $-1$? $-4 \neq -1$, so not perpendicular.
Therefore, Pair C is strictly **NEITHER**! Always verify both flips!""",

    3: r"""[Prof. Park] Now turn to Example 4 on page 40 of your workbook: Determine if the two lines $x + y = 5$ and $-2x - 2y = 7$ are parallel, perpendicular, or neither. On this slide, we tackle Step 1: Analyzing Line 1.

[TA Sora] Notice how both equations are presented in Standard Form: $Ax + By = C$. You cannot determine whether lines are parallel or perpendicular simply by glancing at their coefficients in standard form! You must convert each equation into the universal comparison format: **Slope-Intercept Form** $y = mx + b$!

[Prof. Park] Let us isolate $y$ in Line 1 step by step:
$$x + y = 5$$
Our objective is to get $y$ completely alone on the left-hand side with a coefficient of positive 1.
We eliminate the $x$-term from the left by subtracting $x$ from both sides:
$$y = -x + 5$$
Notice how we intentionally write the $-x$ term before the $+5$. That aligns our equation directly with $y = mx + b$!

[TA Sora] Now let us extract the vital parameters from Line 1:
What is multiplying $x$? There is a negative sign, which represents an invisible $-1$:
$$m_1 = -1$$
And what is the constant term at the end? It is $+5$:
$$b_1 = 5 \implies \text{The } y\text{-intercept is } (0, 5)$$

[Prof. Park] Think about what this line represents in real life. Suppose you have a fixed budget of $500 for a weekend ski trip to Bridger Bowl. If $x$ represents the amount you spend on lift tickets and $y$ represents what you have left for food and lodging, $x + y = 5$ (in hundreds of dollars) means every single dollar you spend on skiing decreases your lodging budget by exactly one dollar! That is a negative slope of $-1$.

[TA Sora] As you run 1 unit right, you drop 1 unit down. Keep $m_1 = -1$ and $b_1 = 5$ locked in your mind. On Slide 4, we solve Line 2!""",

    4: r"""[Prof. Park] On Slide 4, we execute Step 2 of Example 4: Converting Line 2, $-2x - 2y = 7$, into Slope-Intercept Form.

[TA Sora] Look at all those negative signs! This equation requires disciplined, step-by-step algebra.
Our equation is:
$$-2x - 2y = 7$$
First, we want the $y$-term alone on the left side. We eliminate the $-2x$ term by adding $2x$ to both sides of the equation:
$$-2y = 2x + 7$$
Again, place the $x$-term first so we maintain the $mx + b$ structure.

[Prof. Park] Now comes the most dangerous moment where many students slip up: We must divide EVERY single term on both sides by the coefficient of $y$, which is $-2$!
$$y = \frac{2x}{-2} + \frac{7}{-2}$$
Let us simplify each fraction individually with absolute precision:
First term: $\frac{2x}{-2} = -1x = -x$.
Second term: $\frac{7}{-2} = -\frac{7}{2} = -3.5$.
So our simplified slope-intercept equation is:
$$y = -x - \frac{7}{2}$$

[TA Sora] Let us read off the parameters for Line 2:
The slope is the coefficient of $x$, which is:
$$m_2 = -1$$
And the constant term is:
$$b_2 = -\frac{7}{2} = -3.5 \implies \text{The } y\text{-intercept is } (0, -3.5)$$

[Prof. Park] Compare those numbers with Line 1 from Slide 3:
Line 1 had slope $m_1 = -1$ and intercept $b_1 = 5$.
Line 2 has slope $m_2 = -1$ and intercept $b_2 = -3.5$.
Look at those slopes: both are $-1$! On Slide 5, let us put them together on the Cartesian grid and deliver our final conclusion.""",

    5: r"""[Prof. Park] On Slide 5, we present the visual confirmation and mathematical conclusion for Example 4. Look at the coordinate plane on your screen!

[TA Sora] Let us conduct our formal two-step comparison:
Step 1: Check the slopes:
$$m_1 = -1 \quad \text{and} \quad m_2 = -1 \implies m_1 = m_2$$
Both slopes are completely identical!
Step 2: Check the $y$-intercepts:
$$b_1 = 5 \quad \text{and} \quad b_2 = -3.5 \implies b_1 \neq b_2$$
The intercepts are completely distinct!

[Prof. Park] Therefore, by the formal definition of parallel lines:
$$\mathbf{\text{Line 1 and Line 2 are PARALLEL!}}$$
Look at the graph: Line 1 crosses the vertical axis high up at $(0, 5)$ and descends at a 45-degree angle. Line 2 crosses lower down at $(0, -3.5)$ and descends at the exact same 45-degree angle. They track across the plane like two cross-country skiers moving down a mountain trail in Bozeman, perfectly side by side, maintaining the exact same separation from negative infinity to positive infinity.

[TA Sora] And think about what this means for solving equations! Later in Unit 2, in Lectures 26 through 30, we will solve systems of linear equations by finding where two lines intersect. If two lines are parallel, they never intersect—not even once! That means the system of equations formed by Line 1 and Line 2 has **NO SOLUTION**!

[Prof. Park] That geometric insight connects algebra to calculus. A system with parallel lines is called 'inconsistent' because there is no point in the universe where both equations can be true at the same time. Remember: Equal slopes and different intercepts always mean Parallel!""",

    6: r"""[Prof. Park] Now let us move to Example 5 on page 40 of your workbook: Determine if the two lines $-x + 2y = 6$ and $2x + y = 4$ are parallel, perpendicular, or neither. On this slide, we begin Step 1: Solving Line 1.

[TA Sora] Our first equation is:
$$-x + 2y = 6$$
Let us isolate $y$ so we can read its slope and intercept clearly.
Step 1: Add $x$ to both sides to move the $x$-term across the equals sign:
$$2y = x + 6$$
Step 2: Now divide every single term on both sides by the coefficient 2:
$$y = \frac{x}{2} + \frac{6}{2}$$

[Prof. Park] Now simplify those fractions. Many students get confused by $\frac{x}{2}$. Remember that $\frac{x}{2}$ is identical to $\frac{1}{2}x$! There is an understood 1 in front of $x$. And $6$ divided by $2$ is $3$:
$$y = \frac{1}{2}x + 3$$

[TA Sora] Let us extract the vital parameters for Line 1:
The slope is:
$$m_1 = \frac{1}{2}$$
And the $y$-intercept is:
$$b_1 = 3 \implies (0, 3)$$

[Prof. Park] Think about this slope in outdoor Montana hiking terms: A slope of $\frac{1}{2}$ means for every 2 horizontal feet you walk along the trail toward Hyalite Canyon, you gain 1 vertical foot of elevation. It is a steady, gentle, gradual uphill climb!
And where did you start? At basecamp elevation 3!

[TA Sora] Record $m_1 = \frac{1}{2}$ in your notebook. On Slide 7, we will solve Line 2, find its slope, and see how they interact!""",

    7: r"""[Prof. Park] On Slide 7, we solve Line 2 of Example 5: $2x + y = 4$, and deliver our visual and algebraic conclusion.

[TA Sora] Let us isolate $y$ in Line 2:
$$2x + y = 4$$
Subtract $2x$ from both sides:
$$y = -2x + 4$$
Look at how wonderfully quick that was! The coefficient of $y$ was already 1, so no division was necessary.
Let us read off the parameters for Line 2:
The slope is:
$$m_2 = -2 \quad \left(\text{or } -\frac{2}{1}\right)$$
And the $y$-intercept is:
$$b_2 = 4 \implies (0, 4)$$

[Prof. Park] Now let us compare our two slopes side by side:
From Slide 6: $m_1 = \frac{1}{2}$.
From Line 2: $m_2 = -2$.
Let us test the perpendicular condition by multiplying them:
$$m_1 \cdot m_2 = \left(\frac{1}{2}\right) \cdot (-2) = -\frac{2}{2} = -1!$$

[TA Sora] The product is $-1$! And let us verify with my Two-Flip Rule:
Take $m_1 = \frac{1}{2}$.
Flip 1: Invert the fraction $\frac{1}{2} \implies \frac{2}{1} = 2$.
Flip 2: Invert the sign from positive to negative $\implies -2$!
It matches $m_2$ with 100% precision!
Therefore:
$$\mathbf{\text{Line 1 and Line 2 are PERPENDICULAR!}}$$

[Prof. Park] Now look at the graph on your screen! Line 1 climbs gently uphill with slope $\frac{1}{2}$, while Line 2 drops steeply downhill with slope $-2$. At their point of intersection, they form a perfect, rigid 90-degree right angle! In civil engineering and road construction, when engineers build drainage channels alongside Montana mountain highways, the culverts are cut perpendicular to the road to channel snowmelt away with maximum hydraulic efficiency!

[TA Sora] Perpendicularity is everywhere around us. Whenever $m_1 \cdot m_2 = -1$, you have guaranteed squareness!""",

    8: r"""[Prof. Park] On Slide 8, we present the Section 2.2 Parallel & Perpendicular Master Summary Checklist. Let us cement these principles into your mathematical reflex system.

[TA Sora] Here is your universal 3-step battle plan for any problem asking about parallel or perpendicular lines:
1. **Always isolate $y$ first:** Convert every equation into Slope-Intercept Form $y = mx + b$. Never guess based on standard form coefficients!
2. **Identify the slopes:** Extract $m_1$ and $m_2$ cleanly as numerical values, never including the letter $x$.
3. **Run the Decision Matrix:**
   - **Parallel:** Are $m_1 = m_2$ and $b_1 \neq b_2$? (Same slope, different intercepts).
   - **Perpendicular:** Is $m_1 \cdot m_2 = -1$? (Negative reciprocals: flip the fraction and flip the sign).
   - **Neither:** If they fail both tests, declare them Neither!

[Prof. Park] And do not forget our special vertical and horizontal cases:
- Any horizontal line ($m = 0$, $y = c$) is **perpendicular** to any vertical line ($m = \text{undefined}$, $x = k$).
- Any two distinct horizontal lines are **parallel** to each other.
- Any two distinct vertical lines are **parallel** to each other.

[TA Sora] Think about this as a life mindset as well: In college and in your career, when you work in parallel with great mentors, you learn to move forward at the same disciplined pace. But sometimes in life, you need to make a perpendicular pivot—a complete 90-degree change in direction that opens up an entirely new horizon!

[Prof. Park] In Lecture 22, we step into Section 2.3: Writing Equations of Lines using the most powerful formula in algebra—the Point-Slope Formula! Outstanding effort today, everyone!"""
}

SCRIPTS_L22 = {
    1: r"""[Prof. Park] Welcome to Lecture 22 of M090 Introductory Algebra! Today on page 41 of your workbook, we open Section 2.3: Writing Equations of Lines.

[TA Sora] In Sections 2.1 and 2.2, we played the role of an inspector: we were handed an equation, and our job was to find its slope, find its intercepts, and plot its graph. Today, we step into the shoes of the architect and builder! We are given real-world data points or geometric clues, and our job is to construct the mathematical equation of the line from scratch!

[Prof. Park] To accomplish this, algebra gives us three primary linear forms:
1. **Slope-Intercept Form:** $y = mx + b$. This is our favorite finishing format because it displays the slope $m$ and $y$-intercept $(0, b)$ directly.
2. **Point-Slope Form:**
$$y - y_1 = m(x - x_1)$$
This formula is the supreme powerhouse of linear algebra!
3. **Standard Form:** $Ax + By = C$.

[TA Sora] Why do we call Point-Slope Form the powerhouse? Because in real-world science, ranching, and engineering, you almost NEVER know the $y$-intercept in advance! Think about wildlife biologists tracking grizzly bears in Yellowstone National Park: you capture a GPS reading at 2:00 PM at coordinates $(x_1, y_1)$, and you measure the bear's heading and speed (slope $m$). You don't know where the bear was at midnight ($x = 0$)! Point-Slope Form lets you plug in ANY known data point $(x_1, y_1)$ on the entire line and construct the exact equation instantly!

[Prof. Park] And where does Point-Slope Form come from? Look at the slope formula we mastered in Lecture 20:
$$m = \frac{y - y_1}{x - x_1}$$
Multiply both sides of that equation by the denominator $(x - x_1)$:
$$m(x - x_1) = y - y_1 \quad \iff \quad y - y_1 = m(x - x_1)$$
It is literally the slope formula rearranged to isolate the change in $y$!

[TA Sora] Let us put this magnificent formula into action with Example 1 on page 41!""",

    2: r"""[Prof. Park] Example 1 on page 41: Find the equation of the line with a slope of $\frac{3}{2}$ that contains the point $(-4, 1)$. Write your final answer in Slope-Intercept Form $y = mx + b$.

[TA Sora] Step 1: Gather and label your given data!
We are given:
Slope: $m = \frac{3}{2}$.
Known point: $(x_1, y_1) = (-4, 1)$.
Notice that this given point has an $x$-coordinate of $-4$, not $0$! That means this point is NOT a $y$-intercept. Therefore, we cannot just plug $1$ into $b$ of $y = mx + b$. We MUST use Point-Slope Form!

[Prof. Park] Step 2: Write down the point-slope formula clearly on your paper:
$$y - y_1 = m(x - x_1)$$
Now substitute our values, using TA Sora's Protective Parentheses Rule around the negative coordinate:
$$y - 1 = \frac{3}{2}(x - (-4))$$
Inside the parentheses, subtracting a negative four turns into addition: $x - (-4) = x + 4$:
$$y - 1 = \frac{3}{2}(x + 4)$$

[TA Sora] Step 3: Distribute the fraction $\frac{3}{2}$ to both terms inside the parentheses:
$$\frac{3}{2} \cdot x = \frac{3}{2}x$$
$$\frac{3}{2} \cdot 4 = \frac{12}{2} = 6$$
So our equation becomes:
$$y - 1 = \frac{3}{2}x + 6$$

[Prof. Park] Step 4: Now isolate $y$ to finish in Slope-Intercept Form $y = mx + b$. Add 1 to both sides:
$$y = \frac{3}{2}x + 6 + 1 \implies y = \frac{3}{2}x + 7$$

[TA Sora] Look at how magnificent that final equation is: $y = \frac{3}{2}x + 7$.
Now let us perform a 5-second sanity check:
Does it have a slope of $\frac{3}{2}$? Yes!
Does it contain the point $(-4, 1)$? Let us plug in $x = -4$:
$$y = \frac{3}{2}(-4) + 7 = -6 + 7 = 1!$$
The output is 1! It passes through $(-4, 1)$ with 100% precision!""",

    3: r"""[Prof. Park] Now turn to Example 2 on page 41: Find the equation of the line with an $x$-intercept of $(-3, 0)$ and a slope of $-\frac{4}{3}$. Write the equation in slope-intercept form.

[TA Sora] Students, please pay extreme attention to the wording of this problem! It says 'an $x$-intercept of $(-3, 0)$.'
During tutoring sessions at Gallatin College, I see at least one student every semester who sees $(-3, 0)$ and writes: '$y = -\frac{4}{3}x - 3$.'
Professor, explain why that is a total disaster!

[Prof. Park] Because the letter $b$ in $y = mx + b$ stands strictly for the **$y$-intercept** $(0, b)$! An $x$-intercept is a point where $y = 0$, sitting on the horizontal axis. You can never plug an $x$-intercept into the $b$ slot of slope-intercept form!
Instead, treat $(-3, 0)$ as an ordinary point: $(x_1, y_1) = (-3, 0)$, with slope $m = -\frac{4}{3}$, and deploy Point-Slope Form!

[TA Sora] Let us substitute into Point-Slope Form:
$$y - y_1 = m(x - x_1)$$
$$y - 0 = -\frac{4}{3}(x - (-3))$$
Look at how cleanly this simplifies:
On the left side: $y - 0$ is simply $y$!
On the right side: $x - (-3)$ becomes $(x + 3)$:
$$y = -\frac{4}{3}(x + 3)$$

[Prof. Park] Now distribute the slope $-\frac{4}{3}$ across the parentheses:
$$-\frac{4}{3} \cdot x = -\frac{4}{3}x$$
$$-\frac{4}{3} \cdot 3 = -\frac{12}{3} = -4$$
So our final equation is:
$$y = -\frac{4}{3}x - 4$$

[TA Sora] Look at that result! The true $y$-intercept is $(0, -4)$, which is completely different from $-3$! If a student had plugged $-3$ into $b$, their entire line would have been parallel to the correct line, but shifted off by an entire unit. Always treat $x$-intercepts as $(x_1, 0)$ in point-slope form!""",

    4: r"""[Prof. Park] On Slide 4, we examine Example 3 Step 1 on page 41: Find the equation of the line that contains the two points $(2, 3)$ and $(-6, 1)$.

[TA Sora] Look at what is given here: We are given TWO points, but we are NOT given the slope $m$!
Think about what we need to build a line: We need a point and a slope. We have two points, but zero slopes! What is our first mission, Professor?

[Prof. Park] Our first mission is to manufacture our own slope! Remember the slope formula from Lecture 20: Given any two points on a line, you can always compute the slope using:
$$m = \frac{y_2 - y_1}{x_2 - x_1}$$
Let us label our coordinates carefully:
Let $(x_1, y_1) = (2, 3)$ and $(x_2, y_2) = (-6, 1)$.

[TA Sora] Now substitute with protective parentheses:
$$m = \frac{1 - 3}{-6 - 2}$$
In the numerator: $1 - 3 = -2$. That is our Rise (a drop of 2 units).
In the denominator: $-6 - 2 = -8$. That is our Run (a move of 8 units to the left).
So our slope fraction is:
$$m = \frac{-2}{-8}$$

[Prof. Park] Now simplify: A negative divided by a negative is always positive! And reduce $\frac{2}{8}$ by dividing numerator and denominator by 2:
$$m = \frac{1}{4}$$
Our slope is positive $\frac{1}{4}$!

[TA Sora] Now we have conquered Step 1! We have our slope $m = \frac{1}{4}$, and we have two points to choose from: $(2, 3)$ or $(-6, 1)$. On Slide 5, we will take these ingredients and construct the final equation!""",

    5: r"""[Prof. Park] On Slide 5, we execute Example 3 Step 2: Use the slope $m = \frac{1}{4}$ and the point $(2, 3)$ to find the equation in Slope-Intercept Form $y = mx + b$.

[TA Sora] A question students always ask: 'Sora, which point should I choose to plug into Point-Slope Form? $(2, 3)$ or $(-6, 1)$?'
The answer is: It does NOT matter! Both points lie on the exact same line, so both will lead to the exact same final equation. My practical advice: choose the point with smaller, positive numbers to keep your arithmetic clean and stress-free!

[Prof. Park] Let us choose $(x_1, y_1) = (2, 3)$ with $m = \frac{1}{4}$:
$$y - y_1 = m(x - x_1)$$
$$y - 3 = \frac{1}{4}(x - 2)$$
Distribute $\frac{1}{4}$ across the parentheses:
$$y - 3 = \frac{1}{4}x - \frac{2}{4}$$
Simplify $\frac{2}{4}$ to $\frac{1}{2}$:
$$y - 3 = \frac{1}{4}x - \frac{1}{2}$$

[TA Sora] Now isolate $y$ by adding 3 to both sides:
$$y = \frac{1}{4}x - \frac{1}{2} + 3$$
To add $-\frac{1}{2}$ and $3$, convert 3 into an equivalent fraction with denominator 2: $3 = \frac{6}{2}$:
$$y = \frac{1}{4}x - \frac{1}{2} + \frac{6}{2}$$
Combine the fractions: $-\frac{1}{2} + \frac{6}{2} = +\frac{5}{2}$:
$$y = \frac{1}{4}x + \frac{5}{2}$$

[Prof. Park] Look at the graph on your screen! The line passes through $(-6, 1)$ and $(2, 3)$, climbing gently with a slope of $\frac{1}{4}$, and it cuts through the vertical axis at exactly $2.5$, which is $\frac{5}{2}$! Let us test $(-6, 1)$ in our finished equation: $\frac{1}{4}(-6) + \frac{5}{2} = -\frac{3}{2} + \frac{5}{2} = \frac{2}{2} = 1$! Everything checks out with total mathematical perfection!""",

    6: r"""[Prof. Park] Turn to Example 4 on page 42: Find the equation of the line containing the points $(1, 7)$ and $(-3, 7)$.

[TA Sora] Before you grab your pencil and start writing out point-slope formulas, stop and apply TA Sora's Three-Second Scan Rule! Look closely at the coordinates of both points:
Point 1: $(1, 7)$
Point 2: $(-3, 7)$
What jumps out immediately? Both points have the exact same $y$-coordinate: $y = 7$!

[Prof. Park] If both points share the exact same vertical elevation of 7, let us see what happens if you mechanically compute the slope:
$$m = \frac{7 - 7}{-3 - 1} = \frac{0}{-4} = 0$$
The slope is zero!

[TA Sora] And what does our famous HOY VUX rule from Lecture 19 tell us?
H - O - Y!
- **H** stands for **Horizontal** line.
- **O** stands for **0 (Zero)** slope.
- **Y** stands for **$y = \text{number}$** equation!
Because the $y$-value is permanently locked at 7, the equation of the line is simply:
$$y = 7$$

[Prof. Park] You do not need point-slope form, you do not need fractions, you do not need four steps of algebra. The equation was right in front of you the entire time: $y = 7$!

[TA Sora] Think of a flat runway at Bozeman Yellowstone International Airport: the elevation of the runway doesn't change whether you are 1 mile east or 3 miles west. The altitude is locked. Whenever $y$-coordinates match, write $y = c$!""",

    7: r"""[Prof. Park] Now examine Example 5 on page 42: Find the equation of the line containing the points $(2, -8)$ and $(2, 1)$.

[TA Sora] Again, run your Three-Second Scan! Look at the coordinates:
Point 1: $(2, -8)$
Point 2: $(2, 1)$
Now the $x$-coordinates are identical: $x_1 = 2$ and $x_2 = 2$!

[Prof. Park] Let us compute the slope and observe what happens algebraically:
$$m = \frac{1 - (-8)}{2 - 2} = \frac{1 + 8}{0} = \frac{9}{0}$$
Division by zero! The slope is **UNDEFINED**!

[TA Sora] And what does HOY VUX command us?
V - U - X!
- **V** stands for **Vertical** line.
- **U** stands for **Undefined** slope.
- **X** stands for **$x = \text{number}$** equation!
Because the $x$-coordinate is permanently locked at 2, you CANNOT write this line in Slope-Intercept Form $y = mx + b$ because there is no $y$ in the equation! The equation of the line is simply:
$$x = 2$$

[Prof. Park] Look at the symmetry of Examples 4 and 5 side by side:
When the $y$-coordinates are identical, you have a horizontal line: $y = c$.
When the $x$-coordinates are identical, you have a vertical line: $x = c$.
Recognizing these patterns instantly saves you minutes on exams and protects you from division-by-zero confusion!""",

    8: r"""[Prof. Park] On Slide 8, we present the Section 2.3 Part 1 Master Line-Building Flowchart. This is the master algorithm that professional mathematicians and engineers use every day.

[TA Sora] Here is your decision tree:
- **Scenario 1: Given Slope $m$ and $y$-intercept $(0, b)$:**
  Plug directly into Slope-Intercept Form: $y = mx + b$. Done in seconds!
- **Scenario 2: Given Slope $m$ and ANY random point $(x_1, y_1)$:**
  Use Point-Slope Form:
  $$y - y_1 = m(x - x_1)$$
  Distribute $m$, add or subtract $y_1$, and finish in $y = mx + b$.
- **Scenario 3: Given TWO points $(x_1, y_1)$ and $(x_2, y_2)$:**
  Step A: Calculate $m = \frac{y_2 - y_1}{x_2 - x_1}$.
  Step B: Pick either point and substitute into $y - y_1 = m(x - x_1)$.
  Step C: Solve for $y$.
- **Scenario 4: Special Lines (HOY VUX):**
  If $y_1 = y_2$, horizontal line: $y = c$.
  If $x_1 = x_2$, vertical line: $x = c$.

[Prof. Park] In Lecture 23, we take this complete flowchart and apply it to advanced scenarios: finding lines parallel or perpendicular to existing equations through given points, followed by a comprehensive set of seven in-class practice problems. Fantastic focus today, everyone!"""
}

SCRIPTS_L23 = {
    1: r"""[Prof. Park] Welcome to Lecture 23 of M090! Today on pages 42 through 44 of your workbook, we reach the grand synthesis of Section 2.3: Writing equations of lines that pass through specific points and are Parallel or Perpendicular to existing lines, followed by comprehensive in-class practice problems.

[TA Sora] Let us begin on page 42 with Example 6: Find the equation of the line containing the point $(-1, 3)$ and **parallel** to the line $y = 4x - 5$. Write the final answer in slope-intercept form.

[Prof. Park] Let us break this problem down like an investigator piecing together clues:
Clue 1: Our target line must pass through the specific point $(x_1, y_1) = (-1, 3)$.
Clue 2: Our target line must be **parallel** to the given reference line $y = 4x - 5$.

[TA Sora] What does 'parallel' tell us about the slope? Parallel lines have the **identical slope**!
Look at the reference line: $y = 4x - 5$. Its slope is $m = 4$.
Therefore, our new line must also have slope:
$$m = 4$$

[Prof. Park] Now we have our two essential building blocks:
We have our slope $m = 4$, and we have our point $(x_1, y_1) = (-1, 3)$.
Now we deploy Point-Slope Form:
$$y - y_1 = m(x - x_1)$$
Substitute with protective parentheses:
$$y - 3 = 4(x - (-1))$$
Inside the parentheses, $x - (-1)$ becomes $x + 1$:
$$y - 3 = 4(x + 1)$$

[TA Sora] Now distribute the 4:
$$y - 3 = 4x + 4$$
Add 3 to both sides to isolate $y$:
$$y = 4x + 4 + 3 \implies y = 4x + 7$$

[Prof. Park] Look at that finished equation: $y = 4x + 7$.
Let us verify both conditions:
1. Is its slope 4? Yes, so it is parallel to $y = 4x - 5$!
2. Does it pass through $(-1, 3)$? Plug in $x = -1$: $4(-1) + 7 = -4 + 7 = 3$!
It satisfies every condition with total mathematical perfection!""",

    2: r"""[Prof. Park] Now turn to Example 7 on page 42: Find the equation of the line containing the point $(2, -3)$ and **perpendicular** to the line $y = -\frac{1}{3}x + 2$.

[TA Sora] Notice that crucial word: **PERPENDICULAR**!
Let us extract our slope using TA Sora's Two-Flip Rule:
The reference line is $y = -\frac{1}{3}x + 2$, so its slope is $m_{\text{ref}} = -\frac{1}{3}$.
To find our perpendicular slope $m_{\perp}$:
Flip 1 (the fraction): Invert $\frac{1}{3} \implies \frac{3}{1} = 3$.
Flip 2 (the sign): Invert negative to positive $\implies +3$!
Therefore, our perpendicular slope is:
$$m_{\perp} = 3$$

[Prof. Park] Now we have our ingredients:
Slope: $m = 3$.
Target point: $(x_1, y_1) = (2, -3)$.
Substitute into Point-Slope Form:
$$y - y_1 = m(x - x_1)$$
$$y - (-3) = 3(x - 2)$$
On the left side, $y - (-3)$ becomes $y + 3$:
$$y + 3 = 3(x - 2)$$

[TA Sora] Distribute the 3 on the right side:
$$y + 3 = 3x - 6$$
Subtract 3 from both sides to isolate $y$:
$$y = 3x - 6 - 3 \implies y = 3x - 9$$

[Prof. Park] Let us verify our answer:
1. Is the slope perpendicular? $3 \cdot \left(-\frac{1}{3}\right) = -1$. Yes!
2. Does it pass through $(2, -3)$? Plug in $x = 2$: $y = 3(2) - 9 = 6 - 9 = -3$!
Both checks pass cleanly! $y = 3x - 9$ is our exact, verified solution!""",

    3: r"""[Prof. Park] On Slide 3, we begin the in-class practice marathon on page 43 with Problem #1: Find the equation of the line with a $y$-intercept of $(0, 5)$ and a slope of $-\frac{3}{5}$.

[TA Sora] This problem is an absolute gift on an exam if you read the clues carefully!
Look at the given information:
Slope: $m = -\frac{3}{5}$.
Given point: $(0, 5)$.
Notice that the $x$-coordinate of the given point is $0$! That means $(0, 5)$ is literally the **$y$-intercept** $b = 5$!

[Prof. Park] Because we are given the slope $m$ and the $y$-intercept $b$, we do not need to do any algebraic manipulations at all. We write down Slope-Intercept Form:
$$y = mx + b$$
And substitute directly:
$$y = -\frac{3}{5}x + 5$$

[TA Sora] Done in five seconds! Students often ask: 'Sora, what if I didn't notice it was the $y$-intercept and used point-slope form instead?'
Let us check: $y - 5 = -\frac{3}{5}(x - 0) \implies y - 5 = -\frac{3}{5}x \implies y = -\frac{3}{5}x + 5$.
You get the exact same answer! But recognizing the $y$-intercept $(0, b)$ instantly saves you valuable exam time.""",

    4: r"""[Prof. Park] Now examine In-Class Practice Problem #2 on page 43: Find the equation of the line with an $x$-intercept of $(5, 0)$ and a slope of $\frac{3}{5}$.

[TA Sora] Compare Problem #2 side by side with Problem #1 from Slide 3!
In Problem #1, we had a $y$-intercept of $(0, 5)$.
Here in Problem #2, we have an **$x$-intercept** of $(5, 0)$!
Remember the fatal trap: You CANNOT plug an $x$-intercept into the $b$ slot of $y = mx + b$! $b$ is strictly the $y$-intercept!

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

[Prof. Park] Look at that: the true $y$-intercept is $(0, -3)$! If a student had mistakenly written $y = \frac{3}{5}x + 5$, their line would have been completely wrong. Always distinguish between $(0, 5)$ and $(5, 0)$!""",

    5: r"""[Prof. Park] Turn to In-Class Practice Problem #3 on page 43: Find the equation of the line containing the points $(-2, -3)$ and $(6, 1)$.

[TA Sora] Step 1: Find the slope $m$ between the two points using the slope formula:
$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{1 - (-3)}{6 - (-2)}$$
Use protective parentheses:
In the numerator: $1 - (-3) = 1 + 3 = 4$.
In the denominator: $6 - (-2) = 6 + 2 = 8$.
$$m = \frac{4}{8} = \frac{1}{2}$$

[Prof. Park] Step 2: Now pick one point to plug into Point-Slope Form. Let us choose $(6, 1)$ because both coordinates are positive:
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

[TA Sora] Problem #4 asks for the equation of the line containing $(4, 2)$ and $(4, -1)$.
Apply Sora's Three-Second Scan: Both points share $x = 4$!
If the $x$-coordinates are identical:
$$m = \frac{-1 - 2}{4 - 4} = \frac{-3}{0} \implies \text{Undefined!}$$
By HOY VUX: V - U - X!
Vertical line, Undefined slope, equation $x = \text{number}$.
Therefore, the equation is:
$$x = 4$$

[Prof. Park] Now examine Problem #5: Find the equation containing $(-1, 6)$ and $(5, 6)$.
Scan the coordinates: both points share $y = 6$!
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

[Prof. Park] Step 2: Since our target line is **parallel**, it must have the exact same slope:
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
