from src.main.main import kmp
import unittest


class TestKPM(unittest.TestCase):

    def test_1(self):
        haystack = "aavcbc abcabcc vf abcabcc"
        needle = "abcabcc"
        self.assertEqual(kmp(haystack, needle), [7, 18])

    def test_2(self):
        haystack = "abcabcc vf abcabcc"
        needle = "abcabcc"
        self.assertEqual(kmp(haystack, needle), [0, 11])

    def test_3(self):
        haystack = "aaa aaa aaa"
        needle = "aaa"
        self.assertEqual(kmp(haystack, needle), [0, 4, 8])

    def test_4(self):
        haystack = "abcabcc vf abcabcc"
        needle = ""
        self.assertEqual(kmp(haystack, needle), [])

    def test_5(self):
        haystack = ""
        needle = "abcabcc"
        self.assertEqual(kmp(haystack, needle), [])

    def test_6(self):
        haystack = "abc abc abc"
        needle = "abcabcc"
        self.assertEqual(kmp(haystack, needle), [])

    def test_7(self):
        haystack = "abacabacabac"
        needle = "abac"
        self.assertEqual(kmp(haystack, needle), [0, 4, 8])

    def test_8(self):
        haystack = "abc_abc abc - abc"
        needle = haystack
        self.assertEqual(kmp(haystack, needle), [0])

    def test_9(self):
        haystack = "aaaaaaaaaa       "
        needle = "a"
        self.assertEqual(kmp(haystack, needle), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_10(self):
        haystack = "          a,a"
        needle = "a"
        self.assertEqual(kmp(haystack, needle), [10, 12])

    def test_11(self):
        haystack = "abcabccabcabccabcabcc"
        needle = "abcabcc"
        self.assertEqual(kmp(haystack, needle), [0, 7, 14])

    def test_12(self):
        haystack = "abababab"
        needle = "ab"
        self.assertEqual(kmp(haystack, needle), [0, 2, 4, 6])

    def test_13(self):
        haystack = "abcd"
        needle = "abc"
        self.assertEqual(kmp(haystack, needle), [0])

    def test_14(self):
        haystack = "abababab"
        needle = "aba"
        self.assertEqual(kmp(haystack, needle), [0, 2, 4])

    def test_15(self):
        haystack = "abcdeabcde"
        needle = "abcde"
        self.assertEqual(kmp(haystack, needle), [0, 5])

    def test_16(self):
        haystack = "aaaaa"
        needle = "aa"
        self.assertEqual(kmp(haystack, needle), [0, 1, 2, 3])

    def test_17(self):
        haystack = "abcabcabc"
        needle = "abcabcabc"
        self.assertEqual(kmp(haystack, needle), [0])

    def test_18(self):
        haystack = "abcabca"
        needle = "abcabc"
        self.assertEqual(kmp(haystack, needle), [0])

    def test_19(self):
        haystack = "abcde"
        needle = "e"
        self.assertEqual(kmp(haystack, needle), [4])
