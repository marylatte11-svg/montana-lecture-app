import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
output_dir = r"c:\Oikos Univ\Montana_State_Univ\lectures"
os.makedirs(output_dir, exist_ok=True)

# ==============================================================================
# LECTURE 05: Exponent Rules
# ==============================================================================
l05 = r"""# Lecture 05: Exponent Properties for Monomial Expressions
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.2 (Student Workbook pp. 8–9)  
**Lecture Duration:** ~23 Minutes (8 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 05: The Superpowers of Exponents](#slide-01-welcome-to-lecture-05-the-superpowers-of-exponents)
- [Slide 02: Exponent Foundation: Base vs. Power ($a^n = a \cdot a \cdots a$)](#slide-02-exponent-foundation-base-vs-power)
- [Slide 03: The Product Rule: When Multiplying Bases, ADD Exponents ($a^m \cdot a^n = a^{m+n}$)](#slide-03-the-product-rule)
- [Slide 04: The Quotient Rule: When Dividing Bases, SUBTRACT Exponents ($\frac{a^m}{a^n} = a^{m-n}$)](#slide-04-the-quotient-rule)
- [Slide 05: Power to a Power Rule: MULTIPLY Exponents ($(a^m)^n = a^{mn}$)](#slide-05-power-to-a-power-rule)
- [Slide 06: Power of a Product & Quotient ($(ab)^n = a^n b^n$ and $(\frac{a}{b})^n = \frac{a^n}{b^n}$)](#slide-06-power-of-a-product-and-quotient)
- [Slide 07: Multi-Rule Simplification: $(3x^4 y^2)(-5x^3 y^7)$ and $\frac{12x^8}{4x^3}$](#slide-07-multi-rule-simplification)
- [Slide 08: Lecture 05 Wrap-Up & Sora's Exponent Cheat Sheet](#slide-08-lecture-05-wrap-up-and-soras-exponent-cheat-sheet)

---

## Slide 01: Welcome to Lecture 05: The Superpowers of Exponents
**Slide Type:** Lecture Orientation  
**Theme:** Mastering shortcut arithmetic with powers  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Welcome back students to Lecture 05! Today we enter Section 1.2: Simplifying Monomial Expressions with Exponents.

[TA Sora] Exponents are like shorthand notation for multiplication! Instead of writing $x \times x \times x \times x \times x$, we simply write $x^5$.

[Prof. Park] But when we start multiplying, dividing, and raising exponents to other powers, students often panic: "Do I add the exponents? Do I multiply them? Or do I subtract them?"

[TA Sora] Exactly! Today we are going to demystify all three major rules with clear visual proofs so you never mix them up again.

---

## Slide 02: Exponent Foundation: Base vs. Power ($a^n = a \cdot a \cdots a$)
**Slide Type:** Definition & Conceptual Anchor  
**LaTeX Anchor:** \text{In } a^n, \ a \text{ is the BASE, } n \text{ is the EXPONENT.}

### 🎙️ English Lecture Script
[Prof. Park] In any expression like $2x^3$, notice who the exponent belongs to! The exponent 3 belongs ONLY to the base $x$, NOT the coefficient 2.

[TA Sora] If we wanted 2 to have the power of 3 as well, we would need parentheses: $(2x)^3 = 8x^3$. Remember: exponents only touch what is immediately beneath their feet!

---

## Slide 03: The Product Rule: When Multiplying Bases, ADD Exponents ($a^m \cdot a^n = a^{m+n}$)
**Slide Type:** Core Rule & Problem Breakdown  
**Workbook Source:** Section 1.2 Table (Workbook p. 8)  
**LaTeX Anchor:** a^m \cdot a^n = a^{m+n}

### 📝 Problem Statement & Example
$$\text{Simplify: } \quad x^3 \cdot x^4$$

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{By Definition: } & x^3 = x \cdot x \cdot x, \qquad x^4 = x \cdot x \cdot x \cdot x \\
\text{Product: } & (x \cdot x \cdot x) \cdot (x \cdot x \cdot x \cdot x) = x^7 \\
\text{Rule Application: } & x^{3+4} = \mathbf{x^7} \quad (\text{KEEP the base, ADD the exponents!})
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Look at $x^3 \cdot x^4$. Why is it $x^7$ and not $x^{12}$?

[TA Sora] Because $x^3$ means 3 factors of $x$, and $x^4$ means 4 factors of $x$. When you multiply them together, you have a grand total of $3 + 4 = 7$ factors!

[Prof. Park] **Crucial Rule:** When multiplying like bases, KEEP the base unchanged and ADD the exponents!

---

## Slide 04: The Quotient Rule: When Dividing Bases, SUBTRACT Exponents ($\frac{a^m}{a^n} = a^{m-n}$)
**Slide Type:** Core Rule & Problem Breakdown  
**Workbook Source:** Section 1.2 Table (Workbook p. 8)  
**LaTeX Anchor:** \dfrac{a^m}{a^n} = a^{m-n}

### 📝 Problem Statement & Example
$$\text{Simplify: } \quad \dfrac{x^6}{x^2}$$

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Expanded Form: } & \dfrac{x \cdot x \cdot x \cdot x \cdot \cancel{x} \cdot \cancel{x}}{\cancel{x} \cdot \cancel{x}} = x \cdot x \cdot x \cdot x = x^4 \\
\text{Rule Application: } & x^{6-2} = \mathbf{x^4} \quad (\text{Subtract top exponent minus bottom exponent})
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Division is the opposite of multiplication. When multiplying means adding factors, dividing means canceling factors!

[TA Sora] Top minus bottom: $6 - 2 = 4$. So $\frac{x^6}{x^2} = x^4$!

---

## Slide 05: Power to a Power Rule: MULTIPLY Exponents ($(a^m)^n = a^{mn}$)
**Slide Type:** Core Rule & Problem Breakdown  
**Workbook Source:** Section 1.2 Table (Workbook p. 8)  
**LaTeX Anchor:** (a^m)^n = a^{m \cdot n}

### 📝 Problem Statement & Example
$$\text{Simplify: } \quad (x^3)^4$$

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Expanded: } & (x^3)^4 = x^3 \cdot x^3 \cdot x^3 \cdot x^3 = x^{3+3+3+3} = x^{12} \\
\text{Rule Application: } & x^{3 \cdot 4} = \mathbf{x^{12}} \quad (\text{One base raised to two powers: MULTIPLY!})
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Now students ask: "When DO we multiply the exponents?"

[TA Sora] When one single base is trapped inside parentheses with an exponent inside AND an exponent outside! $(x^3)^4$ means four bags of three, which is $3 \times 4 = 12$!

---

## Slide 06: Power of a Product & Quotient ($(ab)^n = a^n b^n$ and $(\frac{a}{b})^n = \frac{a^n}{b^n}$)
**Slide Type:** Core Rule & Problem Breakdown  
**Workbook Source:** Section 1.2 Table (Workbook p. 8)  
**LaTeX Anchor:** (ab)^n = a^n b^n, \quad \left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}

### 📝 Problem Statement
$$\text{Simplify: } \quad \text{A. } (2x^3)^4 \qquad \text{B. } \left(\dfrac{y^2}{3}\right)^3$$

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Part A: } & (2x^3)^4 = 2^4 \cdot (x^3)^4 = 16 \cdot x^{3 \cdot 4} = \mathbf{16x^{12}} \\
\text{Part B: } & \left(\dfrac{y^2}{3}\right)^3 = \dfrac{(y^2)^3}{3^3} = \mathbf{\dfrac{y^6}{27}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Notice in Part A: the coefficient 2 gets raised to the 4th power as well! $2^4 = 16$, NOT $2 \times 4 = 8$!

[TA Sora] Yes! Coefficients are regular numbers: $2 \times 2 \times 2 \times 2 = 16$. Exponents get multiplied: $3 \times 4 = 12$. So $16x^{12}$!

---

## Slide 07: Multi-Rule Simplification: $(3x^4 y^2)(-5x^3 y^7)$ and $\frac{12x^8}{4x^3}$
**Slide Type:** Paired Problem Breakdown  
**Workbook Source:** Section 1.2 Example 2 (Workbook p. 8)  

### 📝 Problem Statements & Solutions
$$\begin{aligned}
\text{A. } (3x^4 y^2)(-5x^3 y^7) &= [3 \cdot (-5)] \cdot (x^{4+3}) \cdot (y^{2+7}) = \mathbf{-15x^7 y^9} \\[0.8em]
\text{B. } \dfrac{12x^8}{4x^3} &= \left(\dfrac{12}{4}\right) \cdot x^{8-3} = \mathbf{3x^5}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] In Part A, treat coefficients and variables like separate teams. Coefficients multiply: $3 \times (-5) = -15$. Like variable exponents add: $4+3=7$ and $2+7=9$.

[TA Sora] And in Part B: divide coefficients: $12 \div 4 = 3$. Subtract exponents: $8 - 3 = 5$. Final answer: $3x^5$!

---

## Slide 08: Lecture 05 Wrap-Up & Sora's Exponent Cheat Sheet
**Slide Type:** Conclusion & Summary  
- **Multiplying bases?** $\implies$ Add exponents ($x^a \cdot x^b = x^{a+b}$).
- **Dividing bases?** $\implies$ Subtract exponents ($\frac{x^a}{x^b} = x^{a-b}$).
- **Power to a power?** $\implies$ Multiply exponents ($(x^a)^b = x^{ab}$).
- **Next Lecture:** Zero and Negative Exponents ($x^0 = 1$ and $x^{-n} = \frac{1}{x^n}$)!
"""

# ==============================================================================
# LECTURE 06: Zero & Negative Exponents
# ==============================================================================
l06 = r"""# Lecture 06: Zero & Negative Exponents: Simplifying Monomials
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.2 (Student Workbook pp. 9–11)  
**Lecture Duration:** ~24 Minutes (8 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 06: Demystifying Negative Exponents](#slide-01-welcome-to-lecture-06-demystifying-negative-exponents)
- [Slide 02: The Zero Exponent Rule ($a^0 = 1$) & The Division Proof](#slide-02-the-zero-exponent-rule)
- [Slide 03: The Negative Exponent Rule ($a^{-n} = \frac{1}{a^n}$): The Elevator Metaphor](#slide-03-the-negative-exponent-rule)
- [Slide 04: Simplifying Basic Negative Exponents: $\frac{x^{-4}}{y^{-3}}$ and $(5x^4)^{-2}$](#slide-04-simplifying-basic-negative-exponents)
- [Slide 05: Master Problem: Comprehensive Fraction Simplification ($\frac{-15x^3 y^{-2} z^0}{5x^{-2} y^4}$)](#slide-05-master-problem-comprehensive-fraction-simplification)
- [Slide 06: Example 5 from Workbook: Compound Powers with Negatives ($\left(\frac{2a^{-3}b^4}{6a^2 b^{-2}}\right)^2$)](#slide-06-example-5-compound-powers-with-negatives)
- [Slide 07: Common Trap: Negative Exponent vs. Negative Coefficient ($-4x^{-2}$ vs. $( -4x )^{-2}$)](#slide-07-common-trap-negative-exponent-vs-negative-coefficient)
- [Slide 08: Lecture 06 Wrap-Up & Sora's 3-Step Monomial Workflow](#slide-08-lecture-06-wrap-up-and-soras-3-step-monomial-workflow)

---

## Slide 01: Welcome to Lecture 06: Demystifying Negative Exponents
**Slide Type:** Lecture Orientation  
**Theme:** Understanding that negative exponents mean reciprocals, NOT negative numbers!  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Welcome to Lecture 06! Today we answer the big riddle: What does it mean to have a negative exponent like $x^{-3}$?

[TA Sora] Professor, the biggest mistake students make is thinking $x^{-3}$ makes the answer negative! They write $x^{-3} = -x^3$!

[Prof. Park] Yes, but exponents count repeated multiplication. A positive exponent multiplies; therefore, a negative exponent must do the inverse: REPEATED DIVISION!

[TA Sora] Exactly! A negative exponent doesn't change the sign of the number—it flips the number into the denominator!

---

## Slide 02: The Zero Exponent Rule ($a^0 = 1$) & The Division Proof
**Slide Type:** Conceptual Proof & Definition  
**LaTeX Anchor:** a^0 = 1 \quad (a \neq 0)

### 📝 Mathematical Proof
$$\dfrac{x^4}{x^4} = 1 \quad (\text{Any non-zero quantity divided by itself is } 1)$$
$$\text{Using Quotient Rule: } \dfrac{x^4}{x^4} = x^{4-4} = x^0 \implies \mathbf{x^0 = 1}$$

### 🎙️ English Lecture Script
[Prof. Park] Look at Slide 2. Any non-zero number to the zero power equals 1! Why?

[TA Sora] Because $\frac{x^4}{x^4}$ equals 1! But by our quotient rule, $4 - 4 = 0$. So $x^0$ MUST equal 1!

[Prof. Park] Notice: $(5,000,000)^0 = 1$. Even $(-17x^9 y^4)^0 = 1$!

---

## Slide 03: The Negative Exponent Rule ($a^{-n} = \frac{1}{a^n}$): The Elevator Metaphor
**Slide Type:** Methodological Metaphor  
**LaTeX Anchor:** a^{-n} = \dfrac{1}{a^n} \quad \text{and} \quad \dfrac{1}{a^{-n}} = a^n

### 🎙️ English Lecture Script
[Prof. Park] Sora, how do you explain negative exponents using your famous elevator metaphor?

[TA Sora] Think of a fraction bar as the floor of an elevator! A term with a negative exponent is unhappy with its current floor:
- If a term has a negative exponent on the top floor (numerator), send it down to the bottom floor, and its exponent turns POSITIVE!
- If it is unhappy in the basement (denominator) with a negative exponent, bring it up to the penthouse, and its exponent turns POSITIVE!

[Prof. Park] That's unforgettable! Moving across the fraction bar flips the sign of the exponent.

---

## Slide 04: Simplifying Basic Negative Exponents: $\frac{x^{-4}}{y^{-3}}$ and $(5x^4)^{-2}$
**Slide Type:** Paired Problem Breakdown  
**Workbook Source:** Section 1.2 Examples 3 & 4 (Workbook p. 10)  

### 📝 Problem Statements & Solutions
$$\begin{aligned}
\text{A. } \dfrac{x^{-4}}{y^{-3}} &\implies \text{Take the elevator: } x^{-4} \text{ goes down, } y^{-3} \text{ goes up:} \quad \mathbf{\dfrac{y^3}{x^4}} \\[0.8em]
\text{B. } (5x^4)^{-2} &= \dfrac{1}{(5x^4)^2} = \dfrac{1}{5^2 \cdot (x^4)^2} = \mathbf{\dfrac{1}{25x^8}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] In Part A: $x^{-4}$ moves to the bottom as $x^4$; $y^{-3}$ moves to the top as $y^3$. Result: $\frac{y^3}{x^4}$!

[TA Sora] In Part B: $(5x^4)^{-2}$. The entire parentheses have a negative exponent of $-2$, so the whole group moves to the denominator as $(5x^4)^2 = 25x^8$!

---

## Slide 05: Master Problem: Comprehensive Fraction Simplification ($\frac{-15x^3 y^{-2} z^0}{5x^{-2} y^4}$)
**Slide Type:** Single Problem Master Breakdown  
**LaTeX Anchor:** \dfrac{-15x^3 y^{-2} z^0}{5x^{-2} y^4}

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Evaluate } z^0 = 1 \implies \dfrac{-15x^3 y^{-2} (1)}{5x^{-2} y^4} \\[0.5em]
\text{Step 2: } & \text{Divide coefficients: } \dfrac{-15}{5} = \mathbf{-3} \\[0.5em]
\text{Step 3: } & \text{Move negative exponents across the fraction bar:} \\
& x^{-2} \text{ in denominator moves to numerator as } x^2 \implies x^3 \cdot x^2 = \mathbf{x^5} \\
& y^{-2} \text{ in numerator moves to denominator as } y^2 \implies y^4 \cdot y^2 = \mathbf{y^6} \\[0.5em]
\text{Step 4: } & \text{Combine: } \mathbf{-\dfrac{3x^5}{y^6}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Look at this master problem on Slide 5. Take it one piece at a time!

[TA Sora] Coefficients first: $-15 \div 5 = -3$. 
Next, $z^0 = 1$, so it disappears!
$x^{-2}$ on bottom travels to the top to join $x^3$, making $x^5$.
$y^{-2}$ on top travels to the bottom to join $y^4$, making $y^6$!

[Prof. Park] Result: $-\frac{3x^5}{y^6}$. Clean, beautiful, and completely error-free!

---

## Slide 06: Example 5 from Workbook: Compound Powers with Negatives ($\left(\frac{2a^{-3}b^4}{6a^2 b^{-2}}\right)^2$)
**Slide Type:** Single Problem Master Breakdown  
**Workbook Source:** Section 1.2 Example 5 (Workbook p. 11)  
**LaTeX Anchor:** \left(\dfrac{2a^{-3}b^4}{6a^2 b^{-2}}\right)^2

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{SIMPLIFY INSIDE PARENTHESES FIRST (PEMDAS!):} \\
& \text{Coefficients: } \dfrac{2}{6} = \dfrac{1}{3} \\
& a^{-3} \text{ moves down: } a^2 \cdot a^3 = a^5 \quad (\text{in denominator}) \\
& b^{-2} \text{ moves up: } b^4 \cdot b^2 = b^6 \quad (\text{in numerator}) \\
& \text{Inside becomes: } \left(\dfrac{b^6}{3a^5}\right)^2 \\[0.5em]
\text{Step 2: } & \text{Apply outer exponent of 2 to every factor:} \\
& \dfrac{(b^6)^2}{3^2 \cdot (a^5)^2} = \mathbf{\dfrac{b^{12}}{9a^{10}}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Many students try to distribute the outer exponent 2 immediately to all four terms. But Sora, what is our golden strategy?

[TA Sora] Simplify INSIDE first! Cleaning up inside makes the numbers tiny and manageable: $\frac{b^6}{3a^5}$.

[Prof. Park] Then squaring gives $(b^6)^2 = b^{12}$, $3^2 = 9$, and $(a^5)^2 = a^{10}$. Answer: $\frac{b^{12}}{9a^{10}}$!

---

## Slide 07: Common Trap: Negative Exponent vs. Negative Coefficient ($-4x^{-2}$ vs. $( -4x )^{-2}$)
**Slide Type:** Pitfall Warning  
**LaTeX Anchor:** -4x^{-2} = -\dfrac{4}{x^2} \quad \text{vs.} \quad (-4x)^{-2} = \dfrac{1}{(-4x)^2} = \dfrac{1}{16x^2}

### 🎙️ English Lecture Script
[Prof. Park] In $-4x^{-2}$, does the $-4$ move down to the denominator?

[TA Sora] NO! $-4$ is a coefficient with an invisible power of $+1$! Only $x$ has the exponent of $-2$. So $-4$ stays on top: $-\frac{4}{x^2}$!

[Prof. Park] Only if $-4$ is inside parentheses does it travel to the bottom!

---

## Slide 08: Lecture 06 Wrap-Up & Sora's 3-Step Monomial Workflow
**Slide Type:** Conclusion & Summary  
- **Step 1:** Simplify inside parentheses first.
- **Step 2:** Use the elevator to make all negative exponents positive.
- **Step 3:** Apply outer powers and combine like bases.
- **Next Lecture:** Section 1.3: Adding, Subtracting Polynomials & The Distributive Property!
"""

with open(os.path.join(output_dir, "lecture05.md"), "w", encoding="utf-8") as f:
    f.write(l05)
with open(os.path.join(output_dir, "lecture06.md"), "w", encoding="utf-8") as f:
    f.write(l06)

print("Generated lecture05.md and lecture06.md successfully.")
