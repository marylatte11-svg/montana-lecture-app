const fs = require('fs');

// Full code generator for L07 to L15
// 100% faithful to Gallatin College MSU M090 Student Workbook pages 12 to 26.

const L07 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Key Terms & Orientation",
    title: "Section 1.3: Adding & Subtracting Polynomials — Key Terms",
    subtitle: "Unit 1 • Lecture 07 • Section 1.3 (Workbook p. 12)",
    detail: "Lecture 07: Adding and Subtracting Polynomials & The Distributive Property",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Polynomial Terminology (Workbook p. 12)\n- **Polynomial:** A monomial, or two or more monomials combined by addition or subtraction.\n- **Monomial:** Exactly one term ($7x^2$, $-5$).\n- **Binomial:** Exactly two terms ($3x + 4$, $y^2 - 9$).\n- **Trinomial:** Exactly three terms ($ax^2 + bx + c$).\n- **Like Terms:** Terms having the **exact same variable(s) and exponent(s)**. Only coefficients are added/subtracted.",
    solution: "$$\\begin{aligned}\n\\text{Like Terms: } & 5x^2 \\text{ and } 3x^2 \\implies (5+3)x^2 = \\mathbf{8x^2} \\\\\n\\text{Unlike Terms: } & 5x^2 \\text{ and } 3x \\implies \\text{CANNOT be combined!}\n\\end{aligned}$$",
    pitfall: "**Sora's Warning:** When adding like terms, NEVER add or change the exponents! $3x^2 + 5x^2 = 8x^2$, NOT $8x^4$!",
    script: "[Prof. Park] Welcome to Lecture 07! Today we open to Section 1.3 on page 12 of your M090 Workbook: Adding and Subtracting Polynomials and the Distributive Property.\n\n[TA Sora] Monomial = 1 term, Binomial = 2 terms, Trinomial = 3 terms. Like terms have the exact same variables and powers.\n\n[Prof. Park] Remember: when you add like terms, you only add their coefficients. The powers never change!"
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1A & 1B: Combining Like Terms",
    subtitle: "Unit 1 • Lecture 07 • Section 1.3 Example 1A & 1B (Workbook p. 12)",
    detail: "Lecture 07: Adding and Subtracting Polynomials & The Distributive Property",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Simplify the polynomial by combining like terms (Workbook p. 12)\n$$\\text{A. } 6y + 12 - 7y$$\n$$\\text{B. } 9m^2 - 24m + 12m - 32$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & 6y + 12 - 7y \\\\\n&= (6y - 7y) + 12 \\\\\n&= (6 - 7)y + 12 = \\mathbf{-y + 12} \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & 9m^2 - 24m + 12m - 32 \\\\\n&= 9m^2 + (-24 + 12)m - 32 \\\\\n&= \\mathbf{9m^2 - 12m - 32}\n\\end{aligned}$$",
    pitfall: "**Sora's Watch-out:** In Part B, $9m^2$ has exponent 2, while $-24m$ has exponent 1. They are NOT like terms! Do not combine them into $-15m$!",
    script: "[Prof. Park] Look at Example 1A: $6y + 12 - 7y$. Sora, which terms can we combine?\n\n[TA Sora] The $y$-terms! $6y$ and $-7y$. $6 - 7 = -1$, so we get $-y + 12$.\n\n[Prof. Park] Exactly. In 1B, only $-24m$ and $+12m$ are like terms. That gives $9m^2 - 12m - 32$."
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1C & 1D: Multi-Term Polynomial Simplification",
    subtitle: "Unit 1 • Lecture 07 • Section 1.3 Example 1C & 1D (Workbook p. 12)",
    detail: "Lecture 07: Adding and Subtracting Polynomials & The Distributive Property",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Simplify the polynomial by combining like terms (Workbook p. 12)\n$$\\text{C. } 3n^2 - 17n - n^2 + 4n$$\n$$\\text{D. } 5x^3 + 3x^2 - 2x - 9 - 12x^3 - 10x + 4$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & (3n^2 - n^2) + (-17n + 4n) \\\\\n&= (3 - 1)n^2 + (-17 + 4)n = \\mathbf{2n^2 - 13n} \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & (5x^3 - 12x^3) + 3x^2 + (-2x - 10x) + (-9 + 4) \\\\\n&= (5 - 12)x^3 + 3x^2 + (-2 - 10)x + (-5) \\\\\n&= \\mathbf{-7x^3 + 3x^2 - 12x - 5}\n\\end{aligned}$$",
    pitfall: "**Sign Error Alert:** Don't forget that $-n^2$ means $-1n^2$. So $3n^2 - 1n^2 = 2n^2$!",
    script: "[Prof. Park] On Slide 3, group by descending powers. In 1C, $3n^2 - n^2 = 2n^2$, and $-17n + 4n = -13n$.\n\n[TA Sora] In 1D, grouping cubic, quadratic, linear, and constant terms gives $-7x^3 + 3x^2 - 12x - 5$."
  },
  {
    num: 4,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2A & 2B: Adding & Subtracting Polynomial Groups",
    subtitle: "Unit 1 • Lecture 07 • Section 1.3 Example 2A & 2B (Workbook p. 12)",
    detail: "Lecture 07: Adding and Subtracting Polynomials & The Distributive Property",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Perform the indicated operation and simplify (Workbook p. 12)\n$$\\text{A. } (5x^3 + 2x^2 - 13x) + (4x^3 - 10x^2 + 9)$$\n$$\\text{B. } (2y^6 + y^4 - y) - (8y^6 - 3y^4 + 9y)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A\\ (Addition):}\\quad & (5x^3 + 4x^3) + (2x^2 - 10x^2) - 13x + 9 \\\\\n&= \\mathbf{9x^3 - 8x^2 - 13x + 9} \\\\[1em]\n\\mathbf{Part\\ B\\ (Subtraction):}\\quad & \\text{Distribute the negative sign to every term in 2nd group!} \\\\\n&= 2y^6 + y^4 - y - 8y^6 + 3y^4 - 9y \\\\\n&= (2y^6 - 8y^6) + (y^4 + 3y^4) + (-y - 9y) \\\\\n&= \\mathbf{-6y^6 + 4y^4 - 10y}\n\\end{aligned}$$",
    pitfall: "**THE BIGGEST EXAM TRAP IN 1.3:** In Part B, distribute the minus to all terms! $-(8y^6 - 3y^4 + 9y) = -8y^6 + 3y^4 - 9y$. Watch the $+3y^4$!",
    script: "[Prof. Park] In Example 2B, notice that minus sign between the groups. Sora, what must every student do first?\n\n[TA Sora] Distribute the negative sign! Change every single sign inside the second group: $8y^6 \\to -8y^6$, $-3y^4 \\to +3y^4$, and $+9y \\to -9y$!\n\n[Prof. Park] Then combine like terms to get $-6y^6 + 4y^4 - 10y$."
  },
  {
    num: 5,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3A & 3B: Distributive Property with Monomials",
    subtitle: "Unit 1 • Lecture 07 • Section 1.3 Example 3A & 3B (Workbook p. 13)",
    detail: "Lecture 07: Adding and Subtracting Polynomials & The Distributive Property",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Perform the indicated operations and simplify fully (Workbook p. 13)\n$$\\text{A. } -2x(3x^2 + 8x - 4)$$\n$$\\text{B. } 2(8y - 5) + 7(-2y - 6)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & (-2x)(3x^2) + (-2x)(8x) + (-2x)(-4) \\\\\n&= -6x^{1+2} - 16x^{1+1} + 8x \\\\\n&= \\mathbf{-6x^3 - 16x^2 + 8x} \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & [2(8y) - 2(5)] + [7(-2y) + 7(-6)] \\\\\n&= (16y - 10) + (-14y - 42) \\\\\n&= (16y - 14y) + (-10 - 42) = \\mathbf{2y - 52}\n\\end{aligned}$$",
    pitfall: "**Negative Monomial Multiplication:** In 3A, $(-2x)(-4) = +8x$. A negative times a negative is POSITIVE!",
    script: "[Prof. Park] Turn to page 13, Example 3. In 3A, multiply $-2x$ across all three terms inside.\n\n[TA Sora] Add exponents when multiplying: $x \\cdot x^2 = x^3$, $x \\cdot x = x^2$. And $(-2x)(-4) = +8x$.\n\n[Prof. Park] In 3B, distribute $2$ and $7$, giving $16y - 10 - 14y - 42 = 2y - 52$."
  },
  {
    num: 6,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3C & 3D: Higher Degree Distribution",
    subtitle: "Unit 1 • Lecture 07 • Section 1.3 Example 3C & 3D (Workbook p. 13)",
    detail: "Lecture 07: Adding and Subtracting Polynomials & The Distributive Property",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Perform the indicated operations and simplify fully (Workbook p. 13)\n$$\\text{C. } -x(x^2 - 4) - 2(x^3 + 2x)$$\n$$\\text{D. } y(7y^2 + 4y - 9) - 3(8y^3 - 3y^2 - 4y)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & [-x(x^2) - x(-4)] + [-2(x^3) - 2(2x)] \\\\\n&= (-x^3 + 4x) - 2x^3 - 4x \\\\\n&= (-x^3 - 2x^3) + (4x - 4x) = \\mathbf{-3x^3} \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & (7y^3 + 4y^2 - 9y) - 24y^3 + 9y^2 + 12y \\\\\n&= (7y^3 - 24y^3) + (4y^2 + 9y^2) + (-9y + 12y) \\\\\n&= \\mathbf{-17y^3 + 13y^2 + 3y}\n\\end{aligned}$$",
    pitfall: "**Notice Cancellation in 3C:** $4x - 4x = 0$. The linear terms completely cancel out!",
    script: "[Prof. Park] Look at 3C: $-x^3 + 4x - 2x^3 - 4x$. The $+4x$ and $-4x$ cancel to zero, leaving $-3x^3$.\n\n[TA Sora] In 3D, distributing $-3$ flips all signs to $-24y^3 + 9y^2 + 12y$. Combining gives $-17y^3 + 13y^2 + 3y$!"
  },
  {
    num: 7,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3E & 3F: Nested Parentheses Simplification",
    subtitle: "Unit 1 • Lecture 07 • Section 1.3 Example 3E & 3F (Workbook p. 13)",
    detail: "Lecture 07: Adding and Subtracting Polynomials & The Distributive Property",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Simplify fully by clearing nested grouping symbols (Workbook p. 13)\n$$\\text{E. } 3 + 2(5x - 4(x - 9)) + 7x$$\n$$\\text{F. } 11x - 8(y + 5(y - 2(y - x)))$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ E:}\\quad & \\text{Innermost first: } -4(x - 9) = -4x + 36 \\\\\n& 3 + 2(5x - 4x + 36) + 7x = 3 + 2(x + 36) + 7x \\\\\n&= 3 + 2x + 72 + 7x = \\mathbf{9x + 75} \\\\[1em]\n\\mathbf{Part\\ F:}\\quad & \\text{Innermost: } -2(y - x) = -2y + 2x \\\\\n&= 11x - 8(y + 5(y - 2y + 2x)) \\\\\n&= 11x - 8(y + 5(-y + 2x)) \\\\\n&= 11x - 8(y - 5y + 10x) = 11x - 8(-4y + 10x) \\\\\n&= 11x + 32y - 80x = \\mathbf{-69x + 32y}\n\\end{aligned}$$",
    pitfall: "**Order of Operations:** In 3E, NEVER add $3 + 2 = 5$ at the start! Multiplication takes precedence over addition!",
    script: "[Prof. Park] In 3E and 3F, work from the inside out! In 3E, distribute $-4$ into $(x - 9)$ first.\n\n[TA Sora] Never do $3 + 2 = 5$ first—that breaks PEMDAS!\n\n[Prof. Park] In 3F, peel each layer from inside out to reach $-69x + 32y$."
  }
];

const L08 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Core Multiplication Law",
    title: "Section 1.4: Multiplying Polynomials & The FOIL Strategy",
    subtitle: "Unit 1 • Lecture 08 • Section 1.4 (Workbook p. 14)",
    detail: "Lecture 08: FOIL Method & Special Products",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### The FOIL Method for Multiplying Two Binomials\n$$(a + b)(c + d) = \\underbrace{ac}_{\\text{First}} + \\underbrace{ad}_{\\text{Outer}} + \\underbrace{bc}_{\\text{Inner}} + \\underbrace{bd}_{\\text{Last}}$$\n- **Every term in the first polynomial** must multiply **every term in the second polynomial**.\n- Combine like terms (typically the Outer and Inner products).",
    solution: "$$\\begin{aligned}\n\\text{Example: } & (x + 3)(x + 5) \\\\\n&= x \\cdot x + x \\cdot 5 + 3 \\cdot x + 3 \\cdot 5 \\\\\n&= x^2 + 5x + 3x + 15 = \\mathbf{x^2 + 8x + 15}\n\\end{aligned}$$",
    pitfall: "**Sora's Warning:** FOIL is just a memory aid for the distributive property. When multiplying a binomial by a trinomial, FOIL expands to 6 multiplications!",
    script: "[Prof. Park] Welcome to Lecture 08! Today we are on pages 14 and 15 of the workbook: Multiplying Polynomials.\n\n[TA Sora] Everyone loves FOIL: First, Outer, Inner, Last! Let's conquer Example 1 on Slide 2!"
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1A & 1B: Standard FOIL Binomial Multiplication",
    subtitle: "Unit 1 • Lecture 08 • Section 1.4 Example 1A & 1B (Workbook p. 14)",
    detail: "Lecture 08: FOIL Method & Special Products",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Use the distributive property to multiply and fully simplify (Workbook p. 14)\n$$\\text{A. } (2x + 4)(3x + 5)$$\n$$\\text{B. } (x - 4)(5x - 1)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & (2x)(3x) + (2x)(5) + (4)(3x) + (4)(5) \\\\\n&= 6x^2 + 10x + 12x + 20 \\\\\n&= \\mathbf{6x^2 + 22x + 20} \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & (x)(5x) + (x)(-1) + (-4)(5x) + (-4)(-1) \\\\\n&= 5x^2 - x - 20x + 4 \\\\\n&= \\mathbf{5x^2 - 21x + 4}\n\\end{aligned}$$",
    pitfall: "**Double Negative Trap:** In 1B, Last times Last is $(-4)(-1) = +4$. Watch your signs!",
    script: "[Prof. Park] In 1A: First is $6x^2$, Outer is $10x$, Inner is $12x$, Last is $20$. $10x + 12x = 22x$, so $6x^2 + 22x + 20$.\n\n[TA Sora] In 1B, watch the negative signs: $-x - 20x = -21x$, and $(-4)(-1) = +4$. Result: $5x^2 - 21x + 4$!"
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1C & 1D: Binomial Products with Leading Constants",
    subtitle: "Unit 1 • Lecture 08 • Section 1.4 Example 1C & 1D (Workbook p. 14)",
    detail: "Lecture 08: FOIL Method & Special Products",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Use the distributive property to multiply and fully simplify (Workbook p. 14)\n$$\\text{C. } 2(b - 3)(b + 4)$$\n$$\\text{D. } 4(w + 2)(w - 2)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & \\text{Step 1: FOIL the binomials first:} \\\\\n& (b - 3)(b + 4) = b^2 + 4b - 3b - 12 = b^2 + b - 12 \\\\\n& \\text{Step 2: Distribute the outer 2:} \\\\\n& 2(b^2 + b - 12) = \\mathbf{2b^2 + 2b - 24} \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & \\text{Step 1: Difference of squares for } (w + 2)(w - 2): \\\\\n& w^2 - 2w + 2w - 4 = w^2 - 4 \\\\\n& \\text{Step 2: Distribute the outer 4:} \\\\\n& 4(w^2 - 4) = \\mathbf{4w^2 - 16}\n\\end{aligned}$$",
    pitfall: "**Sora's Strategy:** FOIL the binomials inside parentheses first, and distribute the constant factor last! Never distribute the constant into BOTH parentheses!",
    script: "[Prof. Park] In 1C and 1D, we have a constant in front: $2(b - 3)(b + 4)$.\n\n[TA Sora] Pro-tip: Multiply the two binomials first! $(b-3)(b+4) = b^2 + b - 12$. Then double everything: $2b^2 + 2b - 24$.\n\n[Prof. Park] And in 1D, $(w+2)(w-2) = w^2 - 4$. Multiply by 4 gives $4w^2 - 16$."
  },
  {
    num: 4,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1E & 1F: Squaring a Binomial Trap",
    subtitle: "Unit 1 • Lecture 08 • Section 1.4 Example 1E & 1F (Workbook p. 14)",
    detail: "Lecture 08: FOIL Method & Special Products",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Fully simplify each expression (Workbook p. 14)\n$$\\text{E. } (2y - 7)^2$$\n$$\\text{F. } 2(y - 7)^2$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ E:}\\quad & \\text{Write out as repeated multiplication:} \\\\\n& (2y - 7)(2y - 7) = (2y)(2y) + (2y)(-7) + (-7)(2y) + (-7)(-7) \\\\\n&= 4y^2 - 14y - 14y + 49 = \\mathbf{4y^2 - 28y + 49} \\\\[1em]\n\\mathbf{Part\\ F:}\\quad & \\text{Expand } (y - 7)^2 \\text{ first:} \\\\\n& (y - 7)(y - 7) = y^2 - 14y + 49 \\\\\n& \\text{Now multiply by 2:} \\\\\n& 2(y^2 - 14y + 49) = \\mathbf{2y^2 - 28y + 98}\n\\end{aligned}$$",
    pitfall: "**THE DEADLIEST ALGEBRA SIN:** $(2y - 7)^2 \\neq 4y^2 + 49$! Exponents DO NOT distribute over subtraction! You MUST write it twice and FOIL to get the middle term $-28y$!",
    script: "[Prof. Park] Slide 4 contains what I call the ultimate algebra trap: $(2y - 7)^2$.\n\n[TA Sora] Please, everyone: NEVER just square the $2y$ and square the $7$! That kills the middle term! Write it as $(2y - 7)(2y - 7)$ and FOIL to get $4y^2 - 28y + 49$.\n\n[Prof. Park] In 1F, expand $(y - 7)^2 = y^2 - 14y + 49$ first, then multiply by 2 to get $2y^2 - 28y + 98$."
  },
  {
    num: 5,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1H & 1I: Multiplying Binomials by Trinomials",
    subtitle: "Unit 1 • Lecture 08 • Section 1.4 Example 1H & 1I (Workbook p. 14)",
    detail: "Lecture 08: FOIL Method & Special Products",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Multiply and combine like terms (Workbook p. 14)\n$$\\text{H. } (w + 2)(w^2 - 2w + 9)$$\n$$\\text{I. } (2x - 1)(x^2 + 3x - 10)$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ H:}\\quad & w(w^2 - 2w + 9) + 2(w^2 - 2w + 9) \\\\\n&= (w^3 - 2w^2 + 9w) + (2w^2 - 4w + 18) \\\\\n&= w^3 + (-2w^2 + 2w^2) + (9w - 4w) + 18 \\\\\n&= \\mathbf{w^3 + 5w + 18} \\\\[1em]\n\\mathbf{Part\\ I:}\\quad & 2x(x^2 + 3x - 10) - 1(x^2 + 3x - 10) \\\\\n&= (2x^3 + 6x^2 - 20x) + (-x^2 - 3x + 10) \\\\\n&= 2x^3 + (6x^2 - x^2) + (-20x - 3x) + 10 \\\\\n&= \\mathbf{2x^3 + 5x^2 - 23x + 10}\n\\end{aligned}$$",
    pitfall: "**Notice Quadratic Cancellation:** In Part H, $-2w^2 + 2w^2 = 0$. The $w^2$ terms completely vanish!",
    script: "[Prof. Park] In 1H and 1I, distribute each term of the binomial across all three terms of the trinomial.\n\n[TA Sora] In 1H, $w(w^2 - 2w + 9) + 2(w^2 - 2w + 9)$. The $w^2$ terms cancel out, leaving $w^3 + 5w + 18$!\n\n[Prof. Park] In 1I, distributing $2x$ and $-1$ yields $2x^3 + 5x^2 - 23x + 10$."
  },
  {
    num: 6,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2 & 3: Perimeter & Area Applications",
    subtitle: "Unit 1 • Lecture 08 • Section 1.4 Example 2 & 3 (Workbook p. 15)",
    detail: "Lecture 08: FOIL Method & Special Products",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Geometry Applications of Polynomials (Workbook p. 15)\nA rectangle has length $L = 3x - 4$ and width $W = 2x + 7$.\n- **Example 2:** Find the perimeter of the rectangle.\n- **Example 3:** Find the area of the rectangle.",
    solution: "$$\\begin{aligned}\n\\mathbf{Example\\ 2\\ (Perimeter):}\\quad P &= 2L + 2W \\\\\n&= 2(3x - 4) + 2(2x + 7) \\\\\n&= 6x - 8 + 4x + 14 = \\mathbf{10x + 6} \\\\[1em]\n\\mathbf{Example\\ 3\\ (Area):}\\quad A &= L \\cdot W \\\\\n&= (3x - 4)(2x + 7) \\\\\n&= (3x)(2x) + (3x)(7) + (-4)(2x) + (-4)(7) \\\\\n&= 6x^2 + 21x - 8x - 28 = \\mathbf{6x^2 + 13x - 28}\n\\end{aligned}$$",
    pitfall: "**Don't Mix Up Perimeter & Area:** Perimeter adds all 4 sides ($2L + 2W$, linear units). Area multiplies length by width ($L \\cdot W$, square units)!",
    script: "[Prof. Park] Now turn to page 15, Examples 2 and 3. We are given a rectangle with length $3x - 4$ and width $2x + 7$.\n\n[TA Sora] Perimeter is the distance around: $2(3x - 4) + 2(2x + 7) = 6x - 8 + 4x + 14 = 10x + 6$.\n\n[Prof. Park] And Area is length times width: FOIL $(3x - 4)(2x + 7) = 6x^2 + 13x - 28$."
  },
  {
    num: 7,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 4: Modified Geometric Area Problem",
    subtitle: "Unit 1 • Lecture 08 • Section 1.4 Example 4 (Workbook p. 15)",
    detail: "Lecture 08: FOIL Method & Special Products",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Modified Rectangle Dimensions (Workbook p. 15)\nA given rectangle has length $2x + 3$ and width $x - 6$.\nIf the **length is decreased by 7** and the **width is increased by 12**, find the **area of the new rectangle** in terms of $x$.",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Find new dimensions:} \\\\\n& L_{\\text{new}} = (2x + 3) - 7 = \\mathbf{2x - 4} \\\\\n& W_{\\text{new}} = (x - 6) + 12 = \\mathbf{x + 6} \\\\[0.8em]\n\\text{Step 2: } & \\text{Calculate new area: } A_{\\text{new}} = L_{\\text{new}} \\cdot W_{\\text{new}} \\\\\n& A_{\\text{new}} = (2x - 4)(x + 6) \\\\\n&= 2x(x) + 2x(6) - 4(x) - 4(6) \\\\\n&= 2x^2 + 12x - 4x - 24 = \\mathbf{2x^2 + 8x - 24}\n\\end{aligned}$$",
    pitfall: "**Sora's Check:** Update BOTH dimensions before multiplying! $(2x - 4)(x + 6)$, then FOIL to get $2x^2 + 8x - 24$!",
    script: "[Prof. Park] Example 4 tests both translation and polynomial multiplication. Length $2x+3$ decreased by 7 becomes $2x-4$. Width $x-6$ increased by 12 becomes $x+6$.\n\n[TA Sora] Then multiply the new dimensions: $(2x - 4)(x + 6) = 2x^2 + 8x - 24$ square units!\n\n[Prof. Park] Outstanding work! That completes all problems in Section 1.4."
  }
];

const L09 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Core Rational Principle",
    title: "Section 1.5: Adding & Subtracting Rational Expressions (Part 1)",
    subtitle: "Unit 1 • Lecture 09 • Section 1.5 (Workbook p. 16)",
    detail: "Lecture 09: Adding & Subtracting Rational Expressions (Mononomial Denominators)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Rational Expressions Addition & Subtraction Principle\n$$\\frac{A}{C} + \\frac{B}{C} = \\frac{A + B}{C} \\quad \\text{and} \\quad \\frac{A}{C} - \\frac{B}{C} = \\frac{A - B}{C}$$\n- Fractions can **ONLY be added or subtracted if they share a Common Denominator (LCD)**.\n- If denominators differ, find the Least Common Multiple (LCM) of numbers and highest power of variables.",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Find LCD of all denominators.} \\\\\n\\text{Step 2: } & \\text{Multiply numerator and denominator of each fraction by missing factor.} \\\\\n\\text{Step 3: } & \\text{Combine numerators over the single common denominator.} \\\\\n\\text{Step 4: } & \\text{Simplify if possible.}\n\\end{aligned}$$",
    pitfall: "**Sora's Warning:** NEVER add denominators! $\\frac{1}{y} + \\frac{1}{y} = \\frac{2}{y}$, NOT $\\frac{2}{2y}$!",
    script: "[Prof. Park] Welcome to Lecture 09! Today we open to Section 1.5 on page 16 of the workbook: Adding and Subtracting Rational Expressions.\n\n[TA Sora] Just like in 4th grade arithmetic, you cannot add fractions until they have the same denominator! Let's examine Example 1 on Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1A & 1B: Basic Numerical & Algebraic Fractions",
    subtitle: "Unit 1 • Lecture 09 • Section 1.5 Example 1A & 1B (Workbook p. 16)",
    detail: "Lecture 09: Adding & Subtracting Rational Expressions (Mononomial Denominators)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Find the sum or difference (Workbook p. 16)\n$$\\text{A. } \\frac{1}{6} + \\frac{3}{4}$$\n$$\\text{B. } \\frac{7}{y} - \\frac{x}{y}$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & \\text{Denominators are } 6 \\text{ and } 4. \\quad \\text{LCD} = 12. \\\\\n&= \\frac{1 \\cdot 2}{6 \\cdot 2} + \\frac{3 \\cdot 3}{4 \\cdot 3} = \\frac{2}{12} + \\frac{9}{12} = \\mathbf{\\frac{11}{12}} \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & \\text{Denominators are already identical: } y. \\\\\n&= \\frac{7 - x}{y} = \\mathbf{\\frac{7 - x}{y}}\n\\end{aligned}$$",
    pitfall: "**Sora's Note:** In Part B, $7 - x$ cannot be simplified further. Do not cancel the $y$!",
    script: "[Prof. Park] In 1A, the LCD between 6 and 4 is 12. $\\frac{2}{12} + \\frac{9}{12} = \\frac{11}{12}$.\n\n[TA Sora] And in 1B, the denominators are already the same ($y$), so we simply combine numerators: $\\frac{7 - x}{y}$!"
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2A & 2B: Monomial Common Denominators",
    subtitle: "Unit 1 • Lecture 09 • Section 1.5 Example 2A & 2B (Workbook p. 16)",
    detail: "Lecture 09: Adding & Subtracting Rational Expressions (Mononomial Denominators)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Add or subtract by obtaining a common denominator (Workbook p. 16)\n$$\\text{A. } \\frac{5}{w} - \\frac{7}{2w}$$\n$$\\text{B. } \\frac{1}{6x} + \\frac{2}{9x}$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & \\text{Denominators: } w, 2w \\implies \\text{LCD} = 2w. \\\\\n&= \\frac{5 \\cdot 2}{w \\cdot 2} - \\frac{7}{2w} = \\frac{10}{2w} - \\frac{7}{2w} = \\mathbf{\\frac{3}{2w}} \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & \\text{Denominators: } 6x, 9x. \\quad \\text{LCM}(6, 9) = 18 \\implies \\text{LCD} = 18x. \\\\\n&= \\frac{1 \\cdot 3}{6x \\cdot 3} + \\frac{2 \\cdot 2}{9x \\cdot 2} = \\frac{3}{18x} + \\frac{4}{18x} = \\mathbf{\\frac{7}{18x}}\n\\end{aligned}$$",
    pitfall: "**LCD Check:** For $6x$ and $9x$, don't use $54x$! The least common multiple of 6 and 9 is 18, so $\\text{LCD} = 18x$.",
    script: "[Prof. Park] In 2A, the LCD of $w$ and $2w$ is $2w$. Multiply the first fraction by $\\frac{2}{2}$ to get $\\frac{10 - 7}{2w} = \\frac{3}{2w}$.\n\n[TA Sora] In 2B, the smallest number both 6 and 9 divide into is 18. So the LCD is $18x$. Result: $\\frac{3 + 4}{18x} = \\frac{7}{18x}$!"
  },
  {
    num: 4,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2C & 2D: Two-Variable Denominators",
    subtitle: "Unit 1 • Lecture 09 • Section 1.5 Example 2C & 2D (Workbook p. 16)",
    detail: "Lecture 09: Adding & Subtracting Rational Expressions (Mononomial Denominators)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Add or subtract by obtaining a common denominator (Workbook p. 16)\n$$\\text{C. } \\frac{3}{y} + \\frac{5}{x}$$\n$$\\text{D. } \\frac{11y}{2x} - \\frac{x}{5y}$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & \\text{Denominators: } y, x \\implies \\text{LCD} = xy. \\\\\n&= \\frac{3 \\cdot x}{y \\cdot x} + \\frac{5 \\cdot y}{x \\cdot y} = \\mathbf{\\frac{3x + 5y}{xy}} \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & \\text{Denominators: } 2x, 5y \\implies \\text{LCD} = 10xy. \\\\\n&= \\frac{11y \\cdot 5y}{2x \\cdot 5y} - \\frac{x \\cdot 2x}{5y \\cdot 2x} = \\frac{55y^2}{10xy} - \\frac{2x^2}{10xy} = \\mathbf{\\frac{55y^2 - 2x^2}{10xy}}\n\\end{aligned}$$",
    pitfall: "**Variable Multiplication Trap:** In 2D, $11y \\cdot 5y = 55y^2$ and $x \\cdot 2x = 2x^2$. Don't forget the squared exponents on the variables!",
    script: "[Prof. Park] In 2C, the denominators share no common factors, so the LCD is simply their product: $xy$. Result: $\\frac{3x + 5y}{xy}$.\n\n[TA Sora] And in 2D, the LCD is $10xy$. When we multiply $11y$ by $5y$, we get $55y^2$. Result: $\\frac{55y^2 - 2x^2}{10xy}$."
  },
  {
    num: 5,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2E & 2F: Mixed Constant & Variable Denominators",
    subtitle: "Unit 1 • Lecture 09 • Section 1.5 Example 2E & 2F (Workbook p. 16)",
    detail: "Lecture 09: Adding & Subtracting Rational Expressions (Mononomial Denominators)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Add or subtract by obtaining a common denominator (Workbook p. 16)\n$$\\text{E. } \\frac{2}{7r} + \\frac{3}{7}$$\n$$\\text{F. } \\frac{4}{5} - \\frac{9}{5w}$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ E:}\\quad & \\text{Denominators: } 7r, 7 \\implies \\text{LCD} = 7r. \\\\\n&= \\frac{2}{7r} + \\frac{3 \\cdot r}{7 \\cdot r} = \\frac{2}{7r} + \\frac{3r}{7r} = \\mathbf{\\frac{2 + 3r}{7r}} \\\\[1em]\n\\mathbf{Part\\ F:}\\quad & \\text{Denominators: } 5, 5w \\implies \\text{LCD} = 5w. \\\\\n&= \\frac{4 \\cdot w}{5 \\cdot w} - \\frac{9}{5w} = \\frac{4w}{5w} - \\frac{9}{5w} = \\mathbf{\\frac{4w - 9}{5w}}\n\\end{aligned}$$",
    pitfall: "**Never Cancel Across Addition/Subtraction:** In Part E, you CANNOT cancel the $r$ in $3r$ with the $r$ in $7r$! Terms connected by $+$ or $-$ cannot be cancelled!",
    script: "[Prof. Park] Look at Example 2E: $\\frac{2}{7r} + \\frac{3}{7}$. The LCD is $7r$. Multiplying the second term by $\\frac{r}{r}$ gives $\\frac{2 + 3r}{7r}$.\n\n[TA Sora] And Sora's warning: you CANNOT cancel the $r$'s here! The 2 has no $r$, and addition blocks cancellation!\n\n[Prof. Park] In 2F, the LCD is $5w$, giving $\\frac{4w - 9}{5w}$."
  }
];

const L10 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Advanced Rational Principle",
    title: "Section 1.5: Advanced Rational Addition & Subtraction (Part 2)",
    subtitle: "Unit 1 • Lecture 10 • Section 1.5 (Workbook p. 17)",
    detail: "Lecture 10: Rational Expressions (Higher Powers & Binomial Numerators)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Advanced Rational Denominators (Workbook p. 17)\nWhen denominators contain higher variable powers or multiple terms:\n1. **Take the highest power of each variable factor** (e.g. $x$ and $x^4 \\implies \\text{LCD has } x^4$).\n2. **Binomial Numerator Trap:** When subtracting fractions with binomial numerators:\n$$\\frac{A}{C} - \\frac{B + D}{C} = \\frac{A - (B + D)}{C} = \\frac{A - B - D}{C}$$\n**The negative sign MUST distribute to every term in the numerator!**",
    solution: "$$\\begin{aligned}\n\\text{Crucial Example: } & \\frac{5}{x} - \\frac{x - 3}{x} = \\frac{5 - (x - 3)}{x} = \\frac{5 - x + 3}{x} = \\mathbf{\\frac{8 - x}{x}}\n\\end{aligned}$$",
    pitfall: "**Fatal Trap:** Writing $\\frac{5 - x - 3}{x}$. You must distribute the subtraction to get $+3$!",
    script: "[Prof. Park] Welcome to Lecture 10! Today we tackle page 17 of your workbook: Example 3. These are the most rigorous rational expression problems in Unit 1.\n\n[TA Sora] Watch out for two things: highest variable powers in LCD, and distributing the subtraction over binomial numerators! Let's go to Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3A: Quadratic Monomial Denominator",
    subtitle: "Unit 1 • Lecture 10 • Section 1.5 Example 3A (Workbook p. 17)",
    detail: "Lecture 10: Rational Expressions (Higher Powers & Binomial Numerators)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Add or subtract the expression and simplify (Workbook p. 17)\n$$\\frac{3}{7x^2} + \\frac{5}{14x}$$",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Find LCD:} \\\\\n& \\text{Coefficients: } \\text{LCM}(7, 14) = 14 \\\\\n& \\text{Variables: Highest power between } x^2 \\text{ and } x \\text{ is } x^2 \\implies \\mathbf{\\text{LCD} = 14x^2} \\\\[0.8em]\n\\text{Step 2: } & \\text{Build common denominator:} \\\\\n& \\frac{3 \\cdot 2}{7x^2 \\cdot 2} + \\frac{5 \\cdot x}{14x \\cdot x} = \\frac{6}{14x^2} + \\frac{5x}{14x^2} \\\\[0.8em]\n\\text{Step 3: } & \\text{Combine numerators:} \\\\\n&= \\mathbf{\\frac{6 + 5x}{14x^2}}\n\\end{aligned}$$",
    pitfall: "**Power Choice:** In the LCD, choose $x^2$, NOT $x^3$ or $x$! The LCD takes the HIGHEST power present: $14x^2$.",
    script: "[Prof. Park] In 3A, we have $7x^2$ and $14x$. Sora, what is the LCD?\n\n[TA Sora] For the numbers 7 and 14, it's 14. For $x^2$ and $x$, we take the higher power, which is $x^2$! So LCD is $14x^2$.\n\n[Prof. Park] Multiply the first fraction by $\\frac{2}{2}$ and the second by $\\frac{x}{x}$, giving $\\frac{6 + 5x}{14x^2}$."
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3B: Three-Term Rational Expression with 4th Power",
    subtitle: "Unit 1 • Lecture 10 • Section 1.5 Example 3B (Workbook p. 17)",
    detail: "Lecture 10: Rational Expressions (Higher Powers & Binomial Numerators)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Add or subtract the expression and simplify (Workbook p. 17)\n$$\\frac{2}{x} - \\frac{9}{10x^4} + \\frac{3}{x}$$",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Notice that } \\frac{2}{x} \\text{ and } \\frac{3}{x} \\text{ already have the same denominator!} \\\\\n& \\left(\\frac{2}{x} + \\frac{3}{x}\\right) - \\frac{9}{10x^4} = \\frac{5}{x} - \\frac{9}{10x^4} \\\\[0.8em]\n\\text{Step 2: } & \\text{Find LCD of } x \\text{ and } 10x^4: \\quad \\mathbf{\\text{LCD} = 10x^4} \\\\[0.8em]\n\\text{Step 3: } & \\text{Convert to common denominator:} \\\\\n& \\frac{5 \\cdot 10x^3}{x \\cdot 10x^3} - \\frac{9}{10x^4} = \\frac{50x^3}{10x^4} - \\frac{9}{10x^4} = \\mathbf{\\frac{50x^3 - 9}{10x^4}}\n\\end{aligned}$$",
    pitfall: "**Sora's Shortcut:** Always combine like fractions first! Adding $\\frac{2}{x} + \\frac{3}{x} = \\frac{5}{x}$ immediately turns a 3-fraction problem into a simple 2-fraction problem!",
    script: "[Prof. Park] Look at 3B: $\\frac{2}{x} - \\frac{9}{10x^4} + \\frac{3}{x}$. Notice anything special, Sora?\n\n[TA Sora] Yes! $\\frac{2}{x}$ and $\\frac{3}{x}$ have the exact same denominator! Combine them first to get $\\frac{5}{x}$.\n\n[Prof. Park] Brilliant! Now we just have $\\frac{5}{x} - \\frac{9}{10x^4}$. The LCD is $10x^4$. Multiplying by $10x^3$ gives $\\frac{50x^3 - 9}{10x^4}$."
  },
  {
    num: 4,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3C & 3D: Multi-Term Common Denominators",
    subtitle: "Unit 1 • Lecture 10 • Section 1.5 Example 3C & 3D (Workbook p. 17)",
    detail: "Lecture 10: Rational Expressions (Higher Powers & Binomial Numerators)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Add or subtract the expressions (Workbook p. 17)\n$$\\text{C. } \\frac{2}{3b} + \\frac{1}{4} + \\frac{1}{6b}$$\n$$\\text{D. } \\frac{2}{5r} - \\frac{3}{4r} - \\frac{7}{10}$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & \\text{Combine } b\\text{-terms first: } \\frac{2}{3b} + \\frac{1}{6b} = \\frac{4}{6b} + \\frac{1}{6b} = \\frac{5}{6b} \\\\\n& \\text{Now add } \\frac{5}{6b} + \\frac{1}{4}. \\quad \\text{LCD of } 6b \\text{ and } 4 \\text{ is } 12b. \\\\\n&= \\frac{5 \\cdot 2}{6b \\cdot 2} + \\frac{1 \\cdot 3b}{4 \\cdot 3b} = \\mathbf{\\frac{10 + 3b}{12b}} \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & \\text{Combine } r\\text{-terms first: } \\frac{2}{5r} - \\frac{3}{4r} = \\frac{8}{20r} - \\frac{15}{20r} = \\frac{-7}{20r} \\\\\n& \\text{Now subtract } \\frac{-7}{20r} - \\frac{7}{10}. \\quad \\text{LCD of } 20r \\text{ and } 10 \\text{ is } 20r. \\\\\n&= \\frac{-7}{20r} - \\frac{7 \\cdot 2r}{10 \\cdot 2r} = \\mathbf{\\frac{-7 - 14r}{20r}}\n\\end{aligned}$$",
    pitfall: "**Sign Caution:** In Part D, $8 - 15 = -7$. Keep that negative sign in front of the 7!",
    script: "[Prof. Park] In 3C, we combine $\\frac{2}{3b} + \\frac{1}{6b} = \\frac{5}{6b}$, then add $\\frac{1}{4}$ using LCD $12b$ to get $\\frac{10 + 3b}{12b}$.\n\n[TA Sora] And in 3D, combining the $r$-terms gives $\\frac{-7}{20r}$, and subtracting $\\frac{14r}{20r}$ gives $\\frac{-7 - 14r}{20r}$."
  },
  {
    num: 5,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3E: Subtracting Fractions with Binomial Numerators",
    subtitle: "Unit 1 • Lecture 10 • Section 1.5 Example 3E (Workbook p. 17)",
    detail: "Lecture 10: Rational Expressions (Higher Powers & Binomial Numerators)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Subtract and simplify fully (Workbook p. 17)\n$$\\frac{2x - 5}{3x} - \\frac{5x + 9}{6x}$$",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Find LCD of } 3x \\text{ and } 6x: \\quad \\mathbf{\\text{LCD} = 6x} \\\\[0.8em]\n\\text{Step 2: } & \\text{Scale the first fraction by } \\frac{2}{2}: \\\\\n& \\frac{2(2x - 5)}{6x} - \\frac{5x + 9}{6x} = \\frac{4x - 10}{6x} - \\frac{5x + 9}{6x} \\\\[0.8em]\n\\text{Step 3: } & \\text{Combine with parentheses to distribute the minus sign!} \\\\\n&= \\frac{(4x - 10) - (5x + 9)}{6x} \\\\\n&= \\frac{4x - 10 - 5x - 9}{6x} = \\mathbf{\\frac{-x - 19}{6x}}\n\\end{aligned}$$",
    pitfall: "**EXAM DISASTER ALERT:** Writing $4x - 10 - 5x + 9$. The minus MUST hit both $5x$ and $+9$, turning $+9$ into $-9$! So $-10 - 9 = -19$!",
    script: "[Prof. Park] Example 3E is one of the most critical exam questions in all of Unit 1. Look closely at that minus sign between the fractions.\n\n[TA Sora] You MUST put parentheses around $(5x + 9)$ when combining! That minus sign distributes: $-(5x + 9) = -5x - 9$.\n\n[Prof. Park] Exactly. Then $4x - 5x = -x$, and $-10 - 9 = -19$, giving $\\frac{-x - 19}{6x}$."
  },
  {
    num: 6,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3F: Second Binomial Subtraction Master Problem",
    subtitle: "Unit 1 • Lecture 10 • Section 1.5 Example 3F (Workbook p. 17)",
    detail: "Lecture 10: Rational Expressions (Higher Powers & Binomial Numerators)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Subtract and simplify fully (Workbook p. 17)\n$$\\frac{3y + 7}{8y} - \\frac{9y - 11}{4y}$$",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Find LCD of } 8y \\text{ and } 4y: \\quad \\mathbf{\\text{LCD} = 8y} \\\\[0.8em]\n\\text{Step 2: } & \\text{Scale the second fraction by } \\frac{2}{2}: \\\\\n& \\frac{3y + 7}{8y} - \\frac{2(9y - 11)}{8y} = \\frac{3y + 7}{8y} - \\frac{18y - 22}{8y} \\\\[0.8em]\n\\text{Step 3: } & \\text{Combine and distribute the subtraction:} \\\\\n&= \\frac{(3y + 7) - (18y - 22)}{8y} \\\\\n&= \\frac{3y + 7 - 18y + 22}{8y} \\\\\n&= \\mathbf{\\frac{-15y + 29}{8y}}\n\\end{aligned}$$",
    pitfall: "**Double Negative Alert:** $-(-22) = +22$! So $7 + 22 = +29$! Do not write $7 - 22 = -15$!",
    script: "[Prof. Park] In 3F, the second fraction is multiplied by $\\frac{2}{2}$, giving $\\frac{18y - 22}{8y}$.\n\n[TA Sora] And when we subtract, $-(-22)$ becomes $+22$! So $7 + 22 = 29$. The final simplified fraction is $\\frac{-15y + 29}{8y}$.\n\n[Prof. Park] Phenomenal! That completes every single problem from Section 1.5 in your workbook."
  }
];

const L11 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Core Principle of Equality",
    title: "Section 1.6: Solving Linear Equations — Properties of Equality",
    subtitle: "Unit 1 • Lecture 11 • Section 1.6 (Workbook p. 18)",
    detail: "Lecture 11: Properties of Equality & Multi-Term Equations",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### The Golden Rule of Equation Solving\n$$\\text{Whatever you do to one side of the equation, you MUST do to the other side!}$$\n- **Addition/Subtraction Property:** If $a = b$, then $a \\pm c = b \\pm c$.\n- **Multiplication/Division Property:** If $a = b$ and $c \\neq 0$, then $ac = bc$ and $\\frac{a}{c} = \\frac{b}{c}$.\n- **Target Goal:** Isolate the variable term on one side and constants on the other.",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Simplify each side separately (distribute, combine like terms).} \\\\\n\\text{Step 2: } & \\text{Use addition/subtraction to move variable terms to one side, numbers to other.} \\\\\n\\text{Step 3: } & \\text{Multiply or divide by the variable's coefficient to get } x = \\text{value}.\n\\end{aligned}$$",
    pitfall: "**Sora's Reminder:** An equation is a balance scale. Never alter one pan without altering the other!",
    script: "[Prof. Park] Welcome to Lecture 11! Today we open to Section 1.6 on page 18 of the workbook: Solving Linear Equations.\n\n[TA Sora] The equal sign is a sacred balance scale. If you subtract 8 from the left side, you must subtract 8 from the right side! Let's solve Example 1 on Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1A: Two-Step Linear Equation",
    subtitle: "Unit 1 • Lecture 11 • Section 1.6 Example 1A (Workbook p. 18)",
    detail: "Lecture 11: Properties of Equality & Multi-Term Equations",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve the linear equation for the given variable (Workbook p. 18)\n$$3x - 8 = -12$$",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Add } 8 \\text{ to both sides to isolate the variable term:} \\\\\n& 3x - 8 + 8 = -12 + 8 \\\\\n& 3x = -4 \\\\[0.8em]\n\\text{Step 2: } & \\text{Divide both sides by the coefficient } 3: \\\\\n& \\frac{3x}{3} = \\frac{-4}{3} \\\\\n& \\mathbf{x = -\\frac{4}{3}}\n\\end{aligned}$$",
    pitfall: "**Fraction Answers are Valid:** Many students panic when they get a fraction like $-\\frac{4}{3}$ and think they made a mistake. In college algebra, fractions are authentic real numbers! Do not convert to rounded decimals!",
    script: "[Prof. Park] In 1A: $3x - 8 = -12$. First add 8 to both sides: $-12 + 8 = -4$.\n\n[TA Sora] Then divide by 3: $x = -\\frac{4}{3}$. Never fear improper fractions—leave it in simplest fraction form!"
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1B: Negative Coefficient Trap",
    subtitle: "Unit 1 • Lecture 11 • Section 1.6 Example 1B (Workbook p. 18)",
    detail: "Lecture 11: Properties of Equality & Multi-Term Equations",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve the linear equation for the given variable (Workbook p. 18)\n$$6 - 4w = 15$$",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Subtract } 6 \\text{ from both sides:} \\\\\n& -4w = 15 - 6 \\\\\n& -4w = 9 \\\\[0.8em]\n\\text{Step 2: } & \\text{Divide both sides by } -4 \\text{ (including the negative sign!):} \\\\\n& \\frac{-4w}{-4} = \\frac{9}{-4} \\\\\n& \\mathbf{w = -\\frac{9}{4}}\n\\end{aligned}$$",
    pitfall: "**The Dropped Negative Sign:** Students often subtract 6 and write $4w = 9$, dropping the minus in front of $4w$. The term is $-4w$, so you MUST divide by $-4$!",
    script: "[Prof. Park] In 1B: $6 - 4w = 15$. Sora, what is the biggest mistake students make here?\n\n[TA Sora] Dropping the negative sign! After subtracting 6, they write $4w = 9$ instead of $-4w = 9$!\n\n[Prof. Park] Absolutely. That minus sign belongs to the $4w$. Dividing by $-4$ gives $w = -\\frac{9}{4}$."
  },
  {
    num: 4,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1C & 1D: Combining Like Terms First",
    subtitle: "Unit 1 • Lecture 11 • Section 1.6 Example 1C & 1D (Workbook p. 18)",
    detail: "Lecture 11: Properties of Equality & Multi-Term Equations",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve each equation (Workbook p. 18)\n$$\\text{C. } y + 4 + 5y - 9 = 87$$\n$$\\text{D. } 6r - 3r + 94 + 2r = 18$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & \\text{Combine like terms on left side first:} \\\\\n& (y + 5y) + (4 - 9) = 87 \\implies 6y - 5 = 87 \\\\\n& 6y = 87 + 5 = 92 \\\\\n& y = \\frac{92}{6} = \\mathbf{\\frac{46}{3}} \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & \\text{Combine like terms on left side:} \\\\\n& (6r - 3r + 2r) + 94 = 18 \\implies 5r + 94 = 18 \\\\\n& 5r = 18 - 94 = -76 \\\\\n& \\mathbf{r = -\\frac{76}{5}}\n\\end{aligned}$$",
    pitfall: "**Reduce Fractions Fully:** In Part C, $\\frac{92}{6}$ can both be divided by 2 to give $\\frac{46}{3}$. Always simplify your final fraction!",
    script: "[Prof. Park] In 1C, combine terms on the left first: $y + 5y = 6y$ and $4 - 9 = -5$. So $6y - 5 = 87 \\implies 6y = 92 \\implies y = \\frac{46}{3}$.\n\n[TA Sora] In 1D, $(6r - 3r + 2r) = 5r$. Then $5r + 94 = 18 \\implies 5r = -76 \\implies r = -\\frac{76}{5}$!"
  },
  {
    num: 5,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2A & 2B: Equations with Distributive Property",
    subtitle: "Unit 1 • Lecture 11 • Section 1.6 Example 2A & 2B (Workbook p. 18)",
    detail: "Lecture 11: Properties of Equality & Multi-Term Equations",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve each equation. Write answer in simplest fraction form (Workbook p. 18)\n$$\\text{A. } 10(a - 5) + 2 = -3$$\n$$\\text{B. } 6(x - 2) - 8 = 3x - 20$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & 10a - 50 + 2 = -3 \\\\\n& 10a - 48 = -3 \\implies 10a = 45 \\\\\n& a = \\frac{45}{10} = \\mathbf{\\frac{9}{2}} \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & 6x - 12 - 8 = 3x - 20 \\\\\n& 6x - 20 = 3x - 20 \\\\\n& 6x - 3x = -20 + 20 \\\\\n& 3x = 0 \\implies \\mathbf{x = 0}\n\\end{aligned}$$",
    pitfall: "**The Zero Solution Trap in 2B:** $x = 0$ is a VALID solution! Zero is a number! It does NOT mean 'no solution'!",
    script: "[Prof. Park] In 2A, distribute 10: $10a - 50 + 2 = -3 \\implies 10a - 48 = -3 \\implies 10a = 45 \\implies a = \\frac{9}{2}$.\n\n[TA Sora] And in 2B, $3x = 0$ means $x = 0$. Please note: $x = 0$ is a perfectly valid number! Do not write 'no solution'!"
  }
];

const L12 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Classification Theory",
    title: "Section 1.6: Classifying Linear Equations (Part 2)",
    subtitle: "Unit 1 • Lecture 12 • Section 1.6 (Workbook p. 19)",
    detail: "Lecture 12: Special Cases & In-Class Practice",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### The Three Types of Linear Equations (Workbook p. 19)\n- **1. Conditional:** The equation has a **finite number of unique real solutions** (e.g. $x = 5$, $x = 0$). True under certain conditions.\n- **2. Contradiction:** Variables cancel out leaving a **FALSE statement** (e.g. $0 = 7$). **NO SOLUTION ($\\emptyset$)**.\n- **3. Identity:** Variables cancel out leaving a **TRUE statement** (e.g. $5 = 5$, $0 = 0$). **ALL REAL NUMBERS ($\\mathbb{R}$)**.",
    solution: "$$\\begin{aligned}\n\\text{Conditional: } & 2x = 6 \\implies x = 3 \\quad (\\text{One unique solution}) \\\\\n\\text{Contradiction: } & x + 1 = x + 4 \\implies 1 = 4 \\quad (\\text{False! No solution}) \\\\\n\\text{Identity: } & 2(x + 1) = 2x + 2 \\implies 2x + 2 = 2x + 2 \\quad (\\text{True for all } x!)\n\\end{aligned}$$",
    pitfall: "**Sora's Warning:** Don't confuse $x = 0$ (conditional, exactly 1 solution) with $0 = 5$ (contradiction, no solution)!",
    script: "[Prof. Park] Welcome to Lecture 12! Today we finish Section 1.6 on pages 18 and 19 of your workbook.\n\n[TA Sora] Every linear equation in the universe falls into one of three buckets: Conditional (one answer), Contradiction (no solution), or Identity (all real numbers). Let's see Examples 2C and 2D on Slide 2!"
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2C & 2D: Special Case Equations",
    subtitle: "Unit 1 • Lecture 12 • Section 1.6 Example 2C & 2D (Workbook p. 18)",
    detail: "Lecture 12: Special Cases & In-Class Practice",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve each equation and classify (Workbook p. 18)\n$$\\text{C. } 2(7 - x) + 11 = 12 - 2x$$\n$$\\text{D. } -4 - (3 - x) - 2 = 9(x - 1) - 8x$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & 14 - 2x + 11 = 12 - 2x \\\\\n& 25 - 2x = 12 - 2x \\\\\n& 25 - 2x + 2x = 12 - 2x + 2x \\\\\n& \\mathbf{25 = 12} \\quad \\text{\\textbf{FALSE statement!}} \\\\\n& \\implies \\mathbf{\\text{Contradiction (No Solution, } \\emptyset\\text{)}} \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & -4 - 3 + x - 2 = 9x - 9 - 8x \\\\\n& x - 9 = x - 9 \\\\\n& -9 = -9 \\quad \\text{\\textbf{TRUE statement!}} \\\\\n& \\implies \\mathbf{\\text{Identity (All Real Numbers, } \\mathbb{R}\\text{)}}\n\\end{aligned}$$",
    pitfall: "**What Happened to the Variable?** When the variable completely cancels out, look at the remaining numbers: False statement $\\implies$ Contradiction. True statement $\\implies$ Identity!",
    script: "[Prof. Park] In 2C, adding $2x$ to both sides cancels the variables completely, leaving $25 = 12$, which is impossible. That is a Contradiction: No Solution.\n\n[TA Sora] In 2D, simplifying both sides gives $x - 9 = x - 9$, which is always true! That is an Identity: All Real Numbers."
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "In-Class Practice #1 & #2",
    subtitle: "Unit 1 • Lecture 12 • Section 1.6 Extra Practice #1 & #2 (Workbook p. 19)",
    detail: "Lecture 12: Special Cases & In-Class Practice",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve and classify (Workbook p. 19)\n$$\\text{1. } 3x - 2 = -9x + 15$$\n$$\\text{2. } r - 3 - 7 + r = 10 + 2r$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Practice\\ 1:}\\quad & 3x + 9x = 15 + 2 \\\\\n& 12x = 17 \\implies \\mathbf{x = \\frac{17}{12}} \\quad \\mathbf{[Conditional]} \\\\[1em]\n\\mathbf{Practice\\ 2:}\\quad & (r + r) + (-3 - 7) = 10 + 2r \\\\\n& 2r - 10 = 2r + 10 \\\\\n& 2r - 2r = 10 + 10 \\implies \\mathbf{-10 = 10} \\quad \\text{\\textbf{FALSE!}} \\\\\n& \\implies \\mathbf{\\text{Contradiction (No Solution, } \\emptyset\\text{)}}\n\\end{aligned}$$",
    pitfall: "**Sign Watch in #2:** $-10$ does NOT equal $+10$! They are opposites, not equals. Hence it is a contradiction!",
    script: "[Prof. Park] On page 19, In-Class Practice #1: $3x - 2 = -9x + 15$. Add $9x$ and add 2 to get $12x = 17 \\implies x = \\frac{17}{12}$. That is Conditional.\n\n[TA Sora] In Practice #2, $2r - 10 = 2r + 10$. Subtracting $2r$ leaves $-10 = 10$, which is false! Contradiction: No Solution."
  },
  {
    num: 4,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "In-Class Practice #3 & #4",
    subtitle: "Unit 1 • Lecture 12 • Section 1.6 Extra Practice #3 & #4 (Workbook p. 19)",
    detail: "Lecture 12: Special Cases & In-Class Practice",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve and classify (Workbook p. 19)\n$$\\text{3. } 3(w - 4) = 3(w - 9) + 15$$\n$$\\text{4. } -4x + 4(x - 4) = -11$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Practice\\ 3:}\\quad & 3w - 12 = 3w - 27 + 15 \\\\\n& 3w - 12 = 3w - 12 \\\\\n& \\mathbf{-12 = -12} \\quad \\text{\\textbf{TRUE statement!}} \\\\\n& \\implies \\mathbf{\\text{Identity (All Real Numbers, } \\mathbb{R}\\text{)}} \\\\[1em]\n\\mathbf{Practice\\ 4:}\\quad & -4x + 4x - 16 = -11 \\\\\n& \\mathbf{-16 = -11} \\quad \\text{\\textbf{FALSE statement!}} \\\\\n& \\implies \\mathbf{\\text{Contradiction (No Solution, } \\emptyset\\text{)}}\n\\end{aligned}$$",
    pitfall: "**Distribute fully in #3:** $3(w-9) = 3w - 27$. Then $-27 + 15 = -12$. The left and right sides match identically!",
    script: "[Prof. Park] In Practice #3, distributing 3 gives $3w - 12 = 3w - 12$. That is an Identity: All Real Numbers.\n\n[TA Sora] In Practice #4, $-4x + 4x$ cancels to 0, leaving $-16 = -11$, which is false! Contradiction: No Solution."
  },
  {
    num: 5,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "In-Class Practice #5 & #6",
    subtitle: "Unit 1 • Lecture 12 • Section 1.6 Extra Practice #5 & #6 (Workbook p. 19)",
    detail: "Lecture 12: Special Cases & In-Class Practice",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve and classify (Workbook p. 19)\n$$\\text{5. } -(-y - 28) = 7(y + 4)$$\n$$\\text{6. } -2(r + 3) + 7 = 1 - 2r$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Practice\\ 5:}\\quad & y + 28 = 7y + 28 \\\\\n& 28 - 28 = 7y - y \\\\\n& 0 = 6y \\implies \\mathbf{y = 0} \\quad \\mathbf{[Conditional]} \\\\[1em]\n\\mathbf{Practice\\ 6:}\\quad & -2r - 6 + 7 = 1 - 2r \\\\\n& -2r + 1 = 1 - 2r \\\\\n& \\mathbf{1 = 1} \\quad \\text{\\textbf{TRUE statement!}} \\\\\n& \\implies \\mathbf{\\text{Identity (All Real Numbers, } \\mathbb{R}\\text{)}}\n\\end{aligned}$$",
    pitfall: "**Practice #5 Check:** $y = 0$ is a UNIQUE real number solution, so Practice #5 is CONDITIONAL!",
    script: "[Prof. Park] In Practice #5, distributing the negative gives $y + 28 = 7y + 28 \\implies 6y = 0 \\implies y = 0$. That is Conditional.\n\n[TA Sora] And in Practice #6, $-2r + 1 = 1 - 2r \\implies 1 = 1$. True for every value of $r$! That is an Identity: All Real Numbers."
  }
];

const L13 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Core Methodological Law",
    title: "Section 1.7: Solving Linear Equations with Fractions — Clearing the LCD",
    subtitle: "Unit 1 • Lecture 13 • Section 1.7 (Workbook p. 20)",
    detail: "Lecture 13: Solving Linear Equations with Fractions (The LCD Clearing Method)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### The Golden Clearing Fractions Strategy (Workbook p. 20)\n$$\\text{Reminder: Whatever you do to one side, you MUST do to the other side!}$$\n- **Instead of struggling with fraction arithmetic**, multiply **EVERY SINGLE TERM on both sides by the LCD**!\n- All denominators will cancel out into whole integers in one single step!\n- **Key equivalence:** $\\frac{3}{4}x = \\frac{3x}{4}$.",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Find the LCD of all fractions in the entire equation.} \\\\\n\\text{Step 2: } & \\text{Multiply every term on both sides by this LCD.} \\\\\n\\text{Step 3: } & \\text{Cancel denominators: all fractions vanish!} \\\\\n\\text{Step 4: } & \\text{Solve the resulting integer linear equation.}\n\\end{aligned}$$",
    pitfall: "**Sora's Warning:** You must multiply EVERY term by the LCD, including standalone integers with no denominator!",
    script: "[Prof. Park] Welcome to Lecture 13! Today we cover Section 1.7 on pages 20 through 22 of the workbook: Solving Linear Equations with Fractions.\n\n[TA Sora] Students often hate fractions, but in equations, fractions are optional! We can make them vanish in one step by multiplying by the LCD! Let's see Example 1 and 2 on Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1 & 2: Dividing by Coefficient vs. Clearing LCD",
    subtitle: "Unit 1 • Lecture 13 • Section 1.7 Example 1 & 2 (Workbook p. 20)",
    detail: "Lecture 13: Solving Linear Equations with Fractions (The LCD Clearing Method)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Two Methods for the Same Equation (Workbook p. 20)\n$$\\frac{3}{4}x = 15$$\n- **Example 1:** Solve by dividing both sides by the coefficient (multiplying by reciprocal $\\frac{4}{3}$).\n- **Example 2:** Solve by the method of clearing fractions (multiplying both sides by LCD $= 4$).",
    solution: "$$\\begin{aligned}\n\\mathbf{Method\\ 1\\ (Reciprocal):}\\quad & \\frac{3}{4}x = 15 \\\\\n& x = 15 \\div \\frac{3}{4} = 15 \\cdot \\frac{4}{3} = \\frac{60}{3} = \\mathbf{20} \\\\[1em]\n\\mathbf{Method\\ 2\\ (Clear\\ LCD = 4):}\\quad & 4 \\cdot \\left(\\frac{3}{4}x\\right) = 4 \\cdot (15) \\\\\n& 3x = 60 \\\\\n& x = \\frac{60}{3} = \\mathbf{20}\n\\end{aligned}$$",
    pitfall: "**Both yield 20!** Notice how Method 2 eliminates the fraction immediately, converting it into $3x = 60$.",
    script: "[Prof. Park] In Example 1 and 2, we compare dividing by the fraction versus clearing the LCD. In Method 1, multiplying by $\\frac{4}{3}$ gives $x = 20$.\n\n[TA Sora] In Method 2, multiplying both sides by 4 cancels the denominator directly: $3x = 60 \\implies x = 20$. Method 2 is much easier when there are multiple fractions!"
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3A & 3B: Simple Fraction Equations",
    subtitle: "Unit 1 • Lecture 13 • Section 1.7 Example 3A & 3B (Workbook p. 20)",
    detail: "Lecture 13: Solving Linear Equations with Fractions (The LCD Clearing Method)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Use the method of clearing fractions to solve (Workbook p. 20)\n$$\\text{A. } \\frac{x}{-5} = 10$$\n$$\\text{B. } \\frac{1}{2}y + \\frac{3}{4} = 10$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & \\text{Multiply both sides by } -5: \\\\\n& -5 \\cdot \\left(\\frac{x}{-5}\\right) = -5 \\cdot (10) \\\\\n& \\mathbf{x = -50} \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & \\text{Denominators: } 2, 4 \\implies \\mathbf{\\text{LCD} = 4} \\\\\n& 4 \\cdot \\left(\\frac{1}{2}y\\right) + 4 \\cdot \\left(\\frac{3}{4}\\right) = 4 \\cdot (10) \\\\\n& 2y + 3 = 40 \\\\\n& 2y = 37 \\implies \\mathbf{y = \\frac{37}{2}}\n\\end{aligned}$$",
    pitfall: "**Don't forget the standalone 10!** In 3B, $4 \\cdot 10 = 40$. A common mistake is writing $2y + 3 = 10$!",
    script: "[Prof. Park] In 3A, multiplying both sides by $-5$ gives $x = -50$.\n\n[TA Sora] In 3B, the LCD between 2 and 4 is 4. Multiply EVERY term by 4: $4(\\frac{1}{2}y) + 4(\\frac{3}{4}) = 4(10) \\implies 2y + 3 = 40 \\implies y = \\frac{37}{2}$!"
  },
  {
    num: 4,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3C & 3D: Multi-Denominator Clearing",
    subtitle: "Unit 1 • Lecture 13 • Section 1.7 Example 3C & 3D (Workbook p. 21)",
    detail: "Lecture 13: Solving Linear Equations with Fractions (The LCD Clearing Method)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Use clearing fractions to solve (Workbook p. 21)\n$$\\text{C. } \\frac{1}{2}x - \\frac{2}{7} = \\frac{5}{4} - x$$\n$$\\text{D. } \\frac{3}{5} + \\frac{x}{5} = 18$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & \\text{Denominators: } 2, 7, 4 \\implies \\mathbf{\\text{LCD} = 28} \\\\\n& 28 \\cdot \\left(\\frac{1}{2}x\\right) - 28 \\cdot \\left(\\frac{2}{7}\\right) = 28 \\cdot \\left(\\frac{5}{4}\\right) - 28 \\cdot (x) \\\\\n& 14x - 8 = 35 - 28x \\\\\n& 14x + 28x = 35 + 8 \\\\\n& 42x = 43 \\implies \\mathbf{x = \\frac{43}{42}} \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & \\text{Denominators are both } 5 \\implies \\mathbf{\\text{LCD} = 5} \\\\\n& 5 \\cdot \\left(\\frac{3}{5}\\right) + 5 \\cdot \\left(\\frac{x}{5}\\right) = 5 \\cdot (18) \\\\\n& 3 + x = 90 \\implies \\mathbf{x = 87}\n\\end{aligned}$$",
    pitfall: "**Multiplying Variables:** In 3C, $-x$ must also be multiplied by 28, becoming $-28x$!",
    script: "[Prof. Park] In 3C, denominators 2, 7, 4 give LCD 28. Multiplying every single term by 28 yields $14x - 8 = 35 - 28x \\implies 42x = 43 \\implies x = \\frac{43}{42}$.\n\n[TA Sora] And in 3D, multiplying by 5 gives $3 + x = 90 \\implies x = 87$."
  },
  {
    num: 5,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3E: Clearing Fractions with Parentheses",
    subtitle: "Unit 1 • Lecture 13 • Section 1.7 Example 3E (Workbook p. 21)",
    detail: "Lecture 13: Solving Linear Equations with Fractions (The LCD Clearing Method)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Use clearing fractions to solve (Workbook p. 21)\n$$\\frac{1}{7}(x - 4) + 5 = \\frac{1}{2}(3x + 4)$$",
    solution: "$$\\begin{aligned}\n\\text{Step 1: } & \\text{Denominators: } 7, 2 \\implies \\mathbf{\\text{LCD} = 14} \\\\[0.8em]\n\\text{Step 2: } & \\text{Multiply every term by } 14: \\\\\n& 14 \\cdot \\left[\\frac{1}{7}(x - 4)\\right] + 14 \\cdot (5) = 14 \\cdot \\left[\\frac{1}{2}(3x + 4)\\right] \\\\\n& 2(x - 4) + 70 = 7(3x + 4) \\\\[0.8em]\n\\text{Step 3: } & \\text{Distribute and solve:} \\\\\n& 2x - 8 + 70 = 21x + 28 \\\\\n& 2x + 62 = 21x + 28 \\\\\n& 62 - 28 = 21x - 2x \\\\\n& 34 = 19x \\implies \\mathbf{x = \\frac{34}{19}}\n\\end{aligned}$$",
    pitfall: "**Multiplying Terms with Parentheses:** In $14 \\cdot \\frac{1}{7}(x - 4)$, the 14 only multiplies the fraction $\\frac{1}{7}$ to make 2! Do NOT multiply inside the parentheses yet!",
    script: "[Prof. Park] In 3E, denominators 7 and 2 have LCD 14. Sora, how do we multiply $14 \\cdot \\frac{1}{7}(x - 4)$?\n\n[TA Sora] Just multiply 14 by $\\frac{1}{7}$, which is 2! Leave $(x - 4)$ alone inside for now. And don't forget $14 \\cdot 5 = 70$!\n\n[Prof. Park] Distributing gives $2x + 62 = 21x + 28 \\implies 19x = 34 \\implies x = \\frac{34}{19}$."
  },
  {
    num: 6,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 3F & 3G: Fractional Proportions & Compound Terms",
    subtitle: "Unit 1 • Lecture 13 • Section 1.7 Example 3F & 3G (Workbook p. 22)",
    detail: "Lecture 13: Solving Linear Equations with Fractions (The LCD Clearing Method)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Use clearing fractions to solve (Workbook p. 22)\n$$\\text{F. } \\frac{x - 7}{8} = \\frac{5}{6}$$\n$$\\text{G. } \\frac{1}{3}(3m + 1) = \\frac{1}{4}(m - 4) + 1$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ F:}\\quad & \\text{LCD of } 8 \\text{ and } 6 \\text{ is } 24. \\\\\n& 24 \\cdot \\left(\\frac{x - 7}{8}\\right) = 24 \\cdot \\left(\\frac{5}{6}\\right) \\\\\n& 3(x - 7) = 4(5) \\implies 3x - 21 = 20 \\\\\n& 3x = 41 \\implies \\mathbf{x = \\frac{41}{3}} \\\\[1em]\n\\mathbf{Part\\ G:}\\quad & \\text{LCD of } 3 \\text{ and } 4 \\text{ is } 12. \\\\\n& 12 \\cdot \\left[\\frac{1}{3}(3m + 1)\\right] = 12 \\cdot \\left[\\frac{1}{4}(m - 4)\\right] + 12 \\cdot (1) \\\\\n& 4(3m + 1) = 3(m - 4) + 12 \\\\\n& 12m + 4 = 3m - 12 + 12 \\implies 12m + 4 = 3m \\\\\n& 9m = -4 \\implies \\mathbf{m = -\\frac{4}{9}}\n\\end{aligned}$$",
    pitfall: "**Don't forget the +1 in 3G:** $12 \\cdot 1 = 12$. Notice on the right side: $-12 + 12 = 0$, leaving just $3m$!",
    script: "[Prof. Park] In 3F, LCD 24 gives $3(x - 7) = 20 \\implies 3x - 21 = 20 \\implies x = \\frac{41}{3}$.\n\n[TA Sora] And in 3G, LCD 12 gives $4(3m + 1) = 3(m - 4) + 12 \\implies 12m + 4 = 3m \\implies 9m = -4 \\implies m = -\\frac{4}{9}$!\n\n[Prof. Park] Excellent! That solves every problem in Section 1.7."
  }
];

const L14 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Core Concept & Definition",
    title: "Section 1.8: Solving Formulas for a Specified Variable",
    subtitle: "Unit 1 • Lecture 14 • Section 1.8 (Workbook p. 23)",
    detail: "Lecture 14: Solving Formulas for a Specified Variable (Literal Equations)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Literal Equations & Formulas (Workbook p. 23)\n- **Literal Equation / Formula:** An equation containing **multiple variables** ($a, b, x, y, r, t$).\n- **Solving for a Specified Variable:** Isolating that target variable completely on one side.\n- **Strategy:** Treat all other letters exactly like known constants/numbers!\n$$\\text{If you would subtract 5, subtract } x\\text{! If you would divide by 3, divide by } m\\text{!}$$",
    solution: "$$\\begin{aligned}\n\\text{Linear Model: } & 3x + y = 8 \\implies y = 8 - 3x \\\\\n\\text{Multiplication Model: } & d = rt \\implies r = \\frac{d}{t}\n\\end{aligned}$$",
    pitfall: "**Sora's Reminder:** The rules do NOT change just because letters are involved. Use the exact same properties of equality!",
    script: "[Prof. Park] Welcome to Lecture 14! Today we explore Section 1.8 on pages 23 and 24 of your workbook: Solving Formulas for a Specified Variable.\n\n[TA Sora] Many students get intimidated when an equation has 4 different letters. But treat the letter you want like the hero of the story, and treat all other letters like regular numbers! Let's see Example 1 on Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1A & 1B: Solving Linear Equations for y",
    subtitle: "Unit 1 • Lecture 14 • Section 1.8 Example 1A & 1B (Workbook p. 23)",
    detail: "Lecture 14: Solving Formulas for a Specified Variable (Literal Equations)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve each formula for y (Workbook p. 23)\n$$\\text{A. } 3x + y = 8$$\n$$\\text{B. } 2x - 5y = 12$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & \\text{Isolate } y \\text{ by subtracting } 3x \\text{ from both sides:} \\\\\n& 3x + y - 3x = 8 - 3x \\\\\n& \\mathbf{y = 8 - 3x} \\quad (\\text{or } \\mathbf{y = -3x + 8}) \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & \\text{Step 1: Subtract } 2x: \\\\\n& -5y = 12 - 2x \\\\\n& \\text{Step 2: Divide by } -5: \\\\\n& y = \\frac{12 - 2x}{-5} = \\mathbf{\\frac{2x - 12}{5}} \\quad \\left(\\text{or } \\mathbf{y = \\frac{2}{5}x - \\frac{12}{5}}\\right)\n\\end{aligned}$$",
    pitfall: "**Dividing by a Negative:** In 1B, dividing by $-5$ flips the signs in the numerator: $\\frac{12 - 2x}{-5} = \\frac{2x - 12}{5}$. Both forms are correct!",
    script: "[Prof. Park] In 1A: $3x + y = 8$. Subtract $3x$: $y = 8 - 3x$.\n\n[TA Sora] In 1B: $2x - 5y = 12$. Subtract $2x$ to get $-5y = 12 - 2x$, then divide by $-5$: $y = \\frac{2x - 12}{5}$ or $\\frac{2}{5}x - \\frac{12}{5}$."
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1C & 1D: Solving for Factored & Monomial Variables",
    subtitle: "Unit 1 • Lecture 14 • Section 1.8 Example 1C & 1D (Workbook p. 23)",
    detail: "Lecture 14: Solving Formulas for a Specified Variable (Literal Equations)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve each formula for y (Workbook p. 23)\n$$\\text{C. } Z = x + wxy$$\n$$\\text{D. } 5xy = 19$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & \\text{Step 1: Subtract } x \\text{ to isolate the } y\\text{-term:} \\\\\n& Z - x = wxy \\\\\n& \\text{Step 2: Divide both sides by the coefficients of } y \\text{, which are } wx: \\\\\n& \\mathbf{y = \\frac{Z - x}{wx}} \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & \\text{Divide both sides by } 5x: \\\\\n& \\mathbf{y = \\frac{19}{5x}}\n\\end{aligned}$$",
    pitfall: "**Multi-Variable Coefficients:** In 1C, $w$ and $x$ are multiplying $y$. To isolate $y$, divide by the entire package $wx$!",
    script: "[Prof. Park] In 1C, $Z = x + wxy$. First subtract $x$: $Z - x = wxy$. Then divide by $wx$ to isolate $y$: $y = \\frac{Z - x}{wx}$.\n\n[TA Sora] And in 1D, $5x$ is multiplying $y$. Divide by $5x$ to get $y = \\frac{19}{5x}$."
  },
  {
    num: 4,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2A & 2B: Solving for Specified Variable b",
    subtitle: "Unit 1 • Lecture 14 • Section 1.8 Example 2A & 2B (Workbook p. 23)",
    detail: "Lecture 14: Solving Formulas for a Specified Variable (Literal Equations)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve each literal equation for the specified variable (Workbook p. 23)\n$$\\text{A. } a + b - c = d; \\quad \\text{solve for } b$$\n$$\\text{B. } ax^2 + bx + c = 0; \\quad \\text{solve for } b$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & \\text{Subtract } a \\text{ and add } c \\text{ to both sides:} \\\\\n& b = d - a + c \\\\\n& \\mathbf{b = d - a + c} \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & \\text{Step 1: Move all non-}b \\text{ terms to the right side:} \\\\\n& bx = -ax^2 - c \\\\\n& \\text{Step 2: Divide both sides by } x: \\\\\n& \\mathbf{b = \\frac{-ax^2 - c}{x}} \\quad \\left(\\text{or } \\mathbf{b = -ax - \\frac{c}{x}}\\right)\n\\end{aligned}$$",
    pitfall: "**Treating Terms as Blocks:** In 2B, $ax^2$ and $c$ have no $b$. Move them as complete units over to the right side!",
    script: "[Prof. Park] In 2A, solve $a + b - c = d$ for $b$. Subtract $a$ and add $c$: $b = d - a + c$.\n\n[TA Sora] In 2B, solve the standard quadratic form for $b$. Move $ax^2$ and $c$ to the right: $bx = -ax^2 - c$. Then divide by $x$: $b = \\frac{-ax^2 - c}{x}$."
  },
  {
    num: 5,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2C & 2D: Solving Fractional Formulas for r",
    subtitle: "Unit 1 • Lecture 14 • Section 1.8 Example 2C & 2D (Workbook p. 24)",
    detail: "Lecture 14: Solving Formulas for a Specified Variable (Literal Equations)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve each formula for r (Workbook p. 24)\n$$\\text{C. } m = \\frac{r - 7n}{5}; \\quad \\text{solve for } r$$\n$$\\text{D. } t = \\frac{d}{r}; \\quad \\text{solve for } r$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & \\text{Step 1: Multiply both sides by } 5: \\\\\n& 5m = r - 7n \\\\\n& \\text{Step 2: Add } 7n \\text{ to both sides:} \\\\\n& \\mathbf{r = 5m + 7n} \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & \\text{Target } r \\text{ is in the denominator! Multiply by } r \\text{ first:} \\\\\n& r \\cdot t = d \\\\\n& \\text{Now divide by } t: \\\\\n& \\mathbf{r = \\frac{d}{t}}\n\\end{aligned}$$",
    pitfall: "**Variable in Denominator Trap:** In 2D, you CANNOT solve for $r$ while it is trapped in the bottom! Multiply by $r$ first to bring it upstairs: $rt = d \\implies r = \\frac{d}{t}$!",
    script: "[Prof. Park] In 2C, clear the denominator 5 first: $5m = r - 7n \\implies r = 5m + 7n$.\n\n[TA Sora] And in 2D, the variable $r$ is trapped in the denominator! Never divide by $d$ while $r$ is downstairs. Multiply by $r$ first to get $rt = d$, then divide by $t$ to get $r = \\frac{d}{t}$!"
  },
  {
    num: 6,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2E & 2F: Geometric Formulas for W",
    subtitle: "Unit 1 • Lecture 14 • Section 1.8 Example 2E & 2F (Workbook p. 24)",
    detail: "Lecture 14: Solving Formulas for a Specified Variable (Literal Equations)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve each geometry formula for W (Workbook p. 24)\n$$\\text{E. } P = 2L + 2W; \\quad \\text{solve for } W$$\n$$\\text{F. } V = LWH; \\quad \\text{solve for } W$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ E\\ (Perimeter):}\\quad & \\text{Step 1: Subtract } 2L \\text{ from both sides:} \\\\\n& P - 2L = 2W \\\\\n& \\text{Step 2: Divide by } 2: \\\\\n& \\mathbf{W = \\frac{P - 2L}{2}} \\quad \\left(\\text{or } \\mathbf{W = \\frac{P}{2} - L}\\right) \\\\[1em]\n\\mathbf{Part\\ F\\ (Volume):}\\quad & \\text{Divide both sides by } LH: \\\\\n& \\mathbf{W = \\frac{V}{LH}}\n\\end{aligned}$$",
    pitfall: "**Don't Cancel the 2 Illegally!** In Part E, $\\frac{P - 2L}{2} \\neq P - L$! The 2 divides the ENTIRE numerator, so it becomes $\\frac{P}{2} - L$!",
    script: "[Prof. Park] In 2E, $P = 2L + 2W$. Subtract $2L$ to get $P - 2L = 2W$, then divide by 2: $W = \\frac{P - 2L}{2}$.\n\n[TA Sora] And in 2F, $V = LWH$. Divide by the package $LH$ to get $W = \\frac{V}{LH}$."
  },
  {
    num: 7,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Section 1.8 Review: Solving Equations by Clearing Fractions",
    subtitle: "Unit 1 • Lecture 14 • Section 1.8 Review A & B (Workbook p. 24)",
    detail: "Lecture 14: Solving Formulas for a Specified Variable (Literal Equations)",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### REVIEW: Solve the following equations by clearing fractions (Workbook p. 24)\n$$\\text{A. } \\frac{y - 2}{5} = \\frac{3}{2}y + \\frac{4}{5}$$\n$$\\text{B. } \\frac{2}{7} = \\frac{3}{7}(x - 4) - \\frac{5}{7}$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Review\\ A:}\\quad & \\text{Denominators: } 5, 2 \\implies \\mathbf{\\text{LCD} = 10} \\\\\n& 10 \\cdot \\left(\\frac{y - 2}{5}\\right) = 10 \\cdot \\left(\\frac{3}{2}y\\right) + 10 \\cdot \\left(\\frac{4}{5}\\right) \\\\\n& 2(y - 2) = 15y + 8 \\\\\n& 2y - 4 = 15y + 8 \\implies -12 = 13y \\implies \\mathbf{y = -\\frac{12}{13}} \\\\[1em]\n\\mathbf{Review\\ B:}\\quad & \\text{Denominators are all } 7 \\implies \\mathbf{\\text{LCD} = 7} \\\\\n& 7 \\cdot \\left(\\frac{2}{7}\\right) = 7 \\cdot \\left[\\frac{3}{7}(x - 4)\\right] - 7 \\cdot \\left(\\frac{5}{7}\\right) \\\\\n& 2 = 3(x - 4) - 5 \\\\\n& 2 = 3x - 12 - 5 \\implies 2 = 3x - 17 \\implies 19 = 3x \\implies \\mathbf{x = \\frac{19}{3}}\n\\end{aligned}$$",
    pitfall: "**Multiplying Binomial Numerator:** In Review A, $10 \\div 5 = 2$, which must distribute to $(y - 2)$ to make $2y - 4$!",
    script: "[Prof. Park] Page 24 ends with two cumulative review problems. In Review A, multiplying by LCD 10 gives $2(y - 2) = 15y + 8 \\implies 2y - 4 = 15y + 8 \\implies y = -\\frac{12}{13}$.\n\n[TA Sora] And in Review B, multiplying by 7 clears all denominators instantly: $2 = 3(x - 4) - 5 \\implies 2 = 3x - 17 \\implies x = \\frac{19}{3}$!"
  }
];

const L15 = [
  {
    num: 1,
    type: "math_problem",
    slideTypeLabel: "Core Inequality Law",
    title: "Section 1.9: Solving Linear Inequalities & Interval Notation",
    subtitle: "Unit 1 • Lecture 15 • Section 1.9 (Workbook p. 25)",
    detail: "Lecture 15: Solving Linear Inequalities, Interval Notation & Unit 1 Grand Review",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### The Golden Rule of Inequalities (Workbook p. 25-26)\n$$\\text{When you MULTIPLY or DIVIDE both sides by a NEGATIVE number,}$$ $$\\text{you MUST REVERSE (FLIP) the inequality symbol!}$$\n- Example: $-2x < 6 \\implies \\frac{-2x}{-2} > \\frac{6}{-2} \\implies \\mathbf{x > -3}$.\n- **Interval Notation:** Parentheses $( \\ )$ for strict ($<, >$), brackets $[ \\ ]$ for inclusive ($\\le, \\ge$).\n- **Infinities:** $\\infty$ and $-\\infty$ **ALWAYS take parentheses**.",
    solution: "$$\\begin{aligned}\n\\text{Strict: } & x > a \\implies (a, \\infty) \\quad \\text{and} \\quad x < a \\implies (-\\infty, a) \\\\\n\\text{Inclusive: } & x \\ge a \\implies [a, \\infty) \\quad \\text{and} \\quad x \\le a \\implies (-\\infty, a]\n\\end{aligned}$$",
    pitfall: "**Sora's Absolute Rule:** If you don't flip the sign when dividing by a negative, your entire solution set is reversed and wrong!",
    script: "[Prof. Park] Welcome to Lecture 15, the grand finale of Unit 1! Today we conquer Section 1.9 on pages 25 and 26: Solving Linear Inequalities.\n\n[TA Sora] The #1 rule: Whenever you multiply or divide by a negative number, FLIP THE INEQUALITY SIGN! Let's see Example 1 on Slide 2."
  },
  {
    num: 2,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1A & 1B: Basic Interval Notation",
    subtitle: "Unit 1 • Lecture 15 • Section 1.9 Example 1A & 1B (Workbook p. 25)",
    detail: "Lecture 15: Solving Linear Inequalities, Interval Notation & Unit 1 Grand Review",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Represent each on a number line graph and convert to interval notation (Workbook p. 25)\n$$\\text{A. } x > 5$$\n$$\\text{B. } x < -6$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & \\text{Open circle at } 5, \\text{ shaded to the right towards } +\\infty \\\\\n& \\mathbf{(5, \\infty)} \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & \\text{Open circle at } -6, \\text{ shaded to the left towards } -\\infty \\\\\n& \\mathbf{(-\\infty, -6)}\n\\end{aligned}$$",
    pitfall: "**Order Matters:** In interval notation, always list numbers from LEFT to RIGHT as they appear on the number line! $(-\\infty, -6)$, NOT $(-6, -\\infty)$!",
    script: "[Prof. Park] In 1A: $x > 5$. That means all numbers strictly greater than 5, stretching to infinity: $(5, \\infty)$.\n\n[TA Sora] And in 1B: $x < -6$. That starts at negative infinity and stops at $-6$: $(-\\infty, -6)$."
  },
  {
    num: 3,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1C & 1D: Variable on the Right Side",
    subtitle: "Unit 1 • Lecture 15 • Section 1.9 Example 1C & 1D (Workbook p. 25)",
    detail: "Lecture 15: Solving Linear Inequalities, Interval Notation & Unit 1 Grand Review",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Represent on number line and convert to interval notation (Workbook p. 25)\n$$\\text{C. } -3 \\le x$$\n$$\\text{D. } 12 \\ge x$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & \\text{Step 1: Rewrite with } x \\text{ on the left side (keep arrow pointing at } -3\\text{):} \\\\\n& -3 \\le x \\iff \\mathbf{x \\ge -3} \\\\\n& \\text{Solid bracket at } -3, \\text{ shade right: } \\mathbf{[-3, \\infty)} \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & \\text{Step 1: Rewrite with } x \\text{ on the left side (arrow points at } x\\text{):} \\\\\n& 12 \\ge x \\iff \\mathbf{x \\le 12} \\\\\n& \\text{Solid bracket at } 12, \\text{ shade left: } \\mathbf{(-\\infty, 12]}\n\\end{aligned}$$",
    pitfall: "**Reading Direction Trap:** When $x$ is on the right, read from the variable! $-3 \\le x$ means '$x$ is greater than or equal to $-3$'! Always rewrite with $x$ on the left first!",
    script: "[Prof. Park] In 1C: $-3 \\le x$. Sora, what should students do when the variable is on the right?\n\n[TA Sora] Flip the whole statement so $x$ comes first! Keep the small point pointing at $-3$: $x \\ge -3$. That means $[-3, \\infty)$!\n\n[Prof. Park] In 1D: $12 \\ge x$ means $x \\le 12$. That is $(-\\infty, 12]$."
  },
  {
    num: 4,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1E & 1F: Double (Bounded) Inequalities",
    subtitle: "Unit 1 • Lecture 15 • Section 1.9 Example 1E & 1F (Workbook p. 25)",
    detail: "Lecture 15: Solving Linear Inequalities, Interval Notation & Unit 1 Grand Review",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Represent on number line and convert to interval notation (Workbook p. 25)\n$$\\text{E. } -3 < x < 1$$\n$$\\text{F. } 2 \\le x < 3$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ E:}\\quad & x \\text{ is trapped strictly between } -3 \\text{ and } 1. \\\\\n& \\text{Open circles at both ends: } \\mathbf{(-3, 1)} \\\\[1em]\n\\mathbf{Part\\ F:}\\quad & x \\text{ is greater than or equal to } 2, \\text{ but strictly less than } 3. \\\\\n& \\text{Solid bracket at } 2, \\text{ parenthesis at } 3: \\mathbf{[2, 3)}\n\\end{aligned}$$",
    pitfall: "**Mixed Endpoints:** In 1F, $2$ is included (bracket $[$), but $3$ is strict (parenthesis $)$). Never write $[2, 3]$!",
    script: "[Prof. Park] In 1E, $x$ is trapped between $-3$ and $1$. Both are strict, so we write $(-3, 1)$.\n\n[TA Sora] In 1F, $x$ includes 2, but does not include 3. Bracket at 2, parenthesis at 3: $[2, 3)$!"
  },
  {
    num: 5,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 1G & 1H: Disjoint Compound Inequalities (Union)",
    subtitle: "Unit 1 • Lecture 15 • Section 1.9 Example 1G & 1H (Workbook p. 25)",
    detail: "Lecture 15: Solving Linear Inequalities, Interval Notation & Unit 1 Grand Review",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Represent on number line and convert to interval notation (Workbook p. 25)\n$$\\text{G. } x < -7 \\text{ or } x \\ge 0$$\n$$\\text{H. } x \\le 2 \\text{ or } x > 5$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ G:}\\quad & \\text{Two separate arrows pointing outward:} \\\\\n& x < -7 \\implies (-\\infty, -7) \\\\\n& x \\ge 0 \\implies [0, \\infty) \\\\\n& \\text{Combine with union symbol } \\cup: \\mathbf{(-\\infty, -7) \\cup [0, \\infty)} \\\\[1em]\n\\mathbf{Part\\ H:}\\quad & x \\le 2 \\implies (-\\infty, 2] \\\\\n& x > 5 \\implies (5, \\infty) \\\\\n& \\text{Combine with union: } \\mathbf{(-\\infty, 2] \\cup (5, \\infty)}\n\\end{aligned}$$",
    pitfall: "**Union Symbol:** Use $\\cup$ (union) to glue two disjoint intervals together!",
    script: "[Prof. Park] When an inequality says 'or', the solutions point in opposite directions.\n\n[TA Sora] In 1G, $(-\\infty, -7)$ combined with $[0, \\infty)$ using the union symbol $\\cup$: $(-\\infty, -7) \\cup [0, \\infty)$. Same in 1H: $(-\\infty, 2] \\cup (5, \\infty)$!"
  },
  {
    num: 6,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2A & 2B: Solving Linear Inequalities",
    subtitle: "Unit 1 • Lecture 15 • Section 1.9 Example 2A & 2B (Workbook p. 26)",
    detail: "Lecture 15: Solving Linear Inequalities, Interval Notation & Unit 1 Grand Review",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve each inequality. Write final answer in interval notation (Workbook p. 26)\n$$\\text{A. } -6 + 3x \\le -12 + 5x$$\n$$\\text{B. } 4(5x - 7) > 10 + 5x$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ A:}\\quad & 3x - 5x \\le -12 + 6 \\\\\n& -2x \\le -6 \\\\\n& \\text{Divide by } -2 \\text{ and } \\textbf{FLIP the inequality sign!} \\\\\n& x \\ge \\frac{-6}{-2} \\implies x \\ge 3 \\implies \\mathbf{[3, \\infty)} \\\\[1em]\n\\mathbf{Part\\ B:}\\quad & 20x - 28 > 10 + 5x \\\\\n& 20x - 5x > 10 + 28 \\\\\n& 15x > 38 \\\\\n& x > \\frac{38}{15} \\implies \\mathbf{\\left(\\frac{38}{15}, \\infty\\right)}\n\\end{aligned}$$",
    pitfall: "**The Flip in 2A:** Dividing $-2x \\le -6$ by $-2$ FLIPS the sign to $\\ge$: $x \\ge 3$, meaning $[3, \\infty)$!",
    script: "[Prof. Park] In 2A, subtracting $5x$ gives $-2x \\le -6$. Dividing by $-2$ flips $\\le$ to $\\ge$: $x \\ge 3 \\implies [3, \\infty)$.\n\n[TA Sora] In 2B, distribute first: $20x - 28 > 10 + 5x \\implies 15x > 38 \\implies x > \\frac{38}{15} \\implies (\\frac{38}{15}, \\infty)$."
  },
  {
    num: 7,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2C & 2D: Inequalities with Fractions & Negatives",
    subtitle: "Unit 1 • Lecture 15 • Section 1.9 Example 2C & 2D (Workbook p. 26)",
    detail: "Lecture 15: Solving Linear Inequalities, Interval Notation & Unit 1 Grand Review",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve each inequality and write in interval notation (Workbook p. 26)\n$$\\text{C. } \\frac{4}{5}y + 5 < 6$$\n$$\\text{D. } 2 \\le \\frac{x}{-8} - 3$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ C:}\\quad & \\text{Subtract } 5: \\quad \\frac{4}{5}y < 1 \\\\\n& \\text{Multiply by } \\frac{5}{4}: \\quad y < \\frac{5}{4} \\implies \\mathbf{\\left(-\\infty, \\frac{5}{4}\\right)} \\\\[1em]\n\\mathbf{Part\\ D:}\\quad & \\text{Add } 3 \\text{ to both sides:} \\quad 5 \\le \\frac{x}{-8} \\\\\n& \\text{Multiply by } -8 \\text{ and } \\textbf{FLIP the inequality sign!} \\\\\n& -8 \\cdot 5 \\ge x \\implies -40 \\ge x \\iff x \\le -40 \\\\\n& \\mathbf{(-\\infty, -40]}\n\\end{aligned}$$",
    pitfall: "**Multiplying by Negative Denominator:** In 2D, multiplying by $-8$ flips $\\le$ to $\\ge$! $-40 \\ge x$ means $x \\le -40$, which is $(-\\infty, -40]$!",
    script: "[Prof. Park] In 2C, subtracting 5 gives $\\frac{4}{5}y < 1 \\implies y < \\frac{5}{4} \\implies (-\\infty, \\frac{5}{4})$.\n\n[TA Sora] And in 2D, adding 3 gives $5 \\le \\frac{x}{-8}$. Multiplying by $-8$ flips the sign: $-40 \\ge x \\implies x \\le -40 \\implies (-\\infty, -40]$!"
  },
  {
    num: 8,
    type: "math_problem",
    slideTypeLabel: "Official Workbook Problem",
    title: "Example 2E & 2F: Binomial Numerator Inequality Comparison",
    subtitle: "Unit 1 • Lecture 15 • Section 1.9 Example 2E & 2F (Workbook p. 26)",
    detail: "Lecture 15: Solving Linear Inequalities, Interval Notation & Unit 1 Grand Review",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Solve both and compare the effect of negative denominator (Workbook p. 26)\n$$\\text{E. } \\frac{x - 30}{-4} \\ge 50$$\n$$\\text{F. } \\frac{x - 30}{4} > 50$$",
    solution: "$$\\begin{aligned}\n\\mathbf{Part\\ E:}\\quad & \\text{Multiply by } -4 \\text{ and } \\textbf{FLIP} \\ge \\text{ to } \\le: \\\\\n& x - 30 \\le 50 \\cdot (-4) \\\\\n& x - 30 \\le -200 \\implies x \\le -170 \\implies \\mathbf{(-\\infty, -170]} \\\\[1em]\n\\mathbf{Part\\ F:}\\quad & \\text{Multiply by positive } 4 \\text{ (sign does } \\textbf{NOT} \\text{ flip!):} \\\\\n& x - 30 > 50 \\cdot 4 \\\\\n& x - 30 > 200 \\implies x > 230 \\implies \\mathbf{(230, \\infty)}\n\\end{aligned}$$",
    pitfall: "**Compare the Two:** In 2E, the $-4$ in the denominator flips $\\ge$ to $\\le$, pointing left! In 2F, the positive $4$ keeps $>$ pointing right! Two totally different answers!",
    script: "[Prof. Park] Compare Examples 2E and 2F side-by-side. In 2E, multiplying by $-4$ flips the inequality to $x - 30 \\le -200 \\implies x \\le -170 \\implies (-\\infty, -170]$.\n\n[TA Sora] But in 2F, 4 is positive, so the sign stays $>$: $x - 30 > 200 \\implies x > 230 \\implies (230, \\infty)$. What a perfect demonstration of the negative multiplication rule!"
  },
  {
    num: 9,
    type: "math_problem",
    slideTypeLabel: "Course Milestone & Synthesis",
    title: "Unit 1 Grand Review & Sora's 10 Core Commandments",
    subtitle: "Unit 1 • Lecture 15 • Unit 1 Complete Synthesis",
    detail: "Lecture 15: Solving Linear Inequalities, Interval Notation & Unit 1 Grand Review",
    instructor: "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    problem: "### Congratulations on Completing Unit 1 (Sections 1.0 - 1.9)!\n- **1. Order of Operations:** PEMDAS always rules.\n- **2. Substitution:** Always wrap substituted numbers in parentheses.\n- **3. Exponents:** $a^0 = 1$, $a^{-n} = \\frac{1}{a^n}$, $a^m a^n = a^{m+n}$, $(a^m)^n = a^{mn}$.\n- **4. Distributive Property:** Watch minus signs inside parentheses!\n- **5. Polynomial Multiplication:** FOIL requires $(2y - 7)^2 = 4y^2 - 28y + 49$.\n- **6. Rational Expressions:** Add/subtract ONLY with common denominator (LCD).\n- **7. Linear Equations:** Balance scale—isolate the variable.\n- **8. Equation Clearing:** Multiply EVERY term by LCD to clear fractions.\n- **9. Classification:** Conditional (1 solution), Identity (all real numbers), Contradiction (no solution).\n- **10. Inequalities:** FLIP the symbol when multiplying or dividing by a negative number!",
    solution: "$$\\mathbf{\\text{Unit 1 Mastered! Next Up: Unit 2 — Graphing, Lines, and Functions!}}$$",
    pitfall: "**Confidence Note:** Review all 15 workbook sections before Exam 1. You have every tool you need to succeed!",
    script: "[Prof. Park] Students, give yourselves a massive round of applause! You have completed all 15 lectures of Unit 1 in M090 Introductory Algebra!\n\n[TA Sora] We have covered every single problem, every example, and every board work exercise in your workbook from page 3 to page 26 without skipping a single detail.\n\n[Prof. Park] Review these slides, practice your workbook problems, and you will walk into Exam 1 with complete confidence. Next time, we begin Unit 2: Graphing, Lines, and Functions!\n\n[TA Sora] Go Bobcats! See you in Unit 2!"
  }
];

// Now update src/data/montanaSlidesData.js
let fileContent = fs.readFileSync('src/data/montanaSlidesData.js', 'utf8');

function replaceLecture(source, lNum, newSlides) {
  const pad = lNum < 10 ? '0' + lNum : '' + lNum;
  const startTag = `export const SLIDES_MONTANA_L${pad} = [`;
  const nextTag = lNum < 15 ? `export const SLIDES_MONTANA_L${lNum < 9 ? '0' + (lNum + 1) : '' + (lNum + 1)} = [` : 'export const MONTANA_ALL_SLIDES';
  
  const startIdx = source.indexOf(startTag);
  const endIdx = source.indexOf(nextTag);
  
  if (startIdx === -1 || endIdx === -1) {
    throw new Error(`Could not find boundaries for L${pad}`);
  }
  
  const formatted = JSON.stringify(newSlides, null, 2);
  const replacement = `export const SLIDES_MONTANA_L${pad} = ${formatted};\n\n`;
  
  return source.slice(0, startIdx) + replacement + source.slice(endIdx);
}

fileContent = replaceLecture(fileContent, 7, L07);
fileContent = replaceLecture(fileContent, 8, L08);
fileContent = replaceLecture(fileContent, 9, L09);
fileContent = replaceLecture(fileContent, 10, L10);
fileContent = replaceLecture(fileContent, 11, L11);
fileContent = replaceLecture(fileContent, 12, L12);
fileContent = replaceLecture(fileContent, 13, L13);
fileContent = replaceLecture(fileContent, 14, L14);
fileContent = replaceLecture(fileContent, 15, L15);

fs.writeFileSync('src/data/montanaSlidesData.js', fileContent, 'utf8');
console.log('Successfully updated Lectures 07 through 15 in src/data/montanaSlidesData.js!');
