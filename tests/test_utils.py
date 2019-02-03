import pytest

import lib.utils as utils
from lib.utils import asp, complex_to_coords, harmonics, truncate_rounding


def test_truncate_rounding():
    """Should convert degrees to degrees and minutes within a sign"""
    assert truncate_rounding(0) == "00° 00' Ari"
    assert truncate_rounding(292.24327) == "22° 15' Cap"
    assert truncate_rounding(242.66082) == "02° 40' Sag"
    assert truncate_rounding(293.01350) == "23° 01' Cap"
    assert truncate_rounding(228.76548) == "18° 46' Sco"
    assert truncate_rounding(24.61269) == "24° 37' Ari"


def test_complex_to_coords():
    """Should convert a list of complex numbers to a flat coordinate list
    """
    c = [(4 + 5j), (6 - 9j), (-2 + 1j)]
    res = complex_to_coords(c)
    assert res == [4, 5, 6, -9, -2, 1]


def test_aspect():
    """Should return the aspect and the size of the orbis"""
    assert asp(60, 0) == (60, 1)
    assert asp(0, 90) == (90, 1)
    assert asp(20, 290) == (90, 1)

    # Inexact, but within orbis
    assert asp(98, 0) == (90, 0)
    assert asp(6, 179) == (180, 1 / 8)
    assert asp(6, 190) == (180, 0.5)
    assert asp(205, 80) == (120, 3 / 8)

    # Not within orbis
    assert asp(102, 49) is None
    assert asp(98.05, 0) is None


def test_harmonics():
    """Should calculate harmonics correctly"""
    angles = [20, 0, 180, 240]
    res = harmonics(angles, 2)
    assert res == [40, 0, 0, 120]
    res = harmonics(angles, 3)
    assert res == [60, 0, 180, 0]


def test_dist():
    """Should handle distances between degrees of a circle"""
    assert utils.dist(0, 20) == 20
    assert utils.dist(20, 0) == 20
    assert utils.dist(355, 20) == 25
    assert utils.dist(20, 355) == 25
    assert utils.dist(190, 20) == 170
    assert utils.dist(0, 190) == 170
    assert utils.dist(20, 20) == 0


def test_sort():
    """Should identify if two angles are in the right order"""
    assert utils.is_sorted(10, 20)
    assert not utils.is_sorted(20, 10)
    assert utils.is_sorted(355, 20)
    assert not utils.is_sorted(20, 355)


def test_dms_to_deg():
    """Should convert degrees, minutes and seconds to bare degrees"""
    assert utils.dms_to_deg(80, 0, 0) == 80
    assert utils.dms_to_deg(70, 30, 0) == 70.5
    assert utils.dms_to_deg(8, 20, 0) == 8 + 1/3
    with pytest.raises(ValueError):
        utils.dms_to_deg(80, 80, 80)
