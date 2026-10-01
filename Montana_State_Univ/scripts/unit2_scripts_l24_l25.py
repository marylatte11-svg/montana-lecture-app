# -*- coding: utf-8 -*-
"""
unit2_scripts_l24_l25.py
High-density broadcast tiki-taka scripts for Lectures 24 and 25.
Target: ~250-350 words per slide (~2,000-2,600 words per lecture).
"""

SCRIPTS_L24 = {
    1: r"""[Prof. Park] Welcome to Lecture 24 of M090! Today on page 45 of your workbook, we step into one of the most foundational concepts in all of modern mathematics: Section 2.4, Relations, Domain, and Range.

[TA Sora] In everyday conversation, a 'relation' describes how two things connect—like parents and children, or Montana weather and snow accumulation. In mathematics, a **relation** has a very precise, universal definition:
A relation is simply **any set of ordered pairs** $(x, y)$!

[Prof. Park] It can be a finite list of five points, or an infinite line stretching across the universe. Every ordered pair connects an **input** to an **output**.
That gives us two essential definitions that will follow you through calculus and data science:
1. The **Domain** is the set of all first coordinates—all allowable input values ($x$-values).
2. The **Range** is the set of all second coordinates—all resulting output values ($y$-values).

[TA Sora] Think of a modern GPS navigation system in Montana. Your input coordinate is your latitude and longitude on the map (Domain), and your output is your driving time or elevation (Range). Or think of Gallatin College student registration: every student ID number (input) is paired with a specific student name (output).

[Prof. Park] In this lecture, we will learn how to extract and report the domain and range in two distinct environments:
First, for **discrete relations**—isolated scatter points where we list numbers in curly braces $\{ \}$.
Second, for **continuous graphs**—smooth unbroken curves where we use interval notation with brackets $[a, b]$!

[TA Sora] Let us dive straight into Example 1 on page 45 and master discrete relations first!""",

    2: r"""[Prof. Park] Example 1 on page 45: For the following relation, determine the domain and the range:
$$\{(1, -1), (2, 0), (3, 1), (4, 2), (1, 3)\}$$

[TA Sora] Let us examine the inputs first to find the **Domain**.
Look at the first number in each ordered pair:
From $(1, -1)$, we get $1$.
From $(2, 0)$, we get $2$.
From $(3, 1)$, we get $3$.
From $(4, 2)$, we get $4$.
From $(1, 3)$, we get $1$ again!

[Prof. Park] Now pause right here! Notice that the input $1$ appears twice in our list of pairs. How do we write that in our final answer, Sora?

[TA Sora] This is the golden rule of set notation: **Never repeat elements inside a set!**
A set is simply a collection of unique elements. Even if the number 1 appears a hundred times, you only write it once:
$$\text{Domain} = \{1, 2, 3, 4\}$$
Notice we wrap them in curly roster braces $\{ \}$, and list them in ascending order from smallest to largest!

[Prof. Park] Now let us examine the outputs to find the **Range**.
Look at the second number in each ordered pair:
From $(1, -1)$, we get $-1$.
From $(2, 0)$, we get $0$.
From $(3, 1)$, we get $1$.
From $(4, 2)$, we get $2$.
From $(1, 3)$, we get $3$.

[TA Sora] Are there any duplicates here? No! All five outputs are distinct:
$$\text{Range} = \{-1, 0, 1, 2, 3\}$$

[Prof. Park] Beautifully organized. Discrete points use curly braces, list elements in numerical order, and never repeat duplicate numbers!""",

    3: r"""[Prof. Park] On Slide 3, we plot all five points of Example 1 on the Cartesian coordinate grid: $(1, -1)$, $(2, 0)$, $(3, 1)$, $(4, 2)$, and $(1, 3)$.

[TA Sora] Look at how these five dots arrange themselves across the grid!
Point $(2, 0)$ rests on the positive $x$-axis.
Points $(3, 1)$ and $(4, 2)$ sit comfortably in Quadrant I.
Point $(1, -1)$ sits in Quadrant IV.
And Point $(1, 3)$ sits high in Quadrant I.

[Prof. Park] Now, students, look very carefully at the two points $(1, -1)$ and $(1, 3)$. What geometric feature do you observe?

[TA Sora] They are stacked directly on top of each other! They share the exact same horizontal position $x = 1$. If you hold a vertical ruler along the line $x = 1$, your ruler touches BOTH points simultaneously!

[Prof. Park] That visual observation is momentous! In Lecture 25, that exact vertical alignment is what will cause this relation to fail the famous Vertical Line Test.

[TA Sora] In a discrete relation, you have empty white space between the points—there are no connecting lines, no fractions between them, just isolated islands. That is why the domain and range are lists of discrete numbers, not intervals!""",

    4: r"""[Prof. Park] Slide 4 introduces one of the most intuitive visual tools in all of mathematics: The Mapping Diagram.

[TA Sora] A mapping diagram translates ordered pairs into a visual flow of information!
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
If you think of the left oval as telephone buttons and the right oval as recipients, pressing button 1 dials two different people at the exact same moment.

[TA Sora] Mapping diagrams make it immediately obvious whether an input is branching out to multiple outputs. Keep that branching picture in mind as we move forward!""",

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

[Prof. Park] Always remember: Domain is horizontal coverage (Left to Right). Range is vertical coverage (Bottom to Top)! Always write the smaller number first: $[\text{min}, \text{max}]$!""",

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

[Prof. Park] That is a vital distinction. Never just grab the endpoints! Always scan from the very bottom of the canvas to the very top: lowest $y$ to highest $y$!""",

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
Which reads: 'The set of all $x$ such that $x$ is between $-4$ and $3$, inclusive.' Both notations describe the exact same geometric reality!""",

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

SCRIPTS_L25 = {
    1: r"""[Prof. Park] Welcome to Lecture 25 of M090! Today on page 46 of your workbook, we arrive at the crown jewel of introductory algebra: The Formal Definition of a Function and the Vertical Line Test.

[TA Sora] In Lecture 24, we saw that *any* collection of ordered pairs is a relation. But mathematics demands predictability! If you build an airplane, design a bridge, or write computer software, you need systems that produce predictable, reliable results. That special, elite class of relations is called a **Function**!

[Prof. Park] Let us read the formal mathematical definition on page 46 together:
A **Function** is a relation that assigns to **each input value ($x$) exactly ONE output value ($y$)**!
Read that phrase again: *Each input has exactly ONE output!*

[TA Sora] Here is my favorite everyday analogy: A vending machine in the Gallatin College student lounge!
You walk up to the machine, insert your money, and press button B2. You expect a bag of barbecue chips to drop into the tray. If every time you press B2 you get barbecue chips, the machine is functioning properly—it is a **function**!
Now imagine you press B2, and today you get chips, but tomorrow you press B2 and it spits out a bottle of water, and the next day it spits out a granola bar! The machine is unpredictable—it is broken—it is **NOT a function**!

[Prof. Park] An input can never be undecided about its output. One input cannot produce two different answers.
Now, can two different buttons give the same snack? Suppose button B2 gives chips, and button B3 also gives chips. Is that allowed?

[TA Sora] Yes! That is completely allowed! Two different inputs can produce the same output—like two different roads leading to the same trailhead in Yellowstone. But one button cannot dispense two different snacks at once! Input must uniquely determine output!""",

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

[TA Sora] But remember: repeated $y$-coordinates are fine! If we had $(1, 2)$ and $(3, 2)$, both inputs lead to 2, which IS a function. It is repeated $x$-values with different $y$-values that break the rule!""",

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

[Prof. Park] Let us take this vertical ruler test and test four diverse graphs in Example 4 on the following slides!""",

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

[Prof. Park] And notice how its equation is written: $y = x^2 - 2$. For any real number you substitute for $x$, squaring it and subtracting 2 gives one and only one unique result. Quadratic equations of the form $y = ax^2 + bx + c$ are always functions!""",

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
A complete circle can never be a function of $x$ because it loops back on top of itself!""",

    6: r"""[Prof. Park] Turn to Example 4C on page 46: Determine if the linear equation $y = 2x - 1$ represents a function.

[TA Sora] Look at the graph: it is a straight line with slope $m = 2$ and $y$-intercept $(0, -1)$, rising steadily from southwest to northeast across the Cartesian plane.

[Prof. Park] Let us apply the Vertical Line Test across this line:
Every vertical line $x = c$ crosses this slanted line at precisely one intersection point: $(c, 2c - 1)$.
Can a vertical line ever hit a slanted line twice? Never! Two straight lines can intersect at most once unless they are the exact same line!

[TA Sora] Therefore:
$$\mathbf{\text{Passes VLT } \implies \text{The line is a FUNCTION!}}$$
In fact, every non-vertical straight line in the universe represents a linear function! That is why we call equations of the form $f(x) = mx + b$ 'Linear Functions!'

[Prof. Park] Exactly. As long as a line has a defined slope—whether positive, negative, or zero—it will pass the Vertical Line Test with flying colors! But what about a vertical line? Let us check Slide 7!""",

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
Vertical lines ($x = c$) have undefined slope and are NEVER functions!""",

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
