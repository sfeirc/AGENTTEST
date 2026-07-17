import pytest

from stats_mean_1784292370147928100 import mean


def test_mean():
    assert mean([2, 4]) == 3


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])
