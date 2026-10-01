# Montana State University - Gallatin College
## M090 Introductory Algebra — Lecture 24
**Instructors:** Prof. Eunju Park & TA Sora (Gallatin College MSU)
**Workbook Source:** M090 Full Student Workbook

---

### [Slide 1] Section 2.4: Relations, Domain & Range
*Unit 2 • Lecture 24 • Section 2.4 (Workbook p. 45)*

#### 📖 Official Workbook Problem
### Fundamentals of Relations (Workbook p. 45)
- **Relation:** Any set of ordered pairs $(x, y)$.
- **Input:** The first value in the ordered pair ($x$).
- **Output:** The second value in the ordered pair ($y$).
- **Domain:** The set of **all input values** ($x$-coordinates).
- **Range:** The set of **all output values** ($y$-coordinates).

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Relation } R & = \{(x_1, y_1), (x_2, y_2), \dots\} \\[0.5em]
\text{Domain} & = \{x \mid (x, y) \in R\} \quad (\text{all } x\text{-values}) \\
\text{Range} & = \{y \mid (x, y) \in R\} \quad (\text{all } y\text{-values})
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**No duplicates in sets:** When writing domain or range in set notation, list repeating numbers only ONCE!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Welcome to Section 2.4! A relation is simply any pairing between inputs and outputs.

[TA Sora] Think of a vending machine: you press a button (input $x$) and get a snack (output $y$)!

---

### [Slide 2] Section 2.4 Example 1: Domain & Range of a Discrete Relation
*Unit 2 • Lecture 24 • Section 2.4 Example 1 (Workbook p. 45)*

#### 📖 Official Workbook Problem
### Example 1 (Workbook p. 45)
For the following relation, determine the domain and range:
$$\mathbf{\{(1, -1), (2, 5), (3, 10), (4, 16), (2, -3)\}}$$
- List all $x$-values in braces $\{\}$.
- List all $y$-values in order from least to greatest.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Inputs } (x): & 1, 2, 3, 4, 2 \\[0.5em]
\mathbf{\text{Domain: }} & \mathbf{\{1, 2, 3, 4\}} \quad (\text{do not repeat } 2!) \\[0.8em]
\text{Outputs } (y): & -1, 5, 10, 16, -3 \\[0.5em]
\mathbf{\text{Range: }} & \mathbf{\{-3, -1, 5, 10, 16\}} \quad (\text{written in numerical order})
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**The repeated input:** Notice that the input $2$ appears twice: $(2, 5)$ and $(2, -3)$! In the domain set, we write $2$ once.

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] In Example 1, we collect all inputs into the domain: $\{1, 2, 3, 4\}$.

[TA Sora] And for the range, list them in increasing order: $\{-3, -1, 5, 10, 16\}$!

---

### [Slide 3] Section 2.4 Example 1: Coordinate Grid of Discrete Points
*Unit 2 • Lecture 24 • Section 2.4 Example 1 Visual*

#### 📖 Official Workbook Problem
### Visualizing Example 1 on the Coordinate Plane
Plot all five points of the relation:
$$(1, -1), \; (2, 5), \; (3, 10), \; (4, 16), \; (2, -3)$$
What do you notice vertically about the points $(2, 5)$ and $(2, -3)$?

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Notice: } & (2, 5) \text{ and } (2, -3) \text{ share the EXACT same } x\text{-coordinate } x = 2. \\[0.5em]
\text{Visual: } & \mathbf{\text{They stack directly above and below each other vertically!}} \\[0.5em]
\text{Significance: } & \text{A single vertical line } x = 2 \text{ passes through BOTH points.}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Vertical stacking:** When two points have the same $x$, they lie on the same vertical line. This will be the key to the Vertical Line Test!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Look at your screen. Point $(2, 5)$ and Point $(2, -3)$ stack vertically at $x = 2$.

[TA Sora] They lie on the same vertical line $x = 2$! Remember this image for when we discuss functions!

---

### [Slide 4] Mapping Diagrams: Visualizing Relations
*Unit 2 • Lecture 24 • Section 2.4 Mapping Diagrams*

#### 📖 Official Workbook Problem
### Mapping Diagrams (Domain $\rightarrow$ Range)
In a mapping diagram:
- The left oval contains the **Domain** elements.
- The right oval contains the **Range** elements.
- Arrows point from each input to its corresponding output.

In Example 1:
- $1 \rightarrow -1$
- $\mathbf{2 \rightarrow 5}$ and $\mathbf{2 \rightarrow -3}$ *(One input branches to TWO outputs!)*
- $3 \rightarrow 10$
- $4 \rightarrow 16$

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Domain Oval: } & \{1, 2, 3, 4\} \\
\text{Range Oval: } & \{-3, -1, 5, 10, 16\} \\[0.5em]
\text{Branching at } 2: & 2 \text{ sends out two arrows: } 2 \rightarrow 5 \text{ and } 2 \rightarrow -3.
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Branching arrows:** If any input has more than one arrow leaving it, that relation CANNOT be a function!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Mapping diagrams show the flow of information. Look at input 2: it shoots out two arrows.

[TA Sora] If you press button 2 on a vending machine, you don't know whether you will get chips or soda! That uncertainty is what prevents it from being a function!

---

### [Slide 5] Section 2.4 Example 2 (Graph A): Continuous Domain & Range
*Unit 2 • Lecture 24 • Section 2.4 Example 2A (Workbook p. 45)*

#### 📖 Official Workbook Problem
### Example 2 Graph A (Workbook p. 45)
For the line segment shown on the graph extending from $(-4, -2)$ to $(4, 2)$:
- Determine the **Domain** in interval notation.
- Determine the **Range** in interval notation.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Leftmost } x: & -4 \quad (\text{closed dot} \implies [) \\
\text{Rightmost } x: & +4 \quad (\text{closed dot} \implies ]) \\[0.5em]
\mathbf{\text{Domain: }} & \mathbf{[-4, 4]} \\[0.8em]
\text{Lowest } y: & -2 \quad (\text{closed dot} \implies [) \\
\text{Highest } y: & +2 \quad (\text{closed dot} \implies ]) \\[0.5em]
\mathbf{\text{Range: }} & \mathbf{[-2, 2]}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Continuous uses intervals, not braces:** A solid curve contains infinitely many points, so we write intervals $[-4, 4]$, NOT discrete lists $\{-4, 4\}$!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] In Example 2 Graph A, we have a continuous line segment. Look left-to-right for domain, and bottom-to-top for range.

[TA Sora] The $x$-values stretch from $-4$ to $4$, so Domain is $[-4, 4]$. The $y$-values stretch from $-2$ to $2$, so Range is $[-2, 2]$!

---

### [Slide 6] Section 2.4 Example 2 (Graph B): Bounded Curve
*Unit 2 • Lecture 24 • Section 2.4 Example 2B (Workbook p. 45)*

#### 📖 Official Workbook Problem
### Example 2 Graph B (Workbook p. 45)
For the graph shown extending from $x = -3$ to $x = 5$ with minimum $y = -2$ and peak $y = 4$:
- State the **Domain** in interval notation.
- State the **Range** in interval notation.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Leftmost } x: & -3, \quad \text{Rightmost } x: 5 \\[0.5em]
\mathbf{\text{Domain: }} & \mathbf{[-3, 5]} \\[0.8em]
\text{Lowest } y: & -2, \quad \text{Highest } y: 4 \\[0.5em]
\mathbf{\text{Range: }} & \mathbf{[-2, 4]}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Peak vs Endpoint:** For range, do not just look at the endpoints! Look for the absolute lowest valley and absolute highest peak on the graph!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] In Example 2 Graph B, the curve dips down to $-2$ and peaks at $+4$.

[TA Sora] So while the domain is $[-3, 5]$ horizontally, the range reaches from $-2$ up to $4$, giving $[-2, 4]$!

---

### [Slide 7] Interval Notation vs Set-Builder Notation
*Unit 2 • Lecture 24 • Section 2.4 Notation Guide*

#### 📖 Official Workbook Problem
### How to Report Domain and Range (Workbook p. 45)
- **Discrete Relations (individual points):**
  Use set braces listing numbers: $\{1, 2, 3, 4\}$.
- **Continuous Relations (connected lines/curves):**
  Use interval notation: $[a, b]$ or $(-\infty, \infty)$.
- **Interval Symbols:**
  - $[$ or $]$: Bracket includes the number (solid dot $\bullet$).
  - $($ or $)$: Parenthesis excludes the number (open circle $\circ$) or for $\pm\infty$.

#### 💡 Complete Step-by-Step Solution
$$\begin{array}{|c|c|c|}
\hline
\textbf{Type of Graph} & \textbf{Format} & \textbf{Example} \\
\hline
\text{Discrete Points} & \text{Set Braces } \{\} & D = \{1, 2, 3\}, \; R = \{4, 5\} \\
\hline
\text{Segment with solid dots} & \text{Closed Interval } [a, b] & D = [-4, 4], \; R = [-2, 2] \\
\hline
\text{Line with arrows both ways} & \text{All Real Numbers} & D = (-\infty, \infty), \; R = (-\infty, \infty) \\
\hline
\end{array}$$

#### ⚠️ Pitfall & Strategy
**Never use braces for intervals:** $\{ -4, 4 \}$ only means two numbers: $-4$ and $4$. $[-4, 4]$ includes all infinite numbers in between!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Always choose the right notation: curly braces for discrete points, square brackets and parentheses for continuous intervals.

[TA Sora] That distinction is essential on quizzes and exams!

---

### [Slide 8] Section 2.4 Part 1 Mastery Summary
*Unit 2 • Lecture 24 • Section 2.4 Wrap-up*

#### 📖 Official Workbook Problem
### Section 2.4 Part 1 Master Checklist
- **Input = $x$-coordinate**
- **Output = $y$-coordinate**
- **Domain = set of all inputs** (look left to right on graph)
- **Range = set of all outputs** (look bottom to top on graph)

#### 💡 Complete Step-by-Step Solution
$$\mathbf{\text{Lecture 24 Complete! Next Up: Section 2.4 Part 2 — Functions \& The Vertical Line Test!}}$$

#### ⚠️ Pitfall & Strategy
**Left-to-Right, Bottom-to-Top:** Always read domain from left to right, and range from bottom to top!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Excellent job! In Lecture 25, we find out which relations earn the special title of FUNCTION!

---

