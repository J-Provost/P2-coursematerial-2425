# Write your code here
import re

def scrape_email_addresses(string):
    pattern = r'\b[a-z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+\b'
    candidates = re.findall(pattern, string)
    # Filter: must have exactly one @, at least one dot after @, and only allowed chars
    result = []
    for email in candidates:
        local, domain = email.split('@', 1)
        if (
            local and
            domain and
            '.' in domain and
            re.fullmatch(r'[a-z0-9.]+', local) and
            re.fullmatch(r'[a-zA-Z0-9.]+', domain)
        ):
            result.append(email)
    return result