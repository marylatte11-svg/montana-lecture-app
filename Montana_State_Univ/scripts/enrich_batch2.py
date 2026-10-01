# -*- coding: utf-8 -*-
import sys
import json
sys.path.append('Montana_State_Univ/scripts')
from unit1_scripts_l06_l08 import SCRIPTS_L06, SCRIPTS_L07, SCRIPTS_L08
from unit1_scripts_l09_l10 import SCRIPTS_L09, SCRIPTS_L10

L06_ADD = {
    6: (
        "\nProf. Park: In Bozeman's precision photonics sector, optical engineers calculate laser pulse frequencies where wavelengths scale as powers of 10 to the negative 6 meters. "
        "If an engineer forgets to distribute an outer negative power across numerical coefficients or drops an elevator sign, an entire optical sensor calibration is ruined!\n"
        "TA Sora: Exactly, Professor! That is why I always tell students: treat exponents like bank transaction entries. "
        "Every negative exponent is a pending wire transfer across the fraction bar line. Once it crosses over, the fee is paid and the sign becomes positive!"
    ),
    7: (
        "\nTA Sora: Here is an extra pro-tip for slide 7: whenever you have a fraction with multiple variables and coefficients raised to a negative power outside, "
        "you can also flip the ENTIRE fraction upside down right at the start to turn the outer exponent positive!\n"
        "Prof. Park: That is the Fraction Inversion Property: (A/B)^(-n) = (B/A)^n! "
        "In our problem, flipping the fraction first gives [ z^(-4) / (3 x^(-2) y) ]^3, which leads to the exact same final answer: x^6 / (27 y^3 z^12). "
        "Having two independent ways to solve a problem is the greatest confidence builder in algebra!"
    ),
    10: (
        "\nProf. Park: Let us also review the difference between (-x)^2 and -x^2 one last time before we leave exponents:\n"
        "TA Sora: In (-3)^2, the negative is inside parentheses, so (-3)(-3) = +9. "
        "In -3^2, the negative is OUTSIDE, so -(3)(3) = -9! Keep this distinction on a sticky note on your computer screen!"
    )
}

L07_ADD = {
    5: (
        "\nProf. Park: Think of residential construction framing across Bozeman and Belgrade: "
        "when contractors calculate structural perimeter lumber or roof truss dimensions with varying spans, variables represent modular lumber dimensions. "
        "Missing terms just mean zero length in that specific component—they do not vanish or break the formula!\n"
        "TA Sora: That is why I tell students to write in placeholder zeros if it helps them stay aligned on paper: write + 0x^3 as a placeholder column. "
        "That way, degree 4, 3, 2, 1, and 0 terms line up in neat vertical columns like an accounting ledger!"
    ),
    6: (
        "\nProf. Park: Multi-variable polynomials appear constantly in physics, such as calculating kinetic energy or heat dissipation across rectangular panels where length x and width y both vary simultaneously.\n"
        "TA Sora: And notice the order in each term: by mathematical convention, we write variable factors in alphabetical order: x before y, a before b. "
        "This makes spotting like terms instantaneous!"
    ),
    7: (
        "\nProf. Park: Let us emphasize one final time the difference between adding terms and multiplying terms:\n"
        "TA Sora: When adding like terms: 3x^2 + 5x^2 = 8x^2. The coefficients add, but the exponent NEVER changes! "
        "When multiplying: (3x^2)(5x^2) = 15x^4. The coefficients multiply and the exponents ADD! "
        "Confusing these two rules is the number one cause of lost points on Exam 1!"
    )
}

L08_ADD = {
    1: (
        "\nTA Sora: Imagine you are designing a high-performance energy-efficient modular home for a client building in the Bridger Foothills. "
        "If one room module has length (2x + 5) feet and width (3x - 4) feet, calculating the total square footage requires finding the product of those two binomials.\n"
        "Prof. Park: Every square foot of flooring, insulation, and solar radiant heating depends on correctly multiplying these algebraic dimensions! "
        "That is why polynomial multiplication is not an abstract puzzle—it is physical reality in construction and architecture."
    ),
    2: (
        "\nProf. Park: You can also visualize monomial multiplication as distributing paint across a series of connected rectangular rooms.\n"
        "TA Sora: That is a wonderful visual! 3x^2 is the height of the wall, and (4x^3 - 5x + 7) is the broken-up length of three adjoining rooms. "
        "The total area is the sum of the three individual room areas: 12x^5 - 15x^3 + 21x^2!"
    ),
    3: (
        "\nTA Sora: Here is a memory hook for FOIL: First, Outer, Inner, Last. "
        "Notice that Outer and Inner are the 'middle children' of the problem—they almost always share the exact same variable power and combine together into a single middle term!\n"
        "Prof. Park: But always be cautious with your signs: if the outer product is negative and the inner product is positive, you must add integers carefully: -10x + 12x = +2x."
    ),
    4: (
        "\nProf. Park: Let us draw the geometric area model for (3x + 4)^2: draw a large square of side length 3x + 4.\n"
        "TA Sora: Split each side into two segments: 3x and 4. That divides the large square into FOUR distinct rooms!\n"
        "One room is 3x by 3x = 9x^2.\n"
        "One room is 4 by 4 = 16.\n"
        "And there are TWO identical hallway rooms, each measuring 3x by 4 = 12x!\n"
        "The two hallway rooms together give 12x + 12x = 24x!\n"
        "If you forget the middle term, you are literally erasing two whole rooms from your house blueprint!"
    ),
    5: (
        "\nProf. Park: Notice why difference of squares is so unique: because the two middle terms are exact opposites (+35x and -35x), they cancel each other out completely!\n"
        "TA Sora: It is like paying 35 dollars and immediately receiving 35 dollars back—your net change is zero! "
        "That leaves only the square of the first term minus the square of the second term: 25x^2 - 49. "
        "Whenever you see conjugate binomials (A - B)(A + B), you can instantly write down A^2 - B^2!"
    ),
    6: (
        "\nTA Sora: When multiplying a binomial by a trinomial, I strongly recommend writing your work in a 2-by-3 grid or lining up like terms vertically:\n"
        "Row 1 from distributing 2x: 2x^3 + 8x^2 - 10x.\n"
        "Row 2 from distributing -3:       - 3x^2 - 12x + 15.\n"
        "Lining up the x^2 and x terms vertically makes combining them practically foolproof!\n"
        "Prof. Park: Vertical alignment prevents students from skipping terms or accidentally combining unlike powers. Neatness on paper translates directly into 100% test scores!"
    ),
    7: (
        "\nTA Sora: And here is a secret preview: in Chapter 2, we will do this exact process in REVERSE! Reversing multiplication is called FACTORING!\n"
        "Prof. Park: If you master FOIL and distribution today, factoring next week will feel completely natural and intuitive. Excellent work mastering polynomial multiplication!"
    )
}

L09_ADD = {
    1: (
        "\nTA Sora: In Gallatin Valley irrigation management, ditch riders control the flow of water to alfalfa fields and cattle pastures. "
        "If headgate A delivers flow at rate 5/(6x^2) and headgate B delivers flow at rate 3/(8x), you cannot simply add the 5 and 3 to get 8, and add the denominators to get 14x^3!\n"
        "Prof. Park: That would be like adding two fractions with different units without converting them first! "
        "In physics and engineering, you must find a common standard unit before combining rates. In algebra, that common unit is the Least Common Denominator."
    ),
    2: (
        "\nTA Sora: Let us review the golden arithmetic rule: A/C + B/C = (A + B)/C. Notice that the denominator C is the denominator of the answer!\n"
        "Prof. Park: If you have quarters, 1 quarter plus 2 quarters is 3 quarters, not 3 eighths! Denominators name the fraction unit; numerators count the units."
    ),
    3: (
        "\nProf. Park: Let us review why we take the HIGHEST power of each variable when finding the LCD:\n"
        "TA Sora: Think of packing luggage for a camping trip in Yellowstone: if one person brings a 2-person tent (x^2) and another brings a 5-person tent (x^5), "
        "your car trunk (the LCD) must be big enough to fit the 5-person tent! If it fits the 5-person tent, it easily fits the 2-person tent with space to spare. "
        "That is why the LCD always takes the highest exponent of every variable factor!"
    ),
    4: (
        "\nProf. Park: Let us highlight the algebraic malpractice warning again: why does (9x + 20) / (24x^2) NOT simplify by cancelling x?\n"
        "TA Sora: Let us test it with a simple number! Suppose x = 2.\n"
        "Then the numerator is 9(2) + 20 = 18 + 20 = 38.\n"
        "The denominator is 24(2^2) = 24(4) = 96.\n"
        "38/96 reduces to 19/48.\n"
        "If a student illegally cancelled the x, they would get (9 + 20)/(24 · 2) = 29/48, which is completely different from 19/48!\n"
        "Numbers never lie. You can only cancel common FACTORS that multiply the entire numerator and denominator, never terms attached by plus or minus!"
    ),
    5: (
        "\nTA Sora: Notice the beauty of our final fraction in Example 3: (21b - 4a^2) / (30 a^3 b^2).\n"
        "Could we cancel the b in 21b with b^2 in the denominator?\n"
        "Prof. Park: No! Because the term -4a^2 does not have a b! If a factor is not shared by EVERY term in the numerator, it cannot be cancelled!\n"
        "TA Sora: That is the ironclad rule of rational expressions: all terms in the numerator must share the factor before anything can cancel across the fraction bar!"
    )
}

L10_ADD = {
    1: (
        "\nTA Sora: Culvert hydraulics under mountain passes like Bozeman Pass or Reynolds Pass along the Madison River deal with turbulent water flow during spring snowmelt. "
        "If an engineer models outflow rates with composite rational expressions, every single minus sign represents back-pressure or friction loss.\n"
        "Prof. Park: Misplacing a single minus sign turns a subtraction into an addition, predicting double drainage when in fact water is backing up! "
        "That is why civil engineers and algebra students alike treat binomial numerators with absolute structural respect."
    ),
    2: (
        "\nTA Sora: Here is my personal study tip for workbook page 17: whenever you see a problem like (A + B)/C - (D + E)/C, draw bright red parentheses around (D + E) before you write another stroke of your pencil!\n"
        "Prof. Park: That single second of drawing protective parentheses eliminates 90% of all student errors on rational expression exams. "
        "Notice also why factoring out the greatest common factor in the numerator is essential: in (4x - 4)/(4x), 4 is a common factor of BOTH terms upstairs. "
        "Factoring gives 4(x - 1). That allows the 4 to cancel with the 4 downstairs. If a student simply crosses out the 4x in the front, they leave -4 behind with no denominator, which is an algebraic catastrophe!\n"
        "TA Sora: Always factor before you cancel! No factoring, no cancelling! That is our golden motto!"
    ),
    3: (
        "\nProf. Park: Look closely at how we simplified (3x + 6) / (3x^2) on slide 3:\n"
        "TA Sora: Notice that we factored out 3 from BOTH terms in the numerator: 3(x + 2).\n"
        "Because 3 is multiplied by (x + 2), 3 is a FACTOR!\n"
        "And 3 in the denominator is also a FACTOR!\n"
        "Now—and ONLY now—can the 3 cancel top and bottom, leaving (x + 2) / (x^2)!\n"
        "Factoring first is the only legal ticket to cancelling in rational expressions!"
    ),
    4: (
        "\nProf. Park: On slide 4, look at the distribution of scaling factors: when multiplying (x + 3) by 3, you must distribute 3 to BOTH x and 3: 3x + 9!\n"
        "TA Sora: And when multiplying (2x - 1) by 2, you must distribute 2 to BOTH 2x and -1: 4x - 2!\n"
        "Never leave a term behind when building equivalent fractions upstairs!\n"
        "Prof. Park: In Example 3C, notice the factored form of the final answer: 7(x + 1) / (12x). On exams, both 7(x + 1)/(12x) and (7x + 7)/(12x) are 100% acceptable. "
        "Factoring out the 7 lets you quickly check whether anything can cancel with the denominator 12x. "
        "Since 7 shares no common factor with 12, and (x + 1) does not cancel with x, you know the fraction is irreducible!\n"
        "TA Sora: That is why factoring your final answer gives you an instant built-in correctness check!"
    ),
    5: (
        "\nProf. Park: Let us review the test value check on slide 5: why is plugging in x = 1 such an incredible strategy?\n"
        "TA Sora: On an exam, you don't have an answer key in the back of the book. But by spending 30 seconds plugging in x = 1 into both the original problem and your simplified answer, "
        "if the two values match, you know with 100% mathematical certainty that your answer is correct! It gives you total peace of mind before turning in your exam paper.\n"
        "Prof. Park: Remember that the negative sign applies to the ENTIRE quantity (5x + 9), so both signs flip: -5x - 9! That gives -10 - 9 = -19. "
        "If you got -1, you forgot to distribute the negative sign! Always double-check every sign distribution!"
    ),
    6: (
        "\nTA Sora: Let us review the full 4-step checklist for adding and subtracting rational expressions:\n"
        "1. Wrap all binomial numerators in protective parentheses!\n"
        "2. Find the LCD of all denominators (LCM of numbers, highest power of variables).\n"
        "3. Scale each fraction top and bottom by its missing factors.\n"
        "4. Distribute and combine like terms over the single LCD, and factor to check for final simplification!\n"
        "Prof. Park: With that checklist, you are fully equipped for any rational expression problem. We look forward to seeing you in Lecture 11 for linear equations!"
    )
}

# Apply additions
for slide, add_text in L06_ADD.items():
    k = str(slide)
    SCRIPTS_L06[k] = SCRIPTS_L06[k] + add_text

for slide, add_text in L07_ADD.items():
    k = str(slide)
    SCRIPTS_L07[k] = SCRIPTS_L07[k] + add_text

for slide, add_text in L08_ADD.items():
    k = str(slide)
    SCRIPTS_L08[k] = SCRIPTS_L08[k] + add_text

for slide, add_text in L09_ADD.items():
    k = str(slide)
    SCRIPTS_L09[k] = SCRIPTS_L09[k] + add_text

for slide, add_text in L10_ADD.items():
    k = str(slide)
    SCRIPTS_L10[k] = SCRIPTS_L10[k] + add_text

# Write updated files
with open('Montana_State_Univ/scripts/unit1_scripts_l06_l08.py', 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n')
    f.write('"""\nunit1_scripts_l06_l08.py\nHigh-volume 20-25 minute broadcast tiki-taka scripts for Lectures 06, 07, and 08.\n"""\n\n')
    f.write('SCRIPTS_L06 = ' + json.dumps(SCRIPTS_L06, indent=4, ensure_ascii=False) + '\n\n')
    f.write('SCRIPTS_L07 = ' + json.dumps(SCRIPTS_L07, indent=4, ensure_ascii=False) + '\n\n')
    f.write('SCRIPTS_L08 = ' + json.dumps(SCRIPTS_L08, indent=4, ensure_ascii=False) + '\n')

with open('Montana_State_Univ/scripts/unit1_scripts_l09_l10.py', 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n')
    f.write('"""\nunit1_scripts_l09_l10.py\nHigh-volume 20-25 minute broadcast tiki-taka scripts for Lectures 09 and 10.\n"""\n\n')
    f.write('SCRIPTS_L09 = ' + json.dumps(SCRIPTS_L09, indent=4, ensure_ascii=False) + '\n\n')
    f.write('SCRIPTS_L10 = ' + json.dumps(SCRIPTS_L10, indent=4, ensure_ascii=False) + '\n')

print('Enrichment complete.')
