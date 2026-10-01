# -*- coding: utf-8 -*-
"""
apply_unit1_batch2.py
Applies true 20-25 minute broadcast tiki-taka scripts for Lectures 06 to 10 to montanaSlidesData.js
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

from patch_scripts import apply_scripts_to_data
from unit1_scripts_l06_l08 import SCRIPTS_L06, SCRIPTS_L07, SCRIPTS_L08
from unit1_scripts_l09_l10 import SCRIPTS_L09, SCRIPTS_L10

print("Applying 20-25 min scripts for Lecture 06...")
apply_scripts_to_data(SCRIPTS_L06, 6)

print("\nApplying 20-25 min scripts for Lecture 07...")
apply_scripts_to_data(SCRIPTS_L07, 7)

print("\nApplying 20-25 min scripts for Lecture 08...")
apply_scripts_to_data(SCRIPTS_L08, 8)

print("\nApplying 20-25 min scripts for Lecture 09...")
apply_scripts_to_data(SCRIPTS_L09, 9)

print("\nApplying 20-25 min scripts for Lecture 10...")
apply_scripts_to_data(SCRIPTS_L10, 10)

print("\nAll batch 2 lectures (L06-L10) updated with full 20-25 minute scripts successfully!")
