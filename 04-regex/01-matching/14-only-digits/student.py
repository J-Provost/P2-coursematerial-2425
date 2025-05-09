# Write your code here


import re

def only_digits(string):
    pattern = r'^\d*$'
    match = re.search(pattern, string)
    return bool(match)