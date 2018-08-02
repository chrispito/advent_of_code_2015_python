import unittest
from ..lib import day_5 as day

class DayFiveTests(unittest.TestCase):
    
    def test_check_first_condition_False(self):
        data = "abcdef"
        self.assertEqual(day.check_first_condition(data), False)

    def test_check_first_condition_True(self):
        data = "abcdefi"
        self.assertEqual(day.check_first_condition(data), True)
    
    def test_check_second_condition_False(self):
        data = "abcdef"
        self.assertEqual(day.check_second_condition(data), False)

    def test_check_second_condition_True(self):
        data = "abcdeefi"
        self.assertEqual(day.check_second_condition(data), True)
    
    def test_check_third_condition_False(self):
        data = "abcdef"
        self.assertEqual(day.check_third_condition(data), False)

    def test_check_third_condition_True(self):
        data = "afbcgdeefi"
        self.assertEqual(day.check_third_condition(data), True)

    def test_nice_string_check_1(self):
        data = "ugknbfddgicrmopn"
        self.assertEqual(day.nice_string_check(data), True)

    def test_nice_string_check_2(self):
        data = "aaa"
        self.assertEqual(day.nice_string_check(data), True)

    def test_nice_string_check_3(self):
        data = "jchzalrnumimnmhp"
        self.assertEqual(day.nice_string_check(data), False)

    def test_nice_string_check_4(self):
        data = "haegwjzuvuyypxyu"
        self.assertEqual(day.nice_string_check(data), False)

    def test_nice_string_check_5(self):
        data = "dvszwmarrgswjxmb"
        self.assertEqual(day.nice_string_check(data), False)
    
    def test_check_first_condition_new_True(self):
        data = "xyxy"
        self.assertEqual(day.check_first_condition_new(data), True)
    
    def test_check_first_condition_new_True_2(self):
        data = "aabcdefgaa"
        self.assertEqual(day.check_first_condition_new(data), True)

    def test_check_first_condition_new_False(self):
        data = "aaa"
        self.assertEqual(day.check_first_condition_new(data), False)

    def test_check_second_condition_new_True(self):
        data = "xyx"
        self.assertEqual(day.check_second_condition_new(data), True)
    
    def test_check_second_condition_new_True_2(self):
        data = "abcdefeghi"
        self.assertEqual(day.check_second_condition_new(data), True)
    
    def test_check_second_condition_new_True_3(self):
        data = "efe"
        self.assertEqual(day.check_second_condition_new(data), True)
    
    def test_check_second_condition_new_True_4(self):
        data = "addada"
        self.assertEqual(day.check_second_condition_new(data), True)
    
    def test_check_second_condition_new_False(self):
        data = "acdsfdcvd"
        self.assertEqual(day.check_second_condition_new(data), False)
    
    def test_nice_string_check_new_1(self):
        data = "qjhvhtzxzqqjkmpb"
        self.assertEqual(day.nice_string_check_new(data), True)

    def test_nice_string_check_new_2(self):
        data = "xxyxx"
        self.assertEqual(day.nice_string_check_new(data), True)

    def test_nice_string_check_new_3(self):
        data = "uurcxstgmygtbstg"
        self.assertEqual(day.nice_string_check_new(data), False)

    def test_nice_string_check_new_4(self):
        data = "ieodomkazucvgmuy"
        self.assertEqual(day.nice_string_check_new(data), False)


if __name__ == '__main__':
    unittest.main()