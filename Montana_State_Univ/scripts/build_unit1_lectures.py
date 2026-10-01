import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding="utf-8")

output_dir = r"c:\Oikos Univ\Montana_State_Univ\lectures"
os.makedirs(output_dir, exist_ok=True)

print("Starting generation of Unit 1 lectures (Lecture 02 to 15)...")
