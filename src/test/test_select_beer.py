import unittest
from src.main.select_beer import select_kinds_of_beer


class TestSelectBeer(unittest.TestCase):
    path_to_files = "../test/"

    def test_1(self):
        input_file = self.path_to_files + 'test_input_file_1.txt'
        self.assertEqual(select_kinds_of_beer(input_file, ''), 2)

    def test_2(self):
        input_file = self.path_to_files + 'test_input_file_2.txt'
        self.assertEqual(select_kinds_of_beer(input_file, ''), 2)

    def test_empty_input(self):
        input_file = self.path_to_files + 'test_input_file_3.txt'
        self.assertEqual(select_kinds_of_beer(input_file, ''), "Incorrect input data")

    def test_all_employer_like_all_beer(self):
        input_file = self.path_to_files + 'test_input_file_4.txt'
        self.assertEqual(select_kinds_of_beer(input_file, ''), 1)

    def test_3(self):
        input_file = self.path_to_files + 'test_input_file_5.txt'
        self.assertEqual(select_kinds_of_beer(input_file, ''), 2)

    def test_4(self):
        input_file = self.path_to_files + 'test_input_file_6.txt'
        self.assertEqual(select_kinds_of_beer(input_file, ''), 4)

    def test_5(self):
        input_file = self.path_to_files + 'test_input_file_7.txt'
        self.assertEqual(select_kinds_of_beer(input_file, ''), 2)

    def test_6(self):
        input_file = self.path_to_files + 'test_input_file_8.txt'
        self.assertEqual(select_kinds_of_beer(input_file, ''), 2)
