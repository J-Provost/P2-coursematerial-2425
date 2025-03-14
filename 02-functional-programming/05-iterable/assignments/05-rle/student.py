def rle_encode(data):
    data = iter(data)
    try:
        current_char = next(data)
    except StopIteration:
        return

    count = 1
    for char in data:
        if char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1
    yield (current_char, count)

def rle_decode(data):
    for char, count in data:
        for _ in range(count):
            yield char

data=[('a', 8), ('b', 5), ('c', 7), ('a', 7)]
for test in rle_decode(data):
    print(test)