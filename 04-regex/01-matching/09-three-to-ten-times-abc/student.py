# Write your code here


import re

def three_to_ten_times_abc(string):
    pattern = r'^(abc){10}+$|^(abc){3}+$'
    match = re.search(pattern, string)
    return bool(match)