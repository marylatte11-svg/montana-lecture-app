# -*- coding: utf-8 -*-
with open('src/data/montanaSlidesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('SLIDES_MONTANA_L20')
end_pos = text.find('"num": 2,', pos)
with open('Montana_State_Univ/scripts/temp_l20_slide1.txt', 'w', encoding='utf-8') as f2:
    f2.write(text[pos:end_pos])

print("Written temp_l20_slide1.txt")
