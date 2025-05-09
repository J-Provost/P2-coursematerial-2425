# Write your code here


import re

def abc_or_xyz(string):
    pattern = r'^(abc)$|^(xyz)$'
    match = re.search(pattern, string)
    return bool(match)