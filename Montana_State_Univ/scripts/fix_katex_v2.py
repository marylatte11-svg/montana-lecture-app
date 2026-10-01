"""
fix_katex_v2.py
Fixes KaTeX errors in L41-L45 sections of montanaSlidesData.js
Problem: \( \) inline math delimiters appear in the JS strings but the KaTeX validator
treats them as "inside math mode" when they appear near $$ blocks.
Fix: Replace \\( ... \\) with $ ... $ throughout L41-L45 sections.
Also fix __ underscores and checkmarks.
"""

import re
import os

data_file = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'data', 'montanaSlidesData.js'))

with open(data_file, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original size: {len(content):,} bytes")

# Find L41-L45 section
l41_start = content.find('export const SLIDES_MONTANA_L41')
map_start = content.find('export const MONTANA_ALL_SLIDES', l41_start)

if l41_start == -1:
    print("ERROR: SLIDES_MONTANA_L41 not found!")
    exit(1)

before = content[:l41_start]
middle = content[l41_start:map_start]
after = content[map_start:]

print(f"L41-L45 section size: {len(middle):,} bytes")

# In the JS file, \\\\( represents \\( in the string, which KaTeX sees as \(
# We need to replace \\\\(CONTENT\\\\) with $CONTENT$
# But in Python reading the file, each \\ in file = 2 chars \\ 
# So file content "\\\\(" = 4 chars: \, \, (, which is \\(

# Count occurrences
count_open = middle.count('\\\\(')
count_close = middle.count('\\\\)')
print(f"Found {count_open} \\\\( and {count_close} \\\\) in L41-L45 section")

# Replace \\( ... \\) with $ ... $
# This regex matches \\( then content (no newlines) then \\)
# In the file, this appears as \\\\( and \\\\)

def replace_inline_math(text):
    # Pattern: \\( content \\) -> $content$
    # In file chars: \\ ( content \\ )
    # Using regex on the actual file content
    result = re.sub(r'\\\\\(([^)]*?)\\\\\)', r'$\1$', text)
    return result

middle_fixed = replace_inline_math(middle)
count_fixed = middle_fixed.count('\\\\(')
print(f"After fix: {count_fixed} \\\\( remaining (should be 0 or minimal)")

# Also fix underscores - __ patterns in math context  
# These come from L35/L36/L37 which are in the EARLIER sections (already handled)
# For L41-L45, check if any remain
underscore_patterns = ['______________', '_____________', '__________________________']
for pat in underscore_patterns:
    if pat in middle_fixed:
        print(f"WARNING: Found '{pat}' in L41-L45, fixing...")
        middle_fixed = middle_fixed.replace(pat, '\\\\underline{\\\\hspace{3cm}}')

# Fix checkmark unicode character in math mode
# ✓ appears in L45 solutions - replace with text version
if '\u2713' in middle_fixed:
    count_check = middle_fixed.count('\u2713')
    print(f"Found {count_check} ✓ characters, replacing with \\checkmark")
    middle_fixed = middle_fixed.replace('\u2713', '\\\\checkmark')

# Fix \textit{} which may not be supported in KaTeX
middle_fixed = middle_fixed.replace('\\\\textit{', '\\\\text{')

content_fixed = before + middle_fixed + after

print(f"Fixed size: {len(content_fixed):,} bytes")

# Also fix L35/L36/L37 underscore issues (earlier in file)
# Find section from L35 to L40
l35_start = content_fixed.find('export const SLIDES_MONTANA_L35')
l41_start2 = content_fixed.find('export const SLIDES_MONTANA_L41')

if l35_start != -1 and l41_start2 != -1:
    before35 = content_fixed[:l35_start]
    middle35 = content_fixed[l35_start:l41_start2]
    after41 = content_fixed[l41_start2:]
    
    # Fix underscores in L35-L40
    for pat in underscore_patterns:
        if pat in middle35:
            c = middle35.count(pat)
            print(f"L35-L40: Fixing {c} occurrences of '{pat[:12]}...'")
            middle35 = middle35.replace(pat, '\\\\underline{\\\\hspace{3cm}}')
    
    content_fixed = before35 + middle35 + after41

with open(data_file, 'w', encoding='utf-8') as f:
    f.write(content_fixed)

print("\nFix written to file!")
print("Now run: node Montana_State_Univ/scripts/validate_katex.js")
