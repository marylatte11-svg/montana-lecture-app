import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
output_dir = r"c:\Oikos Univ\Montana_State_Univ\lectures"
os.makedirs(output_dir, exist_ok=True)

# ==============================================================================
# LECTURE 11: Solving Linear Equations (Basic & Multi-Step)
# ==============================================================================
l11 = r"""# Lecture 11: Solving Linear Equations: Properties of Equality
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.6 (Student Workbook p. 18)  
**Lecture Duration:** ~23 Minutes (8 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 11: The Balance Scale of Algebra](#slide-01-welcome-to-lecture-11-the-balance-scale-of-algebra)
- [Slide 02: Properties of Equality: Addition & Multiplication Properties](#slide-02-properties-of-equality)
- [Slide 03: Example 1A: Two-Step Linear Equation ($3x - 8 = -12$)](#slide-03-example-1a-two-step-linear-equation)
- [Slide 04: Example 1B: Negative Coefficient Trap ($6 - 4w = 15$)](#slide-04-example-1b-negative-coefficient-trap)
- [Slide 05: Example 1C: Combining Like Terms First ($y + 4 + 5y - 9 = 87$)](#slide-05-example-1c-combining-like-terms-first)
- [Slide 06: Example 1D: Multi-Term Linear Equation ($6r - 3r + 94 + 2r = 18$)](#slide-06-example-1d-multi-term-linear-equation)
- [Slide 07: Checking Your Solution by Substitution](#slide-07-checking-your-solution-by-substitution)
- [Slide 08: Lecture 11 Wrap-Up & Sora's Equation Solving Roadmap](#slide-08-lecture-11-wrap-up-and-soras-equation-solving-roadmap)

---

## Slide 01: Welcome to Lecture 11: The Balance Scale of Algebra
**Slide Type:** Lecture Orientation  
**Theme:** Solving for an unknown value while maintaining perfect balance  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Welcome to Lecture 11! Today we begin one of the central milestones of our entire course in Section 1.6: Solving Linear Equations.

[TA Sora] An equation is like a balanced scale. Whatever you do to the left side, you MUST do to the exact same degree to the right side!

[Prof. Park] If you add 5 to the left, you add 5 to the right. If you divide the left by 3, you divide the right by 3. Our goal is to isolate the variable all by itself on one side!

---

## Slide 02: Properties of Equality: Addition & Multiplication Properties
**Slide Type:** Core Mathematical Principles  
**LaTeX Anchor:** a = b \iff a + c = b + c, \qquad a = b \iff ac = bc \ (c \neq 0)

### 🎙️ English Lecture Script
[Prof. Park] To undo operations, we use inverse operations:
- Addition is undone by Subtraction.
- Subtraction is undone by Addition.
- Multiplication is undone by Division.
- Division is undone by Multiplication!

[TA Sora] Always peel away addition and subtraction first before dividing by the coefficient!

---

## Slide 03: Example 1A: Two-Step Linear Equation ($3x - 8 = -12$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.6 Example 1A (Workbook p. 18)  
**LaTeX Anchor:** 3x - 8 = -12

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Add 8 to both sides to isolate the variable term:} \\
& 3x - 8 + 8 = -12 + 8 \\
& 3x = -4 \\[0.5em]
\text{Step 2: } & \text{Divide both sides by the coefficient 3:} \\
& \dfrac{3x}{3} = \dfrac{-4}{3} \implies \mathbf{x = -\dfrac{4}{3}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Look at $3x - 8 = -12$. The 8 is subtracted, so we add 8 to both sides.

[TA Sora] $-12 + 8 = -4$. Then divide by 3: $x = -\frac{4}{3}$!

[Prof. Park] Leave it as an improper fraction $-\frac{4}{3}$! In algebra, improper fractions are our preferred format.

---

## Slide 04: Example 1B: Negative Coefficient Trap ($6 - 4w = 15$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.6 Example 1B (Workbook p. 18)  
**LaTeX Anchor:** 6 - 4w = 15

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Subtract 6 from both sides:} \\
& -4w = 15 - 6 \implies -4w = 9 \\[0.5em]
\text{Step 2: } & \text{Divide both sides by the NEGATIVE coefficient } -4: \\
& w = \dfrac{9}{-4} \implies \mathbf{w = -\dfrac{9}{4}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] What is the big trap in $6 - 4w = 15$?

[TA Sora] When students subtract 6, they forget the minus sign in front of $4w$! They write $4w = 9$!

[Prof. Park] But that minus sign belongs to the $4w$! It is $-4w = 9$. Dividing by $-4$ gives $w = -\frac{9}{4}$.

---

## Slide 05: Example 1C: Combining Like Terms First ($y + 4 + 5y - 9 = 87$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.6 Example 1C (Workbook p. 18)  
**LaTeX Anchor:** y + 4 + 5y - 9 = 87

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Combine like terms on the left side FIRST:} \\
& (y + 5y) + (4 - 9) = 87 \\
& 6y - 5 = 87 \\[0.5em]
\text{Step 2: } & \text{Add 5 to both sides: } 6y = 92 \\[0.5em]
\text{Step 3: } & \text{Divide by 6 and reduce: } y = \dfrac{92}{6} = \mathbf{\dfrac{46}{3}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Clean up each side of the equation before moving terms across the equal sign!

[TA Sora] $y + 5y = 6y$, and $4 - 9 = -5$. So $6y - 5 = 87$. Then add 5 to get 92, and divide by 6! Reduce by 2 to get $\frac{46}{3}$!

---

## Slide 06: Example 1D: Multi-Term Linear Equation ($6r - 3r + 94 + 2r = 18$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.6 Example 1D (Workbook p. 18)  
**LaTeX Anchor:** 6r - 3r + 94 + 2r = 18

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Combine like terms: } (6r - 3r + 2r) + 94 = 18 \implies 5r + 94 = 18 \\
\text{Step 2: } & \text{Subtract 94: } 5r = 18 - 94 = -76 \\
\text{Step 3: } & \text{Divide by 5: } \mathbf{r = -\dfrac{76}{5}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] $6r - 3r + 2r = 5r$. Subtract 94 to get $-76$.

[TA Sora] Divide by 5: $r = -\frac{76}{5}$. Done!

---

## Slide 07: Checking Your Solution by Substitution
**Slide Type:** Verification Strategy  
**Theme:** How to guarantee 100% on your exam by checking your work  

### 🎙️ English Lecture Script
[Prof. Park] In algebra, you never have to wonder if your answer is right. You can plug your solution back into the original equation!

[TA Sora] If left side equals right side, you KNOW you got 100%!

---

## Slide 08: Lecture 11 Wrap-Up & Sora's Equation Solving Roadmap
**Slide Type:** Conclusion & Summary  
- **1. Simplify:** Combine like terms on each side separately.
- **2. Isolate Variable Term:** Add or subtract constants.
- **3. Isolate Variable:** Multiply or divide by the coefficient.
- **Next Lecture:** Multi-step equations, variables on both sides, identities & contradictions!
"""

# ==============================================================================
# LECTURE 12: Multi-Step Equations & Special Cases
# ==============================================================================
l12 = r"""# Lecture 12: Solving Linear Equations: Multi-Step & Special Cases
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.6 (Student Workbook p. 19)  
**Lecture Duration:** ~24 Minutes (8 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 12: Conquering Multi-Step Equations](#slide-01-welcome-to-lecture-12-conquering-multi-step-equations)
- [Slide 02: Example 2A: Distribute First ($10(a - 5) + 2 = -3$)](#slide-02-example-2a-distribute-first)
- [Slide 03: Example 2B: Variables on Both Sides ($6(x - 2) - 8 = 3x - 20$)](#slide-03-example-2b-variables-on-both-sides)
- [Slide 04: The Zero Solution Reality: $x = 0$ is a Real Number!](#slide-04-the-zero-solution-reality)
- [Slide 05: Example 2C: The Identity ($2(7 - x) + 11 = 25 - 2x \implies$ All Real Numbers)](#slide-05-example-2c-the-identity)
- [Slide 06: Example 2D: The Contradiction (Variables Cancel & False Statement $\implies$ No Solution)](#slide-06-example-2d-the-contradiction)
- [Slide 07: Classification Matrix: Conditional vs. Identity vs. Contradiction](#slide-07-classification-matrix)
- [Slide 08: Lecture 12 Wrap-Up & Sora's Master Flowchart](#slide-08-lecture-12-wrap-up-and-soras-master-flowchart)

---

## Slide 01: Welcome to Lecture 12: Conquering Multi-Step Equations
**Slide Type:** Lecture Orientation  
**Theme:** Handling distribution, collecting variables on both sides, and uncovering special equation types  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Welcome to Lecture 12! Today we advance to multi-step equations where variables appear on both sides of the equal sign, and parentheses demand distribution.

[TA Sora] And even more exciting: we will discover what happens when all variables cancel out! Does it mean No Solution, or All Real Numbers?

[Prof. Park] Let’s master the complete workflow starting with Example 2A!

---

## Slide 02: Example 2A: Distribute First ($10(a - 5) + 2 = -3$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.6 Example 2A (Workbook p. 19)  
**LaTeX Anchor:** 10(a - 5) + 2 = -3

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Distribute 10:} \\
& 10a - 50 + 2 = -3 \\
\text{Step 2: } & \text{Combine like constants on left:} \\
& 10a - 48 = -3 \\
\text{Step 3: } & \text{Add 48 to both sides:} \\
& 10a = 45 \\
\text{Step 4: } & \text{Divide by 10 and reduce fraction:} \\
& a = \dfrac{45}{10} = \mathbf{\dfrac{9}{2}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Distribute the 10 first: $10a - 50$. Then combine $-50 + 2 = -48$.

[TA Sora] Add 48 to both sides: $10a = 45$. Divide by 10 and reduce by 5: $a = \frac{9}{2}$!

---

## Slide 03: Example 2B: Variables on Both Sides ($6(x - 2) - 8 = 3x - 20$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.6 Example 2B (Workbook p. 19)  
**LaTeX Anchor:** 6(x - 2) - 8 = 3x - 20

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Distribute 6 on left: } 6x - 12 - 8 = 3x - 20 \\
\text{Step 2: } & \text{Combine constants: } 6x - 20 = 3x - 20 \\
\text{Step 3: } & \text{Subtract } 3x \text{ from both sides: } 3x - 20 = -20 \\
\text{Step 4: } & \text{Add 20 to both sides: } 3x = 0 \\
\text{Step 5: } & \text{Divide by 3: } \mathbf{x = 0}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Look at $3x = 0$. Sora, what do students often write here?

[TA Sora] Students write: "No solution!" because they think zero means nothing exists!

[Prof. Park] But zero is a perfectly legitimate real number! If you check $x = 0$ in the original equation: $6(0-2)-8 = -20$, and $3(0)-20 = -20$. Both sides equal $-20$! So $x = 0$ is the TRUE solution!

---

## Slide 04: The Zero Solution Reality: $x = 0$ is a Real Number!
**Slide Type:** Conceptual Clarification  
**LaTeX Anchor:** 3x = 0 \implies x = \dfrac{0}{3} = 0 \quad (\text{VALID SOLUTION!})

### 🎙️ English Lecture Script
[Prof. Park] Never confuse $x = 0$ with "No Solution." Zero is a location on the number line—right between $-1$ and $+1$!

[TA Sora] Exactly! Having 0 dollars in your wallet is a definite number!

---

## Slide 05: Example 2C: The Identity ($2(7 - x) + 11 = 25 - 2x \implies$ All Real Numbers)
**Slide Type:** Special Case 1  
**Workbook Source:** Section 1.6 Example 2C (Workbook p. 19)  
**LaTeX Anchor:** 2(7 - x) + 11 = 25 - 2x \implies 25 = 25

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & 14 - 2x + 11 = 25 - 2x \\
\text{Step 2: } & 25 - 2x = 25 - 2x \\
\text{Step 3: } & \text{Add } 2x \text{ to both sides:} \\
& \mathbf{25 = 25} \quad (\text{Variables vanish, and statement is ALWAYS TRUE!}) \\
\text{Conclusion: } & \mathbf{\text{All Real Numbers } (\mathbb{R}) \text{ or } (-\infty, \infty)}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Look at $25 = 25$. The variable $x$ completely disappeared!

[TA Sora] And 25 ALWAYS equals 25! It is an **Identity**! Any number in the universe will make this equation true!

---

## Slide 06: Example 2D: The Contradiction (Variables Cancel & False Statement $\implies$ No Solution)
**Slide Type:** Special Case 2  
**LaTeX Anchor:** 3x - 5 = 3x + 8 \implies -5 = 8 \quad (\text{FALSE!})

### 🎙️ English Lecture Script
[Prof. Park] Now consider $3x - 5 = 3x + 8$. Subtract $3x$ from both sides, and you get $-5 = 8$.

[TA Sora] That is a lie! $-5$ never equals $8$! 

[Prof. Park] When variables cancel and you get a FALSE statement, it is a **Contradiction**. The answer is **No Solution** ($\emptyset$)!

---

## Slide 07: Classification Matrix: Conditional vs. Identity vs. Contradiction
**Slide Type:** Synthesis Table  

| Type | Outcome | Number of Solutions | Notation |
| :--- | :--- | :--- | :--- |
| **Conditional** | $x = \text{number}$ | Exactly One | $x = 5$ |
| **Identity** | True statement ($7=7$) | Infinitely Many | All Real Numbers ($\mathbb{R}$) |
| **Contradiction** | False statement ($0=9$) | None | No Solution ($\emptyset$) |

---

## Slide 08: Lecture 12 Wrap-Up & Sora's Master Flowchart
**Slide Type:** Conclusion & Summary  
- **Step 1:** Distribute parentheses.
- **Step 2:** Combine like terms on each side.
- **Step 3:** Move variables to one side, constants to the other.
- **Next Lecture:** Section 1.7: Solving Linear Equations with Fractions (The LCD Clearing Method)!
"""

# ==============================================================================
# LECTURE 13: Solving Fractional Equations (LCD Clearing)
# ==============================================================================
l13 = r"""# Lecture 13: Solving Linear Equations with Fractions (The LCD Clearing Method)
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.7 (Student Workbook pp. 20–22)  
**Lecture Duration:** ~24 Minutes (8 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 13: The Magic of Clearing Fractions](#slide-01-welcome-to-lecture-13-the-magic-of-clearing-fractions)
- [Slide 02: The Golden Equation Trick: Multiplying Every Term by the LCD](#slide-02-the-golden-equation-trick)
- [Slide 03: Example 1: Solving with Coefficients vs. Multiplying by Reciprocal ($\frac{2}{3}x = 8$)](#slide-03-example-1-solving-with-coefficients)
- [Slide 04: Example 2: Three-Denominator Clearing ($\frac{x}{4} + \frac{2}{3} = \frac{5}{6}$)](#slide-04-example-2-three-denominator-clearing)
- [Slide 05: Master Problem: Fractional Binomial Numerators ($\frac{3x-2}{5} - \frac{x+1}{2} = 1$)](#slide-05-master-problem-fractional-binomial-numerators)
- [Slide 06: The Fatal Trap: Forgetting to Multiply Integers on the Right Side!](#slide-06-the-fatal-trap)
- [Slide 07: Distributing Subtraction When Denominators Vanish](#slide-07-distributing-subtraction-when-denominators-vanish)
- [Slide 08: Lecture 13 Wrap-Up & Sora's Fraction-Clearing Checklist](#slide-08-lecture-13-wrap-up-and-soras-fraction-clearing-checklist)

---

## Slide 01: Welcome to Lecture 13: The Magic of Clearing Fractions
**Slide Type:** Lecture Orientation  
**Theme:** Eliminating all denominators in one single algebraic step!  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Welcome to Lecture 13! Today we cover Section 1.7: Solving Linear Equations with Fractions.

[TA Sora] This is my absolute favorite lecture in Unit 1! Because today, Professor Park teaches us the magic wand that makes every fraction disappear in step one!

[Prof. Park] That's right! You do not have to struggle with fractions through four steps. If you multiply BOTH sides of an equation by the LCD, every denominator cancels out immediately!

---

## Slide 02: The Golden Equation Trick: Multiplying Every Term by the LCD
**Slide Type:** Core Methodological Law  
**LaTeX Anchor:** \text{Multiply EVERY term on BOTH sides by the LCD!}

### 🎙️ English Lecture Script
[Prof. Park] Because an equation has an equal sign, we can multiply the entire equation by any non-zero number.

[TA Sora] And if we choose the LCD of all denominators, every denominator divides evenly into that number, leaving only whole numbers!

---

## Slide 03: Example 1: Solving with Coefficients vs. Multiplying by Reciprocal ($\frac{2}{3}x = 8$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.7 Example 1 & 2 (Workbook p. 20)  
**LaTeX Anchor:** \dfrac{2}{3}x = 8

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Method 1 (Reciprocal): } & \text{Multiply both sides by } \dfrac{3}{2}: \\
& \left(\dfrac{3}{2}\right) \cdot \left(\dfrac{2}{3}x\right) = 8 \cdot \left(\dfrac{3}{2}\right) \\
& x = \dfrac{24}{2} = \mathbf{12} \\[1em]
\text{Method 2 (Clear Denominator): } & \text{Multiply both sides by LCD } 3: \\
& 3 \cdot \left(\dfrac{2}{3}x\right) = 3 \cdot 8 \implies 2x = 24 \implies \mathbf{x = 12}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Notice how multiplying by 3 clears the fraction: $2x = 24$, giving $x = 12$ immediately!

---

## Slide 04: Example 2: Three-Denominator Clearing ($\frac{x}{4} + \frac{2}{3} = \frac{5}{6}$)
**Slide Type:** Single Problem Breakdown  
**LaTeX Anchor:** \dfrac{x}{4} + \dfrac{2}{3} = \dfrac{5}{6} \xrightarrow{\times 12} 3x + 8 = 10

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Find LCD of 4, 3, and 6:} \quad \mathbf{\text{LCD} = 12} \\
\text{Step 2: } & \text{Multiply EVERY term by 12:} \\
& 12\left(\dfrac{x}{4}\right) + 12\left(\dfrac{2}{3}\right) = 12\left(\dfrac{5}{6}\right) \\[0.5em]
\text{Step 3: } & \text{Divide before multiplying:} \\
& 3(x) + 4(2) = 2(5) \\
& 3x + 8 = 10 \\[0.5em]
\text{Step 4: } & \text{Solve the simple linear equation:} \\
& 3x = 2 \implies \mathbf{x = \dfrac{2}{3}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Look at Step 3: $12 \div 4 = 3$, $12 \div 3 = 4$, $12 \div 6 = 2$.

[TA Sora] The fractions are gone in one second! We are left with $3x + 8 = 10 \implies 3x = 2 \implies x = \frac{2}{3}$!

---

## Slide 05: Master Problem: Fractional Binomial Numerators ($\frac{3x-2}{5} - \frac{x+1}{2} = 1$)
**Slide Type:** Single Problem Master Breakdown  
**LaTeX Anchor:** \dfrac{3x-2}{5} - \dfrac{x+1}{2} = 1

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{LCD of 5 and 2 is } \mathbf{10}. \\
\text{Step 2: } & \text{Multiply EVERY term by 10 (including the 1 on the right!):} \\
& 10\left(\dfrac{3x-2}{5}\right) - 10\left(\dfrac{x+1}{2}\right) = 10(1) \\[0.5em]
\text{Step 3: } & \text{Cancel denominators (wrap numerators in parentheses!):} \\
& 2(3x - 2) - 5(x + 1) = 10 \\[0.5em]
\text{Step 4: } & \text{Distribute:} \\
& 6x - 4 - 5x - 5 = 10 \\
& x - 9 = 10 \implies \mathbf{x = 19}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] In Slide 5, the numerators have multiple terms: $(3x-2)$ and $(x+1)$.

[TA Sora] Notice that $-5$ distributes to BOTH $x$ and $+1$, giving $-5x - 5$!

[Prof. Park] $6x - 5x = x$, and $-4 - 5 = -9$. So $x - 9 = 10 \implies x = 19$!

---

## Slide 06: The Fatal Trap: Forgetting to Multiply Integers on the Right Side!
**Slide Type:** Common Pitfall Warning  
**LaTeX Anchor:** 10(1) = 10 \quad (\mathbf{\text{NOT }} 1!)

### 🎙️ English Lecture Script
[Prof. Park] Sora, what is the most common error students make when clearing fractions?

[TA Sora] They multiply the fractions by 10, but they leave the regular number on the right as 1!

[Prof. Park] Remember the balance scale: EVERY SINGLE TERM must be multiplied by the LCD!

---

## Slide 07: Distributing Subtraction When Denominators Vanish
**Slide Type:** Technique Focus  
**LaTeX Anchor:** -5(x + 1) = -5x - 5 \quad (\mathbf{\text{NOT }} -5x + 5!)

### 🎙️ English Lecture Script
[Prof. Park] Always place parentheses around numerators before clearing! It guards against the negative distribution error.

---

## Slide 08: Lecture 13 Wrap-Up & Sora's Fraction-Clearing Checklist
**Slide Type:** Conclusion & Summary  
- **1. Find the LCD** of ALL denominators.
- **2. Multiply every term** on both sides by the LCD.
- **3. Cancel denominators** and keep parentheses around numerators.
- **4. Distribute and solve!**
- **Next Lecture:** Section 1.8: Solving Formulas for a Specified Variable!
"""

# ==============================================================================
# LECTURE 14: Solving Formulas (Literal Equations)
# ==============================================================================
l14 = r"""# Lecture 14: Solving Formulas for a Specified Variable (Literal Equations)
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.8 (Student Workbook pp. 23–24)  
**Lecture Duration:** ~23 Minutes (8 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 14: Rearranging Real-World Formulas](#slide-01-welcome-to-lecture-14-rearranging-real-world-formulas)
- [Slide 02: What is a Literal Equation? Treating Letters as Numbers](#slide-02-what-is-a-literal-equation)
- [Slide 03: Example 1A & 1B: Solving for $y$ in Linear Equations ($3x + y = 8$ and $2x - 5y = 12$)](#slide-03-example-1a-and-1b-solving-for-y)
- [Slide 04: Example 1C: Factoring Out Variables ($Z = x + xwy$ solve for $y$)](#slide-04-example-1c-factoring-out-variables)
- [Slide 05: Example 1D: Monomial Formulas ($5xy = 19$ solve for $y$)](#slide-05-example-1d-monomial-formulas)
- [Slide 06: Example 2: Multi-Variable Formula ($a + b - c = d$ solve for $b$)](#slide-06-example-2-multi-variable-formula)
- [Slide 07: Famous Geometric & Physics Formulas: $P = 2l + 2w$ and $C = \frac{5}{9}(F - 32)$](#slide-07-famous-formulas)
- [Slide 08: Lecture 14 Wrap-Up & Sora's Formula Reorganization Protocol](#slide-08-lecture-14-wrap-up-and-soras-formula-protocol)

---

## Slide 01: Welcome to Lecture 14: Rearranging Real-World Formulas
**Slide Type:** Lecture Orientation  
**Theme:** Solving for target variables when everything is a letter!  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Welcome to Lecture 14! Today we explore Section 1.8: Solving Formulas for a Specified Variable.

[TA Sora] In science, engineering, and nursing, you rarely get equations with only one variable. You get formulas like $P = 2l + 2w$ or $C = \frac{5}{9}(F - 32)$!

[Prof. Park] And today we learn how to isolate any requested variable by treating all other letters as if they were plain numbers!

---

## Slide 02: What is a Literal Equation? Treating Letters as Numbers
**Slide Type:** Conceptual Anchor  
**LaTeX Anchor:** \text{If } 2x + 5 = 11 \implies 2x = 11 - 5 \implies x = \dfrac{11-5}{2} \\
\text{Then } ax + b = c \implies ax = c - b \implies x = \dfrac{c - b}{a}

### 🎙️ English Lecture Script
[Prof. Park] Compare the two equations on Slide 2. The steps are 100% identical!

[TA Sora] Subtract the constant term, then divide by the coefficient! Letters follow the exact same rules of algebra as numbers!

---

## Slide 03: Example 1A & 1B: Solving for $y$ in Linear Equations ($3x + y = 8$ and $2x - 5y = 12$)
**Slide Type:** Paired Problem Breakdown  
**Workbook Source:** Section 1.8 Example 1A & 1B (Workbook p. 23)  

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Problem 1A: } & 3x + y = 8 \\
& \text{Subtract } 3x: \quad \mathbf{y = -3x + 8} \\[1em]
\text{Problem 1B: } & 2x - 5y = 12 \\
& \text{Subtract } 2x: \quad -5y = -2x + 12 \\
& \text{Divide by } -5: \quad y = \dfrac{-2x + 12}{-5} = \mathbf{\dfrac{2}{5}x - \dfrac{12}{5}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] In Unit 2, we will graph lines in $y = mx + b$ form. Solving for $y$ is the exact skill you need!

[TA Sora] In 1B, divide each term by $-5$. A negative divided by negative gives positive $\frac{2}{5}x$, and $12 \div (-5) = -\frac{12}{5}$!

---

## Slide 04: Example 1C: Factoring Out Variables ($Z = x + xwy$ solve for $y$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.8 Example 1C (Workbook p. 23)  
**LaTeX Anchor:** Z = x + xwy \implies y = \dfrac{Z - x}{xw}

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Subtract } x \text{ to isolate the term containing } y: \\
& Z - x = xwy \\[0.5em]
\text{Step 2: } & \text{Divide both sides by the coefficients of } y \text{ (which are } xw\text{):} \\
& \mathbf{y = \dfrac{Z - x}{xw}}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] In $Z = x + xwy$, $y$ is multiplied by $x$ and $w$. 

[TA Sora] Subtract $x$ first: $Z - x = xwy$. Then divide by $xw$! Result: $y = \frac{Z-x}{xw}$!

---

## Slide 05: Example 1D: Monomial Formulas ($5xy = 19$ solve for $y$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.8 Example 1D (Workbook p. 23)  
**LaTeX Anchor:** 5xy = 19 \implies y = \dfrac{19}{5x}

### 🎙️ English Lecture Script
[Prof. Park] $5xy = 19$. To isolate $y$, divide both sides by $5x$.

[TA Sora] $y = \frac{19}{5x}$. Simple and direct!

---

## Slide 06: Example 2: Multi-Variable Formula ($a + b - c = d$ solve for $b$)
**Slide Type:** Single Problem Breakdown  
**Workbook Source:** Section 1.8 Example 2 (Workbook p. 23)  
**LaTeX Anchor:** a + b - c = d \implies b = d - a + c

### 🎙️ English Lecture Script
[Prof. Park] To isolate $b$, subtract $a$ and add $c$ to both sides.

[TA Sora] $b = d - a + c$! Everything on the other side changes signs when crossing the equal sign!

---

## Slide 07: Famous Geometric & Physics Formulas: $P = 2l + 2w$ and $C = \frac{5}{9}(F - 32)$
**Slide Type:** Applied Science Formulas  

### 💡 AI Step-by-Step Breakdown
$$\begin{aligned}
\text{Perimeter: } & P = 2l + 2w \implies P - 2l = 2w \implies \mathbf{w = \dfrac{P - 2l}{2}} \\[1em]
\text{Temperature: } & C = \dfrac{5}{9}(F - 32) \implies \dfrac{9}{5}C = F - 32 \implies \mathbf{F = \dfrac{9}{5}C + 32}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] When Montana winters drop down to $-20^\circ\text{F}$, this formula converts it straight into Celsius!

---

## Slide 08: Lecture 14 Wrap-Up & Sora's Formula Reorganization Protocol
**Slide Type:** Conclusion & Summary  
- **1. Target the Variable:** Highlight the letter you want.
- **2. Move Other Terms:** Add or subtract all terms without the target variable.
- **3. Divide by Coefficients:** Isolate your target variable completely.
- **Next Lecture:** Section 1.9 & Unit 1 Mastery Review: Linear Inequalities!
"""

# ==============================================================================
# LECTURE 15: Linear Inequalities & Unit 1 Review
# ==============================================================================
l15 = r"""# Lecture 15: Solving Linear Inequalities, Interval Notation & Unit 1 Grand Review
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.9 & Unit 1 Review (Student Workbook pp. 25–26)  
**Lecture Duration:** ~25 Minutes (10 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 15: The Grand Finale of Unit 1!](#slide-01-welcome-to-lecture-15-the-grand-finale-of-unit-1)
- [Slide 02: Inequality Symbols & Number Line Representation ($<, \le, >, \ge$)](#slide-02-inequality-symbols-and-number-line)
- [Slide 03: Interval Notation Mastery: Parentheses $( \ )$ vs. Brackets $[ \ ]$](#slide-03-interval-notation-mastery)
- [Slide 04: The Golden Rule of Inequalities: Flipping the Sign when Multiplying/Dividing by a Negative!](#slide-04-the-golden-rule-of-inequalities)
- [Slide 05: Example 1 from Workbook: Graphing Inequalities & Interval Notation](#slide-05-example-1-graphing-inequalities)
- [Slide 06: Solving Linear Inequalities: $-3x + 7 \le 19$](#slide-06-solving-linear-inequalities)
- [Slide 07: Multi-Step Inequality with Distribution: $4(2x - 1) > 10x + 8$](#slide-07-multi-step-inequality-with-distribution)
- [Slide 08: Compound Inequalities: $-3 < x < 1$ vs. $x < -7 \text{ or } x \ge 0$](#slide-08-compound-inequalities)
- [Slide 09: Unit 1 Grand Review & 10 Core Commandments Recap](#slide-09-unit-1-grand-review)
- [Slide 10: Unit 1 Mastery Celebration & Transition to Unit 2 (Graphing & Lines)](#slide-10-unit-1-mastery-celebration)

---

## Slide 01: Welcome to Lecture 15: The Grand Finale of Unit 1!
**Slide Type:** Milestone Celebration & Orientation  
**Theme:** Completing foundational algebra and conquering inequalities  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Welcome to Lecture 15, everyone! This is a tremendous milestone in our semester. Today we complete Unit 1!

[TA Sora] Fifteen lectures of pure algebraic power! You have conquered PEMDAS, fractions, polynomials, FOIL, and multi-step equations!

[Prof. Park] Today we cover Section 1.9: Linear Inequalities and Interval Notation, followed by our Unit 1 Grand Review to prepare you for your first mastery exam!

---

## Slide 02: Inequality Symbols & Number Line Representation ($<, \le, >, \ge$)
**Slide Type:** Definitions & Symbols  

| Symbol | Meaning | Circle on Number Line | Interval Bracket |
| :--- | :--- | :--- | :--- |
| **$<$ or $>$** | Strict inequality (less/greater than) | **Open Circle** $\circ$ | Parenthesis $( \ )$ |
| **$\le$ or $\ge$** | Inclusive (less/greater than or equal to) | **Solid Circle** $\bullet$ | Square Bracket $[ \ ]$ |
| **$\pm \infty$** | Positive or Negative Infinity | Arrow to edge | ALWAYS Parenthesis $( \ )$ |

---

## Slide 03: Interval Notation Mastery: Parentheses $( \ )$ vs. Brackets $[ \ ]$
**Slide Type:** Notation Standards  
**LaTeX Anchor:** x > 5 \implies (5, \infty), \qquad x \le -6 \implies (-\infty, -6]

### 🎙️ English Lecture Script
[Prof. Park] Always write interval notation from LEFT to RIGHT: $\text{Smaller Number, Larger Number}$.

[TA Sora] And infinity is not a number you can ever catch or hold—so infinity ALWAYS gets a soft parenthesis $( \ )$, never a bracket!

---

## Slide 04: The Golden Rule of Inequalities: Flipping the Sign when Multiplying/Dividing by a Negative!
**Slide Type:** Critical Law  
**LaTeX Anchor:** -2 < 5 \xrightarrow{\times (-1)} +2 > -5 \quad (\mathbf{\text{FLIP THE SIGN!}})

### 🎙️ English Lecture Script
[Prof. Park] Why do we flip the inequality sign when multiplying or dividing by a negative number?

[TA Sora] Because $-2$ is greater than $-5$. But if you multiply both by $-1$, $2$ is LESS than $5$! The entire number line flips backwards!

[Prof. Park] **Sora's Golden Rule:** Multiply or divide by a negative? FLIP THAT SIGN IMMEDIATELY!

---

## Slide 05: Example 1 from Workbook: Graphing Inequalities & Interval Notation
**Slide Type:** Paired Problem Breakdown  
**Workbook Source:** Section 1.9 Example 1 (Workbook p. 25)  

### 📝 Problem Statements & Solutions
$$\begin{aligned}
\text{A. } x > 5 &\implies \text{Open circle at 5, shade right} \implies \mathbf{(5, \infty)} \\
\text{B. } x \le -6 &\implies \text{Solid circle at -6, shade left} \implies \mathbf{(-\infty, -6]} \\
\text{C. } -3 \le x &\implies \text{Rewrite with } x \text{ first: } x \ge -3 \implies \mathbf{[-3, \infty)}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Look at Part C: $-3 \le x$. Always read inequalities from the variable's perspective!

[TA Sora] If $-3$ is less than or equal to $x$, that means $x$ is GREATER than or equal to $-3$! So $x \ge -3 \implies [-3, \infty)$!

---

## Slide 06: Solving Linear Inequalities: $-3x + 7 \le 19$
**Slide Type:** Single Problem Master Breakdown  
**LaTeX Anchor:** -3x + 7 \le 19

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Subtract 7 from both sides:} \\
& -3x \le 19 - 7 \implies -3x \le 12 \\[0.5em]
\text{Step 2: } & \text{Divide by } -3 \text{ and FLIP the inequality sign } (\le \ \to \ \ge): \\
& \dfrac{-3x}{-3} \ge \dfrac{12}{-3} \implies \mathbf{x \ge -4} \\[0.5em]
\text{Step 3: } & \text{Write in interval notation: } \mathbf{[-4, \infty)}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] In Step 2, we divided by $-3$. The $\le$ flipped to $\ge$!

[TA Sora] And $12 \div (-3) = -4$. So $x \ge -4$. In interval notation: $[-4, \infty)$!

---

## Slide 07: Multi-Step Inequality with Distribution: $4(2x - 1) > 10x + 8$
**Slide Type:** Single Problem Breakdown  
**LaTeX Anchor:** 4(2x - 1) > 10x + 8

### 💡 AI Step-by-Step Solution Breakdown
$$\begin{aligned}
\text{Step 1: } & \text{Distribute: } 8x - 4 > 10x + 8 \\
\text{Step 2: } & \text{Subtract } 10x: -2x - 4 > 8 \\
\text{Step 3: } & \text{Add 4: } -2x > 12 \\
\text{Step 4: } & \text{Divide by } -2 \text{ and FLIP sign } (> \ \to \ <): \\
& x < \dfrac{12}{-2} \implies \mathbf{x < -6} \\
\text{Interval: } & \mathbf{(-\infty, -6)}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Dividing by $-2$ flips $>$ into $<$. Answer: $(-\infty, -6)$!

---

## Slide 08: Compound Inequalities: $-3 < x < 1$ vs. $x < -7 \text{ or } x \ge 0$
**Slide Type:** Paired Concept Breakdown  
**Workbook Source:** Section 1.9 Example 1E & 1G (Workbook p. 25)  

### 📝 Problem Statements & Solutions
$$\begin{aligned}
\text{"AND" Compound (Trapped between): } & -3 < x < 1 \implies \mathbf{(-3, 1)} \\[0.8em]
\text{"OR" Compound (Separate intervals): } & x < -7 \text{ or } x \ge 0 \implies \mathbf{(-\infty, -7) \cup [0, \infty)}
\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] In $-3 < x < 1$, $x$ is sandwiched between $-3$ and $1$. Interval: $(-3, 1)$.

[TA Sora] In an "OR" inequality, the regions point away from each other. We use the union symbol $\cup$ to join them: $(-\infty, -7) \cup [0, \infty)$!

---

## Slide 09: Unit 1 Grand Review & 10 Core Commandments Recap
**Slide Type:** Comprehensive Synthesis  
1. **PEMDAS:** Left-to-right for $\times/\div$ and $+/-$.
2. **Negative Signs:** Always use protective parentheses $(-3)^2 = 9$.
3. **Division by Zero:** Always undefined ($\frac{N}{0} = \text{undefined}$).
4. **Exponent Product Rule:** Add exponents ($x^a \cdot x^b = x^{a+b}$).
5. **Negative Exponents:** Move across fraction bar ($x^{-n} = \frac{1}{x^n}$).
6. **Distributive Law:** Distribute negatives to every term: $-(a-b) = -a+b$.
7. **FOIL:** First, Outer, Inner, Last for multiplying binomials.
8. **Rational Addition:** LCD is mandatory; never add denominators!
9. **Fraction Clearing:** Multiply every term by the LCD.
10. **Inequality Flip:** Reverse sign when multiplying/dividing by negative.

---

## Slide 10: Unit 1 Mastery Celebration & Transition to Unit 2 (Graphing & Lines)
**Slide Type:** Course Milestone & Blessing  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Congratulations, students! You have completed all 15 lectures of Unit 1!

[TA Sora] You came into this class with math anxiety, and look at you now—solving multi-step fractional equations and interval inequalities like true mathematicians!

[Prof. Park] Take this confidence into your Unit 1 Mastery Exam. In Unit 2, we will step into the visual world of coordinate graphing, slope, and lines.

[TA Sora] We are so proud of your hard work. See you all in Unit 2!
"""

with open(os.path.join(output_dir, "lecture11.md"), "w", encoding="utf-8") as f:
    f.write(l11)
with open(os.path.join(output_dir, "lecture12.md"), "w", encoding="utf-8") as f:
    f.write(l12)
with open(os.path.join(output_dir, "lecture13.md"), "w", encoding="utf-8") as f:
    f.write(l13)
with open(os.path.join(output_dir, "lecture14.md"), "w", encoding="utf-8") as f:
    f.write(l14)
with open(os.path.join(output_dir, "lecture15.md"), "w", encoding="utf-8") as f:
    f.write(l15)

print("Generated lectures 11, 12, 13, 14, 15 successfully.")
