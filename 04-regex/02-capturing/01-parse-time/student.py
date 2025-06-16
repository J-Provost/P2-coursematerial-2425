import re

def parse_time(string):
    pattern = r'(\d{2}):(\d{2}):(\d{2})(?:\.(\d{3}))?'
    match = re.fullmatch(pattern, string)
    if not match:
        return None
    h, m, s, ms = match.groups()
    return (int(h), int(m), int(s), int(ms) if ms is not None else 0)