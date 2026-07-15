import pytest

from calc.mul_div import div, mul


def test_mul():
    assert mul(3, 4) == 12
    assert mul(-2, 5) == -10


def test_div():
    assert div(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
