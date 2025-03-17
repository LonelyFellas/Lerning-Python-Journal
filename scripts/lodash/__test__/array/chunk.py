import pytest

from scripts.lodash.array.chunk import chunk

parametrize = pytest.mark.parametrize


@parametrize(
    "case,expected",
    [
        (([1, 2, 3, 4, 5],), [[1], [2], [3], [4], [5]]),
        (([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]),
        (([1, 2, 3, 4, 5], 3), [[1, 2, 3], [4, 5]]),
        (([1, 2, 3, 4, 5], 4), [[1, 2, 3, 4], [5]]),
        (([1, 2, 3, 4, 5], 5), [[1, 2, 3, 4, 5]]),
        (([1, 2, 3, 4, 5], 6), [[1, 2, 3, 4, 5]]),
    ],
)
def test_chunk(case, expected):
    assert chunk(*case) == expected