import pytest
from mystatistics import average
from pytest import approx

@pytest.mark.parametrize("ns, expected", [
    ([0.1, 0.1, 0.1], 0.1),
    ([1, 2, 3, 4, 5], 3),
    ([10, 20, 30], 20),
    ([1.5, 2.5, 3.5], 2.5),
    ([100, 200, 300, 400], 250),
    ([0, 0, 0], 0),
    ([1], 1),
    ([], 0),
])
def test_average(ns, expected):
    assert average(ns) == approx(expected, abs=0.01)