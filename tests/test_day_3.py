import unittest
from ..lib import day_3 as day

class DayTwoTests(unittest.TestCase):
    
    def test_min_home_1(self):
        data = ">"
        self.assertEqual(day.min_home_count(data), 2)

    def test_min_home_2(self):
        data = "^>v<"
        self.assertEqual(day.min_home_count(data), 4)

    def test_min_home_3(self):
        data = "^v^v^v^v^v"
        self.assertEqual(day.min_home_count(data), 2)

    def test_min_home_4(self):
        data = "^v"
        self.assertEqual(day.min_home_count_2(data), 3)

    def test_min_home_5(self):
        data = "^>v<"
        self.assertEqual(day.min_home_count_2(data), 3)

    def test_min_home_6(self):
        data = "^v^v^v^v^v"
        self.assertEqual(day.min_home_count_2(data), 11)

if __name__ == '__main__':
    unittest.main()