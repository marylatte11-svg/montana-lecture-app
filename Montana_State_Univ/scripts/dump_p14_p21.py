import sys, pypdf
sys.stdout.reconfigure(encoding='utf-8')

reader = pypdf.PdfReader('Montana_State_Univ/M090 Full Student Workbook.pdf')

for p_num in [14, 15, 18, 19, 20, 21]:
    page = reader.pages[p_num]
    print(f"\n==================== PDF Page {p_num} (Book p. {p_num - 2}) ====================")
    current_line = []
    def visitor(text, cm, tm, font_dict, font_size):
        if text:
            y = tm[5] if len(tm) > 5 else 0
            current_line.append((y, text))
    page.extract_text(visitor_text=visitor)
    if current_line:
        sorted_chars = sorted(current_line, key=lambda x: -x[0])
        print(''.join([c[1] for c in sorted_chars]))
