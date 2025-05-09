import re

def is_valid_password(string):
    plength = r'.{12,}' 
    pdigit = r'\d'
    pupper = r'[A-Z]' 
    plower = r'[a-z]'
    psymbol = r'[-+/.*@]' 

    pthreechar = r'(.)\1{2}' 
    pfourchar = r'(.)(.*\1){3}'

    length = re.search(plength, string)
    digit = re.search(pdigit, string)
    upper = re.search(pupper, string)
    lower = re.search(plower, string)
    symbol = re.search(psymbol, string)

    no_three_consecutive = not re.search(pthreechar, string)
    no_four_repeated = not re.search(pfourchar, string)

    return all([length, digit, upper, lower, symbol, no_three_consecutive, no_four_repeated])