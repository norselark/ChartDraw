import unittest
from aq_functions import truncate_rounding

class TestSuite(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
