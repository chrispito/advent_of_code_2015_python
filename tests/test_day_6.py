import unittest
from ..lib import day_6 as day

class DaySixTests(unittest.TestCase):
    
    def test_get_coordinate(self):
        data = "0,0 through 999,999"
        self.assertEqual(day.get_coordinate(data), {'x': (0, 0), 'y': (999, 999)})
    
    def test_on_0_0_999_999(self):
        data = "turn on 0,0 through 999,999"
        puzzel = day.lights_count(data, 1000)
        self.assertEqual(day.count_lighted(puzzel), 1000000)

    def test_toggle_0_0_999_0(self):
        data = "toggle 0,0 through 999,0"
        puzzel = day.lights_count(data, 1000)
        self.assertEqual(day.count_lighted(puzzel), 1000)

    def test_off_499_499_500_500(self):
        data = "turn off 499,499 through 500,500"
        puzzel = day.lights_count(data, 1000)
        self.assertEqual(day.count_lighted(puzzel), 0)

    def test_off_0_0_0_0(self):
        data = "turn on 0,0 through 0,0"
        puzzel = day.lights_count(data, 1000)
        self.assertEqual(day.count_brightness(puzzel), 1)

    def test_off_0_0_999_999(self):
        data = "toggle 0,0 through 999,999"
        puzzel = day.lights_count(data, 1000)
        self.assertEqual(day.count_brightness(puzzel), 2000000)


if __name__ == '__main__':
    unittest.main()