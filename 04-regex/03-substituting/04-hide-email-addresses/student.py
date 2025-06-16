# Write your code here
import re

def hide_email_addresses(string):
    pattern = r'[a-zA-Z0-9.]+@[a-zA-Z0-9.]+'
    def replace(match):
        return '*' * len(match.group(0))
    return re.sub(pattern, replace, string)