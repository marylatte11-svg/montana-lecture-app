import sys, pypdf
sys.stdout.reconfigure(encoding='utf-8')

reader = pypdf.PdfReader('Montana_State_Univ/M090 Full Student Workbook.pdf')
page = reader.pages[16]

def visitor_body(text, cm, tm, font_dict, font_size):
    if text.strip():
        base_font = font_dict.get('/BaseFont', '') if font_dict else ''
        print(f"{text} (font: {base_font})")

page.extract_text(visitor_text=visitor_body)
