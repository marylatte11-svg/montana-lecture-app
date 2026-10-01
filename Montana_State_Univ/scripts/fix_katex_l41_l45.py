"""
fix_katex_l41_l45.py
Fixes KaTeX errors introduced in unit3_data_l41_l45.py within montanaSlidesData.js:
1. Removes \( \) inline math delimiters used inside $$ blocks (causes parse errors)
2. Fixes __ underscores in math mode
3. Removes ✓ characters from math contexts
"""

import re
import os

data_file = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'data', 'montanaSlidesData.js'))

with open(data_file, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original size: {len(content):,} bytes")
original = content

# The issue: in the JS strings (after JSON serialization by to_js),
# \( and \) become \\( and \\) which when rendered as JS is \( and \).
# The validator strips $$ markers and then sees \( inside and complains.
# Fix: these are in SLIDES_MONTANA_L41 through L45 export sections.
# We need to find fields like "problem": "...\\(...\\)..." and convert.
# The JSON strings have \( rendered as \\( in the JS file.

# The errors show patterns like:
# "Identify: \\(a = 1,\\; b = -17..." - inline \( used in a non-$$ context - these are actually FINE
# The validator parses ALL $$ blocks and ALL \( \) as math.
# Looking at the error: "Can't use function '\(' in math mode" - this means
# there's a $$ block that CONTAINS \( which KaTeX treats as nested and fails.

# Strategy: in the problematic slides, make sure no $$ block contains \(
# The issue is strings like: "$$...\\( ... \\)..." 

# Let's look at specific patterns from errors:
# "**x-intercepts:** \\((9,0)\\) and \\((8,0)\\)" - These are in $$ solution blocks
# The solution fields start with $$ and then have \( \) inside

# The fix: Move \( \) items OUT of $$ blocks, or replace $$ blocks with the content directly
# Simpler: Replace \( and \) with just the content (remove the delimiters)

# In JS strings: \\( becomes \( in actual string, which is what KaTeX sees
# Fix: replace \\\\( with just ( in non-$$ contexts, OR
# Better: in strings that mix $$ and \\( \\), separate them

# Actually the real fix is: the validator is reading $$ blocks and within those
# finding \( which confuses it. But in reality the markdown renderer processes
# $$ blocks separately from \( \) blocks. The validator may be overly strict.

# Let's check what the actual render does - the issue is in the PROBLEM field
# where we have mixed content like:
# "**Identify:** \\(a = 1,\\; b = -17,\\; c = 72\\)\n\nApply the Quadratic Formula:\n$$x = ...$$"
# This is actually valid markdown + LaTeX but the validator strips all text and 
# finds the \( inside what it thinks is a $$ block context.

# The simplest fix: In slide problem/solution, avoid using \( \) inline math.
# Use just plain text or $...$ single dollar signs instead.

# Let's do targeted replacements in L41-L45 sections:

def fix_inline_in_l41_l45(content):
    """Fix specific KaTeX issues in L41-L45 slides."""
    
    # Find start of L41 slides section
    l41_start = content.find('export const SLIDES_MONTANA_L41')
    if l41_start == -1:
        print("ERROR: Could not find SLIDES_MONTANA_L41")
        return content
    
    # Get the portion from L41 onwards (up to end of MONTANA_ALL_SLIDES)
    suffix_start = content.find('export const MONTANA_ALL_SLIDES', l41_start)
    
    before = content[:l41_start]
    middle = content[l41_start:suffix_start]
    after = content[suffix_start:]
    
    # In the middle section, fix issues:
    # 1. Replace \\( ... \\) inline math with $...$ 
    #    In JS string: \\( becomes \\( in file = \( when parsed
    #    We want to replace \\\\( with $ and \\\\) with $
    
    # The file has literal text like: \\\\(a = 1\\\\)
    # Which in JS string becomes: \\(a = 1\\)
    # Which KaTeX sees as: \(a = 1\)
    # The fix is to use: $a = 1$
    
    # Pattern in file: \\( ... \\) -> convert to $ ... $
    # But \\\\ in file = \\ in JS = \ which means \\( = \( in JS
    
    # Let's just do string replacement at the file level:
    # \\\\( -> $ and \\\\) -> $  -- NO this is wrong
    
    # The file contains: "\\(a = 1" as literal characters \(a = 1 in the string
    # Let's count: in Python source we wrote \\( which in the string is \(
    # When to_js encodes it: \( -> \\( in JS file
    # So in the JS file we see: \\(
    
    # The validator reads the JS file and sees \\( and interprets it as \( LaTeX
    # Within a $$ block, KaTeX sees \( and fails.
    
    # Fix in the JS file: \\( -> $ and \\) -> $
    # But we need to be careful - $$ blocks should not be broken
    
    # Actually the validator error says:
    # "Can't use function '\(' in math mode at position 11: Identify: \(a = 1..."
    # This suggests the WHOLE text including "Identify: \(..." is being parsed as math
    # which means the $$ block is not closed before the \( appears
    
    # Let me look at actual slide content more carefully...
    # The problem field in L41 slide 2:
    # "**Step 1 — Identify x-intercepts:** Set \\(g(x) = 0\\)\n$$x^2 - 17x + 72 = 0$$\n\nIdentify: \\(a = 1,\\; b = -17,\\; c = 72\\)\n\nApply the Quadratic Formula:\n$$x = \\dfrac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$"
    
    # The validator sees text -> $$ block (x^2...) -> text -> $$ block (quadratic formula)
    # But the Identify: \(a = 1...\) line has \( after the first $$ closes
    # Wait - maybe the validator sees: "$$x^2...0$$\n\nIdentify: \\(a..." 
    # and the $$ closes, then outside math we have \\( which is fine
    # But then "Apply...$$x =..." opens another $$ 
    # Hmm, validator may not properly handle the \( outside $$
    
    # The real issue may be that the validator splits on $$ and sees the \\( as part of math
    # Let's replace \\( and \\) with just their content (no delimiters) in text areas
    # OR replace with $...$
    
    # In the JS file, \\( is literally backslash-backslash-( 
    # Let's replace all \\( ... \\) patterns (that are NOT inside $$) with $...$
    # This is complex to do reliably, so let's just do it globally in the L41-L45 section
    
    # Simple approach: replace \\( with nothing and \\) with nothing
    # No - that removes the math!
    
    # Better: replace \\( with single $ and \\) with single $
    # \\( -> $ and \\) -> $  BUT only outside of $$ blocks
    
    # Simplest safe approach: just remove ALL occurrences of the literal strings
    # "\\\\(" and "\\\\)" from the middle section and wrap with $
    # (In the actual file these appear as \\( and \\))
    
    # Let's do regex: find \\(content\\) and replace with $content$
    # In file: \\( = literal chars \\ and (
    middle = re.sub(r'\\\\\(([^)]*?)\\\\\)', r'$\1$', middle)
    
    # Fix underscores issue in L35/L36/L37
    # Replace sequences of underscores in math with \underline{\hspace{...}}
    # These appear as \\text{___...___}
    middle = middle.replace('\\\\text{_____________}', '\\\\underline{\\\\hspace{3cm}}')
    middle = middle.replace('\\\\text{__________________________}', '\\\\underline{\\\\hspace{4cm}}')
    
    # Fix ✓ character - replace with \\checkmark in math contexts or remove from math
    middle = middle.replace('✓', '\\\\checkmark')
    
    return before + middle + after

content = fix_inline_in_l41_l45(content)

print(f"Fixed size: {len(content):,} bytes")

with open(data_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fix applied! Now run validate_katex.js to check.")
