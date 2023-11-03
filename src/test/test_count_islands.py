import unittest
from src.main.main import count_islands


class TestCountIslands(unittest.TestCase):
    def test_1(self):
        map = [
            [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        ]
        self.assertEqual(count_islands(map), 7)

    def test_2(self):
        map = [
            [1, 0, 0],
            [0, 0, 1],
            [1, 0, 0]
        ]
        self.assertEqual(count_islands(map), 3)

    def test_3(self):
        map = [[]]
        self.assertEqual(count_islands(map), 0)

    def test_4(self):
        map = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(count_islands(map), 1)
