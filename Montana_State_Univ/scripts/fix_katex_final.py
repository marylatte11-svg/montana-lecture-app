"""
fix_katex_final.py - Fix remaining 4 KaTeX errors
"""
import re
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_file = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'data', 'montanaSlidesData.js'))

with open(data_file, 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

# Fix 1: \\underline{\\hspace{3cm}}____________ - the replacement left extra underscores
# Pattern: \\underline{\\hspace{3cm}} followed by underscores
content = re.sub(
    r'\\\\underline\{\\\\hspace\{3cm\}\}_{3,}',
    r'\\\\underline{\\\\hspace{3cm}}',
    content
)
print("Fix 1: Removed trailing underscores after underline")

# Fix 2: \\left(\\dfrac{-b}{a},\\,c\\right)\\ at end (trailing backslash)
# This comes from the pitfall field in L44 slide 1
content = content.replace(
    r'\\left(\\dfrac{-b}{a},\\,c\\right)\\',
    r'\\left(\\dfrac{-b}{a},\\,c\\right)'
)
# Try the JS escaped version
content = content.replace(
    '\\\\left(\\\\dfrac{-b}{a},\\\\,c\\\\right)\\\\\\n',
    '\\\\left(\\\\dfrac{-b}{a},\\\\,c\\\\right)\\n'
)
print("Fix 2: Removed trailing backslash after \\right)")

# Fix 3: Also check for any remaining __ sequences (less specific)
remaining_underscores = re.findall(r'_{4,}', content)
print(f"Remaining underscore sequences of 4+: {len(remaining_underscores)}")
if remaining_underscores:
    # Fix them - but only in math-adjacent contexts (inside $$ blocks)
    # For safety, fix all
    content = re.sub(r'_{4,}', r'\\\\underline{\\\\hspace{2cm}}', content)
    print("Fixed remaining underscore sequences")

print(f"Size change: {original_len:,} -> {len(content):,} bytes")

with open(data_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
