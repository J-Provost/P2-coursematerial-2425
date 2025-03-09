def group_by(xs, key_function):
    grouped = {}
    for x in xs:
        key = key_function(x)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(x)
    return grouped