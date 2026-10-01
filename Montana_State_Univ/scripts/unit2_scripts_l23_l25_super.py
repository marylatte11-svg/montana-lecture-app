# -*- coding: utf-8 -*-
"""
unit2_scripts_l23_l25_super.py
Ultra-rich, high-density 20-25 minute broadcast scripts for Lectures 23, 24, and 25.
Target: 2,400 - 2,800 words per lecture (~300-360 words per slide across 8 slides).
Packed with Montana real-world examples: PLSS surveying, irrigation canals, solar angles, geysers, LiDAR drones.
"""

SCRIPTS_L23_SUPER = {
    1: r"""[Prof. Park] Welcome to Lecture 23 of M090! Today on pages 42 through 44 of your workbook, we reach the grand synthesis of Section 2.3: Writing equations of lines that pass through specific points and are Parallel or Perpendicular to existing lines, followed by comprehensive in-class practice problems.

[TA Sora] In construction, surveying, and civil engineering across Montana, this is the daily bread and butter of technical work! If you are laying out a new subdivision in Bozeman or designing an agricultural access road parallel to an existing canal, you cannot simply eyeball the angle. You must compute the exact slope and anchor it to a known survey monument!

[Prof. Park] Let us begin on page 42 with Example 6: Find the equation of the line containing the point $(-1, 3)$ and **parallel** to the line $y = 4x - 5$. Write the final answer in slope-intercept form. Let us break this problem down like an investigator piecing together clues:
Clue 1: Our target line must pass through the specific survey point $(x_1, y_1) = (-1, 3)$.
Clue 2: Our target line must be **parallel** to the given reference line $y = 4x - 5$.

[TA Sora] What does 'parallel' tell us about the slope? Parallel lines have the **identical slope**!
Look at the reference line: $y = 4x - 5$. Its slope is $m = 4$.
Because our new line is parallel, it must inherit that exact same steepness:
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
It satisfies every condition with total mathematical perfection! Think of a civil engineer adding a parallel passing lane to Highway 191 in Gallatin Canyon—it shares the exact road curvature (slope 4), but has an offset boundary passing through a specific landmark point!""",

    2: r"""[Prof. Park] Now turn to Example 7 on page 42: Find the equation of the line containing the point $(2, -3)$ and **perpendicular** to the line $y = -\frac{1}{3}x + 2$.

[TA Sora] Notice that crucial word: **PERPENDICULAR**!
In Montana roofing and solar energy, perpendicularity is vital. When technicians install solar panel arrays on residential roofs in Bozeman, the mounting rails must be bolted at a precise 90-degree angle to the roof rafters. If the mounting rails are skewed even two degrees, the winter snow load won't shed evenly, creating uneven structural stress that can crack the mounts!

[Prof. Park] Let us extract our slope using TA Sora's Two-Flip Rule:
The reference line is $y = -\frac{1}{3}x + 2$, so its slope is $m_{\text{ref}} = -\frac{1}{3}$.
To find our perpendicular slope $m_{\perp}$, we perform our two flips:
Flip 1 (the fraction): Invert $\frac{1}{3} \implies \frac{3}{1} = 3$.
Flip 2 (the sign): Invert negative to positive $\implies +3$!
Therefore, our perpendicular slope is:
$$m_{\perp} = 3$$

[TA Sora] Now we assemble our pieces:
Slope: $m = 3$.
Target point: $(x_1, y_1) = (2, -3)$.
Substitute into Point-Slope Form:
$$y - y_1 = m(x - x_1)$$
$$y - (-3) = 3(x - 2)$$
On the left side, $y - (-3)$ becomes $y + 3$:
$$y + 3 = 3(x - 2)$$

[Prof. Park] Distribute the 3 on the right side:
$$y + 3 = 3x - 6$$
Subtract 3 from both sides to isolate $y$:
$$y = 3x - 6 - 3 \implies y = 3x - 9$$

[TA Sora] Let us verify our answer:
1. Is the slope perpendicular? $3 \cdot \left(-\frac{1}{3}\right) = -1$. Yes!
2. Does it pass through $(2, -3)$? Plug in $x = 2$: $y = 3(2) - 9 = 6 - 9 = -3$!
Both checks pass cleanly! $y = 3x - 9$ is our exact, verified perpendicular line!""",

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
You get the exact same answer! But recognizing the $y$-intercept $(0, b)$ instantly saves you valuable exam time.

[Prof. Park] In real-world terms, think of an agricultural water reservoir on a ranch near Belgrade: it starts at an initial water level of 5 feet on July 1st ($b = 5$), and decreases by $\frac{3}{5}$ of a foot per week during peak summer alfalfa irrigation ($m = -3/5$). The linear model $y = -\frac{3}{5}x + 5$ predicts exactly when the rancher will need to switch to groundwater pumps before the reservoir runs dry! Mathematical modeling turns numbers into practical wisdom.""",

    4: r"""[Prof. Park] Now examine In-Class Practice Problem #2 on page 43: Find the equation of the line with an $x$-intercept of $(5, 0)$ and a slope of $\frac{3}{5}$.

[TA Sora] Compare Problem #2 side by side with Problem #1 from Slide 3!
In Problem #1, we had a $y$-intercept of $(0, 5)$.
Here in Problem #2, we have an **$x$-intercept** of $(5, 0)$!
Remember the fatal trap: You CANNOT plug an $x$-intercept into the $b$ slot of $y = mx + b$! $b$ is strictly the $y$-intercept!
If you write $y = \frac{3}{5}x + 5$, you have drawn a line that is shifted ten vertical units away from the correct location!

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

[Prof. Park] Look at that: the true $y$-intercept is $(0, -3)$! If a student had mistakenly written $y = \frac{3}{5}x + 5$, their line would have had a positive intercept at $+5$ instead of a negative intercept at $-3$. Always distinguish between $(0, 5)$ and $(5, 0)$! One sits on the vertical spine; the other sits on the horizontal floor. In surveying, confusing north-south coordinates with east-west coordinates puts you on the wrong parcel of land!""",

    5: r"""[Prof. Park] Turn to In-Class Practice Problem #3 on page 43: Find the equation of the line containing the points $(-2, -3)$ and $(6, 1)$.

[TA Sora] This is the classic two-point challenge!
Imagine a Montana backcountry trail connecting two backcountry shelters in the Absaroka-Beartooth Wilderness: Shelter A at coordinates $(-2, -3)$ and Shelter B at coordinates $(6, 1)$. We need to establish the linear trail connecting them.
Step 1: Find the slope $m$ between the two shelters using the slope formula:
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
It works with 100% precision! The trail climbs at a gentle grade of 1 vertical foot for every 2 horizontal feet, crossing the vertical axis at base elevation $-2$!""",

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

[TA Sora] Look at how effortless these problems become when you train your eyes to scan for identical coordinates before touching any algebra! Problem #4 is $x = 4$; Problem #5 is $y = 6$! 

[Prof. Park] In the American Public Land Survey System (PLSS) that divided all of Montana into 6-mile-square townships and 1-mile-square sections, boundary lines run strictly along meridians (vertical lines $x = k$) and parallels of latitude (horizontal lines $y = c$). Every fence line in Gallatin County follows these exact special equations!""",

    7: r"""[Prof. Park] In-Class Practice Problem #6 on page 44: Find the equation of the line containing $(2, 1)$ and **parallel** to $3x - y = 7$.

[TA Sora] Step 1: Find the slope of the reference line by solving for $y$:
$$3x - y = 7$$
Subtract $3x$:
$$-y = -3x + 7$$
Divide every single term by $-1$:
$$y = 3x - 7$$
The slope of the reference line is $m = 3$.

[Prof. Park] Step 2: Since our target line is **parallel**, it must inherit the exact same slope:
$$m = 3$$
Step 3: Now use Point-Slope Form with point $(2, 1)$:
$$y - 1 = 3(x - 2)$$
Distribute the 3:
$$y - 1 = 3x - 6$$
Add 1 to both sides:
$$y = 3x - 5$$

[TA Sora] Verify: Slope is 3 (parallel to $3x - y = 7$), and when $x = 2$, $y = 3(2) - 5 = 1$, matching point $(2, 1)$! Clean, precise, and fast!

[Prof. Park] Notice how systematic this workflow is. In surveying, if you are establishing a new irrigation ditch parallel to a ranch property line $3x - y = 7$ through headgate $(2, 1)$, $y = 3x - 5$ gives the exact ditch path that guarantees equal spacing along the entire pasture!""",

    8: r"""[Prof. Park] In-Class Practice Problem #7 on page 44: Find the equation of the line containing $(6, 3)$ and **perpendicular** to $2y - x = 20$.

[TA Sora] Step 1: Solve the reference line for $y$:
$$2y - x = 20$$
Add $x$ to both sides:
$$2y = x + 20$$
Divide every term by 2:
$$y = \frac{1}{2}x + 10$$
The reference slope is $m_{\text{ref}} = \frac{1}{2}$.

[Prof. Park] Step 2: Because our line is **perpendicular**, we find the negative reciprocal using our Two-Flip Rule:
Flip $\frac{1}{2} \implies 2$.
Flip the sign from positive to negative $\implies -2$.
So our perpendicular slope is:
$$m_{\perp} = -2$$

[TA Sora] Step 3: Use Point-Slope Form with point $(6, 3)$:
$$y - 3 = -2(x - 6)$$
Distribute $-2$:
$$y - 3 = -2x + 12$$
Add 3 to both sides:
$$y = -2x + 15$$

[Prof. Park] Outstanding! Verify: $(-2) \cdot (1/2) = -1$ (perpendicular!). At $x = 6$, $y = -2(6) + 15 = -12 + 15 = 3$, passing right through $(6, 3)$!

[TA Sora] In mountain road construction across the Rockies, water drainage culverts are installed perpendicular to the road to divert torrential spring snowmelt off the embankment. If the road climbs at slope $\frac{1}{2}$, the culverts drop across at slope $-2$!

[Prof. Park] You have completely mastered Section 2.3! In Lecture 24, we enter Section 2.4: Relations, Domain, Range, and the foundation of Functions! See you there!"""
}

SCRIPTS_L24_SUPER = {
    1: r"""[Prof. Park] Welcome to Lecture 24 of M090! Today on page 45 of your workbook, we step into one of the most foundational concepts in all of modern science, data analytics, and calculus: Section 2.4, Relations, Domain, and Range.

[TA Sora] In everyday conversation, the word 'relation' describes how two entities connect—like parents and children, rainfall and wheat yield on a Montana dryland farm, or the temperature in Bozeman and the thickness of ice on Hyalite Reservoir. In mathematics, a **relation** has a very precise, universal definition:
A relation is simply **any set of ordered pairs** $(x, y)$!

[Prof. Park] It can be a finite list of five data points collected in a chemistry lab, or an infinite line stretching across the universe. Every ordered pair connects an **input** to an **output**.
That gives us two essential definitions that will follow you through every higher-level math and science course you will ever take:
1. The **Domain** is the set of all first coordinates—all allowable input values ($x$-values).
2. The **Range** is the set of all second coordinates—all resulting output values ($y$-values).

[TA Sora] Think of wildlife biologists tracking Yellowstone bison herds: your input $x$ is the year or month (Domain), and your output $y$ is the estimated herd population size (Range). Or think of Gallatin River streamflow monitoring gauges maintained by the US Geological Survey: input $x$ is the day in June, and output $y$ is the water discharge rate in cubic feet per second (cfs)!

[Prof. Park] In this lecture, we master how to extract and report domain and range in two very different mathematical environments:
First, for **discrete relations**—scattered, isolated data points where we list individual numbers inside curly roster braces $\{ \}$.
Second, for **continuous graphs**—smooth unbroken curves where we report continuous coverage using interval notation with brackets $[a, b]$!

[TA Sora] Let us dive straight into Example 1 on page 45 and master discrete relations first!""",

    2: r"""[Prof. Park] Example 1 on page 45: For the following relation, determine the domain and the range:
$$\{(1, -1), (2, 0), (3, 1), (4, 2), (1, 3)\}$$

[TA Sora] Let us examine the inputs first to find the **Domain**.
Look at the first number in each ordered pair from left to right:
From the first pair $(1, -1)$, our input is $1$.
From the second pair $(2, 0)$, our input is $2$.
From the third pair $(3, 1)$, our input is $3$.
From the fourth pair $(4, 2)$, our input is $4$.
From the fifth pair $(1, 3)$, our input is $1$ again!

[Prof. Park] Now pause right here! Notice that the input $1$ appears twice in our list of pairs. How do we write that in our final answer, Sora?

[TA Sora] This is the golden rule of set theory: **Never repeat elements inside a set!**
A set is simply a collection of unique items. Even if the number 1 appears five hundred times in your raw data log, you only write it once in the domain list:
$$\text{Domain} = \{1, 2, 3, 4\}$$
Notice that we wrap our list in curly roster braces $\{ \}$, and we always list the numbers in ascending numerical order from smallest to largest!

[Prof. Park] Now let us examine the outputs to find the **Range**.
Look at the second coordinate in each ordered pair:
From $(1, -1)$, we get $-1$.
From $(2, 0)$, we get $0$.
From $(3, 1)$, we get $1$.
From $(4, 2)$, we get $2$.
From $(1, 3)$, we get $3$.

[TA Sora] Are there any duplicates in this output list? No, all five numbers are distinct!
Let us list them in ascending order from lowest to highest:
$$\text{Range} = \{-1, 0, 1, 2, 3\}$$

[Prof. Park] Beautifully organized. Remember: Discrete data points use curly roster braces $\{ \}$, list elements in order, and never repeat duplicate numbers! In database management, this is like creating a unique primary key index: duplicate keys are merged into a single entry.""",

    3: r"""[Prof. Park] On Slide 3, we take those five ordered pairs from Example 1 and plot them onto the Cartesian coordinate plane: $(1, -1)$, $(2, 0)$, $(3, 1)$, $(4, 2)$, and $(1, 3)$.

[TA Sora] Look at how these five dots arrange themselves across the grid!
Point $(2, 0)$ rests right on the positive $x$-axis.
Points $(3, 1)$ and $(4, 2)$ sit comfortably in Quadrant I.
Point $(1, -1)$ sits in Quadrant IV.
And Point $(1, 3)$ sits high up in Quadrant I.

[Prof. Park] Now, students, look very carefully at the two points $(1, -1)$ and $(1, 3)$. What geometric feature do you observe?

[TA Sora] They are stacked directly on top of each other! They share the exact same horizontal coordinate $x = 1$. If you hold a vertical straightedge or ruler along the grid line $x = 1$, your ruler touches BOTH points at the exact same moment!

[Prof. Park] That visual observation is momentous! In Lecture 25, that exact vertical alignment is what will cause this relation to fail the famous Vertical Line Test.

[TA Sora] In a discrete relation, notice that you have empty white space between the points—there are no connecting lines, no fractions between them, just isolated islands. That is why the domain and range are lists of discrete numbers inside curly braces $\{ \}$, NOT continuous intervals with brackets! You cannot say $[1, 4]$ because numbers like $1.5$ and $2.7$ are not in this relation! Discrete means countable individual points!""",

    4: r"""[Prof. Park] Slide 4 introduces one of the most intuitive visual tools in all of mathematics: The Mapping Diagram.

[TA Sora] A mapping diagram translates abstract ordered pairs into a clear visual flow of cause and effect!
On the left, we draw an oval representing the **Domain** (Inputs): $\{1, 2, 3, 4\}$.
On the right, we draw an oval representing the **Range** (Outputs): $\{-1, 0, 1, 2, 3\}$.

[Prof. Park] Then, for each ordered pair $(x, y)$, we draw a directional arrow starting from the input in the left oval and pointing directly to its corresponding output in the right oval.
Look at the arrows:
An arrow goes from $2$ to $0$.
An arrow goes from $3$ to $1$.
An arrow goes from $4$ to $2$.

[TA Sora] But now look at the input $1$ in the left oval!
Two separate arrows originate from the number $1$:
One arrow shoots down to $-1$, and another arrow shoots up to $3$!

[Prof. Park] That branching arrow is the visual smoking gun of a non-functional relation!
If you think of the left oval as telephone speed-dial buttons and the right oval as recipients, pressing button 1 tries to call two different people at the exact same moment. In electronics and software, a single input triggering two contradictory commands causes a system crash!

[TA Sora] Mapping diagrams make it immediately obvious whether an input is branching out to multiple outputs. In data science, when you clean raw data logs from weather sensors or GPS trackers, duplicate input timestamps with conflicting readings are the first errors you must filter out! Keep that branching picture in mind as we move forward!""",

    5: r"""[Prof. Park] Turn to page 45 for Example 2 Graph A: Determining the Domain and Range of a Continuous Line Segment.

[TA Sora] Here the graph is not a collection of isolated dots; it is a solid, unbroken straight line segment stretching from $(-4, -2)$ to $(3, 5)$ with solid dots at both ends!

[Prof. Park] Because there are infinitely many points packed along that segment, we cannot list every number in curly braces. We must report the domain and range as continuous intervals!
Let us find the **Domain** first. Sora, how do we find the domain from a graph?

[TA Sora] Imagine shining a spotlight from the top and bottom of the graph to cast a shadow onto the horizontal $x$-axis!
Look at the leftmost edge: The segment starts at $x = -4$.
Look at the rightmost edge: The segment ends at $x = 3$.
Because both endpoints have solid closed circles, $-4$ and $3$ are included!
Therefore, the Domain is:
$$\text{Domain} = [-4, 3]$$

[Prof. Park] Exactly. From left to right: $[-4, 3]$.
Now let us find the **Range**. How do we find the range from a graph?

[TA Sora] Now imagine shining a spotlight from the left and right to cast a shadow onto the vertical $y$-axis!
Look at the lowest point on the graph: The bottom endpoint is at height $y = -2$.
Look at the highest point on the graph: The top endpoint reaches height $y = 5$.
Both heights are solid and included!
Therefore, the Range is:
$$\text{Range} = [-2, 5]$$

[Prof. Park] Always remember: Domain is horizontal coverage (Left to Right). Range is vertical coverage (Bottom to Top)! Always write the smaller number first: $[\text{min}, \text{max}]$! Think of hiking elevation in Montana: you always state your elevation from basecamp minimum to summit maximum!""",

    6: r"""[Prof. Park] Now examine Example 2 Graph B on page 45: A Bounded Curve.

[TA Sora] This is a curved wave that extends horizontally from $x = -3$ to $x = 5$. Notice the endpoints: at $x = -3$, there is a solid dot at height 0. At $x = 5$, there is a solid dot at height 2. And between them, the curve plunges down to a deep valley at $(1, -4)$ and rises to a peak at $(3, 4)$!

[Prof. Park] Let us find the **Domain** first:
How far left does the curve travel? Leftmost point is at $x = -3$.
How far right does the curve travel? Rightmost point is at $x = 5$.
Both boundaries are solid and included:
$$\text{Domain} = [-3, 5]$$

[TA Sora] Now comes the most critical trap in Section 2.4! When finding the **Range**, many students look only at the two endpoints and say: 'The endpoints are at heights 0 and 2, so the range is $[0, 2]$!'
Why is that a massive error, Professor?

[Prof. Park] Because the curve dips far below 0 and climbs far above 2! The range must capture the ENTIRE vertical extent of the graph—from its absolute lowest valley to its absolute highest peak!

[TA Sora] Look at the valley: the lowest point on the entire curve touches the horizontal grid line at $y = -4$!
Look at the peak: the highest crest reaches up to $y = +4$!
The graph touches every single height between $-4$ and $+4$.
Therefore, the Range is:
$$\text{Range} = [-4, 4]$$

[Prof. Park] That is a vital distinction. Never just grab the endpoints! Always scan from the very bottom of the canvas to the very top: lowest $y$ to highest $y$! In Montana weather forecasting, you report the daily temperature range from the overnight low ($-4^\circ\text{F}$) to the afternoon high ($+4^\circ\text{F}$), not where the thermometer sat at 8:00 AM! Always look for peaks and valleys!""",

    7: r"""[Prof. Park] On Slide 7, we compare the two fundamental notation languages used in algebra: Roster Notation for Discrete Sets versus Interval Notation for Continuous Graphs.

[TA Sora] Let us make sure every student knows when to use which notation:
1. **Discrete Relations (Individual Dots):**
Use **Curly Braces** $\{ \}$. Inside, list each individual number separated by commas:
$$\{1, 2, 3, 4\}$$
This means ONLY the integers 1, 2, 3, and 4. It does NOT include $1.5$, $2.7$, or $\pi$!

[Prof. Park] 2. **Continuous Graphs (Unbroken Lines & Curves):**
Use **Interval Notation** with brackets and parentheses:
$$[-4, 3]$$
This means EVERY SINGLE real number between $-4$ and $3$, including $-3.99$, $0$, $1.414$, and $2.999$!

[TA Sora] And remember our bracket rules from Unit 1:
- **Square Bracket $[$ or $]$:** The endpoint is **included** (solid dot on the graph, $\le$ or $\ge$).
- **Round Parenthesis $($ or $)$:** The endpoint is **excluded** (open circle on the graph, $<$ or $>$, or $\pm\infty$).

[Prof. Park] And in Set-Builder notation, that same interval is written as:
$$\{x \mid -4 \le x \le 3\}$$
Which reads: 'The set of all $x$ such that $x$ is between $-4$ and $3$, inclusive.' Both notations describe the exact same geometric reality! Knowing both notations gives you the bilingual fluency needed for engineering, computer programming, and higher-level calculus!""",

    8: r"""[Prof. Park] Slide 8 brings us to the Section 2.4 Part 1 Mastery Checklist. Let us review the golden rules before we step into the definition of a function.

[TA Sora] Rule 1: A relation is any set of ordered pairs $(x, y)$.
Rule 2: The Domain is the set of all inputs ($x$-coordinates).
Rule 3: The Range is the set of all outputs ($y$-coordinates).

[Prof. Park] Rule 4: For discrete sets, list unique elements inside curly braces without repeating duplicates.
Rule 5: For continuous graphs, scan Left-to-Right for Domain, and Bottom-to-Top for Range.

[TA Sora] Rule 6: Solid dots mean square brackets $[ ]$; open circles mean round parentheses $( )$.
Rule 7: Never assume the endpoints are the maximum or minimum of the range! Always check the highest peaks and lowest valleys of the curve.

[Prof. Park] In Lecture 25, we take this exact foundation and answer the ultimate question: Which relations earn the prestigious title of being a **Function**? See you in Lecture 25!"""
}

SCRIPTS_L25_SUPER = {
    1: r"""[Prof. Park] Welcome to Lecture 25 of M090! Today on page 46 of your workbook, we arrive at the crown jewel of introductory algebra: The Formal Definition of a Function and the Vertical Line Test.

[TA Sora] In Lecture 24, we saw that *any* collection of ordered pairs is a relation. But mathematics, modern technology, and science demand predictability! If you build an airplane, design a bridge across the Yellowstone River, launch a weather satellite, or write computer software, you need systems that produce predictable, reliable, reproducible results. That special, elite class of relations is called a **Function**!

[Prof. Park] Let us read the formal mathematical definition on page 46 together:
A **Function** is a relation that assigns to **each input value ($x$) exactly ONE output value ($y$)**!
Read that phrase again: *Each input has exactly ONE output!*

[TA Sora] Here is my favorite everyday analogy: A vending machine in the Gallatin College student lounge!
You walk up to the machine, insert your dollar, and press button B2. You expect a bag of barbecue chips to drop into the tray. If every time you press B2 you get barbecue chips, the machine is functioning properly—it is a **function**!
Now imagine you press B2, and today you get chips, but tomorrow you press B2 and it spits out a bottle of water, and the next day it spits out a granola bar! The machine is unpredictable—it is broken—it is **NOT a function**!

[Prof. Park] An input can never be undecided about its output. One input cannot produce two different answers.
Now, can two different buttons give the same snack? Suppose button B2 gives chips, and button B3 also gives chips. Is that allowed?

[TA Sora] Yes! That is completely allowed! Two different inputs can produce the same output—like two different hiking trails leading to the same summit on Mount Blackmore. But one single trail cannot take you to two different mountain summits at the exact same moment! Input must uniquely determine output! In computer science, this is deterministic execution: identical inputs always yield identical outputs!""",

    2: r"""[Prof. Park] Let us apply that vending machine test directly to Example 3 on page 46: Based off the definition of a function, determine if Example 1 from page 45 is a function.

[TA Sora] Let us recall the ordered pairs from Example 1:
$$\{(1, -1), (2, 0), (3, 1), (4, 2), (1, 3)\}$$
Let us inspect each input value one by one:
Input $2$ produces output $0$ (one output, fine).
Input $3$ produces output $1$ (one output, fine).
Input $4$ produces output $2$ (one output, fine).

[Prof. Park] But now look at input $1$!
In the first pair, input $1$ produces output $-1$.
In the fifth pair, input $1$ produces output $3$!
Input $1$ is assigned to TWO DIFFERENT outputs: $-1$ and $3$!

[TA Sora] It pressed button 1, and got two different snacks!
Because the input $x = 1$ is paired with more than one output, this relation **FAILS** the definition of a function!
Therefore:
$$\mathbf{\text{This relation is NOT a function!}}$$

[Prof. Park] Exactly right. Whenever you see a repeated $x$-coordinate paired with different $y$-coordinates in a set of ordered pairs, you can declare immediately: NOT a function!

[TA Sora] But remember: repeated $y$-coordinates are fine! If we had $(1, 2)$ and $(3, 2)$, both inputs lead to 2, which IS a function. It is repeated $x$-values with different $y$-values that break the rule! One input, one output! In pharmacy and medicine, a single dose of medication cannot have two contradictory effects in the same patient at the exact same moment—medical dosing must be a true function!""",

    3: r"""[Prof. Park] On Slide 3, we translate that algebraic definition of a function into a visual, geometric tool: The Vertical Line Test, universally known as the **VLT**!

[TA Sora] The Vertical Line Test is one of the most elegant concepts in all of mathematics:
**The Vertical Line Test:**
A set of points in a rectangular coordinate system is the graph of a function if and only if **NO vertical line intersects the graph at more than one point**!

[Prof. Park] Why does this test work so flawlessly?
Think about what a vertical line is: An equation of the form $x = c$. Every point on that vertical line shares the exact same $x$-coordinate!
If a vertical line slices through a graph at two or more points, say $(c, y_1)$ and $(c, y_2)$, that means the single input $x = c$ is paired with two different outputs $y_1$ and $y_2$!

[TA Sora] That is the vending machine breaking down right before your eyes!
If your vertical ruler hits the graph at two or more points anywhere on the entire page, the graph fails the test and is NOT a function!
If every vertical line you could ever draw intersects the graph at most once, then every input has at most one output, and the graph **IS a function**!

[Prof. Park] Think of radar or sonar scanning across Hebgen Lake or the Bridger Mountains: As the vertical beam sweeps across the terrain from left to right, if it detects the ground elevation at only one height per horizontal coordinate, it creates a clean elevation map! But if there is an overhanging cliff or cave, the beam hits the top of the cliff and the floor below, signaling that elevation is not a single-valued function of position! Let us test four diverse graphs in Example 4 on the following slides!""",

    4: r"""[Prof. Park] Example 4A on page 46: Determine if the parabola $y = x^2 - 2$ represents a function.

[TA Sora] Look at the graph on your screen: it is a smooth, U-shaped parabola opening upward, with its lowest vertex point sitting at $(0, -2)$ on the vertical axis.

[Prof. Park] Now let us perform the Vertical Line Test. Imagine sliding a vertical straightedge across the screen from left to right:
At $x = -2$, the vertical line hits the curve at $(-2, 2)$—exactly one point!
At $x = -1$, the vertical line hits at $(-1, -1)$—exactly one point!
At $x = 0$, the vertical line hits at $(0, -2)$—exactly one point!
At $x = 2$, the vertical line hits at $(2, 2)$—exactly one point!

[TA Sora] No matter where you place a vertical line across the entire domain from $-\infty$ to $+\infty$, it intersects the parabola at **exactly one single point**!
It never doubles back on itself.
Therefore:
$$\mathbf{\text{Passes VLT } \implies \text{The parabola is a FUNCTION!}}$$

[Prof. Park] And notice how its equation is written: $y = x^2 - 2$. For any real number you substitute for $x$, squaring it and subtracting 2 gives one and only one unique result. Quadratic equations of the form $y = ax^2 + bx + c$ are always functions! In physics, this models the parabolic trajectory of a thrown football or an avalanche mitigation shell fired across Bridger Bowl! At every instant of time $t$, the projectile has exactly one altitude $y$!""",

    5: r"""[Prof. Park] Now examine Example 4B on page 46: Determine if the circle $x^2 + y^2 = 16$ represents a function.

[TA Sora] Look at the graph: it is a circle of radius 4 centered at the origin $(0, 0)$. It passes through $(4, 0)$, $(0, 4)$, $(-4, 0)$, and $(0, -4)$.

[Prof. Park] Now let us apply our vertical straightedge!
Place a vertical line right down the center along the $y$-axis, which is the line $x = 0$.
Where does that vertical line intersect the circle?

[TA Sora] It hits the circle at the very top at $(0, 4)$, AND it hits the circle at the very bottom at $(0, -4)$!
That is TWO distinct points of intersection for the single input $x = 0$!

[Prof. Park] In fact, almost every vertical line between $x = -4$ and $x = 4$ intersects the circle at two points—one on the upper hemisphere and one on the lower hemisphere.
For example, if $x = 0$, $0^2 + y^2 = 16 \implies y^2 = 16 \implies y = \pm 4$! Two outputs!

[TA Sora] Because a vertical line intersects the circle at more than one point:
$$\mathbf{\text{Fails VLT } \implies \text{A circle is NOT a function!}}$$
A complete circle can never be a function of $x$ because it loops back on top of itself! To make it a function in calculus, we have to slice it into two halves: the top half $y = +\sqrt{16 - x^2}$ and the bottom half $y = -\sqrt{16 - x^2}$!

[Prof. Park] That is why in computer graphics and GIS mapping, closed loops like lakes and boundaries are stored as parametric curves or polygons, because they cannot be modeled as a single $y = f(x)$ function!""",

    6: r"""[Prof. Park] Turn to Example 4C on page 46: Determine if the linear equation $y = 2x - 1$ represents a function.

[TA Sora] Look at the graph: it is a straight line with slope $m = 2$ and $y$-intercept $(0, -1)$, rising steadily from southwest to northeast across the Cartesian plane.

[Prof. Park] Let us apply the Vertical Line Test across this line:
Every vertical line $x = c$ crosses this slanted line at precisely one intersection point: $(c, 2c - 1)$.
Can a vertical line ever hit a slanted line twice? Never! Two straight lines can intersect at most once unless they are the exact same line!

[TA Sora] Therefore:
$$\mathbf{\text{Passes VLT } \implies \text{The line is a FUNCTION!}}$$
In fact, every non-vertical straight line in the universe represents a linear function! That is why we call equations of the form $f(x) = mx + b$ 'Linear Functions!'

[Prof. Park] Exactly. As long as a line has a defined slope—whether positive, negative, or zero—it will pass the Vertical Line Test with flying colors! In economics, think of a simple wage model: if you earn $20 an hour as an apprentice carpenter in Bozeman, your total earnings $y = 20x$ is a linear function of hours worked $x$. For any number of hours you work, your paycheck is uniquely determined! But what about a vertical line? Let us check Slide 7!""",

    7: r"""[Prof. Park] On Slide 7, we test the ultimate extreme in Example 4D on page 46: Determine if the vertical line $x = 3$ represents a function.

[TA Sora] Look at the graph: it is a vertical line passing through 3 on the horizontal axis.
Now let us apply the Vertical Line Test to this graph!
What happens when we test the vertical line $x = 3$?

[Prof. Park] The vertical test line $x = 3$ lands DIRECTLY on top of the graph!
It does not intersect at one point; it does not even intersect at two points—it intersects at **INFINITELY MANY POINTS** simultaneously!
Points $(3, -2)$, $(3, 0)$, $(3, 1)$, $(3, 5)$, $(3, 100)$ all belong to the line!

[TA Sora] The input $x = 3$ is paired with literally every real number in existence!
This is the most catastrophic failure of the Vertical Line Test possible in mathematics!
Therefore:
$$\mathbf{\text{Fails VLT disastrously } \implies \text{A vertical line is NOT a function!}}$$

[Prof. Park] Remember HOY VUX:
Horizontal lines ($y = c$) have slope 0 and ARE functions (they pass VLT, hitting once).
Vertical lines ($x = c$) have undefined slope and are NEVER functions!

[TA Sora] If a GPS navigation device told you that at longitude $x = 3$, your vehicle was located simultaneously in Bozeman, Helena, Billings, and Missoula, you would immediately know the device was malfunctioning. One location input cannot yield infinite outputs!""",

    8: r"""[Prof. Park] On Slide 8, we present the Section 2.4 Complete Mastery Summary. You now hold the complete conceptual toolkit for Relations, Domain, Range, and Functions!

[TA Sora] Let us review our master checklist:
1. **Relation:** Any set of ordered pairs.
2. **Domain:** The set of all inputs ($x$-coordinates).
3. **Range:** The set of all outputs ($y$-coordinates).
4. **Function:** A relation where each input has **exactly one** output.

[Prof. Park] 5. **Testing Ordered Pairs:** Look for repeated $x$-coordinates with different $y$-coordinates. If found, NOT a function.
6. **Testing Graphs (VLT):** If ANY vertical line hits the graph at more than one point, NOT a function.
7. **Function Hall of Fame:**
   - Parabolas ($y = ax^2 + bx + c$): Function!
   - Non-vertical lines ($y = mx + b$): Function!
   - Horizontal lines ($y = c$): Function!
   - Circles & Ellipses: NOT a function!
   - Vertical lines ($x = c$): NOT a function!

[TA Sora] In Lecture 26, we enter the final major chapter of Unit 2: Section 2.5, Systems of Linear Equations, starting with solving systems by graphing! Outstanding work, everyone!"""
}
