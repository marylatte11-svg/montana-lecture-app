# -*- coding: utf-8 -*-
"""
apply_unit2_batch1.py
Applies high-volume broadcast tiki-taka scripts for Lectures 16 to 20 to montanaSlidesData.js
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

from patch_scripts import apply_scripts_to_data
from unit2_scripts_l16_l17 import SCRIPTS_L16, SCRIPTS_L17
from unit2_scripts_l18_l20 import SCRIPTS_L18, SCRIPTS_L19, SCRIPTS_L20

print("Applying scripts for Lecture 16...")
apply_scripts_to_data(SCRIPTS_L16, 16)

print("\nApplying scripts for Lecture 17...")
apply_scripts_to_data(SCRIPTS_L17, 17)

print("\nApplying scripts for Lecture 18...")
apply_scripts_to_data(SCRIPTS_L18, 18)

print("\nApplying scripts for Lecture 19...")
apply_scripts_to_data(SCRIPTS_L19, 19)

print("\nApplying scripts for Lecture 20...")
apply_scripts_to_data(SCRIPTS_L20, 20)

print("\nAll batch 1 lectures (L16-L20) updated successfully!")
