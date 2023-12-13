"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""
# Imports
from functions import is_hydroxide
# Constants


chemical_formula = input("Enter a chemical formula: ")
result = is_hydroxide(chemical_formula)

if result:
    print("True")
else:
    print("False")
