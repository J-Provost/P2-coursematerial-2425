# Write your code here

import re

def is_valid_email_address(string):
    pattern = r'[\w.]+@(ucll\.be|student\.ucll\.be)'
    match = re.fullmatch(pattern, string)
    return bool(match)