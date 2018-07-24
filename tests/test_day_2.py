import unittest
from ..lib import day_two as day

class DayTwoTests(unittest.TestCase):
    
    def test_surface_1(self):
        data_1 = "2x3x4"
        self.assertEqual(day.surface(data_1), 58)

    def test_surface_2(self):
        data_1 = "1x1x10"
        self.assertEqual(day.surface(data_1), 43)

    def test_feet_of_ribbon_1(self):
        data_1 = "2x3x4"
        self.assertEqual(day.feet_of_ribbon(data_1), 34)

    def test_feet_of_ribbon_2(self):
        data_1 = "1x1x10"
        self.assertEqual(day.feet_of_ribbon(data_1), 14)

if __name__ == '__main__':
    unittest.main()