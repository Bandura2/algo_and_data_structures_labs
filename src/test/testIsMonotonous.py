import unittest
import main


class TestMonotonous(unittest.TestCase):
    def test_is_monotonous_up(self):
        initial_arr = [1, 2, 3, 4, 6]
        self.assertEqual(main.is_monotonous(initial_arr), True)

    def test_is_monotonous_down(self):
        initial_arr = [6, 5, 4, 3, 2, 1]
        self.assertEqual(main.is_monotonous(initial_arr), True)

    def test_is_not_monotonous(self):
        initial_arr = [1, 2, 6, 4, 5, 3]
        self.assertEqual(main.is_monotonous(initial_arr), False)

    def test_emtpy_array(self):
        self.assertEqual(main.is_monotonous([]), False)

    def test_1(self):
        self.assertEqual(main.is_monotonous([2, 2, -1]), True)

    def test_2(self):
        self.assertEqual(main.is_monotonous([2, 2, 2, 2]), True)

    def test_3(self):
        self.assertEqual(main.is_monotonous([2, 2, 2, 3]), True)

    def test_4(self):
        self.assertEqual(main.is_monotonous([3]), True)

    def test_5(self):
        self.assertEqual(main.is_monotonous([4, 2, 2, 2]), True)
