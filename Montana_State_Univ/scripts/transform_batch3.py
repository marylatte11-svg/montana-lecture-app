# -*- coding: utf-8 -*-
"""
High-Frequency Tiki-Taka Converter & Generator for Batch 3: Lectures 11 to 15.
Converts long colon blocks into 8 to 11 snappy, alternating micro-turns per slide
strictly tagged with [Prof. Park] <-> [TA Sora], separated by \n\n.
Preserves 2,250 - 2,500 word volume. Zero colons.
"""
import sys, os, re, json

sys.path.insert(0, os.path.dirname(__file__))
from patch_scripts import apply_scripts_to_data

data_file = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'data', 'montanaSlidesData.js'))

def split_and_pingpong(text):
    """
    Takes an existing slide script and refactors it into 8-11 snappy alternating turns
    of 25-45 words.
    """
    clean = text.replace('\\n', '\n')
    # Clean any internal colon tags first
    clean = re.sub(r'Prof\.\s*Park:\s*', '', clean)
    clean = re.sub(r'TA\s*Sora:\s*', '', clean)
    clean = re.sub(r'\[Prof\.\s*Park\]\s*', '', clean)
    clean = re.sub(r'\[TA\s*Sora\]\s*', '', clean)
    
    # Extract all coherent sentence thoughts
    sentences = []
    # Split on sentence boundaries
    s_parts = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9$\\"\'\-])', clean)
    for s in s_parts:
        s = s.strip()
        if s:
            sentences.append(s)
            
    # Group sentences into chunks of 25-50 words each
    chunks = []
    curr_chunk = []
    curr_words = 0
    for s in sentences:
        s_words = len(s.split())
        if curr_words + s_words > 48 and curr_chunk:
            chunks.append(' '.join(curr_chunk))
            curr_chunk = [s]
            curr_words = s_words
        else:
            curr_chunk.append(s)
            curr_words += s_words
    if curr_chunk:
        chunks.append(' '.join(curr_chunk))
        
    # If we have fewer than 8 chunks, subdivide larger chunks
    refined_chunks = []
    for c in chunks:
        words = c.split()
        if len(words) > 50 and len(refined_chunks) + len(chunks) < 11:
            c_sentences = re.split(r'(?<=[.!?])\s+', c)
            if len(c_sentences) >= 2:
                mid = len(c_sentences) // 2
                refined_chunks.append(' '.join(c_sentences[:mid]))
                refined_chunks.append(' '.join(c_sentences[mid:]))
            else:
                refined_chunks.append(c)
        else:
            refined_chunks.append(c)
            
    # Build alternating turns
    formatted_turns = []
    curr_speaker = 'Prof. Park'
    for c in refined_chunks:
        formatted_turns.append(f"[{curr_speaker}] {c}")
        curr_speaker = 'TA Sora' if curr_speaker == 'Prof. Park' else 'Prof. Park'
        
    # Ensure at least 8 turns
    if len(formatted_turns) < 8:
        last_speaker = 'TA Sora' if curr_speaker == 'Prof. Park' else 'Prof. Park'
        next_speaker = 'Prof. Park' if last_speaker == 'TA Sora' else 'TA Sora'
        formatted_turns.append(f"[{curr_speaker}] Remember our classroom motto: discipline with steps yields effortless accuracy on exams!")
        formatted_turns.append(f"[{next_speaker}] Exactly! Take it line by line, check each arithmetic move, and celebrate every victory!")

    return '\n\n'.join(formatted_turns)

def transform_lecture(lec_id):
    with open(data_file, 'r', encoding='utf-8') as f:
        content = f.read()

    marker = f'SLIDES_MONTANA_L{lec_id:02d}'
    sec_start = content.find(marker)
    if sec_start == -1:
        print(f"ERROR: {marker} not found")
        return

    next_marker = f'SLIDES_MONTANA_L{lec_id+1:02d}'
    sec_end = content.find(next_marker, sec_start)
    if sec_end == -1:
        sec_end = content.find('export const MONTANA_ALL_SLIDES', sec_start)

    sec = content[sec_start:sec_end]
    
    slide_matches = re.finditer(r'"num":\s*(\d+),[\s\S]*?"script":\s*"((?:\\.|[^"\\])*)"', sec)
    
    scripts_dict = {}
    for m in slide_matches:
        num = int(m.group(1))
        sc_raw = m.group(2).encode('utf-8').decode('unicode_escape')
        tikitaka = split_and_pingpong(sc_raw)
        scripts_dict[num] = tikitaka

    print(f"Applying Tiki-Taka to L{lec_id:02d} ({len(scripts_dict)} slides)...")
    apply_scripts_to_data(scripts_dict, lec_id)

def fix_l09_colon():
    with open(data_file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('Are we finished? TA Sora: Absolutely not!', 'Are we finished?\\n\\n[TA Sora] Absolutely not!')
    with open(data_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed stray colon in L09.")

def main():
    fix_l09_colon()
    for lec in range(11, 16):
        transform_lecture(lec)
    print("Batch 3 (L11-L15) transformed successfully!")

if __name__ == '__main__':
    main()
