# Montana State University - Gallatin College
## M090 Introductory Algebra — Lecture 30
**Instructors:** Prof. Eunju Park & TA Sora (Gallatin College MSU)
**Workbook Source:** M090 Full Student Workbook

---

### [Slide 1] Section 2.7 Example 4: Adult Systolic Blood Pressure Model
*Unit 2 • Lecture 30 • Section 2.7 Example 4 (Workbook p. 54)*

#### 📖 Official Workbook Problem
### Adult Systolic Blood Pressure (Workbook p. 54)
Let $x$ represent age in years and $P(x)$ represent systolic blood pressure in mmHg:
- A **23-year-old** adult has a blood pressure of **120 mmHg** $\implies (23, 120)$.
- A **53-year-old** adult has a blood pressure of **132 mmHg** $\implies (53, 132)$.
Find the linear function $P(x)$.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Step 1: } & m = \frac{132 - 120}{53 - 23} = \frac{12}{30} = \mathbf{0.4 \text{ mmHg/year}} \\[0.5em]
\text{Step 2: } & P - 120 = 0.4(x - 23) \\[0.5em]
& P - 120 = 0.4x - 9.2 \\[0.5em]
\mathbf{P(x)} & = \mathbf{0.4x + 110.8}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Decimal slope:** $12/30 = 0.4$. That means on average, adult systolic blood pressure increases by $0.4$ mmHg every year of age!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] In Example 4, we model medical data. Blood pressure rises at a rate of 0.4 mmHg per year of life.

[TA Sora] The baseline model intercept at age 0 is 110.8 mmHg, giving $P(x) = 0.4x + 110.8$!

---

### [Slide 2] Section 2.7 Example 5 (Part 1): Bozeman Elevation & Boiling Point
*Unit 2 • Lecture 30 • Section 2.7 Example 5 (Workbook p. 55)*

#### 📖 Official Workbook Problem
### Bozeman Elevation vs Boiling Point (Workbook p. 55)
The relationship between elevation $x$ (in feet) and boiling point of water $B(x)$ (in $^\circ$F):
- At **0 ft elevation** (sea level camping), water boils at **$212^\circ$F** $\implies (0, 212)$.
- Hiking up to the **Bozeman "M"** at **5700 ft elevation**, water boils at **$200^\circ$F** $\implies (5700, 200)$.
Identify the two ordered pairs and state the $y$-intercept.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Sea level point: } & (x_1, B_1) = \mathbf{(0, 212)} \quad (y\text{-intercept } b = 212) \\[0.5em]
\text{Bozeman "M" point: } & (x_2, B_2) = \mathbf{(5700, 200)}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Notice b is already given!** Because sea level is elevation $0$, $(0, 212)$ is our $y$-intercept directly!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] In Example 5, we connect to Bozeman's famous 'M' trail on the Bridger foothills! Water boils at a lower temperature at higher elevations.

[TA Sora] Because atmospheric pressure is lower! At 0 feet it boils at 212 degrees, but at 5700 feet it boils at 200 degrees.

---

### [Slide 3] Section 2.7 Example 5 (Part 2): Boiling Point Function B(x)
*Unit 2 • Lecture 30 • Section 2.7 Example 5 Solution (Workbook p. 55)*

#### 📖 Official Workbook Problem
### Example 5 Solution (Workbook p. 55)
Write a linear function $B(x)$ that represents the boiling point of water in degrees Fahrenheit in terms of elevation $x$ in feet:
- Calculate slope $m$.
- Assemble the linear function.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
m & = \frac{200 - 212}{5700 - 0} = \frac{-12}{5700} = \mathbf{-\frac{1}{475} \; ^\circ\text{F/ft}} \\[0.6em]
\text{Since } b = 212: & \\
\mathbf{B(x)} & = \mathbf{-\frac{1}{475}x + 212}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Negative rate:** Boiling point drops as elevation increases, so the slope must be negative: $-\frac{1}{475}$!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] The slope simplifies to $-\frac{1}{475}$ degrees per foot of elevation.

[TA Sora] That means water boiling point drops by 1 degree Fahrenheit for every 475 feet you climb in Montana!

---

### [Slide 4] Section 2.7 Example 6 (Part 1): Montana Grain Bin Storage
*Unit 2 • Lecture 30 • Section 2.7 Example 6 (Workbook p. 55)*

#### 📖 Official Workbook Problem
### Montana Grain Bin Depletion (Workbook p. 55)
In **2001**, the volume in a grain bin is **45 tons**. In **2025**, there were only **15 tons** remaining.
- Create a linear model $V(t)$ that represents the volume of grain left in the bin, $t$ years after 2000.
- State the data points in terms of $t$ (years after 2000).

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
2001 \implies t_1 & = 2001 - 2000 = \mathbf{1} \implies \mathbf{(1, 45)} \\[0.5em]
2025 \implies t_2 & = 2025 - 2000 = \mathbf{25} \implies \mathbf{(25, 15)}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Base year offset:** Years are defined as $t$ years AFTER 2000! So 2001 is $t = 1$, NOT $t = 2001$!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] In Montana agriculture, grain bins are vital for harvest storage. Here $t$ is measured from the year 2000.

[TA Sora] So 2001 is $t=1$, and 2025 is $t=25$!

---

### [Slide 5] Section 2.7 Example 6 (Part 2): Grain Model & When Empty
*Unit 2 • Lecture 30 • Section 2.7 Example 6 Solution (Workbook p. 55)*

#### 📖 Official Workbook Problem
### Example 6 Solution (Workbook p. 55)
- Find the linear model $V(t)$.
- **Determine when the grain bin will be completely empty.**

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Step 1: } & m = \frac{15 - 45}{25 - 1} = \frac{-30}{24} = \mathbf{-1.25 \text{ tons/year}} \\[0.5em]
\text{Step 2: } & V - 45 = -1.25(t - 1) \\
& V - 45 = -1.25t + 1.25 \implies \mathbf{V(t) = -1.25t + 46.25} \\[0.8em]
\text{Step 3: } & \text{Set } V(t) = 0: \\
& 0 = -1.25t + 46.25 \implies 1.25t = 46.25 \implies \mathbf{t = 37} \\[0.5em]
\text{Calendar Year: } & 2000 + 37 = \mathbf{\text{Year } 2037}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Convert t back to calendar year:** $t = 37$ means 37 years after 2000, so the bin will empty in the year 2037!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Slope is $-1.25$ tons per year. The model is $V(t) = -1.25t + 46.25$.

[TA Sora] Setting $V(t) = 0$ gives $t = 37$, so the grain bin will be completely empty in the year 2037!

---

### [Slide 6] Unit 2 Master Principles: The Linear Universe
*Unit 2 • Lecture 30 • Unit 2 Complete Synthesis*

#### 📖 Official Workbook Problem
### Unit 2 Master Principles Recap (Sections 2.0 – 2.7)
1. **Cartesian Coordinates:** $(x, y)$, Quadrants I–IV, Intercepts $(a, 0)$ and $(0, b)$.
2. **Slope:** $m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\text{Rise}}{\text{Run}}$.
3. **Parallel & Perpendicular:** Parallel ($m_1 = m_2$), Perpendicular ($m_1 \cdot m_2 = -1$).
4. **Linear Forms:** Slope-intercept ($y = mx + b$), Point-slope ($y - y_1 = m(x - x_1)$).
5. **Special Lines (HOY VUX):** Horizontal ($y = c, m = 0$), Vertical ($x = c, m = \text{undefined}$).
6. **Functions & VLT:** Every input has exactly one output. Passes Vertical Line Test.
7. **Function Notation:** $y = f(x)$, evaluating $f(a)$ vs solving $f(x) = k$.
8. **Linear Models:** $f(x) = mx + b$ where $m = \text{rate}$ and $b = \text{initial value}$.

#### 💡 Complete Step-by-Step Solution
$$\begin{array}{|c|c|c|}
\hline
\textbf{Topic} & \textbf{Formula / Rule} & \textbf{Key Application} \\
\hline
\text{Slope} & m = \frac{y_2 - y_1}{x_2 - x_1} & \text{Steepness \& Direction} \\
\hline
\text{Point-Slope} & y - y_1 = m(x - x_1) & \text{Writing any line} \\
\hline
\text{Parallel} & m_1 = m_2 & \text{Same direction} \\
\hline
\text{Perpendicular} & m_1 \cdot m_2 = -1 & 90^\circ \text{ intersection} \\
\hline
\text{Linear Function} & f(x) = mx + b & \text{Real-world rates} \\
\hline
\end{array}$$

#### ⚠️ Pitfall & Strategy
**You have built a powerhouse algebraic foundation:** These 8 pillars will support everything you do in algebra and calculus!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Look at how much ground we have conquered together from page 29 to page 56 of the workbook!

[TA Sora] You can graph any line, find any equation, test any function, and model any real-world problem!

---

### [Slide 7] Unit 2 Master Coordinate Grid: All Line Types
*Unit 2 • Lecture 30 • Visual Comparison*

#### 📖 Official Workbook Problem
### Visualizing Every Line Family on One Coordinate Plane
Observe how all forms of lines coexist in the Cartesian coordinate system:
- **Rising Line ($m > 0$):** $y = x + 1$ (Blue)
- **Falling Line ($m < 0$):** $y = -x + 3$ (Pink)
- **Horizontal Line (HOY):** $y = -2$ (Green)
- **Vertical Line (VUX):** $x = 4$ (Gold)

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Blue: } & y = x + 1 \quad (m = +1 > 0) \\
\text{Pink: } & y = -x + 3 \quad (m = -1 < 0) \\
\text{Green: } & y = -2 \quad (m = 0, \text{ HOY}) \\
\text{Gold: } & x = 4 \quad (m = \text{undefined}, \text{ VUX})
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Coordinate Plane Mastery:** The coordinate plane is a unified visual stage for every equation in algebra!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Here is the grand visual summary: positive slope, negative slope, zero slope, and undefined slope on one Cartesian plane.

[TA Sora] A masterpiece of visual algebra!

---

### [Slide 8] Unit 2 Mastered! Transition to Unit 3 (Quadratics)
*Unit 2 • Lecture 30 • Course Milestone*

#### 📖 Official Workbook Problem
### Milestone Achieved: Two-Thirds of M090 Complete!
- **Unit 1 Conquered:** Algebraic Expressions, Signed Numbers, Fractions, Equations, Inequalities.
- **Unit 2 Conquered:** Cartesian Coordinates, Linear Equations, Slopes, Functions, Real-World Modeling.
- **Coming Next in Unit 3:** Quadratic Functions, Factoring Polynomials, Solving Quadratic Equations, and Parabolas!

#### 💡 Complete Step-by-Step Solution
$$\mathbf{\text{Unit 2 Complete! Onward to Unit 3: Quadratic Functions \& Factoring!}}$$

#### ⚠️ Pitfall & Strategy
**Celebrate your achievement:** You have mastered two entire units of college developmental algebra!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Students, congratulations on mastering Unit 2 of M090 Introductory Algebra at Gallatin College MSU!

[TA Sora] Every problem, every graph, every slope, and every real-world Montana model has been conquered!

[Prof. Park] In Unit 3, we move from straight lines to curves: Quadratic Functions and Factoring!

[TA Sora] Go Bobcats! See you in Unit 3!

---

