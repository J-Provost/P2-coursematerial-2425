def take_while(xs, condition):
    true_list = []
    false_list = []
    for x in xs:
        if condition(x):
            true_list.append(x)
        else:
            false_list = xs[xs.index(x):]
            break
    return (true_list, false_list)