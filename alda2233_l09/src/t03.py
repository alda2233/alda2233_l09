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
from functions import parse_code
# Constants

product_code = input("Enter a product code: ")
pc, pi, pq = parse_code(product_code)

print(f"{pc},{pi},{pq}")
