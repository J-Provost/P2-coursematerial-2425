
# Write your code here


import re

def only_letters(string):
    pattern = r'^[a-zA-Z]*$'
    match = re.search(pattern, string)
    return bool(match)