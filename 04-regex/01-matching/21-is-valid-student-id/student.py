# Write your code here


import re

def is_valid_student_id(string):
    pattern = r'^[RrsS]\d{7}$'
    match = re.match(pattern, string)
    return bool(match)