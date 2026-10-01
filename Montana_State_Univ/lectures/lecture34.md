# Lecture 34 - 8 slides

## Slide 1: Section 3.1: The Vertex Formula x_v = -b / (2a)

**Subtitle:** Unit 3 • Lecture 34 • Section 3.1 (Workbook p. 63)

### Problem
### The Vertex Formula (Workbook p. 63)
For any quadratic function in General Form $\mathbf{f(x) = ax^2 + bx + c}$:
- **$x$-coordinate of the vertex:**
  $$\mathbf{x_v = -\frac{b}{2a}}$$
- **$y$-coordinate of the vertex:**
  $$\mathbf{y_v = f(x_v)} = f\left(-\frac{b}{2a}\right)$$
- **Axis of Symmetry:** The vertical line $\mathbf{x = -\frac{b}{2a}}$.
- **$y$-intercept:** Always $\mathbf{(0, c)}$ since $f(0) = c$.

### Solution
$$\begin{aligned}
\text{Step 1: } & \text{Identify } a, b, c \text{ from } ax^2 + bx + c. \\
\text{Step 2: } & \text{Compute } x_v = -\frac{b}{2a}. \\
\text{Step 3: } & \text{Substitute } x_v \text{ into } f(x) \text{ to find } y_v. \\
\text{Step 4: } & \text{Vertex is } (x_v, y_v). \text{ Axis of symmetry is } x = x_v.
\end{aligned}$$

### Key Note
**Division by 2a:** Make sure to multiply $2 \cdot a$ in the denominator before dividing! Use protective parentheses: $-b / (2a)$.

### Script
[Prof. Park] Welcome to Section 3.1! This formula $x = -\frac{b}{2a}$ is your superpower. It finds the exact turning point of any parabola in seconds.

[TA Sora] Once you have $x$, just plug it back into the function to get $y$!

---

## Slide 2: Section 3.1 Example 1: Finding Vertex for f(x) = x^2 + 6x - 8

**Subtitle:** Unit 3 • Lecture 34 • Section 3.1 Example 1 (Workbook p. 63)

### Problem
### Example 1 (Workbook p. 63)
For $\mathbf{f(x) = x^2 + 6x - 8}$:
- **A. Find the vertex:** __________________________
- **B. Find the $y$-intercept:** __________________________
- **C. Axis of Symmetry:** __________________________
- **D. Maximum or Minimum Value:** __________________________

### Solution
$$\begin{aligned}
\text{Identify: } & a = 1, \quad b = 6, \quad c = -8 \\[0.5em]
\mathbf{x_v} & = -\frac{b}{2a} = -\frac{6}{2(1)} = \mathbf{-3} \\[0.5em]
\mathbf{y_v} & = f(-3) = (-3)^2 + 6(-3) - 8 = 9 - 18 - 8 = \mathbf{-17} \\[0.8em]
\textbf{A. Vertex: } & \mathbf{(-3, -17)} \\
\textbf{B. y-intercept: } & \mathbf{(0, -8)} \quad (c = -8) \\
\textbf{C. Axis of Symmetry: } & \mathbf{x = -3} \\
\textbf{D. Minimum Value: } & \mathbf{-17} \quad (a = 1 > 0 \implies \text{opens up})
\end{aligned}$$

### Key Note
**Squaring negative 3:** $(-3)^2 = +9$. Then $9 - 18 = -9$, and $-9 - 8 = -17$!

### Script
[Prof. Park] In Example 1, $a = 1, b = 6$. So $x_v = -\frac{6}{2} = -3$. Plugging $-3$ in gives $y_v = -17$.

[TA Sora] The vertex is $(-3, -17)$. Since $a > 0$, the parabola opens up, making $-17$ a MINIMUM value!

---

## Slide 3: Section 3.1 Example 2: Fraction Leading Coefficient

**Subtitle:** Unit 3 • Lecture 34 • Section 3.1 Example 2 (Workbook p. 63)

### Problem
### Example 2 (Workbook p. 63)
For $\mathbf{f(x) = -\frac{1}{4}x^2 - 3x + 9}$:
- **A. Find the vertex:** __________________________
- **B. Find the $y$-intercept:** __________________________
- **C. Axis of Symmetry:** __________________________
- **D. Maximum or Minimum Value:** __________________________

### Solution
$$\begin{aligned}
\text{Identify: } & a = -\frac{1}{4}, \quad b = -3, \quad c = 9 \\[0.5em]
\mathbf{x_v} & = -\frac{b}{2a} = -\frac{-3}{2\left(-\frac{1}{4}\right)} = -\frac{-3}{-\frac{1}{2}} = -\left(3 \cdot 2\right) = \mathbf{-6} \\[0.8em]
\mathbf{y_v} & = f(-6) = -\frac{1}{4}(-6)^2 - 3(-6) + 9 \\
& = -\frac{1}{4}(36) + 18 + 9 = -9 + 18 + 9 = \mathbf{18} \\[0.8em]
\textbf{A. Vertex: } & \mathbf{(-6, 18)} \\
\textbf{B. y-intercept: } & \mathbf{(0, 9)} \\
\textbf{C. Axis of Symmetry: } & \mathbf{x = -6} \\
\textbf{D. Maximum Value: } & \mathbf{18} \quad (a < 0 \implies \text{opens down})
\end{aligned}$$

### Key Note
**Watch triple negatives:** In $x_v = -\frac{-3}{2(-1/4)}$, three minus signs equal a negative: $-6$!

### Script
[Prof. Park] In Example 2, the denominator is $2(-\frac{1}{4}) = -\frac{1}{2}$. Dividing $-3$ by $-\frac{1}{2}$ is $+6$, then negated gives $-6$.

[TA Sora] Then $f(-6) = -\frac{1}{4}(36) + 18 + 9 = 18$. The vertex is $(-6, 18)$ and it's a MAXIMUM value of 18!

---

## Slide 4: Why Does x = -b / (2a) Work? The Midpoint of Roots

**Subtitle:** Unit 3 • Lecture 34 • Section 3.1 Geometric Derivation

### Problem
### The Origin of the Vertex Formula
Recall the Quadratic Formula for finding roots:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \mathbf{-\frac{b}{2a}} \pm \frac{\sqrt{b^2 - 4ac}}{2a}$$
- Notice the central starting value: **$-\frac{b}{2a}$**!
- The two $x$-intercepts spread out symmetrically to the left and right by $\pm \frac{\sqrt{b^2 - 4ac}}{2a}$.
- Therefore, the exact middle (axis of symmetry) is always at **$x = -\frac{b}{2a}$**!

### Solution
$$\begin{aligned}
\text{Root 1: } & x_1 = -\frac{b}{2a} - \frac{\sqrt{D}}{2a} \\
\text{Root 2: } & x_2 = -\frac{b}{2a} + \frac{\sqrt{D}}{2a} \\[0.5em]
\text{Midpoint: } & \frac{x_1 + x_2}{2} = \frac{-2b / (2a)}{2} = \mathbf{-\frac{b}{2a}}
\end{aligned}$$

### Key Note
**Even when there are no real x-intercepts:** Even if a parabola never touches the $x$-axis, $-\frac{b}{2a}$ STILL gives the exact vertex!

### Script
[Prof. Park] Look at how beautifully mathematics connects. The vertex formula is simply the center point of the quadratic formula!

[TA Sora] That's why the axis of symmetry is always exactly in the middle of any two symmetric points!

---

## Slide 5: Sora's Protocol for Finding the Vertex & Max/Min

**Subtitle:** Unit 3 • Lecture 34 • Section 3.1 Protocol

### Problem
### Sora's 4-Step Vertex Checklist
1. **Identify $a, b, c$:** Make sure the equation is in standard descending order $ax^2 + bx + c$.
2. **Calculate $x_v$:** $x_v = -\frac{b}{2a}$. Write out $-b$ and $(2a)$ with parentheses.
3. **Calculate $y_v$:** Substitute $x_v$ back into the original function: $y_v = f(x_v)$.
4. **Classify Max vs Min:**
   - If $a > 0$: **Minimum value is $y_v$ at $x = x_v$.
   - If $a < 0$: **Maximum value is $y_v$ at $x = x_v$.

### Solution
$$\begin{array}{|c|c|} 
\hline
\textbf{Feature} & \textbf{How to Report} \\
\hline
\text{Vertex} & (x_v, y_v) \\
\hline
\text{Axis of Symmetry} & \mathbf{x = x_v} \; (\text{include 'x ='}) \\
\hline
\text{Max or Min Value} & y_v \; (\text{just the number}) \\
\hline
\text{Where it occurs} & \text{at } x = x_v \\
\hline
\end{array}$$

### Key Note
**Reporting Max/Min:** Exam question: 'Find the maximum value of $f(x)$'. Correct answer: $18$. Incorrect answer: $(-6, 18)$. The value is strictly the $y$-coordinate!

### Script
[Prof. Park] Sora's table will save you from common test pitfalls. Pay attention to how the question is phrased!

[TA Sora] 'Maximum value' means $y$. 'Where it occurs' means $x$!

---

## Slide 6: Check Your Understanding: Vertex of f(x) = -2x^2 + 8x - 3

**Subtitle:** Unit 3 • Lecture 34 • Section 3.1 Checkpoint

### Problem
### Checkpoint Practice
Find the vertex, axis of symmetry, and state whether it is a maximum or minimum for:
$$\mathbf{f(x) = -2x^2 + 8x - 3}$$

### Solution
$$\begin{aligned}
\text{Identify: } & a = -2, \quad b = 8, \quad c = -3 \\[0.5em]
x_v & = -\frac{8}{2(-2)} = -\frac{8}{-4} = \mathbf{2} \\[0.5em]
y_v & = f(2) = -2(2)^2 + 8(2) - 3 = -2(4) + 16 - 3 = -8 + 16 - 3 = \mathbf{5} \\[0.8em]
\mathbf{\text{Vertex: }} & \mathbf{(2, 5)} \\
\mathbf{\text{Axis of Symmetry: }} & \mathbf{x = 2} \\
\mathbf{\text{Maximum Value: }} & \mathbf{5} \quad (a = -2 < 0 \implies \text{opens down})
\end{aligned}$$

### Key Note
**Negative leading coefficient:** $-2(2)^2 = -2(4) = -8$. Don't make it $+8$!

### Script
[Prof. Park] In this checkpoint, $x_v = -\frac{8}{-4} = 2$. $f(2) = -8 + 16 - 3 = 5$.

[TA Sora] Vertex is $(2, 5)$, and the maximum value is 5 occurring at $x = 2$!

---

## Slide 7: Visualizing Vertex & Symmetry on the Grid

**Subtitle:** Unit 3 • Lecture 34 • Section 3.1 Visual Analysis

### Problem
### The Mirror Property of Parabolas
Every point on a parabola has a reflection across the axis of symmetry $x = h$:
- Point $(0, -3)$ is $2$ units left of $x = 2$.
- Its reflection is $(4, -3)$, exactly $2$ units right of $x = 2$!
Verify: $f(4) = -2(4)^2 + 8(4) - 3 = -32 + 32 - 3 = -3$.

### Solution
$$\begin{aligned}
\text{Left Point: } & (0, -3) \quad [\text{distance to } x=2 \text{ is } 2] \\
\text{Right Point: } & (4, -3) \quad [\text{distance to } x=2 \text{ is } 2] \\[0.5em]
\text{Symmetric Heights: } & f(0) = f(4) = -3
\end{aligned}$$

### Key Note
**Use symmetry to graph quickly:** If you know the $y$-intercept $(0, c)$, reflect it across the axis of symmetry to instantly get a free second point!

### Script
[Prof. Park] Notice how $(0, -3)$ and $(4, -3)$ sit at the exact same height on opposite sides of the gold axis of symmetry line.

[TA Sora] Parabolas are perfectly bilateral! This mirror symmetry makes graphing fast and accurate.

---

## Slide 8: Section 3.1 Part 1 Mastery Summary

**Subtitle:** Unit 3 • Lecture 34 • Section 3.1 Wrap-up

### Problem
### Section 3.1 Part 1 Master Summary
- **Formula:** $x_v = -\frac{b}{2a}$, $y_v = f(x_v)$.
- **Axis of Symmetry:** $x = x_v$.
- **$y$-intercept:** $(0, c)$.
- **Optimization:** If $a > 0$, vertex is minimum; if $a < 0$, vertex is maximum.

### Solution
$$\mathbf{\text{Lecture 34 Complete! Next Up: Lecture 35 — Vertex from Vertex Form } a(x-h)^2 + k!}$$

### Key Note
**Double check signs:** A sign error in $x = -b/(2a)$ ruins both the vertex and axis of symmetry!

### Script
[Prof. Park] Great job! In Lecture 35, we examine how Vertex Form lets us read the vertex without doing any calculation at all!

---

