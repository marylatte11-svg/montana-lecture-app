# -*- coding: utf-8 -*-
"""
unit2_scripts_l26_l28_master.py
High-density 20-25 minute broadcast scripts for Lectures 26, 27, and 28.
Target: 2,400 - 2,800 words per lecture (~300-360 words per slide across 8 slides).
Rich with Montana life examples: weather telemetry, medical dosages, mountain elevation boiling points.
"""

SCRIPTS_L26 = {
    1: r"""[Prof. Park] Welcome to Lecture 26 of M090! Today on page 47 of your workbook, we introduce the single most important symbolic language in all of modern STEM: Section 2.5, Function Notation.

[TA Sora] Up to this point in algebra, every relationship between two variables was written as an equation: $y = 4x - 5$, $y = x^2$, or $y = -2x + 7$. Today, we retire the simple variable $y$ and introduce its sophisticated, professional counterpart: **$f(x)$**, pronounced aloud as **'f of x'**!

[Prof. Park] Let us decode that symbol with absolute clarity because beginners often make a dangerous mistake right here:
$$\mathbf{y = f(x)}$$
- The letter **$f$** is simply the **name** of the function! Just like people have names like Sora or Eunju, functions have names like $f$, $g$, $h$, or $C$ for Cost and $P$ for Profit.
- The parentheses do NOT mean multiplication! This is NOT '$f$ times $x$.'
- The variable inside the parentheses, **$x$**, is the **input**!
- The entire symbol, **$f(x)$**, is the **output**—the exact equivalent of $y$!

[TA Sora] Think of a function as a physical machine with an input chute and an output tray. The name stamped on the side of the machine is $f$. You drop a raw number $x$ into the input chute, the gears inside the machine follow the formula's recipe, and out drops the finished product into the output tray: $f(x)$!

[Prof. Park] In everyday life in Bozeman, think of postage: your input is the weight of a letter in ounces ($x$), and the output is the required postage in cents: $P(x)$. In pharmacy, your input is the patient's weight in kilograms ($w$), and the output is the safe antibiotic dosage in milligrams: $D(w)$. Function notation makes the input-output relationship explicit right on the page!

[TA Sora] Let us look at Examples 1 and 2 on page 47 to see how $y$ and $f(x)$ work side by side!""",

    2: r"""[Prof. Park] On Slide 2, we compare the old language of $y$ with the new language of $f(x)$ using Examples 1 and 2 on page 47 of your workbook.

[TA Sora] In Example 1, we are given the familiar linear equation:
$$y = 4x - 5$$
The problem asks: 'Find the value of $y$ when $x = 3$.'
How did we do this in previous lectures? We wrote:
'Substitute $x = 3$ into the equation':
$$y = 4(3) - 5 = 12 - 5 = 7$$
Notice how many words we had to write in English: 'when $x = 3$, $y = 7$.' That took an entire sentence!

[Prof. Park] Now look at Example 2 using **Function Notation**:
We write the exact same rule, but give it the name $f$:
$$f(x) = 4x - 5$$
And instead of writing a long English sentence, the question simply asks:
$$\text{Find } \mathbf{f(3)}$$
Look at how concise, elegant, and powerful that is! The number inside the parentheses is 3, which directly commands: 'Plug 3 into the input slot wherever you see $x$!'

[TA Sora] Let us follow the command:
$$f(3) = 4(3) - 5 = 12 - 5 = 7$$
And look at what the notation preserves! In the old style, your final line was '$y = 7$.' But by itself, '$y = 7$' doesn't tell anyone what input produced that 7! You lost the history of your calculation!

[Prof. Park] But with function notation, your final line reads:
$$\mathbf{f(3) = 7}$$
That single mathematical statement tells you everything! It tells you:
1. The input was $x = 3$.
2. The output is $y = 7$.
3. As an ordered pair on the Cartesian grid, this point is $(3, 7)$!

[TA Sora] It is an all-in-one information container: $(x, f(x)) = (3, 7)$! No lost data, zero ambiguity!""",

    3: r"""[Prof. Park] On Slide 3, we summarize the Three Primary Reasons Why Function Notation is Absolutely Essential in STEM fields.

[TA Sora] Reason 1: **Guaranteed Predictability (Single Output)**.
Writing an equation as $f(x)$ is an explicit guarantee to the reader that this mathematical rule represents a true function—it passes the Vertical Line Test! Every input $x$ will produce exactly one predictable output. You never have to wonder if it might branch out into multiple conflicting answers.

[Prof. Park] Reason 2: **Managing Multiple Equations Simultaneously**.
In business economics or Montana agricultural management, you rarely deal with just one formula! Suppose you own a bakery in Bozeman. You have a Revenue formula, a Cost formula, and a Profit formula.
If you used the old notation, all three would start with '$y = \dots$':
$$y = 8x \quad \text{and} \quad y = 3x + 500 \quad \text{and} \quad y = 5x - 500$$
If someone says 'find $y$ when $x = 100$,' which $y$ do they mean? It creates total chaos!

[TA Sora] But with function notation, you give each machine its own unique name!
$$R(x) = 8x \quad (\text{Revenue})$$
$$C(x) = 3x + 500 \quad (\text{Cost})$$
$$P(x) = 5x - 500 \quad (\text{Profit})$$
Now, if you want the cost of baking 100 loaves of sourdough bread, you write $C(100)$. If you want the profit, you write $P(100)$. There is zero confusion!

[Prof. Park] Reason 3: **Clear Input-Output Pairing**.
Writing $f(a) = b$ directly encodes the coordinate pair $(a, b)$ on the Cartesian plane. The input sits inside the parentheses, and the output sits on the other side of the equals sign.

[TA Sora] It is the universal language of computer programming and science! Now let us practice evaluating diverse inputs in Example 3!""",

    4: r"""[Prof. Park] Turn to page 48 of your workbook for Example 3A and 3B: Evaluating Functions with Negative Inputs.
We are given two distinct linear functions:
$$g(x) = -2x + 7 \quad \text{and} \quad h(x) = 3x - 5$$

[TA Sora] Let us tackle Part A first: Find $g(-3)$.
Step 1: Check the name of the function! The name is $g$, so we must use the formula for $g(x)$, NOT $h(x)$!
Step 2: Identify the input: the number inside the parentheses is $-3$.
Step 3: Replace $x$ with $-3$ using TA Sora's Protective Parentheses Rule:
$$g(-3) = -2(-3) + 7$$

[Prof. Park] Now compute the arithmetic carefully following PEMDAS:
First, multiply: $-2 \times (-3) = +6$. A negative multiplied by a negative is positive!
Next, add: $6 + 7 = 13$.
Therefore:
$$g(-3) = 13$$
As an ordered pair on the graph of $g$, this represents the point $(-3, 13)$!

[TA Sora] Now let us evaluate Part B: Find $h(-2)$.
Step 1: Check the name: the name is $h$, so we switch to the formula $h(x) = 3x - 5$!
Step 2: Substitute the input $-2$ inside protective parentheses:
$$h(-2) = 3(-2) - 5$$
Multiply first: $3 \times (-2) = -6$.
Now subtract 5: $-6 - 5 = -11$.
Therefore:
$$h(-2) = -11$$
As an ordered pair on the graph of $h$, this represents the point $(-2, -11)$!

[Prof. Park] Notice how protective parentheses prevent sign errors. When you write $-2(-3)$, you instantly see it is multiplication resulting in positive 6. Order and precision guarantee success!""",

    5: r"""[Prof. Park] On Slide 5, we examine Example 3C and 3D on page 48: Evaluating Functions at Zero and Connecting to $y$-Intercepts.
We continue with:
$$g(x) = -2x + 7 \quad \text{and} \quad h(x) = 3x - 5$$

[TA Sora] Let us evaluate Part C: Find $g(0)$.
The input is 0. We plug 0 into $g(x)$:
$$g(0) = -2(0) + 7 = 0 + 7 = 7$$
So $g(0) = 7$!
As an ordered pair, this is $(0, 7)$.

[Prof. Park] Now evaluate Part D: Find $h(0)$.
The input is 0. We plug 0 into $h(x)$:
$$h(0) = 3(0) - 5 = 0 - 5 = -5$$
So $h(0) = -5$!
As an ordered pair, this is $(0, -5)$.

[TA Sora] Now, students, look at those two points: $(0, 7)$ and $(0, -5)$. What do they have in common?
Their $x$-coordinate is zero!
And what did we learn back in Lecture 18 about any point with $x = 0$?
Any point with $x = 0$ is a **$y$-intercept**!

[Prof. Park] That gives us a profound algebraic theorem that you will use from now through calculus:
$$\mathbf{\text{To find the } y\text{-intercept of ANY function, compute } f(0)!}$$
Evaluating a function at 0 wipes out all the variable terms and leaves only the constant term $b$!
For $g(x) = -2x + 7$, $g(0) = 7$, so the $y$-intercept is $(0, 7)$.
For $h(x) = 3x - 5$, $h(0) = -5$, so the $y$-intercept is $(0, -5)$.

[TA Sora] Whenever you need the starting condition, the initial elevation, or the $y$-intercept, feed zero into the input chute!""",

    6: r"""[Prof. Park] Turn to Example 3E and 3F on page 48: Evaluating Functions with Fractions and Variable Inputs!
Our functions remain:
$$g(x) = -2x + 7 \quad \text{and} \quad h(x) = 3x - 5$$

[TA Sora] Let us tackle Part E: Find $g\left(\frac{1}{2}\right)$.
Do not be intimidated by fractions! Treat it like any other number:
Substitute $\frac{1}{2}$ into $g(x)$:
$$g\left(\frac{1}{2}\right) = -2\left(\frac{1}{2}\right) + 7$$
Multiply first: $-2 \times \frac{1}{2} = -\frac{2}{2} = -1$!
Now add 7: $-1 + 7 = 6$.
Therefore:
$$g\left(\frac{1}{2}\right) = 6$$
As an ordered pair, this is $\left(\frac{1}{2}, 6\right)$!

[Prof. Park] Now examine Part F: Find $h(a)$.
Many students freeze when they see a letter inside the parentheses! They ask: 'Professor Park, what number is $a$?'
You don't need a number! The input slot is simply a placeholder. If the input is $a$, you replace $x$ with $a$:
$$h(a) = 3(a) - 5 = 3a - 5$$
That is your final answer!

[TA Sora] If the input was a picture of a smiley face, the output would be $3(\text{smiley face}) - 5$! The function rule simply says: 'Multiply whatever enters the machine by 3, and subtract 5!' If $a$ enters the machine, $3a - 5$ comes out!

[Prof. Park] That abstract flexibility is what allows scientists to create general formulas in physics and chemistry. Understanding variable inputs prepares you directly for composite functions!""",

    7: r"""[Prof. Park] Now let us examine Example 3G and 3H on page 48: Binomial and Algebraic Expression Inputs.
We have:
$$g(x) = -2x + 7 \quad \text{and} \quad h(x) = 3x - 5$$

[TA Sora] Look at Part G: Find $g(x + 2)$.
Here, the entire expression $(x + 2)$ is being fed into the input chute!
Whatever sits inside the parentheses replaces the variable $x$ inside protective parentheses:
$$g(x + 2) = -2(x + 2) + 7$$

[Prof. Park] Now distribute the $-2$ across both terms inside the parentheses:
$$-2 \cdot x = -2x$$
$$-2 \cdot 2 = -4$$
So we have:
$$-2x - 4 + 7$$
Combine like terms: $-4 + 7 = +3$:
$$g(x + 2) = -2x + 3$$

[TA Sora] Beautiful! Now let us evaluate Part H: Find $h(2x - 1)$.
Feed $(2x - 1)$ into $h(x) = 3x - 5$:
$$h(2x - 1) = 3(2x - 1) - 5$$
Distribute the 3:
$$3 \cdot 2x = 6x$$
$$3 \cdot (-1) = -3$$
So we have:
$$6x - 3 - 5$$
Combine constant terms: $-3 - 5 = -8$:
$$h(2x - 1) = 6x - 8$$

[Prof. Park] In advanced mathematics and calculus, substituting an expression like $(x + h)$ into a function is the foundation of the Difference Quotient, which defines the instantaneous rate of change and the derivative! You are building college-level mathematical muscles today!""",

    8: r"""[Prof. Park] On Slide 8, we reach Example 4 on page 48, which introduces the single most critical conceptual distinction in Section 2.5: Evaluating a Function versus Solving for $x$!
We are given:
$$f(x) = 5x + 3$$

[TA Sora] Compare these two questions very carefully:
Question A: 'Evaluate $f(3)$.'
Question B: 'Solve $f(x) = 18$ for $x$.'
Students, do you see the difference?
In Question A, the 3 is INSIDE the parentheses. That means $x = 3$ is the **input**! You plug 3 in and find the output: $5(3) + 3 = 18$.
In Question B, the 18 is on the OUTSIDE! 18 is the **output** ($y = 18$), and your job is to work backwards to find the input $x$ that created it!

[Prof. Park] Let us solve Part A: $f(x) = 18$.
Replace $f(x)$ with the formula $5x + 3$:
$$5x + 3 = 18$$
Now solve for $x$ using standard two-step algebra:
Subtract 3 from both sides:
$$5x = 15$$
Divide both sides by 5:
$$x = 3$$
The input that produced output 18 was $x = 3$!

[TA Sora] Now let us solve Part B: $f(x) = -12$.
Set the formula equal to $-12$:
$$5x + 3 = -12$$
Subtract 3 from both sides:
$$5x = -15$$
Divide by 5:
$$x = -3$$
The input that produced output $-12$ was $x = -3$!

[Prof. Park] Always look at where the number is sitting:
If the number is inside: $f(\text{number})$, plug it in!
If the number is outside: $f(x) = \text{number}$, set it equal and solve!
In Lecture 27, we take this exact distinction and read function values directly off coordinate graphs!"""
}

SCRIPTS_L27 = {
    1: r"""[Prof. Park] Welcome to Lecture 27 of M090! Today on pages 49 and 50 of your workbook, we master the visual art of Function Notation: Reading Function Values Directly from Graphs.

[TA Sora] In Lecture 26, we evaluated functions using algebraic formulas. But in the real world—in meteorology, hospital telemetry, stock markets, and aeronautics—data rarely arrives as a neat polynomial formula! It arrives as a live, continuous line graph on a monitor or computer display!

[Prof. Park] To read a graph fluently using function notation, you must remember the fundamental geometric translation we proved in Lecture 26:
$$\mathbf{(x, y) \iff (x, f(x))}$$
Every single point on the graph of a function is an ordered pair where:
- The **horizontal coordinate** along the $x$-axis is the **input**: $x$.
- The **vertical height** along the $y$-axis is the **output**: $f(x)$!

[TA Sora] That gives us two straightforward navigation protocols for reading any graph:
1. **Finding $f(a)$:** You are given the input $x = a$.
Start on the horizontal $x$-axis at $a$. Walk vertically until you hit the graph. Read the corresponding height on the vertical $y$-axis! That height is $f(a)$!
2. **Solving $f(x) = b$ for $x$:** You are given the output height $y = b$.
Start on the vertical $y$-axis at height $b$. Walk horizontally until you hit the graph. Look straight down or up at the horizontal $x$-axis to read the input $x$!

[Prof. Park] Think of a high-altitude weather balloon launched from Bozeman measuring temperature as it climbs through the atmosphere: $T(h)$ gives the temperature at altitude $h$. If you want $T(10{,}000)$, you look at altitude 10,000 feet and read the thermometer. If you want to know at what altitude the temperature hits freezing ($T(h) = 32^\circ\text{F}$), you start at 32 degrees and trace across to find the altitude!

[TA Sora] Let us put this visual protocol into action on Example 5 on page 49!""",

    2: r"""[Prof. Park] On Slide 2, we examine Example 5 Part 1 on page 49: Finding $h(2)$ and $h(4)$ using the given graph of $y = h(x)$.

[TA Sora] Look at the graph of $y = h(x)$ on your screen. It is a straight line cutting through the Cartesian coordinate plane.
Let us answer Question A: 'Find $h(2)$.'
Step 1: Where is the number 2 located? It is inside the parentheses, which means **$x = 2$ is our input**!
Step 2: Go to the horizontal $x$-axis and find $2$.
Step 3: Move your pencil vertically to touch the line.
Notice that from $x = 2$, you must move DOWNWARD to reach the graph!

[Prof. Park] Where does your pencil touch the line? It lands squarely on the grid intersection at height $-1$!
That means the point on the line is $(2, -1)$.
Therefore:
$$\mathbf{h(2) = -1}$$

[TA Sora] Now let us answer Question C: 'Find $h(4)$.'
The number 4 is inside the parentheses, so our input is $x = 4$.
Go to $4$ on the horizontal $x$-axis.
Look vertically: to hit the line, we must travel upward!
Follow the vertical grid line at $x = 4$ up to the graph. Your pencil hits the line at height $+2$!
The point on the line is $(4, 2)$.
Therefore:
$$\mathbf{h(4) = 2}$$

[Prof. Park] Look at how effortless and visual that is!
$h(2) = -1$ corresponds to $(2, -1)$.
$h(4) = 2$ corresponds to $(4, 2)$.
No algebraic scratch work required—just clean, disciplined coordinate reading!""",

    3: r"""[Prof. Park] Now turn to Example 5 Part 2 on page 49: Solving $h(x) = -3$ and $h(x) = -2$ for $x$.

[TA Sora] Compare these questions with Slide 2!
On Slide 2, the number was inside the parentheses ($h(2)$).
Here, the number is on the outside:
$$\mathbf{h(x) = -3}$$
This means we are GIVEN the vertical output $y = -3$, and our mission is to find the horizontal input $x$!

[Prof. Park] Let us execute the reverse protocol:
Step 1: Go to the vertical $y$-axis and locate height $-3$.
Step 2: Move horizontally across the grid until you intersect the line $y = h(x)$.
Your pencil hits the line at horizontal coordinate $x = \frac{2}{3}$, or looking at the grid lines, let us check the slope!
Notice that at height $-2$, the graph crosses cleanly at an integer:

[TA Sora] Let us check Question D: 'Solve $h(x) = -2$; find $x$.'
Start on the vertical $y$-axis at height $-2$.
Travel horizontally to the graph: You hit the line at $x = 1$!
The point is $(1, -2)$.
Since $h(1) = -2$, the solution to $h(x) = -2$ is:
$$\mathbf{x = 1}$$

[Prof. Park] And for $h(x) = -3$, tracing horizontally to the line, we find $x = 0$!
The line crosses the vertical axis at $(0, -3)$!
Since $h(0) = -3$, the solution to $h(x) = -3$ is:
$$\mathbf{x = 0}$$

[TA Sora] Notice that point $(0, -3)$! When $x = 0$, that point sits directly on the vertical axis—it is our $y$-intercept! Slide 4 explores intercepts in function notation!""",

    4: r"""[Prof. Park] On Slide 4, we examine Example 5 Part 3 on page 49: Finding Intercepts and Slope from the Graph of $y = h(x)$.

[TA Sora] Question E asks for the **$x$-intercept** of the graph.
Look at where the line crosses the horizontal $x$-axis:
It cuts cleanly through at $x = 3$!
As an ordered pair, the $x$-intercept is $(3, 0)$.
In function notation, how do we write an $x$-intercept?
An $x$-intercept always has an output of zero:
$$\mathbf{h(3) = 0}$$

[Prof. Park] Question F asks for the **$y$-intercept** of the graph.
Look at where the line crosses the vertical $y$-axis:
It cuts cleanly through at height $y = -3$!
As an ordered pair, the $y$-intercept is $(0, -3)$.
In function notation, how do we write a $y$-intercept?
A $y$-intercept always has an input of zero:
$$\mathbf{h(0) = -3}$$

[TA Sora] Question G asks: 'What is the slope of the line $y = h(x)$?'
Let us count Rise over Run between our two clean intercepts:
Point 1: $(0, -3)$
Point 2: $(3, 0)$
Starting from $(0, -3)$, to reach $(3, 0)$:
You climb UPWARD from $-3$ to $0$: That is a **Rise** of $+3$!
You run to the RIGHT from $0$ to $3$: That is a **Run** of $+3$!
$$m = \frac{\text{Rise}}{\text{Run}} = \frac{+3}{+3} = 1$$

[Prof. Park] The slope is $m = 1$, and the $y$-intercept is $b = -3$.
Therefore, the full equation of this function is:
$$\mathbf{h(x) = 1x - 3 \implies h(x) = x - 3}$$
Look at how everything connects: the graph, the intercepts, the slope, and the algebraic formula all tell the exact same unified story!""",

    5: r"""[Prof. Park] Turn to page 50 for In-Class Practice Problems #1 and #2: Multi-Function Algebraic Practice.
We are given two linear functions:
$$f(x) = 2x - 8 \quad \text{and} \quad g(x) = x - 9$$

[TA Sora] In Practice Problem #1, we are asked to evaluate three expressions:
Part A: Find $f(5)$.
Substitute $5$ into $f(x)$:
$$f(5) = 2(5) - 8 = 10 - 8 = 2$$
Point on the graph: $(5, 2)$.

[Prof. Park] Part B: Find $f(-1)$.
Substitute $-1$ inside protective parentheses:
$$f(-1) = 2(-1) - 8 = -2 - 8 = -10$$
Point on the graph: $(-1, -10)$.

[TA Sora] Part C: Find $f(0)$.
Substitute $0$:
$$f(0) = 2(0) - 8 = 0 - 8 = -8$$
That gives the $y$-intercept: $(0, -8)$!

[Prof. Park] Now let us tackle Practice Problem #2 using the function $g(x) = x - 9$:
Part A: Find $g(-4)$.
$$g(-4) = (-4) - 9 = -13$$
Part B: Find $g(9)$.
$$g(9) = 9 - 9 = 0$$
Notice that $g(9) = 0$ means $(9, 0)$ is the $x$-intercept of $g$!
Part C: Find $g(0)$.
$$g(0) = 0 - 9 = -9$$
That is the $y$-intercept: $(0, -9)$!

[TA Sora] Look at how rapid and confident you become when you know whether you are feeding inputs into the machine or reading outputs! Practice creates mastery!""",

    6: r"""[Prof. Park] On Slide 6, we examine Practice Problem #3 on page 50: Solving for $x$ given $p(x) = 2x - 11$.

[TA Sora] Look at the wording of Problem #3: 'Solve the following for $x$.'
Part A asks us to solve:
$$\mathbf{p(x) = 1}$$
Remember: 1 is the OUTPUT, not the input! Do not plug 1 in for $x$!
Replace $p(x)$ with the expression $2x - 11$:
$$2x - 11 = 1$$

[Prof. Park] Now solve for $x$ using basic algebra:
Add 11 to both sides:
$$2x = 1 + 11 = 12$$
Divide both sides by 2:
$$x = 6$$
Let us verify: $p(6) = 2(6) - 11 = 12 - 11 = 1$! Perfectly true!
The ordered pair is $(6, 1)$.

[TA Sora] Now let us solve Part B:
$$\mathbf{p(x) = -15}$$
Set the formula equal to $-15$:
$$2x - 11 = -15$$
Add 11 to both sides:
$$2x = -15 + 11 = -4$$
Divide by 2:
$$x = -2$$
Let us check: $p(-2) = 2(-2) - 11 = -4 - 11 = -15$! True!
The ordered pair is $(-2, -15)$.

[Prof. Park] Look at the symmetry:
When given $p(x) = k$, you write an equation with $k$ on the right side and solve for the unknown input $x$. It is the reverse journey of evaluating a function!""",

    7: r"""[Prof. Park] On Slide 7, we examine Practice Problem #4 on page 50: Reading Values from a Curved Graph of $y = f(x)$.

[TA Sora] Look at the graph on your screen: it is a smooth curve passing through multiple grid intersections. Let us answer the four questions systematically:
Question A: 'Find $f(2)$.'
Input is $x = 2$.
Go to 2 on the horizontal axis. Move vertically to hit the curve. The curve passes through at height $-1$!
Therefore:
$$\mathbf{f(2) = -1}$$

[Prof. Park] Question B: 'Find $f(0)$.'
Input is $x = 0$.
Look at the vertical axis: where does the curve cross the $y$-axis?
It crosses cleanly at height $3$!
Therefore:
$$\mathbf{f(0) = 3}$$
This is our $y$-intercept: $(0, 3)$!

[TA Sora] Question C: 'Solve $f(x) = 0$ for $x$.'
Output is $y = 0$! This is asking for the **$x$-intercepts**—where the curve touches the horizontal ground!
Looking at the horizontal axis, the curve crosses at $x = -1$ AND at $x = 3$!
Therefore:
$$\mathbf{x = -1 \quad \text{and} \quad x = 3}$$
Both inputs produce an output of zero!

[Prof. Park] Question D: 'Solve $f(x) = 3$ for $x$.'
Find height 3 on the vertical axis. Trace horizontally across:
The curve touches height 3 at $x = 0$ and at $x = 4$!
Therefore:
$$\mathbf{x = 0 \quad \text{and} \quad x = 4}$$

[TA Sora] Notice how a single output can have two different inputs, while each input still has only one output! It completely satisfies the Vertical Line Test!""",

    8: r"""[Prof. Park] Slide 8 brings us to the Section 2.5 Mastery Summary: The Golden Rule of Function Notation.

[TA Sora] Let us summarize this core distinction once and for all so you never mix them up on an exam:
- **Evaluating $f(a)$:**
  The value $a$ is the **INPUT** ($x = a$).
  Plug $a$ into the formula, or locate $a$ on the horizontal axis and find the vertical height.
- **Solving $f(x) = b$:**
  The value $b$ is the **OUTPUT** ($y = b$).
  Set the formula equal to $b$ and solve for $x$, or locate $b$ on the vertical axis and trace horizontally to find the input $x$.

[Prof. Park] And remember our intercept identities in function notation:
- The **$y$-intercept** is always found by evaluating **$f(0)$**.
- The **$x$-intercepts** are always found by solving **$f(x) = 0$**.

[TA Sora] In Lecture 28, we combine function notation with everything we learned about slopes and straight lines to study Section 2.6: Linear Functions $f(x) = mx + b$! You have done outstanding work today!"""
}

SCRIPTS_L28 = {
    1: r"""[Prof. Park] Welcome to Lecture 28 of M090! Today on pages 51 and 52 of your workbook, we formally unite two massive branches of algebra: Section 2.6, Linear Functions.

[TA Sora] In Sections 2.1 through 2.3, we studied linear equations of the form $y = mx + b$. In Sections 2.4 and 2.5, we mastered the language of functions, domain, range, and $f(x)$. Today, we merge them into a single, unified mathematical structure:
$$\mathbf{f(x) = mx + b}$$
A **Linear Function** is simply any function whose graph is a straight line!

[Prof. Park] Look at the two key parameters in $f(x) = mx + b$:
- The parameter **$m$** is the **slope**, which represents the **constant rate of change**! In science and economics, $m$ tells you how fast the output changes per unit of change in the input—dollars per hour, miles per gallon, or degrees per thousand feet of elevation.
- The parameter **$b$** is the **$y$-intercept**, which represents the **initial condition** or starting value: $f(0) = b$.

[TA Sora] What are the Domain and Range of a non-horizontal linear function?
Think about an endless straight line slanting across the Cartesian plane:
It extends infinitely far to the left ($-\infty$) and infinitely far to the right ($+\infty$). So the **Domain** is $(-\infty, \infty)$!
And it climbs infinitely high ($+\infty$) and drops infinitely deep ($-\infty$). So the **Range** is $(-\infty, \infty)$!
Every non-horizontal, non-vertical linear function has domain and range equal to all real numbers!

[Prof. Park] Let us explore how to graph, analyze, and build these linear functions in Example 1 on page 51!""",

    2: r"""[Prof. Park] Example 1 on page 51: Graph the linear function $f(x) = 2x - 4$, and identify its slope, $y$-intercept, $x$-intercept, domain, and range.

[TA Sora] Let us extract our parameters directly from the equation $f(x) = 2x - 4$:
Step 1: The slope $m$ is the coefficient of $x$:
$$m = 2 \quad \left(\text{or } \frac{2}{1}\right)$$
This means a **Rise of $+2$** for every **Run of $+1$**.
Step 2: The $y$-intercept is the constant term $b = -4$:
$$\text{Point: } (0, -4)$$

[Prof. Park] Step 3: Now let us find the **$x$-intercept** algebraically by setting $f(x) = 0$:
$$0 = 2x - 4$$
Add 4 to both sides:
$$2x = 4 \implies x = 2$$
So the $x$-intercept is $(2, 0)$!

[TA Sora] Step 4: Now let us plot and graph!
Place your first point at the $y$-intercept: $(0, -4)$.
From $(0, -4)$, use your slope: rise up 2 units, run right 1 unit, landing at $(1, -2)$.
Rise up 2 units, run right 1 unit again, landing at $(2, 0)$, which confirms our $x$-intercept!
Draw a straight line through these points with arrowheads on both ends.

[Prof. Park] Step 5: State the Domain and Range:
Since the line extends without bound in both horizontal directions:
$$\text{Domain: } (-\infty, \infty)$$
Since it extends without bound in both vertical directions:
$$\text{Range: } (-\infty, \infty)$$

[TA Sora] Everything connects with total clarity: Slope $+2$, intercepts at $(0, -4)$ and $(2, 0)$, domain and range all real numbers!""",

    3: r"""[Prof. Park] Now turn to Example 2 on page 51: Graph the linear function $g(x) = -x + 4$, and identify its slope, $y$-intercept, $x$-intercept, domain, and range.

[TA Sora] Let us analyze $g(x) = -x + 4$:
Look in front of $x$: there is a negative sign, which means there is an understood $-1$ multiplying $x$!
The slope is:
$$m = -1 \quad \left(\text{or } \frac{-1}{1}\right)$$
This represents a **Rise of $-1$** (a drop of 1 unit) for every **Run of $+1$** to the right.
The $y$-intercept is:
$$b = 4 \implies (0, 4)$$

[Prof. Park] Now find the **$x$-intercept** algebraically: set $g(x) = 0$:
$$0 = -x + 4$$
Add $x$ to both sides:
$$x = 4 \implies \text{Point: } (4, 0)$$

[TA Sora] Let us graph the line:
Plot the $y$-intercept at $(0, 4)$ on the vertical axis.
Count your slope: drop down 1 unit, run right 1 unit to $(1, 3)$.
Drop down 1, run right 1 to $(2, 2)$.
Continue to $(3, 1)$ and $(4, 0)$—our exact $x$-intercept!
Draw the line slanting downhill from left to right at a 45-degree angle.

[Prof. Park] Now evaluate Domain and Range:
Horizontal coverage has no barriers:
$$\text{Domain: } (-\infty, \infty)$$
Vertical coverage reaches both infinities:
$$\text{Range: } (-\infty, \infty)$$

[TA Sora] Notice the difference between Examples 1 and 2: Example 1 had a positive slope ($m = 2$) and sloped uphill. Example 2 has a negative slope ($m = -1$) and sloped downhill. The sign of the slope dictates the entire visual personality of the function!""",

    4: r"""[Prof. Park] On Slide 4, we examine Example 3 on page 52: Determining Domain, Range, and Function Values from a Given Graph.

[TA Sora] Look at the graph on your screen. It displays a linear function cutting through the coordinate plane. Let us answer each question step by step:
Question A: 'What is the Domain in interval notation?'
Since the line has arrows on both ends extending infinitely left and right:
$$\text{Domain: } (-\infty, \infty)$$
Question B: 'What is the Range in interval notation?'
Since it extends infinitely down and up:
$$\text{Range: } (-\infty, \infty)$$

[Prof. Park] Question C: 'Find the $y$-intercept.'
Look at where the line crosses the vertical axis:
It crosses at $(0, 2)$. In function notation: $f(0) = 2$.
Question D: 'Find the $x$-intercept.'
Look at where the line crosses the horizontal axis:
It crosses at $(-4, 0)$. In function notation: $f(-4) = 0$.

[TA Sora] Question E: 'Find the slope of the line.'
Let us use our two intercepts: $(-4, 0)$ and $(0, 2)$:
Rise from 0 to 2 is $+2$.
Run from $-4$ to 0 is $+4$.
$$m = \frac{\text{Rise}}{\text{Run}} = \frac{+2}{+4} = \frac{1}{2}$$

[Prof. Park] Question F: 'Write the linear function formula.'
With slope $m = \frac{1}{2}$ and $y$-intercept $b = 2$:
$$\mathbf{f(x) = \frac{1}{2}x + 2}$$
Question G: 'Evaluate $f(4)$ using the formula.'
$$f(4) = \frac{1}{2}(4) + 2 = 2 + 2 = 4$$
Check the graph at $x = 4$: the height is exactly 4! The formula and the graph confirm each other with 100% precision!""",

    5: r"""[Prof. Park] Turn to page 52 for Example 4: Creating a Linear Function $h(x)$ from Given Conditions.
Find the equation of the linear function $h(x)$ that has a **slope of $\frac{3}{4}$** and a **$y$-intercept of $(0, -5)$**.

[TA Sora] This problem is an absolute breeze if you know your definitions!
Look at what is given:
Slope: $m = \frac{3}{4}$.
$y$-intercept: $(0, -5)$, which gives $b = -5$.

[Prof. Park] Since we have $m$ and $b$, we write down the Linear Function template:
$$h(x) = mx + b$$
Substitute $m = \frac{3}{4}$ and $b = -5$:
$$\mathbf{h(x) = \frac{3}{4}x - 5}$$

[TA Sora] Notice that the problem asked for the function $h(x)$. If you write $y = \frac{3}{4}x - 5$, you might lose a point on your exam for notation! When a problem asks for a function named $h$, use $h(x)$!

[Prof. Park] Think of what this function models in Montana construction: Suppose you are building an access ramp at Gallatin College. The ramp starts 5 feet below ground level in an excavation trench ($b = -5$), and rises at a steady ADA-compliant incline of $\frac{3}{4}$ of an inch per horizontal foot. The function $h(x) = \frac{3}{4}x - 5$ predicts the ramp's elevation at any distance $x$!""",

    6: r"""[Prof. Park] Now examine Example 5 on page 52: Creating a Linear Function $k(x)$ given a slope of $\frac{1}{3}$ that passes through the point $(6, -2)$.

[TA Sora] Look at the given point: $(6, -2)$.
Notice that $x = 6 \neq 0$! This is NOT a $y$-intercept!
Therefore, we cannot just plug $-2$ into $b$. We must deploy our trusted friend: **Point-Slope Form**!
$$y - y_1 = m(x - x_1)$$

[Prof. Park] Substitute $m = \frac{1}{3}$ and $(x_1, y_1) = (6, -2)$ with protective parentheses:
$$y - (-2) = \frac{1}{3}(x - 6)$$
On the left side: $y - (-2) = y + 2$:
$$y + 2 = \frac{1}{3}(x - 6)$$

[TA Sora] Distribute the slope $\frac{1}{3}$:
$$\frac{1}{3} \cdot x = \frac{1}{3}x$$
$$\frac{1}{3} \cdot (-6) = -2$$
So we have:
$$y + 2 = \frac{1}{3}x - 2$$
Subtract 2 from both sides to isolate $y$:
$$y = \frac{1}{3}x - 2 - 2 \implies y = \frac{1}{3}x - 4$$

[Prof. Park] Now convert to the requested function notation $k(x)$:
$$\mathbf{k(x) = \frac{1}{3}x - 4}$$
Let us verify: $k(6) = \frac{1}{3}(6) - 4 = 2 - 4 = -2$! It passes through $(6, -2)$ with 100% accuracy!""",

    7: r"""[Prof. Park] Turn to Example 6 on page 52: Find the equation of the linear function $f(x)$ that passes through the two points $(2, 3)$ and $(4, 9)$.

[TA Sora] Here we are given TWO points, but no slope!
Step 1: Compute the slope $m$ between $(2, 3)$ and $(4, 9)$ using the slope formula:
$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{9 - 3}{4 - 2}$$
In the numerator: $9 - 3 = 6$.
In the denominator: $4 - 2 = 2$.
$$m = \frac{6}{2} = 3$$
The slope is $m = 3$!

[Prof. Park] Step 2: Now choose one point and use Point-Slope Form. Let us select $(2, 3)$ with $m = 3$:
$$y - y_1 = m(x - x_1)$$
$$y - 3 = 3(x - 2)$$
Distribute the 3:
$$y - 3 = 3x - 6$$
Add 3 to both sides:
$$y = 3x - 6 + 3 \implies y = 3x - 3$$

[TA Sora] Step 3: Write in the requested function notation $f(x)$:
$$\mathbf{f(x) = 3x - 3}$$
Let us verify with our other point $(4, 9)$:
$$f(4) = 3(4) - 3 = 12 - 3 = 9!$$
It works perfectly!

[Prof. Park] In forestry science in Montana's Gallatin National Forest, if a lodgepole pine seedling is 3 inches tall at year 2 and 9 inches tall at year 4, this linear function $f(x) = 3x - 3$ models its annual growth rate of 3 inches per year!""",

    8: r"""[Prof. Park] On Slide 8, we examine Example 7 on page 52: Find the equation of the linear function $g(x)$ that contains the points $(7, 9)$ and $(-4, 9)$.

[TA Sora] Apply TA Sora's Three-Second Scan! Look at the coordinates:
Point 1: $(7, 9)$
Point 2: $(-4, 9)$
What jumps out immediately? Both points share the exact same output: $y = 9$!

[Prof. Park] Let us check the slope formula:
$$m = \frac{9 - 9}{-4 - 7} = \frac{0}{-11} = 0$$
The slope is zero!
By HOY VUX: Horizontal line, zero slope, equation $y = 9$.

[TA Sora] And how do we write that in function notation?
Replace $y$ with $g(x)$:
$$\mathbf{g(x) = 9}$$
This is the **Constant Function**! No matter what input you feed into $g(x)$—whether $x = 7$, $x = -4$, or $x = 1{,}000$—the output is always 9!

[Prof. Park] What are the Domain and Range of a constant function?
- **Domain:** Any real number can enter, so $\text{Domain} = (-\infty, \infty)$.
- **Range:** It only touches one single height! So $\text{Range} = \{9\}$.

[TA Sora] In food science and pharmaceutical storage in Bozeman, refrigeration units must maintain a constant temperature of $9^\circ\text{C}$ regardless of outside weather fluctuations. That is a constant function $g(x) = 9$!

[Prof. Park] In Lecture 29, we take all of these skills and step into full real-world modeling: ski shop economics, car depreciation, and sales commissions! Fantastic job today, everyone!"""
}
