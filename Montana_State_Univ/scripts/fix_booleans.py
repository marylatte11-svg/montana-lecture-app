with open('Montana_State_Univ/scripts/unit3_data_l41_l45.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('"dashed": true', '"dashed": True')
content = content.replace('"dashed": false', '"dashed": False')

with open('Montana_State_Univ/scripts/unit3_data_l41_l45.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed booleans')
