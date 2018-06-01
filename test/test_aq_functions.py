import unittest
from lib.utils import truncate_rounding, complex_to_coords

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
