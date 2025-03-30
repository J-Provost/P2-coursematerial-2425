from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert overlapping_intervals((5, 5), (5, 6))
    assert overlapping_intervals((2, 6), (4, 8))
    assert overlapping_intervals((0, 10), (5, 7))
    assert overlapping_intervals((3, 8), (1, 5))

    assert not overlapping_intervals((2, 5), (7, 10))
    assert not overlapping_intervals((5, 5), (6, 6))
    assert not overlapping_intervals((1, 3), (4, 6))
    assert not overlapping_intervals((7, 9), (10, 12))

    assert overlapping_intervals((5, 5), (5, 5))
    assert not overlapping_intervals((6, 2), (5, 7))
    assert not overlapping_intervals((1, 0), (1, 6))
    assert not overlapping_intervals((7, 5), (7, 10))
    assert not overlapping_intervals((8, 7), (7, 9))
    assert not overlapping_intervals((9, 8), (10, 12))

    assert overlapping_intervals((1, 10), (3, 7))
    assert overlapping_intervals((3, 7), (1, 10))