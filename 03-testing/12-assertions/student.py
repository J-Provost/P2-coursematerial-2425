def merge_sort(ns):
    # Check if input is a list
    assert isinstance(ns, list), f"Expected a list, got {type(ns)}"

    # Base case: If the list has one or zero elements, it's already sorted
    if len(ns) <= 1:
        return ns
    
    # Split the list into two halves
    mid = len(ns) // 2
    left = ns[:mid]
    right = ns[mid:]

    # Recursively split and merge the halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Ensure that the two halves are sorted before merging
    assert all(left_sorted[i] <= left_sorted[i + 1] for i in range(len(left_sorted) - 1)), "Left half is not sorted"
    assert all(right_sorted[i] <= right_sorted[i + 1] for i in range(len(right_sorted) - 1)), "Right half is not sorted"

    # Merge the two sorted halves
    result = merge(left_sorted, right_sorted)
    
    # Check that the result is sorted
    assert all(result[i] <= result[i + 1] for i in range(len(result) - 1)), "Merged result is not sorted"
    
    return result


def merge(left, right):
    # Ensure both lists are sorted
    assert all(left[i] <= left[i + 1] for i in range(len(left) - 1)), "Left list is not sorted before merge"
    assert all(right[i] <= right[i + 1] for i in range(len(right) - 1)), "Right list is not sorted before merge"

    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # If any elements are left in either list, add them to the result
    result.extend(left)
    result.extend(right)

    # Ensure the result is sorted
    assert all(result[i] <= result[i + 1] for i in range(len(result) - 1)), "Merged result is not sorted after merge"

    return result
