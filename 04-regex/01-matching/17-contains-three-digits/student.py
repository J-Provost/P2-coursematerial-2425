
# Write your code here

import re

def contains_three_digits(string):
    pattern = r'\d.*\d.*\d'
    match = re.search(pattern, string)
    return bool(match)