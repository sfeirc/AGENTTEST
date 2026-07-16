from calc.add_sub import scale, scale_alt


def test_scale_alt_coexists_with_scale():
    assert scale(2, 3) == 203
    assert scale_alt(2, 3) == 197
