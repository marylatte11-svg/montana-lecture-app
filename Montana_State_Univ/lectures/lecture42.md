# Lecture 42 - 8 slides

## Slide 1: Section 3.5 Part 2: The Discriminant

**Subtitle:** Unit 3 • Lecture 42 • Section 3.5 (Workbook p. 79–82)

### Problem
**The Discriminant** is the expression inside the square root of the Quadratic Formula:

$$\Delta = b^2 - 4ac$$

**It tells us the number of x-intercepts WITHOUT solving:**

| Discriminant | Solutions | Graph |
|---|---|---|
| \(\Delta > 0\) | 2 real x-intercepts | Crosses x-axis twice |
| \(\Delta = 0\) | 1 real x-intercept | Touches x-axis at vertex |
| \(\Delta < 0\) | No real x-intercepts | Parabola floats above or below x-axis |

### Solution
**Why does this matter?**
- Saves time! If \(\Delta < 0\), you know immediately there are no real x-intercepts.
- Tells you the shape of your parabola’s relationship with the x-axis.
- Discriminant zero means vertex is ON the x-axis (special case!).

### Key Note
**Sora’s Warning:** The discriminant is \(b^2 - 4ac\), NOT \(\sqrt{b^2-4ac}\). Compute it BEFORE taking the square root.

### Script
[Prof. Park] Welcome to Lecture 42! Today we study the discriminant, the gatekeeper of quadratic solutions.

[TA Sora] I love this concept because just computing b²-4ac tells you everything about how many answers you’ll get. It’s like a spoiler for the answer!

[Prof. Park] Exactly, Sora. Three outcomes: cross twice, touch once, or miss entirely.

---

## Slide 2: Discriminant \(\Delta > 0\): Two Real x-Intercepts

**Subtitle:** Unit 3 • Lecture 42 • Discriminant Case 1

### Problem
**Find and classify solutions for:** \(f(x) = x^2 - 5x + 4\)

**Step 1 — Compute discriminant:** \(a=1, b=-5, c=4\)
$$\Delta = (-5)^2 - 4(1)(4) = 25 - 16 = 9 > 0$$

**Conclusion:** The parabola crosses the x-axis at **2 distinct points**.

### Solution
**Apply the formula:**
$$x = \dfrac{5 \pm \sqrt{9}}{2} = \dfrac{5 \pm 3}{2}$$

$$x = \dfrac{5+3}{2} = 4 \qquad x = \dfrac{5-3}{2} = 1$$

**x-intercepts:** \((1,\,0)\) and \((4,\,0)\)

**Vertex:** \(x = 2.5\), \(f(2.5) = 6.25-12.5+4 = -2.25\)

**Vertex:** \((2.5,\,-2.25)\)

### Key Note
**Sora’s Note:** \(\sqrt{9} = 3\) (a perfect square!). When \(\Delta\) is a perfect square, solutions are rational numbers.

### Script
[Prof. Park] When delta equals 9, a perfect square, we get the cleanest possible answer: two rational roots.

[TA Sora] x=1 and x=4. The parabola clearly crosses the x-axis at both points. I can see it on the graph!

---

## Slide 3: Discriminant \(\Delta = 0\): Exactly One Real x-Intercept

**Subtitle:** Unit 3 • Lecture 42 • Discriminant Case 2

### Problem
**Find and classify solutions for:** \(f(x) = x^2 - 6x + 9\)

**Step 1 — Compute discriminant:** \(a=1, b=-6, c=9\)
$$\Delta = (-6)^2 - 4(1)(9) = 36 - 36 = 0$$

**Conclusion:** The parabola **touches** the x-axis at exactly **one point** (the vertex).

### Solution
**Apply the formula:**
$$x = \dfrac{6 \pm \sqrt{0}}{2} = \dfrac{6 \pm 0}{2} = \dfrac{6}{2} = 3$$

**One x-intercept:** \((3,\,0)\)

**Vertex = x-intercept:** \((3,\,0)\)

**Note:** \(f(x) = x^2-6x+9 = (x-3)^2\). The vertex form confirms vertex is at \((3,0)\), sitting ON the x-axis.

### Key Note
**Sora’s Insight:** \(\Delta = 0\) means it’s a perfect square trinomial! \(x^2-6x+9 = (x-3)^2\). So the answer is a double root: \(x=3\) repeated twice.

### Script
[TA Sora] When the discriminant is exactly zero, there’s only one solution. The parabola just barely touches the x-axis at its lowest point.

[Prof. Park] This is called a double root or a repeated root. x=3 is the answer, and visually the parabola is tangent to the x-axis.

---

## Slide 4: Discriminant \(\Delta < 0\): No Real x-Intercepts

**Subtitle:** Unit 3 • Lecture 42 • Discriminant Case 3

### Problem
**Find and classify solutions for:** \(f(x) = x^2 + 2x + 5\)

**Step 1 — Compute discriminant:** \(a=1, b=2, c=5\)
$$\Delta = (2)^2 - 4(1)(5) = 4 - 20 = -16 < 0$$

**Conclusion:** There are **no real x-intercepts**. The parabola floats entirely above the x-axis.

### Solution
**Why no real solutions?**
$$x = \dfrac{-2 \pm \sqrt{-16}}{2}$$

$$\sqrt{-16} \text{ is not a real number!}$$

We cannot take the square root of a negative number in the real number system.

**Vertex:** \(x = \dfrac{-2}{2} = -1\), \(f(-1) = 1-2+5 = 4\)

**Vertex:** \((-1,\,4)\) — The parabola opens upward with minimum at \(y=4 > 0\). Never crosses the x-axis!

### Key Note
**Sora’s Note:** You will encounter imaginary numbers (\(\sqrt{-16} = 4i\)) in future math courses. For M090, we just state: NO REAL SOLUTIONS.

### Script
[Prof. Park] When the discriminant is negative, the square root doesn’t exist in real numbers. The parabola simply floats above the x-axis entirely.

[TA Sora] I can see on the graph that the vertex is at y=4, which is above the x-axis. So the parabola never crosses it. That makes perfect sense!

---

## Slide 5: Classify Without Solving: \(h(x) = -2x^2 + 3x - 5\)

**Subtitle:** Unit 3 • Lecture 42 • Discriminant Application

### Problem
**Without fully solving, determine the number of x-intercepts for:**
$$h(x) = -2x^2 + 3x - 5$$

Identify: \(a = -2,\; b = 3,\; c = -5\)

Compute the discriminant:
$$\Delta = b^2 - 4ac = (3)^2 - 4(-2)(-5)$$

### Solution
$$\Delta = 9 - 40 = -31 < 0$$

**Conclusion: No real x-intercepts.**

The parabola opens **downward** (a=-2<0) and sits entirely **below** the x-axis.

**Vertex:** \(x = \dfrac{-3}{2(-2)} = \dfrac{3}{4} = 0.75\)
$$h(0.75) = -2(0.5625)+3(0.75)-5 = -1.125+2.25-5 = -3.875$$

**Vertex:** \((0.75,\,-3.875)\) — Maximum is negative, parabola entirely below x-axis.

### Key Note
**Sora’s Check:** \(-4(-2)(-5) = -4 \times 10 = -40\). Two negatives in a=-2 and c=-5 give a negative product! Don’t accidentally make it positive.

### Script
[TA Sora] Wait, a is negative AND c is negative. So -4ac = -4(-2)(-5). Let me compute: negative four times negative two is positive eight, times negative five is negative forty!

[Prof. Park] Precisely! So delta = 9-40 = -31. Negative discriminant. No real x-intercepts confirmed.

---

## Slide 6: Function Evaluation: \( f(x) = 3x^2 - 5x + 7 \) (Parts A & B)

**Subtitle:** Unit 3 • Lecture 42 • Section 3.5 Example 2 (Workbook p. 82)

### Problem
**Use \(f(x) = 3x^2 - 5x + 7\) to find:**

**A.** \(f(4)\)

**B.** \(f(p)\)

**Recall:** To evaluate \(f(\text{input})\), replace every \(x\) in the formula with the input.

### Solution
**A.** \(f(4)\): Replace \(x\) with \(4\)
$$f(4) = 3(4)^2 - 5(4) + 7 = 3(16) - 20 + 7 = 48 - 20 + 7 = \mathbf{35}$$

**B.** \(f(p)\): Replace \(x\) with \(p\)
$$f(p) = 3p^2 - 5p + 7$$

This stays as an **algebraic expression** — we substitute the variable \(p\) directly.

### Key Note
**Sora’s Note on Part B:** When the input is a variable (like \(p\)), the output is a new expression, not a number. Just replace every \(x\) with \(p\)!

### Script
[Prof. Park] Example 2A gives a numeric answer. Example 2B gives an algebraic expression. Both are valid evaluations of function notation.

[TA Sora] So f of 4 equals 35 (a number), but f of p equals 3p²-5p+7 (still an expression). Got it!

---

## Slide 7: Function Composition & Solving: \( f(x) = 3x^2 - 5x + 7 \) (Parts C & D)

**Subtitle:** Unit 3 • Lecture 42 • Section 3.5 Example 2 (Workbook p. 82)

### Problem
**Use \(f(x) = 3x^2 - 5x + 7\) to find:**

**C.** \(f(x+3)\)

**D.** Solve \(f(x) = 13\) for \(x\)

### Solution
**C.** \(f(x+3)\): Replace every \(x\) with \((x+3)\)
$$f(x+3) = 3(x+3)^2 - 5(x+3) + 7$$
$$= 3(x^2+6x+9) - 5x - 15 + 7$$
$$= 3x^2 + 18x + 27 - 5x - 8$$
$$= \mathbf{3x^2 + 13x + 19}$$

**D.** Set \(f(x) = 13\):
$$3x^2 - 5x + 7 = 13$$
$$3x^2 - 5x - 6 = 0$$
$$x = \dfrac{5 \pm \sqrt{25+72}}{6} = \dfrac{5 \pm \sqrt{97}}{6} \approx \dfrac{5 \pm 9.85}{6}$$
$$x \approx \mathbf{2.47} \quad \text{or} \quad x \approx \mathbf{-0.81}$$

### Key Note
**Sora’s FOIL Reminder for Part C:** \((x+3)^2 = x^2+6x+9\), NOT \(x^2+9\)! Always expand fully.

### Script
[TA Sora] Part C is so interesting! We’re substituting an expression x+3 instead of a number. We just replace every x with the whole thing in parentheses.

[Prof. Park] And Part D requires moving 13 to the left to get standard form equal to zero, then the Quadratic Formula gives two solutions.

---

## Slide 8: Discriminant Summary — Three Cases Visualized

**Subtitle:** Unit 3 • Lecture 42 Summary

### Problem
**Discriminant Decision Chart:**

| Compute \(\Delta = b^2-4ac\) | Result | Parabola |
|---|---|---|
| \(\Delta > 0\) | **2** real solutions | Crosses x-axis at 2 points |
| \(\Delta = 0\) | **1** real solution | Vertex touches x-axis |
| \(\Delta < 0\) | **0** real solutions | No x-intercepts exist |

**Remember:** This works for ANY quadratic, regardless of the value of \(a\)!

### Solution
**Lecture 42 examples covered:**
- \(f(x)=x^2-5x+4\): \(\Delta=9>0\) → \(x=1,4\)
- \(f(x)=x^2-6x+9\): \(\Delta=0\) → \(x=3\) (double root)
- \(f(x)=x^2+2x+5\): \(\Delta=-16<0\) → No real solutions
- \(h(x)=-2x^2+3x-5\): \(\Delta=-31<0\) → No real solutions

**Next Lecture:** Master decision strategy — which method to use and when!

### Key Note
**Sora’s Final Tip:** Before solving ANY quadratic, compute the discriminant first. It tells you what to expect and saves time if there are no real solutions.

### Script
[TA Sora] Three cases, perfectly memorized!

[Prof. Park] In Lecture 43, we bring everything together: Square Root Property, Factoring, Completing the Square, and the Quadratic Formula. You’ll learn exactly when to use each method.

---

