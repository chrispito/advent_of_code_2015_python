import unittest
from ..lib import day_4 as day

class DayTwoTests(unittest.TestCase):
    
    def test_md5_1(self):
        data = "abcdef"
        self.assertEqual(day.hash_check(data), 609043)

    def test_md5_2(self):
        data = "pqrstuv"
        self.assertEqual(day.hash_check(data), 1048970)

if __name__ == '__main__':
    unittest.main()