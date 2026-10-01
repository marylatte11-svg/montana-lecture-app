import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
output_dir = r"c:\Oikos Univ\Montana_State_Univ\lectures"
os.makedirs(output_dir, exist_ok=True)

# ==============================================================================
# LECTURE 03: Evaluating Expressions
# ==============================================================================
l03 = r"""# Lecture 03: Evaluating Algebraic Expressions with Signed Numbers
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.1 (Student Workbook p. 6)  
**Lecture Duration:** ~24 Minutes (9 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 03: The Magic of Substitution](#slide-01-welcome-to-lecture-03-the-magic-of-substitution)
- [Slide 02: Golden Rule of Substitution: Protective Parentheses](#slide-02-golden-rule-of-substitution-protective-parentheses)
- [Slide 03: Example 1: Rational Fraction Evaluation ($\frac{d^2 - f^2}{d^2 + f^2}$ for $d=-2, f=5$)](#slide-03-example-1-rational-fraction-evaluation)
- [Slide 04: Example 2: Absolute Values & Cubes ($\frac{2x^2 + y^2}{|-10 + z^3|}$ for $x=-1, y=-3, z=2$)](#slide-04-example-2-absolute-values-and-cubes)
- [Slide 05: Example 3: The Discriminant Formula ($b^2 - 4ac$ for $a=5, b=-6, c=-3$)](#slide-05-example-3-the-discriminant-formula)
- [Slide 06: Example 4: The Quadratic Formula Expression ($\frac{-b + \sqrt{b^2-4ac}}{2a}$ for $a=1, b=7, c=-6$)](#slide-06-example-4-the-quadratic-formula-expression)
- [Slide 07: Example 5: Simplifying Radical Outcomes ($\frac{-b + \sqrt{b^2-4ac}}{2a}$ for $a=2, b=-10, c=8$)](#slide-07-example-5-simplifying-radical-outcomes)
- [Slide 08: Calculator Pitfalls vs. Paper Algebra](#slide-08-calculator-pitfalls-vs-paper-algebra)
- [Slide 09: Lecture 03 Wrap-Up & Sora's Substitution Checklist](#slide-09-lecture-03-wrap-up-and-soras-substitution-checklist)

---

## Slide 01: Welcome to Lecture 03: The Magic of Substitution
**Slide Type:** Lecture Orientation  
**Theme:** Converting variable formulas into numerical facts  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Hello students! Welcome to Lecture 03. Today we enter Section 1.1: Evaluating Algebraic Expressions.

[TA Sora] What does it actually mean to "evaluate" an expression, Professor Park?

[Prof. Park] In everyday English, to evaluate means to calculate the numerical value of something. In algebra, it means replacing every variable with a given number, and then following PEMDAS to find the single number it equals.

[TA Sora] But there is a huge trap here! Over 70% of errors in Section 1.1 happen when students substitute negative numbers without parentheses!

[Prof. Park] Exactly. Today, Sora and I will teach you the "Protective Parentheses" technique so that negative signs never sabotage your grade again!

---

## Slide 02: Golden Rule of Substitution: Protective Parentheses
**Slide Type:** Core Methodological Framework  
**LaTeX Anchor:** x = -3 \implies x^2 = (-3)^2 = 9 \quad (\text{NOT } -3^2 = -9)

### 📝 The Three Substitution Commandments
1. **Empty Pockets First:** Everywhere you see a variable, replace the letter with empty parentheses $( \ )$.
2. **Deposit the Number:** Place the given value inside the parentheses, keeping its sign intact.
3. **Follow PEMDAS:** Evaluate exponents, grouping symbols, and multiplication before addition and subtraction.

### 🎙️ English Lecture Script
[Prof. Park] Look at Slide 2. If $x = -3$, what is $x^2$?

[TA Sora] If you don't use parentheses, your paper says $-3^2$, which equals $-9$! But $x$ itself is negative three, so $x^2$ means $(-3) \times (-3) = +9$!

[Prof. Park] That is why Commandment #1 is so vital: write empty parentheses $( \ )^2$, and then drop $-3$ inside: $(-3)^2 = 9$.

[TA Sora] **Sora's Pro-Tip:** The parentheses are your body armor. Never substitute without armor!

---

## Slide 03: Example 1: Rational Fraction Evaluation ($\frac{d^2 - f^2}{d^2 + f^2}$ for $d=-2, f=5$)
**Slide Type:** Single Problem Master Breakdown  
**Workbook Source:** Section 1.1 Example 1 (Workbook p. 6)  
**LaTeX Anchor:** \dfrac{d^2 - f^2}{d^2 + f^2}

### 📝 Problem Statement
$$\text{Evaluate for } d = -2 \text{ and } f = 5: \quad \dfrac{d^2 - f^2}{d^2 + f^2}$$

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Substitute using protective parentheses:} \\
& \dfrac{(-2)^2 - (5)^2}{(-2)^2 + (5)^2} \\[0.5em]
\text{Step 2: } & \text{Evaluate the powers in the numerator and denominator independently:} \\
& (-2)^2 = 4, \qquad (5)^2 = 25 \\[0.5em]
\text{Step 3: } & \text{Perform the arithmetic on top and bottom:} \\
& \text{Numerator: } 4 - 25 = -21 \\
& \text{Denominator: } 4 + 25 = 29 \\[0.5em]
\text{Step 4: } & \text{Express as a single fraction: } \mathbf{-\dfrac{21}{29}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Look at Example 1: $\frac{d^2 - f^2}{d^2 + f^2}$ with $d=-2$ and $f=5$. Sora, why can't we just cancel $d^2$ with $d^2$?

[TA Sora] NO! That is the classic "Algebra Heartbreak"! You can only cancel common FACTORS that are multiplied, never terms that are added or subtracted!

[Prof. Park] Exactly. We must evaluate top and bottom separately. $(-2)^2$ is positive 4. $5^2$ is 25.

[TA Sora] On top: $4 - 25 = -21$. On bottom: $4 + 25 = 29$. Final answer: $-\frac{21}{29}$!

---

## Slide 04: Example 2: Absolute Values & Cubes ($\frac{2x^2 + y^2}{|-10 + z^3|}$ for $x=-1, y=-3, z=2$)
**Slide Type:** Single Problem Master Breakdown  
**Workbook Source:** Section 1.1 Example 2 (Workbook p. 6)  
**LaTeX Anchor:** \dfrac{2x^2 + y^2}{|-10 + z^3|}

### 📝 Problem Statement
$$\text{Evaluate if } x = -1, \ y = -3, \ z = 2: \quad \dfrac{2x^2 + y^2}{|-10 + z^3|}$$

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Substitute with parentheses:} \\
& \dfrac{2(-1)^2 + (-3)^2}{|-10 + (2)^3|} \\[0.5em]
\text{Step 2: } & \text{Evaluate powers:} \\
& (-1)^2 = 1, \quad (-3)^2 = 9, \quad (2)^3 = 8 \\[0.5em]
\text{Step 3: } & \text{Numerator: } 2(1) + 9 = 2 + 9 = \mathbf{11} \\
& \text{Denominator: } |-10 + 8| = |-2| = \mathbf{2} \\[0.5em]
\text{Step 4: } & \text{Final simplified fraction: } \mathbf{\dfrac{11}{2}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Example 2 has three variables, exponents, and absolute value bars!

[TA Sora] Remember: absolute value bars act like parentheses! You must calculate inside first: $-10 + 2^3 = -10 + 8 = -2$.

[Prof. Park] And the absolute value of $-2$ is positive $2$, because absolute value represents distance from zero on the number line.

[TA Sora] On top, $2(-1)^2 + (-3)^2 = 2(1) + 9 = 11$. So the whole fraction simplifies neatly to $\frac{11}{2}$!

---

## Slide 05: Example 3: The Discriminant Formula ($b^2 - 4ac$ for $a=5, b=-6, c=-3$)
**Slide Type:** Single Problem Master Breakdown  
**Workbook Source:** Section 1.1 Example 3 (Workbook p. 6)  
**LaTeX Anchor:** b^2 - 4ac

### 📝 Problem Statement
$$\text{For } a = 5, \ b = -6, \ c = -3, \text{ evaluate: } \quad b^2 - 4ac$$

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Set up with empty parentheses: } ( \ )^2 - 4( \ )( \ ) \\
\text{Step 2: } & \text{Substitute: } (-6)^2 - 4(5)(-3) \\[0.5em]
\text{Step 3: } & \text{Evaluate the square: } (-6)^2 = 36 \\[0.5em]
\text{Step 4: } & \text{Carefully track signs in multiplication: } \\
& -4 \cdot 5 = -20, \quad -20 \cdot (-3) = \mathbf{+60} \\[0.5em]
\text{Step 5: } & \text{Add: } 36 + 60 = \mathbf{96}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] This formula, $b^2 - 4ac$, will become your best friend when we reach Unit 3! It is the discriminant of the quadratic formula.

[TA Sora] Look at that multiplication: $-4(5)(-3)$. A negative times a positive times a negative gives a POSITIVE!

[Prof. Park] Yes! Students often write $36 - 60 = -24$ by mistake. But the two negative signs cancel each other out to make $+60$!

[TA Sora] $36 + 60 = 96$! Always count your negative signs before multiplying: two negatives make a positive!

---

## Slide 06: Example 4: The Quadratic Formula Expression ($\frac{-b + \sqrt{b^2-4ac}}{2a}$ for $a=1, b=7, c=-6$)
**Slide Type:** Single Problem Master Breakdown  
**Workbook Source:** Section 1.1 Example 4 (Workbook p. 6)  
**LaTeX Anchor:** \dfrac{-b + \sqrt{b^2 - 4ac}}{2a}

### 📝 Problem Statement
$$\text{Given } a = 1, \ b = 7, \ c = -6, \text{ find: } \quad \dfrac{-b + \sqrt{b^2 - 4ac}}{2a}$$

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Substitute all three values:} \\
& \dfrac{-(7) + \sqrt{(7)^2 - 4(1)(-6)}}{2(1)} \\[0.5em]
\text{Step 2: } & \text{Simplify inside the radical (radicand):} \\
& (7)^2 = 49, \quad -4(1)(-6) = +24 \\
& 49 + 24 = 73 \\[0.5em]
\text{Step 3: } & \text{Assemble the exact answer (73 is not a perfect square):} \\
& \mathbf{\dfrac{-7 + \sqrt{73}}{2}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] On Slide 6, we evaluate the full quadratic root expression with $a=1, b=7, c=-6$.

[TA Sora] Notice that under the radical, we have $49 - (-24) = 49 + 24 = 73$. Since 73 is not a square like 25 or 49, we leave it inside the square root symbol!

[Prof. Park] In college algebra, exact answers like $\frac{-7 + \sqrt{73}}{2}$ are preferred over rounded decimals unless a word problem asks for an approximation.

---

## Slide 07: Example 5: Simplifying Radical Outcomes ($\frac{-b + \sqrt{b^2-4ac}}{2a}$ for $a=2, b=-10, c=8$)
**Slide Type:** Single Problem Master Breakdown  
**Workbook Source:** Section 1.1 Example 5 (Workbook p. 6)  
**LaTeX Anchor:** \dfrac{-b + \sqrt{b^2 - 4ac}}{2a} \implies \text{Integer Result}

### 📝 Problem Statement
$$\text{Evaluate for } a = 2, \ b = -10, \ c = 8: \quad \dfrac{-b + \sqrt{b^2 - 4ac}}{2a}$$

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Substitute carefully (notice double negative!):} \\
& \dfrac{-(-10) + \sqrt{(-10)^2 - 4(2)(8)}}{2(2)} = \dfrac{10 + \sqrt{100 - 64}}{4} \\[0.5em]
\text{Step 2: } & \text{Evaluate under radical: } 100 - 64 = 36 \\[0.5em]
\text{Step 3: } & \text{Square root of 36 is 6:} \\
& \dfrac{10 + 6}{4} = \dfrac{16}{4} = \mathbf{4}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] In Example 5, $b$ is negative 10. Look at the leading term: $-(-10)$.

[TA Sora] The opposite of negative 10 is positive 10! 

[Prof. Park] And under the square root, $100 - 64 = 36$. $\sqrt{36}$ is a perfect square: 6!

[TA Sora] $10 + 6 = 16$, and $16 \div 4 = 4$! Look at how clean that turns out!

---

## Slide 08: Calculator Pitfalls vs. Paper Algebra
**Slide Type:** Study Skills & Technology  
**Theme:** Why typing directly into a phone calculator causes errors  

### 🎙️ English Lecture Script
[Prof. Park] Sora, what happens when students type $-10^2$ into their smartphone?

[TA Sora] It gives $-100$! Because smartphones follow raw coding logic: exponent first, then negative. 

[Prof. Park] But on paper, with your protective parentheses, $(-10)^2 = +100$.

[TA Sora] Always write your steps on paper first before touching a calculator!

---

## Slide 09: Lecture 03 Wrap-Up & Sora's Substitution Checklist
**Slide Type:** Conclusion & Summary  
- **Step 1:** Replace letters with parentheses $( \ )$.
- **Step 2:** Watch out for double negatives: $-(-b) = +b$.
- **Step 3:** Count negative factors in multiplication (2 negatives = positive).
- **Next Lecture:** Translating English words into algebra!
"""

with open(os.path.join(output_dir, "lecture03.md"), "w", encoding="utf-8") as f:
    f.write(l03)

print("Generated lecture03.md successfully.")
