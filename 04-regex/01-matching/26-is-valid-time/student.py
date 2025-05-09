# Write your code here

import re

def is_valid_time(string):
    pattern = r'\d{2}:\d{2}:(\d{2}|\d{2}\.\d{3})'
    match = re.fullmatch(pattern, string)
    return bool(match)

