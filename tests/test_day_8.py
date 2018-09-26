import unittest, re
from os import path
from ..lib import day_8 as day

basepath = path.dirname(__file__)

class DaySevenTests(unittest.TestCase):
    def test_code_all(self):
        filepath = path.abspath(path.join(basepath,"day_8_test.txt"))
        with open(filepath, "r") as file:
            counter = 0
            for line in file:
                counter += 1
                line = line.strip()
                if counter == 1:
                    print("Test 1")
                    self.assertEqual(day.string_count(line), (0, 2))
                    continue
                if counter == 2:
                    print("Test 2")
                    self.assertEqual(day.string_count(line), (3, 5))
                    continue
                if counter == 3:
                    print("Test 3")
                    self.assertEqual(day.string_count(line), (7, 10))
                    continue
                if counter == 4:
                    print("Test 4")
                    self.assertEqual(day.string_count(line), (1, 6))
                    continue
                if counter == 5:
                    print("Test 5")
                    self.assertEqual(day.string_count(line), (6, 11))
                    continue
                if counter == 6:
                    print("Test 6")
                    self.assertEqual(day.string_count(line), (2, 7))
                    continue
                if counter == 7:
                    print("Test 7")
                    self.assertEqual(day.string_count(line), (3, 9))
                    continue
                if counter == 8:
                    print("Test 8")
                    self.assertEqual(day.string_count(line), (30, 39))
                    continue
                else:
                    break

    def test_encode_all(self):
        filepath = path.abspath(path.join(basepath,"day_8_test.txt"))
        with open(filepath, "r") as file:
            counter = 0
            for line in file:
                counter += 1
                line = line.strip()
                if counter == 1:
                    print("Test 1")
                    self.assertEqual(day.string_encode_count(line), (6, 2))
                    continue
                if counter == 2:
                    print("Test 2")
                    self.assertEqual(day.string_encode_count(line), (9, 5))
                    continue
                if counter == 3:
                    print("Test 3")
                    self.assertEqual(day.string_encode_count(line), (16, 10))
                    continue
                if counter == 4:
                    print("Test 4")
                    self.assertEqual(day.string_encode_count(line), (11, 6))
                    continue
                if counter == 5:
                    print("Test 5")
                    self.assertEqual(day.string_encode_count(line), (16, 11))
                    continue
                if counter == 6:
                    print("Test 6")
                    self.assertEqual(day.string_encode_count(line), (12, 7))
                    continue
                if counter == 7:
                    print("Test 7")
                    self.assertEqual(day.string_encode_count(line), (16, 9))
                    continue
                if counter == 8:
                    print("Test 8")
                    self.assertEqual(day.string_encode_count(line), (47, 39))
                    continue
                else:
                    break


if __name__ == '__main__':
    unittest.main()