import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
output_dir = r"c:\Oikos Univ\Montana_State_Univ\lectures"
os.makedirs(output_dir, exist_ok=True)

# Lecture 04: Translating English Phrases
l04 = r"""# Lecture 04: Translating English Phrases into Algebraic Expressions
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.1 (Student Workbook p. 7)  
**Lecture Duration:** ~22 Minutes (8 Slides • "Paired Phrases = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 04: The English-to-Algebra Dictionary](#slide-01-welcome-to-lecture-04-the-english-to-algebra-dictionary)
- [Slide 02: The Big 4 Operation Signal Words (+, -, ×, ÷)](#slide-02-the-big-4-operation-signal-words)
- [Slide 03: Reversal Words Alert: "Less Than" and "Subtracted From"](#slide-03-reversal-words-alert-less-than-and-subtracted-from)
- [Slide 04: Translations 1 & 2: Sums and Reversals ($x + 5$ and $3x - 6$)](#slide-04-translations-1-and-2-sums-and-reversals)
- [Slide 05: Translations 3 & 4: Quotients & Multi-Operations ($\frac{x}{y}$ and $9x + 7$)](#slide-05-translations-3-and-4-quotients-and-multi-operations)
- [Slide 06: Translations 5 & 6: The Square of a Sum vs. Sum of Squares ($(x + 42)^2$ and $x - 11x$)](#slide-06-translations-5-and-6-the-square-of-a-sum-vs-sum-of-squares)
- [Slide 07: Translations 7, 8, 9: Powers, Opposites & Fraction Coefficients ($x^3 - (-x)$ and $\frac{3}{4}x + 100$)](#slide-07-translations-7-8-9-powers-opposites-and-fraction-coefficients)
- [Slide 08: Lecture 04 Wrap-Up & Sora's Word Problem Survival Code](#slide-08-lecture-04-wrap-up-and-soras-word-problem-survival-code)

---

## Slide 01: Welcome to Lecture 04: The English-to-Algebra Dictionary
**Slide Type:** Lecture Orientation  
**Theme:** Breaking the language barrier between words and mathematical symbols  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Welcome to Lecture 04! Today we explore one of the most practical skills in all of mathematics: translating ordinary English phrases into crisp algebraic expressions.

[TA Sora] Many students tell me: "Professor Park, I can do the arithmetic when you give me numbers, but when word problems start, my brain freezes!"

[Prof. Park] That's because algebra is literally a foreign language! Just like learning Spanish or Korean, you need a translation dictionary for the vocabulary.

[TA Sora] Exactly! Once you know that "quotient" means division and "difference" means subtraction, the fear vanishes!

---

## Slide 02: The Big 4 Operation Signal Words (+, -, ×, ÷)
**Slide Type:** Vocabulary & Concept Reference  

| Operation | Signal English Words | Example |
| :--- | :--- | :--- |
| **Addition ($+$)** | sum, increased by, more than, total, plus | sum of $x$ and $5 \to x + 5$ |
| **Subtraction ($-$)** | difference, decreased by, minus, diminished by | difference of $x$ and $7 \to x - 7$ |
| **Multiplication ($\cdot$)**| product, times, twice ($2x$), of (fraction of) | product of 3 numbers $\to xyz$ |
| **Division ($\div$)** | quotient, divided by, ratio of | quotient of $x$ and $y \to \frac{x}{y}$ |

### 🎙️ English Lecture Script
[Prof. Park] Take a screenshot of Slide 2. These are your foundational translation keys.

[TA Sora] Notice the word "of" in multiplication! "Half of thirty" means $\frac{1}{2} \times 30 = 15$. That shows up everywhere in banking and shopping discounts!

---

## Slide 03: Reversal Words Alert: "Less Than" and "Subtracted From"
**Slide Type:** Common Pitfall Warning  
**LaTeX Anchor:** \text{"Six less than } 3x\text{"} \implies 3x - 6 \quad (\mathbf{\text{NOT }} 6 - 3x!)

### 🎙️ English Lecture Script
[Prof. Park] Sora, what is the single most dangerous phrase in English math translation?

[TA Sora] Without hesitation: **"LESS THAN"**! When people hear "six less than twenty," they think: "I started with twenty dollars, and I have six less, so $20 - 6 = 14$."

[Prof. Park] Exactly. But when they see "six less than three times a number," they write $6 - 3x$ because the six was spoken first!

[TA Sora] **Sora's Reversal Rule:** Whenever you see "less than" or "subtracted from", draw a big reverse arrow! The number mentioned first goes to the BACK!

---

## Slide 04: Translations 1 & 2: Sums and Reversals ($x + 5$ and $3x - 6$)
**Slide Type:** Paired Problem Breakdown  
**Workbook Source:** Section 1.1 Table rows 1 & 2 (Workbook p. 7)  

### 📝 Translations
- **Phrase 1:** "the sum of a number and five" $\implies \mathbf{x + 5}$
- **Phrase 2:** "six less than three times a number" $\implies \mathbf{3x - 6}$

### 💡 AI Step-by-Step Breakdown
1. In Phrase 1, "sum" signals addition: start with unknown $x$ and add 5: $x + 5$.
2. In Phrase 2, "three times a number" is $3x$. "Six less than" reverses the order: $3x - 6$.

### 🎙️ English Lecture Script
[Prof. Park] Let’s compare rows 1 and 2 from page 7 of our workbook. Row 1 is straightforward: $x + 5$.

[TA Sora] But row 2 has our reversal trap: "six less than three times a number." 

[Prof. Park] Three times a number is $3x$. Six less than that is $3x - 6$. If you wrote $6 - 3x$, you just reversed who owes money to whom!

---

## Slide 05: Translations 3 & 4: Quotients & Multi-Operations ($\frac{x}{y}$ and $9x + 7$)
**Slide Type:** Paired Problem Breakdown  
**Workbook Source:** Section 1.1 Table rows 3 & 4 (Workbook p. 7)  

### 📝 Translations
- **Phrase 3:** "the quotient of two unknown numbers" $\implies \mathbf{\dfrac{x}{y}}$
- **Phrase 4:** "seven more than nine times a number" $\implies \mathbf{9x + 7}$

### 🎙️ English Lecture Script
[Prof. Park] In Phrase 3, we have two unknown numbers. So we need two different letters: $x$ and $y$. Quotient means division: $\frac{x}{y}$.

[TA Sora] And in Phrase 4: "nine times a number" is $9x$. "Seven more than" adds 7: $9x + 7$. Addition is commutative, but writing $9x + 7$ matches standard algebraic form!

---

## Slide 06: Translations 5 & 6: The Square of a Sum vs. Sum of Squares ($(x + 42)^2$ and $x - 11x$)
**Slide Type:** Paired Problem Breakdown  
**Workbook Source:** Section 1.1 Table rows 5 & 6 (Workbook p. 7)  

### 📝 Translations
- **Phrase 5:** "the square of the sum of a number and forty-two" $\implies \mathbf{(x + 42)^2}$
- **Phrase 6:** "a number decreased by the product of eleven and that same number" $\implies \mathbf{x - 11x}$

### 🎙️ English Lecture Script
[Prof. Park] Pay special attention to Phrase 5: "the square OF the sum..." Notice the word "of" tells you that the squaring happens to the ENTIRE sum!

[TA Sora] That means we must wrap the sum in parentheses before applying the exponent: $(x + 42)^2$! If you wrote $x^2 + 42$, that’s the sum of a square, not the square of a sum!

[Prof. Park] And in Phrase 6: start with a number $x$. Decrease it by the product of 11 and that same number: $x - 11x$.

---

## Slide 07: Translations 7, 8, 9: Powers, Opposites & Fraction Coefficients ($x^3 - (-x)$ and $\frac{3}{4}x + 100$)
**Slide Type:** Paired Problem Breakdown  
**Workbook Source:** Section 1.1 Table rows 7, 9, 10 (Workbook p. 7)  

### 📝 Translations
- **Phrase 7:** "the difference between a number cubed and the opposite of that number" $\implies \mathbf{x^3 - (-x)} = \mathbf{x^3 + x}$
- **Phrase 8:** "five times a number reduced by the square of a second number" $\implies \mathbf{5x - y^2}$
- **Phrase 9:** "three-fourths of a number increased by one hundred" $\implies \mathbf{\dfrac{3}{4}x + 100}$

### 🎙️ English Lecture Script
[Prof. Park] Phrase 7 has a beautiful subtlety: "the opposite of that number." The opposite of $x$ is $-x$. 

[TA Sora] So the difference between $x^3$ and $-x$ is $x^3 - (-x)$, which simplifies to $x^3 + x$!

[Prof. Park] And Phrase 9: "three-fourths of a number" is $\frac{3}{4}x$. Increased by 100 gives $\frac{3}{4}x + 100$.

---

## Slide 08: Lecture 04 Wrap-Up & Sora's Word Problem Survival Code
**Slide Type:** Conclusion & Summary  
- **1. Reversal Words:** "Less than" $\implies$ reverse the order.
- **2. Grouping Clues:** "Square of the sum" $\implies$ parentheses $(x + c)^2$.
- **3. Distinct Letters:** "Two unknown numbers" $\implies$ use $x$ and $y$.
- **Next Lecture:** Section 1.2: The Laws of Exponents!
"""

with open(os.path.join(output_dir, "lecture04.md"), "w", encoding="utf-8") as f:
    f.write(l04)
print("Generated lecture04.md successfully.")
