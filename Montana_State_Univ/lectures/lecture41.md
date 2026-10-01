# Lecture 41 - 8 slides

## Slide 1: Section 3.5: The Quadratic Formula

**Subtitle:** Unit 3 • Lecture 41 • Section 3.5 (Workbook p. 79)

### Problem
**The Quadratic Formula** can solve ANY quadratic equation once it is set equal to zero in general form.

$$\text{If } ax^2 + bx + c = 0 \text{ then:}$$

$$\boxed{x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}}$$

**Why do we need this?**
- Square Root Property works when there is no middle \(bx\) term.
- Factoring works when nice integer roots exist.
- The **Quadratic Formula** always works, no matter what!

### Solution
**Formula Components:**
- \(a\) = leading coefficient
- \(b\) = middle coefficient
- \(c\) = constant term
- \(b^2 - 4ac\) = **discriminant** (determines the number of solutions)

**Three possible outcomes:**
$$b^2 - 4ac > 0 \Rightarrow \text{2 real x-intercepts}$$
$$b^2 - 4ac = 0 \Rightarrow \text{1 real x-intercept (vertex on x-axis)}$$
$$b^2 - 4ac < 0 \Rightarrow \text{No real x-intercepts (parabola doesn’t cross x-axis)}$$

### Key Note
**Sora’s Warning:** The \(\pm\) sign means you compute TWO values: one with \(+\) and one with \(-\). Never skip one!

### Script
[Prof. Park] Welcome to Lecture 41! We’ve mastered the Square Root Property and Factoring. Today we unlock the most powerful tool of all: the Quadratic Formula.

[TA Sora] I remember when I first saw this formula I thought it looked scary. But honestly, it’s just a recipe—plug in a, b, and c, and out come the x-intercepts!

[Prof. Park] Exactly. And unlike factoring, this formula ALWAYS works. Let’s see it in action.

---

## Slide 2: Quadratic Formula: \( g(x) = x^2 - 17x + 72 \)

**Subtitle:** Unit 3 • Lecture 41 • Section 3.5 Example 1A (Workbook p. 79)

### Problem
**Find the intercepts and vertex for:** \(g(x) = x^2 - 17x + 72\)

**Step 1 — Identify x-intercepts:** Set \(g(x) = 0\)
$$x^2 - 17x + 72 = 0$$

Identify: \(a = 1,\; b = -17,\; c = 72\)

Apply the Quadratic Formula:
$$x = \dfrac{-(-17) \pm \sqrt{(-17)^2 - 4(1)(72)}}{2(1)}$$

### Solution
$$x = \dfrac{17 \pm \sqrt{289 - 288}}{2} = \dfrac{17 \pm \sqrt{1}}{2} = \dfrac{17 \pm 1}{2}$$

$$x = \dfrac{17+1}{2} = \dfrac{18}{2} = \mathbf{9} \qquad x = \dfrac{17-1}{2} = \dfrac{16}{2} = \mathbf{8}$$

**x-intercepts:** \((9,0)\) and \((8,0)\)

**y-intercept:** \(g(0) = 0 - 0 + 72 = \mathbf{72}\) → \((0, 72)\)

**Vertex:** \(x = \dfrac{-(-17)}{2(1)} = \dfrac{17}{2} = 8.5\)
$$g(8.5) = (8.5)^2 - 17(8.5) + 72 = 72.25 - 144.5 + 72 = -0.25$$

**Vertex:** \((8.5,\; -0.25)\)

### Key Note
**Sora’s Note:** \(\sqrt{1} = 1\), not 0! The discriminant being 1 (very close to 0) means the two roots are almost equal but still distinct: \(x = 8\) and \(x = 9\).

### Script
[Prof. Park] Example 1A has a=1, b=-17, c=72. Let’s plug in carefully.

[TA Sora] The discriminant is 289 minus 288 which equals 1. So we get two roots very close together, x=8 and x=9!

[Prof. Park] Perfect. The parabola barely dips below the x-axis between x=8 and x=9 before going back up.

---

## Slide 3: Quadratic Formula: \( h(x) = x^2 - 5x - 7 \)

**Subtitle:** Unit 3 • Lecture 41 • Section 3.5 Example 1B (Workbook p. 80)

### Problem
**Find the intercepts and vertex for:** \(h(x) = x^2 - 5x - 7\)

Set \(h(x) = 0\): \(x^2 - 5x - 7 = 0\)

Identify: \(a = 1,\; b = -5,\; c = -7\)

$$x = \dfrac{-(-5) \pm \sqrt{(-5)^2 - 4(1)(-7)}}{2(1)} = \dfrac{5 \pm \sqrt{25 + 28}}{2}$$

### Solution
$$x = \dfrac{5 \pm \sqrt{53}}{2}$$

$$\sqrt{53} \approx 7.28$$

$$x = \dfrac{5 + 7.28}{2} = \dfrac{12.28}{2} \approx \mathbf{6.14} \qquad x = \dfrac{5 - 7.28}{2} = \dfrac{-2.28}{2} \approx \mathbf{-1.14}$$

**x-intercepts:** \(\approx (6.14,\,0)\) and \(\approx (-1.14,\,0)\)

**y-intercept:** \(h(0) = -7\) → \((0,\,-7)\)

**Vertex:** \(x = \dfrac{5}{2} = 2.5\),\quad \(h(2.5) = 6.25 - 12.5 - 7 = -13.25\)

**Vertex:** \((2.5,\,-13.25)\)

### Key Note
**Sora’s Note:** When \(c\) is negative, \(-4ac\) becomes positive (negative times negative). Always double-check: \(-4(1)(-7) = +28\).

### Script
[Prof. Park] In Example 1B, c is -7 which makes the discriminant larger: 25+28=53. A positive discriminant means two real roots.

[TA Sora] And since 53 is not a perfect square, our answers are irrational. We leave them as fractions with the radical or use a decimal approximation.

[Prof. Park] Great observation, Sora. Both forms are correct, but irrational exact form is preferred in math.

---

## Slide 4: Quadratic Formula: \( h(x) = 13x - x^2 + 1 \)

**Subtitle:** Unit 3 • Lecture 41 • Section 3.5 Example 1C (Workbook p. 80)

### Problem
**Find the intercepts and vertex for:** \(h(x) = 13x - x^2 + 1\)

**Step 1 — Rewrite in standard form** \(ax^2 + bx + c\):
$$h(x) = -x^2 + 13x + 1$$

Set \(h(x) = 0\): \(-x^2 + 13x + 1 = 0\)

Identify: \(a = -1,\; b = 13,\; c = 1\)

$$x = \dfrac{-13 \pm \sqrt{13^2 - 4(-1)(1)}}{2(-1)} = \dfrac{-13 \pm \sqrt{169+4}}{-2}$$

### Solution
$$x = \dfrac{-13 \pm \sqrt{173}}{-2}$$

$$\sqrt{173} \approx 13.15$$

$$x = \dfrac{-13 + 13.15}{-2} = \dfrac{0.15}{-2} \approx \mathbf{-0.08}$$

$$x = \dfrac{-13 - 13.15}{-2} = \dfrac{-26.15}{-2} \approx \mathbf{13.08}$$

**x-intercepts:** \(\approx (-0.08,\,0)\) and \(\approx (13.08,\,0)\)

**y-intercept:** \(h(0) = 1\) → \((0,\,1)\)

**Vertex:** \(x = \dfrac{-13}{2(-1)} = \dfrac{13}{2} = 6.5\)
$$h(6.5) = -(6.5)^2 + 13(6.5) + 1 = -42.25 + 84.5 + 1 = 43.25$$

**Vertex:** \((6.5,\;43.25)\)

### Key Note
**Sora’s Warning:** Always rearrange to \(ax^2 + bx + c = 0\) FIRST! And with \(a = -1\), remember dividing by \(-2\) flips sign.

### Script
[Prof. Park] Example 1C is written out of standard order: 13x minus x squared plus 1. Our first job is to reorder it.

[TA Sora] So we get -x²+13x+1. Now a=-1. That means the parabola opens downward, and the vertex is at the TOP!

[Prof. Park] Exactly. The parabola opens down with a maximum at (6.5, 43.25).

---

## Slide 5: Quadratic Formula: \( f(x) = -x^2 - 5x + 7 \)

**Subtitle:** Unit 3 • Lecture 41 • Section 3.5 Example 1D (Workbook p. 81)

### Problem
**Find the intercepts and vertex for:** \(f(x) = -x^2 - 5x + 7\)

Set \(f(x) = 0\): \(-x^2 - 5x + 7 = 0\)

Identify: \(a = -1,\; b = -5,\; c = 7\)

$$x = \dfrac{-(-5) \pm \sqrt{(-5)^2 - 4(-1)(7)}}{2(-1)} = \dfrac{5 \pm \sqrt{25 + 28}}{-2}$$

### Solution
$$x = \dfrac{5 \pm \sqrt{53}}{-2}$$

$$\sqrt{53} \approx 7.28$$

$$x = \dfrac{5 + 7.28}{-2} = \dfrac{12.28}{-2} \approx \mathbf{-6.14}$$

$$x = \dfrac{5 - 7.28}{-2} = \dfrac{-2.28}{-2} \approx \mathbf{1.14}$$

**x-intercepts:** \(\approx (-6.14,\,0)\) and \(\approx (1.14,\,0)\)

**y-intercept:** \(f(0) = 7\) → \((0,\,7)\)

**Vertex:** \(x = \dfrac{-(-5)}{2(-1)} = \dfrac{5}{-2} = -2.5\)
$$f(-2.5) = -(-2.5)^2 - 5(-2.5) + 7 = -6.25 + 12.5 + 7 = 13.25$$

**Vertex:** \((-2.5,\;13.25)\)

### Key Note
**Sora’s Note:** Two negatives in a=-1, b=-5. Be extra careful. \(-b = -(-5) = +5\) and \(-4(-1)(7) = +28\).

### Script
[Prof. Park] Example 1D has two negative signs for a and b. These are the problems where students make sign errors.

[TA Sora] I always write out every step slowly when I see negative a. It’s so easy to flip the wrong sign!

[Prof. Park] Wise advice, Sora. Slow down, write every step, and check your signs twice.

---

## Slide 6: Quadratic Formula: \( f(x) = -1 + 2x^2 - 3x \)

**Subtitle:** Unit 3 • Lecture 41 • Section 3.5 Example 1E (Workbook p. 81)

### Problem
**Find the intercepts and vertex for:** \(f(x) = -1 + 2x^2 - 3x\)

**Step 1 — Rewrite in standard form:**
$$f(x) = 2x^2 - 3x - 1$$

Set \(f(x) = 0\): \(2x^2 - 3x - 1 = 0\)

Identify: \(a = 2,\; b = -3,\; c = -1\)

$$x = \dfrac{-(-3) \pm \sqrt{(-3)^2 - 4(2)(-1)}}{2(2)} = \dfrac{3 \pm \sqrt{9 + 8}}{4}$$

### Solution
$$x = \dfrac{3 \pm \sqrt{17}}{4}$$

$$\sqrt{17} \approx 4.12$$

$$x = \dfrac{3 + 4.12}{4} = \dfrac{7.12}{4} \approx \mathbf{1.78}$$

$$x = \dfrac{3 - 4.12}{4} = \dfrac{-1.12}{4} \approx \mathbf{-0.28}$$

**x-intercepts:** \(\approx (1.78,\,0)\) and \(\approx (-0.28,\,0)\)

**y-intercept:** \(f(0) = -1\) → \((0,\,-1)\)

**Vertex:** \(x = \dfrac{-(-3)}{2(2)} = \dfrac{3}{4} = 0.75\)
$$f(0.75) = 2(0.75)^2 - 3(0.75) - 1 = 1.125 - 2.25 - 1 = -2.125$$

**Vertex:** \((0.75,\;-2.125)\)

### Key Note
**Sora’s Tip:** \(-4(2)(-1) = +8\). Two negatives make a positive! The discriminant 9+8=17 is positive, so two real roots exist.

### Script
[Prof. Park] Our last example in Section 3.5 Part 1 has a=2. Notice how 2a=4 appears in the denominator.

[TA Sora] And the terms are written out of order! I had to rearrange to 2x²-3x-1 to see a, b, and c clearly.

[Prof. Park] Always rewrite first. Standard form ax²+bx+c is essential before applying any formula.

---

## Slide 7: Function Evaluation: \( f(x) = 3x^2 - 5x + 7 \)

**Subtitle:** Unit 3 • Lecture 41 • Section 3.5 Example 2 (Workbook p. 82)

### Problem
**Use \(f(x) = 3x^2 - 5x + 7\) to find:**

**A.** \(f(4)\)

**B.** \(f(p)\)

**C.** \(f(x+3)\)

**D.** Solve \(f(x) = 13\) for \(x\)

### Solution
**A.** \(f(4) = 3(4)^2 - 5(4) + 7 = 48 - 20 + 7 = \mathbf{35}\)

**B.** \(f(p) = 3p^2 - 5p + 7\)

**C.** \(f(x+3) = 3(x+3)^2 - 5(x+3) + 7\)
$$= 3(x^2+6x+9) - 5x - 15 + 7 = 3x^2+18x+27-5x-15+7$$
$$= \mathbf{3x^2 + 13x + 19}$$

**D.** Set \(f(x) = 13\):
$$3x^2 - 5x + 7 = 13 \Rightarrow 3x^2 - 5x - 6 = 0$$
$$x = \dfrac{5 \pm \sqrt{25+72}}{6} = \dfrac{5 \pm \sqrt{97}}{6} \approx \dfrac{5 \pm 9.85}{6}$$
$$x \approx \mathbf{2.47} \quad \text{or} \quad x \approx \mathbf{-0.81}$$

### Key Note
**Sora’s Note for Part C:** Use FOIL or the perfect-square pattern for \((x+3)^2 = x^2 + 6x + 9\). Then distribute the 3!

### Script
[Prof. Park] Section 3.5 Example 2 tests ALL our function notation skills together. Evaluation, expression substitution, and solving.

[TA Sora] Part D is so interesting! We set f(x) equal to 13, move 13 to the left, and then we HAVE to use the Quadratic Formula because the result doesn’t factor nicely.

[Prof. Park] Perfect connection, Sora. The Quadratic Formula saves us when factoring fails.

---

## Slide 8: Quadratic Formula — Key Takeaways

**Subtitle:** Unit 3 • Lecture 41 Summary

### Problem
**Quadratic Formula Summary:**

| Step | Action |
|------|--------|
| 1 | Write in standard form: \(ax^2+bx+c=0\) |
| 2 | Identify \(a\), \(b\), \(c\) |
| 3 | Compute discriminant: \(b^2 - 4ac\) |
| 4 | Apply: \(x = \dfrac{-b \pm \sqrt{b^2-4ac}}{2a}\) |
| 5 | Simplify both \(+\) and \(-\) solutions |

### Solution
**Examples covered today:**
- \(g(x) = x^2-17x+72\) → \(x = 8, 9\)
- \(h(x) = x^2-5x-7\) → \(x \approx 6.14,\,-1.14\)
- \(h(x) = 13x-x^2+1\) → \(x \approx -0.08,\,13.08\)
- \(f(x) = -x^2-5x+7\) → \(x \approx -6.14,\,1.14\)
- \(f(x) = -1+2x^2-3x\) → \(x \approx 1.78,\,-0.28\)

**Next Lecture:** The Discriminant — predicting solutions before solving!

### Key Note
**Sora’s Final Reminder:** Always check that your equation equals ZERO before applying the Quadratic Formula. If it equals a non-zero constant, move it first!

### Script
[TA Sora] Five examples in one lecture! You’re all Quadratic Formula champions now!

[Prof. Park] In Lecture 42 we’ll study the discriminant, which lets us predict how many solutions exist WITHOUT fully solving the equation. See you then!

---

