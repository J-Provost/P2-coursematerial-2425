def partition(lst, condition):
    true_list = []
    false_list = []
    for item in lst:
        if condition(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return (true_list, false_list)

def children_and_adults(people):
    return partition(people, lambda person: person.age < 18)