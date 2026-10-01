# -*- coding: utf-8 -*-
"""
apply_unit1_batch1.py
Applies true 20-25 minute broadcast tiki-taka scripts for Lectures 01 to 05 to montanaSlidesData.js
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

from patch_scripts import apply_scripts_to_data
from unit1_scripts_l01_l03 import SCRIPTS_L01, SCRIPTS_L02, SCRIPTS_L03
from unit1_scripts_l04_l05 import SCRIPTS_L04, SCRIPTS_L05

print("Applying 20-25 min scripts for Lecture 01...")
apply_scripts_to_data(SCRIPTS_L01, 1)

print("\nApplying 20-25 min scripts for Lecture 02...")
apply_scripts_to_data(SCRIPTS_L02, 2)

print("\nApplying 20-25 min scripts for Lecture 03...")
apply_scripts_to_data(SCRIPTS_L03, 3)

print("\nApplying 20-25 min scripts for Lecture 04...")
apply_scripts_to_data(SCRIPTS_L04, 4)

print("\nApplying 20-25 min scripts for Lecture 05...")
apply_scripts_to_data(SCRIPTS_L05, 5)

print("\nAll batch 1 lectures (L01-L05) updated with full 20-25 minute scripts successfully!")
