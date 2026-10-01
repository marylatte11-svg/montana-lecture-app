# -*- coding: utf-8 -*-
"""
unit2_scripts_l16_l17.py
High-density broadcast tiki-taka scripts for Lectures 16 and 17.
Target: ~250-350 words per slide (~2,400-2,800 words per lecture).
"""

SCRIPTS_L16 = {
    1: """[Prof. Park] Welcome, everyone, to Unit 2 of M090 Introductory Algebra! In Unit 1, we worked primarily along a single dimension—the one-dimensional real number line. Today, we make a tremendous conceptual leap into two-dimensional space: the Rectangular Coordinate System, also universally known as the Cartesian Coordinate Plane.

[TA Sora] Named after the seventeenth-century French philosopher and mathematician René Descartes! Legend has it that Descartes was lying in bed watching a fly crawl across a tiled ceiling and realized he could pinpoint the fly's exact location at every moment simply by measuring its distance from two perpendicular walls.

[Prof. Park] That simple, brilliant realization revolutionized all of modern science. On the screen before you, look at those two perpendicular number lines. The horizontal axis is our $x$-axis, running from left to right, while the vertical axis is our $y$-axis, running from bottom to top. Where those two number lines intersect at right angles is our anchor: the Origin, denoted by the ordered pair $(0, 0)$.

[TA Sora] And notice how those two intersecting axes divide the entire infinite plane into four distinct regions called Quadrants. We label them with Roman numerals, starting from the upper-right corner as Quadrant I and moving counterclockwise: Quadrant I is top-right, Quadrant II is top-left, Quadrant III is bottom-left, and Quadrant IV is bottom-right!

[Prof. Park] Why counterclockwise, students often ask? In trigonometry and navigation, positive angles rotate counterclockwise from the positive horizontal axis. Notice the sign signatures in each quadrant: Quadrant I has positive $x$ and positive $y$, $(+, +)$. Quadrant II has negative $x$ and positive $y$, $(-, +)$. Quadrant III is entirely negative, $(-, -)$. And Quadrant IV has positive $x$ and negative $y$, $(+, -)$.

[TA Sora] Here is my favorite paper-and-pencil memory hack for every beginner: 'Walk along the hallway before you take the elevator!' Alphabetically, $x$ comes before $y$. In the ordered pair $(x, y)$, the first number always commands horizontal travel along the $x$-axis, and the second number commands vertical travel up or down. If you reverse them, you end up on the wrong floor in the wrong building!""",

    2: """[Prof. Park] Let us put Sora's hallway-and-elevator rule immediately into practice with Example 1A from page 30 of your workbook: plot and label the ordered pair $A(4, 0)$, and determine whether it lies in a quadrant or on an axis.

[TA Sora] First, let us identify our coordinates clearly. In the ordered pair $(4, 0)$, our horizontal coordinate is $x = 4$, and our vertical coordinate is $y = 0$. We always begin our journey at the center of the universe: the origin, $(0, 0)$.

[Prof. Park] Now follow the coordinates step by step. Since $x = +4$, we walk four units to the right along the horizontal $x$-axis: one, two, three, four. Now look at the vertical coordinate: $y = 0$. How many units do we travel vertically, Sora?

[TA Sora] Exactly zero units! We do not move up, and we do not move down. We place our pencil point firmly on the grid right there at 4 on the horizontal axis, draw a clear solid dot, and label it with a capital letter $A$ and its coordinates $(4, 0)$.

[Prof. Park] Now comes the crucial conceptual question: does point $A$ lie in Quadrant I, Quadrant IV, or neither? This is one of the most frequent trap questions on the first midterm!

[TA Sora] It lies in neither quadrant! Points that sit directly on the boundary lines—the axes—do not belong to any quadrant. Because its $y$-coordinate is zero, point $A$ lies directly on the positive $x$-axis. In fact, throughout Unit 2, we will call any point where a graph crosses the $x$-axis an '$x$-intercept.'

[Prof. Park] Exactly right. Whenever $y = 0$, you are standing on the $x$-axis. Keep that principle etched in your mind: $(a, 0)$ is always on the $x$-axis!""",

    3: """[Prof. Park] Moving directly to Example 1B on page 30: plot and classify the ordered pair $B(-1, 3)$.

[TA Sora] Let us break down the address: $x = -1$ and $y = +3$. Starting at the origin $(0, 0)$, our $x$-coordinate is negative one. That means we travel one unit to the left along the horizontal axis, stopping at $-1$.

[Prof. Park] Now look at the vertical coordinate: $y = +3$. Since it is positive three, we take our elevator up three full units: up one, two, three. We mark our dot right at that intersection, label it $B(-1, 3)$, and observe where we landed.

[TA Sora] We are in the upper-left territory! Going left means $x < 0$, and going up means $y > 0$. That matches our signature $(-, +)$, which places point $B$ squarely inside Quadrant II!

[Prof. Park] Notice how clear and unambiguous the coordinate grid is. In geography, when you navigate around the Gallatin Valley using GPS coordinates, your GPS receiver is doing this exact calculation in spherical coordinates. West is negative longitude, North is positive latitude. Point $B$ is like driving one mile west of downtown Bozeman and three miles north toward Springhill!

[TA Sora] A common student pitfall here is accidentally plotting $(3, -1)$ instead of $(-1, 3)$. That happens when someone rushes and grabs the positive number first! Remember: $x$ comes first in the alphabet, $x$ comes first in the ordered pair, horizontal motion is always first. Guard against flipping your axes!""",

    4: """[Prof. Park] Next up is Example 1C: plot and classify point $C(0, 5)$. Look closely at this coordinate pair, students. How does this compare with point $A(4, 0)$ that we graphed two slides ago?

[TA Sora] This is the exact mirror counterpart of the zero-coordinate trap! Here, $x = 0$ and $y = 5$. If $x = 0$, we start at the origin $(0, 0)$, and our horizontal movement is zero—we do not move left, and we do not move right!

[Prof. Park] We remain right on the vertical spine of the plane. Then we read $y = +5$, which commands us to move five units straight up along the vertical axis: one, two, three, four, five. We plot our point and label it $C(0, 5)$.

[TA Sora] And just like point $A$, point $C$ sits directly on a boundary line! Because it rests on the vertical number line, it does not belong to Quadrant I or Quadrant II. It lies directly on the positive $y$-axis.

[Prof. Park] In algebraic graphing, any point of the form $(0, b)$ where $x = 0$ is called a '$y$-intercept' because it is where a line or curve intercepts the vertical $y$-axis. 

[TA Sora] Think about this in real life: if $x$ represents time elapsed in seconds and $y$ represents your elevation or bank account balance, $x = 0$ is the starting line—the initial condition! That $y$-intercept tells you where you began before any time ticked away.""",

    5: """[Prof. Park] Let us examine Example 1D: plot and classify point $D(-3, -4)$. Both coordinates are now negative numbers. Sora, walk us through the movement.

[TA Sora] We reset to the origin $(0, 0)$. First, our horizontal address is $x = -3$. A negative $x$ means we travel left three units on the horizontal axis: left 1, 2, 3 to $-3$. Next, our vertical address is $y = -4$. A negative $y$ means we travel downward four units: down 1, 2, 3, 4 to $-4$.

[Prof. Park] We locate the intersection of the vertical grid line at $x = -3$ and the horizontal grid line at $y = -4$. We draw a crisp dot and label it $D(-3, -4)$. Since both coordinates are negative, $(- , -)$, point $D$ lies deep in the lower-left section: Quadrant III.

[TA Sora] Students often ask me during tutoring sessions: 'Sora, why does Quadrant III have both negative numbers?' Think about temperature and depth. To the left is below zero horizontally, and downwards is below zero vertically—like measuring depth beneath the surface of the Madison River in sub-zero winter temperatures!

[Prof. Park] That is a memorable visual. Notice the contrast: Quadrant I is $(+, +)$, completely positive. Quadrant III is $(- , -)$, completely negative. They are diagonal opposites across the origin. If you reflect a point across the origin, both signs flip!""",

    6: """[Prof. Park] On Slide 6, we have brought all four points together onto a single, unified Cartesian coordinate grid: Point $A(4, 0)$, Point $B(-1, 3)$, Point $C(0, 5)$, and Point $D(-3, -4)$. Take a wide-angle view of this canvas.

[TA Sora] Look at how beautifully balanced this display is! Point $A(4, 0)$ anchors the positive $x$-axis. Point $C(0, 5)$ anchors the positive $y$-axis. Point $B(-1, 3)$ stands proudly in Quadrant II. And Point $D(-3, -4)$ sits in Quadrant III.

[Prof. Park] Compare points $A(4, 0)$ and $C(0, 5)$ side by side. Notice how students who confuse $(x, y)$ with $(y, x)$ will accidentally swap these two types of points. An ordered pair is called 'ordered' precisely because the order of elements conveys meaning: $(4, 0) \\neq (0, 4)$!

[TA Sora] One is four miles east of the town square; the other is four miles north! If you swap them on a Montana mountain trail map, you end up on the ridge of Mount Ellis instead of downtown Bozeman.

[Prof. Park] When working on your homework, always verify the quadrant signs before lifting your pencil: Quadrant I is $(+, +)$, Quadrant II is $(-, +)$, Quadrant III is $(-, -)$, Quadrant IV is $(+, -)$, and zero coordinates always belong to an axis, never a quadrant.""",

    7: """[Prof. Park] Now that we know how to plot static points, let us talk about the dynamic bridge between algebra and geometry: the Basic Graphing Strategy on page 30 of your workbook. 

[TA Sora] This is where mathematics becomes truly powerful. An equation with two variables, like $y = 2x + 1$, is an input-output machine. You feed in an input value for the independent variable $x$, the equation processes it through arithmetic operations, and it produces an output value for the dependent variable $y$!

[Prof. Park] Why do we call $x$ the 'independent variable'? Because you, the mathematician, have the total freedom to choose any valid number from the domain to plug in for $x$. You can choose $x = 0$, $x = 1$, $x = -2$, or $x = 100$. But once you pick $x$, the value of $y$ is entirely dependent on the equation's rule.

[TA Sora] And each pair of input and output forms an ordered pair $(x, y)$! When you plot several of these ordered pairs on your Cartesian coordinate grid, a visual pattern begins to emerge—a line, a gentle curve, a parabola, or a V-shape.

[Prof. Park] That geometric figure is what we call the 'graph' of the equation. A graph is not just a pretty picture; it is a visual picture of infinitely many true solutions packed together side by side.

[TA Sora] My golden recommendation for building a table of values: always pick $x = 0$ first because arithmetic with zero is effortless! Then pick a small positive number like $x = 1$ or $x = 2$, and a small negative number like $x = -1$ or $x = -2$. That gives you a balanced view across both sides of the vertical axis!""",

    8: """[Prof. Park] Let us formalize that definition on Slide 8: What does it mean for an ordered pair to be a 'solution' to an equation in two variables?

[TA Sora] By strict algebraic definition: an ordered pair $(x, y)$ is a solution to an equation if substituting the first number for $x$ and the second number for $y$ turns the equation into a true mathematical statement!

[Prof. Park] Let us test that with an example right now. Suppose we have the equation $3x - 2y = 8$. Is the ordered pair $(4, 2)$ a solution? Let us check: replace $x$ with 4 inside protective parentheses, and replace $y$ with 2 inside protective parentheses: $3(4) - 2(2) = 12 - 4 = 8$. Does $8 = 8$? Absolutely true! Therefore, $(4, 2)$ is a valid solution.

[TA Sora] Now test the ordered pair $(2, 1)$ in that same equation: $3(2) - 2(1) = 6 - 2 = 4$. Does $4 = 8$? No, that is completely false! Therefore, $(2, 1)$ is NOT a solution.

[Prof. Park] And here is the profound connection between algebra and the Cartesian coordinate plane: If a point is a solution, it sits directly ON the graph. If a point is NOT a solution, it floats somewhere off the graph!

[TA Sora] That means a drawn line or curve is literally the collection of every single point in the entire universe that makes the equation true! Every single microscopic point on that line satisfies the equation. Algebra and geometry are two languages speaking the exact same truth!""",

    9: """[Prof. Park] Let us apply this verification method to the equation given on Slide 9: $2x + y = 7$. We are given three test points: $P_1(2, 3)$, $P_2(1, 5)$, and $P_3(4, -1)$. Let us test each one algebraically and visually.

[TA Sora] Let us test Point 1: $(2, 3)$. Here $x = 2$ and $y = 3$. We substitute: $2(2) + 3 = 4 + 3 = 7$. That is $7 = 7$, perfectly true! So $(2, 3)$ is a solution and lies on the line.

[Prof. Park] Now test Point 2: $(1, 5)$. We substitute $x = 1$ and $y = 5$: $2(1) + 5 = 2 + 5 = 7$. Again, $7 = 7$, true! Point $(1, 5)$ is also on the line.

[TA Sora] Now test Point 3: $(4, -1)$. We substitute $x = 4$ and $y = -1$: $2(4) + (-1) = 8 - 1 = 7$. True again! Point $(4, -1)$ is on the line.

[Prof. Park] Now look at the graph on your screen. Notice how those three points—$(1, 5)$, $(2, 3)$, and $(4, -1)$—fall in a perfectly straight line! If you lay a straightedge across them, they line up without any wobble or deviation.

[TA Sora] What if someone tested $(3, 2)$? Let us check: $2(3) + 2 = 6 + 2 = 8 \\neq 7$. If you plot $(3, 2)$ on that coordinate grid, you will see it sits just slightly to the right of the line, hovering off the path. Only the points that satisfy $2x + y = 7$ lie on the line!""",

    10: """[Prof. Park] Outstanding work on Lecture 16! You have officially entered the world of two-dimensional coordinate geometry. Let us review the foundational principles we established today.

[TA Sora] Principle 1: The Cartesian plane is formed by two perpendicular number lines intersecting at the origin $(0, 0)$. Horizontal is $x$, vertical is $y$.

[Prof. Park] Principle 2: In any ordered pair $(x, y)$, order is sacred. Always walk horizontally first, then travel vertically.

[TA Sora] Principle 3: Quadrants are numbered counterclockwise I, II, III, IV starting from top-right. Quadrant I is $(+,+)$, Quadrant II is $(-,+)$, Quadrant III is $(-,-)$, and Quadrant IV is $(+,-)$. Any point containing a zero sits directly on an axis, not in any quadrant.

[Prof. Park] Principle 4: A point is a solution to an equation if and only if substituting its coordinates makes the equation true. The graph is the visual collection of all true solutions.

[TA Sora] In Lecture 17, we take this exact coordinate grid and explore the Seven Fundamental Parent Functions of algebra—from straight lines to parabolas, square roots, and absolute value curves! Rest up, review your workbook page 30, and we will see you in Lecture 17!"""
}

SCRIPTS_L17 = {
    1: """[Prof. Park] Welcome to Lecture 17 of M090! Today, on pages 31 and 32 of your workbook, we explore one of the most exciting libraries in all of precalculus and introductory algebra: The Seven Fundamental Parent Functions and their Domains and Ranges.

[TA Sora] In architecture, before you design a custom house or a bridge in Bozeman, you need to understand your fundamental building materials: steel beams, wooden joists, concrete slabs. In mathematics, these seven basic equations are your structural building blocks!

[Prof. Park] Every complex formula you encounter in physics, business economics, engineering, and data science is simply a transformation—a stretch, a shift, or a reflection—of one of these seven basic parent equations.

[TA Sora] Today we will construct a table of values for each of the seven, plot their points, discover their characteristic shapes, and write their Domain and Range using the interval notation we mastered back in Unit 1!

[Prof. Park] Remember our definitions: The **Domain** is the set of all allowable input values ($x$-values) that you can safely plug into the equation without causing mathematical catastrophe like division by zero or square roots of negative numbers. The **Range** is the set of all resulting output values ($y$-values). Let us inspect Equation A!""",

    2: """[Prof. Park] Equation A on page 31 is the Constant Function: $y = 3$. At first glance, students often look at this equation and say, 'Professor Park, where is the $x$?'

[TA Sora] That is the beauty of a constant function! No matter what input value you choose for $x$—whether $x = -2$, $x = 0$, $x = 2$, or even $x = 1,000$—the output $y$ does not care! The rule simply states: $y$ is always 3!

[Prof. Park] Look at our table of values: when $x = -2$, $y = 3$, giving us the point $(-2, 3)$. When $x = 0$, $y = 3$, giving us $(0, 3)$, which is our $y$-intercept. When $x = 2$, $y = 3$, giving us $(2, 3)$.

[TA Sora] When you plot those points on the grid and connect them, you get a perfectly flat, level, horizontal line passing through 3 on the $y$-axis! Think of a calm, flat lake or the level surface of a workshop workbench.

[Prof. Park] Now let us determine its Domain and Range in interval notation. Can $x$ be any real number? Yes! You can walk as far to the left as $-\\infty$ or as far to the right as $+\\infty$. So the Domain is $(-\\infty, \\infty)$.

[TA Sora] But what about the Range? What vertical heights does the graph achieve? It only ever touches one single height: 3! It never goes up to 4, and it never drops down to 2. So the Range is written in set notation as the single element $\\{3\\}$. A flat horizontal line has domain all reals, but a single fixed range!""",

    3: """[Prof. Park] Let us examine Equation B on page 31: the Linear Identity Function, $y = x$.

[TA Sora] The identity function is the ultimate mirror of algebra! Whatever number goes in for $x$ comes out unchanged as $y$. If $x = -2$, then $y = -2$. If $x = 0$, then $y = 0$, which means it passes straight through the origin! If $x = 2$, then $y = 2$.

[Prof. Park] Notice the slope: for every one unit you move to the right, you move exactly one unit up. It cuts right through Quadrant I and Quadrant III at a perfect 45-degree angle.

[TA Sora] Let us analyze the Domain and Range. How far left and right does this line travel? It extends without bound in both directions, so the Domain is $(-\\infty, \\infty)$.

[Prof. Park] And how far down and up does it travel vertically? As you travel to the right, it rises toward $+\\infty$. As you travel to the left, it plunges toward $-\\infty$. Therefore, the Range is also $(-\\infty, \\infty)$!

[TA Sora] In real life, think of a direct one-to-one conversion: if you exchange one US dollar for one dollar credit at a campus store, your output exactly mirrors your input. The identity function is the baseline reference against which all other linear equations are measured.""",

    4: """[Prof. Park] Now we step into non-linear functions with Equation C on page 31: the Quadratic Parent Function, $y = x^2$. This is the foundation of parabolas, which we study extensively throughout Unit 3!

[TA Sora] Let us build our table of values very carefully, paying special attention to negative inputs. What happens when we plug in $x = -2$? Remember protective parentheses: $(-2)^2 = (-2) \\times (-2) = +4$! A negative multiplied by a negative is positive!

[Prof. Park] Exactly. When $x = -1$, $(-1)^2 = +1$. When $x = 0$, $0^2 = 0$. When $x = 1$, $1^2 = 1$. And when $x = 2$, $2^2 = 4$. Look at the symmetry in those $y$-values: 4, 1, 0, 1, 4!

[TA Sora] When you plot those points on the Cartesian grid, you do NOT get a V-shape with straight lines; you get a smooth, curved, symmetrical cup known as a Parabola! The bottom-most turning point at $(0, 0)$ is called the Vertex.

[Prof. Park] Now let us evaluate the Domain and Range. Can you square any real number? Of course! Positive, negative, zero, fractions—anything can be squared. So the Domain is $(-\\infty, \\infty)$.

[TA Sora] But look at the Range! Can the square of a real number ever be negative? Never! The lowest $y$-value on the graph is 0 at the origin, and the parabola opens upward toward $+\\infty$. Therefore, the Range in interval notation is $[0, \\infty)$, with a square bracket at 0 because 0 is included! Parabolic shapes appear everywhere in Montana—from the trajectory of a tossed football to satellite dish receivers.""",

    5: """[Prof. Park] Next is Equation D: the Square Root Function, $y = \\sqrt{x}$. Here we encounter our very first restricted domain in algebra!

[TA Sora] This is a critical moment. In the real number system, can you take the square root of a negative number like $\\sqrt{-4}$? No! No real number multiplied by itself gives negative four. That means negative numbers are completely forbidden from entering this square root machine!

[Prof. Park] Therefore, in our table of values, we only select non-negative inputs, and specifically perfect squares to keep our arithmetic clean: $x = 0$, $x = 1$, $x = 4$, and $x = 9$.

[TA Sora] Let us compute the outputs: $\\sqrt{0} = 0$, giving $(0, 0)$. Next, $\\sqrt{1} = 1$, giving $(1, 1)$. Next, $\\sqrt{4} = 2$, giving $(4, 2)$. And $\\sqrt{9} = 3$, giving $(9, 3)$.

[Prof. Park] Look at the graph: it starts firmly at the origin $(0, 0)$ and curves gently to the right in Quadrant I, flattening out as $x$ increases. Notice there is absolutely nothing in Quadrants II or III—the entire left half of the coordinate plane is blank!

[TA Sora] That directly defines our Domain and Range! The Domain starts at 0 and goes right to infinity: $[0, \\infty)$. The Range starts at height 0 and climbs slowly upward to infinity: $[0, \\infty)$! Both Domain and Range are $[0, \\infty)$ with square brackets at zero!""",

    6: """[Prof. Park] Turn to page 32 of your workbook for Equation E: the Absolute Value Function, $y = |x|$.

[TA Sora] What does absolute value mean geometrically? It represents distance from zero on the number line! And distance can never be negative. So if $x = -3$, $|-3| = 3$. If $x = -1$, $|-1| = 1$. If $x = 0$, $|0| = 0$. If $x = 1$, $|1| = 1$. And if $x = 3$, $|3| = 3$.

[Prof. Park] Compare this carefully with the parabola $y = x^2$ we saw on Slide 4. A parabola curves smoothly at the bottom like a rounded bowl. But the absolute value graph consists of two straight linear rays meeting at a sharp corner at the origin $(0, 0)$—a sharp V-shape!

[TA Sora] To the right of the $y$-axis, it has a constant slope of $+1$. To the left of the $y$-axis, it has a constant slope of $-1$. That sharp corner at $(0, 0)$ is called the vertex.

[Prof. Park] Let us identify its Domain and Range. Any real number can be placed inside an absolute value bar, so the Domain is all real numbers, $(-\\infty, \\infty)$.

[TA Sora] And just like $y = x^2$, the outputs can never be negative! The lowest point on the V is at $y = 0$, and both wings rise upward toward $+\\infty$. So the Range is $[0, \\infty)$. When you see a sharp V-shape, your brain should immediately recognize: Absolute Value!""",

    7: """[Prof. Park] Slide 7 introduces Equation F on page 32: the Cubic Function, $y = x^3$.

[TA Sora] Cubing a number means multiplying three copies together: $x \\cdot x \\cdot x$. Let us test our signs carefully! When $x = -2$, $(-2)^3 = (-2) \\cdot (-2) \\cdot (-2) = -8$! Because we have an odd number of negative factors, the result stays negative!

[Prof. Park] Exactly. When $x = -1$, $(-1)^3 = -1$. When $x = 0$, $0^3 = 0$. When $x = 1$, $1^3 = 1$. And when $x = 2$, $2^3 = +8$. Look at the points: $(-2, -8)$, $(-1, -1)$, $(0, 0)$, $(1, 1)$, and $(2, 8)$.

[TA Sora] When you connect these points, you get an elegant S-shaped curve! In Quadrant I, it shoots steeply upward. In Quadrant III, it plunges steeply downward. It passes through the origin $(0, 0)$, where it flattens momentarily.

[Prof. Park] Notice the contrast with $y = x^2$. The parabola was U-shaped and stayed completely above the horizontal axis. The cubic function is S-shaped and reaches into both positive and negative infinity!

[TA Sora] Therefore, its Domain is $(-\\infty, \\infty)$, and its Range is also $(-\\infty, \\infty)$! In engineering and economics, cubic functions model volume growth—like the volume of concrete required for building foundations as structural dimensions expand.""",

    8: """[Prof. Park] Our seventh and final parent function on page 32 is Equation G: the Cube Root Function, $y = \\sqrt[3]{x}$.

[TA Sora] Compare this with the square root function we studied on Slide 5. With a square root, negative inputs were strictly forbidden because no real number squared produces a negative. But can you take the cube root of a negative number?

[Prof. Park] Absolutely! Because $(-2) \\cdot (-2) \\cdot (-2) = -8$, the cube root of negative eight is a perfectly valid real number: $\\sqrt[3]{-8} = -2$!

[TA Sora] Let us check our key table values: If $x = -8$, $y = -2$. If $x = -1$, $y = -1$. If $x = 0$, $y = 0$. If $x = 1$, $y = 1$. And if $x = 8$, $y = 2$.

[Prof. Park] Look at the graph: it is literally the cubic S-curve from Slide 7 rotated onto its side! It hugs the $x$-axis, passing smoothly through the origin and extending infinitely to the left and to the right.

[TA Sora] Because odd roots accept any real number input, there are no domain restrictions! The Domain is $(-\\infty, \\infty)$. And because it rises infinitely slowly to the right and drops infinitely slowly to the left, the Range is also $(-\\infty, \\infty)$!

[Prof. Park] Notice that distinction: even roots (like square roots) have restricted non-negative domains $[0, \\infty)$, while odd roots (like cube roots) have unrestricted domains $(-\\infty, \\infty)$!""",

    9: """[Prof. Park] On Slide 9, we present the Grand Summary Table of all seven fundamental parent functions from Section 2.0. Every student in M090 should commit these visual profiles to memory.

[TA Sora] Let us do a rapid-fire review:
1. $y = c$ (Constant): Horizontal line, Domain $(-\\infty, \\infty)$, Range $\\{c\\}$.
2. $y = x$ (Linear Identity): 45-degree straight line through origin, Domain $(-\\infty, \\infty)$, Range $(-\\infty, \\infty)$.
3. $y = x^2$ (Quadratic): U-shaped parabola opening upward, Domain $(-\\infty, \\infty)$, Range $[0, \\infty)$.
4. $y = \\sqrt{x}$ (Square Root): Gentle half-arm curve starting at $(0, 0)$ in Quadrant I, Domain $[0, \\infty)$, Range $[0, \\infty)$.

[Prof. Park] And the remaining three:
5. $y = |x|$ (Absolute Value): Sharp V-shape with corner at $(0, 0)$, Domain $(-\\infty, \\infty)$, Range $[0, \\infty)$.
6. $y = x^3$ (Cubic): Steep vertical S-curve passing through origin, Domain $(-\\infty, \\infty)$, Range $(-\\infty, \\infty)$.
7. $y = \\sqrt[3]{x}$ (Cube Root): Flat horizontal S-curve passing through origin, Domain $(-\\infty, \\infty)$, Range $(-\\infty, \\infty)$.

[TA Sora] Notice that only two functions have restricted domains: the square root function, because you cannot take an even root of a negative number! All others have domain $(-\\infty, \\infty)$.

[Prof. Park] In Lecture 18, we zoom in on the most fundamental of all these families: linear equations in two variables, standard form, slope-intercept form, and graphing by intercepts. Exceptional work today, everyone!"""
}
