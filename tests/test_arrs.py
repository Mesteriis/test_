import pytest

from utils import arrs
from utils.arrs import my_slice


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


@pytest.fixture()
def data_for_test_slice():
    return [([], 0, 1, []),
            ([1, 2, 3, 4, 5, 6, 7], 0, 0, []),
            ([1, 2, 3, 4, 5, 6, 7], 7, None, []),
            ([1, 2, 3, 4, 5, 6, 7], -2, None, [6, 7]),
            ([1, 2, 3, 4, 5, 6, 7], -5, -2, [3, 4, 5]),
            ([], 0, -1, []),
            ([], None, None, []),
            ([-1], -2, None, [-1]),
    ]



def test_my_slice(data_for_test_slice):
    for coll, start, end, expected  in data_for_test_slice:
        print(coll, start, end, expected)
        assert my_slice(coll, start, end) == expected
