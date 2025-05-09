# Write your code here

import re

def is_dna(string):
    pattern = r'^[ACGT]+$'
    match = re.search(pattern, string)
    return bool(match)