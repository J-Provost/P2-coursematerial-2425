class Student:
    def __init__(self, id):
        self.id = id

def linear_search(students, target_id):
    for student in students:
        if student.id == target_id:
            return student
    return None

def binary_search(students, target_id):
    left, right = 0, len(students) - 1
    while left <= right:
        mid = (left + right) // 2
        if students[mid].id == target_id:
            return students[mid]
        elif students[mid].id < target_id:
            left = mid + 1
        else:
            right = mid - 1
    return None
