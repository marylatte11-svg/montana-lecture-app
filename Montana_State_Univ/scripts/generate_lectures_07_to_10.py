import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
output_dir = r"c:\Oikos Univ\Montana_State_Univ\lectures"
os.makedirs(output_dir, exist_ok=True)

# ==============================================================================
# LECTURE 07: Polynomial Addition & Subtraction, Distributive Property
# ==============================================================================
l07 = r"""# Lecture 07: Adding and Subtracting Polynomials & The Distributive Property
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.3 (Student Workbook pp. 12–13)  
**Lecture Duration:** ~23 Minutes (8 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 07: The Anatomy of Polynomials](#slide-01-welcome-to-lecture-07-the-anatomy-of-polynomials)
- [Slide 02: Monomials, Binomials, Trinomials & Degree](#slide-02-monomials-binomials-trinomials-and-degree)
- [Slide 03: Identifying Like Terms: Same Variables with Identical Exponents](#slide-03-identifying-like-terms)
- [Slide 04: The Distributive Property ($a(b + c) = ab + ac$)](#slide-04-the-distributive-property)
- [Slide 05: Distributing Negative Signs: The Sign-Flip Trap ($ - (2x^2 - 5x + 3) $)](#slide-05-distributing-negative-signs)
- [Slide 06: Adding and Subtracting Polynomials (Horizontal & Vertical Methods)](#slide-06-adding-and-subtracting-polynomials)
- [Slide 07: Real-World Application: Perimeter of Algebraic Polygons](#slide-07-real-world-application-perimeter-of-algebraic-polygons)
- [Slide 08: Lecture 07 Wrap-Up & Sora's Like-Terms Rule](#slide-08-lecture-07-wrap-up-and-soras-like-terms-rule)

---

## Slide 01: Welcome to Lecture 07: The Anatomy of Polynomials
**Slide Type:** Lecture Orientation  
**Theme:** Combining algebraic building blocks with the distributive law  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Hello everyone, welcome to Lecture 07! Today we step from single monomials into the broader world of polynomials in Section 1.3.

[TA Sora] "Poly" means many, and "nomial" means term! So a polynomial is simply a mathematical expression made up of one or more terms combined by addition and subtraction!

[Prof. Park] In this lecture, we will master the Distributive Property and learn how to collect "Like Terms" cleanly without changing any exponents!

---

## Slide 02: Monomials, Binomials, Trinomials & Degree
**Slide Type:** Definitions & Terminology  
**Workbook Source:** Section 1.3 Key Terms (Workbook p. 12)  

| Name | Number of Terms | Examples |
| :--- | :--- | :--- |
| **Monomial** | Exactly 1 term | $7x, \ -5x^3 y, \ 14$ |
| **Binomial** | Exactly 2 terms | $3x - 5, \ x^2 - 16$ |
| **Trinomial** | Exactly 3 terms | $2x^2 + 7x - 4$ |
| **Polynomial** | Any number of terms | $x^4 - 3x^3 + 2x^2 - 8x + 1$ |

### 🎙️ English Lecture Script
[Prof. Park] Think of a bicycle (2 wheels $\implies$ binomial) and a tricycle (3 wheels $\implies$ trinomial). 

[TA Sora] And the degree of a term is the sum of its exponents! For example, $5x^3$ has degree 3.

---

## Slide 03: Identifying Like Terms: Same Variables with Identical Exponents
**Slide Type:** Core Concept  
**LaTeX Anchor:** 3x^2 \text{ and } 5x^2 \implies \text{LIKE TERMS!} \quad 3x^2 \text{ and } 3x^3 \implies \text{NOT LIKE TERMS!}

### 🎙️ English Lecture Script
[Prof. Park] Sora, can you add $3x^2 + 5x^2$?

[TA Sora] Yes! $3x^2 + 5x^2 = 8x^2$! Think of $x^2$ as a physical object—like 3 apples plus 5 apples equals 8 apples!

[Prof. Park] But notice: does the exponent change to $x^4$?

[TA Sora] NO! When you add apples, you don't get giant mutant square-apples! You just get 8 apples! Keep the variable and exponent completely unchanged when adding or subtracting like terms!

---

## Slide 04: The Distributive Property ($a(b + c) = ab + ac$)
**Slide Type:** Operational Rule  
**Workbook Source:** Section 1.3 (Workbook p. 12)  
**LaTeX Anchor:** a(b + c) = ab + ac

### 📝 Problem Statement
$$\text{Simplify by distributing: } \quad 4(3x - 5)$$

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Multiply outer term by the FIRST inside term: } 4 \cdot 3x = \mathbf{12x} \\
\text{Step 2: } & \text{Multiply outer term by the SECOND inside term: } 4 \cdot (-5) = \mathbf{-20} \\
\text{Step 3: } & \text{Combine: } \mathbf{12x - 20}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Think of the distributive property as greeting people at a party: if you walk into a room with two people $(3x - 5)$, you must shake hands with BOTH of them!

[TA Sora] $4 \times 3x = 12x$, and $4 \times (-5) = -20$. Result: $12x - 20$!

---

## Slide 05: Distributing Negative Signs: The Sign-Flip Trap ($ - (2x^2 - 5x + 3) $)
**Slide Type:** Common Pitfall Breakdown  
**LaTeX Anchor:** -(2x^2 - 5x + 3) = -2x^2 + 5x - 3

### 🎙️ English Lecture Script
[Prof. Park] What happens when there is a negative sign outside parentheses with NO number?

[TA Sora] There is an INVISIBLE 1! It is literally $-1(2x^2 - 5x + 3)$!

[Prof. Park] And distributing $-1$ reverses every single sign inside:
- Positive $2x^2$ becomes $-2x^2$
- Negative $5x$ flips to $+5x$
- Positive $3$ flips to $-3$!

[TA Sora] **Sora's Pro-Tip:** A negative in front of parentheses is a sign reverser! Flip every sign inside!

---

## Slide 06: Adding and Subtracting Polynomials (Horizontal & Vertical Methods)
**Slide Type:** Paired Problem Breakdown  
**Workbook Source:** Section 1.3 Examples (Workbook p. 13)  

### 📝 Problem Statements & Solutions
$$\begin{aligned}
\text{A. Add: } & (3x^2 - 5x + 7) + (2x^2 + 8x - 4) \\
&= (3x^2 + 2x^2) + (-5x + 8x) + (7 - 4) = \mathbf{5x^2 + 3x + 3} \\[1em]
\text{B. Subtract: } & (4x^2 - 3x + 7) - (2x^2 + 5x - 8) \\
&= 4x^2 - 3x + 7 - 2x^2 - 5x + 8 \\
&= (4x^2 - 2x^2) + (-3x - 5x) + (7 + 8) = \mathbf{2x^2 - 8x + 15}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Look at Part B: subtraction! The negative sign distributes to all three terms in the second polynomial.

[TA Sora] Notice $-(-8)$ becomes $+8$! So $7 + 8 = 15$. 

[Prof. Park] Then group: $4x^2 - 2x^2 = 2x^2$, and $-3x - 5x = -8x$. Result: $2x^2 - 8x + 15$!

---

## Slide 07: Real-World Application: Perimeter of Algebraic Polygons
**Slide Type:** Applied Word Problem  
**LaTeX Anchor:** P = \text{Side}_1 + \text{Side}_2 + \text{Side}_3 + \text{Side}_4

### 📝 Problem Statement
$$\text{Find the perimeter of a rectangle with length } L = 3x - 4 \text{ and width } W = 2x + 7.$$

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Perimeter Formula: } & P = 2L + 2W \\
\text{Substitute: } & P = 2(3x - 4) + 2(2x + 7) \\
\text{Distribute: } & P = 6x - 8 + 4x + 14 \\
\text{Combine Like Terms: } & (6x + 4x) + (-8 + 14) = \mathbf{10x + 6}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Perimeter means the distance all the way around the outside fence. Two lengths plus two widths!

[TA Sora] $2(3x - 4) + 2(2x + 7) = 6x - 8 + 4x + 14 = 10x + 6$!

---

## Slide 08: Lecture 07 Wrap-Up & Sora's Like-Terms Rule
**Slide Type:** Conclusion & Summary  
- **Like Terms:** Same letters with exact matching powers.
- **Adding/Subtracting:** Coefficients change; exponents NEVER change.
- **Distributing a Minus:** Flips every sign inside parentheses.
- **Next Lecture:** Section 1.4: Multiplying Polynomials (FOIL & Special Products)!
"""

# ==============================================================================
# LECTURE 08: Multiplying Polynomials (FOIL)
# ==============================================================================
l08 = r"""# Lecture 08: Multiplying Polynomials: FOIL Method & Special Products
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.4 (Student Workbook pp. 14–15)  
**Lecture Duration:** ~24 Minutes (8 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 08: The Power of FOIL](#slide-01-welcome-to-lecture-08-the-power-of-foil)
- [Slide 02: Monomial Times Polynomial: $3x(2x - 5)$](#slide-02-monomial-times-polynomial)
- [Slide 03: Binomial Times Binomial: The FOIL Acronym Explained](#slide-03-binomial-times-binomial-foil)
- [Slide 04: Example 1A & 1B: Standard FOIL Practice ($(2x+4)(3x+5)$ and $(x-4)(5x-1)$)](#slide-04-example-1a-and-1b-standard-foil-practice)
- [Slide 05: Multiplying with Outer Coefficients ($2(b-3)(b+4)$ and $4(w+2)(w-2)$)](#slide-05-multiplying-with-outer-coefficients)
- [Slide 06: Special Product 1: The Difference of Squares ($(a-b)(a+b) = a^2 - b^2$)](#slide-06-special-product-1-difference-of-squares)
- [Slide 07: Special Product 2: Squaring a Binomial ($(2y - 7)^2 \neq 4y^2 + 49$!)](#slide-07-special-product-2-squaring-a-binomial)
- [Slide 08: Lecture 08 Wrap-Up & Area vs. Perimeter Formulas](#slide-08-lecture-08-wrap-up-and-area-vs-perimeter)

---

## Slide 01: Welcome to Lecture 08: The Power of FOIL
**Slide Type:** Lecture Orientation  
**Theme:** Multiplying binomials and mastering shortcut patterns  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Welcome to Lecture 08! Today we tackle Section 1.4: Multiplying Polynomials.

[TA Sora] This is where algebra starts to look like serious college math! Today we learn the famous FOIL method.

[Prof. Park] FOIL is just repeated distribution: every term in the first parenthesis multiplies every term in the second parenthesis. Let's master it together!

---

## Slide 02: Monomial Times Polynomial: $3x(2x - 5)$
**Slide Type:** Foundation  
**LaTeX Anchor:** 3x(2x - 5) = 6x^2 - 15x

### 🎙️ English Lecture Script
[Prof. Park] Start simple: $3x(2x - 5)$.

[TA Sora] Distribute $3x$: $3x \times 2x = 6x^2$. And $3x \times (-5) = -15x$.

[Prof. Park] Notice that $x \cdot x$ gives $x^2$! Exponents DO add when you multiply!

---

## Slide 03: Binomial Times Binomial: The FOIL Acronym Explained
**Slide Type:** Methodological Framework  
**LaTeX Anchor:** (a + b)(c + d) = \mathbf{F} + \mathbf{O} + \mathbf{I} + \mathbf{L}

| Letter | Stands For | Meaning |
| :--- | :--- | :--- |
| **F** | **First** | Multiply the first term in each parenthesis ($a \cdot c$) |
| **O** | **Outer** | Multiply the two terms on the outside edges ($a \cdot d$) |
| **I** | **Inner** | Multiply the two terms on the inside ($b \cdot c$) |
| **L** | **Last** | Multiply the last term in each parenthesis ($b \cdot d$) |

### 🎙️ English Lecture Script
[Prof. Park] FOIL stands for First, Outer, Inner, Last.

[TA Sora] And almost always, the Outer and Inner terms are like terms that combine together!

---

## Slide 04: Example 1A & 1B: Standard FOIL Practice ($(2x+4)(3x+5)$ and $(x-4)(5x-1)$)
**Slide Type:** Paired Problem Breakdown  
**Workbook Source:** Section 1.4 Example 1A & 1B (Workbook p. 14)  

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Problem A: } & (2x + 4)(3x + 5) \\
\text{F: } & (2x)(3x) = 6x^2 \\
\text{O: } & (2x)(5) = 10x \\
\text{I: } & (4)(3x) = 12x \\
\text{L: } & (4)(5) = 20 \\
\text{Combine: } & 6x^2 + (10x + 12x) + 20 = \mathbf{6x^2 + 22x + 20} \\[1em]
\text{Problem B: } & (x - 4)(5x - 1) \\
\text{F, O, I, L: } & 5x^2 - x - 20x + 4 = \mathbf{5x^2 - 21x + 4}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] In Problem B, look at the signs: $-x - 20x = -21x$. And Last is $(-4)(-1) = +4$!

[TA Sora] Two negatives make a positive! Final answer: $5x^2 - 21x + 4$!

---

## Slide 05: Multiplying with Outer Coefficients ($2(b-3)(b+4)$ and $4(w+2)(w-2)$)
**Slide Type:** Paired Problem Breakdown  
**Workbook Source:** Section 1.4 Example 1C & 1D (Workbook p. 14)  

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Problem C: } & 2(b - 3)(b + 4) \\
\text{Step 1: FOIL inside: } & (b - 3)(b + 4) = b^2 + 4b - 3b - 12 = b^2 + b - 12 \\
\text{Step 2: Distribute 2: } & 2(b^2 + b - 12) = \mathbf{2b^2 + 2b - 24}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] When there is a number in front like $2(b-3)(b+4)$, FOIL the two binomials first, and then distribute the 2 at the very end!

[TA Sora] That avoids distributing the 2 twice by mistake!

---

## Slide 06: Special Product 1: The Difference of Squares ($(a-b)(a+b) = a^2 - b^2$)
**Slide Type:** Special Pattern  
**LaTeX Anchor:** (a - b)(a + b) = a^2 - b^2

### 📝 Problem Statement
$$\text{Multiply: } \quad 4(w + 2)(w - 2)$$

### 💡 AI Step-by-Step Breakdown
$$\begin{aligned}
\text{Inside: } & (w + 2)(w - 2) = w^2 - 2w + 2w - 4 = w^2 - 4 \quad (\text{Middle terms cancel!}) \\
\text{Multiply by 4: } & 4(w^2 - 4) = \mathbf{4w^2 - 16}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] When the binomials are twins with opposite signs $(w+2)(w-2)$, the Outer and Inner terms cancel: $-2w + 2w = 0$!

[TA Sora] This is called the **Difference of Squares**! It leaves only $w^2 - 4$. Times 4 gives $4w^2 - 16$!

---

## Slide 07: Special Product 2: Squaring a Binomial ($(2y - 7)^2 \neq 4y^2 + 49$!)
**Slide Type:** Critical Pitfall Breakdown  
**Workbook Source:** Section 1.4 Example 1E (Workbook p. 14)  
**LaTeX Anchor:** (2y - 7)^2 = (2y - 7)(2y - 7) = 4y^2 - 28y + 49

### 🎙️ English Lecture Script
[Prof. Park] Sora, warn everyone about the fatal error on $(2y - 7)^2$!

[TA Sora] Students try to distribute the exponent: $(2y)^2 - 7^2 = 4y^2 - 49$. That is **DEAD WRONG**!

[Prof. Park] Squaring means multiplying the binomial by itself: $(2y - 7)(2y - 7)$.

[TA Sora] FOIL gives $4y^2 - 14y - 14y + 49 = 4y^2 - 28y + 49$! Never forget the middle term!

---

## Slide 08: Lecture 08 Wrap-Up & Area vs. Perimeter Formulas
**Slide Type:** Conclusion & Summary  
- **Perimeter:** Add sides together (degree stays 1).
- **Area of Rectangle:** Multiply $\text{Length} \times \text{Width}$ using FOIL!
- **Next Lecture:** Section 1.5: Adding & Subtracting Rational Expressions!
"""

# ==============================================================================
# LECTURE 09: Rational Expressions Part 1: Common Denominators
# ==============================================================================
l09 = r"""# Lecture 09: Adding and Subtracting Rational Expressions (Part 1: Like Denominators)
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.5 (Student Workbook p. 16)  
**Lecture Duration:** ~22 Minutes (8 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 09: What is a Rational Expression?](#slide-01-welcome-to-lecture-09-what-is-a-rational-expression)
- [Slide 02: The Golden Rational Rule: $\frac{A}{C} \pm \frac{B}{C} = \frac{A \pm B}{C}$](#slide-02-the-golden-rational-rule)
- [Slide 03: Basic Like Denominators: $\frac{7}{y} - \frac{x}{y}$](#slide-03-basic-like-denominators)
- [Slide 04: Combining Variable Numerators: $\frac{2}{7r} + \frac{3}{7}$ (Wait, are these like?)](#slide-04-combining-variable-numerators)
- [Slide 05: The Subtraction Distribution Trap: $\frac{3x+1}{x-4} - \frac{x+9}{x-4}$](#slide-05-the-subtraction-distribution-trap)
- [Slide 06: Factoring to Reduce Final Answers: $\frac{2(x-4)}{x-4} = 2$](#slide-06-factoring-to-reduce-final-answers)
- [Slide 07: Restrictions on the Domain: When Denominator Equals Zero!](#slide-07-restrictions-on-the-domain)
- [Slide 08: Lecture 09 Wrap-Up & Sora's Rational Numerator Shield](#slide-08-lecture-09-wrap-up-and-soras-rational-numerator-shield)

---

## Slide 01: Welcome to Lecture 09: What is a Rational Expression?
**Slide Type:** Lecture Orientation  
**Theme:** Applying fraction rules to algebraic fractions  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Welcome to Lecture 09! Today we enter Section 1.5: Adding and Subtracting Rational Expressions.

[TA Sora] What does the word "rational" mean in math, Professor?

[Prof. Park] It comes from the word "ratio"—which means a fraction! A rational expression is simply a fraction where the top and bottom are polynomials.

[TA Sora] And just like numerical fractions, if the denominators match, adding them is super simple!

---

## Slide 02: The Golden Rational Rule: $\frac{A}{C} \pm \frac{B}{C} = \frac{A \pm B}{C}$
**Slide Type:** Core Operational Law  
**LaTeX Anchor:** \dfrac{A}{C} + \dfrac{B}{C} = \dfrac{A + B}{C}, \qquad \dfrac{A}{C} - \dfrac{B}{C} = \dfrac{A - B}{C}

### 🎙️ English Lecture Script
[Prof. Park] If the denominators match, write that single denominator down, and add or subtract the numerators.

[TA Sora] And never add the denominators together! The denominator stays $C$!

---

## Slide 03: Basic Like Denominators: $\frac{7}{y} - \frac{x}{y}$
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.5 Example 1B (Workbook p. 16)  
**LaTeX Anchor:** \dfrac{7}{y} - \dfrac{x}{y} = \dfrac{7 - x}{y}

### 🎙️ English Lecture Script
[Prof. Park] Look at $\frac{7}{y} - \frac{x}{y}$. The denominator is $y$ in both fractions.

[TA Sora] So we write $y$ in the denominator, and subtract numerators: $7 - x$. 

[Prof. Park] Can $7 - x$ be simplified further?

[TA Sora] No, 7 and $-x$ are not like terms! So the final answer is simply $\frac{7-x}{y}$!

---

## Slide 04: Combining Variable Numerators: $\frac{2}{7r} + \frac{3}{7}$ (Wait, are these like?)
**Slide Type:** Comparison  
**Workbook Source:** Section 1.5 Example 1C (Workbook p. 16)  
**LaTeX Anchor:** \dfrac{2}{7r} + \dfrac{3}{7} \implies \text{LCD is } 7r!

### 💡 AI Step-by-Step Breakdown
$$\begin{aligned}
\text{Denominators: } & 7r \text{ and } 7 \implies \text{LCD} = \mathbf{7r} \\
\text{Convert second fraction: } & \dfrac{3}{7} \cdot \dfrac{r}{r} = \dfrac{3r}{7r} \\
\text{Add: } & \dfrac{2}{7r} + \dfrac{3r}{7r} = \mathbf{\dfrac{2 + 3r}{7r}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Notice in $\frac{2}{7r} + \frac{3}{7}$, the denominators look almost the same, but the second one is missing the variable $r$!

[TA Sora] So we multiply the second fraction by $\frac{r}{r}$ to get a common denominator of $7r$. Answer: $\frac{2 + 3r}{7r}$!

---

## Slide 05: The Subtraction Distribution Trap: $\frac{3x+1}{x-4} - \frac{x+9}{x-4}$
**Slide Type:** Single Problem Master Breakdown  
**LaTeX Anchor:** \dfrac{3x+1}{x-4} - \dfrac{x+9}{x-4}

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Wrap each numerator in parentheses before subtracting:} \\
& \dfrac{(3x + 1) - (x + 9)}{x - 4} \\[0.5em]
\text{Step 2: } & \text{Distribute the negative sign to BOTH terms:} \\
& \dfrac{3x + 1 - x - 9}{x - 4} \\[0.5em]
\text{Step 3: } & \text{Combine like terms on top:} \\
& \dfrac{2x - 8}{x - 4}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] This is the #1 error on rational exams! That minus sign applies to the ENTIRE numerator $(x + 9)$!

[TA Sora] $- (x + 9) = -x - 9$! If you wrote $-x + 9$, your entire answer is wrong!

[Prof. Park] $3x - x = 2x$, and $1 - 9 = -8$. So we have $\frac{2x - 8}{x - 4}$.

---

## Slide 06: Factoring to Reduce Final Answers: $\frac{2(x-4)}{x-4} = 2$
**Slide Type:** Continuation & Simplification  
**LaTeX Anchor:** \dfrac{2x - 8}{x - 4} = \dfrac{2(x-4)}{x-4} = 2

### 🎙️ English Lecture Script
[Prof. Park] Are we finished with $\frac{2x - 8}{x - 4}$?

[TA Sora] Look at the top: $2x - 8$ has a GCF of 2! Factor it out: $2(x - 4)$!

[Prof. Park] And look at the denominator: $x - 4$!

[TA Sora] They match! The entire binomial factor $(x - 4)$ cancels out, leaving just the number **2**! That is so satisfying!

---

## Slide 07: Restrictions on the Domain: When Denominator Equals Zero!
**Slide Type:** Mathematical Restriction  
**LaTeX Anchor:** x - 4 \neq 0 \implies x \neq 4

### 🎙️ English Lecture Script
[Prof. Park] Remember our black hole rule from Lecture 01: You can NEVER divide by zero!

[TA Sora] In $\frac{2x-8}{x-4}$, if $x = 4$, the denominator becomes $4 - 4 = 0$!

[Prof. Park] That's why in rational expressions, we state the restriction: $x \neq 4$.

---

## Slide 08: Lecture 09 Wrap-Up & Sora's Rational Numerator Shield
**Slide Type:** Conclusion & Summary  
- **Like Denominators:** Combine numerators directly over the shared denominator.
- **Subtraction:** Always put parentheses around the second numerator: $-(B)$.
- **Factor & Reduce:** Check if the final numerator factors to cancel with the denominator!
- **Next Lecture:** Section 1.5 Part 2: Unlike Denominators & Finding the LCD!
"""

# ==============================================================================
# LECTURE 10: Rational Expressions Part 2: Unlike Denominators & LCD
# ==============================================================================
l10 = r"""# Lecture 10: Adding and Subtracting Rational Expressions (Part 2: Unlike Denominators)
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.5 (Student Workbook pp. 16–17)  
**Lecture Duration:** ~24 Minutes (8 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 10: The Art of Finding the Algebraic LCD](#slide-01-welcome-to-lecture-10-the-art-of-finding-the-algebraic-lcd)
- [Slide 02: Finding the LCD of Monomials (Coefficients & Highest Powers)](#slide-02-finding-the-lcd-of-monomials)
- [Slide 03: Example 2A: Variable Multiples ($\frac{5}{w} - \frac{7}{2w}$)](#slide-03-example-2a-variable-multiples)
- [Slide 04: Example 2B: Multiple Variable Coefficients ($\frac{1}{6x} + \frac{2}{9x}$)](#slide-04-example-2b-multiple-variable-coefficients)
- [Slide 05: Example 2C: Two Different Variables ($\frac{3}{y} + \frac{5}{x}$)](#slide-05-example-2c-two-different-variables)
- [Slide 06: Example 2D: Compound Monomials ($\frac{11y}{2x} - \frac{x}{5y}$)](#slide-06-example-2d-compound-monomials)
- [Slide 07: Example 2F: Integers and Variables ($\frac{4}{5} - \frac{9}{5w}$)](#slide-07-example-2f-integers-and-variables)
- [Slide 08: Lecture 10 Wrap-Up & Sora's 4-Step Rational Blueprint](#slide-08-lecture-10-wrap-up-and-soras-4-step-rational-blueprint)

---

## Slide 01: Welcome to Lecture 10: The Art of Finding the Algebraic LCD
**Slide Type:** Lecture Orientation  
**Theme:** Unifying denominators with different variables and numbers  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Welcome to Lecture 10! Today we tackle the true heavyweight champion of rational arithmetic: unlike denominators.

[TA Sora] When denominators have different numbers and letters, you cannot add or subtract until they speak the exact same language!

[Prof. Park] Today, we will build a reliable 4-step pipeline to find the Least Common Denominator (LCD) and build equivalent fractions every single time.

---

## Slide 02: Finding the LCD of Monomials (Coefficients & Highest Powers)
**Slide Type:** Methodological Anchor  
**LaTeX Anchor:** \text{LCD} = \text{LCM of numbers} \times \text{Highest power of each variable}

### 🎙️ English Lecture Script
[Prof. Park] To find the LCD of terms like $6x$ and $9x$:
1. Find the LCM of the numbers: LCM of 6 and 9 is 18.
2. Take each variable with its highest exponent: $x^1$.
3. LCD = $18x$!

[TA Sora] What about $2x$ and $5y$?
- LCM of 2 and 5 is 10.
- Variables are $x$ and $y$.
- LCD = $10xy$! It’s like gathering all ingredients for a recipe!

---

## Slide 03: Example 2A: Variable Multiples ($\frac{5}{w} - \frac{7}{2w}$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.5 Example 2A (Workbook p. 16)  
**LaTeX Anchor:** \dfrac{5}{w} - \dfrac{7}{2w}

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Find LCD of } w \text{ and } 2w \implies \mathbf{\text{LCD} = 2w} \\
\text{Step 2: } & \text{Multiply first fraction by } \dfrac{2}{2}: \\
& \dfrac{5 \cdot 2}{w \cdot 2} - \dfrac{7}{2w} = \dfrac{10}{2w} - \dfrac{7}{2w} \\
\text{Step 3: } & \text{Subtract numerators: } \dfrac{10 - 7}{2w} = \mathbf{\dfrac{3}{2w}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Look at $\frac{5}{w} - \frac{7}{2w}$. The second denominator already has $2w$. The first is just missing a 2!

[TA Sora] Multiply top and bottom by 2: $\frac{10}{2w}$. Now subtract: $10 - 7 = 3$. Final answer: $\frac{3}{2w}$!

---

## Slide 04: Example 2B: Multiple Variable Coefficients ($\frac{1}{6x} + \frac{2}{9x}$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.5 Example 2B (Workbook p. 16)  
**LaTeX Anchor:** \dfrac{1}{6x} + \dfrac{2}{9x}

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{LCD of } 6x \text{ and } 9x \text{ is } \mathbf{18x}. \\
\text{Step 2: } & \text{Build equivalent fractions:} \\
& \dfrac{1}{6x} \cdot \dfrac{3}{3} = \dfrac{3}{18x}, \qquad \dfrac{2}{9x} \cdot \dfrac{2}{2} = \dfrac{4}{18x} \\
\text{Step 3: } & \text{Add: } \dfrac{3 + 4}{18x} = \mathbf{\dfrac{7}{18x}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] To get 18x from 6x, multiply by 3. To get 18x from 9x, multiply by 2.

[TA Sora] $3 + 4 = 7$. Over $18x$, giving $\frac{7}{18x}$!

---

## Slide 05: Example 2C: Two Different Variables ($\frac{3}{y} + \frac{5}{x}$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.5 Example 2C (Workbook p. 16)  
**LaTeX Anchor:** \dfrac{3}{y} + \dfrac{5}{x}

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{LCD of } y \text{ and } x \text{ is } \mathbf{xy}. \\
\text{Step 2: } & \left(\dfrac{3}{y} \cdot \dfrac{x}{x}\right) + \left(\dfrac{5}{x} \cdot \dfrac{y}{y}\right) = \dfrac{3x}{xy} + \dfrac{5y}{xy} \\
\text{Step 3: } & \text{Combine: } \mathbf{\dfrac{3x + 5y}{xy}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] When variables have nothing in common like $y$ and $x$, their LCD is simply their product: $xy$.

[TA Sora] So $\frac{3}{y}$ gets $\frac{x}{x}$, and $\frac{5}{x}$ gets $\frac{y}{y}$. Result: $\frac{3x + 5y}{xy}$!

---

## Slide 06: Example 2D: Compound Monomials ($\frac{11y}{2x} - \frac{x}{5y}$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.5 Example 2D (Workbook p. 16)  
**LaTeX Anchor:** \dfrac{11y}{2x} - \dfrac{x}{5y}

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{LCD of } 2x \text{ and } 5y \text{ is } \mathbf{10xy}. \\
\text{Step 2: } & \left(\dfrac{11y}{2x} \cdot \dfrac{5y}{5y}\right) - \left(\dfrac{x}{5y} \cdot \dfrac{2x}{2x}\right) = \dfrac{55y^2}{10xy} - \dfrac{2x^2}{10xy} \\
\text{Step 3: } & \text{Combine: } \mathbf{\dfrac{55y^2 - 2x^2}{10xy}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] In Example 2D: $11y \times 5y = 55y^2$. And $x \times 2x = 2x^2$.

[TA Sora] Over $10xy$, giving $\frac{55y^2 - 2x^2}{10xy}$!

---

## Slide 07: Example 2F: Integers and Variables ($\frac{4}{5} - \frac{9}{5w}$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.5 Example 2F (Workbook p. 16)  
**LaTeX Anchor:** \dfrac{4}{5} - \dfrac{9}{5w}

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{LCD of } 5 \text{ and } 5w \text{ is } \mathbf{5w}. \\
\text{Step 2: } & \left(\dfrac{4}{5} \cdot \dfrac{w}{w}\right) - \dfrac{9}{5w} = \dfrac{4w - 9}{5w}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] The LCD is $5w$. Multiply $\frac{4}{5}$ by $\frac{w}{w}$ to get $\frac{4w}{5w}$.

[TA Sora] Subtract 9 to get $\frac{4w - 9}{5w}$! 

---

## Slide 08: Lecture 10 Wrap-Up & Sora's 4-Step Rational Blueprint
**Slide Type:** Conclusion & Summary  
- **1. Find the LCD** (LCM of numbers $\times$ highest powers of variables).
- **2. Multiply top & bottom** by whatever each fraction is missing.
- **3. Combine numerators** over the shared LCD.
- **4. Check if you can factor & reduce!**
- **Next Lecture:** Section 1.6: Solving Linear Equations!
"""

with open(os.path.join(output_dir, "lecture07.md"), "w", encoding="utf-8") as f:
    f.write(l07)
with open(os.path.join(output_dir, "lecture08.md"), "w", encoding="utf-8") as f:
    f.write(l08)
with open(os.path.join(output_dir, "lecture09.md"), "w", encoding="utf-8") as f:
    f.write(l09)
with open(os.path.join(output_dir, "lecture10.md"), "w", encoding="utf-8") as f:
    f.write(l10)

print("Generated lectures 07, 08, 09, 10 successfully.")
