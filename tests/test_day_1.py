import unittest
from ..lib import day_one as day

class DayOneTests(unittest.TestCase):
    
    def test_hello_world(self):
        self.assertEqual(day.hello_world(), 'hello world')

    def test_move_1(self):
        steps_1 = "(())"
        steps_2 = "()()"
        self.assertEqual(day.move(steps_1), 0)
        self.assertEqual(day.move(steps_2), 0)

    def test_move_2(self):
        steps_1 = "((("
        steps_2 = "(()(()("
        self.assertEqual(day.move(steps_1), 3)
        self.assertEqual(day.move(steps_2), 3)

    def test_move_3(self):
        steps_1 = "))((((("
        self.assertEqual(day.move(steps_1), 3)

    def test_move_4(self):
        steps_1 = "())"
        steps_2 = "))("
        self.assertEqual(day.move(steps_1), -1)
        self.assertEqual(day.move(steps_2), -1)

    def test_move_5(self):
        steps_1 = ")))"
        steps_2 = ")())())"
        self.assertEqual(day.move(steps_1), -3)
        self.assertEqual(day.move(steps_2), -3)

    def test_position_1(self):
        step_1 = (')')
        step_2 = ('()())')
        move_with_pos_1 = day.move_with_position(step_1, 1)
        move_with_pos_2 = day.move_with_position(step_2, 0)
        self.assertEqual(move_with_pos_1["move"], -1)
        self.assertEqual(move_with_pos_1["position"], 1)
        self.assertEqual(move_with_pos_2["move"], 0)
        self.assertEqual(move_with_pos_2["position"], 2)

if __name__ == '__main__':
    unittest.main()