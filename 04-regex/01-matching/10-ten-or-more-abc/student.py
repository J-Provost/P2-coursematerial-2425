# Write your code here

import re

def ten_or_more_abc(string):
    pattern = r'^(abc){10}+$|^(abc){10,}+$'
    match = re.search(pattern, string)
    return bool(match)