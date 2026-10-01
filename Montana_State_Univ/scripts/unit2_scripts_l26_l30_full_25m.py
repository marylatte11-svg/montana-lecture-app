# -*- coding: utf-8 -*-
"""
unit2_scripts_l26_l30_full_25m.py
Full 20-25 minute broadcast scripts for Lectures 26 to 30.
Target: 2,400 - 2,800 words per lecture (~300-360 words per slide across 8 slides).
Rich with Montana life examples: ski shops, grain bins, Bozeman elevation boiling points, blood pressure.
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

from unit2_scripts_l26_l28_master import SCRIPTS_L26, SCRIPTS_L27, SCRIPTS_L28

# Let us enrich L26, L27, L28 to guarantee >= 2,400 words
SCRIPTS_L26_EXP = dict(SCRIPTS_L26)
SCRIPTS_L27_EXP = dict(SCRIPTS_L27)
SCRIPTS_L28_EXP = dict(SCRIPTS_L28)

# L26 expansions
SCRIPTS_L26_EXP[1] = SCRIPTS_L26[1] + """\n\n[TA Sora] Notice how this matches modern computer programming languages like Python or JavaScript! In Python, when you define a function `def calculate_tax(income):`, `calculate_tax` is the name, `income` is the input parameter, and the returned value is the output. Math notation was the original programming language centuries before computers existed!"""
SCRIPTS_L26_EXP[2] = SCRIPTS_L26[2] + """\n\n[Prof. Park] In physics, if $v(t)$ represents the velocity of an avalanche projectile at time $t$, writing $v(3) = 45$ tells the whole story: at exactly 3 seconds after launch, the projectile travels at 45 meters per second! Compact, unambiguous, and mathematically elegant!"""
SCRIPTS_L26_EXP[3] = SCRIPTS_L26[3] + """\n\n[TA Sora] In Montana agriculture, if you manage both a wheat field and a barley field, you might write $W(x)$ for wheat yield and $B(x)$ for barley yield as a function of fertilizer $x$. Function notation lets you track both crops side by side without ever getting their outputs crossed!"""
SCRIPTS_L26_EXP[4] = SCRIPTS_L26[4] + """\n\n[TA Sora] Here is my golden rule for negative inputs: Always whisper to yourself, 'protect the negative!' When you write parentheses around $(-3)$, your eyes immediately recognize that you are multiplying $-2$ by $-3$, avoiding the catastrophic mistake of treating it as subtraction $-2 - 3$!"""
SCRIPTS_L26_EXP[5] = SCRIPTS_L26[5] + """\n\n[Prof. Park] In chemistry, evaluating at zero gives the baseline temperature of an unheated solution. Finding $f(0)$ is universally the initial condition of any physical or financial system!"""
SCRIPTS_L26_EXP[6] = SCRIPTS_L26[6] + """\n\n[Prof. Park] When evaluating fraction inputs like $g(1/2)$, always look for cancellation opportunities between the slope coefficient and the denominator before doing any multiplication. Simplifying before multiplying keeps numbers manageable and prevents computational errors!"""
SCRIPTS_L26_EXP[7] = SCRIPTS_L26[7] + """\n\n[TA Sora] When substituting expressions like $(x+2)$, think of it as upgrading the input software inside the machine: the machine's internal mechanism stays the exact same, but it now processes an entire packet of information simultaneously!"""
SCRIPTS_L26_EXP[8] = SCRIPTS_L26[8] + """\n\n[TA Sora] Remember: In evaluating, you are standing at the top of the mountain looking down; in solving, you are standing in the valley looking up to find which trail brought you here! Always check whether you are searching for input or output!"""

# L27 expansions
SCRIPTS_L27_EXP[1] = SCRIPTS_L27[1] + """\n\n[TA Sora] In our modern visual culture, being able to read and interpret charts and graphs is one of the top five skills employers look for in technical and business careers. When an executive or engineer looks at a performance graph, they don't solve equations by hand—they read inputs and outputs directly from the axes using this exact visual protocol!"""
SCRIPTS_L27_EXP[2] = SCRIPTS_L27[2] + """\n\n[Prof. Park] When students practice graph reading, I always tell them to trace with their finger or pencil tip: start at the horizontal coordinate, move perpendicular to the axis until you hit the line, then turn 90 degrees and read the vertical scale. That physical movement builds muscle memory that prevents axis-swapping errors!"""
SCRIPTS_L27_EXP[3] = SCRIPTS_L27[3] + """\n\n[TA Sora] When solving $h(x) = -2$, think of setting a horizontal laser line across the room at height $-2$. Wherever that laser beam intersects the graph, look down at your feet to find the floor coordinate $x$! Looking horizontally first, then vertically down, is the reverse of evaluating!"""
SCRIPTS_L27_EXP[4] = SCRIPTS_L27[4] + """\n\n[Prof. Park] In geotechnical engineering across Gallatin County, when surveyors analyze slope stability on mountain hillsides, identifying where the surface profile intersects horizontal bedrock and vertical survey stakes determines safe excavation limits for new homes!"""
SCRIPTS_L27_EXP[5] = SCRIPTS_L27[5] + """\n\n[Prof. Park] In medical diagnostics, think of patient monitoring: if $f(t)$ represents patient body temperature over time, $f(0)$ is baseline admission temperature, and solving $f(t) = 102$ finds the exact hour when fever peaked so nurses can administer medication!"""
SCRIPTS_L27_EXP[6] = SCRIPTS_L27[6] + """\n\n[TA Sora] Notice how solving $p(x) = k$ is literally finding the $x$-coordinate of the intersection between the line $y = p(x)$ and the horizontal line $y = k$! Algebra and geometry are two mirrors reflecting the exact same truth!"""
SCRIPTS_L27_EXP[7] = SCRIPTS_L27[7] + """\n\n[TA Sora] In hydrology, when river streamflow gauges record discharge during spring snowmelt, solving $f(t) = \text{flood stage}$ alerts the county emergency services to issue sandbag warnings to downstream ranches!"""
SCRIPTS_L27_EXP[8] = SCRIPTS_L27[8] + """\n\n[Prof. Park] Take a moment to reflect on your journey: in just a few lectures, you have transitioned from basic arithmetic on a number line to fluently reading and manipulating two-dimensional functional coordinate graphs. That is a massive intellectual milestone!"""

# Extra enrichments for L27 and L28 to guarantee >= 2,400 words
SCRIPTS_L27_EXP[4] = SCRIPTS_L27_EXP[4] + """\n\n[TA Sora] Notice how finding the slope directly from the graph allows us to write the function $h(x) = x - 3$. Once you have the formula, you can compute values far beyond the boundaries of your graph paper—like $h(50) = 47$! Algebra gives you infinite foresight!"""
SCRIPTS_L27_EXP[5] = SCRIPTS_L27_EXP[5] + """\n\n[TA Sora] Notice that finding $f(0) = -8$ gives us the vertical starting point, while finding $g(9) = 0$ gives us the horizontal landing point. In physics, these are initial position and final impact!"""
SCRIPTS_L27_EXP[6] = SCRIPTS_L27_EXP[6] + """\n\n[Prof. Park] In civil engineering, solving $p(x) = 1$ is how bridge designers determine the exact thermal expansion joint spacing needed on Montana bridges during 100-degree summer heatwaves!"""

SCRIPTS_L28_EXP[1] = SCRIPTS_L28[1] + """\n\n[Prof. Park] In physics, Sir Isaac Newton built the foundation of classical mechanics on linear rates of change: velocity is the rate of change of position, and acceleration is the rate of change of velocity. Linear functions are the simplest, most fundamental building blocks of all physical laws in the universe!"""
SCRIPTS_L28_EXP[2] = SCRIPTS_L28[2] + """\n\n[TA Sora] When graphing $f(x) = 2x - 4$, always verify that your slope triangle matches your calculated intercepts! Starting at $(0, -4)$, rising 2 and running 1 brings you to $(1, -2)$, and rising 2 and running 1 again hits $(2, 0)$—our exact $x$-intercept! When your slope steps land directly on your calculated intercepts, you have 100% confidence your graph is correct!"""
SCRIPTS_L28_EXP[3] = SCRIPTS_L28[3] + """\n\n[Prof. Park] Notice how in $g(x) = -x + 4$, the $x$-intercept is $(4, 0)$ and the $y$-intercept is $(0, 4)$. It forms an isosceles right triangle with the axes in Quadrant I, with both legs equal to 4 units! Geometric symmetry provides an instant visual verification!"""
SCRIPTS_L28_EXP[4] = SCRIPTS_L28[4] + """\n\n[TA Sora] Notice that writing the formula as $f(x) = \frac{1}{2}x + 2$ lets you calculate the height at ANY point in the future—even $x = 1{,}000$—without having to draw graph paper miles wide! Math gives you infinite reach!"""
SCRIPTS_L28_EXP[5] = SCRIPTS_L28[5] + """\n\n[TA Sora] When solving real-world construction problems, always double-check the units: if slope is given in inches of rise per foot of run, make sure your $x$ variable is measured in feet and your output in inches, or convert them to consistent units before building!""" + """\n\n[Prof. Park] In carpentry framing for a Bozeman timber home, when carpenters establish the roof pitch slope of $3/4$, knowing the exact starting offset from the foundation ($b = -5$) ensures the rafter plumb cuts align with the top plate!"""
SCRIPTS_L28_EXP[6] = SCRIPTS_L28[6] + """\n\n[Prof. Park] In mechanical engineering, when selecting gear ratios or pulley drives, the relationship between input motor rpm and output spindle rpm is a linear function passing through a specific operating design point!""" + """\n\n[TA Sora] Notice how we solved for $y$ step by step without skipping: $y + 2 = \\frac{1}{3}(x - 6) \\implies y + 2 = \\frac{1}{3}x - 2 \\implies y = \\frac{1}{3}x - 4$. Every line has a reason, and every reason brings total confidence!"""
SCRIPTS_L28_EXP[7] = SCRIPTS_L28[7] + """\n\n[TA Sora] Notice that between year 2 and year 4, 2 years elapsed and height increased by 6 inches. Dividing 6 inches by 2 years gives 3 inches per year! The slope formula is simply calculating average unit rate!""" + """\n\n[Prof. Park] In hydrology, if snowpack depth increases linearly by 3 inches per storm cycle, modeling cumulative winter precipitation allows reservoir managers to forecast springtime irrigation runoff for Gallatin Valley ranches!"""
SCRIPTS_L28_EXP[8] = SCRIPTS_L28[8] + """\n\n[Prof. Park] In computer software, a constant function represents a locked configuration setting or a flat subscription fee. It reminds us that horizontal lines are the peaceful ground floor of linear algebra!"""

# Now write fully expanded L29 and L30 (>= 2,400 words each!)
SCRIPTS_L29 = {
    1: r"""[Prof. Park] Welcome to Lecture 29 of M090! Today on pages 53 and 54 of your workbook, we step into the true practical power of mathematics: Section 2.7, Modeling with Linear Functions.

[TA Sora] Up to this point in Unit 2, we have studied the mechanics of lines—finding slopes, plotting intercepts, writing equations, and evaluating functions. Today, we put all of those tools to work solving real-world problems in Montana business, vehicle finance, and career economics!

[Prof. Park] Every linear model in the real world follows our trusted master formula:
$$\mathbf{f(x) = mx + b}$$
In real-world applications, each piece of this formula has an immediate, concrete physical meaning:
- **The Slope $m$ is the Rate of Change!** Whenever you read a word problem, look for action words like 'per', 'each', 'every', 'rate of', 'gaining', or 'depreciating'. That rate is always your slope $m$! If the value is increasing, $m$ is positive. If the value is decreasing, $m$ is negative.
- **The $y$-Intercept $b$ is the Initial Value or Fixed Cost!** This is the baseline starting amount at time zero ($x = 0$)—the initial deposit, the flat rental fee, the purchase price, or the starting elevation before any activity begins.

[TA Sora] In Montana business management, this separation of fixed costs ($b$) and variable costs ($m$) is how every small business owner calculates their operating budget and sets their customer prices. Whether you are running a fly-fishing guide service on the Madison River, an elk hunting outfitting company, or a winter ski shop in Bozeman, linear modeling gives you total financial control!

[Prof. Park] Think of a cattle ranch in the Gallatin Valley: the ranch has fixed overhead costs—property taxes on the land, barn maintenance, and tractor loan payments—which exist even if zero calves are raised ($b$). Then there is the variable cost per head of cattle—feed, veterinary care, and ear tags ($m$). Total annual cost is directly $C(x) = mx + b$!

[TA Sora] Understanding linear models allows you to separate what you cannot change (fixed overhead) from what you can control (variable activity). That financial clarity is essential for building a thriving enterprise!

[Prof. Park] Let us look at Example 1 on page 53 and see how Kim models his Bozeman ski rental business!""",

    2: r"""[Prof. Park] Example 1 Part 1 on page 53: Kim owns a ski rental business in Bozeman. His monthly fixed costs—which cover his shop lease on Main Street, insurance, and utilities—are **$350**. He pays an employee **$15 per hour** to operate the tuning and rental desk. Let us build a linear cost model!

[TA Sora] Let us identify our variables and parameters with complete clarity:
Step 1: Define the independent variable:
Let $x$ represent the **number of hours** the employee works during the month.
Step 2: Define the dependent function:
Let $C(x)$ represent the **total monthly operating cost** in dollars.

[Prof. Park] Step 3: Identify the fixed cost ($b$):
Kim must pay $350 for the shop lease every month, even if the shop is closed and zero hours are worked!
Therefore, the initial starting cost at $x = 0$ is:
$$b = 350$$

[TA Sora] Step 4: Identify the variable rate ($m$):
Kim pays the employee $15 *per hour*. That keyword 'per' signals our rate of change:
$$m = 15$$
Step 5: Assemble the linear cost function:
$$\mathbf{C(x) = 15x + 350}$$

[Prof. Park] Look at how beautifully that formula models reality!
If $x = 0$ hours are worked: $C(0) = 15(0) + 350 = \$350$ (just the fixed lease).
For every single additional hour the employee works, the total monthly cost increases by exactly $15. That is a constant rate of change!

[TA Sora] In Bozeman's winter tourist season, when blizzards dump fresh powder at Bridger Bowl and Big Sky, Kim might need the shop open 60 hours a week! Having a linear cost model allows him to forecast his exact wage liabilities before the season even begins.

[Prof. Park] Small business owners who fail to calculate their cost functions often run out of cash during slow shoulder seasons like April and May. Mathematical modeling provides the foresight needed to maintain healthy cash reserves year-round!

[TA Sora] On Slide 3, we will use Kim's cost function to evaluate a specific monthly work schedule!""",

    3: r"""[Prof. Park] On Slide 3, we execute Example 1 Part 2 on page 53: Find Kim's total monthly cost if his employee works **25 hours**.

[TA Sora] Let us look at our mathematical model from Slide 2:
$$C(x) = 15x + 350$$
The problem tells us: 'the employee works 25 hours.'
Is 25 an input or an output? Hours worked is our independent input variable $x$!
So the problem commands us: 'Evaluate $C(25)$!'

[Prof. Park] Let us substitute $x = 25$ inside protective parentheses:
$$C(25) = 15(25) + 350$$
Multiply first following PEMDAS:
$$15 \times 25 = 375$$
Kim pays $\$375$ in employee wages.
Now add the fixed lease cost:
$$375 + 350 = 725$$
Therefore:
$$\mathbf{C(25) = 725}$$

[TA Sora] Now write the answer in a complete, professional English sentence:
'If the employee works 25 hours, Kim's total monthly operating cost is **$725**.'
Notice how we state the units: 25 hours, and 725 dollars.

[Prof. Park] What if Kim rents out ski packages at $\$45$ per rental? If his cost is $\$725$, he needs to rent about 17 ski packages that month just to cover his operating expenses! That is the famous 'break-even point.'

[TA Sora] Any rental beyond the 17th package is pure net profit! Linear cost models allow business owners in Bozeman to plan their break-even points with absolute precision and make smart hiring decisions!

[Prof. Park] If Kim expects a busy holiday weekend in December, he can immediately calculate whether hiring a second part-time worker will generate enough additional rental volume to exceed the extra wage cost. Math turns gut feelings into profitable business strategy!""",

    4: r"""[Prof. Park] Now turn to Example 2 Part 1 on page 53: Car Depreciation Model.
You purchased a reliable all-wheel-drive vehicle in Bozeman in the year 2023 for **$22,500**. You learned that the car **depreciates (loses value) by $1,500 each year**.

[TA Sora] Let us construct a linear model for the car's resale value over time!
Step 1: Define our variables:
Let $t$ represent the **time in years since purchase** (where $t = 0$ corresponds to 2023).
Let $V(t)$ represent the **current resale value of the car in dollars**.

[Prof. Park] Step 2: Identify the initial purchase value ($b$):
At time $t = 0$ (the year 2023), the car was purchased brand new for $\$22,500$.
Therefore, the $y$-intercept is:
$$b = 22{,}500$$

[TA Sora] Step 3: Identify the rate of depreciation ($m$):
The problem states: 'loses value by $1,500 each year.'
Look at that word 'loses!' That means the car's value is DECREASING!
When a quantity decreases over time, its slope MUST be negative:
$$m = -1{,}500$$

[Prof. Park] Step 4: Assemble the linear depreciation function:
$$\mathbf{V(t) = -1{,}500t + 22{,}500}$$

[TA Sora] Look at how cleanly that formula captures the vehicle's financial life!
At $t = 1$ year (2024): $V(1) = -1500(1) + 22500 = \$21{,}000$.
At $t = 2$ years (2025): $V(2) = -1500(2) + 22500 = \$19{,}500$.
In Montana, vehicles experience wear and tear from winter road salt, gravel roads in Gallatin Canyon, and sub-zero cold starts. Depreciation is a real expense every vehicle owner must budget for!

[Prof. Park] In accounting and tax preparation, straight-line depreciation is the standard method permitted by the IRS for business vehicle write-offs. Knowing how to write and graph this linear equation gives you practical personal finance literacy!

[TA Sora] On Slide 5, let us determine when the car's book value drops all the way to zero!""",

    5: r"""[Prof. Park] On Slide 5, we analyze Example 2 Part 2 on page 53: Using $V(t) = -1{,}500t + 22{,}500$, determine **when the car's value reaches $0$**, and graph the depreciation function.

[TA Sora] Look at the question carefully: 'when does the value reach zero?'
What is zero here? The VALUE is zero! That means the OUTPUT $V(t) = 0$!
This is a solving problem, NOT an evaluating problem!
We set the entire formula equal to 0:
$$-1{,}500t + 22{,}500 = 0$$

[Prof. Park] Let us solve for $t$ step by step:
Add $1{,}500t$ to both sides to make the variable term positive:
$$22{,}500 = 1{,}500t$$
Divide both sides by $1{,}500$:
$$t = \frac{22{,}500}{1{,}500} = \frac{225}{15} = 15$$
Therefore:
$$\mathbf{t = 15 \text{ years}}$$

[TA Sora] What calendar year does that represent?
Since $t = 0$ was 2023:
$$\text{Year} = 2023 + 15 = \mathbf{2038}$$
In the year 2038, after 15 years of driving on Montana mountain roads and gravel highways, the vehicle's book value will reach zero!

[Prof. Park] Now look at the graph on your screen!
The line starts high up at $(0, 22500)$ on the vertical axis (the purchase price).
It slopes steadily downward with slope $m = -1500$.
It hits the horizontal axis at $(15, 0)$—our $x$-intercept!
Notice that in the real world, the graph STOPS at $t = 15$. A car's value cannot drop below zero into negative dollars!
So the practical **Domain** is $[0, 15]$ years, and the practical **Range** is $[0, 22{,}500]$ dollars! Practical boundaries protect models from absurd extrapolation!

[TA Sora] Even if the car still runs in 2038, for tax and insurance accounting, its book asset value is fully depreciated! This is why businesses sell company trucks every 5 to 7 years to capture remaining residual value!""",

    6: r"""[Prof. Park] Turn to page 54 for Example 3 Part 1: Automobile Salesperson Commission Points.
A salesperson at a dealership in Bozeman earns a weekly salary plus commission on car sales.
In a week where she sold **3 cars**, her total paycheck was **$850**.
In another week where she sold **5 cars**, her total paycheck was **$1,250**.

[TA Sora] Notice how this real-world problem is structured!
Are we given the slope directly? No!
Are we given the base salary ($y$-intercept) directly? No!
What are we given? We are given **TWO DATA POINTS**!
Let us translate the English story into mathematical ordered pairs $(x, y)$:
Let $x$ represent the **number of cars sold**.
Let $E(x)$ represent the **weekly earnings in dollars**.

[Prof. Park] Let us write out our two coordinate points:
When $x = 3$ cars, earnings are $\$850$:
$$\text{Point 1: } (x_1, y_1) = (3, 850)$$
When $x = 5$ cars, earnings are $\$1,250$:
$$\text{Point 2: } (x_2, y_2) = (5, 1250)$$

[TA Sora] Look at that: We have two points on a line! $(3, 850)$ and $(5, 1250)$.
And what did we learn in Lectures 20 and 22? Whenever you have two points, you can construct the entire linear equation using the slope formula and Point-Slope Form!

[Prof. Park] Think about what this means for a job applicant in Bozeman: when an employer says 'you earn commission on sales,' you can take two sample weeks and calculate your exact base pay and commission rate! Mathematics empowers you in contract negotiations!

[TA Sora] Many sales positions in Montana offer a 'base draw plus commission' compensation package. Being able to extract the rate per sale and base salary from your paystubs ensures you are being paid accurately according to your agreement!

[Prof. Park] On Slide 7, let us find her commission per car and her base weekly salary!""",

    7: r"""[Prof. Park] On Slide 7, we execute Example 3 Part 2 on page 54: Finding the Linear Function $E(x)$ representing weekly earnings when $x$ cars are sold.

[TA Sora] Step 1: Find the slope $m$ (the commission per car) between $(3, 850)$ and $(5, 1250)$:
$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{1250 - 850}{5 - 3}$$
In the numerator: $1250 - 850 = 400$.
In the denominator: $5 - 3 = 2$.
$$m = \frac{400}{2} = 200$$
Look at what that slope means in real life: The salesperson earns a **commission of $200 per car sold**!

[Prof. Park] Step 2: Now find her base weekly salary ($b$) using Point-Slope Form with point $(3, 850)$ and $m = 200$:
$$y - y_1 = m(x - x_1)$$
$$y - 850 = 200(x - 3)$$
Distribute the 200:
$$y - 850 = 200x - 600$$
Add 850 to both sides to isolate $y$:
$$y = 200x - 600 + 850 \implies y = 200x + 250$$

[TA Sora] Step 3: Write in function notation:
$$\mathbf{E(x) = 200x + 250}$$
Look at what that $y$-intercept $b = 250$ represents: Even if she sells ZERO cars ($x = 0$), she still earns a **base guaranteed salary of $250 per week**!

[Prof. Park] Now let us evaluate for a stellar week where she sells 8 cars:
$$E(8) = 200(8) + 250 = 1600 + 250 = \mathbf{\$1{,}850!}$$
Two data points unlocked her entire compensation structure! She can budget her living expenses in Bozeman with total financial confidence!

[TA Sora] Notice how algebra connects two scattered observations into a permanent formula that predicts any future week. That is the magic of linear modeling!""",

    8: r"""[Prof. Park] On Slide 8, we present the Section 2.7 Part 1 Real-World Modeling Master Summary.

[TA Sora] Here are your core modeling takeaways:
1. **Rate = Slope ($m$):**
   Look for unit rates like dollars per hour, loss per year, or miles per gallon. Increasing quantities have $m > 0$; decreasing quantities have $m < 0$.
2. **Initial Condition = $y$-Intercept ($b$):**
   Look for the starting baseline at time zero: flat rental fees, initial car purchase price, base salary.
3. **Two-Point Scenarios:**
   If you are given two real-world observations $(x_1, y_1)$ and $(x_2, y_2)$, compute $m = \frac{y_2 - y_1}{x_2 - x_1}$, deploy point-slope form, and solve for $y$!

[Prof. Park] 4. **Evaluating vs Solving in Word Problems:**
   - If they give you the input (e.g., 'find cost for 25 hours'), plug in $x = 25$!
   - If they give you the target outcome (e.g., 'when is value zero?'), set $f(x) = 0$ and solve for $x$!

[TA Sora] Modeling gives you the power to translate English stories into actionable algebraic formulas that make predictions about the future!

[Prof. Park] Whether in agriculture, personal finance, healthcare, or business leadership across Montana, linear modeling is the tool that transforms raw numbers into wisdom and successful decision-making!

[TA Sora] In Lecture 30, we conclude Unit 2 with advanced modeling—blood pressure, Bozeman boiling points, Montana grain storage—and the Grand Unit 2 Synthesis! See you in our final Unit 2 lecture!"""
}

SCRIPTS_L30 = {
    1: r"""[Prof. Park] Welcome to Lecture 30 of M090! Today on pages 54 and 55 of your workbook, we conclude Unit 2 with advanced real-world modeling and the Grand Synthesis of our entire coordinate geometry curriculum.

[TA Sora] Let us begin on page 54 with Example 4: Adult Systolic Blood Pressure Modeling.
Medical researchers have determined that for adults, average systolic blood pressure $P(x)$ (measured in millimeters of mercury, $\text{mmHg}$) can be modeled as a linear function of age $x$ (in years):
$$\mathbf{P(x) = \frac{1}{2}x + 110}$$

[Prof. Park] Let us examine the clinical parameters of this linear function:
- Look at the slope: $m = \frac{1}{2} = 0.5$. In medicine, this means that as blood vessels naturally lose elasticity over time, average systolic blood pressure increases at a rate of **half a millimeter of mercury per year** (or $1\text{ mmHg}$ every two years).
- Look at the $y$-intercept: $b = 110$. In this model, $110\text{ mmHg}$ represents the theoretical baseline blood pressure for a young adult entering maturity at age zero of adulthood.

[TA Sora] Let us evaluate Question A: 'Find the average systolic blood pressure for a **30-year-old** adult.'
Here, the age is the input: $x = 30$.
We evaluate $P(30)$:
$$P(30) = \frac{1}{2}(30) + 110 = 15 + 110 = \mathbf{125\text{ mmHg}}$$
As an ordered pair, this is $(30, 125)$.

[Prof. Park] Now evaluate Question B: 'Find the average blood pressure for a **60-year-old** adult.'
We evaluate $P(60)$:
$$P(60) = \frac{1}{2}(60) + 110 = 30 + 110 = \mathbf{140\text{ mmHg}}$$

[TA Sora] Now Question C asks a solving question: 'At what age would an adult have an average systolic blood pressure of **135 mmHg**?'
Here, 135 is the output: $P(x) = 135$!
$$\frac{1}{2}x + 110 = 135$$
Subtract 110 from both sides:
$$\frac{1}{2}x = 25$$
Multiply both sides by 2:
$$x = 50\text{ years old!}$$
At age 50, average systolic blood pressure is $135\text{ mmHg}$!

[Prof. Park] In healthcare careers at Bozeman Health Deaconess Hospital, medical practitioners use these baseline models to spot hypertension early. If a 30-year-old patient registers $150\text{ mmHg}$, the practitioner immediately recognizes an abnormal deviation from the expected linear baseline and intervenes with dietary and lifestyle counseling!""",

    2: r"""[Prof. Park] Now turn to page 55 for one of the most fascinating physical science applications in all of Montana: Example 5 Part 1, Bozeman Elevation versus the Boiling Point of Water!

[TA Sora] If you have ever tried to boil pasta or can fresh elk meat in Bozeman, you know it takes significantly longer than it does at sea level in Seattle or New York! Why? Because Bozeman sits nearly a mile high in the Rocky Mountains! As elevation increases, atmospheric air pressure decreases, which allows water molecules to escape into steam at a lower temperature!

[Prof. Park] Let us look at the given scientific data:
1. At **sea level ($0\text{ feet}$)**, water boils at **$212^\circ\text{F}$**.
2. At an **elevation of $5{,}000\text{ feet}$**, water boils at **$203^\circ\text{F}$**.
Let us translate these two observations into ordered pairs $(x, y)$:
Let $x$ represent the **elevation in feet above sea level**.
Let $B(x)$ represent the **boiling point of water in degrees Fahrenheit**.

[TA Sora] Let us write out our two coordinate points:
At sea level ($x = 0$), temperature is $212$:
$$\text{Point 1: } (x_1, y_1) = (0, 212)$$
Notice that because $x = 0$, $(0, 212)$ is our **$y$-intercept** $b = 212$!
At elevation $5{,}000$, temperature is $203$:
$$\text{Point 2: } (x_2, y_2) = (5000, 203)$$

[Prof. Park] Now compute the slope $m$ (the rate of temperature drop per foot of elevation):
$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{203 - 212}{5000 - 0} = \frac{-9}{5000}$$
Convert that fraction to a decimal:
$$m = -0.0018^\circ\text{F per foot}$$
Every foot you climb into the Montana sky, the boiling point of water drops by $0.0018$ degrees Fahrenheit!

[TA Sora] That negative sign makes total sense: As elevation goes UP, boiling point goes DOWN! In aviation, barometric altimeters inside aircraft cockpits flying into Bozeman Yellowstone International Airport use this exact pressure-altitude relationship to calculate true height above ground! On Slide 3, we construct our boiling point function!""",

    3: r"""[Prof. Park] On Slide 3, we execute Example 5 Part 2 on page 55: Writing the Boiling Point Function $B(x)$ and evaluating it for the city of Bozeman!

[TA Sora] Let us assemble our function from Slide 2:
We have our slope $m = -0.0018$ and our $y$-intercept $b = 212$:
$$\mathbf{B(x) = -0.0018x + 212}$$
Look at how elegant that formula is!
Now let us answer: 'What is the boiling point of water in downtown **Bozeman**, which sits at an elevation of approximately **$4{,}800\text{ feet}$**?'

[Prof. Park] The elevation of Bozeman is our input: $x = 4{,}800\text{ feet}$!
Let us evaluate $B(4800)$:
$$B(4800) = -0.0018(4800) + 212$$
Multiply $-0.0018$ by $4{,}800$:
$$-0.0018 \times 4800 = -8.64$$
Now add 212:
$$-8.64 + 212 = \mathbf{203.36^\circ\text{F}}$$

[TA Sora] That is nearly **9 degrees cooler** than boiling water at sea level!
When you boil water in Bozeman, it bubbles vigorously at just $203.4^\circ\text{F}$. Because the water is 9 degrees cooler, food cooks more slowly, which is why recipes printed on pasta boxes and cake mixes include special 'High Altitude Cooking Instructions!'

[Prof. Park] And what if you are camping at the summit of Sacajawea Peak in the Bridger Range at $9{,}600\text{ feet}$?
$$B(9600) = -0.0018(9600) + 212 = -17.28 + 212 = 194.72^\circ\text{F}!$$
At the mountain summit, water boils below $195^\circ\text{F}$! In sterilization autoclaves at mountain clinics, medical instruments must be heated under pressure to reach proper sterilization temperatures. Linear models explain physical reality across the Rocky Mountain West!""",

    4: r"""[Prof. Park] Turn to page 55 for Example 6 Part 1: Montana Grain Bin Storage Depletion.
Agriculture is the foundation of Montana's economy. In the year **2001**, the volume of grain stored in a large ranch silo near Great Falls was **45 tons**. By the year **2005**, regular shipments and livestock feeding had reduced the volume to **27 tons**.

[TA Sora] Let us establish our linear variables:
Let $t$ represent the **time in years since 2001** (so $t = 0$ corresponds to 2001).
Let $V(t)$ represent the **remaining volume of grain in tons**.
Let us translate our historical data into two ordered pairs $(t, V)$:
In 2001 ($t = 0$), volume was 45 tons:
$$\text{Point 1: } (0, 45) \implies b = 45\text{ tons (our } y\text{-intercept!)}$$
In 2005 ($t = 2005 - 2001 = 4\text{ years}$), volume was 27 tons:
$$\text{Point 2: } (4, 27)$$

[Prof. Park] Now let us compute the slope $m$ (the annual rate of grain depletion):
$$m = \frac{V_2 - V_1}{t_2 - t_1} = \frac{27 - 45}{4 - 0}$$
In the numerator: $27 - 45 = -18\text{ tons}$.
In the denominator: $4 - 0 = 4\text{ years}$.
$$m = \frac{-18}{4} = -4.5\text{ tons per year}$$

[TA Sora] What does $m = -4.5$ tell the ranch manager?
Every single year, the silo loses $4.5$ tons of grain!
Now assemble the linear storage function:
$$\mathbf{V(t) = -4.5t + 45}$$

[Prof. Park] In Montana's Golden Triangle—the premier wheat-growing region stretching from Great Falls to Havre and Conrad—grain storage managers monitor silo levels continuously. Tracking depletion rates allows cooperatives to book freight rail cars on the BNSF railway months in advance to ensure smooth grain export to Pacific Rim ports!

[TA Sora] On Slide 5, let us determine when the grain bin will be completely empty!""",

    5: r"""[Prof. Park] On Slide 5, we complete Example 6 Part 2 on page 55: Determining **when the grain bin will be completely empty**.

[TA Sora] What does 'empty' mean in mathematical terms?
An empty bin has a volume of ZERO!
Therefore, the output $V(t) = 0$!
This is a solving problem:
$$-4.5t + 45 = 0$$

[Prof. Park] Let us isolate $t$:
Add $4.5t$ to both sides:
$$45 = 4.5t$$
Divide both sides by $4.5$:
$$t = \frac{45}{4.5} = \mathbf{10\text{ years}}$$

[TA Sora] What calendar year will that be?
Since $t = 0$ was 2001:
$$\text{Year} = 2001 + 10 = \mathbf{2011}$$
In the year 2011, the grain silo will be completely depleted!

[Prof. Park] Look at the graph on your screen:
The graph starts at $(0, 45)$ on the vertical axis (45 tons).
It slopes downward at a rate of $-4.5$ tons per year.
It intersects the horizontal time axis at $(10, 0)$—our $x$-intercept!
The practical **Domain** is $[0, 10]$ years, and the practical **Range** is $[0, 45]$ tons.
Linear functions give farmers and resource managers the ability to foresee depletion years in advance and schedule resupply shipments!

[TA Sora] Real-world models always have domain boundaries. If you plugged in $t = 12$ years, the formula would predict $-9$ tons of grain! But a silo cannot hold negative wheat. Always define the valid physical domain of your model!""",

    6: r"""[Prof. Park] On Slide 6, we step back and view the Master Principles of Unit 2: The Linear Universe. Over the past 15 lectures, we have built a complete, interconnected mathematical world.

[TA Sora] Let us review the foundational pillars we have mastered:
1. **The Cartesian Plane (Section 2.0):**
   Origin $(0, 0)$, $x$-axis (horizontal), $y$-axis (vertical), four quadrants counterclockwise. Points $(x, y)$—walk the hallway before taking the elevator!
2. **Graphing Lines (Section 2.1):**
   Standard Form $Ax + By = C$. Three graphing methods: Table of values, Intercepts (Cover-up method), and Slope-Intercept.
3. **The Slope of a Line (Section 2.2):**
   $m = \frac{\Delta y}{\Delta x} = \frac{\text{Rise}}{\text{Run}} = \frac{y_2 - y_1}{x_2 - x_1}$. Four types of slope: Positive (uphill), Negative (downhill), Zero (horizontal), Undefined (vertical).

[Prof. Park] 4. **Parallel & Perpendicular Lines (Section 2.2):**
   Parallel lines share equal slopes ($m_1 = m_2$). Perpendicular lines have negative reciprocal slopes ($m_1 \cdot m_2 = -1$).
5. **Writing Equations (Section 2.3):**
   Point-Slope Form: $y - y_1 = m(x - x_1)$. The universal construction tool!
6. **Relations & Functions (Section 2.4):**
   Domain (inputs), Range (outputs). A function assigns each input exactly one output (passes VLT!).
7. **Function Notation & Modeling (Sections 2.5–2.7):**
   $y = f(x)$, evaluating $f(a)$ vs solving $f(x) = b$. Real-world rate modeling: $f(x) = mx + b$.

[TA Sora] Every single concept connected seamlessly into the next! When you build a house on a solid foundation, every wall stands true!

[Prof. Park] And think of the mindset shift: in Unit 1, you learned how to manipulate isolated symbols. In Unit 2, you learned how to visualize cause and effect in two-dimensional space. That ability to see the geometric consequences of an algebraic formula is what transforms students into true problem solvers!""",

    7: r"""[Prof. Park] On Slide 7, we present the Master Coordinate Grid: Visualizing Every Line Family simultaneously on a single canvas!

[TA Sora] Look at how all forms of lines coexist in the coordinate plane:
1. **Standard Rising Line ($m > 0$):** Slants uphill from southwest to northeast.
2. **Standard Falling Line ($m < 0$):** Slants downhill from northwest to southeast.
3. **Horizontal Line ($y = c$):** Flat level line, slope $m = 0$, passes VLT (HOY).
4. **Vertical Line ($x = k$):** Vertical cliff, slope undefined, fails VLT (VUX).
5. **Parallel Pair:** Dual tracks that never intersect, identical slopes $m_1 = m_2$.
6. **Perpendicular Pair:** Meeting at a true 90-degree right angle, $m_1 \cdot m_2 = -1$.

[Prof. Park] Notice how geometry and algebra are two languages describing the exact same underlying reality. When you look at an equation like $y = -2x + 7$, your mind should instantly see a line crossing at 7 and plunging downhill twice as fast as it runs forward.

[TA Sora] That visual intuition is what separates struggling students from confident, fluent mathematicians. When you can see the line before you draw it, algebra becomes a creative art!

[Prof. Park] Think of architectural drafting or video game design: game engines render entire 3D worlds by computing millions of intersecting lines and polygons every second using these exact coordinate formulas! You are mastering the visual engine of modern computing!""",

    8: r"""[Prof. Park] On Slide 8, we celebrate an immense academic milestone: You have officially mastered Unit 2 of M090 Introductory Algebra! Give yourselves a tremendous round of applause!

[TA Sora] Let us take stock of where you stand in the curriculum:
- **Unit 1 Conquered:** Signed numbers, fractions, algebraic expressions, linear equations in one variable, and interval notation!
- **Unit 2 Conquered:** The Cartesian coordinate plane, slopes, intercepts, line construction, relations, functions, and real-world linear modeling!
You have completed two full units—that is two-thirds of the foundational material of introductory algebra!

[Prof. Park] Look ahead to what awaits you in **Unit 3**:
In Unit 3, we leave straight lines behind and enter the dynamic, curved world of **Quadratic Functions and Polynomials**! We will explore parabolas, projectile motion, factoring, the quadratic formula, vertex optimization, and business revenue maximization!

[TA Sora] Everything you learned in Unit 2—plotting points, evaluating functions, understanding domain and range, finding intercepts—is the exact foundation that makes Unit 3 intuitive and exciting!

[Prof. Park] Review your workbook pages 30 through 55, take pride in how far your mathematical abilities have grown, and remember: with disciplined practice and systematic thinking, there is no mathematical problem you cannot conquer!

[TA Sora] We are so proud of your dedication and hard work throughout Unit 2. Rest up, celebrate this victory, and we will see you in Unit 3! Go Bobcats!"""
}

# Extra enrichments for L30
SCRIPTS_L30_EXP = dict(SCRIPTS_L30)
SCRIPTS_L30_EXP[1] = SCRIPTS_L30[1] + """\n\n[TA Sora] In cardiovascular fitness, regular aerobic training like trail running in the Gallatin foothills can actually flatten this slope! If a 60-year-old runner maintains a blood pressure of 120, their biological vascular age functions like a 20-year-old! Linear models quantify the benefits of healthy living!"""
SCRIPTS_L30_EXP[2] = SCRIPTS_L30[2] + """\n\n[Prof. Park] At the top of Mount Everest (29,032 feet), air pressure is one-third of sea level, and water boils at a chilly 160 degrees Fahrenheit—so cold that you cannot even brew hot coffee! Pressure and temperature are bound by thermodynamics!"""
SCRIPTS_L30_EXP[4] = SCRIPTS_L30[4] + """\n\n[TA Sora] In Montana agriculture, wheat grain bins are equipped with digital moisture and temperature cables: when the volume decreases at $-4.5$ tons per year, farmers can balance livestock winter feeding rations with commercial export sales!"""
SCRIPTS_L30_EXP[5] = SCRIPTS_L30[5] + """\n\n[Prof. Park] Solving for the $t$-intercept ($V=0$) gives the exact horizon date: 10 years after 2001 is 2011! Mathematical modeling transforms raw data into actionable life planning!"""
SCRIPTS_L30_EXP[6] = SCRIPTS_L30[6] + """\n\n[Prof. Park] When you reflect on Unit 2, realize that you now possess the mathematical literacy to understand scientific papers, economic reports, and engineering blueprints. You can look at raw data and extract the underlying linear equations that govern the phenomenon!"""
SCRIPTS_L30_EXP[7] = SCRIPTS_L30[7] + """\n\n[TA Sora] Think of this master grid as your mathematical toolbox: whenever a problem appears on an exam, you identify which line family it belongs to, grab the appropriate formula, and execute with total confidence!"""

