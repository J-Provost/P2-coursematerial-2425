# Write your code here

import re

def starts_with_a(string):
    pattern = r'a'
    match = re.match(pattern, string)
    return bool(match)