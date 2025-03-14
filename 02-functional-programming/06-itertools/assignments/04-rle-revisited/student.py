from itertools import groupby, chain

def rle_encode(data):
    return ((char, sum(1 for _ in group)) for char, group in groupby(data))

def rle_decode(data):
    return chain.from_iterable(char * count for char, count in data)