def find(xs, condition):
    for x in xs:
        if condition(x):
            return x
    return None

def has_consecutive_characters(string):
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            return True
    return False

def find_string_with_consecutive_characters(strings):
    return find(strings, has_consecutive_characters)