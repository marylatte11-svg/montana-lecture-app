import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
output_dir = r"c:\Oikos Univ\Montana_State_Univ\lectures"
os.makedirs(output_dir, exist_ok=True)

# ==============================================================================
# LECTURE 02: Fraction Operations & Signed Numbers
# ==============================================================================
lecture02_content = """# Lecture 02: Arithmetic Review: Fractions & Signed Numbers
**Course:** M090 Introductory Algebra • Developmental Mathematics  
**Institution:** Gallatin College, Montana State University (Bozeman, MT)  
**Instructors:** Prof. Eunju Park (Lead Faculty) & TA Sora (Teaching Assistant)  
**Textbook Section:** Unit 1 • Section 1.0 (Student Workbook pp. 4–5)  
**Lecture Duration:** ~23 Minutes (9 Slides • "One or Two Problems = One Slide")  
**Format:** Duo Broadcast Dialogue • KaTeX Mathematical Notation • AI Step-by-Step Solutions  

---

## 📌 Slide Deck Overview & Problem Directory
- [Slide 01: Welcome to Lecture 02: Conquering Fraction Fear & Signed Numbers](#slide-01-welcome-to-lecture-02-conquering-fraction-fear-and-signed-numbers)
- [Slide 02: Multiplying Whole Numbers & Fractions ($(4)(\\frac{6}{7})$)](#slide-02-multiplying-whole-numbers-and-fractions-4frac67)
- [Slide 03: Adding Fractions with Different Denominators ($\\frac{3}{5} + \\frac{1}{4}$)](#slide-03-adding-fractions-with-different-denominators-frac35--frac14)
- [Slide 04: Subtracting Fractions with Shared Multiples ($\\frac{3}{4} - \\frac{5}{12}$)](#slide-04-subtracting-fractions-with-shared-multiples-frac34---frac512)
- [Slide 05: Order of Operations with Fraction Subtraction & Exponents ($(\\frac{4}{7} - \\frac{2}{3})^2$)](#slide-05-order-of-operations-with-fraction-subtraction-and-exponents-frac47---frac232)
- [Slide 06: Multiplying Small Unit Fractions ($\\frac{1}{9} \\cdot \\frac{1}{6}$)](#slide-06-multiplying-small-unit-fractions-frac19-cdot-frac16)
- [Slide 07: Dividing Fractions: The "Keep, Change, Flip" Rule ($\\frac{3}{8} \\div \\frac{1}{16}$)](#slide-07-dividing-fractions-the-keep-change-flip-rule-frac38-div-frac116)
- [Slide 08: Complex Fractions & Pre-simplifying Factors ($\\frac{5/8}{3/4}$ and $\\frac{(16)(3)}{(9)(4)}$)](#slide-08-complex-fractions-and-pre-simplifying-factors-frac5834-and-frac16394)
- [Slide 09: Mixed Order of Operations ($16 - \\frac{3}{4} + 9$) & Sora's Fraction Mastery Takeaway](#slide-09-mixed-order-of-operations-16---frac34--9-and-soras-fraction-mastery-takeaway)

---

## Slide 01: Welcome to Lecture 02: Conquering Fraction Fear & Signed Numbers
**Slide Type:** Lecture Orientation  
**Theme:** Breaking down fraction anxiety into logical slice manipulation  

### 🎙️ English Lecture Script (Prof. Park & TA Sora Dialogue)
[Prof. Park] Welcome back to Lecture 02 of M090! Today, Sora and I are addressing the single biggest fear factor in introductory mathematics: fractions and negative numbers.

[TA Sora] Oh, absolutely, Professor Park! When I survey Gallatin College students on day one and ask what makes them break into a cold sweat, over 80% answer: "Fractions!"

[Prof. Park] But fractions are not your enemies. A fraction is simply a division problem that hasn't finished calculating yet, or a way to count equal slices of a whole.

[TA Sora] Exactly! And today, we are going to work through the board exercises on page 4 of your workbook. We'll show you the exact tricks to multiply, divide, add, and simplify them without getting lost in giant numbers.

[Prof. Park] Let’s dive straight into Slide 2 with whole number and fraction multiplication!

### 🇰🇷 한국어 강의 가이드 및 핵심 요약
- **개요 요약:** 2강 도입: 발달수학 수강생들의 최대 난관인 분수와 음수 연산 극복 전략 소개
- **핵심 티칭 포인트:** 분수는 완료되지 않은 나눗셈이자 동일한 크기의 조각을 세는 도구임을 강조하여 심리적 장벽 해소
- **용어:** `Numerator` (분자), `Denominator` (분모), `Reciprocal` (역수)

---

## Slide 02: Multiplying Whole Numbers & Fractions ($(4)(\\frac{6}{7})$)
**Slide Type:** Single Problem Master Breakdown  
**Workbook Source:** Section 1.0 Board Work #2 (Workbook p. 4)  
**LaTeX Anchor:** $(4)\left(\\dfrac{6}{7}\\right)$

### 📝 Problem Statement
$$\\text{Simplify into a single improper fraction or mixed number: } \\quad (4)\\left(\\dfrac{6}{7}\\right)$$

### 💡 AI Step-by-Step Solution Breakdown
$$\\begin{aligned}
\\text{Step 1: } & \\text{Rewrite the whole number 4 as a fraction over 1:} \\\\
& 4 = \\dfrac{4}{1} \\\\[0.5em]
\\text{Step 2: } & \\text{Multiply numerators straight across, and denominators straight across:} \\\\
& \\dfrac{4}{1} \\cdot \\dfrac{6}{7} = \\dfrac{4 \\cdot 6}{1 \\cdot 7} = \\mathbf{\\dfrac{24}{7}} \\\\[0.5em]
\\text{Step 3: } & \\text{Convert to mixed number if required: } 24 \\div 7 = 3 \\text{ with remainder } 3 \\implies \\mathbf{3\\dfrac{3}{7}}
\\end{aligned}$$

### ⚠️ Sora's Pitfall Alert
$$\\text{FATAL MISTAKE: Multiplying both top and bottom by 4: } \\dfrac{4 \\cdot 6}{4 \\cdot 7} = \\dfrac{24}{28} = \\dfrac{6}{7} \\quad \\mathbf{\\text{WRONG!}}$$

### 🎙️ English Lecture Script
[Prof. Park] Sora, look at Problem #2: $(4)(\\frac{6}{7})$. Why do students sometimes multiply both the top AND the bottom by 4?

[TA Sora] Because they confuse multiplying by a whole number with finding a common denominator! When you multiply top and bottom by 4, you are actually multiplying by $\\frac{4}{4}$, which equals 1! You didn't quadruple the fraction at all!

[Prof. Park] Exactly. Whole numbers live on the top floor of the fraction building. Write $4$ as $\\frac{4}{1}$.

[TA Sora] Top times top, bottom times bottom! $4 \\times 6 = 24$, and $1 \\times 7 = 7$. Result: $\\frac{24}{7}$!

[Prof. Park] Clean, fast, and mathematically rigorous. Let’s look at addition on Slide 3.

### 🇰🇷 한국어 강의 가이드 및 핵심 요약
- **개요 요약:** 정수와 분수의 곱셈 $(4)(\\frac{6}{7})$ 풀이
- **핵심 티칭 포인트:** 정수는 분모가 1인 분수($\\frac{4}{1}$)이므로 분자에만 곱해야 함을 시각적으로 각인

---

## Slide 03: Adding Fractions with Different Denominators ($\\frac{3}{5} + \\frac{1}{4}$)
**Slide Type:** Single Problem Master Breakdown  
**Workbook Source:** Section 1.0 Board Work #3 (Workbook p. 4)  
**LaTeX Anchor:** $\\dfrac{3}{5} + \\dfrac{1}{4}$

### 📝 Problem Statement
$$\\text{Simplify into a single fraction: } \\quad \\dfrac{3}{5} + \\dfrac{1}{4}$$

### 💡 AI Step-by-Step Solution Breakdown
$$\\begin{aligned}
\\text{Step 1: } & \\text{Identify the Least Common Denominator (LCD) of 5 and 4:} \\\\
& 5 \\text{ is prime}, \\quad 4 = 2^2 \\implies \\text{LCD} = 5 \\cdot 4 = \\mathbf{20} \\\\[0.5em]
\\text{Step 2: } & \\text{Multiply each fraction by the missing form of 1 to achieve denominator 20:} \\\\
& \\left(\\dfrac{3}{5} \\cdot \\dfrac{4}{4}\\right) + \\left(\\dfrac{1}{4} \\cdot \\dfrac{5}{5}\\right) = \\dfrac{12}{20} + \\dfrac{5}{20} \\\\[0.5em]
\\text{Step 3: } & \\text{Add the numerators over the common denominator:} \\\\
& \\dfrac{12 + 5}{20} = \\mathbf{\\dfrac{17}{20}}
\\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] On Slide 3, we have $\\frac{3}{5} + \\frac{1}{4}$. The denominators are 5 and 4. What is our first mission?

[TA Sora] We cannot add fifths and fourths directly! It's like adding 3 quarters and 1 euro—different currencies! We need a common currency, which is the LCD.

[Prof. Park] The smallest number both 5 and 4 divide into is 20. 

[TA Sora] So we transform $\\frac{3}{5}$ into $\\frac{12}{20}$ by multiplying by $\\frac{4}{4}$. And $\\frac{1}{4}$ becomes $\\frac{5}{20}$ by multiplying by $\\frac{5}{5}$.

[Prof. Park] Now add the numerators: $12 + 5 = 17$. The denominator stays 20. Final answer: $\\frac{17}{20}$.

[TA Sora] Notice we do NOT add the denominators! It is not 40; the slice size remains twentieths!

### 🇰🇷 한국어 강의 가이드 및 핵심 요약
- **개요 요약:** 서로 다른 분모의 덧셈 $\\frac{3}{5} + \\frac{1}{4}$ 및 최소공분모(LCD=20) 변환
- **핵심 티칭 포인트:** 통분 후 분모끼리는 더하지 않고 분자만 합산한다는 기본 원칙 재확인

---

## Slide 04: Subtracting Fractions with Shared Multiples ($\\frac{3}{4} - \\frac{5}{12}$)
**Slide Type:** Single Problem Master Breakdown  
**Workbook Source:** Section 1.0 Board Work #4 (Workbook p. 4)  
**LaTeX Anchor:** $\\dfrac{3}{4} - \\dfrac{5}{12}$

### 📝 Problem Statement
$$\\text{Simplify into simplest fraction form: } \\quad \\dfrac{3}{4} - \\dfrac{5}{12}$$

### 💡 AI Step-by-Step Solution Breakdown
$$\\begin{aligned}
\\text{Step 1: } & \\text{Find LCD of 4 and 12:} \\\\
& 12 \\text{ is already a multiple of 4 } (4 \\cdot 3 = 12) \\implies \\mathbf{\\text{LCD} = 12} \\\\[0.5em]
\\text{Step 2: } & \\text{Convert only the first fraction:} \\\\
& \\left(\\dfrac{3}{4} \\cdot \\dfrac{3}{3}\\right) - \\dfrac{5}{12} = \\dfrac{9}{12} - \\dfrac{5}{12} \\\\[0.5em]
\\text{Step 3: } & \\text{Subtract numerators:} \\\\
& \\dfrac{9 - 5}{12} = \\dfrac{4}{12} \\\\[0.5em]
\\text{Step 4: } & \\text{Reduce to simplest terms by dividing top and bottom by 4:} \\\\
& \\dfrac{4 \\div 4}{12 \\div 4} = \\mathbf{\\dfrac{1}{3}}
\\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Look at Slide 4: $\\frac{3}{4} - \\frac{5}{12}$. Sora, do we need to multiply $4 \\times 12$ to get 48?

[TA Sora] No! Please don't! That creates huge numbers that you have to reduce later. Always look to see if the larger denominator is already a multiple of the smaller one! 12 is already a multiple of 4!

[Prof. Park] That's a great time-saver. So our LCD is simply 12. The second fraction already has 12, so it stays $\\frac{5}{12}$.

[TA Sora] We only change $\\frac{3}{4}$ by multiplying top and bottom by 3, which gives $\\frac{9}{12}$.

[Prof. Park] $9 - 5$ gives $4$, so we have $\\frac{4}{12}$. Are we done?

[TA Sora] Almost! Never walk away from a fraction without checking if it can be reduced! $4$ and $12$ both divide by $4$, giving us our final answer: $\\frac{1}{3}$.

### 🇰🇷 한국어 강의 가이드 및 핵심 요약
- **개요 요약:** 배수 관계 분모의 뺄셈 $\\frac{3}{4} - \\frac{5}{12}$과 약분(Simplification)
- **핵심 티칭 포인트:** 무조건 두 분모를 곱하지 않고 최소공배수를 선택하는 지혜와 기약분수 마무리 습관

---

## Slide 05: Order of Operations with Fraction Subtraction & Exponents ($(\\frac{4}{7} - \\frac{2}{3})^2$)
**Slide Type:** Multi-Step Problem Breakdown  
**Workbook Source:** Section 1.0 Board Work #5 (Workbook p. 4)  
**LaTeX Anchor:** $\\left(\\dfrac{4}{7} - \\dfrac{2}{3}\\right)^2$

### 📝 Problem Statement
$$\\text{Evaluate using order of operations: } \\quad \\left(\\dfrac{4}{7} - \\dfrac{2}{3}\\right)^2$$

### 💡 AI Step-by-Step Solution Breakdown
$$\\begin{aligned}
\\text{Step 1: } & \\text{PEMDAS requires evaluating inside Parentheses first:} \\\\
& \\text{LCD of 7 and 3 is } 21. \\\\
& \\dfrac{4}{7} \\cdot \\dfrac{3}{3} = \\dfrac{12}{21}, \\qquad \\dfrac{2}{3} \\cdot \\dfrac{7}{7} = \\dfrac{14}{21} \\\\[0.5em]
\\text{Step 2: } & \\text{Subtract inside the parentheses (notice the signed number!):} \\\\
& \\dfrac{12}{21} - \\dfrac{14}{21} = \\mathbf{-\\dfrac{2}{21}} \\\\[0.5em]
\\text{Step 3: } & \\text{Apply the Exponent of 2 to the resulting fraction:} \\\\
& \\left(-\\dfrac{2}{21}\\right)^2 = \\dfrac{(-2)^2}{(21)^2} = \\mathbf{\\dfrac{4}{441}}
\\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Problem #5 combines three skills: fractions, negative numbers, and exponents! Look at $(\\frac{4}{7} - \\frac{2}{3})^2$.

[TA Sora] Following PEMDAS, we must conquer the parentheses first! The LCD of 7 and 3 is 21.

[Prof. Park] That turns the problem into $\\frac{12}{21} - \\frac{14}{21}$. Now, Sora, what is $12 - 14$?

[TA Sora] It's negative 2! So inside the parentheses, we have $-\\frac{2}{21}$.

[Prof. Park] And now we square that entire quantity: $(-\\frac{2}{21})^2$. 

[TA Sora] And remember our rule from Lecture 01: A negative times a negative is POSITIVE! $(-2)^2 = +4$, and $21^2 = 441$. Result: positive $\\frac{4}{441}$!

[Prof. Park] Outstanding reasoning.

### 🇰🇷 한국어 강의 가이드 및 핵심 요약
- **개요 요약:** 괄호 안 분수 뺄셈 후 거듭제곱 $(\\frac{4}{7} - \\frac{2}{3})^2$ 단계별 연산
- **핵심 티칭 포인트:** 괄호 우선(P), 음수 분수 결과 도출, 음수의 짝수 거듭제곱 시 양수 부호 변환 확인

---

## Slide 06: Multiplying Small Unit Fractions ($\\frac{1}{9} \\cdot \\frac{1}{6}$)
**Slide Type:** Paired Concept Breakdown  
**Workbook Source:** Section 1.0 Board Work #6 (Workbook p. 4)  
**LaTeX Anchor:** $\\dfrac{1}{9} \\cdot \\dfrac{1}{6}$

### 📝 Problem Statement & Comparison
$$\\text{A. Multiply: } \\dfrac{1}{9} \\cdot \\dfrac{1}{6} \\qquad \\text{vs.} \\qquad \\text{B. Compare with Addition: } \\dfrac{1}{9} + \\dfrac{1}{6}$$

### 💡 AI Step-by-Step Solution Breakdown
$$\\begin{aligned}
\\text{Multiplication: } & \\dfrac{1}{9} \\cdot \\dfrac{1}{6} = \\dfrac{1 \\cdot 1}{9 \\cdot 6} = \\mathbf{\\dfrac{1}{54}} \\\\[0.5em]
\\text{Addition (for contrast): } & \\text{LCD of 9 and 6 is } 18 \\\\
& \\dfrac{2}{18} + \\dfrac{3}{18} = \\mathbf{\\dfrac{5}{18}}
\\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] On Slide 6, we have $\\frac{1}{9} \\cdot \\frac{1}{6}$. Students often ask: "Professor, do I need an LCD to multiply fractions?"

[TA Sora] And the answer is a giant, resounding **NO**! You NEVER need a common denominator to multiply!

[Prof. Park] That's right! Multiplication is the easiest fraction operation in the world: you just multiply straight across the top, and straight across the bottom.

[TA Sora] $1 \\times 1 = 1$, and $9 \\times 6 = 54$. Answer: $\\frac{1}{54}$. Done in five seconds!

[Prof. Park] Keep that distinction crystal clear: LCD is for addition and subtraction only!

### 🇰🇷 한국어 강의 가이드 및 핵심 요약
- **개요 요약:** 단위분수의 곱셈 $\\frac{1}{9} \\cdot \\frac{1}{6}$과 덧셈과의 구조적 차이 비교
- **핵심 티칭 포인트:** 곱셈 시에는 통분(LCD)이 전혀 필요 없이 분자·분모를 직진 곱셈함을 강조

---

## Slide 07: Dividing Fractions: The "Keep, Change, Flip" Rule ($\\frac{3}{8} \\div \\frac{1}{16}$)
**Slide Type:** Single Problem Master Breakdown  
**Workbook Source:** Section 1.0 Board Work #7 (Workbook p. 4)  
**LaTeX Anchor:** $\\dfrac{3}{8} \\div \\dfrac{1}{16}$

### 📝 Problem Statement
$$\\text{Perform the division: } \\quad \\dfrac{3}{8} \\div \\dfrac{1}{16}$$

### 💡 AI Step-by-Step Solution Breakdown
$$\\begin{aligned}
\\text{Step 1: } & \\text{Apply Keep, Change, Flip (Multiply by the Reciprocal):} \\\\
& \\text{KEEP the first fraction: } \\dfrac{3}{8} \\\\
& \\text{CHANGE } \\div \\text{ to } \\cdot \\\\
& \\text{FLIP the second fraction: } \\dfrac{1}{16} \\to \\dfrac{16}{1} \\\\[0.5em]
\\text{Step 2: } & \\text{Write as a single product: } \\dfrac{3}{8} \\cdot \\dfrac{16}{1} \\\\[0.5em]
\\text{Step 3: } & \\text{Cross-cancel the common factor of 8 before multiplying:} \\\\
& \\dfrac{3}{\\cancel{8}_1} \\cdot \\dfrac{\\cancel{16}_2}{1} = \\dfrac{3 \\cdot 2}{1 \\cdot 1} = \\mathbf{6}
\\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] Problem #7 introduces division: $\\frac{3}{8} \\div \\frac{1}{16}$. Sora, what is our famous mnemonic rhyme for dividing fractions?

[TA Sora] **Keep, Change, Flip!** 
- Keep the first fraction exactly as $\\frac{3}{8}$.
- Change division to multiplication.
- Flip the second fraction upside down into its reciprocal: $\\frac{16}{1}$!

[Prof. Park] And look at how easy it becomes: $\\frac{3}{8} \\cdot \\frac{16}{1}$. Before multiplying $3 \\times 16$, notice that 8 and 16 share a factor of 8!

[TA Sora] $16 \\div 8 = 2$, and $8 \\div 8 = 1$. So we just have $3 \\times 2 = 6$! 

[Prof. Park] Dividing by $\\frac{1}{16}$ means asking: "How many sixteenths fit inside $\\frac{3}{8}$?" Exactly 6 of them!

### 🇰🇷 한국어 강의 가이드 및 핵심 요약
- **개요 요약:** 분수의 나눗셈 $\\frac{3}{8} \\div \\frac{1}{16}$과 역수 곱셈(Keep, Change, Flip)
- **핵심 티칭 포인트:** 나눗셈을 역수의 곱셈으로 바꾸고, 곱하기 전 약분(Cross-Cancel)하여 계산 간소화

---

## Slide 08: Complex Fractions & Pre-simplifying Factors ($\\frac{5/8}{3/4}$ and $\\frac{(16)(3)}{(9)(4)}$)
**Slide Type:** Paired Problem Breakdown  
**Workbook Source:** Section 1.0 Board Work #8 & #10 (Workbook p. 4)  
**LaTeX Anchor:** \\dfrac{5/8}{3/4} \\quad \\text{and} \\quad \\dfrac{(16)(3)}{(9)(4)}

### 📝 Problem Statements
$$\\text{A. Simplify the complex fraction: } \\dfrac{\\ \\frac{5}{8}\\ }{\\frac{3}{4}} \\qquad \\text{B. Simplify: } \\dfrac{(16)(3)}{(9)(4)}$$

### 💡 AI Step-by-Step Solution Breakdown
$$\\begin{aligned}
\\text{Part A: } & \\dfrac{\\ \\frac{5}{8}\\ }{\\frac{3}{4}} = \\dfrac{5}{8} \\div \\dfrac{3}{4} = \\dfrac{5}{\\cancel{8}_2} \\cdot \\dfrac{\\cancel{4}_1}{3} = \\mathbf{\\dfrac{5}{6}} \\\\[1em]
\\text{Part B: } & \\dfrac{(16)(3)}{(9)(4)} = \\dfrac{\\cancel{16}_4 \\cdot \\cancel{3}_1}{\\cancel{9}_3 \\cdot \\cancel{4}_1} = \\mathbf{\\dfrac{4}{3}}
\\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] On Slide 8, we look at complex fractions like $\\frac{5/8}{3/4}$. Don't let the multi-story fraction bar intimidate you!

[TA Sora] The main fraction bar in the middle just means "divided by"! So it’s literally $\\frac{5}{8} \\div \\frac{3}{4}$.

[Prof. Park] And applying Keep-Change-Flip gives $\\frac{5}{8} \\times \\frac{4}{3}$. Cross-canceling 4 and 8 gives $\\frac{5}{6}$!

[TA Sora] And for Part B: $\\frac{(16)(3)}{(9)(4)}$, please don't multiply out to get $\\frac{48}{36}$ first! Cancel the 16 and 4 to get 4, and cancel the 3 and 9 to get 3! You immediately get $\\frac{4}{3}$ without doing big arithmetic!

[Prof. Park] Work smarter, not harder.

### 🇰🇷 한국어 강의 가이드 및 핵심 요약
- **개요 요약:** 번분수(Complex Fraction) 해석과 거대 곱셈 전 사전 약분 기법
- **핵심 티칭 포인트:** 번분수는 가운데 분수 바를 나눗셈 기호로 치환하면 간단한 나눗셈으로 환원됨

---

## Slide 09: Mixed Order of Operations ($16 - \\frac{3}{4} + 9$) & Sora's Fraction Mastery Takeaway
**Slide Type:** Problem Breakdown & Conclusion  
**Workbook Source:** Section 1.0 Board Work #9 (Workbook p. 4)  
**LaTeX Anchor:** 16 - \\dfrac{3}{4} + 9

### 📝 Problem Statement & Solution
$$\\begin{aligned}
\\text{Evaluate: } & 16 - \\dfrac{3}{4} + 9 \\\\[0.5em]
\\text{Step 1: } & \\text{Group whole numbers first using associative/commutative properties:} \\\\
& (16 + 9) - \\dfrac{3}{4} = 25 - \\dfrac{3}{4} \\\\[0.5em]
\\text{Step 2: } & \\text{Convert 25 into fourths: } 25 = \\dfrac{100}{4} \\\\[0.5em]
\\text{Step 3: } & \\text{Subtract: } \\dfrac{100}{4} - \\dfrac{3}{4} = \\mathbf{\\dfrac{97}{4}} \\quad \\left(\\text{or } 24\\dfrac{1}{4}\\right)
\\end{aligned}$$

### 🎙️ English Lecture Script
[Prof. Park] To wrap up Lecture 02, look at $16 - \\frac{3}{4} + 9$. You can convert everything to fourths right away, or add the integers first: $16 + 9 = 25$.

[TA Sora] And $25 - \\frac{3}{4}$ is just 24 and one-quarter, or $\\frac{97}{4}$!

[Prof. Park] Today we took the fear out of fractions. You now have the exact computational fluency needed for algebraic expressions.

[TA Sora] Next time in Lecture 03, we begin Section 1.1: evaluating algebraic formulas with variables and exponents! See you then!
"""

with open(os.path.join(output_dir, "lecture02.md"), "w", encoding="utf-8") as f:
    f.write(lecture02_content)

print("Generated lecture02.md successfully.")
