# -*- coding: utf-8 -*-
"""
apply_unit2_batch2.py
Applies true 20-25 minute broadcast tiki-taka scripts for Lectures 21 to 25 to montanaSlidesData.js
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

from patch_scripts import apply_scripts_to_data
from unit2_scripts_l21_l25_master_25m import SCRIPTS_L21, SCRIPTS_L22_EXP, SCRIPTS_L23_EXP, SCRIPTS_L24_EXP, SCRIPTS_L25_EXP

print("Applying 20-25 min scripts for Lecture 21...")
apply_scripts_to_data(SCRIPTS_L21, 21)

print("\nApplying 20-25 min scripts for Lecture 22...")
apply_scripts_to_data(SCRIPTS_L22_EXP, 22)

print("\nApplying 20-25 min scripts for Lecture 23...")
apply_scripts_to_data(SCRIPTS_L23_EXP, 23)

print("\nApplying 20-25 min scripts for Lecture 24...")
apply_scripts_to_data(SCRIPTS_L24_EXP, 24)

print("\nApplying 20-25 min scripts for Lecture 25...")
apply_scripts_to_data(SCRIPTS_L25_EXP, 25)

print("\nAll batch 2 lectures (L21-L25) updated with full 20-25 minute scripts successfully!")
