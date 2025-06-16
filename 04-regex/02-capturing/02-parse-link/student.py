# Write your code here
import re

def parse_link(string):
    pattern = r'<a href="([^"]*)">([^<]*)</a>'
    match = re.fullmatch(pattern, string)
    if not match:
        return None
    link, caption = match.group(1), match.group(2)
    return (caption, link)