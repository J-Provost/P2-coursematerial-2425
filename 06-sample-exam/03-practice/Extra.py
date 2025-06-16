import re

def is_valid_date(date_str):
    r = r'^\d{4}-\d{2}-\d{2}$'
    if bool(re.match(r, date_str)):
        return True
    return False


def is_valid_date1(date_str):
    regex = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(regex, date_str):
        return False
    return True

print(is_valid_date('2025-05-20'))
print(is_valid_date1('2025-05-20'))


# date_str = '2025-05-20'
# r = r'^\d{4}-\d{2}-\d{2}$'
# print(re.match(r, date_str))