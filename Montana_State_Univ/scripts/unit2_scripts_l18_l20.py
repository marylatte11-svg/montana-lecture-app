# -*- coding: utf-8 -*-
"""
unit2_scripts_l18_l20.py
High-density broadcast tiki-taka scripts for Lectures 18, 19, and 20.
Target: ~250-350 words per slide (~2,200-2,800 words per lecture).
"""

SCRIPTS_L18 = {
    1: """[Prof. Park] Welcome to Lecture 18 of M090 Introductory Algebra! Today on page 33 of your workbook, we begin Section 2.1: Graphing Linear Equations in Two Variables.

[TA Sora] Up to this point, we plotted individual isolated points $(x, y)$. Today, we connect the dots to form continuous, unbroken straight lines that stretch infinitely in both directions across the Cartesian plane!

[Prof. Park] Every straight line in algebra can be expressed in two primary mathematical forms. The first is **Standard Form**: $Ax + By = C$, where $A$, $B$, and $C$ are typically integers and $A$ and $B$ are not both zero. The second is **Slope-Intercept Form**: $y = mx + b$, where $m$ represents the steepness or slope of the line, and $b$ represents the $y$-intercept where the line crosses the vertical axis at $(0, b)$.

[TA Sora] Many students ask: 'Sora, why do we need two different forms for the exact same line?' Think of it like tools in a carpenter's belt in Bozeman. Standard form $Ax + By = C$ is fantastic when you want to quickly find where a line hits the walls—the $x$- and $y$-intercepts—using the cover-up method. But Slope-Intercept form $y = mx + b$ gives you the rate of change and the starting elevation at a single glance!

[Prof. Park] Exactly. In Section 2.1, we master three essential techniques for graphing lines:
1. The Table of Values method.
2. The Intercepts method.
3. The Slope-Intercept method.

[TA Sora] Let us dive straight into Example 1 on page 33 and master the table method first!""",

    2: """[Prof. Park] In Example 1 on page 33, we are asked to graph the linear equation $2x + 3y = 6$ by creating a table of values. 

[TA Sora] Notice how $x$ and $y$ are both on the left-hand side: $2x + 3y = 6$. This is Standard Form $Ax + By = C$. We are completely free to choose any inputs we want for $x$, but look at the coefficient of $y$: it is 3. If we choose random numbers like $x = 1$, we get $2(1) + 3y = 6 \\implies 3y = 4 \\implies y = 4/3$, which is an awkward fraction to plot on graph paper!

[Prof. Park] That brings us to TA Sora's Golden Rule of Choosing Inputs: Pick inputs that produce clean integer outputs! Since $y$ is multiplied by 3, choosing multiples of 3 for $x$ will eliminate fractional remainders. Let us test $x = -3$, $x = 0$, and $x = 3$.

[TA Sora] Let us compute the first row with $x = -3$: Substitute inside protective parentheses: $2(-3) + 3y = 6 \\implies -6 + 3y = 6$. Add 6 to both sides: $3y = 12$. Divide by 3: $y = 4$! That gives us our first clean ordered pair: $(-3, 4)$.

[Prof. Park] Next, the easiest number in the universe: $x = 0$! Substitute $0$: $2(0) + 3y = 6 \\implies 0 + 3y = 6 \\implies 3y = 6 \\implies y = 2$! That gives us our second point: $(0, 2)$, which is our $y$-intercept.

[TA Sora] Finally, let us compute the third row with $x = 3$: Substitute: $2(3) + 3y = 6 \\implies 6 + 3y = 6$. Subtract 6 from both sides: $3y = 0 \\implies y = 0$! That gives us $(3, 0)$, which is our $x$-intercept. Three perfect, whole-number points!""",

    3: """[Prof. Park] Now let us examine Part 2 of Example 1: solving the equation $2x + 3y = 6$ explicitly for $y$. Why is solving for $y$ such a critical algebraic skill, Sora?

[TA Sora] Because solving for $y$ converts any standard-form equation directly into Slope-Intercept Form $y = mx + b$! When an equation is solved for $y$, graphing calculators and computer spreadsheets can evaluate it instantly, and human mathematicians can read the slope and intercept without doing any scratch work!

[Prof. Park] Let us perform the isolation steps with absolute precision:
$$2x + 3y = 6$$
Our goal is to isolate $y$. First, we eliminate the $x$-term from the left side by subtracting $2x$ from both sides:
$$3y = -2x + 6$$
Notice how we write $-2x$ in front of the $+6$. We do this intentionally to match the $mx + b$ structure!

[TA Sora] Now comes the most dangerous step where half of introductory algebra students lose points: we must divide every single term on both sides by the coefficient of $y$, which is 3!
$$y = \\frac{-2x + 6}{3} = -\\frac{2}{3}x + \\frac{6}{3}$$
Simplify the constant term: $6 / 3 = 2$:
$$y = -\\frac{2}{3}x + 2$$

[Prof. Park] Look at that finished equation: $y = -\\frac{2}{3}x + 2$. The slope $m$ is $-\\frac{2}{3}$, meaning for every 3 units you run to the right, you fall 2 units downward. And the $y$-intercept $b$ is $+2$, confirming the point $(0, 2)$ that we found in our table!""",

    4: """[Prof. Park] On Slide 4, we bring together the table of values, the algebraic formula, and the visual coordinate plane for $2x + 3y = 6$.

[TA Sora] Let us verify our three plotted points on the grid: $(-3, 4)$, $(0, 2)$, and $(3, 0)$. Place your straightedge along those three points. Notice how they line up perfectly!

[Prof. Park] Why do we always recommend plotting three points instead of just two? Theoretically, Euclid taught us that two points determine a unique line. But if you make an arithmetic error with one of the two points, you will draw an incorrect line and never know it!

[TA Sora] Exactly! The third point is your algebraic insurance policy—a checkpoint! If your three points do not form a perfectly straight line, one of your calculations has an arithmetic error. Stop, check your signs, and fix it before moving on.

[Prof. Park] Now look at the intercepts on the screen:
The graph crosses the vertical $y$-axis at $(0, 2)$. That is our **$y$-intercept**.
The graph crosses the horizontal $x$-axis at $(3, 0)$. That is our **$x$-intercept**.

[TA Sora] Notice that the line slopes downward from left to right. That makes total sense because our slope is $m = -2/3$. When you hike down from the ridge of the Bridger Mountains toward Bozeman, your elevation decreases as your horizontal distance increases—that is a negative slope!""",

    5: """[Prof. Park] Turn to Example 2A on page 33: Identify the slope and $y$-intercept for the equation $y = \\frac{1}{4}x - 6$.

[TA Sora] This problem is an absolute gift if you know what to look for! Look at the equation: $y = \\frac{1}{4}x - 6$. It is already in pure Slope-Intercept Form: $y = mx + b$!

[Prof. Park] When an equation is already solved for $y$, you do not need to do any algebraic manipulations at all. You simply align it with the template:
$$y = mx + b$$
$$y = \\frac{1}{4}x + (-6)$$

[TA Sora] Comparing terms directly:
The coefficient sitting in front of $x$ is the slope: $m = \\frac{1}{4}$.
The constant term at the end is $b = -6$.
Therefore, the line intercepts the $y$-axis at the ordered pair $(0, -6)$!

[Prof. Park] Let us translate what $m = \\frac{1}{4}$ means geometrically for graphing. The numerator is the **Rise** ($+1$), and the denominator is the **Run** ($+4$). Starting from the $y$-intercept at $(0, -6)$, you rise up 1 unit vertically, and run 4 units to the right horizontally, landing at $(4, -5)$!

[TA Sora] A common student pitfall: writing 'the slope is $\\frac{1}{4}x$.' Never include the variable $x$ in the slope! The slope is purely the numerical coefficient $\\frac{1}{4}$. $x$ is the independent variable, not the slope!""",

    6: """[Prof. Park] Now examine Example 2B on page 33: Identify the slope and $y$-intercept for $2x - y = 7$.

[TA Sora] Notice that this equation is NOT in slope-intercept form yet. The $x$ and $y$ are both on the left-hand side, so we must solve for $y$ first!

[Prof. Park] Step 1: Subtract $2x$ from both sides to clear the $x$-term from the left:
$$-y = -2x + 7$$
Now pause right here. Many students stop and say, 'The slope is $-2$ and the intercept is $7$!' Why is that completely wrong, Sora?

[TA Sora] Because that is negative $y$, not positive $y$! The negative sign in front of $y$ represents an invisible $-1$ multiplying $y$: $(-1)y = -2x + 7$. Slope-intercept form requires $y$ to have a coefficient of positive $1$!

[Prof. Park] To eliminate that negative sign, we must divide every single term on both sides by $-1$, or multiply through by $-1$:
$$\\frac{-y}{-1} = \\frac{-2x}{-1} + \\frac{7}{-1}$$
$$y = 2x - 7$$

[TA Sora] Look at how both signs flipped on the right-hand side! $-2x$ divided by $-1$ became positive $2x$, and $+7$ divided by $-1$ became $-7$.
Now we can read off our parameters:
Slope: $m = 2$ (or $\\frac{2}{1}$, meaning rise 2, run 1).
$y$-intercept: $b = -7$, which corresponds to the point $(0, -7)$!

[Prof. Park] Beautifully done. Always be on high alert whenever $y$ has a minus sign in front of it!""",

    7: """[Prof. Park] On Slide 7, we arrive at page 34 of your workbook and one of the most powerful concepts in all of linear graphing: The Formal Definition of Intercepts.

[TA Sora] An **intercept** is simply the geometric address where a graph cuts through or intercepts one of the coordinate axes.
- The **$x$-intercept** is the point where the line crosses the horizontal $x$-axis. At any point on the horizontal axis, the vertical elevation is zero! Therefore, every $x$-intercept has the form $(a, 0)$, where $y = 0$.
- The **$y$-intercept** is the point where the line crosses the vertical $y$-axis. At any point on the vertical spine, the horizontal position is zero! Therefore, every $y$-intercept has the form $(0, b)$, where $x = 0$.

[Prof. Park] This gives us the universal, foolproof algebraic recipe for finding intercepts:
To find the **$x$-intercept**, substitute $y = 0$ into the equation and solve for $x$.
To find the **$y$-intercept**, substitute $x = 0$ into the equation and solve for $y$.

[TA Sora] In Montana carpentry and drafting, this is known as the 'Cover-Up Method!' If you have an equation like $5x + 2y = 10$, and you want the $x$-intercept, put your thumb right over the $2y$ term because $y=0$ wipes it out completely! You are left with $5x = 10$, so $x = 2$. It takes less than two seconds!

[Prof. Park] It is extraordinarily fast and reliable. Let us apply this technique to Example 3A on the very next slide!""",

    8: """[Prof. Park] Example 3A on page 34: Find the $x$- and $y$-intercepts algebraically for $5x + 2y = 6$, and then re-write the equation in slope-intercept form.

[TA Sora] Let us find the **$x$-intercept** first: Set $y = 0$ in $5x + 2y = 6$:
$$5x + 2(0) = 6 \\implies 5x = 6$$
Divide both sides by 5:
$$x = \\frac{6}{5} = 1.2$$
So the $x$-intercept as an ordered pair is $\\left(\\frac{6}{5}, 0\\right)$.

[Prof. Park] Next, find the **$y$-intercept**: Set $x = 0$ in $5x + 2y = 6$:
$$5(0) + 2y = 6 \\implies 2y = 6$$
Divide both sides by 2:
$$y = 3$$
So the $y$-intercept as an ordered pair is $(0, 3)$!

[TA Sora] Now let us re-write the equation in Slope-Intercept Form $y = mx + b$. Start with $5x + 2y = 6$.
Subtract $5x$ from both sides:
$$2y = -5x + 6$$
Divide every term by 2:
$$y = -\\frac{5}{2}x + \\frac{6}{2} \\implies y = -\\frac{5}{2}x + 3$$

[Prof. Park] Notice the beautiful consistency! The slope-intercept form gives $b = 3$, which exactly matches the $y$-intercept $(0, 3)$ we found with the cover-up method. The slope is $m = -5/2$, meaning from $(0, 3)$ you drop 5 units down and run 2 units right.

[TA Sora] In Lecture 19, we explore more intercept problems, including fractional lines, direct variation, and the special cases of horizontal and vertical lines!"""
}

SCRIPTS_L19 = {
    1: """[Prof. Park] Welcome to Lecture 19 of M090! Today we continue Section 2.1, diving deeper into intercepts, direct variation through the origin, and the famous special lines: horizontal lines and vertical lines.

[TA Sora] Let us pick up right where we left off on page 35 of your workbook with Example 3B: Find the $x$- and $y$-intercepts algebraically for the linear equation $4x - 5y = 10$, and then re-write it in slope-intercept form.

[Prof. Park] Let us calculate the **$x$-intercept** first. Sora, what is our golden rule for $x$-intercepts?

[TA Sora] Set $y = 0$! Substituting zero for $y$:
$$4x - 5(0) = 10 \\implies 4x = 10$$
Divide both sides by 4:
$$x = \\frac{10}{4} = \\frac{5}{2} = 2.5$$
As a formal ordered pair, our $x$-intercept is $\\left(\\frac{5}{2}, 0\\right)$.

[Prof. Park] Now calculate the **$y$-intercept**: Set $x = 0$:
$$4(0) - 5y = 10 \\implies -5y = 10$$
Divide both sides by $-5$:
$$y = \\frac{10}{-5} = -2$$
As a formal ordered pair, our $y$-intercept is $(0, -2)$!

[TA Sora] Now re-write in Slope-Intercept Form:
$$4x - 5y = 10 \\implies -5y = -4x + 10$$
Divide every single term by $-5$:
$$y = \\frac{-4}{-5}x + \\frac{10}{-5} \\implies y = \\frac{4}{5}x - 2$$

[Prof. Park] Notice how the negative divided by negative produces a positive slope $m = +4/5$, and the constant is $b = -2$, matching $(0, -2)$. Always write your intercepts as full ordered pairs $(x, y)$, never just single numbers!""",

    2: """[Prof. Park] Turn to page 36 for Example 3C: Find the intercepts for $y = -\\frac{3}{2}x - 3$.

[TA Sora] Notice that this equation is already presented in slope-intercept form! That means we get the $y$-intercept for free without any algebraic work at all! The constant term is $b = -3$, which immediately tells us the $y$-intercept is $(0, -3)$.

[Prof. Park] But what about the $x$-intercept? We must still do the algebraic work by substituting $y = 0$:
$$0 = -\\frac{3}{2}x - 3$$
How do we solve for $x$ when a fraction is involved, Sora?

[TA Sora] Add 3 to both sides first to isolate the fraction term:
$$3 = -\\frac{3}{2}x$$
Now, multiply both sides by the reciprocal of $-\\frac{3}{2}$, which is $-\\frac{2}{3}$:
$$\\left(-\\frac{2}{3}\\right) \\cdot 3 = x \\implies x = -2!$$

[Prof. Park] Clean and elegant: $x = -2$. That means our $x$-intercept is $(-2, 0)$.

[TA Sora] Look at the graph on your screen. The line crosses the horizontal axis at $(-2, 0)$ and the vertical axis at $(0, -3)$. Between those two points, you drop down 3 units and run right 2 units, which perfectly confirms the slope $m = -3/2$!

[Prof. Park] If you ever get stuck clearing fractions, remember that multiplying both sides of an equation by the denominator clears the fraction in one single step. Mathematics always gives you multiple paths to the truth!""",

    3: """[Prof. Park] Now examine Example 3D on page 36: Find the $x$- and $y$-intercepts for the direct variation equation $y = 2x$. 

[TA Sora] This is a fascinating problem that surprises many students! Let us follow our standard procedure:
To find the $y$-intercept, set $x = 0$:
$$y = 2(0) = 0 \\implies (0, 0)$$
Now to find the $x$-intercept, set $y = 0$:
$$0 = 2x \\implies x = 0 \\implies (0, 0)$$

[Prof. Park] Both intercepts are the exact same point: the Origin $(0, 0)$! What does that mean for someone trying to graph this line using only the intercepts method?

[TA Sora] It means the intercept method fails to give you two distinct points! You only have one point—the origin. And as we know, infinitely many different lines can pivot through the origin at different angles. You cannot draw a unique line with only one point!

[Prof. Park] So what is the remedy? Whenever a line passes through the origin ($b = 0$), you must choose an additional test point by picking a non-zero input for $x$.

[TA Sora] Let us pick $x = 1$: $y = 2(1) = 2$, giving us the point $(1, 2)$. Or pick $x = -1$: $y = 2(-1) = -2$, giving $(-1, -2)$. Now you have $(0, 0)$, $(1, 2)$, and $(-1, -2)$, which clearly define a line with slope $m = 2$ passing straight through the origin!

[Prof. Park] Direct variation equations $y = kx$ always pass through the origin. If you work 0 hours, your paycheck is 0 dollars!""",

    4: """[Prof. Park] On page 37, we encounter two of the most famous special cases in all of algebra. First is Example 3E: Graph the equation $y = -2$ and analyze its intercepts and slope.

[TA Sora] Look at that equation: $y = -2$. Where is $x$? There is no $x$ present! That means no matter what value $x$ takes, $y$ is permanently locked at $-2$.
If $x = -3$, $y = -2$. If $x = 0$, $y = -2$. If $x = 4$, $y = -2$.

[Prof. Park] When you plot those points on the Cartesian grid, what shape do you get? A perfectly horizontal line hovering two units below the $x$-axis!

[TA Sora] Now let us answer the intercept questions:
Does this line cross the vertical $y$-axis? Yes, at $(0, -2)$. So the $y$-intercept is $(0, -2)$.
Does this line ever cross the horizontal $x$-axis? Look at the graph: it runs completely parallel to the $x$-axis! It will never touch or cross the $x$-axis from $-\\infty$ to $+\\infty$. Therefore, there is **NO $x$-intercept**!

[Prof. Park] And what is its slope? Can we write $y = -2$ in slope-intercept form? Yes:
$$y = 0x - 2$$
The slope is $m = 0$! A horizontal line has zero slope. Think of cross-country skiing on a flat meadow near Bozeman: there is zero incline, zero tilt, slope equals zero!""",

    5: """[Prof. Park] Now turn to Example 3F on page 37: Graph the equation $x = 3$ and analyze its intercepts and slope.

[TA Sora] This is the counterpart to Example 3E. Here, the equation is $x = 3$. There is no $y$ in the equation! That means no matter what vertical height $y$ you choose, $x$ is permanently locked at $+3$.
Points on this line include $(3, -2)$, $(3, 0)$, $(3, 4)$, and $(3, 100)$!

[Prof. Park] Plot those points and connect them: you get a perfectly straight **Vertical Line** passing through 3 on the horizontal axis!

[TA Sora] Let us analyze its intercepts:
It crosses the horizontal axis at $(3, 0)$, so its $x$-intercept is $(3, 0)$.
Does it ever touch the vertical $y$-axis? No! It runs perfectly parallel to the $y$-axis, so there is **NO $y$-intercept**!

[Prof. Park] Now, what about its slope? Can you write $x = 3$ in slope-intercept form $y = mx + b$? No! Because there is no $y$ variable to solve for!
If you tried to calculate slope between $(3, 0)$ and $(3, 4)$:
$$m = \\frac{4 - 0}{3 - 3} = \\frac{4}{0}$$
Division by zero is strictly undefined in mathematics! Therefore, the slope of a vertical line is **UNDEFINED**!

[TA Sora] Do not confuse 'zero' with 'undefined!' Zero is a real number; undefined is an impossible division!""",

    6: """[Prof. Park] On Slide 6, we introduce the single most famous, time-tested mnemonic in American algebra education: The HOY VUX Rule!

[TA Sora] HOY VUX! Every student in Gallatin College should write HOY VUX at the top of their scratch paper on Exam 2:
- **H - O - Y:**
  - **H** stands for **Horizontal** line.
  - **O** stands for **0 (Zero)** slope ($m = 0$).
  - **Y** stands for **$y = \\text{number}$** equation!

[Prof. Park] And its partner:
- **V - U - X:**
  - **V** stands for **Vertical** line.
  - **U** stands for **Undefined** slope.
  - **X** stands for **$x = \\text{number}$** equation!

[TA Sora] Here is my favorite outdoor Montana analogy for remembering HOY vs VUX:
Think of skiing at Bridger Bowl. If you are on a flat Nordic cross-country trail, your slope is 0—it takes effort to glide, but you are completely safe ($m = 0$, Horizontal, $y = c$).
Now imagine skiing straight off the vertical cliff of the Bridger Ridge! That is a vertical freefall—your skis have zero traction, division by zero, your survival is completely undefined! ($m = \\text{undefined}$, Vertical, $x = c$).

[Prof. Park] That ski cliff visual will stick with you forever! Whenever you see an equation with only $y$, think HOY: Horizontal, zero slope. Whenever you see an equation with only $x$, think VUX: Vertical, undefined slope.""",

    7: """[Prof. Park] On Slide 7, we place both special lines together on the exact same coordinate plane: the horizontal line $y = -2$ and the vertical line $x = 3$.

[TA Sora] Look at how they intersect! The horizontal line runs west-to-east at height $y = -2$. The vertical line runs south-to-north at position $x = 3$. They cross each other at a single unique point: $(3, -2)$!

[Prof. Park] Notice that they meet at a crisp 90-degree right angle. Every horizontal line is perpendicular to every vertical line on the Cartesian plane!

[TA Sora] And notice how easy it is to find their intersection: the $x$-coordinate must be 3 because $x = 3$, and the $y$-coordinate must be $-2$ because $y = -2$. The intersection point literally writes itself: $(3, -2)$!

[Prof. Park] In Unit 2, when we solve systems of linear equations in Lectures 26 through 30, the intersection of two lines represents the simultaneous solution to the system. For the system $\\{x = 3, y = -2\\}$, the solution is simply the ordered pair $(3, -2)$.

[TA Sora] Compare their slopes one more time: $y = -2$ has slope $0$; $x = 3$ has undefined slope. One is flat, one is a sheer cliff, and together they create a perfect perpendicular crosshair!""",

    8: """[Prof. Park] Slide 8 brings us to the Section 2.1 Mastery Review. Let us consolidate our three graphing strategies so you can choose the optimal tool for any problem on your homework.

[TA Sora] Strategy 1: **The Table Method**.
Best when the equation is already solved for $y$, or when you want to pick specific inputs like $x = -1, 0, 1$. Always use three points to catch any arithmetic slips!

[Prof. Park] Strategy 2: **The Intercept Method (Cover-Up Method)**.
Best when the equation is in Standard Form $Ax + By = C$ and both $A$ and $B$ divide evenly into $C$. Set $y=0$ to find the $x$-intercept; set $x=0$ to find the $y$-intercept. Connect the two intercepts! (Unless the line passes through the origin, in which case pick a third point).

[TA Sora] Strategy 3: **The Slope-Intercept Method**.
Best when the equation is in form $y = mx + b$. Plot the $y$-intercept $(0, b)$ first, then count Rise over Run to find your next points!

[Prof. Park] And never forget **HOY VUX** for lines with only one variable: $y = c$ is horizontal with zero slope; $x = c$ is vertical with undefined slope.

[TA Sora] In Lecture 20, we zoom in on the most fundamental parameter of linear algebra: Section 2.2, The Slope of a Line, Rise over Run, and the Slope Formula! Outstanding work today!"""
}

SCRIPTS_L20 = {
    1: """[Prof. Park] Welcome to Lecture 20 of M090! Today, on pages 38 and 39 of your workbook, we begin Section 2.2: The Slope of a Line and Rates of Change.

[TA Sora] If there is one concept in all of introductory algebra that echoes through physics, engineering, chemistry, economics, and calculus, it is the concept of **Slope**!

[Prof. Park] Geometrically, slope measures two distinct properties of a line: its **steepness** (how steeply it rises or falls) and its **direction** (whether it tilts uphill, downhill, flat, or vertical).

[TA Sora] In English, we define slope as the ratio of the vertical change to the horizontal change:
$$\\text{Slope } m = \\frac{\\text{Vertical Change}}{\\text{Horizontal Change}} = \\frac{\\text{Rise}}{\\text{Run}}$$
And mathematically, if you are given any two points $(x_1, y_1)$ and $(x_2, y_2)$ on a line, the slope formula is:
$$m = \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{\\Delta y}{\\Delta x}$$

[Prof. Park] Notice that Greek letter $\\Delta$ (Delta). In science, $\\Delta$ always symbolizes 'change in.' $\\Delta y$ is the change in vertical elevation, and $\\Delta x$ is the change in horizontal distance.

[TA Sora] Think about real life here in Bozeman: when highway engineers build Interstate 90 over Bozeman Pass, road signs warn truckers of a '6% grade.' That means the road rises or drops 6 vertical feet for every 100 horizontal feet! In roofing, carpenters measure pitch as rise per 12 inches of run. Slope is woven into the physical world all around us!""",

    2: """[Prof. Park] Let us apply the slope formula directly to Example 1A on page 38: Find the slope of the line passing through $(2, 3)$ and $(5, 7)$.

[TA Sora] Step 1: Label your coordinates clearly to avoid mixing them up!
Let $(x_1, y_1) = (2, 3)$ and $(x_2, y_2) = (5, 7)$.
Write down the formula before plugging in numbers:
$$m = \\frac{y_2 - y_1}{x_2 - x_1}$$

[Prof. Park] Now substitute our values carefully:
$$m = \\frac{7 - 3}{5 - 2}$$
In the numerator, $7 - 3 = 4$. That is our Rise!
In the denominator, $5 - 2 = 3$. That is our Run!
Therefore, our slope is:
$$m = \\frac{4}{3}$$

[TA Sora] What if a student swapped the order and labeled $(5, 7)$ as point 1 and $(2, 3)$ as point 2? Let us calculate:
$$m = \\frac{3 - 7}{2 - 5} = \\frac{-4}{-3} = +\\frac{4}{3}!$$
You get the exact same answer! It does not matter which point you call Point 1 and which you call Point 2, as long as you subtract in the SAME order in both the numerator and the denominator!

[Prof. Park] That is a crucial insight. The fatal error is subtracting $y$ in one direction and $x$ in the opposite direction. Always stay consistent! Since $m = +4/3 > 0$, the line rises from left to right.""",

    3: """[Prof. Park] Now let us tackle Example 1B on page 38: Find the slope of the line passing through $(3, -4)$ and $(-2, -8)$.

[TA Sora] Look at all those negative signs! This is where TA Sora's Protective Parentheses Rule becomes your best friend. Whenever you subtract a negative number, wrap it in parentheses so you do not drop a sign!

[Prof. Park] Let $(x_1, y_1) = (3, -4)$ and $(x_2, y_2) = (-2, -8)$.
Substitute into the formula with protective parentheses:
$$m = \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{-8 - (-4)}{-2 - 3}$$

[TA Sora] Now simplify step by step:
In the numerator: $-8 - (-4)$ becomes $-8 + 4 = -4$!
In the denominator: $-2 - 3$ becomes $-5$!
So we have:
$$m = \\frac{-4}{-5}$$
And what is a negative divided by a negative, Professor?

[Prof. Park] A negative divided by a negative is always a positive!
$$m = \\frac{4}{5}$$

[TA Sora] Exactly! Many students accidentally leave the answer as $\\frac{-4}{-5}$ or make a sign mistake and get $-\\frac{4}{5}$. By using protective parentheses, $-8 - (-4)$ clearly became $-8 + 4 = -4$, and the two negatives cancel out to give a positive slope $m = +4/5$. The line rises gently from left to right!""",

    4: """[Prof. Park] Look at Example 1C on page 38: Find the slope of the line passing through $(3, 7)$ and $(3, -10)$. Look very closely at those two points before writing anything down. What do you notice, Sora?

[TA Sora] Both points have the exact same $x$-coordinate: $x_1 = 3$ and $x_2 = 3$! If both points share the same horizontal coordinate, they must sit vertically above and below each other on the grid!

[Prof. Park] Let us run the formula and see what happens algebraically:
$$m = \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{-10 - 7}{3 - 3}$$
In the numerator: $-10 - 7 = -17$.
In the denominator: $3 - 3 = 0$!
$$m = \\frac{-17}{0}$$

[TA Sora] Red alert! We have a zero in the denominator! In mathematics, dividing any number by zero is strictly impossible and undefined!

[Prof. Park] Therefore, the slope of this line is **UNDEFINED**. It does not exist as a real number. 

[TA Sora] And remember our HOY VUX rule from Lecture 19:
V - U - X!
Vertical line, Undefined slope, equation $x = 3$!
Whenever the $x$-coordinates are identical, the denominator is zero, the slope is undefined, and the line is a vertical cliff!""",

    5: """[Prof. Park] Now examine Example 1D on page 38: Find the slope of the line passing through $(-2, -5)$ and $(3, -5)$. What do you notice about these two points?

[TA Sora] Now the $y$-coordinates are identical: $y_1 = -5$ and $y_2 = -5$! Both points share the exact same vertical elevation!

[Prof. Park] Let us apply the slope formula:
$$m = \\frac{-5 - (-5)}{3 - (-2)}$$
In the numerator: $-5 - (-5) = -5 + 5 = 0$!
In the denominator: $3 - (-2) = 3 + 2 = 5$.
$$m = \\frac{0}{5} = 0$$

[TA Sora] Notice the enormous difference between Example 1C and Example 1D:
In Example 1C, the zero was in the denominator ($\frac{-17}{0}$), which is **Undefined**!
Here in Example 1D, the zero is in the numerator ($\frac{0}{5}$), which is perfectly valid and equals **Zero** ($0$)!

[Prof. Park] Think about sharing: If you have zero cookies to divide among five students, each student receives zero cookies! That is a perfectly legitimate real number. 

[TA Sora] And recall HOY:
H - O - Y!
Horizontal line, Zero ($0$) slope, equation $y = -5$!
A flat horizontal line has a slope of zero. Do not mix up zero slope with undefined slope!""",

    6: """[Prof. Park] Turn to Example 1E on page 38: Fraction Coordinates! Find the slope of the line passing through $\\left(\\frac{1}{2}, \\frac{1}{3}\\right)$ and $\\left(\\frac{3}{4}, \\frac{7}{5}\\right)$.

[TA Sora] When students see fraction coordinates, their hearts often beat a little faster! But don't panic—this is simply Unit 1 fraction arithmetic combined with our slope formula. Take it one piece at a time!

[Prof. Park] Let us compute the numerator ($\\Delta y$) first:
$$\\Delta y = y_2 - y_1 = \\frac{7}{5} - \\frac{1}{3}$$
Find the least common denominator between 5 and 3, which is 15:
$$\\frac{7 \\times 3}{15} - \\frac{1 \\times 5}{15} = \\frac{21}{15} - \\frac{5}{15} = \\frac{16}{15}$$

[TA Sora] Now compute the denominator ($\\Delta x$):
$$\\Delta x = x_2 - x_1 = \\frac{3}{4} - \\frac{1}{2}$$
The common denominator between 4 and 2 is 4:
$$\\frac{3}{4} - \\frac{2}{4} = \\frac{1}{4}$$

[Prof. Park] Now assemble the complex fraction:
$$m = \\frac{\\Delta y}{\\Delta x} = \\frac{\\frac{16}{15}}{\\frac{1}{4}}$$
How do we divide two fractions, Sora?

[TA Sora] Multiply by the reciprocal of the denominator! 'Keep, Change, Flip!'
$$m = \\frac{16}{15} \\times \\frac{4}{1} = \\frac{64}{15}$$
Can 64 and 15 be simplified? 64 has factors of 2; 15 has factors of 3 and 5. There are no common factors, so our final slope is $\\frac{64}{15}$! Beautiful, patient pencil work!""",

    7: """[Prof. Park] Moving to page 39, Example 2A: Finding the slope directly by counting Rise over Run from a given graph!

[TA Sora] Sometimes on an exam, you are not given coordinates in a sentence; you are simply handed a graph with a line drawn on a grid. To find the slope visually:
Step 1: Identify two clean grid intersections—points where the line crosses grid lines exactly at integer coordinates.
Looking at Example 2A, the line crosses cleanly at Point 1: $(0, 1)$ and Point 2: $(3, 3)$!

[Prof. Park] Step 2: Draw a right triangle between those two points, called a 'slope triangle.'
Start at $(0, 1)$ and travel vertically to match the height of Point 2:
You climb upward from $y = 1$ to $y = 3$. That is a **Rise** of $+2$ units!

[TA Sora] Step 3: Now travel horizontally to reach Point 2:
You run to the right from $x = 0$ to $x = 3$. That is a **Run** of $+3$ units!

[Prof. Park] Step 4: Write the ratio of Rise over Run:
$$m = \\frac{\\text{Rise}}{\\text{Run}} = \\frac{+2}{+3} = \\frac{2}{3}$$

[TA Sora] And do a quick common-sense reality check: Does the line slant uphill from left to right? Yes, it rises like a gentle hiking trail up Peets Hill in Bozeman. Uphill lines must have positive slopes, so $+2/3$ makes total visual sense!""",

    8: """[Prof. Park] Now let us inspect Example 2B on page 39: Finding a negative slope from a graph.

[TA Sora] Let us locate two clean grid intersections on this line:
Point 1 is the $y$-intercept at $(0, 4)$.
Point 2 is the $x$-intercept at $(2, 0)$.

[Prof. Park] Let us construct our slope triangle starting from $(0, 4)$ and moving to $(2, 0)$:
First, look at the vertical movement: to go from height 4 down to height 0, you must travel DOWNWARD 4 units!
Because you are moving down, the **Rise** is negative four: $\\text{Rise} = -4$!

[TA Sora] Next, look at the horizontal movement: from $x = 0$ to $x = 2$, you move to the right 2 units.
The **Run** is positive two: $\\text{Run} = +2$.

[Prof. Park] Now compute the slope ratio:
$$m = \\frac{\\text{Rise}}{\\text{Run}} = \\frac{-4}{+2} = -2$$

[TA Sora] Notice the sign! The line slants downward from left to right—like skiing down the slopes at Bridger Bowl. Downhill lines always have **negative** slopes!
If you ever count a slope and get a positive number for a downhill line, you forgot the minus sign on the downward rise. Always check the overall direction!""",

    9: """[Prof. Park] On Slide 9, we conclude Section 2.2 Part 1 with the Four Universal Types of Slope on the Coordinate Plane. Every line in the universe falls into one of these four categories.

[TA Sora] Let us summarize them with full visual intuition:
1. **Positive Slope ($m > 0$):** Slants uphill from left to right. As $x$ increases, $y$ increases. Like climbing a mountain ridge.
2. **Negative Slope ($m < 0$):** Slants downhill from left to right. As $x$ increases, $y$ decreases. Like descending into Gallatin Canyon.

[Prof. Park] And the two special extremes:
3. **Zero Slope ($m = 0$):** Perfectly flat horizontal line ($y = c$). Rise is zero, so $0 / \\text{Run} = 0$. Like a calm lake or flat prairie.
4. **Undefined Slope ($m = \\text{undefined}$):** Perfectly vertical line ($x = c$). Run is zero, and division by zero is undefined! Like a vertical cliff face.

[TA Sora] Remember the ski analogies, remember HOY VUX, and remember protective parentheses when subtracting negative coordinates!

[Prof. Park] In Lecture 21, we continue Section 2.2 with Parallel and Perpendicular Lines, comparing their slopes and proving their geometric relationships. Outstanding focus today, everyone!"""
}
