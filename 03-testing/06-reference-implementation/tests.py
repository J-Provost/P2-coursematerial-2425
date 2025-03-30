import pytest
from search import linear_search, binary_search, Student

@pytest.mark.parametrize('students, target_id', [
    ([Student(i) for i in range(1, 11)], 5),  # target is in the middle
    ([Student(i) for i in range(1, 11)], 1),  # target is the first student
    ([Student(i) for i in range(1, 11)], 10),  # target is the last student
    ([Student(i) for i in range(1, 11)], 0),  # target is less than any student id
    ([Student(i) for i in range(1, 11)], 11),  # target is greater than any student id
    ([Student(1), Student(3), Student(5), Student(7)], 5),  # target exists with gaps
    ([Student(1), Student(3), Student(5), Student(7)], 6),  # target doesn't exist with gaps
    ([], 1)  # empty list
])
def test_search_algorithms(students, target_id):
    expected = linear_search(students, target_id)
    actual = binary_search(students, target_id)
    assert expected == actual
