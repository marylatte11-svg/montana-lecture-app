# Montana State University - Gallatin College
## M090 Introductory Algebra — Lecture 29
**Instructors:** Prof. Eunju Park & TA Sora (Gallatin College MSU)
**Workbook Source:** M090 Full Student Workbook

---

### [Slide 1] Section 2.7: Modeling with Linear Functions
*Unit 2 • Lecture 29 • Section 2.7 (Workbook p. 53)*

#### 📖 Official Workbook Problem
### Modeling with Linear Functions (Workbook p. 53)
$$\mathbf{f(x) = mx + b}$$
In real-world applications:
- **$m$ = Rate of Change:** (e.g. dollars per hour, miles per gallon, depreciation per year).
- **$b$ = Initial Value / Fixed Cost:** (e.g. startup fee, purchase price, base charge at time $0$).
- **Strategy:** Decide if you are directly given the rate $m$ and initial value $b$, or if you need to build two data points $(x_1, y_1)$ and $(x_2, y_2)$ from the story!

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Case 1: } & \text{Given rate } m \text{ and initial value } b \implies \mathbf{f(x) = mx + b} \\
\text{Case 2: } & \text{Given two scenarios } (x_1, y_1), \; (x_2, y_2) \implies m = \frac{y_2 - y_1}{x_2 - x_1}, \; \text{then point-slope}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Units matter:** Always include units on the slope (e.g. 'dollars per hour') and the intercept (e.g. 'dollars')!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Welcome to Section 2.7! This is where algebra comes alive: modeling real Montana businesses, cars, and science.

[TA Sora] $m$ is the rate of change, and $b$ is the starting point!

---

### [Slide 2] Section 2.7 Example 1 (Part 1): Kim's Bozeman Ski Rental Model
*Unit 2 • Lecture 29 • Section 2.7 Example 1 (Workbook p. 53)*

#### 📖 Official Workbook Problem
### Kim's Bozeman Ski Rental (Workbook p. 53)
Kim owns a ski rental business in Bozeman. His monthly fixed costs are **$2450** (rent, utilities, supplies). Additionally, Kim pays his employee **$15 per hour**.
- Write a linear function $C(h)$ that models Kim's monthly cost in terms of $h$, the number of hours his employee works.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Fixed cost (initial value } b): & 2450 \text{ dollars} \\[0.5em]
\text{Hourly wage (rate } m): & 15 \text{ dollars/hour} \\[0.5em]
\mathbf{C(h)} & = \mathbf{15h + 2450}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Use variable h:** The prompt asks for $C(h)$, so use $h$ for hours, not $x$!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] In Example 1, fixed costs are $2450 and hourly wage is $15.

[TA Sora] The function is $C(h) = 15h + 2450$!

---

### [Slide 3] Section 2.7 Example 1 (Part 2): Monthly Cost for 25 Hours
*Unit 2 • Lecture 29 • Section 2.7 Example 1 Evaluation (Workbook p. 53)*

#### 📖 Official Workbook Problem
### Example 1 Evaluation (Workbook p. 53)
Find the monthly cost if Kim pays an employee to work **25 hours**.
- Evaluate $C(25)$.
- Plot the cost curve and highlight $(25, C(25))$.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
C(25) & = 15(25) + 2450 \\[0.5em]
& = 375 + 2450 \\[0.5em]
\mathbf{C(25)} & = \mathbf{2825} \\[0.8em]
\mathbf{\text{Sentence: }} & \mathbf{\text{The monthly cost for 25 employee hours is 2825 dollars.}}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Always state answers in context:** Don't just write $2825$. State what it means: Kim pays $2825 in total monthly costs!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Evaluating $C(25) = 15(25) + 2450 = 375 + 2450 = 2825 dollars.

[TA Sora] Notice on the coordinate grid how the base cost starts at 2450 and rises linearly!

---

### [Slide 4] Section 2.7 Example 2 (Part 1): Car Depreciation Model
*Unit 2 • Lecture 29 • Section 2.7 Example 2 (Workbook p. 53)*

#### 📖 Official Workbook Problem
### Car Depreciation (Workbook p. 53)
You purchased your car in 2023 for **$22,500**. You learned that the car would **depreciate linearly by $1500 per year**.
- Write a function $V(t)$ that gives the value of the car $t$ years after 2023.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Initial purchase price } (b): & 22500 \text{ dollars} \\[0.5em]
\text{Depreciation rate } (m): & \mathbf{-1500} \text{ dollars/year} \quad (\text{value decreases!}) \\[0.5em]
\mathbf{V(t)} & = \mathbf{-1500t + 22500}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Depreciation means negative slope:** The car is LOSING value, so $m = -1500$, NOT $+1500$!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] In Example 2, the car depreciates. Depreciation means decreasing value, so slope is negative $1500$.

[TA Sora] Our function is $V(t) = -1500t + 22500$!

---

### [Slide 5] Section 2.7 Example 2 (Part 2): When is Car Value Zero?
*Unit 2 • Lecture 29 • Section 2.7 Example 2 Analysis (Workbook p. 53)*

#### 📖 Official Workbook Problem
### Example 2 Graph & Zero Value (Workbook p. 53)
Using $V(t) = -1500t + 22500$:
- Find when the car's value reaches **$0** (the $t$-intercept).
- What calendar year does this correspond to?

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Set } V(t) = 0: & 0 = -1500t + 22500 \\[0.5em]
1500t & = 22500 \\[0.5em]
t & = \frac{22500}{1500} = \mathbf{15 \text{ years}} \\[0.8em]
\text{Calendar Year: } & 2023 + 15 = \mathbf{\text{Year } 2038}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Calendar year interpretation:** $t = 15$ means 15 years after 2023, which is 2038!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] Setting $V(t) = 0$ gives $t = 15$ years.

[TA Sora] That means in the year 2038, the car's value will reach $0 on our coordinate graph!

---

### [Slide 6] Section 2.7 Example 3 (Part 1): Car Salesperson Commission Points
*Unit 2 • Lecture 29 • Section 2.7 Example 3 (Workbook p. 54)*

#### 📖 Official Workbook Problem
### Car Salesperson Commission (Workbook p. 54)
A salesperson earns commission on car sales:
- Sold **3 cars**, earned **$760** for the week.
- Sold **5 cars**, earned **$920** for the week.
Translate these two statements into ordered pairs $(x, E)$ where $x$ is cars sold and $E$ is weekly earnings.

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
\text{Week 1: } & 3 \text{ cars sold, } 760 \text{ dollars earned} \implies \mathbf{(3, 760)} \\[0.5em]
\text{Week 2: } & 5 \text{ cars sold, } 920 \text{ dollars earned} \implies \mathbf{(5, 920)}
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Identify variables correctly:** $x$ = number of cars (input), $E(x)$ = earnings in dollars (output).

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] In Example 3, we are not given the slope or intercept directly. We are given two data points!

[TA Sora] $(3, 760)$ and $(5, 920)$. Now we can find the commission rate!

---

### [Slide 7] Section 2.7 Example 3 (Part 2): Commission Function E(x)
*Unit 2 • Lecture 29 • Section 2.7 Example 3 Solution (Workbook p. 54)*

#### 📖 Official Workbook Problem
### Example 3 Solution (Workbook p. 54)
Find the linear function $E(x)$ that represents weekly earnings when $x$ cars are sold:
- Calculate commission per car (slope $m$).
- Use point-slope form to find base weekly salary (intercept $b$).

#### 💡 Complete Step-by-Step Solution
$$\begin{aligned}
m & = \frac{920 - 760}{5 - 3} = \frac{160}{2} = \mathbf{80 \text{ dollars/car}} \\[0.5em]
E - 760 & = 80(x - 3) \\[0.5em]
E - 760 & = 80x - 240 \\[0.5em]
\mathbf{E(x)} & = \mathbf{80x + 520} \\[0.8em]
\text{Interpretation: } & \text{Base salary is } \mathbf{520 \text{ dollars/week}}, \text{ plus } \mathbf{80 \text{ dollars per car sold}}.
\end{aligned}$$

#### ⚠️ Pitfall & Strategy
**Meaning of intercept:** $b = 520$ means if the salesperson sells 0 cars ($x = 0$), they still take home a base salary of $520!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] The slope is 80 dollars per car. Point-slope reveals a base salary of 520 dollars.

[TA Sora] So $E(x) = 80x + 520$. Both data points $(3, 760)$ and $(5, 920)$ sit right on the line!

---

### [Slide 8] Section 2.7 Part 1 Mastery Summary
*Unit 2 • Lecture 29 • Section 2.7 Wrap-up*

#### 📖 Official Workbook Problem
### Real-World Modeling Takeaways
- **Rate = Slope ($m$):** Watch for words like 'per', 'each', 'rate of', 'depreciates'.
- **Initial Value = Intercept ($b$):** The value when input $x = 0$.
- **Two Scenarios:** Build $(x_1, y_1)$ and $(x_2, y_2)$ and calculate $m = \frac{y_2 - y_1}{x_2 - x_1}$.

#### 💡 Complete Step-by-Step Solution
$$\mathbf{\text{Lecture 29 Complete! Next Up: Lecture 30 — Blood Pressure, Elevation \& Unit 2 Grand Review!}}$$

#### ⚠️ Pitfall & Strategy
**Sentence answers:** Always conclude word problems with a complete English sentence describing the practical meaning of your solution!

#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)
[Prof. Park] You did a fantastic job modeling these real-world scenarios.

[TA Sora] In Lecture 30, we hike up to the Bozeman 'M' and celebrate our mastery of Unit 2!

---

