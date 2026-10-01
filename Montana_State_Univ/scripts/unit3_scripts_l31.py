# -*- coding: utf-8 -*-
"""
unit3_scripts_l31.py
Full 20-25 Minute Broadcast Tiki-Taka Dialogue for Lecture 31
Prof. Eunju Park & TA Sora (Gallatin College Montana State University)
Covers all 8 slides with ~320-380 words per slide (~2,600-2,900 total words).
"""

SCRIPTS_L31 = {
    1: """[Prof. Park] Hello everyone, and welcome to Unit 3 of M090 Introductory Algebra here at Gallatin College, Montana State University! I'm Professor Eunju Park, and joining me as always is our wonderful teaching assistant, Sora. Sora, can you believe we are already entering Unit 3?

[TA Sora] Welcome, Bobcats! Yes, Professor Park, it feels like just yesterday we were defining integers in Unit 1 and graphing straight ski slopes in Unit 2. But Unit 3 is truly where algebra comes to life because nature and real human experiences rarely move in rigid straight lines—they curve!

[Prof. Park] Exactly right. In Unit 2, every equation was linear: $y = mx + b$. If you walked at a steady pace down Main Street in Bozeman, that was a line. But what happens when you throw a baseball, when water arches out of a Yellowstone geyser, or when a ski jumper launches off the ramp at Bridger Bowl? Gravity takes over, and the path bends into a graceful symmetrical curve known as a parabola.

[TA Sora] That's one of my favorite things about quadratics. Whether you are studying nursing and calculating drug dosage curves, studying aviation at Gallatin College and analyzing flight glide paths, or working in carpentry and designing arched roof trusses that can withstand heavy Montana winter snow loads, quadratic functions are everywhere.

[Prof. Park] That brings us to our core mathematical formula for this unit: the General Form of a Quadratic Function, $f(x) = ax^2 + bx + c$, where $a \\neq 0$. Notice that the highest exponent on the variable $x$ is 2. That single exponent of 2 changes everything.

[TA Sora] And students, please make a big note right here on page 60 of your workbook: $a$ cannot equal 0. Professor Park, why is that condition so crucial?

[Prof. Park] Think about it, Sora: if $a$ were 0, the $ax^2$ term would completely vanish, leaving us with just $bx + c$. That would demote our curved parabola back down to a straight line! We need that $x^2$ term alive and kicking.

[TA Sora] So throughout this entire lecture, keep your eyes open for that $x^2$ power. Take a deep breath, grab your pencil and workbook, and let's explore the anatomy of these beautiful curves together!""",

    2: """[Prof. Park] Let's look at Slide 2 and examine the precise anatomy of our general quadratic form: $f(x) = ax^2 + bx + c$. Just like a builder inspects the foundation, framing, and roof of a house before construction, we must distinguish between the algebraic terms and their numerical coefficients.

[TA Sora] This is where many students lose easy points on their first exam, so let's clarify the terminology right away. An algebraic 'term' includes both the number and the variable part, while a 'coefficient' is strictly the multiplying number sitting in front of that variable!

[Prof. Park] Beautifully put, Sora. Let's break down the three parts: First, the quadratic term is $ax^2$, and its coefficient is $a$. Second, the linear term is $bx$, with coefficient $b$. And third, the constant term is $c$, which has no variable attached to it.

[TA Sora] Professor Park, let's connect this to real-world financial planning. Suppose you run a small business in Bozeman, like a local food truck or custom fly-fishing rod workshop. Your total profit function often looks like $P(x) = -2x^2 + 80x - 300$, where $x$ is the price you charge.

[Prof. Park] What a great real-life model, Sora! Look at the parts: the $-300$ is your constant overhead cost—rent, insurance, permits you pay even if you sell zero items. The $80x$ represents revenue coming in per customer. And the $-2x^2$ quadratic term reflects diminishing returns—if you price your rods too high, customer demand drops off!

[TA Sora] Exactly! The quadratic term dictates the curve of profit reaching a peak and then falling. That's why understanding which number plays which role is essential not just for passing M090, but for making sound business and engineering decisions.

[Prof. Park] And always remember: keep the sign attached to the coefficient! If a term is written as $-7x$, the coefficient is $-7$, not positive 7. 

[TA Sora] Yes! Treat the minus sign like a backpack that the number wears wherever it travels. Let's turn to page 60 in the workbook and put this into practice on Example 1!""",

    3: """[Prof. Park] Now we arrive at our first official workbook problem on Slide 3: Section 3.0 Example 1 on page 60. The problem asks: For the function $f(x) = -x^2 + 3x + 8$, identify the quadratic term, its coefficient, the linear term, its coefficient, and the constant term.

[TA Sora] Look at that first term: $-x^2$. Professor Park, every semester at the Gallatin tutoring center, I see students write down that the coefficient is 0, or they just write down a lonely minus sign! How should students read $-x^2$?

[Prof. Park] That is what I call 'the invisible 1' trap! When you see $-x^2$, there is an understood 1 between the negative sign and the variable: it is $(-1)x^2$. So the quadratic term is $-x^2$, and its numerical coefficient is $a = -1$. Never leave a coefficient as just a minus sign, and never call it zero!

[TA Sora] What a great reminder. If the coefficient were zero, the term wouldn't exist at all. Moving to the middle term, we have $+3x$. The linear term is $3x$, and its coefficient is $b = 3$. And finally, the standalone number at the end is the constant term, $c = 8$.

[Prof. Park] Now take a glance at the Cartesian coordinate plane on the right side of your screen. Because $a = -1$, which is a negative number, the parabola curves downward like an umbrella or an arch bridge over the Madison River. Notice how the highest peak—the vertex—sits up at $(1.5, 10.25)$.

[TA Sora] And look at where the curve crosses the vertical $y$-axis: right at $(0, 8)$! Notice that the $y$-intercept matches the constant term $c = 8$ exactly! That is not a coincidence, Bobcats. When you plug in $x = 0$, both variable terms vanish, leaving only $c$.

[Prof. Park] Connecting the algebraic equation directly to its visual picture on the coordinate plane builds lasting intuition. Don't just memorize the labels; picture the graph in your mind as you identify each coefficient.

[TA Sora] Double check your workbook notes: Quadratic term is $-x^2$ with coefficient $-1$; linear term is $3x$ with coefficient $3$; constant term is $8$. All three confirmed!""",

    4: """[Prof. Park] Let's turn to Section 3.0 Example 2 on Slide 4: $f(x) = 2x^2 - 7$. At first glance, this function looks shorter than the previous one. Sora, what is missing here?

[TA Sora] There is no $x$ term in the middle! We have $2x^2$, and then we jump straight to $-7$. A lot of students get nervous and write 'none' or leave the linear coefficient blank on their worksheet. But in mathematics, absence is represented by a very specific number.

[Prof. Park] Precisely. The number that represents nothingness or absence is zero. We can rewrite $f(x) = 2x^2 - 7$ in complete standard form as $f(x) = 2x^2 + 0x - 7$. Writing in that placeholder of $0x$ makes the structure transparent.

[TA Sora] So the quadratic term is $2x^2$ with coefficient $a = 2$. The linear term is $0x$ (or none) with coefficient $b = 0$. And the constant term is $-7$, keeping that negative sign firmly attached.

[Prof. Park] Now look at the graph on your right! The leading coefficient is $a = 2$, which is positive ($a > 0$). Therefore, the parabola opens upward like a soup bowl or a satellite dish catching signals up in the Montana mountains.

[TA Sora] And notice where the lowest point—the vertex—sits: right on the $y$-axis at $(0, -7)$! Because $b = 0$, the parabola doesn't shift left or right at all; its vertical line of symmetry is the $y$-axis itself, $x = 0$. 

[Prof. Park] This has immediate practical applications. If you are an engineer designing a parabolic solar collector or headlight reflector, having $b = 0$ means your focal point is centered perfectly along the axis of symmetry, simplifying manufacturing costs.

[TA Sora] That is so satisfying. When a term is missing, its coefficient is 0. Write that in bold letters in your workbook margin: Missing linear term means $b = 0$, not undefined!""",

    5: """[Prof. Park] Slide 5 brings us to Example 3: $f(x) = 5 - 2x + 4x^2$. Sora, this is a classic textbook trap designed to test whether students are truly paying attention or just skimming from left to right.

[TA Sora] Yes! The biggest mistake here is assuming that whatever number comes first must be $a$. Students see 5 first and write $a = 5$, then $b = -2$, and $c = 4$. But algebra doesn't care about the order you write them; it cares about the powers attached to the variable!

[Prof. Park] Exactly. Standard general form is always arranged in descending order of exponents: power of 2 first, then power of 1, then power of 0 (the constant). So before doing any identification, our golden rule is: rearrange the terms into descending order first!

[TA Sora] Let's do that together right now. Take the $4x^2$ and bring it to the front. Then take the $-2x$ and place it in the middle. Finally, take the positive 5 and place it at the end: $f(x) = 4x^2 - 2x + 5$.

[Prof. Park] Now the coefficients reveal themselves cleanly: $a = 4$, $b = -2$, and $c = 5$. Notice how drastically different $a = 4$ is from the mistaken $a = 5$. Since $a = 4 > 0$, this parabola opens upward and is relatively narrow and steep because 4 stretches the graph vertically.

[TA Sora] This teaches us a valuable life habit as well. When you face a chaotic problem in your daily schedule, budgeting, or work projects, you can't just react to whichever item caught your eye first. You have to organize and prioritize your tasks in order before you start solving them!

[Prof. Park] That's the mindset of a successful student and professional. Order brings clarity. Always rewrite your quadratic expression in descending order: $ax^2 + bx + c$.

[TA Sora] So for Example 3: descending order gives $f(x) = 4x^2 - 2x + 5$. Quadratic term $4x^2$ with $a = 4$; linear term $-2x$ with $b = -2$; constant term 5 with $c = 5$. Perfectly organized!""",

    6: """[Prof. Park] On Slide 6, Example 4 asks us to compare two functions side-by-side: $f(x) = 3x - 4$ versus $g(x) = 3x^2 - 4$. Sora, why did the MSU course designers include this comparison right here in Section 3.0?

[TA Sora] Because one little exponent of 2 completely transforms the algebraic universe we are living in! Let's examine $f(x) = 3x - 4$. What is the highest power on $x$? It's an exponent of 1 ($x^1$). That makes $f(x)$ a Linear Function, exactly like the ones we mastered in Unit 2.

[Prof. Park] Right. The graph of $f(x) = 3x - 4$ is a straight line with a constant slope of $m = 3$ and a $y$-intercept at $(0, -4)$. Its rate of change never varies. For every 1 step you walk to the right, you climb 3 steps up, forever and ever.

[TA Sora] But look at $g(x) = 3x^2 - 4$! The variable $x$ is squared. That makes $g(x)$ a Quadratic Function of degree 2. Its graph is not a straight line at all—it is a curved parabola with a vertex at $(0, -4)$.

[Prof. Park] And think about the rate of change! In $g(x)$, as $x$ increases, the output doesn't grow at a constant rate; it accelerates! When $x = 1$, $g(1) = -1$. When $x = 2$, $g(2) = 8$. When $x = 3$, $g(3) = 23$! The curve gets steeper and steeper. That is quadratic growth.

[TA Sora] This distinction is vital in finance and economics. Simple interest grows linearly like $3x - 4$. But compound interest, kinetic energy in a moving vehicle ($E = \\frac{1}{2}mv^2$), and braking distance when driving on icy Montana highways in January grow quadratically!

[Prof. Park] That's a life-saving example, Sora. If you double your driving speed from 30 mph to 60 mph on ice, your stopping distance doesn't just double—it quadruples because kinetic energy depends on $v^2$!

[TA Sora] So remember: degree 1 is linear (straight line, constant slope); degree 2 is quadratic (curved parabola, accelerating rate of change). Check the exponent before you classify!""",

    7: """[Prof. Park] Let's move to Slide 7, which explores one of the most visual and intuitive properties of any parabola: its direction of opening. Whether a parabola opens upward or downward is dictated entirely by a single sign—the sign of our leading coefficient $a$.

[TA Sora] Here is Sora's memory trick that students at Gallatin College love: Think of the parabola as a smile or a frown! When $a > 0$ (positive, optimistic attitude), the parabola smiles upward like a U-shape! When $a < 0$ (negative, pessimistic attitude), the parabola frowns downward like an upside-down U!

[Prof. Park] That is unforgettable, Sora! Let's look at the mathematical consequences of that smile and frown. When $a > 0$ and the parabola opens upward, the vertex represents the lowest possible valley on the curve. In mathematical terms, the vertex gives us the Minimum value of the function.

[TA Sora] And conversely, when $a < 0$ and the parabola opens downward, the curve climbs to a peak and then descends. That means the vertex represents the Maximum value of the function!

[Prof. Park] Think about what this means in practical problem-solving. If a rancher in the Gallatin Valley wants to minimize the cost of fencing a pasture, they model the cost with a quadratic where $a > 0$ and look for the minimum at the vertex. If a business wants to maximize revenue, they model revenue with $a < 0$ and look for the maximum at the vertex!

[TA Sora] Look at the two curves plotted side-by-side on your screen right now: the blue curve $y = x^2$ opens upward with vertex at $(0, 0)$ as its absolute minimum. The orange curve $y = -x^2$ opens downward with vertex at $(0, 0)$ as its absolute maximum.

[Prof. Park] The leading coefficient $a$ is the master conductor of the parabola. Its sign determines the direction (up or down), and its magnitude determines how narrow or wide the curve opens.

[TA Sora] Always look at $a$ first: $a > 0$ means opens up with a minimum; $a < 0$ means opens down with a maximum. It takes two seconds to check, and it immediately sets your mental compass!""",

    8: """[Prof. Park] We have reached the final slide of Lecture 31—our Section 3.0 Part 1 Mastery Summary! Let's take a moment to look back at the ground we've covered today and solidify these core principles.

[TA Sora] We started by stepping into Unit 3, transitioning from straight lines into the curved, dynamic world of parabolas. We learned the General Form: $f(x) = ax^2 + bx + c$, where $a \\neq 0$. 

[Prof. Park] We mastered the identification of terms and coefficients: the quadratic term $ax^2$ with coefficient $a$, the linear term $bx$ with coefficient $b$, and the constant term $c$. We warned against the 'invisible 1' in $-x^2$ where $a = -1$, and we learned that missing terms simply have a coefficient of 0.

[TA Sora] And we emphasized the golden rule of organization: always rearrange polynomials into descending order of powers before identifying coefficients, so you never get tricked by scrambled equations. Finally, we learned that the sign of $a$ tells us whether the parabola opens upward with a minimum ($a > 0$) or downward with a maximum ($a < 0$).

[Prof. Park] To all our students watching: math is a skill built one brick at a time. If you struggled with algebra in high school, remember that this is a fresh start. You are building mental muscles that will serve you in your career, your financial life, and your critical thinking every single day.

[TA Sora] Be patient with yourself, write out every step clearly on paper, and never skip the details. Tonight, complete the Section 3.0 practice exercises on pages 60 and 61 of your workbook. 

[Prof. Park] In Lecture 32, we will dive into calculating the exact coordinates of the vertex using the famous Vertex Formula and exploring domain and range. Thank you for your focus and dedication today.

[TA Sora] Keep up the great work, Bobcats! We will see you all in Lecture 32!"""
}
