import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from stats_median_1784291211415972800 import median


def test_median():
    assert median([3, 1, 2]) == 2
