# Write your code here


import re

def contains_a(string):
    pattern = r'a'
    match = re.search(pattern, string)
    return bool(match)