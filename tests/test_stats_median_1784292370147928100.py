import pytest

from stats_median_1784292370147928100 import median


def test_median():
    assert median([3, 1, 2]) == 2


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_median_empty_raises():
    with pytest.raises(ValueError):
        median([])
