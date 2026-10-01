# Lecture 40 - 8 slides

## Slide 1: Section 3.4: Completing the Square

**Subtitle:** Unit 3 • Lecture 40 • Section 3.4 (Workbook p. 75)

### Problem
### Why Complete the Square? (Workbook p. 75)
Many quadratic equations cannot be factored using whole numbers.
**Completing the Square** is an algebraic technique that turns ANY quadratic expression into a **perfect square binomial**:
$$x^2 + bx + \mathbf{\left(\frac{b}{2}\right)^2} = \mathbf{\left(x + \frac{b}{2}\right)^2}$$
- Then we can solve it using the **Square Root Property** from Section 3.2!
- The 'magic number' you must add to both sides is **$\left(\frac{b}{2}\right)^2$**.

### Solution
$$\begin{aligned}
\text{Magic Number: } & \mathbf{\left(\frac{b}{2}\right)^2} \\[0.5em]
\text{Take half of } b: & \frac{b}{2} \\
\text{Square it: } & \left(\frac{b}{2}\right)^2 \\
\text{Factor result: } & \left(x + \frac{b}{2}\right)^2
\end{aligned}$$

### Key Note
**Add to BOTH sides:** When solving an equation, if you add $(\frac{b}{2})^2$ to the left side, you MUST add it to the right side to keep the balance!

### Script
[Prof. Park] Welcome to Section 3.4! Completing the Square is one of the greatest triumphs of classical algebra.

[TA Sora] It forces a stubborn expression into a perfect square $(x + \frac{b}{2})^2$ so we can use our trusty Square Root Property!

---

## Slide 2: Section 3.4 Example 1: Finding the 'Magic Number'

**Subtitle:** Unit 3 • Lecture 40 • Section 3.4 Example 1 (Workbook p. 75)

### Problem
### Example 1 (Workbook p. 75)
Find the constant term that must be added to each binomial to make it a perfect square trinomial, then write the factored form:
- **A.** $x^2 + 6x + \underline{\quad}$
- **B.** $x^2 - 10x + \underline{\quad}$
- **C.** $x^2 + 5x + \underline{\quad}$

### Solution
$$\begin{aligned}
\textbf{A. } b = 6: & \quad \left(\frac{6}{2}\right)^2 = (3)^2 = \mathbf{9} \implies x^2 + 6x + 9 = \mathbf{(x + 3)^2} \\[0.8em]
\textbf{B. } b = -10: & \quad \left(\frac{-10}{2}\right)^2 = (-5)^2 = \mathbf{25} \implies x^2 - 10x + 25 = \mathbf{(x - 5)^2} \\[0.8em]
\textbf{C. } b = 5: & \quad \left(\frac{5}{2}\right)^2 = \mathbf{\frac{25}{4}} \implies x^2 + 5x + \frac{25}{4} = \mathbf{\left(x + \frac{5}{2}\right)^2}
\end{aligned}$$

### Key Note
**The number inside the factored binomial:** The number inside the parentheses is ALWAYS half of $b$ ($rac{b}{2}$)! Look at $x+3$ (half of 6) and $x-5$ (half of $-10$)!

### Script
[Prof. Park] In Example 1, take half of $b$ and square it. Half of 6 is 3, squared is 9. Factor is $(x + 3)^2$.

[TA Sora] Half of $-10$ is $-5$, squared is 25. Factor is $(x - 5)^2$!

---

## Slide 3: Section 3.4 Example 2: Solving x^2 + 6x = 7

**Subtitle:** Unit 3 • Lecture 40 • Section 3.4 Example 2 (Workbook p. 75)

### Problem
### Example 2 (Workbook p. 75)
Solve the equation by completing the square:
$$\mathbf{x^2 + 6x = 7}$$
- Add $(\frac{6}{2})^2 = 9$ to both sides.
- Factor the left side as a perfect square.
- Apply the Square Root Property and solve.

### Solution
$$\begin{aligned}
x^2 + 6x & = 7 \\[0.5em]
x^2 + 6x + \mathbf{9} & = 7 + \mathbf{9} \quad (\text{add } 9 \text{ to BOTH sides!}) \\[0.5em]
(x + 3)^2 & = 16 \\[0.5em]
x + 3 & = \pm \sqrt{16} \\[0.5em]
x + 3 & = \pm 4 \\[0.5em]
x & = -3 \pm 4 \\[0.8em]
\text{Case 1: } & x = -3 + 4 = \mathbf{1} \\
\text{Case 2: } & x = -3 - 4 = \mathbf{-7} \\[0.8em]
\mathbf{\text{Solutions: }} & \mathbf{x = 1 \quad \text{and} \quad x = -7}
\end{aligned}$$

### Key Note
**Subtract 3 in front:** $x + 3 = \pm 4 \implies x = -3 \pm 4$. Subtract 3 from both sides!

### Script
[Prof. Park] In Example 2, add 9 to both sides: $(x + 3)^2 = 16$. Square root gives $x + 3 = \pm 4$.

[TA Sora] Subtract 3: $-3 + 4 = 1$, and $-3 - 4 = -7$. Two clean integer roots!

---

## Slide 4: Section 3.4 Example 3: Solving x^2 - 8x - 5 = 0

**Subtitle:** Unit 3 • Lecture 40 • Section 3.4 Example 3 (Workbook p. 76)

### Problem
### Example 3 (Workbook p. 76)
Solve the equation by completing the square:
$$\mathbf{x^2 - 8x - 5 = 0}$$
- Move the constant $-5$ to the right side first.
- Add $(\frac{-8}{2})^2 = 16$ to both sides.
- Solve for exact radical answers.

### Solution
$$\begin{aligned}
x^2 - 8x & = 5 \quad (\text{move constant to right side}) \\[0.5em]
x^2 - 8x + \mathbf{16} & = 5 + \mathbf{16} \quad \left(\text{add } \left(\frac{-8}{2}\right)^2 = 16\right) \\[0.5em]
(x - 4)^2 & = 21 \\[0.5em]
x - 4 & = \pm \sqrt{21} \\[0.5em]
\mathbf{x} & = \mathbf{4 \pm \sqrt{21}} \\[0.8em]
\text{Two exact roots: } & \mathbf{x = 4 + \sqrt{21} \approx 8.58} \quad \text{and} \quad \mathbf{x = 4 - \sqrt{21} \approx -0.58}
\end{aligned}$$

### Key Note
**Notice this equation COULD NOT be factored:** There are no whole numbers multiplying to $-5$ and adding to $-8$. Completing the square solved it smoothly!

### Script
[Prof. Park] In Example 3, $x^2 - 8x - 5 = 0$ is unfactorable with integers. But completing the square handles it with ease.

[TA Sora] We get $x = 4 \pm \sqrt{21}$. That is the exact mathematical truth!

---

## Slide 5: Section 3.4 Example 4: Leading Coefficient a != 1

**Subtitle:** Unit 3 • Lecture 40 • Section 3.4 Example 4 (Workbook p. 77)

### Problem
### Example 4: When $a \neq 1$ (Workbook p. 77)
Solve by completing the square:
$$\mathbf{2x^2 + 12x - 10 = 0}$$
- **Golden Rule:** Completing the square requires the leading coefficient to be **$1$**!
- Divide EVERY term on both sides by $2$ first.

### Solution
$$\begin{aligned}
\frac{2x^2 + 12x - 10}{2} & = \frac{0}{2} \\[0.5em]
x^2 + 6x - 5 & = 0 \\[0.5em]
x^2 + 6x & = 5 \\[0.5em]
x^2 + 6x + \mathbf{9} & = 5 + \mathbf{9} \quad \left(\text{add } \left(\frac{6}{2}\right)^2 = 9\right) \\[0.5em]
(x + 3)^2 & = 14 \\[0.5em]
x + 3 & = \pm \sqrt{14} \\[0.5em]
\mathbf{x} & = \mathbf{-3 \pm \sqrt{14}}
\end{aligned}$$

### Key Note
**Divide by a FIRST:** You CANNOT find the magic number while the coefficient of $x^2$ is 2! Always divide everything by $a$ first!

### Script
[Prof. Park] In Example 4, $a = 2$. Divide every single term by 2 before doing anything else!

[TA Sora] $x^2 + 6x - 5 = 0$. Now complete the square by adding 9: $(x + 3)^2 = 14 \implies x = -3 \pm \sqrt{14}$!

---

## Slide 6: Converting General Form to Vertex Form via CTS

**Subtitle:** Unit 3 • Lecture 40 • Section 3.4 Application

### Problem
### Transforming $f(x) = x^2 - 6x + 5$ into Vertex Form
Watch how completing the square transforms General Form into Vertex Form:
- Group the $x$-terms: $(x^2 - 6x) + 5$.
- Complete the square inside: add $9$ and subtract $9$ to keep balance!
- State the vertex $(h, k)$.

### Solution
$$\begin{aligned}
f(x) & = (x^2 - 6x) + 5 \\[0.5em]
& = (x^2 - 6x + \mathbf{9}) + 5 - \mathbf{9} \quad (\text{add and subtract } 9) \\[0.5em]
& = \mathbf{(x - 3)^2 - 4} \\[0.8em]
\mathbf{\text{Vertex: }} & \mathbf{(3, -4)} \quad \implies \quad \text{Vertex Form matches Section 3.0 Example 5!}
\end{aligned}$$

### Key Note
**Add and subtract on the same side:** If you work on one side of an expression, adding $9$ and subtracting $9$ adds zero overall, preserving the equation!

### Script
[Prof. Park] This is how mathematicians convert general form into vertex form!

[TA Sora] $(x - 3)^2 - 4$ gives the vertex $(3, -4)$ immediately without memorizing the vertex formula!

---

## Slide 7: Sora's Complete CTS Protocol

**Subtitle:** Unit 3 • Lecture 40 • Section 3.4 Protocol

### Problem
### Master 5-Step CTS Protocol
1. **Ensure $a = 1$:** If $a \neq 1$, divide all terms on both sides by $a$.
2. **Isolate variable terms:** Move constant $c$ to the right side: $x^2 + bx = -c$.
3. **Compute magic number:** Calculate $(\frac{b}{2})^2$.
4. **Add to BOTH sides:** $x^2 + bx + (\frac{b}{2})^2 = -c + (\frac{b}{2})^2$.
5. **Factor and solve:** $(x + \frac{b}{2})^2 = k \implies x = -\frac{b}{2} \pm \sqrt{k}$.

### Solution
$$\mathbf{\text{Result: Solves EVERY quadratic equation, factorable or unfactorable!}}$$

### Key Note
**Fraction b values:** If $b$ is odd (like $b = 5$), $(\frac{5}{2})^2 = \frac{25}{4}$. Don't fear fractions; just find common denominators!

### Script
[Prof. Park] This 5-step method is foolproof. It works for every single quadratic equation in existence.

[TA Sora] And even more amazingly, if you apply this exact protocol to the general equation $ax^2 + bx + c = 0$, you derive the Quadratic Formula!

---

## Slide 8: Section 3.4 Mastery Summary & The Gateway to the Formula

**Subtitle:** Unit 3 • Lecture 40 • Section 3.4 Wrap-up

### Problem
### The Gateway to Section 3.5
- Completing the square proved that ANY quadratic equation can be solved.
- In Section 3.5, we complete the square on the abstract symbols $ax^2 + bx + c = 0$ once and for all.
- That yields the crown jewel of algebra: **The Quadratic Formula**!

### Solution
$$\mathbf{\text{Section 3.4 Mastered! Next Up: Section 3.5 — The Quadratic Formula!}}$$

### Key Note
**Celebrate your progress:** You have conquered Square Root Property, Factoring, and Completing the Square!

### Script
[Prof. Park] You have conquered three major methods. Now get ready for the grand master key.

[TA Sora] In Lecture 41, we unlock the legendary Quadratic Formula!

---

