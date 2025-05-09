# Write your code here

import re

def is_number(string):
    pattern = r'\b^[+-]?(\d+(\.\d*)?|\.\d+)$\b'
    match = re.search(pattern, string)
    return bool(match)