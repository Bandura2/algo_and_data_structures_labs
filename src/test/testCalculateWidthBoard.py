import unittest
import main


class TestCalculationWidth(unittest.TestCase):
    def test_first(self):
        self.assertEqual(main.calculate_width_board(10, 2, 3), 9)

    def test_second(self):
        self.assertEqual(main.calculate_width_board(2, 1000000000, 999999999), (-1, -1))

    def test_third(self):
        self.assertEqual(main.calculate_width_board(4, 1, 1), (-1, -1))

    def test_none_card(self):
        self.assertEqual(main.calculate_width_board(0, 2, 4), (-1, -1))

    def test_square_card(self):
        self.assertEqual(main.calculate_width_board(10, 2, 2), (-1, -1))

    def test_max_numbers_card(self):
        self.assertEqual(main.calculate_width_board(1012, 7, 4), (-1, -1))

    def test_max_weidth_card(self):
        self.assertEqual(main.calculate_width_board(12, 109, 4), (-1, -1))

    def test_max_heigth_card(self):
        self.assertEqual(main.calculate_width_board(12, 14, 109), (-1, -1))

    def test_any_test(self):
        self.assertEqual(main.calculate_width_board(501, 108, 23), 1173)

    def test_any_test_2(self):
        self.assertEqual(main.calculate_width_board(240, 50, 99), 1100)
