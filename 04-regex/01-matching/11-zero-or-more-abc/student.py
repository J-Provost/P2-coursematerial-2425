# Write your code here


import re

def zero_or_more_abc(string):
    pattern = r'^(abc)*$'
    match = re.search(pattern, string)
    return bool(match)