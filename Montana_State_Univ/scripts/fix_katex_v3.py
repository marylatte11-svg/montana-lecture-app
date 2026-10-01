"""
fix_katex_v3.py
Fixes KaTeX errors in L41-L45 sections of montanaSlidesData.js
"""

import re
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_file = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'data', 'montanaSlidesData.js'))

with open(data_file, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original size: {len(content):,} bytes")

# Find L41-L45 section
l41_start = content.find('export const SLIDES_MONTANA_L41')
map_start = content.find('export const MONTANA_ALL_SLIDES', l41_start)

before = content[:l41_start]
middle = content[l41_start:map_start]
after = content[map_start:]

print(f"L41-L45 section size: {len(middle):,} bytes")

# Replace \\( ... \\) inline math with $...$
# In file: \\( = two chars backslash backslash open-paren
count_open = middle.count('\\\\(')
print(f"Found {count_open} open inline math markers")

# Regex: replace \\( non-greedy content \\) with $content$
# Need to handle nested parens carefully - use a simpler non-paren approach
def fix_inline_math(text):
    # Strategy: replace \\\\ followed by ( then content then \\) 
    # The content can have anything except the closing \\)
    # Use a non-greedy match
    return re.sub(r'\\\\\((.+?)\\\\\)', lambda m: '$' + m.group(1) + '$', text)

middle = fix_inline_math(middle)
remaining = middle.count('\\\\(')
print(f"After fix: {remaining} remaining \\\\( (complex nested cases)")

# For remaining ones (with nested parens like \((9,0)\)), do another pass
if remaining > 0:
    middle = fix_inline_math(middle)
    remaining2 = middle.count('\\\\(')
    print(f"After 2nd pass: {remaining2} remaining")

# Fix checkmark unicode - replace \u2713 (checkmark) with text 
middle = middle.replace('\u2713', '\\\\checkmark')
print("Replaced checkmarks")

# Fix underscore sequences in math mode  
for bad_pattern in ['______________', '_____________', '__________________________', '________________']:
    count = middle.count(bad_pattern)
    if count > 0:
        print(f"Fixing {count} occurrences of long underscore sequence")
        middle = middle.replace(bad_pattern, '\\\\underline{\\\\hspace{3cm}}')

content_fixed = before + middle + after

# Also fix L35-L40 underscore issues
l35_start = content_fixed.find('export const SLIDES_MONTANA_L35')
l41_start2 = content_fixed.find('export const SLIDES_MONTANA_L41')

if l35_start != -1 and l41_start2 != -1:
    before35 = content_fixed[:l35_start]
    middle35 = content_fixed[l35_start:l41_start2]
    after41 = content_fixed[l41_start2:]
    
    for bad_pattern in ['______________', '_____________', '__________________________', '________________']:
        count = middle35.count(bad_pattern)
        if count > 0:
            print(f"L35-L40: Fixing {count} underscore sequences")
            middle35 = middle35.replace(bad_pattern, '\\\\underline{\\\\hspace{3cm}}')
    
    content_fixed = before35 + middle35 + after41

print(f"Fixed size: {len(content_fixed):,} bytes")

with open(data_file, 'w', encoding='utf-8') as f:
    f.write(content_fixed)

print("Written! Running validation next...")
