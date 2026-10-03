import sys, re
sys.stdout.reconfigure(encoding='utf-8')
content = open(r'c:\Oikos Univ\Montana_State_Univ\lectures\lecture01.md', encoding='utf-8').read()
slide_blocks = re.split(r'###\s*\[Slide\s*(\d+)\]', content)[1:]
for i in range(0, len(slide_blocks), 2):
    s_num = int(slide_blocks[i])
    s_text = slide_blocks[i+1]
    title = re.search(r'^(.*?)\n', s_text.strip()).group(1).strip()
    dialogue_match = re.search(r'####\s*🎙️\s*Lecture Dialogue.*?\n(.*?)(?=\n---|---|\Z)', s_text, re.DOTALL)
    dialogue = dialogue_match.group(1).strip() if dialogue_match else ''
    turns = [p.strip() for p in dialogue.split('\n\n') if p.strip()]
    print(f'Slide {s_num}: "{title}" ({len(turns)} turns)')
    for idx, t in enumerate(turns):
        print(f'   Turn {idx+1}: {t[:60]}...')
