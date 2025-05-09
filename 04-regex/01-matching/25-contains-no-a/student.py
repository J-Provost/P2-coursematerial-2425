# Write your code here
import re

def contains_no_a(string):
    pattern = r'^((?!a).)*$'
    match = re.fullmatch(pattern, string)
    return bool(match)