# Write your code here

import re

def one_or_more_b(string):
    pattern = r'^b+$'
    match = re.search(pattern, string)
    return bool(match)