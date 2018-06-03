import unittest
from lib.utils import truncate_rounding, complex_to_coords, asp

class TestFunctions(unittest.TestCase):
    def test_truncate_rounding(self):
        # Float arguments
        self.assertEqual(truncate_rounding(292.24327), '22-15 Cap')
        self.assertEqual(truncate_rounding(242.66082), '02-40 Sag')
        self.assertEqual(truncate_rounding(293.01350), '23-01 Cap')
        self.assertEqual(truncate_rounding(228.76548), '18-46 Sco')
        self.assertEqual(truncate_rounding(24.61269), '24-37 Ari')
        # String arguments
        self.assertEqual(truncate_rounding('292.24327'), '22-15 Cap')
        self.assertEqual(truncate_rounding('242.66082'), '02-40 Sag')
        self.assertEqual(truncate_rounding('293.01350'), '23-01 Cap')
        self.assertEqual(truncate_rounding('228.76548'), '18-46 Sco')
        self.assertEqual(truncate_rounding(' 24.61269'), '24-37 Ari')
    
    def test_complex_to_coords(self):
        c = [(4 + 5j), (6 - 9j), (-2 + 1j)]
        res = complex_to_coords(c)
        self.assertEqual(res, [4, 5, 6, -9, -2, 1])

    def test_aspect(self):
        self.assertEqual(asp(60, 0), 60)
        self.assertEqual(asp(0, 90), 90)
        self.assertEqual(asp(98, 0), 90)
        self.assertEqual(asp(20, 290), 90)

        # Inexact, but within orbis
        self.assertEqual(asp(6, 179), 180)
        self.assertEqual(asp(205, 80), 120)

        # Not within orbis
        self.assertIsNone(asp(102, 49))
