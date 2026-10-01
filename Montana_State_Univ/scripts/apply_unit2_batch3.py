# -*- coding: utf-8 -*-
"""
apply_unit2_batch3.py
Applies true 20-25 minute broadcast tiki-taka scripts for Lectures 26 to 30 to montanaSlidesData.js
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

from patch_scripts import apply_scripts_to_data
from unit2_scripts_l26_l30_full_25m import SCRIPTS_L26_EXP, SCRIPTS_L27_EXP, SCRIPTS_L28_EXP, SCRIPTS_L29, SCRIPTS_L30_EXP

print("Applying 20-25 min scripts for Lecture 26...")
apply_scripts_to_data(SCRIPTS_L26_EXP, 26)

print("\nApplying 20-25 min scripts for Lecture 27...")
apply_scripts_to_data(SCRIPTS_L27_EXP, 27)

print("\nApplying 20-25 min scripts for Lecture 28...")
apply_scripts_to_data(SCRIPTS_L28_EXP, 28)

print("\nApplying 20-25 min scripts for Lecture 29...")
apply_scripts_to_data(SCRIPTS_L29, 29)

print("\nApplying 20-25 min scripts for Lecture 30...")
apply_scripts_to_data(SCRIPTS_L30_EXP, 30)

print("\nAll batch 3 lectures (L26-L30) updated with full 20-25 minute scripts successfully!")
