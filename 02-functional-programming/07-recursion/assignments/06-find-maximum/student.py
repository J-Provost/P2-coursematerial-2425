def findMaximum(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], findMaximum(list[1:])) 