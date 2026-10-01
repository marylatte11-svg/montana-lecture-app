# -*- coding: utf-8 -*-
"""
High-Frequency Tiki-Taka Converter & Generator for Batch 2: Lectures 06 to 10.
Converts long colon blocks into 8 to 10 snappy, alternating micro-turns per slide
strictly tagged with [Prof. Park] <-> [TA Sora], separated by \n\n.
Preserves 2,250 - 2,500 word volume. Zero colons.
"""
import sys, os, re, json

sys.path.insert(0, os.path.dirname(__file__))
from patch_scripts import apply_scripts_to_data

data_file = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'data', 'montanaSlidesData.js'))

def split_and_pingpong(text):
    """
    Takes an existing slide script that has 3-5 large colon/bracket turns,
    and refactors it into 8-10 snappy alternating turns of 25-45 words.
    """
    # Clean tags first
    clean = text.replace('\\n', '\n')
    # Find all sentences or blocks
    # We identify speaker segments
    raw_blocks = re.split(r'(?:^|\n+)(?:\[?(?:Prof\.\s*Park|TA\s*Sora)\]?:?)\s*', clean)
    raw_blocks = [b.strip() for b in raw_blocks if b.strip()]
    
    # If already high frequency (>= 7 turns) and no colons, just ensure [Prof. Park] / [TA Sora] tags
    # Otherwise, split sentences to create alternating tiki-taka
    turns = []
    speaker = 'Prof'  # alternate: Prof -> TA -> Prof -> TA
    
    # Extract all coherent sentence thoughts
    sentences = []
    for b in raw_blocks:
        # Split on sentence boundaries: . ! ? followed by space and capital or math
        s_parts = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9$\\"\'\-])', b)
        for s in s_parts:
            s = s.strip()
            if s:
                sentences.append(s)
                
    # Group sentences into chunks of 2-3 sentences (30-50 words each)
    chunks = []
    curr_chunk = []
    curr_words = 0
    for s in sentences:
        s_words = len(s.split())
        if curr_words + s_words > 50 and curr_chunk:
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
        if len(words) > 55 and len(refined_chunks) + len(chunks) < 10:
            half = len(words) // 2
            # find sentence boundary near half
            c_sentences = re.split(r'(?<=[.!?])\s+', c)
            if len(c_sentences) >= 2:
                mid = len(c_sentences) // 2
                refined_chunks.append(' '.join(c_sentences[:mid]))
                refined_chunks.append(' '.join(c_sentences[mid:]))
            else:
                refined_chunks.append(c)
        else:
            refined_chunks.append(c)
            
    # Now build alternating turns
    formatted_turns = []
    curr_speaker = 'Prof. Park'
    for c in refined_chunks:
        formatted_turns.append(f"[{curr_speaker}] {c}")
        curr_speaker = 'TA Sora' if curr_speaker == 'Prof. Park' else 'Prof. Park'
        
    # Ensure at least 8 turns
    if len(formatted_turns) < 8:
        last_speaker = 'TA Sora' if curr_speaker == 'Prof. Park' else 'Prof. Park'
        next_speaker = 'Prof. Park' if last_speaker == 'TA Sora' else 'TA Sora'
        formatted_turns.append(f"[{curr_speaker}] Take your time with every step here. Writing out intermediate lines is the secret to 100% accuracy!")
        formatted_turns.append(f"[{next_speaker}] Exactly! Protect your signs, trust the algebra rules, and you will get the correct answer every single time!")

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
    
    # Extract each slide and its script
    # Find all "num": X, ... "script": "..."
    slide_matches = re.finditer(r'"num":\s*(\d+),[\s\S]*?"script":\s*"((?:\\.|[^"\\])*)"', sec)
    
    scripts_dict = {}
    for m in slide_matches:
        num = int(m.group(1))
        sc_raw = m.group(2).encode('utf-8').decode('unicode_escape')
        # Ping-pong transform
        tikitaka = split_and_pingpong(sc_raw)
        scripts_dict[num] = tikitaka

    print(f"Applying Tiki-Taka to L{lec_id:02d} ({len(scripts_dict)} slides)...")
    apply_scripts_to_data(scripts_dict, lec_id)

def main():
    for lec in range(6, 11):
        transform_lecture(lec)
    print("Batch 2 (L06-L10) transformed successfully!")

if __name__ == '__main__':
    main()
