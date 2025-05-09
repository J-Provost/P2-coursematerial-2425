# Write your code here


import re

def only_vowels(string):
    pattern = r'^[aeiuo]*$'
    match = re.search(pattern, string)
    return bool(match)