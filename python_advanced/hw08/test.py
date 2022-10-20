import unittest
from hw08 import find_anagrams


class TestFindAnagrams(unittest.TestCase):

    def test_empty_answer(self):
        text, pattern = "a", "b"
        self.assertEqual(find_anagrams(text, pattern), [])

        text, pattern = "a b c", "abc"
        self.assertEqual(find_anagrams(text, pattern), [])

        text, pattern = "defgh", "abc"
        self.assertEqual(find_anagrams(text, pattern), [])

        text, pattern = "", "abc"
        self.assertEqual(find_anagrams(text, pattern), [])

        text, pattern = "   ", "abc"
        self.assertEqual(find_anagrams(text, pattern), [])

    def test_single_answer(self):
        text, pattern = "a", "a"
        self.assertEqual(find_anagrams(text, pattern), [0])

        text, pattern = "xyzbca", "abc"
        self.assertEqual(find_anagrams(text, pattern), [3])

        text, pattern = "xayabzabc", "abc"
        self.assertEqual(find_anagrams(text, pattern), [6])

    def test_another_cases(self):
        text, pattern = "abcba", "abc"
        self.assertEqual(find_anagrams(text, pattern), [0, 2])

        text, pattern = "aaa", "a"
        self.assertEqual(find_anagrams(text, pattern), [0, 1, 2])

        text, pattern = "abc cba xabcd", "abc"
        self.assertEqual(find_anagrams(text, pattern), [0, 4, 9])

        text, pattern = "abcab", "abc"
        self.assertEqual(find_anagrams(text, pattern), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
