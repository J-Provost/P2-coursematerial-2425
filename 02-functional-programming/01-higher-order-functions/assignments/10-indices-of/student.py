def indices_of(xs, condition):
    indices = []
    for index, x in enumerate(xs):
        if condition(x):
            indices.append(index)
    return indices

def is_palindrome(string):
    return string == string[::-1]