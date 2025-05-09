# Write your code here

import re

def ababa(string):
    pattern = r'(.+)(.+)\1\2\1'
    match = re.fullmatch(pattern, string)
    return bool(match)