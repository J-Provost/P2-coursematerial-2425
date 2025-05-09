# Write your code here

import re

def two_or_more_abc(string):
    pattern = r'^abc(abc)+$'
    match = re.search(pattern, string)
    return bool(match)