import unittest
from lib.utils import truncate_rounding, complex_to_coords, asp, harmonics
import lib.utils as utils

class TestFunctions(unittest.TestCase):
    def test_truncate_rounding(self):
        # Float arguments
        self.assertEqual(truncate_rounding(292.24327), "22° 15' Cap")
        self.assertEqual(truncate_rounding(242.66082), "02° 40' Sag")
        self.assertEqual(truncate_rounding(293.01350), "23° 01' Cap")
        self.assertEqual(truncate_rounding(228.76548), "18° 46' Sco")
        self.assertEqual(truncate_rounding(24.61269), "24° 37' Ari")
        # String arguments
        self.assertEqual(truncate_rounding("292.24327"), "22° 15' Cap")
        self.assertEqual(truncate_rounding("242.66082"), "02° 40' Sag")
        self.assertEqual(truncate_rounding("293.01350"), "23° 01' Cap")
        self.assertEqual(truncate_rounding("228.76548"), "18° 46' Sco")
        self.assertEqual(truncate_rounding(" 24.61269"), "24° 37' Ari")
    
    def test_complex_to_coords(self):
        c = [(4 + 5j), (6 - 9j), (-2 + 1j)]
        res = complex_to_coords(c)
        self.assertEqual(res, [4, 5, 6, -9, -2, 1])

    def test_aspect(self):
        self.assertEqual(asp(60, 0), (60, 1))
        self.assertEqual(asp(0, 90), (90, 1))
        self.assertEqual(asp(20, 290), (90, 1))

        # Inexact, but within orbis
        self.assertEqual(asp(98, 0), (90, 0))
        self.assertEqual(asp(6, 179), (180, 1 / 8))
        self.assertEqual(asp(6, 190), (180, 0.5))
        self.assertEqual(asp(205, 80), (120, 3 / 8))

        # Not within orbis
        self.assertEqual(asp(102, 49), (None, None))
        self.assertEqual(asp(98.05, 0), (None, None))

    def test_harmonics(self):
        angles = [20, 0, 180, 240]
        res = harmonics(angles, 2)
        self.assertEqual(res, [40, 0, 0, 120])
        res = harmonics(angles, 3)
        self.assertEqual(res, [60, 0, 180, 0])

    def test_dist(self):
        self.assertEqual(utils.dist(0, 20), 20)
        self.assertEqual(utils.dist(20, 0), 20)
        self.assertEqual(utils.dist(355, 20), 25)
        self.assertEqual(utils.dist(20, 355), 25)
        self.assertEqual(utils.dist(190, 20), 170)
        self.assertEqual(utils.dist(0, 190), 170)
        self.assertEqual(utils.dist(20, 20), 0)

    def test_sort(self):
        self.assertTrue(utils.is_sorted(10, 20))
        self.assertFalse(utils.is_sorted(20, 10))
        self.assertTrue(utils.is_sorted(355, 20))
        self.assertFalse(utils.is_sorted(20, 355))

