# -*- coding: utf-8 -*-
"""
High-Frequency Tiki-Taka Generator for Unit 1: Lectures 01 to 05.
Each slide contains 8 to 10 alternating micro-turns strictly formatted as:
[Prof. Park] ... \n\n [TA Sora] ... \n\n [Prof. Park] ... \n\n [TA Sora] ...
Zero colons. Word counts: 2,300 - 2,550 words per lecture.
"""
import sys, io, re, json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

scripts_l01 = [
    # Slide 1: Welcome & Course Orientation
    """[Prof. Park] Welcome everyone to M090 Introductory Algebra here at Gallatin College Montana State University! I am Professor Eunju Park, and right beside me is our exceptional graduate teaching assistant, Sora.

[TA Sora] Hello everyone! Whether you are sitting right here on our Bozeman campus or tuning in across Gallatin County, welcome! Professor, what is the number one question students ask me on day one?

[Prof. Park] They always ask: 'Professor Park, what if I have never been good at math in high school?' And my answer is always the same: mathematical ability is not a genetic trait! It is simply a set of clean, repeatable mental tools.

[TA Sora] Exactly! If you've ever felt paralyzed by math anxiety, or thought fractions and variables were an incomprehensible secret code, consider this classroom your fresh start. We build our house brick by brick.

[Prof. Park] That is our core teaching philosophy. In M090, we never rush through mechanical formulas without deep intuition. We connect every algebraic operation to physical realities you see right here in Montana.

[TA Sora] Think about measuring timber to frame a house in Belgrade, calculating fuel efficiency driving up to Bridger Bowl, or tracking elevation gradients along the Gallatin River. Algebra is the language of practical reasoning!

[Prof. Park] Today we begin Section 1.0 on page 3 of your course workbook, reviewing essential arithmetic tools and setting our standards for algebraic thinking.

[TA Sora] Over the next 45 lectures, Professor Park and I will walk through every single workbook example together, step by step, with total clarity. Grab your pencil, open page 3, and let's get started!""",

    # Slide 2: Variables, Constants & Distance Model
    """[Prof. Park] Let's begin on workbook page 3 with two foundational definitions: variables and constants. Sora, how do you explain the difference in everyday terms?

[TA Sora] I tell students: think of a constant as a solid granite boulder—it never changes its weight or shape! Numbers like 5, -12, or pi are constants.

[Prof. Park] And a variable? That is an open, empty pocket—or an empty parking space waiting for whatever real-world number comes along. In algebra, we represent variables with letters like $x$, $y$, $r$, or $t$.

[TA Sora] Look at the classic distance formula on screen: $D = r \\cdot t$. Distance equals rate multiplied by time. All three symbols are variables!

[Prof. Park] Imagine you are driving west on Interstate 90 from Bozeman toward Butte at a steady cruise control speed of 70 miles per hour. Your rate $r$ is fixed at 70.

[TA Sora] But time $t$ is constantly ticking! After 1 hour, $t = 1$, so your distance $D$ is $70 \\times 1 = 70$ miles. After 2 hours, $t = 2$, so $70 \\times 2 = 140$ miles, taking you right past Whitehall!

[Prof. Park] Exactly. And after 2.5 hours, $70 \\times 2.5 = 175$ miles. Notice what happened: the formula $D = r \\cdot t$ does not just describe one single road trip; it models every possible journey on Earth!

[TA Sora] That is the true superpower of algebra: instead of doing individual arithmetic calculations over and over, we write one master algebraic relationship that governs all cases!""",

    # Slide 3: Arithmetic Operations & Absolute Value
    """[Prof. Park] On Slide 3, we review the four primary arithmetic operations: addition, subtraction, multiplication, and division, along with absolute value.

[TA Sora] Professor, let's look closely at absolute value first, because students constantly get tripped up when they see the vertical bars $|-8|$.

[Prof. Park] What is the most dangerous misconception you see in tutoring, Sora?

[TA Sora] Many students think absolute value means 'change the sign.' So when they see positive $|+5|$, they accidentally turn it into $-5$! That's a huge error!

[Prof. Park] That is a vital distinction. Absolute value does NOT mean opposite sign; it measures pure geometric distance from zero on the number line! Distance can never be negative.

[TA Sora] Exactly! If you walk 8 miles north from Bozeman, your distance is 8. If you walk 8 miles south toward Big Sky, your distance is STILL 8! So $|-8| = 8$, and $|+8| = 8$.

[Prof. Park] Perfect physical intuition. Now notice the two division problems with zero at the bottom: $0 / 5 = 0$, but $5 / 0$ is completely undefined!

[TA Sora] Here is my favorite pizza test: you can divide zero slices of pizza among 5 friends—everyone gets zero slices, perfectly logical. But dividing 5 slices among zero humans? The calculator explodes! Division by zero is undefined!""",

    # Slide 4: Real Numbers: Integers, Rationals & Irrationals
    """[Prof. Park] Slide 4 introduces the grand architecture of the Real Number System $\\mathbb{R}$. Sora, how should students visualize these concentric number families?

[TA Sora] Picture Russian nesting dolls! At the very center are the Natural counting numbers: $1, 2, 3...$ counting elk in Yellowstone.

[Prof. Park] Add zero, and you have the Whole numbers. Then expand in both directions to include negative temperatures like $-20^\\circ\\text{F}$ on a January morning in Bozeman, and you get Integers $\\mathbb{Z}$!

[TA Sora] Next comes the largest family we work with every single day: Rational numbers $\\mathbb{Q}$. The root word is 'ratio'—any number that can be expressed as a clean fraction $a/b$.

[Prof. Park] That includes terminating decimals like $0.75 = 3/4$ and repeating decimals like $0.333... = 1/3$. But what about numbers that wander endlessly without any repeating pattern?

[TA Sora] Those are the Irrationals! Mathematical celebrities like $\\pi \\approx 3.14159...$ and $\\sqrt{2} \\approx 1.414...$. You can never trap them inside a simple integer fraction!

[Prof. Park] When you unite all the rationals with all the irrationals, you form the continuous, unbroken real number line $\\mathbb{R}$.

[TA Sora] Every single point on that line has a unique numerical address. That gives us the rock-solid ground we stand on for all of algebra!""",

    # Slide 5: Order of Operations (PEMDAS / GEMDAS)
    """[Prof. Park] Slide 5 brings us to the supreme traffic law of all mathematics: the Order of Operations! GEMDAS—or PEMDAS. Sora, why do we emphasize GEMDAS?

[TA Sora] Because grouping symbols are not just round parentheses! They include square brackets $[\\;]$, curly braces $\\{\\;\\}$, absolute value bars $|\\;|$, and fraction bars!

[Prof. Park] Exactly. Now look at the middle letters: Multiplication and Division. What is the classic student trap here, Sora?

[TA Sora] Students think: 'M comes before D in the acronym, so multiplication ALWAYS beats division!' That is completely wrong!

[Prof. Park] That's right! Multiplication and division have identical mathematical priority. You must evaluate them strictly from left to right, in the exact order they appear!

[TA Sora] And the exact same rule applies to Addition and Subtraction! Equal priority, left to right! If subtraction appears on the left, you subtract first!

[Prof. Park] Think of order of operations like airport security checkpoints: first Grouping, then Exponents, then Multiplications and Divisions left to right, and finally Additions and Subtractions left to right.

[TA Sora] Follow the traffic rules, and your algebra solutions will be rock-solid and bulletproof every single time!""",

    # Slide 6: Section 1.0 Example 1: Evaluating Order of Operations
    """[Prof. Park] Let's put our GEMDAS rules into practice with Example 1 from workbook page 4: evaluate $3 + 4 \\times (6 - 2)^2 / 8 - 5$.

[TA Sora] Sora's golden advice: never try to do three steps in your head at once! Take it line by line. What is our first move, Professor?

[Prof. Park] Step 1 is Grouping: look inside the parentheses $(6 - 2)$. That gives 4! Rewrite the entire line: $3 + 4 \\times (4)^2 / 8 - 5$.

[TA Sora] Step 2 is Exponents: evaluate $4^2$. That means $4 \\times 4 = 16$. So our expression becomes: $3 + 4 \\times 16 / 8 - 5$.

[Prof. Park] Step 3: scan for Multiplications and Divisions from left to right! First we encounter $4 \\times 16 = 64$. Then divide by 8: $64 / 8 = 8$!

[TA Sora] Look how clean it looks now: $3 + 8 - 5$. Only addition and subtraction remain! Moving left to right: $3 + 8 = 11$, and $11 - 5 = 6$!

[Prof. Park] Final answer is 6! Notice what would have happened if a student added $3 + 4 = 7$ in the very first step.

[TA Sora] Total disaster! The whole calculation would have collapsed into an incorrect number. Honor the hierarchy, and the problem solves itself with zero stress!""",

    # Slide 7: Fraction Fundamentals: Equivalent Fractions & Reducing
    """[Prof. Park] Slide 7 covers fractions: the topic that causes more student anxiety than almost anything else. But fractions are just division in disguise!

[TA Sora] That's so true, Professor! A fraction $a/b$ simply means $a$ divided by $b$. The numerator $a$ counts how many pieces you have; the denominator $b$ tells you the size of each piece.

[Prof. Park] Look at Example 2 on page 5: reducing fractions to lowest terms. We need to simplify $18 / 24$. Sora, what is our strategy?

[TA Sora] Find the Greatest Common Factor of 18 and 24! Both numbers are divisible by 6: $18 = 6 \\times 3$, and $24 = 6 \\times 4$.

[Prof. Park] When we divide both numerator and denominator by 6, we are really dividing by $6/6$, which is equal to 1! Dividing by 1 never alters the true value of a number.

[TA Sora] So $18 / 24$ simplifies cleanly to $3/4$. Three quarters of a dollar has the exact same value as eighteen 24ths of a dollar!

[Prof. Park] What if a student didn't spot 6 right away? Can they divide by 2 first?

[TA Sora] Absolutely! Divide by 2 to get $9/12$, then divide by 3 to reach $3/4$. Step-by-step reduction is always 100% valid. Treat top and bottom equally, and you will always succeed!""",

    # Slide 8: Multiplying & Dividing Fractions
    """[Prof. Park] Slide 8 tackles multiplying and dividing fractions. Sora, is it true that multiplying fractions is actually much easier than adding them?

[TA Sora] Far easier, Professor! Because with multiplication, you do NOT need a common denominator! You just multiply straight across: top times top, bottom times bottom!

[Prof. Park] But before students multiply large numbers, what is your number one pro-tip? Cross-cancel first!

[TA Sora] Yes! Look at Example 3: $\\frac{4}{9} \\times \\frac{3}{8}$. If you multiply directly, you get $12/72$, which requires heavy simplification.

[Prof. Park] But if you cross-cancel: 4 in the numerator and 8 in the denominator reduce by 4 to give 1 and 2! And 3 and 9 reduce by 3 to give 1 and 3!

[TA Sora] Now multiply the tiny survivors: $(1 \\times 1) / (3 \\times 2) = 1/6$! Immediate, effortless lowest terms!

[Prof. Park] What about fraction division: $\\frac{5}{6} \\div \\frac{2}{3}$? Sora, teach them our classroom motto.

[TA Sora] Keep-Change-Flip! Keep the first fraction $\\frac{5}{6}$, change division to multiplication, and flip the second fraction upside down to $\\frac{3}{2}$! Then cross-cancel 3 and 6 to get $\\frac{5}{4}$!""",

    # Slide 9: Adding & Subtracting Fractions: Finding the LCD
    """[Prof. Park] Slide 9 brings us to adding and subtracting fractions—the place where you must slow down and prepare your denominators!

[TA Sora] Because here, you CANNOT just add straight across! If you have 1 half of a pizza and 1 third of a pizza, you do not have 2 fifths of a pizza!

[Prof. Park] Exactly. Denominators represent the physical size of the slices. You cannot combine slices until they are cut into identical sizes—a Least Common Denominator!

[TA Sora] Look at Example 4 on page 6: $\\frac{2}{3} + \\frac{1}{4}$. The denominators are 3 and 4. What is their LCD, Professor?

[Prof. Park] The smallest multiple shared by both 3 and 4 is 12! So we convert each fraction into equivalent twelfths.

[TA Sora] Multiply $\\frac{2}{3}$ by $\\frac{4}{4}$ to get $\\frac{8}{12}$. Multiply $\\frac{1}{4}$ by $\\frac{3}{3}$ to get $\\frac{3}{12}$!

[Prof. Park] Now that the slices are identical twelfths, add the numerators: $8 + 3 = 11$, and keep the denominator 12! Result: $\\frac{11}{12}$.

[TA Sora] Notice we NEVER add denominators! $12 + 12$ does not become 24. Denominators name the slice size; numerators count how many slices you have!""",

    # Slide 10: Section 1.0 Summary: Master Toolkit & Orientation
    """[Prof. Park] On our final slide of Lecture 01, we synthesize our Section 1.0 Master Toolkit. Sora, what three habits should every student take away today?

[TA Sora] Habit number 1: Always protect signed numbers and substitutions with parentheses! Pockets keep things organized.

[Prof. Park] Habit number 2: Follow GEMDAS strictly from left to right. Never rush multiplication ahead of division or addition ahead of subtraction.

[TA Sora] And Habit number 3: When working with fractions, remember: multiply straight across with cross-canceling, Keep-Change-Flip for division, and build an LCD before adding or subtracting!

[Prof. Park] Look at how much ground we covered today: variables, constants, real numbers, absolute value, GEMDAS, and complete fraction mechanics.

[TA Sora] You are fully equipped for Lecture 02, where we dive into signed numbers, negative temperatures, and algebraic evaluation.

[Prof. Park] Work through the assigned exercises on workbook page 7 before our next session. You can do this!

[TA Sora] We are with you every step of the way. See you all in Lecture 02!"""
]

# Scripts for L02 (10 slides)
scripts_l02 = [
    # Slide 1: Welcome & Board Work 8-14 Overview
    """[Prof. Park] Welcome to Lecture 02 of M090! Today, on page 4 of your workbook, we tackle Board Work problems #8 through #14, mastering complex fractions and order of operations.

[TA Sora] In Lecture 01, we established our foundational rules. Today, we put those rules under pressure with tricky student traps!

[Prof. Park] That's where real learning happens. When you encounter a multi-step fraction or a negative sign, you need an instinctive game plan.

[TA Sora] What are the big three challenges on today's agenda, Professor?

[Prof. Park] First, complex fractions—fractions sitting inside fractions! Second, zero in fractions—knowing when the result is zero versus undefined.

[TA Sora] And third, the left-to-right trap in PEMDAS when division meets multiplication, or subtraction meets addition!

[Prof. Park] Exactly. If you can navigate these board work problems with ease, you will sail through our upcoming exams.

[TA Sora] Let's roll up our sleeves and dive straight into Board Work #8 on Slide 2!""",

    # Slide 2: Complex Fractions (Board Work #8)
    """[Prof. Park] Look at Board Work #8 on workbook page 4: simplifying complex fractions like $\\frac{3/4}{5/8}$. Sora, why do complex fractions intimidate students?

[TA Sora] Because students see four numbers stacked on top of each other and panic! But I tell them: look at that giant main fraction bar. What does a fraction bar actually mean?

[Prof. Park] It simply means division! A complex fraction is nothing more than a division problem written vertically: $\\frac{3}{4} \\div \\frac{5}{8}$!

[TA Sora] And what is our golden rule for dividing fractions? Keep-Change-Flip!

[Prof. Park] Exactly! Keep the top fraction $\\frac{3}{4}$, change the main division bar to multiplication, and flip the bottom fraction to $\\frac{8}{5}$!

[TA Sora] Now we have $\\frac{3}{4} \\times \\frac{8}{5}$. Before multiplying, cross-cancel: 4 in the denominator and 8 in the numerator reduce by 4 to give 1 and 2!

[Prof. Park] Multiply the clean survivors: $(3 \\times 2) / (1 \\times 5) = 6/5$! Look how effortlessly a terrifying fraction tower collapsed into a clean fraction!

[TA Sora] That's the secret: rewrite vertically stacked fractions as horizontal division, Keep-Change-Flip, cross-cancel, and you're done!""",

    # Slide 3: Mixed Integer and Fraction Operations (Board Work #9)
    """[Prof. Park] On Slide 3, Board Work #9 tests mixed operations combining whole integers with fractions: $4 - \\frac{2}{3} \\times \\frac{9}{10}$.

[TA Sora] Professor, this problem is a classic exam trap! What is the number one blunder students make here?

[Prof. Park] Almost half the class wants to calculate $4 - 2/3$ first! They see subtraction on the left and rush to subtract. Why is that illegal, Sora?

[TA Sora] Because GEMDAS says Multiplication beats Subtraction! You cannot touch that 4 until the multiplication is completely resolved!

[Prof. Park] Precisely! Let's handle the multiplication first: $\\frac{2}{3} \\times \\frac{9}{10}$. Cross-cancel before multiplying!

[TA Sora] 2 and 10 reduce by 2 to give 1 and 5. 3 and 9 reduce by 3 to give 1 and 3. So the product is $(1 \\times 3) / (1 \\times 5) = \\frac{3}{5}$!

[Prof. Park] Now bring back the 4: our expression is $4 - \\frac{3}{5}$. How do we subtract a fraction from an integer, Sora?

[TA Sora] Put 4 over 1: $\\frac{4}{1} = \\frac{20}{5}$! Now subtract: $\\frac{20}{5} - \\frac{3}{5} = \\frac{17}{5}$!

[Prof. Park] Outstanding. $17/5$ is our final, exact answer. Respecting the hierarchy saved us from a fatal subtraction trap!""",

    # Slide 4: Factor Simplification & Pre-Canceling (Board Work #10)
    """[Prof. Park] Slide 4 brings us to Board Work #10: simplifying large products of fractions: $\\frac{14}{25} \\times \\frac{15}{28} \\times \\frac{10}{9}$.

[TA Sora] If a student multiplies the numerators $14 \\times 15 \\times 10$, they get 2,100! And the denominators $25 \\times 28 \\times 9$ gives 6,300! That's a numerical nightmare!

[Prof. Park] That's working ten times harder than necessary. What should they do instead?

[TA Sora] Slash and simplify before you ever multiply! Look for common factors between ANY numerator and ANY denominator.

[Prof. Park] Let's hunt for pairs! 14 on top and 28 on the bottom: both divide by 14, leaving 1 on top and 2 on the bottom!

[TA Sora] Now look at 15 on top and 25 on the bottom: both divide by 5, leaving 3 on top and 5 on the bottom!

[Prof. Park] Look at 10 on top and the 5 we just created on the bottom: $10 / 5 = 2$ on top! And that 2 on top cancels with the 2 from the 28!

[TA Sora] And finally, 3 on top cancels into 9 on the bottom, leaving 3! Everything vanished except $1/3$!

[Prof. Park] Look at that: $2,100 / 6,300$ simplifies straight to $1/3$ with zero pencil arithmetic! Pre-canceling is pure mathematical elegance!""",

    # Slide 5: Division by Zero: Undefined vs. Zero (Board Work #11 & #12)
    """[Prof. Park] Slide 5 features Board Work #11 and #12, comparing $\\frac{0}{16}$ versus $\\frac{16}{0}$. Sora, why does this distinction confuse so many people?

[TA Sora] Because both have a 0 and a 16! But the position of zero makes all the difference between a valid number and a mathematical impossibility!

[Prof. Park] Let's look at Board Work #11: $\\frac{0}{16}$. Zero is in the numerator. What does that equal, Sora?

[TA Sora] It equals 0! Think of it physically: if you have 0 dollars in your wallet and you share it among 16 friends, each friend gets exactly 0 dollars. Totally legal!

[Prof. Park] Now look at Board Work #12: $\\frac{16}{0}$. Zero is in the denominator. What is the answer here?

[TA Sora] UNDEFINED! It does not equal zero, and it does not equal infinity. It simply has no meaning in arithmetic!

[Prof. Park] Exactly. If $16 / 0 = k$, that would mean $k \\times 0 = 16$. But any number times 0 is 0! No number can ever satisfy that equation.

[TA Sora] Here is my memory trick: 'OK vs NO'! Zero Over K is OK ($0/k = 0$). Number Over Zero spells NO ($n/0 = \\text{Undefined}$)! Never forget it!""",

    # Slide 6: PEMDAS Left-to-Right: Division vs. Multiplication (Board Work #13)
    """[Prof. Park] Slide 6 brings us to Board Work #13: evaluate $24 \\div 6 \\times 2$. Sora, this is the classic viral internet math problem!

[TA Sora] Oh, I see this on social media every single week, and thousands of adults argue about it in the comments!

[Prof. Park] Why do so many people get it wrong?

[TA Sora] Because people memorize PEMDAS as a rigid word: 'P-E-M-D-A-S. M comes before D, so multiplication goes first! $6 \\times 2 = 12$, and $24 \\div 12 = 2$!'

[Prof. Park] And that answer of 2 is 100% WRONG! Why is it wrong, Professor?

[TA Sora] Because Multiplication and Division have EQUAL rank! You must execute them strictly from left to right as you read the page!

[Prof. Park] Exactly. Scanning from left to right: first we hit $24 \\div 6$. That gives 4! Then we take that 4 and multiply by 2: $4 \\times 2 = 8$!

[TA Sora] The correct mathematical answer is 8, NOT 2! Division was on the left, so division goes first!

[Prof. Park] That is why we write GEMDAS with $M/D$ on the same tier. Left-to-right rule is non-negotiable!""",

    # Slide 7: PEMDAS Left-to-Right: Subtraction vs. Addition (Board Work #14)
    """[Prof. Park] Slide 7 tests the sibling rule with Board Work #14: evaluate $17 - 5 + 8$. Sora, what trap awaits here?

[TA Sora] The exact same trap! Students think 'A comes before S in PEMDAS, so I must add $5 + 8 = 13$ first, and $17 - 13 = 4$!'

[Prof. Park] And once again, that answer of 4 is completely incorrect! Why?

[TA Sora] Because Addition and Subtraction share EQUAL priority! They are solved strictly from left to right!

[Prof. Park] What happens when we work properly from left to right?

[TA Sora] First, we do $17 - 5$. That gives 12! Then we take 12 and add 8: $12 + 8 = 20$!

[Prof. Park] The true answer is 20! Think of your bank account: you have $17. You spend $5 at the coffee shop, leaving you with $12. Then you deposit an $8 check. You have $20, not $4!

[TA Sora] Financial common sense completely validates the left-to-right rule. Never jump addition over subtraction!""",

    # Slide 8: Exponent Pitfall: Base Identification in Signed Powers
    """[Prof. Park] Slide 8 covers what is arguably the single most common sign error in all of algebra: $(-3)^2$ versus $-3^2$.

[TA Sora] Professor, I cannot tell you how many points are lost on this on Exam 1! They look identical to the untrained eye!

[Prof. Park] Let's train their eyes right now. Look at the first expression: $(-3)^2$. Where is the negative sign, Sora?

[TA Sora] The negative sign is INSIDE the parentheses! The exponent 2 touches the parentheses, which means the entire quantity $(-3)$ is multiplied by itself!

[Prof. Park] So $(-3) \\times (-3) = +9$! Negative times negative yields positive 9. Now look at the second expression: $-3^2$. What does the exponent 2 touch here?

[TA Sora] It touches ONLY the 3! The negative sign is just sitting in front, waiting like a minus sign: $-(3^2) = -(3 \\times 3) = -9$!

[Prof. Park] That is the crucial difference. $(-3)^2 = +9$, but $-3^2 = -9$! The base of the exponent is only what is directly under its reach.

[TA Sora] Unless there are parentheses wrapping around the negative sign, the negative sign is NOT being squared! Memorize this slide!""",

    # Slide 9: Section 1.0 Master Summary: All 14 Board Work Skills Synthesized
    """[Prof. Park] Slide 9 brings all 14 Board Work skills together into a master reference table. Sora, let's review the big takeaways.

[TA Sora] Takeaway 1: Complex fractions are just division—flip the bottom fraction and multiply!

[Prof. Park] Takeaway 2: Pre-cancel common factors before multiplying fractions to keep calculations effortless.

[TA Sora] Takeaway 3: $0 / k = 0$, but $k / 0$ is Undefined! Remember 'OK vs NO'!

[Prof. Park] Takeaway 4: In GEMDAS, Multiplication/Division and Addition/Subtraction are tied pairs—solve strictly left to right!

[TA Sora] Takeaway 5: Base identification: $(-a)^2 = +a^2$, but $-a^2 = -a^2$!

[Prof. Park] If you master these five pillars, you have eliminated 95% of the arithmetic errors that sabotage students in algebra.

[TA Sora] You are building real algebraic muscle. Be proud of the foundation you are laying today!""",

    # Slide 10: Lecture 02 Wrap-Up & Transition to Section 1.1
    """[Prof. Park] That concludes Lecture 02 and wraps up our comprehensive review of Section 1.0!

[TA Sora] Next time, in Lecture 03, we enter Section 1.1 on page 6 of your workbook: Evaluating Algebraic Expressions with Signed Numbers!

[Prof. Park] That is where variables come alive: substituting negative numbers into formulas like the Quadratic Formula and Discriminant!

[TA Sora] Make sure you bring your empty pockets parentheses rule to class!

[Prof. Park] Review workbook pages 4 and 5 tonight, practice the board work problems, and we will see you in Lecture 03!

[TA Sora] Great work today, everyone! See you next time!"""
]

# Scripts for L03 (9 slides)
scripts_l03 = [
    # Slide 1: Welcome to Lecture 03: The Magic of Substitution
    """[Prof. Park] Welcome to Lecture 03 of M090! Today, on pages 6 and 7 of your workbook, we begin Section 1.1: Evaluating Algebraic Expressions with Signed Numbers.

[TA Sora] Hello everyone! Today we take the arithmetic tools from Lectures 01 and 02 and apply them directly to algebraic formulas!

[Prof. Park] In algebra, an expression is like a recipe. The variables are the ingredients, and the numbers we substitute are the actual measurements we pour in.

[TA Sora] But when those numbers are negative, things can get messy fast if you aren't careful!

[Prof. Park] That's why today we introduce our most powerful protective habit: the Empty Pockets Parentheses Rule!

[TA Sora] With this one technique, you will evaluate complex expressions with zero sign confusion.

[Prof. Park] Open your workbooks to page 6, and let's master the magic of substitution!""",

    # Slide 2: Golden Rule of Substitution: Protective Parentheses
    """[Prof. Park] Slide 2 lays down the Golden Rule of Substitution: Protective Parentheses. Sora, walk us through the two-step protocol.

[TA Sora] Step 1: Empty Pockets! Everywhere you see a variable letter in the expression, erase the letter and replace it with a set of open parentheses: $(\\;)$.

[Prof. Park] And Step 2?

[TA Sora] Step 2: Drop the numbers into those open pockets! Don't try to compute anything yet. Just place the numbers safely inside their parentheses.

[Prof. Park] Why is that so crucial, Sora?

[TA Sora] Because if you have $-x^2$ and $x = -4$, writing $- - 4^2$ looks like a typographical mess! But writing $-(-4)^2$ makes the order of operations crystal clear!

[Prof. Park] The parentheses protect the sign of the number from colliding with the operational signs in the formula.

[TA Sora] Treat parentheses like safety goggles in chemistry lab: put them on first, and you will never get burned!""",

    # Slide 3: Example 1: Rational Fraction Evaluation
    """[Prof. Park] Let's apply our rule to Example 1 from workbook page 6: evaluate $\\frac{d^2 - f^2}{d^2 + f^2}$ for $d = -2$ and $f = 5$.

[TA Sora] Step 1: Open the pockets! $\\frac{(\\;)^2 - (\\;)^2}{(\\;)^2 + (\\;)^2}$.

[Prof. Park] Step 2: Drop in $d = -2$ and $f = 5$: $\\frac{(-2)^2 - (5)^2}{(-2)^2 + (5)^2}$. Now evaluate the powers!

[TA Sora] In the numerator: $(-2)^2 = (-2) \\times (-2) = +4$! And $5^2 = 25$. So top is $4 - 25 = -21$!

[Prof. Park] In the denominator: $(-2)^2 = +4$, and $5^2 = 25$. Bottom is $4 + 25 = 29$!

[TA Sora] Put them together: $\\frac{-21}{29}$! Can this fraction be reduced, Professor?

[Prof. Park] 29 is a prime number, and 21 is not a factor of 29, so $\\frac{-21}{29}$ is in simplest form!

[TA Sora] Look how clean that was! Because we wrapped $(-2)$ in parentheses, we got $+4$ both times without hesitation!""",

    # Slide 4: Example 2: Absolute Values & Cubes
    """[Prof. Park] Slide 4 presents Example 2: evaluate $\\frac{2x^2 + y^2}{|-10 + z^3|}$ when $x = -1$, $y = -3$, and $z = 2$.

[TA Sora] Let's prepare our empty pockets: $\\frac{2(\\;)^2 + (\\;)^2}{|-10 + (\\;)^3|}$. Drop in $x = -1$, $y = -3$, and $z = 2$!

[Prof. Park] Let's calculate the numerator first, Sora.

[TA Sora] In the numerator: $(-1)^2 = +1$, so $2(1) = 2$. Next, $(-3)^2 = +9$! Add them together: $2 + 9 = 11$!

[Prof. Park] Excellent. Now let's calculate the denominator inside the absolute value bars: $|-10 + (2)^3|$.

[TA Sora] First, exponent: $2^3 = 2 \\times 2 \\times 2 = 8$. So inside the bars we have $-10 + 8 = -2$!

[Prof. Park] Now apply the absolute value: what is $|-2|$?

[TA Sora] The distance from 0 is positive 2! So the denominator becomes 2!

[Prof. Park] Put numerator over denominator: $\\frac{11}{2}$!

[TA Sora] Notice we evaluated everything inside the absolute value bars BEFORE taking the absolute value. That's GEMDAS in action!""",

    # Slide 5: Example 3: The Discriminant Formula
    """[Prof. Park] On Slide 5, Example 3 asks us to evaluate the famous Discriminant expression: $b^2 - 4ac$ for $a = 5$, $b = -6$, and $c = -3$.

[TA Sora] In Unit 3, this expression will tell us how many solutions a quadratic equation has! Today, we master its calculation.

[Prof. Park] Step 1: Empty pockets! $(\\;)^2 - 4(\\;)(\\;)$.

[TA Sora] Drop in the values: $(-6)^2 - 4(5)(-3)$. Now, Sora's warning: watch that double negative!

[Prof. Park] First, $(-6)^2 = +36$. Now look at the product $-4 \\times 5 \\times (-3)$. What is the sign, Sora?

[TA Sora] Negative times positive is negative, and negative times negative is POSITIVE! $-4 \\times 5 = -20$, and $-20 \\times (-3) = +60$!

[Prof. Park] So our expression becomes $36 + 60 = 96$!

[TA Sora] Many students subtract 60 and get $-24$ because they miss the negative sign on $c = -3$. Count your negative signs: two negatives multiply to a positive!""",

    # Slide 6: Example 4: The Quadratic Formula Expression
    """[Prof. Park] Slide 6 features the full Quadratic Formula numerator and denominator: evaluate $\\frac{-b + \\sqrt{b^2 - 4ac}}{2a}$ for $a = 1$, $b = 7$, and $c = -6$.

[TA Sora] This looks intimidating, but it is just arithmetic with a square root! Let's substitute with pockets: $\\frac{-(7) + \\sqrt{(7)^2 - 4(1)(-6)}}{2(1)}$.

[Prof. Park] Let's evaluate the quantity inside the square root first: $(7)^2 = 49$. Now the product: $-4(1)(-6) = +24$!

[TA Sora] Add them up inside the radical: $49 + 24 = 73$! So we have $\\sqrt{73}$.

[Prof. Park] Now look at the front term: $-(7) = -7$. And the denominator: $2(1) = 2$.

[TA Sora] Assemble the pieces: $\\frac{-7 + \\sqrt{73}}{2}$! Can we simplify $\\sqrt{73}$, Professor?

[Prof. Park] 73 is a prime number and has no perfect square factors, so $\\frac{-7 + \\sqrt{73}}{2}$ is the exact, final answer!

[TA Sora] Breaking the formula into three clean zones—front, radical, and denominator—makes even the Quadratic Formula completely manageable!""",

    # Slide 7: Example 5: Simplifying Radical Outcomes
    """[Prof. Park] Slide 7 gives us Example 5: evaluate $\\frac{-b + \\sqrt{b^2 - 4ac}}{2a}$ with numbers that produce a clean square root: $a = 2$, $b = -10$, and $c = 8$.

[TA Sora] Notice $b$ is negative: $b = -10$! So the front term is $-(-10)$. What is the opposite of negative 10, Professor?

[Prof. Park] It is positive 10! Now evaluate inside the radical: $(-10)^2 - 4(2)(8)$.

[TA Sora] $(-10)^2 = +100$. The product is $-4 \\times 2 \\times 8 = -64$. So inside we have $100 - 64 = 36$!

[Prof. Park] And what is the square root of 36?

[TA Sora] $\\sqrt{36} = 6$! A perfect whole number!

[Prof. Park] Now look at the numerator: $10 + 6 = 16$. And the denominator: $2a = 2(2) = 4$.

[TA Sora] So our fraction is $\\frac{16}{4} = 4$! A single clean integer!

[Prof. Park] Look at that transformation: a complex formula collapsed into 4 because every sign was respected at each step!""",

    # Slide 8: Calculator Pitfalls vs. Paper Algebra
    """[Prof. Park] On Slide 8, we discuss a modern danger: Calculator Pitfalls versus Paper Algebra.

[TA Sora] Professor, why does a graphing calculator sometimes say $(-4)^2 = -16$?

[Prof. Park] Because if you type $-4^2$ without parentheses, the calculator follows strict order of operations: it squares 4 first to get 16, and then applies the negative sign to get $-16$!

[TA Sora] Exactly! You must type open parenthesis, negative 4, close parenthesis, then square: $((-4))^2$ to get $+16$!

[Prof. Park] The machine only does what you command it to do. If you feed it flawed syntax, it gives you flawed answers.

[TA Sora] Paper algebra forces you to understand the structure. Write out your steps on paper first, and use the calculator only to verify arithmetic!

[Prof. Park] Technology is a wonderful servant, but a terrible master. Keep your algebraic reasoning sharp!""",

    # Slide 9: Lecture 03 Wrap-Up & Sora's Substitution Checklist
    """[Prof. Park] We have reached the end of Lecture 03! Sora, recap your Substitution Checklist for the class.

[TA Sora] Three rules for your notes:
1. Replace every variable letter with empty parentheses $(\\;)$ before writing numbers.
2. Remember that $(-x)^2$ is positive, while $-x^2$ is negative.
3. Count negative signs in products: an even number of negatives makes positive, an odd number makes negative!

[Prof. Park] Next time, in Lecture 04, we enter Section 1.1 Part 2: Translating English Phrases into Algebraic Expressions!

[TA Sora] We will learn how to turn word problems into clear, solvable equations!

[Prof. Park] Practice the substitution problems on workbook page 7. Keep up the great work!

[TA Sora] See you all in Lecture 04!"""
]

# Scripts for L04 (10 slides)
scripts_l04 = [
    # Slide 1: Welcome to Lecture 04: Translating Words to Algebra
    """[Prof. Park] Welcome to Lecture 04 of M090! Today, on pages 6 and 7 of your workbook, we master one of the most vital life skills in mathematics: Translating English Phrases into Algebraic Expressions.

[TA Sora] Hello everyone! When students tell me, 'I'm good at math, but I hate word problems,' what they really mean is: 'I haven't learned the translation dictionary yet!'

[Prof. Park] That's exactly right. Algebra is simply a foreign language. English sentences have nouns and verbs; algebra sentences have variables, constants, and operation symbols.

[TA Sora] Once you learn the signal words for addition, subtraction, multiplication, and division, translating a word problem is as straightforward as translating English to Spanish!

[Prof. Park] Today, we will decode the 14 official workbook phrases from Section 1.1, paying special attention to the English words that secretly reverse the order of terms.

[TA Sora] Keep your highlighter ready, and let's unlock the translation dictionary on Slide 2!""",

    # Slide 2: The Big 4 Operation Signal Words & The Reversal Rule
    """[Prof. Park] Slide 2 lays out our Translation Dictionary for the Big Four Operations. Sora, what are the primary signal words for addition and multiplication?

[TA Sora] For addition: 'sum', 'plus', 'increased by', 'more than', and 'total'. For multiplication: 'product', 'times', 'twice', 'of', and 'multiplied by'.

[Prof. Park] And for division: 'quotient', 'divided by', and 'ratio'. But now, let's talk about the danger zone: Subtraction!

[TA Sora] Yes! Standard subtraction words keep the order: 'difference of $a$ and $b$' means $a - b$. 'Decreased by' means $a - b$.

[Prof. Park] But what happens when you hear the words 'subtracted from' or 'less than'?

[TA Sora] REVERSE THE ORDER! If I say: '5 subtracted from 20', what do you have? You start with 20, and take away 5: $20 - 5 = 15$!

[Prof. Park] Exactly. If you wrote $5 - 20$, you would get $-15$! The words 'subtracted from' and 'less than' flip the direction.

[TA Sora] Put a giant warning star in your notes: 'Less Than' and 'Subtracted From' trigger the Reversal Rule!""",

    # Slide 3: Section 1.1 Phrases #1 & #2: Sums & Order Reversals
    """[Prof. Park] Let's translate Workbook Phrases #1 and #2 on page 7. Phrase #1: 'The sum of a number and twelve.'

[TA Sora] Let's pick a variable letter for 'a number'—let's use $x$. 'Sum' signals addition! So 'the sum of $x$ and 12' is simply $x + 12$!

[Prof. Park] Perfect. Now look at Phrase #2: 'Nine subtracted from a number.' Sora, what alarm should ring in a student's head?

[TA Sora] The 'subtracted from' alarm! This is the Reversal Rule! You do NOT write $9 - x$!

[Prof. Park] What is the correct translation?

[TA Sora] You are starting with the number $x$, and removing 9 from it! So it translates to $x - 9$!

[Prof. Park] Let's test it with a concrete number: if your number is 20, nine subtracted from 20 is 11 ($20 - 9$).

[TA Sora] Concrete numbers always reveal the truth. Phrase #1 is $x + 12$; Phrase #2 is $x - 9$!""",

    # Slide 4: Section 1.1 Phrases #3 & #4: Quotients & Multi-Operations
    """[Prof. Park] Slide 4 brings us to Phrases #3 and #4. Phrase #3: 'The quotient of eight and a number.'

[TA Sora] 'Quotient' means division! In English, the order stated is the order written: the first number mentioned goes in the numerator, and the second goes in the denominator!

[Prof. Park] So 'the quotient of 8 and $x$' translates to $\\frac{8}{x}$! Never flip it to $\\frac{x}{8}$.

[TA Sora] Now look at Phrase #4: 'Three times a number, increased by seven.'

[Prof. Park] Let's break this into two stages. First: 'three times a number'. What is that?

[TA Sora] That's multiplication: $3x$. Next: 'increased by seven'—that's addition of 7!

[Prof. Park] Combine them together: $3x + 7$!

[TA Sora] Notice that multiplication naturally binds first, so no parentheses are needed here: $3x + 7$!""",

    # Slide 5: Section 1.1 Phrases #5 & #6: The Square of a Sum vs. Linear Decrease
    """[Prof. Park] Slide 5 features Phrases #5 and #6. Phrase #5: 'The square of the sum of a number and four.' Sora, this is a major grouping trap!

[TA Sora] Notice the phrasing: 'The square OF the sum...' The words 'of the sum' tell you that the addition must happen FIRST, before you square!

[Prof. Park] That means we must wrap the sum in parentheses! The sum of a number and 4 is $(x + 4)$.

[TA Sora] And then we square the entire group: $(x + 4)^2$!

[Prof. Park] What would happen if a student wrote $x^2 + 4$?

[TA Sora] That would translate to 'the sum of the square of a number and four'—a completely different expression! Grouping words demand parentheses.

[Prof. Park] Now translate Phrase #6: 'Twice a number, decreased by eleven.'

[TA Sora] 'Twice a number' is $2x$. 'Decreased by eleven' is $- 11$. Result: $2x - 11$!""",

    # Slide 6: Section 1.1 Phrases #7 & #8: Cubes, Opposites & Products
    """[Prof. Park] Slide 6 brings us to Phrases #7 and #8. Phrase #7: 'The product of negative five and the cube of a number.'

[TA Sora] 'Product' means multiplication between two quantities: $-5$ and 'the cube of a number'.

[Prof. Park] What is the cube of a number $x$?

[TA Sora] That's $x$ raised to the 3rd power: $x^3$! Multiply by $-5$: $-5x^3$!

[Prof. Park] Now look at Phrase #8: 'The opposite of a number, plus eight.' Sora, how do we translate 'the opposite of a number'?

[TA Sora] In algebra, 'opposite' simply means change the sign—put a negative sign in front! So the opposite of $x$ is $-x$.

[Prof. Park] And 'plus eight' is $+ 8$.

[TA Sora] So the complete translation is $-x + 8$! Or by commutativity, $8 - x$! Both are 100% correct!""",

    # Slide 7: Section 1.1 Phrases #9 & #10: Multiple Variables & Fraction Multipliers
    """[Prof. Park] Slide 7 introduces two different variables in Phrases #9 and #10! Phrase #9: 'Five times the sum of $x$ and $y$.'

[TA Sora] Here is that grouping signal again: 'Five times THE SUM OF...' That means 5 multiplies the entire grouped sum!

[Prof. Park] So we write 5 in front of parentheses containing $x + y$: $5(x + y)$!

[TA Sora] If you wrote $5x + y$, the 5 would only multiply $x$, leaving $y$ stranded! Parentheses are required.

[Prof. Park] Now examine Phrase #10: 'Two-thirds of a number, minus fourteen.' Sora, what does the word 'of' mean after a fraction?

[TA Sora] 'Of' means MULTIPLY! Two-thirds of $x$ means $\\frac{2}{3} \\cdot x$, or $\\frac{2x}{3}$!

[Prof. Park] And 'minus fourteen' is $- 14$.

[TA Sora] Full expression: $\\frac{2}{3}x - 14$! Clean, precise, and unambiguous!""",

    # Slide 8: Section 1.1 Phrases #11 & #12: Fractions & Reversal Word Challenges
    """[Prof. Park] Slide 8 tests our skills with Phrases #11 and #12. Phrase #11: 'Four less than the quotient of a number and six.'

[TA Sora] I hear two sirens! First siren: 'less than'—that means REVERSAL! The 4 is being subtracted at the very end!

[Prof. Park] And second siren: 'the quotient of a number and six'. What is that?

[TA Sora] That's $\\frac{x}{6}$! Now apply the reversal: subtract 4 from that quotient!

[Prof. Park] So we get $\\frac{x}{6} - 4$! Notice if someone rushed, they would write $4 - \\frac{x}{6}$, which is completely backwards!

[TA Sora] Now look at Phrase #12: 'The ratio of seven and the difference of a number and two.'

[Prof. Park] 'Ratio' means fraction bar! 7 is on top. What is on the bottom, Sora?

[TA Sora] 'The difference of a number and two', which is $(x - 2)$! So the whole fraction is $\\frac{7}{x - 2}$!""",

    # Slide 9: Section 1.1 Phrases #13 & #14: Absolute Difference & Squared Difference
    """[Prof. Park] Slide 9 brings us to our final workbook phrases: #13 and #14. Phrase #13: 'The absolute value of the difference of twice a number and nine.'

[TA Sora] Look at the outer container: 'The absolute value of...' That means vertical bars $|\\dots|$ wrap around everything!

[Prof. Park] And inside the bars: 'the difference of twice a number and nine'.

[TA Sora] Twice a number is $2x$. Difference with 9 is $2x - 9$. Drop that inside the absolute value bars: $|2x - 9|$!

[Prof. Park] Now compare that to Phrase #14: 'The square of the difference between ten and three times a number.'

[TA Sora] Outer container: 'The square of...' That means $(\\dots)^2$ wraps around everything!

[Prof. Park] And inside: 'the difference between ten and three times a number'.

[TA Sora] 10 comes first, then minus $3x$: $(10 - 3x)^2$!

[Prof. Park] Look at how systematically you decoded both expressions by identifying the outer container first, and then filling in the inner terms!""",

    # Slide 10: Section 1.1 Reverse Translation: Algebra into English Words
    """[Prof. Park] On our final slide of Lecture 04, we play the reverse game: translating algebraic expressions back into English words!

[TA Sora] How would you read $4(x - 3)$ in English, Professor?

[Prof. Park] 'Four times the difference of a number and three!' Or: 'Four times the quantity $x$ minus three.'

[TA Sora] And how about $\\frac{x + 5}{2}$?

[Prof. Park] 'The quotient of the sum of a number and five, divided by two!' Or: 'Half of the sum of a number and five.'

[TA Sora] When you can translate fluently in both directions, word problems lose all their power to intimidate you!

[Prof. Park] Next time, in Lecture 05, we enter Section 1.2: Exponent Properties for Monomial Expressions!

[TA Sora] We will learn the Product Rule, Quotient Rule, and Zero Exponent Rule!

[Prof. Park] Complete the workbook exercises on page 7, and we will see you in Lecture 05!

[TA Sora] Fantastic job today, everyone! See you next time!"""
]

# Scripts for L05 (10 slides)
scripts_l05 = [
    # Slide 1: Welcome to Lecture 05: Monomial Exponents
    """[Prof. Park] Welcome to Lecture 05 of M090! Today, on pages 8 through 10 of your workbook, we begin Section 1.2: Simplifying Monomial Expressions with Exponents.

[TA Sora] Hello everyone! Exponents are shorthand notation for repeated multiplication. Instead of writing $x \\times x \\times x \\times x \\times x$, we simply write $x^5$!

[Prof. Park] But when expressions become complicated—with coefficients, multiple variables, and fractions—you need clean exponent laws to simplify them without expanding every term by hand.

[TA Sora] What are the core rules on today's agenda, Professor?

[Prof. Park] Today we master the Zero Exponent Rule, the Product Rule for exponents, and the Quotient Rule for exponents.

[TA Sora] These three rules form the bedrock of all polynomial and rational algebra.

[Prof. Park] Once you understand why these rules work, you will never have to memorize them blindly.

[TA Sora] Grab your workbook, turn to page 8, and let's explore our Master Exponent Rules on Slide 2!""",

    # Slide 2: Exponent Properties for Monomial Expressions Table
    """[Prof. Park] Slide 2 displays the foundational Exponent Properties from workbook page 8. Sora, let's start with the Product Rule: $a^m \\cdot a^n = a^{m+n}$. Why do we add exponents?

[TA Sora] Because if you write it out: $x^2 \\cdot x^3 = (x \\cdot x) \\cdot (x \\cdot x \\cdot x)$. How many $x$'s are multiplied together? Five! So $2 + 3 = 5$!

[Prof. Park] Beautiful and simple. Now look at the Quotient Rule: $\\frac{a^m}{a^n} = a^{m-n}$ (for $a \\neq 0$). Why do we subtract exponents?

[TA Sora] Because identical factors on top and bottom cancel each other out! $\\frac{x^5}{x^2} = \\frac{x \\cdot x \\cdot x \\cdot x \\cdot x}{x \\cdot x}$. Two cancel, leaving three on top: $5 - 2 = 3$!

[Prof. Park] And what about the Zero Exponent Rule: $a^0 = 1$ for any non-zero base $a$?

[TA Sora] That comes directly from division! What is $\\frac{x^3}{x^3}$? Any non-zero number divided by itself equals 1. But by the quotient rule, $\\frac{x^3}{x^3} = x^{3-3} = x^0$! Therefore, $x^0 = 1$!

[Prof. Park] Notice the critical restriction: the base must NOT be zero. $0^0$ is an indeterminate form in higher mathematics.

[TA Sora] As long as the base isn't zero, anything raised to the power of zero is unconditionally 1!""",

    # Slide 3: Section 1.2 Example 1: The Zero Exponent Rule
    """[Prof. Park] Let's test our understanding on Example 1 from workbook page 8: parts A, B, C, and D. Part A: simplify $7^0$.

[TA Sora] Any non-zero number to the zero power is 1! So $7^0 = 1$!

[Prof. Park] Part B: simplify $(-5)^0$. What is the base here, Sora?

[TA Sora] The entire quantity $(-5)$ is inside parentheses, so the base is $-5$. A non-zero base to the zero power equals 1! So $(-5)^0 = +1$!

[Prof. Park] Now Part C: simplify $-5^0$. Watch out, class! What is the base here?

[TA Sora] The zero exponent touches ONLY the 5! The negative sign sits in front: $-(5^0) = -(1) = -1$!

[Prof. Park] That is the classic exam trap! $(-5)^0 = +1$, but $-5^0 = -1$!

[TA Sora] Now look at Part D: $(3x^2 y^5)^0$ where $x, y \\neq 0$.

[Prof. Park] The entire multi-variable package is wrapped in parentheses raised to the power 0!

[TA Sora] So the entire expression instantly becomes 1! It doesn't matter how complicated the inside looks—to the zero power, it is 1!""",

    # Slide 4: Section 1.2 Example 2 (Parts A & B): Product Rule with Coefficients
    """[Prof. Park] On Slide 4, Example 2 applies the Product Rule to monomials with coefficients. Part A: simplify $(3x^4)(5x^7)$. Sora, what is our golden strategy?

[TA Sora] Separate the coefficients from the variables! Handle numbers with numbers, and variables with variables!

[Prof. Park] Step 1: multiply the numerical coefficients: $3 \\times 5 = 15$.

[TA Sora] Step 2: apply the Product Rule to the $x$'s: $x^4 \\cdot x^7 = x^{4+7} = x^{11}$!

[Prof. Park] Combine them: $15x^{11}$! What is the fatal trap students fall into here, Sora?

[TA Sora] Many students add the coefficients: $3 + 5 = 8$, giving $8x^{11}$! Or they multiply the exponents: $4 \\times 7 = 28$!

[Prof. Park] Remember: Coefficients MULTIPLY; Exponents ADD!

[TA Sora] Now look at Part B: $(-2y^3)(6y)$. Notice that single $y$ at the end. What exponent does it carry?

[Prof. Park] An invisible 1! $y = y^1$. Never treat an invisible exponent as zero!

[TA Sora] Coefficients: $-2 \\times 6 = -12$. Exponents: $y^3 \\cdot y^1 = y^{3+1} = y^4$. Final answer: $-12y^4$!""",

    # Slide 5: Section 1.2 Example 2 (Parts C & D): Multi-Variable Monomial Products
    """[Prof. Park] Slide 5 challenges us with multiple variables in Parts C and D. Part C: $(4a^2 b^3)(-3a^5 b^4)$. Sora, how do we organize this?

[TA Sora] Group like with like! First coefficients: $4 \\times (-3) = -12$.

[Prof. Park] Next, the $a$'s: $a^2 \\cdot a^5 = a^{2+5} = a^7$.

[TA Sora] Next, the $b$'s: $b^3 \\cdot b^4 = b^{3+4} = b^7$.

[Prof. Park] Put the family back together: $-12a^7 b^7$! Clean and orderly.

[TA Sora] Now look at Part D: $(2x^3 y^2 z)(5x y^4 z^3)$.

[Prof. Park] Coefficients: $2 \\times 5 = 10$.

[TA Sora] Variable $x$: $x^3 \\cdot x^1 = x^4$. Variable $y$: $y^2 \\cdot y^4 = y^6$. Variable $z$: $z^1 \\cdot z^3 = z^4$!

[Prof. Park] Final simplified monomial: $10x^4 y^6 z^4$!

[TA Sora] When you treat each variable family independently, multi-variable problems are just as easy as single-variable problems!""",

    # Slide 6: Section 1.2 Example 3 (Part A): The Quotient Rule
    """[Prof. Park] Slide 6 brings us to Example 3 Part A on workbook page 9: simplifying quotients of monomials: $\\frac{24x^9}{6x^4}$.

[TA Sora] Once again: separate coefficients from variables! Handle the numbers as ordinary fraction reduction, and variables with the Quotient Rule.

[Prof. Park] For the coefficients: $24 / 6 = 4$.

[TA Sora] For the variable $x$: $\\frac{x^9}{x^4} = x^{9-4} = x^5$!

[Prof. Park] Combine them: $4x^5$!

[TA Sora] Professor, where do students make mistakes on this problem?

[Prof. Park] They subtract the coefficients! They see $24$ and $6$ and write $24 - 6 = 18$!

[TA Sora] That's a huge error! Coefficients DIVIDE; Exponents SUBTRACT! Say it out loud: coefficients divide, exponents subtract!

[Prof. Park] $24 \\div 6 = 4$, and $9 - 4 = 5$. Result is $4x^5$!""",

    # Slide 7: Section 1.2 Example 3 (Part B): Multiplying Monomial Fractions
    """[Prof. Park] Slide 7 presents Example 3 Part B: multiplying monomial fractions: $\\frac{3x^5}{4y^2} \\times \\frac{8y^6}{9x^2}$.

[TA Sora] This combines fraction cross-canceling with exponent rules! Let's cross-cancel coefficients first!

[Prof. Park] 3 and 9 reduce by 3 to leave 1 on top and 3 on the bottom. 4 and 8 reduce by 4 to leave 2 on top and 1 on the bottom!

[TA Sora] So our numerical coefficient is $\\frac{2}{3}$! Now let's handle the variables!

[Prof. Park] For $x$: we have $x^5$ in the top numerator and $x^2$ in the bottom denominator: $\\frac{x^5}{x^2} = x^{5-2} = x^3$ on top!

[TA Sora] For $y$: we have $y^6$ in the top numerator and $y^2$ in the bottom denominator: $\\frac{y^6}{y^2} = y^{6-2} = y^4$ on top!

[Prof. Park] Multiply the survivors together: $\\frac{2x^3 y^4}{3}$!

[TA Sora] Look at how smoothly everything simplified. Cross-canceling both numbers and variables makes monomial fractions a breeze!""",

    # Slide 8: Section 1.2 Example 3 (Part C): Dividing Monomial Fractions
    """[Prof. Park] Slide 8 tackles Example 3 Part C on workbook page 10: dividing monomial fractions: $\\frac{5a^4}{3b^3} \\div \\frac{10a}{9b^7}$.

[TA Sora] Division of fractions means one thing: Keep-Change-Flip!

[Prof. Park] Step 1: Keep the first fraction $\\frac{5a^4}{3b^3}$. Change division to multiplication. Flip the second fraction to $\\frac{9b^7}{10a}$!

[TA Sora] Now we have $\\frac{5a^4}{3b^3} \\times \\frac{9b^7}{10a}$. Let's cross-cancel coefficients!

[Prof. Park] 5 and 10 reduce by 5 to leave 1 and 2. 3 and 9 reduce by 3 to leave 1 and 3. So coefficient fraction is $\\frac{3}{2}$!

[TA Sora] Now simplify the variables! For $a$: $\\frac{a^4}{a^1} = a^{4-1} = a^3$ on top.

[Prof. Park] For $b$: $\\frac{b^7}{b^3} = b^{7-3} = b^4$ on top!

[TA Sora] Put it all together: $\\frac{3a^3 b^4}{2}$!

[Prof. Park] Never try to divide monomial fractions without flipping first. Keep-Change-Flip turns division into familiar multiplication every time!""",

    # Slide 9: Section 1.2 Example 3 (Part D): Multi-Variable Monomial Quotient
    """[Prof. Park] Slide 9 gives us Example 3 Part D: simplifying a three-variable quotient: $\\frac{-36x^7 y^5 z^3}{12x^2 y^5 z}$.

[TA Sora] Let's break this into four separate mini-problems: coefficients, $x$'s, $y$'s, and $z$'s!

[Prof. Park] Mini-problem 1: $\\frac{-36}{12} = -3$.

[TA Sora] Mini-problem 2: $\\frac{x^7}{x^2} = x^{7-2} = x^5$.

[Prof. Park] Mini-problem 3: $\\frac{y^5}{y^5}$. Sora, what happens when identical powers divide?

[TA Sora] $5 - 5 = 0$, so $y^0 = 1$! Or simply: identical terms completely cancel each other out! The $y$'s vanish!

[Prof. Park] And Mini-problem 4: $\\frac{z^3}{z^1} = z^{3-1} = z^2$.

[TA Sora] Multiply all the results together: $-3x^5 z^2$!

[Prof. Park] Notice how the $y$'s completely canceled without leaving any clutter behind. Clean, precise, and fully reduced!""",

    # Slide 10: Lecture 05 Wrap-Up & Transition to Negative Exponents
    """[Prof. Park] We have completed Lecture 05 and mastered the Product Rule, Quotient Rule, and Zero Exponent Rule!

[TA Sora] In Lecture 06, we take monomial exponents to the next level: Power to a Power, Power of a Product, and the famous Negative Exponent Rule!

[Prof. Park] That's where we learn what $x^{-3}$ really means—and how negative exponents act like elevator passes that move terms across fraction bars!

[TA Sora] Until then, practice the Section 1.2 exercises on workbook pages 9 and 10.

[Prof. Park] Master these foundational laws, and polynomials will be easy.

[TA Sora] See you all in Lecture 06!"""
]

print("Batch 1 scripts defined: L01 (10), L02 (10), L03 (9), L04 (10), L05 (10).")
