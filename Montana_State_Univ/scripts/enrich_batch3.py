# -*- coding: utf-8 -*-
"""
enrich_batch3.py
Enriches Unit 1 Batch 3 (Lectures 11 to 15) to reach full 20-25 minute broadcast length (~2,280 - 2,500 words each).
"""
import sys
import json

sys.path.append('Montana_State_Univ/scripts')
from unit1_scripts_l11_l13 import SCRIPTS_L11, SCRIPTS_L12, SCRIPTS_L13
from unit1_scripts_l14_l15 import SCRIPTS_L14, SCRIPTS_L15

L11_ADD = {
    1: (
        "\nProf. Park: In the history of mathematics, the word 'algebra' comes from the 9th-century Arabic treatise 'Al-Kitab al-mukhtasar fi hisab al-jabr wal-muqabala' "
        "by the Persian mathematician Muhammad ibn Musa al-Khwarizmi. "
        "The word 'al-jabr' literally meant 'the restoration of broken parts' or 'setting a broken bone'—re-balancing two sides of a scale! "
        "When an equation is out of balance, algebra provides the precise surgical operations to restore absolute equilibrium.\n"
        "TA Sora: That historical root is so inspiring! Whenever students ask me why algebra is so strict about doing the exact same thing to both sides, "
        "I tell them: think of flying a backcountry bush plane across the Absaroka Range. "
        "If you load 50 pounds of survival gear onto the left wing, you MUST balance the aircraft by loading 50 pounds onto the right wing, or your plane will bank into the trees! "
        "Equations obey the exact same law of physical balance."
    ),
    2: (
        "\nProf. Park: Let's discuss why we reverse the order of operations when solving equations. "
        "In Section 1.0, we learned PEMDAS: Parentheses, Exponents, Multiplication and Division, Addition and Subtraction. "
        "PEMDAS is for EVALUATING when you already know all the numbers and want to find the final value. "
        "Solving an equation is the exact REVERSE process: you already know the final value (-12), and you are working backward through time to discover what mystery number x created it!\n"
        "TA Sora: Exactly! It's like wrapping a birthday gift: you put the toy in a box (multiplication), wrap it in paper (subtraction), and tie a bow. "
        "When unwrapping the gift, you don't break the toy first—you untie the bow, unwrap the paper (add 8), and open the box (divide by 3)! "
        "Reverse order of operations is the natural, logical unwrapping of an algebraic gift!"
    ),
    3: (
        "\nTA Sora: Here is an exam horror story from my first year as a TA: "
        "On a midterm question almost identical to 6 - 4w = 15, over 50% of the class wrote 4w = 9 instead of -4w = 9! "
        "They saw 6 - 4w and treated the minus sign like a decorative hyphen! "
        "A minus sign in algebra is never decorative! It is a negative charge that binds directly to the term immediately following it.\n"
        "Prof. Park: If you ever feel tempted to ignore that sign, rewrite the equation in standard form using the Commutative Property of Addition: "
        "-4w + 6 = 15! "
        "When you see -4w + 6 = 15, no one ever forgets that the 4 is negative! "
        "Rearranging terms to put the variable first is a bulletproof test-taking strategy."
    ),
    4: (
        "\nProf. Park: Let's emphasize Sora's 'Border Crossing Rule' for slide 4: "
        "Look at Example 1C: y + 4 + 5y - 9 = 87. "
        "y and 5y are both on the left side of the border (the equal sign). "
        "Because they are on the same side, they don't need passports! You simply combine them: 1y + 5y = 6y! "
        "Students who try to subtract 5y from both sides here end up with a double-subtraction catastrophe!\n"
        "TA Sora: That's right! You only use inverse operations when crossing the international border of the equal sign! "
        "If terms are inside the same country, just group them together normally like old friends. "
        "Organize your own house first before knocking on your neighbor's door!"
    ),
    5: (
        "\nProf. Park: In Example 2B, notice what happened when we reached 3x = 0: "
        "Many students panic and write: 'No solution' or 'Undefined.' "
        "Let's be 100% clear: 0 divided by 3 is ZERO: 0 / 3 = 0! "
        "Dividing zero by a number is completely legal and equals zero! "
        "Dividing by zero—like 3 / 0—is what is undefined!\n"
        "TA Sora: Zero is a perfectly respectable integer! "
        "If the temperature outside in Bozeman during January drops to exactly 0° Fahrenheit, that does NOT mean the thermometer broke or that temperature has no solution! "
        "It means the temperature is zero! "
        "Always embrace x = 0 as a proud, valid solution!"
    )
}

L12_ADD = {
    1: (
        "\nProf. Park: Let's provide three real-world analogies to make the three equation types unforgettable: "
        "1. Conditional equation: Imagine programming your GPS to drive to the Museum of the Rockies in Bozeman. "
        "There is one specific destination coordinate. The condition is met at that single point: x = 5. "
        "2. Contradiction: Imagine setting your GPS to drive directly from Bozeman to Honolulu, Hawaii by car! "
        "No matter what route you try, you cannot drive across the Pacific Ocean! It is physically impossible. "
        "Contradiction = No Solution (∅). "
        "3. Identity: Imagine asking: 'What points on the Yellowstone River are wet?' "
        "Every single drop of water on the entire river is wet! It is true by definition everywhere and for all time! "
        "Identity = All Real Numbers (ℝ)!\n"
        "TA Sora: Those analogies make the concepts click immediately! "
        "Remember: when you are taking an exam, never just write down 'Identity' without stating the solution set! "
        "The classification is 'Identity,' but the actual solution is 'All Real Numbers' or ℝ! "
        "Similarly, the classification is 'Contradiction,' but the solution is 'No Solution' or ∅!"
    ),
    2: (
        "\nProf. Park: Let's also look at the geometric visualization of these special cases: "
        "In Unit 2, we will graph linear equations as straight lines on the Cartesian coordinate plane. "
        "A conditional equation represents two lines that intersect at one single point (x, y). "
        "A contradiction represents two parallel lines with the same slope that run side-by-side forever and never cross! Because they never meet, they share no points: No Solution! "
        "An identity represents two equations that describe the exact same physical line lying directly on top of itself! Every single point on the line is a shared solution: All Real Numbers!\n"
        "TA Sora: Seeing algebra through geometry turns abstract symbols into visual maps. "
        "When the variables cancel and you see 25 = 12, your mental image should instantly be two parallel railroad tracks running through the Gallatin Canyon that never touch!"
    ),
    3: (
        "\nTA Sora: In Practice Problem 2, look at how the problem was disguised: "
        "r - 3 - 7 + r = 10 + 2r. "
        "Before combining like terms, the left side looked completely different from the right side! "
        "Only after combining r + r into 2r and -3 - 7 into -10 did the true nature of the equation emerge: 2r - 10 = 2r + 10. "
        "Notice that both sides had 2r, but the constants were different (-10 vs +10). "
        "Whenever both sides have the EXACT same variable coefficient but DIFFERENT constant terms, the variables will inevitably cancel, creating an automatic contradiction!\n"
        "Prof. Park: That is an expert pattern recognition tip, Sora! "
        "If variable coefficients match but constants differ, you know immediately it's a contradiction without doing five lines of arithmetic! "
        "And look at Problem 1: 3x - 2 = -9x + 15. The coefficients were +3 and -9. "
        "Since +3 does not equal -9, the variable CANNOT cancel out! It is guaranteed to be conditional. "
        "Checking variable coefficients before you calculate saves mental energy on exams!"
    ),
    4: (
        "\nProf. Park: In Practice Problem 3: 3(w - 4) = 3(w - 9) + 15, "
        "let's test our identity by plugging in a random number for w, say w = 10: "
        "Left side: 3(10 - 4) = 3(6) = 18. "
        "Right side: 3(10 - 9) + 15 = 3(1) + 15 = 3 + 15 = 18! "
        "18 = 18! "
        "Now test w = -5: "
        "Left: 3(-5 - 4) = 3(-9) = -27. "
        "Right: 3(-5 - 9) + 15 = 3(-14) + 15 = -42 + 15 = -27! "
        "-27 = -27!\n"
        "TA Sora: No matter what number you plug in—positive, negative, fraction, or decimal—both sides evaluate to the exact same value! "
        "That is the living definition of an identity."
    ),
    5: (
        "\nProf. Park: Let's review the critical distinction between Problem 5 and Problem 6: "
        "In Problem 5, -(-y - 28) = 7(y + 4) led to y = 0. "
        "Notice that the variable y did NOT disappear! We had y on the left and 7y on the right: 1y ≠ 7y! "
        "Because the coefficients were different (1 vs 7), the variable COULD NOT cancel! "
        "Whenever the coefficients of the variable are different on opposite sides of the equation, the equation is GUARANTEED to be conditional and have exactly one unique solution!\n"
        "TA Sora: That is a golden rule: Different variable coefficients mean ONE UNIQUE SOLUTION! "
        "Identical variable coefficients mean either NO SOLUTION (if constants differ) or ALL REAL NUMBERS (if constants match)! "
        "Let's write down this master classification summary in your lecture notebook:\n"
        "1. Coefficients different: Conditional (e.g. 5x + 2 = 3x - 8 -> 1 solution).\n"
        "2. Coefficients same, constants different: Contradiction (e.g. 4x + 7 = 4x - 1 -> No Solution ∅).\n"
        "3. Coefficients same, constants same: Identity (e.g. 2x + 6 = 2x + 6 -> All Real Numbers ℝ)!\n"
        "Prof. Park: Memorizing that 3-part classification matrix gives you 100% confidence on any equation classification question on Exam 1!"
    )
}

L13_ADD = {
    1: (
        "\nProf. Park: In physics and engineering research at Montana State University, mathematical models of fluid dynamics, aerodynamics, and circuit resistance "
        "routinely generate complex equations filled with rational coefficients. "
        "Senior engineering professors don't crunch fractions by hand across twenty lines of paper—they immediately clear denominators by multiplying through by the system's common modulus! "
        "What you are learning today in Section 1.7 is the exact industry-standard simplification algorithm used by professional engineers and scientific software.\n"
        "TA Sora: And notice the emotional shift when you learn this technique: "
        "Students go from dreading fraction problems to being excited when they see one on a quiz, because clearing fractions feels like magic! "
        "With one stroke of your pen, every fraction vanishes, leaving a simple integer puzzle."
    ),
    2: (
        "\nProf. Park: Let's emphasize why Method 1 (multiplying by the reciprocal) is only useful for single-term equations: "
        "If you have (3/4)x = 15, multiplying by 4/3 is great. "
        "But if you have (3/4)x + 2/5 = 7/10, what would you multiply by? You can't multiply by the reciprocal of 3/4 without turning the other terms into horrific fractions! "
        "That is why Method 2—clearing fractions using the LCD—is universally superior for general equations!\n"
        "TA Sora: Method 2 works on ALL equations, whether they have one term, three terms, or ten terms! "
        "Always master the universal method that never lets you down."
    ),
    3: (
        "\nTA Sora: Let's do another sanity check on Example 3B: (1/2)y + 3/4 = 10. "
        "We found y = 37/2. Let's plug it back into the original fraction equation to verify: "
        "(1/2)(37/2) + 3/4 = 37/4 + 3/4 = 40/4 = 10! "
        "10 = 10! The verification took ten seconds and proves our answer is rock solid!\n"
        "Prof. Park: And remember Sora's Golden Warning: The integer 10 had to be multiplied by 4 to become 40. "
        "Think of distributing the LCD like distributing hot chocolate to campers around a campfire: "
        "You can't skip the camper sitting on the right just because they didn't bring a fraction cup! "
        "Every single term gets a cup of LCD!"
    ),
    4: (
        "\nProf. Park: In Example 3C, our denominators were 2, 7, and 4. "
        "Let's review how we found LCD = 28 using prime factorization: "
        "2 is prime: 2^1. "
        "7 is prime: 7^1. "
        "4 is 2^2. "
        "To build the LCD, we take the highest power of every prime factor: "
        "Highest power of 2 is 2^2 = 4. "
        "Highest power of 7 is 7^1 = 7. "
        "4 · 7 = 28! "
        "Prime factorization takes the guesswork out of finding the LCD, no matter how complicated the numbers are!\n"
        "TA Sora: And notice how cleanly 28 divided into every denominator: "
        "28/2 = 14. 28/7 = 4. 28/4 = 7. "
        "If your LCD doesn't divide evenly into every denominator, you made a mistake finding the LCD! "
        "The whole point of the LCD is that every denominator cancels into a whole integer."
    ),
    5: (
        "\nTA Sora: On slide 5, let's revisit why we did NOT multiply inside the parentheses: "
        "In (1/7)(x - 4), think of (x - 4) as a locked suitcase, and 1/7 is the luggage tag on the handle. "
        "When the airport scanner (14) multiplies the bag, it only multiplies the tag on the outside: 14 · (1/7) = 2! "
        "The suitcase (x - 4) remains safely locked until the next step! "
        "Multiplying both the outside and inside would be multiplying by 14 TWICE (which would be multiplying by 196)!\n"
        "Prof. Park: That suitcase analogy is unforgettable! Only multiply the outside coefficient factor by the LCD."
    ),
    6: (
        "\nProf. Park: In Example 3F, (x - 7)/8 = 5/6, many high school students are taught 'cross-multiplication': 6(x - 7) = 8 · 5 = 40. "
        "Notice that 6(x - 7) = 40 is 6x - 42 = 40, 6x = 82, x = 82/6 = 41/3! "
        "Cross-multiplication gives the exact same result, but it uses the common denominator 48 instead of the LEAST common denominator 24! "
        "Using LCD = 24 kept our numbers smaller (3x - 21 = 20) and prevented awkward reduction at the end!\n"
        "TA Sora: Clearing by LCD is the master technique that generalizes to all rational equations in college algebra!"
    )
}

L14_ADD = {
    1: (
        "\nProf. Park: In civil engineering, environmental science, and business management, real equations are almost always literal formulas. "
        "For example, the Manning formula calculates open-channel water velocity in irrigation canals across the Gallatin Valley based on channel slope, roughness, and hydraulic radius. "
        "An engineer rarely needs to solve for velocity; they already know the target water flow rate, and they need to solve for the channel slope S or roughness coefficient n! "
        "Rearranging formulas is the daily bread and butter of working professionals.\n"
        "TA Sora: That is why literal equations are so empowering. Once you isolate a formula for your target variable, "
        "you can plug in twenty different datasets into a spreadsheet and compute answers instantly without re-doing algebra every single time!"
    ),
    2: (
        "\nTA Sora: In Example 1B, 2x - 5y = 12, we isolated y to get y = (2/5)x - 12/5. "
        "Notice why we split the fraction into two separate terms: "
        "In Unit 2, we will graph linear equations using the slope-intercept form: y = mx + b. "
        "Here, m = 2/5 is the slope (the steepness of the line: rise 2, run 5), "
        "and b = -12/5 is the y-intercept (where the line crosses the vertical axis)! "
        "Solving literal equations for y is the exact skill that unlocks all of linear graphing in Unit 2!\n"
        "Prof. Park: Every topic in Unit 1 is purposefully laying the groundwork for Unit 2. Practice this isolation until it is second nature!"
    ),
    3: (
        "\nProf. Park: Let's look closely at Part C: Z = x + wxy; solve for y. "
        "Notice why students fail this problem: they try to divide by wx before subtracting x! "
        "If you divide by wx first, you would have to divide the x term as well: Z/(wx) = x/(wx) + y. That creates a fraction mess! "
        "Always isolate the entire term containing your target variable FIRST by adding or subtracting non-target terms, "
        "and ONLY THEN divide by the coefficient factors!\n"
        "TA Sora: Isolate the term first, then isolate the variable! That two-step rhythm guarantees success every time."
    ),
    4: (
        "\nTA Sora: In Part B: ax^2 + bx + c = 0; solve for b. "
        "Notice that x appears with an exponent of 2 in ax^2, but our target is b! "
        "Don't worry about the x^2—to variable b, ax^2 is just a single package term! "
        "Subtract ax^2, subtract c, and divide by x. "
        "Treating non-target variable clusters as single numbers is the mark of a mature algebra student."
    ),
    5: (
        "\nProf. Park: Let's look at the physics formula in Part D: t = d / r. "
        "If you drive from Bozeman to Billings on Interstate 90, the distance d is about 142 miles. "
        "If you want to make the trip in t = 2 hours, what average speed r must you maintain? "
        "Using our solved formula r = d / t: r = 142 / 2 = 71 miles per hour! "
        "Formulas give you direct control over real physical decisions.\n"
        "TA Sora: And notice the common pitfall: students see t = d/r and write r = d · t! "
        "Remember: since r was in the denominator, multiplying by r brings it to the numerator on the other side: rt = d. "
        "Then dividing by t gives r = d/t!"
    ),
    6: (
        "\nTA Sora: In Part E: P = 2L + 2W; solve for W. "
        "Let's see the pasture fencing example with real numbers: "
        "Suppose a Gallatin rancher has P = 1,000 feet of wooden post fencing and wants the pasture length to be L = 300 feet. "
        "Using our formula W = (P - 2L) / 2: "
        "W = (1000 - 2(300)) / 2 = (1000 - 600) / 2 = 400 / 2 = 200 feet! "
        "The pasture width must be 200 feet. "
        "Formula rearranged once, solved in ten seconds!\n"
        "Prof. Park: That is the beauty of applied mathematics."
    ),
    7: (
        "\nProf. Park: In Review Problem A: (y - 2)/5 = (3/2)y + 4/5, "
        "we multiplied by LCD = 10 to get 2(y - 2) = 15y + 8, leading to y = -12/13. "
        "Notice how literal equations and clearing fractions reinforce each other: "
        "Both skills require identifying the structural anatomy of an equation and systematically peeling away outer operations. "
        "In Lecture 15, we will conclude Unit 1 with inequalities!"
    )
}

L15_ADD = {
    1: (
        "\nProf. Park: Let's reflect on the number line to understand why the inequality symbol flips: "
        "Imagine a giant mirror sitting right at the origin, zero: x = 0. "
        "If you are standing at +3 and your friend is standing at +7, your friend is farther to the right: 3 < 7. "
        "Now reflect both of your positions across the mirror by multiplying by -1: "
        "You are now at -3, and your friend is at -7! "
        "On the negative side of the mirror, who is farther to the right? YOU ARE! -3 is closer to zero and farther right than -7! "
        "So -3 > -7! "
        "Multiplying by a negative literally flips the entire universe of numbers across the mirror, turning right into left and left into right!\n"
        "TA Sora: That mirror analogy makes it impossible to forget! "
        "Whenever a negative number multiplies or divides across an inequality, the world flips!"
    ),
    2: (
        "\nTA Sora: Let's review interval notation formatting: "
        "Interval notation ALWAYS reads from left to right—from smaller numbers to larger numbers! "
        "Never write (∞, 5) or (-6, -∞)! "
        "Negative infinity is the furthest possible destination to the left, so it must ALWAYS be on the left: (-∞, -6). "
        "Positive infinity is the furthest destination to the right, so it must ALWAYS be on the right: (5, ∞)!"
    ),
    3: (
        "\nProf. Park: In Examples 1C and 1D, notice why reading from the variable's perspective is essential: "
        "When students read -3 ≤ x from left to right as 'negative 3 is less than or equal to x', "
        "they hear the words 'less than' and immediately want to shade to the left! "
        "That is a fatal trap! "
        "Always turn around and read starting with the variable: 'x is GREATER than or equal to -3!' "
        "The wide opening of the inequality symbol faces x, which means x is the larger quantity, pointing to the right!"
    ),
    4: (
        "\nTA Sora: In agricultural applications across the Gallatin Valley, grain moisture content for winter wheat storage must be strictly between 12% and 14%: 12 < m < 14. "
        "If moisture exceeds 14%, grain molds and can spontaneously combust in grain elevators. "
        "If moisture drops below 12%, grain kernels crack during milling. "
        "Bounded intervals like (-3, 1) and [2, 3) define the safe operational zones in biology, chemistry, and manufacturing."
    ),
    5: (
        "\nProf. Park: Notice the union symbol ∪ in compound inequalities: "
        "In computer programming and database querying (like SQL), ∪ represents the OR operator. "
        "If a point belongs to either the left interval OR the right interval, it is accepted into the solution set! "
        "In contrast, the intersection symbol ∩ (an upside-down U) represents AND—where intervals overlap."
    ),
    6: (
        "\nTA Sora: In Example 2A: -6 + 3x ≤ -12 + 5x, "
        "what if a student subtracted 3x instead of 5x? "
        "Let's see: subtract 3x: -6 ≤ -12 + 2x. "
        "Add 12: 6 ≤ 2x. "
        "Divide by positive 2: 3 ≤ x! "
        "Reading from x: x ≥ 3! "
        "Notice that by moving the variable to the right, the coefficient was positive (+2), so they never had to divide by a negative or flip the sign! "
        "Both algebraic paths lead to the exact same interval [3, ∞)!"
    ),
    7: (
        "\nProf. Park: In Example 2D: 2 ≤ x / (-8) - 3, "
        "notice how clearing the negative denominator flips the symbol: "
        "5 ≤ x / (-8) multiplied by -8 gives -40 ≥ x, which is x ≤ -40! "
        "Let's check with a number in the interval, say x = -48: "
        "Right side: -48 / -8 - 3 = 6 - 3 = 3. "
        "Is 2 ≤ 3? Yes, 2 is less than 3! The inequality holds true!"
    ),
    8: (
        "\nTA Sora: Look at the visual contrast between Examples 2E and 2F: "
        "In 2E, dividing by -4 gives x ≤ -170: (-∞, -170]. "
        "In 2F, dividing by +4 gives x > 230: (230, ∞). "
        "That comparison shows why attention to negative signs is the hallmark of a true mathematician."
    ),
    9: (
        "\nProf. Park: As we close Unit 1, let's look at the incredible ground we have covered: "
        "From fractions, real numbers, and exponents in Sections 1.0 to 1.2, "
        "to polynomials and FOIL in Sections 1.3 and 1.4, "
        "to rational expressions in Section 1.5, "
        "and finally linear equations, clearing fractions, literal formulas, and inequalities in Sections 1.6 through 1.9! "
        "You have built an unshakeable mathematical foundation. "
        "In Unit 2, we will bring all of this algebra to life on the two-dimensional Cartesian plane. "
        "Thank you for your fantastic dedication, and we will see you in Unit 2!"
    )
}

# Apply additions
for slide, add_text in L11_ADD.items():
    k = str(slide)
    SCRIPTS_L11[k] = SCRIPTS_L11[k] + add_text

for slide, add_text in L12_ADD.items():
    k = str(slide)
    SCRIPTS_L12[k] = SCRIPTS_L12[k] + add_text

for slide, add_text in L13_ADD.items():
    k = str(slide)
    SCRIPTS_L13[k] = SCRIPTS_L13[k] + add_text

for slide, add_text in L14_ADD.items():
    k = str(slide)
    SCRIPTS_L14[k] = SCRIPTS_L14[k] + add_text

for slide, add_text in L15_ADD.items():
    k = str(slide)
    SCRIPTS_L15[k] = SCRIPTS_L15[k] + add_text

# Write updated files
with open('Montana_State_Univ/scripts/unit1_scripts_l11_l13.py', 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n')
    f.write('"""\nunit1_scripts_l11_l13.py\nHigh-volume 20-25 minute broadcast tiki-taka scripts for Lectures 11, 12, and 13.\n"""\n\n')
    f.write('SCRIPTS_L11 = ' + json.dumps(SCRIPTS_L11, indent=4, ensure_ascii=False) + '\n\n')
    f.write('SCRIPTS_L12 = ' + json.dumps(SCRIPTS_L12, indent=4, ensure_ascii=False) + '\n\n')
    f.write('SCRIPTS_L13 = ' + json.dumps(SCRIPTS_L13, indent=4, ensure_ascii=False) + '\n')

with open('Montana_State_Univ/scripts/unit1_scripts_l14_l15.py', 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n')
    f.write('"""\nunit1_scripts_l14_l15.py\nHigh-volume 20-25 minute broadcast tiki-taka scripts for Lectures 14 and 15.\n"""\n\n')
    f.write('SCRIPTS_L14 = ' + json.dumps(SCRIPTS_L14, indent=4, ensure_ascii=False) + '\n\n')
    f.write('SCRIPTS_L15 = ' + json.dumps(SCRIPTS_L15, indent=4, ensure_ascii=False) + '\n')

print("Batch 3 enrichment complete.")
