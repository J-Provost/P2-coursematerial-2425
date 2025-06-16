# Write your code here
import re

def collect_links(string):
    pattern = r'<a href="([^"]*)">[^<]*</a>'
    return re.findall(pattern, string)