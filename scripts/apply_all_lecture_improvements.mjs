import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const baseDir = path.resolve(__dirname, '..');
const filePath = path.join(baseDir, 'src/data/montanaSlidesData.js');

let content = fs.readFileSync(filePath, 'utf-8');

// 1. L01 S01 problem format update
const l01_s01_old = `"problem": "$$\\\\mathbf{M090\\\\text{ Introductory Algebra} \\\\quad \\\\bullet \\\\quad \\\\text{Montana State University}}$$\\n- **Instructional Team:** Prof. Eunju Park (Lead Instructor) & TA Sora (Gallatin College)\\n- **Teaching Philosophy:** Banish math anxiety through conceptual understanding and practical modeling.\\n- **The Golden Rule:** **One Problem = One Slide** (Zero clutter, 100% step-by-step clarity).\\n- **Course Materials:** Gallatin College M090 Student Notes Packet (Section 1.0, Page 3)."`;

const l01_s01_new = `"problem": "**Course Orientation:** Introductory Algebra at Gallatin College MSU\\n\\n$$\\\\mathbf{M090\\\\text{ Introductory Algebra} \\\\quad \\\\bullet \\\\quad \\\\text{Montana State University}}$$\\n\\n- **Instructional Team:** Prof. Eunju Park (Lead Instructor) & TA Sora (Gallatin College)\\n- **Teaching Philosophy:** Banish math anxiety through conceptual understanding and practical modeling.\\n- **The Golden Rule:** **One Problem = One Slide** (Zero clutter, 100% step-by-step clarity).\\n- **Course Materials:** Gallatin College M090 Student Notes Packet (Section 1.0, Page 3)."`;

if (content.includes(l01_s01_old)) {
  content = content.replace(l01_s01_old, l01_s01_new);
  console.log('Fixed L01 S01');
} else {
  console.log('L01 S01 target not matched, checking regex...');
}

// 2. L03 S01, S08, S09 problem content
const l03_s01_old = `    "num": 1,
    "type": "math_problem",
    "slideTypeLabel": "Lecture Orientation",
    "title": "Welcome to Lecture 03: The Magic of Substitution",
    "subtitle": "Unit 1 • Lecture 03 • Unit 1 • Lecture 03",
    "detail": "Lecture 03: Evaluating Algebraic Expressions with Signed Numbers",
    "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    "problem": "",`;

const l03_s01_new = `    "num": 1,
    "type": "math_problem",
    "slideTypeLabel": "Lecture Orientation",
    "title": "Welcome to Lecture 03: The Magic of Substitution",
    "subtitle": "Unit 1 • Lecture 03 • Section 1.1 Overview (Workbook p. 6)",
    "detail": "Lecture 03: Evaluating Algebraic Expressions with Signed Numbers",
    "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    "problem": "**Section 1.1 Evaluating Algebraic Expressions with Signed Numbers**\\n\\n- **Focus:** Replacing variable placeholders with real signed numbers.\\n- **Golden Protocol:** The \\"Empty Pockets\\" Protective Parentheses Rule.\\n- **Course Workbook:** Gallatin College M090 Student Notes Packet (Section 1.1, Page 6).",`;

if (content.includes(l03_s01_old)) {
  content = content.replace(l03_s01_old, l03_s01_new);
  console.log('Fixed L03 S01');
}

const l03_s08_old = `    "num": 8,
    "type": "math_problem",
    "slideTypeLabel": "Study Skills & Technology",
    "title": "Calculator Pitfalls vs. Paper Algebra",
    "subtitle": "Unit 1 • Lecture 03 • Unit 1 • Lecture 03",
    "detail": "Lecture 03: Evaluating Algebraic Expressions with Signed Numbers",
    "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    "problem": "",
    "solution": "",
    "pitfall": "",`;

const l03_s08_new = `    "num": 8,
    "type": "math_problem",
    "slideTypeLabel": "Study Skills & Technology",
    "title": "Calculator Pitfalls vs. Paper Algebra",
    "subtitle": "Unit 1 • Lecture 03 • Section 1.1 Study Skills (Workbook p. 6)",
    "detail": "Lecture 03: Evaluating Algebraic Expressions with Signed Numbers",
    "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    "problem": "**Calculator Pitfalls vs. Paper Algebra Analysis:**\\n\\n- **The Pitfall:** Entering $-4^2$ into a calculator yields $-16$ because exponentiation takes precedence over unary negation.\\n- **The Solution:** Always input with protective parentheses: $(-4)^2 = +16$.\\n- **Best Practice:** Perform structural algebra by hand on paper; use technology only for arithmetic verification.",
    "solution": "$$\\\\mathbf{\\\\text{Paper Algebra Guarantee: Parentheses First } \\\\implies (-4)^2 = 16, \\\\quad -(4^2) = -16}$$",
    "pitfall": "**TECHNOLOGY TRAP:** Never trust a screen that interprets $-4^2$ without asking what base YOU intended!",`;

if (content.includes(l03_s08_old)) {
  content = content.replace(l03_s08_old, l03_s08_new);
  console.log('Fixed L03 S08');
}

const l03_s09_old = `    "num": 9,
    "type": "math_problem",
    "slideTypeLabel": "Conclusion & Summary",
    "title": "Lecture 03 Wrap-Up & Sora's Substitution Checklist",
    "subtitle": "Unit 1 • Lecture 03 • Unit 1 • Lecture 03",
    "detail": "Lecture 03: Evaluating Algebraic Expressions with Signed Numbers",
    "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    "problem": "",
    "solution": "",
    "pitfall": "",`;

const l03_s09_new = `    "num": 9,
    "type": "math_problem",
    "slideTypeLabel": "Conclusion & Summary",
    "title": "Lecture 03 Wrap-Up & Sora's Substitution Checklist",
    "subtitle": "Unit 1 • Lecture 03 • Section 1.1 Summary (Workbook p. 6)",
    "detail": "Lecture 03: Evaluating Algebraic Expressions with Signed Numbers",
    "instructor": "Prof. Eunju Park • TA Sora (Gallatin College MSU)",
    "problem": "**Sora's Substitution Checklist & Wrap-Up (Workbook p. 6):**\\n\\n1. **Empty Pockets:** Erase variable letters and replace with empty parentheses $(\\\\;)$.\\n2. **Even vs. Odd Negatives:** Even powers of negatives are positive: $(-a)^2 = a^2$.\\n3. **Sign Counting:** Count negative factors in products: even number yields positive, odd number yields negative.\\n4. **Next Lecture Preview:** Section 1.1 Part 2 — Translating English Phrases to Algebra.",
    "solution": "$$\\\\mathbf{\\\\text{Mastery Complete: Empty Pockets Parentheses Rule Unlocks 100\\\\% Accuracy!}}$$",
    "pitfall": "**Sora's Pro-Tip:** Complete Workbook Page 7 practice drills tonight to cement your substitution reflexes!",`;

if (content.includes(l03_s09_old)) {
  content = content.replace(l03_s09_old, l03_s09_new);
  console.log('Fixed L03 S09');
}

// 3. L03 S03 to S07 2-line problems
const l03_replacements = [
  {
    old: `"problem": "$$\\\\text{Evaluate for } d = -2 \\\\text{ and } f = 5: \\\\quad \\\\dfrac{d^2 - f^2}{d^2 + f^2}$$"`,
    new: `"problem": "**Example 1 (Workbook p. 6):** Evaluate for $d = -2$ and $f = 5$:\\n\\n$$\\\\mathbf{\\\\dfrac{d^2 - f^2}{d^2 + f^2}}$$"`
  },
  {
    old: `"problem": "$$\\\\text{Evaluate if } x = -1, \\\\ y = -3, \\\\ z = 2: \\\\quad \\\\dfrac{2x^2 + y^2}{|-10 + z^3|}$$"`,
    new: `"problem": "**Example 2 (Workbook p. 6):** Evaluate if $x = -1, \\\\ y = -3, \\\\ z = 2$:\\n\\n$$\\\\mathbf{\\\\dfrac{2x^2 + y^2}{|-10 + z^3|}}$$"`
  },
  {
    old: `"problem": "$$\\\\text{For } a = 5, \\\\ b = -6, \\\\ c = -3, \\\\text{ evaluate: } \\\\quad b^2 - 4ac$$"`,
    new: `"problem": "**Example 3 (Workbook p. 6):** For $a = 5, \\\\ b = -6, \\\\ c = -3$, evaluate the discriminant:\\n\\n$$\\\\mathbf{b^2 - 4ac}$$"`
  },
  {
    old: `"problem": "$$\\\\text{Given } a = 1, \\\\ b = 7, \\\\ c = -6, \\\\text{ find: } \\\\quad \\\\dfrac{-b + \\\\sqrt{b^2 - 4ac}}{2a}$$"`,
    new: `"problem": "**Example 4 (Workbook p. 6):** Given $a = 1, \\\\ b = 7, \\\\ c = -6$, find:\\n\\n$$\\\\mathbf{\\\\dfrac{-b + \\\\sqrt{b^2 - 4ac}}{2a}}$$"`
  },
  {
    old: `"problem": "$$\\\\text{Evaluate for } a = 2, \\\\ b = -10, \\\\ c = 8: \\\\quad \\\\dfrac{-b + \\\\sqrt{b^2 - 4ac}}{2a}$$"`,
    new: `"problem": "**Example 5 (Workbook p. 6):** Evaluate for $a = 2, \\\\ b = -10, \\\\ c = 8$:\\n\\n$$\\\\mathbf{\\\\dfrac{-b + \\\\sqrt{b^2 - 4ac}}{2a}}$$"`
  }
];

for (const r of l03_replacements) {
  if (content.includes(r.old)) {
    content = content.replace(r.old, r.new);
    console.log('Applied L03 replacement');
  } else {
    console.log('Failed to match L03 replacement:', r.old.slice(0, 40));
  }
}

// 4. L05 S06, S07, S08, S09, S10
const l05_replacements = [
  {
    old: `"problem": "$$\\\\text{Example 3: Fully simplify using only positive integer exponents (Workbook p. 9): } \\\\quad \\\\dfrac{r^{10}}{r^2}$$"`,
    new: `"problem": "**Example 3 Part A (Workbook p. 9):** Fully simplify using only positive integer exponents:\\n\\n$$\\\\mathbf{\\\\dfrac{r^{10}}{r^2}}$$"`
  },
  {
    old: `"problem": "$$\\\\text{Example 3 Part B: Fully simplify (Workbook p. 9): } \\\\quad \\\\dfrac{2m^2}{5n^3} \\\\cdot \\\\dfrac{10n^5}{m^3}$$"`,
    new: `"problem": "**Example 3 Part B (Workbook p. 9):** Fully simplify:\\n\\n$$\\\\mathbf{\\\\dfrac{2m^2}{5n^3} \\\\cdot \\\\dfrac{10n^5}{m^3}}$$"`
  },
  {
    old: `"problem": "$$\\\\text{Example 3 Part C: Fully simplify (Workbook p. 10): } \\\\quad \\\\dfrac{2m^2}{5n^3} \\\\div \\\\dfrac{10n^5}{m^3}$$"`,
    new: `"problem": "**Example 3 Part C (Workbook p. 10):** Fully simplify:\\n\\n$$\\\\mathbf{\\\\dfrac{2m^2}{5n^3} \\\\div \\\\dfrac{10n^5}{m^3}}$$"`
  },
  {
    old: `"problem": "$$\\\\text{Example 3 Part D: Fully simplify (Workbook p. 10): } \\\\quad \\\\dfrac{8x^9 y^8 z^5}{12x^4 y^{12} z^0}$$"`,
    new: `"problem": "**Example 3 Part D (Workbook p. 10):** Fully simplify:\\n\\n$$\\\\mathbf{\\\\dfrac{8x^9 y^8 z^5}{12x^4 y^{12} z^0}}$$"`
  },
  {
    old: `"problem": "$$\\\\text{Upcoming in Lecture 06: Negative Exponents \\\\& Power Rules (Workbook pp. 10-11)}$$\\n- **Next Class:** We conquer **Example 4 (Parts A through F)** and **Example 5 (Parts A through F)**.\\n- **Workbook Preview:**\\n  - Moving negative exponents using the **Elevator Metaphor** ($12x^{-4}, 3a^{-2}b^9$).\\n  - Fraction negative powers like $(5/8)^{-2}$ and $(4y)^{-3}$.\\n  - Compound power rules like $(5x^4)^2$ and $\\\\left(\\\\frac{3x^{11}y^5}{2x^{-1}y^8}\\\\right)\\\\left(\\\\frac{2x^5 y^{12}}{5x}\\\\right)$."`,
    new: `"problem": "**Upcoming in Lecture 06: Negative Exponents & Power Rules (Workbook pp. 10–11)**\\n\\n- **Next Class:** We conquer **Example 4 (Parts A through F)** and **Example 5 (Parts A through F)**.\\n- **Workbook Preview:**\\n  - Moving negative exponents using the **Elevator Metaphor** ($12x^{-4}, 3a^{-2}b^9$).\\n  - Fraction negative powers like $(5/8)^{-2}$ and $(4y)^{-3}$.\\n  - Compound power rules like $(5x^4)^2$ and $\\\\left(\\\\frac{3x^{11}y^5}{2x^{-1}y^8}\\\\right)\\\\left(\\\\frac{2x^5 y^{12}}{5x}\\\\right)$."`
  }
];

for (const r of l05_replacements) {
  if (content.includes(r.old)) {
    content = content.replace(r.old, r.new);
    console.log('Applied L05 replacement');
  } else {
    console.log('Failed to match L05 replacement:', r.old.slice(0, 40));
  }
}

// 5. L06 S08, S09
const l06_replacements = [
  {
    old: `"problem": "$$\\\\text{Example 5 Part E: Simplify fully (Workbook p. 11): } \\\\quad \\\\left(\\\\dfrac{2x^6 w^5}{3x w^5}\\\\right)\\\\left(\\\\dfrac{7x^5 w^2}{9x^2}\\\\right)$$"`,
    new: `"problem": "**Example 5 Part E (Workbook p. 11):** Simplify fully:\\n\\n$$\\\\mathbf{\\\\left(\\\\dfrac{2x^6 w^5}{3x w^5}\\\\right)\\\\left(\\\\dfrac{7x^5 w^2}{9x^2}\\\\right)}$$"`
  },
  {
    old: `"problem": "$$\\\\text{Example 5 Part F: Simplify fully (Workbook p. 11): } \\\\quad \\\\left(\\\\dfrac{3x^{11}y^5}{2x^{-1}y^8}\\\\right)\\\\left(\\\\dfrac{2x^5 y^{12}}{5x}\\\\right)$$"`,
    new: `"problem": "**Example 5 Part F (Workbook p. 11):** Simplify fully:\\n\\n$$\\\\mathbf{\\\\left(\\\\dfrac{3x^{11}y^5}{2x^{-1}y^8}\\\\right)\\\\left(\\\\dfrac{2x^5 y^{12}}{5x}\\\\right)}$$"`
  }
];

for (const r of l06_replacements) {
  if (content.includes(r.old)) {
    content = content.replace(r.old, r.new);
    console.log('Applied L06 replacement');
  } else {
    console.log('Failed to match L06 replacement:', r.old.slice(0, 40));
  }
}

// 6. Remove the repetitive trailer blocks from L03, L04, L05, L06, L15, L45
const l03_trailer = `\\n\\n[Prof. Park] Think about physics and engineering here at Montana State: every computer model is running millions of these exact substitutions every second!\\n\\n[TA Sora] When you master substitution by hand with protective parentheses, you understand the logic that powers modern software and engineering design!\\n\\n[Prof. Park] Keep that principle close at hand as we move forward.\\n\\n[TA Sora] Absolutely, Professor! On to the next challenge!\\n\\n[Prof. Park] Notice how substituting numbers into algebraic expressions transforms an abstract formula into concrete reality. Always take that extra moment to double-check your arithmetic line by line!\\n\\n[TA Sora] Exactly, Professor! Whether you're calculating wind chill on the ski slopes or stress tolerances on a bridge, clean substitution habits guarantee you get the exact right number every time!`;

if (content.includes(l03_trailer)) {
  const count = content.split(l03_trailer).length - 1;
  content = content.replaceAll(l03_trailer, '');
  console.log(`Cleaned up L03 repetitive trailer (${count} occurrences removed)`);
}

const l04_trailer = `\\n\\n[Prof. Park] Notice how algebraic translation trains your brain to break down ambiguous human language into precise, logical components.\\n\\n[TA Sora] That skill goes way beyond mathematics: in law, computer programming, and business contracts, parsing exact meanings is everything!\\n\\n[Prof. Park] Keep that principle close at hand as we move forward.\\n\\n[TA Sora] Absolutely, Professor! On to the next challenge!\\n\\n[Prof. Park] When students encounter complex word problems on midterms, what is the best strategy to avoid feeling overwhelmed?\\n\\n[TA Sora] Read the sentence through three times! First for the story, second to circle the operation signal words, and third to write the algebraic symbols! Patience and method always win!`;

if (content.includes(l04_trailer)) {
  const count = content.split(l04_trailer).length - 1;
  content = content.replaceAll(l04_trailer, '');
  console.log(`Cleaned up L04 repetitive trailer (${count} occurrences removed)`);
}

const l05_trailer = `\\n\\n[Prof. Park] Why are exponent properties considered the backbone of higher mathematics, Sora?\\n\\n[TA Sora] Because without them, manipulating polynomials, scientific notation in astronomy, or compound interest formulas in finance would be completely impossible!\\n\\n[Prof. Park] Keep that principle close at hand as we move forward.\\n\\n[TA Sora] Absolutely, Professor! On to the next challenge!\\n\\n[Prof. Park] Think about scientific notation and computer memory: exponents allow engineers to describe microscopic nanometers and cosmic light years with equal precision!\\n\\n[TA Sora] That's why these foundational properties matter so much! When you know the product and quotient rules inside out, complicated algebra expressions simplify like clockwork!`;

if (content.includes(l05_trailer)) {
  const count = content.split(l05_trailer).length - 1;
  content = content.replaceAll(l05_trailer, '');
  console.log(`Cleaned up L05 repetitive trailer (${count} occurrences removed)`);
}

const l06_trailer = `\\n\\n[Prof. Park] Take your time with every step here. Writing out intermediate lines is the secret to 100% accuracy!\\n\\n[Prof. Park] Exactly! Protect your signs, trust the algebra rules, and you will get the correct answer every single time!`;

if (content.includes(l06_trailer)) {
  const count = content.split(l06_trailer).length - 1;
  content = content.replaceAll(l06_trailer, '');
  console.log(`Cleaned up L06 repetitive trailer (${count} occurrences removed)`);
}

fs.writeFileSync(filePath, content, 'utf-8');
console.log('Successfully written updated montanaSlidesData.js');
