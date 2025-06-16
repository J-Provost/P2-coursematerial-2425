# Write your code here
import re

def correct_dates(string):
    # Match dates like 12/11/2019 or 1/2/3 and swap the first two parts
    return re.sub(r'\b(\d{1,2})/(\d{1,2})/(\d{1,4})\b', r'\2/\1/\3', string)