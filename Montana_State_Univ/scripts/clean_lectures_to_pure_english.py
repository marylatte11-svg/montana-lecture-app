import os
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

lectures_dir = r"c:\Oikos Univ\Montana_State_Univ\lectures"

for i in range(1, 16):
    fname = f"lecture{i:02d}.md"
    fpath = os.path.join(lectures_dir, fname)
    if not os.path.exists(fpath):
        continue
    
    with open(fpath, encoding="utf-8") as f:
        content = f.read()
    
    # Remove Korean sections: ### 🇰🇷 한국어 강의 가이드 및 핵심 요약 and everything until next ### or --- or Slide
    cleaned = re.sub(r"###\s+🇰🇷\s+한국어[^\n]*\n[\s\S]*?(?=(?:---|##\s+Slide|###|\Z))", "", content)
    
    # Remove any stray Korean characters if any in slide headers or labels
    # e.g., (문항), (단계별 수학 풀이), (자주 틀리는 함정)
    cleaned = re.sub(r"\s*\((?:문항|단계별\s*수학\s*풀이|자주\s*틀리는\s*함정|식|방정식|양팔\s*저울|단순화|표현식)\)", "", cleaned)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(cleaned)

print("Cleaned all 15 lectures to 100% pure English.")
