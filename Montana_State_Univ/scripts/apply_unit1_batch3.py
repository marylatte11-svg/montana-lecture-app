# -*- coding: utf-8 -*-
"""
apply_unit1_batch3.py
Applies true 20-25 minute broadcast tiki-taka scripts for Lectures 11 to 15 to montanaSlidesData.js
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

from patch_scripts import apply_scripts_to_data
from unit1_scripts_l11_l13 import SCRIPTS_L11, SCRIPTS_L12, SCRIPTS_L13
from unit1_scripts_l14_l15 import SCRIPTS_L14, SCRIPTS_L15

print("Applying 20-25 min scripts for Lecture 11...")
apply_scripts_to_data(SCRIPTS_L11, 11)

print("\nApplying 20-25 min scripts for Lecture 12...")
apply_scripts_to_data(SCRIPTS_L12, 12)

print("\nApplying 20-25 min scripts for Lecture 13...")
apply_scripts_to_data(SCRIPTS_L13, 13)

print("\nApplying 20-25 min scripts for Lecture 14...")
apply_scripts_to_data(SCRIPTS_L14, 14)

print("\nApplying 20-25 min scripts for Lecture 15...")
apply_scripts_to_data(SCRIPTS_L15, 15)

print("\nAll batch 3 lectures (L11-L15) updated with full 20-25 minute scripts successfully!")
