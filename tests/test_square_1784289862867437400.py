import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from square_1784289862867437400 import square


def test_square():
    assert square(4) == 16
