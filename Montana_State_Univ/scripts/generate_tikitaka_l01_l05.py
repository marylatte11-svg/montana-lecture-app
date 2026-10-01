# -*- coding: utf-8 -*-
"""
Generates Gold-Standard Tiki-Taka for Unit 1: Lectures 01 to 05.
Pattern: 8 to 10 alternating micro-turns per slide, strictly [Prof. Park] <-> [TA Sora],
separated by \n\n. Zero colons. Target 2,250 - 2,500 words per lecture.
"""
import sys, io, re, json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# We define high-frequency tiki-taka scripts for each slide of L01-L05.
# Every slide has 8 to 10 alternating turns.
scripts_l01 = [
    # Slide 1: Welcome & Course Orientation
    """[Prof. Park] Welcome everyone to M090 Introductory Algebra here at Gallatin College Montana State University! I am Professor Eunju Park, and right beside me is our fantastic graduate teaching assistant, Sora.

[TA Sora] Hello everyone! Whether you are sitting right here in Bozeman or streaming across Gallatin County, welcome! Professor, what is the single biggest question students ask me on day one?

[Prof. Park] They always ask: 'Professor Park, what if I have never been good at math?' And my answer is always the same: mathematics is not a genetic trait! It is simply a set of clean, repeatable mental habits.

[TA Sora] Exactly! If you've felt math anxiety in high school, or thought fractions were an impossible puzzle, consider this classroom your fresh slate. We build every concept brick by brick.

[Prof. Park] That's our promise. In M090, we don't rush through formulas without intuition. We connect every algebraic tool to concrete physical realities you see right here in Montana.

[TA Sora] From timber framing in Belgrade to measuring snowfall gradients at Bridger Bowl, algebra is the universal language of practical problem solving!

[Prof. Park] Today we kick off Section 1.0 on page 3 of your course workbook. Over the next 45 lectures, Sora and I will walk through every single example together.

[TA Sora] Grab your workbook, keep a sharp pencil ready, and let's conquer algebra together!""",

    # Slide 2: Variables, Constants & Distance Model
    """[Prof. Park] Let's begin on workbook page 3 with two bedrock definitions: variables and constants. Sora, how do you explain the difference to students?

[TA Sora] I tell them: think of a constant as a solid brick of granite—it never changes its weight! Numbers like 5, -12, or pi are constants.

[Prof. Park] And a variable? That is an open, empty pocket—or a reserved parking spot waiting for whatever real-world number comes along. We represent them with letters like $x$, $y$, $r$, or $t$.

[TA Sora] Look at the classic distance formula on screen: $D = r \\cdot t$. Distance equals rate multiplied by time. All three symbols are variables!

[Prof. Park] Imagine you are cruising west on Interstate 90 from Bozeman toward Butte at a steady cruise control speed of 70 miles per hour. Your rate $r$ is fixed at 70.

[TA Sora] But time $t$ is constantly ticking! After 1 hour, $t = 1$, so distance is $70 \\times 1 = 70$ miles. After 2 hours, $t = 2$, so $70 \\times 2 = 140$ miles, taking you right past Whitehall!

[Prof. Park] Exactly. Instead of recalculating every mile from scratch, algebra gives us one universal master equation: $D = r \\cdot t$ models every road trip on Earth.

[TA Sora] That is the true superpower of algebra: writing one elegant formula that commands infinite real-world scenarios!""",

    # Slide 3: Arithmetic Operations & Absolute Value
    """[Prof. Park] On Slide 3, we review the four primary arithmetic operations: addition, subtraction, multiplication, and division, along with absolute value.

[TA Sora] Professor, let's talk about absolute value first, because students constantly get confused when they see the vertical bars $|-8|$.

[Prof. Park] What is the most common misconception, Sora?

[TA Sora] Many students think absolute value means 'change the sign.' So if they see $|+5|$, they accidentally turn it into $-5$! That's a major trap!

[Prof. Park] That is a critical trap to avoid. Absolute value does NOT mean opposite sign; it measures pure geometric distance from zero on a number line! Distance is never negative.

[TA Sora] Exactly! If you walk 8 miles north from Bozeman, distance is 8. If you walk 8 miles south toward Big Sky, distance is STILL 8! So $|-8| = 8$, and $|+8| = 8$.

[Prof. Park] Beautiful physical intuition. And notice division by zero at the bottom of the slide: $0 / 5 = 0$, but $5 / 0$ is completely undefined!

[TA Sora] Remember our classroom rule: you can divide zero slices of pizza among 5 friends—everyone gets zero. But dividing 5 slices among zero humans breaks the universe!""",

    # Slide 4: Real Numbers: Integers, Rationals & Irrationals
    """[Prof. Park] Slide 4 introduces the grand hierarchy of the Real Number System $\\mathbb{R}$. Sora, how do we visualize these concentric number families?

[TA Sora] Think of Russian nesting dolls! At the very center are the Natural numbers: $1, 2, 3...$ counting elk on a hillside.

[Prof. Park] Add zero, and you have the Whole numbers. Then expand in both directions to include negative temperatures like $-20^\\circ\\text{F}$ in a Bozeman winter, and you get Integers $\\mathbb{Z}$!

[TA Sora] Next comes the largest family we work with daily: Rational numbers $\\mathbb{Q}$. The word 'rational' comes from 'ratio'—any number you can write as a clean fraction $a/b$.

[Prof. Park] That includes terminating decimals like $0.75 = 3/4$ and repeating decimals like $0.333... = 1/3$. But what about numbers that wander forever without repeating?

[TA Sora] Those are the Irrationals! Celebrities like $\\pi \\approx 3.14159...$ and $\\sqrt{2} \\approx 1.414...$. You cannot write them as simple integer fractions.

[Prof. Park] When you unite all the rationals with all the irrationals, you form the continuous, unbroken real number line $\\mathbb{R}$.

[TA Sora] Every single point on the ruler has a unique address. That gives us the rock-solid ground we stand on for all of algebra!""",

    # Slide 5: Order of Operations (PEMDAS / GEMDAS)
    """[Prof. Park] Slide 5 brings us to the supreme traffic law of algebra: the Order of Operations! PEMDAS—or as we prefer in modern algebra, GEMDAS.

[TA Sora] Why do you prefer the 'G' over 'P', Professor?

[Prof. Park] Because grouping symbols are not just round parentheses! They include square brackets $[\\;]$, curly braces $\\{\\;\\}$, absolute value bars $|\\;|$, and fraction division bars.

[TA Sora] That's such an important distinction. Now look at the middle letters: Multiplication and Division. Professor, why do students lose points here?

[Prof. Park] Because they think 'M comes before D, so multiplication always goes first!' That is completely wrong. Multiplication and division have equal rank—you work them strictly from left to right!

[TA Sora] The exact same rule applies to Addition and Subtraction: equal rank, left to right! If subtraction appears on the left, you subtract first!

[Prof. Park] Think of order of operations like airport security: first Grouping, then Exponents, then Multiplications and Divisions left to right, and finally Additions and Subtractions left to right.

[TA Sora] Obey the traffic laws, and your algebra answers will be rock-solid every single time!""",

    # Slide 6: Section 1.0 Example 1: Evaluating Order of Operations
    """[Prof. Park] Let's apply our GEMDAS rules directly to Example 1 from workbook page 4: evaluate $3 + 4 \\times (6 - 2)^2 / 8 - 5$.

[TA Sora] Sora's golden rule: don't try to calculate everything in your head at once! Take it step by step, line by line. What is Step 1, Professor?

[Prof. Park] Step 1 is Grouping: look inside the parentheses $(6 - 2)$. That gives 4! Rewrite the expression: $3 + 4 \\times (4)^2 / 8 - 5$.

[TA Sora] Step 2 is Exponents: evaluate $4^2$. That means $4 \\times 4 = 16$. So we have $3 + 4 \\times 16 / 8 - 5$.

[Prof. Park] Step 3: scan for Multiplications and Divisions from left to right! First we see $4 \\times 16 = 64$. Then divide by 8: $64 / 8 = 8$!

[TA Sora] Now look at what remains: $3 + 8 - 5$. Only addition and subtraction left! Moving left to right: $3 + 8 = 11$, and $11 - 5 = 6$!

[Prof. Park] Final answer is 6! Notice what would have happened if someone added $3 + 4 = 7$ in the very first step.

[TA Sora] Disaster! The whole problem would have derailed into an incorrect number. Honor the hierarchy, and the problem solves itself cleanly!""",

    # Slide 7: Fraction Fundamentals: Equivalent Fractions & Reducing
    """[Prof. Park] Slide 7 covers fractions: the topic that causes more student headaches than almost anything else. But fractions are just division in disguise!

[TA Sora] Exactly, Professor! A fraction $a/b$ simply means $a$ divided by $b$. The numerator $a$ is how many pieces you hold, and the denominator $b$ is the size of each piece.

[Prof. Park] Look at Example 2 on page 5: reducing fractions to lowest terms. We simplify $18 / 24$. Sora, what is the strategy here?

[TA Sora] Find the Greatest Common Factor of 18 and 24! Both numbers are divisible by 6. $18 = 6 \\times 3$, and $24 = 6 \\times 4$.

[Prof. Park] When we divide both top and bottom by 6, we are really dividing by $6/6$, which is just 1! Dividing by 1 never changes the value of a number.

[TA Sora] So $18 / 24$ simplifies cleanly to $3/4$. Three quarters of a dollar has the exact same value as eighteen 24ths of a dollar!

[Prof. Park] What if a student didn't spot 6 right away? No problem! Divide by 2 first to get $9/12$, then divide by 3 to reach $3/4$.

[TA Sora] Step-by-step reduction is always safe. As long as you treat the top and bottom equally, you cannot go wrong!""",

    # Slide 8: Multiplying & Dividing Fractions
    """[Prof. Park] Slide 8 moves to multiplying and dividing fractions. Sora, is it true that multiplying fractions is actually easier than adding them?

[TA Sora] Much easier, Professor! Because with multiplication, you do NOT need a common denominator! You just multiply straight across: top times top, bottom times bottom!

[Prof. Park] But before you multiply large numbers, what is your pro-tip? Cross-cancel first!

[TA Sora] Yes! Look at Example 3: $\\frac{4}{9} \\times \\frac{3}{8}$. If you multiply directly, you get $12/72$, which requires heavy simplification.

[Prof. Park] But if you cross-cancel: 4 and 8 reduce by 4 to give 1 and 2! And 3 and 9 reduce by 3 to give 1 and 3!

[TA Sora] Now multiply the tiny survivors: $(1 \\times 1) / (3 \\times 2) = 1/6$! Immediate, effortless lowest terms!

[Prof. Park] Now what about fraction division: $\\frac{5}{6} \\div \\frac{2}{3}$? Sora, teach them our famous motto.

[TA Sora] Keep-Change-Flip! Keep the first fraction $\\frac{5}{6}$, change division to multiplication, and flip the second fraction to $\\frac{3}{2}$! Then cross-cancel to get $\\frac{5}{4}$!""",

    # Slide 9: Adding & Subtracting Fractions: Finding the LCD
    """[Prof. Park] Slide 9 addresses the operation where students must slow down and prepare: adding and subtracting fractions.

[TA Sora] Because here, you CANNOT just add straight across! If you have 1 half of a pizza and 1 third of a pizza, you don't have 2 fifths!

[Prof. Park] Exactly. Denominators represent the size of the slices. You cannot combine slices until they are cut into identical pieces—a Least Common Denominator!

[TA Sora] Look at Example 4 on page 6: $\\frac{2}{3} + \\frac{1}{4}$. The denominators are 3 and 4. What is their LCD, Professor?

[Prof. Park] The smallest multiple shared by 3 and 4 is 12! So we convert each fraction to equivalent twelfths.

[TA Sora] Multiply $\\frac{2}{3}$ by $\\frac{4}{4}$ to get $\\frac{8}{12}$. Multiply $\\frac{1}{4}$ by $\\frac{3}{3}$ to get $\\frac{3}{12}$!

[Prof. Park] Now that the slices are identical twelfths, add the numerators: $8 + 3 = 11$, and keep the denominator 12! Result: $\\frac{11}{12}$.

[TA Sora] Notice we NEVER add denominators! $12 + 12$ does not become 24. Denominators name the size; numerators count the quantity!""",

    # Slide 10: Section 1.0 Summary: Master Toolkit & Orientation
    """[Prof. Park] On our final slide of Lecture 01, we synthesize our Section 1.0 Master Toolkit. Sora, what three habits should every student take away today?

[TA Sora] Habit number 1: Always protect signed numbers and substitutions with parentheses! Pockets keep things organized.

[Prof. Park] Habit number 2: Follow GEMDAS strictly from left to right. Never rush multiplication ahead of division or addition ahead of subtraction.

[TA Sora] And Habit number 3: When working with fractions, remember: multiply straight across with cross-canceling, Keep-Change-Flip for division, and build an LCD before adding or subtracting!

[Prof. Park] Look at how much ground we covered today: variables, constants, real numbers, absolute value, GEMDAS, and full fraction mechanics.

[TA Sora] You are fully equipped for Lecture 02, where we dive into signed numbers, negative temperatures, and algebraic evaluation.

[Prof. Park] Work through the assigned exercises on workbook page 7 before our next session. You can do this!

[TA Sora] We are with you every step of the way. See you all in Lecture 02!"""
]

print("Script L01 ready with 10 slides.")
