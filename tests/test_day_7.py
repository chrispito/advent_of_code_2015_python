import unittest
from ..lib import day_7 as day

class DaySevenTests(unittest.TestCase):
    
    def test_binary_operator_1(self):
        data = [
            "123 -> x",
            "456 -> y"
        ]
            
        self.assertEqual(day.binary_operator(data), {'x': 123, 'y': 456})

    def test_binary_operator_2(self):
        data = [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e"
        ]
            
        self.assertEqual(day.binary_operator(data), {'x': 123, 'y': 456, 'd': 72, 'e': 507})

    def test_binary_operator_3(self):
        data = [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
        ]
            
        self.assertEqual(day.binary_operator(data), {'x': 123, 'y': 456, 'd': 72, 'e': 507, 'f': 492, 'g': 114})

    def test_binary_operator_4(self):
        data = [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i"
        ] 
            
        self.assertEqual(day.binary_operator(data), {
            'x': 123,
            'y': 456,
            'd': 72,
            'e': 507,
            'f': 492,
            'g': 114,
            'h': 65412,
            'i': 65079
        })
    

if __name__ == '__main__':
    unittest.main()