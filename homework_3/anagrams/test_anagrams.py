"""Тесты к задаче 2. Запуск: python3 test_anagrams.py"""

import unittest

from anagrams import group_anagrams


class TestGroupAnagrams(unittest.TestCase):
    def test_example_from_statement(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.assertEqual(
            group_anagrams(words),
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        )

    def test_empty_input(self):
        self.assertEqual(group_anagrams([]), [])

    def test_single_word(self):
        self.assertEqual(group_anagrams(["abc"]), [["abc"]])

    def test_no_anagrams(self):
        self.assertEqual(group_anagrams(["one", "two", "six"]), [["one"], ["two"], ["six"]])

    def test_all_in_one_group(self):
        self.assertEqual(group_anagrams(["abc", "bca", "cab"]), [["abc", "bca", "cab"]])

    def test_repeated_words(self):
        # Одинаковые слова тоже анаграммы друг друга, обе копии остаются.
        self.assertEqual(group_anagrams(["eat", "eat", "tea"]), [["eat", "eat", "tea"]])

    def test_empty_strings(self):
        self.assertEqual(group_anagrams(["", "", "a"]), [["", ""], ["a"]])

    def test_letter_counts_matter(self):
        # Набор букв один и тот же, но количества разные - это не анаграммы.
        self.assertEqual(group_anagrams(["aab", "abb"]), [["aab"], ["abb"]])
        self.assertEqual(group_anagrams(["aab", "aba", "baa"]), [["aab", "aba", "baa"]])

    def test_different_lengths_never_group(self):
        self.assertEqual(group_anagrams(["ab", "aab", "ba"]), [["ab", "ba"], ["aab"]])

    def test_case_matters(self):
        # Заглавная и строчная это разные символы.
        self.assertEqual(group_anagrams(["Tea", "eat"]), [["Tea"], ["eat"]])

    def test_non_latin(self):
        self.assertEqual(group_anagrams(["ток", "кот", "рот"]), [["ток", "кот"], ["рот"]])

    def test_order_follows_input(self):
        # Группы идут в порядке первого появления, слова внутри - как во входе.
        self.assertEqual(
            group_anagrams(["bat", "tab", "cat", "abt"]),
            [["bat", "tab", "abt"], ["cat"]],
        )

    def test_many_words(self):
        words = ["ab", "ba"] * 1000
        groups = group_anagrams(words)
        self.assertEqual(len(groups), 1)
        self.assertEqual(len(groups[0]), 2000)


if __name__ == "__main__":
    unittest.main()
