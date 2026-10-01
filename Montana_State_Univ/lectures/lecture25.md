# Montana State University - Gallatin College
## M090 Introductory Algebra — Lecture 25
**Instructors:** Prof. Eunju Park & TA Sora (Gallatin College MSU)
**Workbook Source:** M090 Full Student Workbook

---

### [Slide 1] The Formal Definition of a Function
*Unit 2 • Lecture 25 • Section 2.4 (Workbook p. 46)*

#### 📖 Official Workbook Problem
### Definition: What is a Function? (Workbook p. 46)
A **function** is a relation that assigns **each element in its domain to exactly one element in its range**.
- **Crucial Rule:** One input value cannot correspond to two different output values!
- **Allowed:** Multiple different inputs can produce the same output value (e.g. $2^2 = 4$ and $(-2)^2 = 4$).
- **Forbidden:** A single input cannot split into two different outputs!

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Function: } & \text{Every } x \text{ has ONE AND ONLY ONE } y. \\
\text{NOT a function: } & \text{An } x \text{ gives two or more different } y\text{'s}.
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**One-to-many is NOT allowed:** Think of a person's birthday: one person can only have ONE birthday (function). But two different people can share the same birthday (allowed)!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Welcome to Lecture 25! A function is predictable: give it an input $x$, and it returns exactly one output $y$.

[TA Sora] If an input gives you multiple different answers, it's not a function!

---

### [Slide 2] Section 2.4 Example 3: Testing Example 1 for Function Status
*Unit 2 • Lecture 25 • Section 2.4 Example 3 (Workbook p. 46)*

#### 📖 Official Workbook Problem
### Example 3 (Workbook p. 46)
Based off the definition of a function, determine if Example 1 is a function:
$$\mathbf{\{(1, -1), (2, 5), (3, 10), (4, 16), (2, -3)\}}$$

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Examine input } x = 2: & \\
& 2 \implies 5 \quad \text{from } (2, 5) \\
& 2 \implies -3 \quad \text{from } (2, -3) \\[0.8em]
\text{Analysis: } & \text{The input } x = 2 \text{ is assigned to TWO different outputs: } 5 \text{ and } -3. \\[0.8em]
\mathbf{\text{Conclusion: }} & \mathbf{\text{NOT A FUNCTION.}}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Look for repeated x-values:** In a set of ordered pairs, if any $x$-value repeats with a different $y$-value, it immediately FAILS to be a function!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] In Example 3, input $x=2$ pairs with 5 and with $-3$.

[TA Sora] That violates the rule of a function! Therefore, Example 1 is NOT a function.

---

### [Slide 3] The Vertical Line Test (VLT)
*Unit 2 • Lecture 25 • Section 2.4 (Workbook p. 46)*

#### 📖 Official Workbook Problem
### The Vertical Line Test (Workbook p. 46)
A set of points in a rectangular coordinate system is the **graph of a function** if **every vertical line intersects the graph in at most one point**.
- If **any** vertical line intersects the graph in **more than one point**, the graph **does not represent a function**.
- Why? Because intersecting twice means that single $x$-value has two different $y$-values!

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{At most 1 intersection everywhere} & \implies \mathbf{\text{IS A FUNCTION}} \\
\text{2 or more intersections anywhere} & \implies \mathbf{\text{NOT A FUNCTION}}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**It only takes ONE failure:** Even if 99% of vertical lines hit once, if a SINGLE vertical line hits twice, the entire graph is NOT a function!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] The Vertical Line Test is the visual equivalent of the function definition.

[TA Sora] Imagine scanning a vertical ruler across the screen from left to right. If the curve touches the ruler twice at any moment, it fails!

---

### [Slide 4] Section 2.4 Example 4A: Parabola y = x^2 - 2 (Passes VLT)
*Unit 2 • Lecture 25 • Section 2.4 Example 4A (Workbook p. 46)*

#### 📖 Official Workbook Problem
### Example 4A (Workbook p. 46)
Determine if the parabola $y = x^2 - 2$ represents a function:
- Apply the Vertical Line Test.
- State whether it is a function.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Vertical Line Test: } & \text{Any vertical line } x = c \text{ intersects the parabola } \mathbf{\text{at exactly ONE point}}. \\[0.8em]
\mathbf{\text{Conclusion: }} & \mathbf{\text{YES, it is a FUNCTION.}}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**U-shape is fine:** It's okay that $(-2, 2)$ and $(2, 2)$ share the same $y$-height. That is a horizontal test, not a vertical test!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Look at the parabola on your screen. Any vertical line hits it in at most one point.

[TA Sora] It passes the Vertical Line Test with flying colors! Parabolas opening upward are functions.

---

### [Slide 5] Section 2.4 Example 4B: Circle x^2 + y^2 = 16 (Fails VLT)
*Unit 2 • Lecture 25 • Section 2.4 Example 4B (Workbook p. 46)*

#### 📖 Official Workbook Problem
### Example 4B (Workbook p. 46)
Determine if the circle $x^2 + y^2 = 16$ represents a function:
- Apply the Vertical Line Test.
- Identify a specific vertical line that intersects the circle more than once.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Test line } x = 0: & 0^2 + y^2 = 16 \implies y^2 = 16 \implies y = \pm 4 \\[0.5em]
\text{Intersections: } & \mathbf{(0, 4) \quad \text{and} \quad (0, -4)} \\[0.8em]
\text{Vertical Line Test: } & \text{The vertical line } x = 0 \text{ intersects the circle in } \mathbf{\text{TWO points}}! \\[0.8em]
\mathbf{\text{Conclusion: }} & \mathbf{\text{NOT A FUNCTION.}}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Circles, ellipses, and sideways parabolas are NOT functions:** Any closed loop curve fails the vertical line test!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] In Example 4B, the red dashed line $x = 0$ cuts right through the circle, hitting $(0, 4)$ at the top and $(0, -4)$ at the bottom!

[TA Sora] Two outputs for a single input $x = 0$. Circles fail the VLT and are NOT functions!

---

### [Slide 6] Section 2.4 Example 4C: Non-Vertical Line y = 2x - 1 (Passes VLT)
*Unit 2 • Lecture 25 • Section 2.4 Example 4C (Workbook p. 46)*

#### 📖 Official Workbook Problem
### Example 4C (Workbook p. 46)
Determine if the linear equation $y = 2x - 1$ represents a function:
- Apply the Vertical Line Test.
- State whether all non-vertical lines are functions.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Vertical Line Test: } & \text{Every vertical line intersects } y = 2x - 1 \text{ exactly ONCE.} \\[0.8em]
\mathbf{\text{Conclusion: }} & \mathbf{\text{YES, it is a FUNCTION.}} \\[0.5em]
\text{Universal Rule: } & \mathbf{\text{ALL non-vertical lines are linear functions!}}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Horizontal lines are functions:** A horizontal line $y = 3$ passes the VLT (every vertical line hits it once). But a vertical line $x = 3$ fails completely!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] All non-vertical straight lines pass the VLT everywhere.

[TA Sora] Every non-vertical line is a linear function!

---

### [Slide 7] Section 2.4 Example 4D: Vertical Line x = 3 (Fails VLT Infinitely)
*Unit 2 • Lecture 25 • Section 2.4 Example 4D (Workbook p. 46)*

#### 📖 Official Workbook Problem
### Example 4D (Workbook p. 46)
Determine if the vertical line $x = 3$ represents a function:
- Apply the Vertical Line Test at $x = 3$.
- How many times does the vertical line $x = 3$ intersect itself?

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Test line at } x = 3: & \text{The test line lies directly ON TOP of } x = 3! \\[0.5em]
\text{Intersections: } & \mathbf{\text{INFINITELY MANY intersection points!}} \\[0.8em]
\mathbf{\text{Conclusion: }} & \mathbf{\text{NOT A FUNCTION.}}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Vertical lines are NEVER functions:** A vertical line has an input of 3 with every conceivable $y$-value simultaneously!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] In Example 4D, $x = 3$ fails the Vertical Line Test in the most catastrophic way possible: infinitely many intersections!

[TA Sora] Vertical lines are relations, but they can NEVER be functions!

---

### [Slide 8] Section 2.4 Complete Mastery Summary
*Unit 2 • Lecture 25 • Section 2.4 Wrap-up*

#### 📖 Official Workbook Problem
### Summary of Section 2.4 Functions
- **Definition:** Every input $x$ has exactly one output $y$.
- **Ordered Pairs:** No $x$-value can repeat with different $y$'s.
- **Graphs (VLT):** No vertical line can hit more than once.
- **Linear Functions:** All lines are functions EXCEPT vertical lines ($x = c$).

#### 💡 Complete Step-by-Step Solution
$$\mathbf{\text{Section 2.4 Mastered! Next Up: Section 2.5 — Function Notation f(x)!}}$$

#### ⚠️ Pitfall & Strategy
**Remember:** Functions are the bedrock of all advanced mathematics and calculus!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Fantastic work mastering Section 2.4! You can now identify functions algebraically and graphically.

[TA Sora] In Lecture 26, we introduce the famous notation $f(x)$!

---

