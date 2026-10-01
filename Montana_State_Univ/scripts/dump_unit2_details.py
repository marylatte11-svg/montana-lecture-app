import sys, pypdf
sys.stdout.reconfigure(encoding='utf-8')

reader = pypdf.PdfReader('Montana_State_Univ/M090 Full Student Workbook.pdf')

for p_num in [35, 36, 40, 42, 43, 44, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57]:
    page = reader.pages[p_num]
    book_p = p_num - 2
    print(f"\n==================== Book Page {book_p} (PDF Page {p_num}) ====================")
    text = page.extract_text()
    for l in text.split('\n'):
        if l.strip():
            print(l)
