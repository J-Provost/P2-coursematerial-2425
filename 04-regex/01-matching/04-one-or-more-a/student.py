# Write your code here

import re

def one_or_more_a(string):
    pattern = r'^a+$'
    match = re.search(pattern, string)
    return bool(match)
