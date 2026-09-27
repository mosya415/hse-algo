"""Тесты к задаче 1. Запуск: python3 test_two_sum.py"""

import unittest

from two_sum import parse_numbers, two_sum


class TestTwoSum(unittest.TestCase):
    def test_examples_from_statement(self):
        self.assertEqual(two_sum([1, 3, 4, 10], 7), (1, 2))
        self.assertEqual(two_sum([5, 5, 1, 4], 10), (0, 1))

    def test_two_elements(self):
        self.assertEqual(two_sum([2, 5], 7), (0, 1))

    def test_pair_at_the_ends(self):
        self.assertEqual(two_sum([9, 2, 3, 4, 1], 10), (0, 4))

    def test_neighbours(self):
        self.assertEqual(two_sum([1, 2, 3, 4], 7), (2, 3))

    def test_negative_numbers(self):
        self.assertEqual(two_sum([-3, 7, 1, -5], -8), (0, 3))
        self.assertEqual(two_sum([-1, 4, 2], 1), (0, 2))

    def test_zero_sum(self):
        self.assertEqual(two_sum([4, 0, -4], 0), (0, 2))

    def test_equal_elements(self):
        # Два одинаковых числа это разные индексы, пара законная.
        self.assertEqual(two_sum([3, 3], 6), (0, 1))

    def test_element_is_not_paired_with_itself(self):
        # 6 + 6 = 12, но шестёрка в массиве одна, ответ даёт другая пара.
        self.assertEqual(two_sum([6, 5, 7], 12), (1, 2))

    def test_indices_are_ascending(self):
        first, second = two_sum([10, 1, 3, 4], 7)
        self.assertLess(first, second)

    def test_no_pair(self):
        self.assertIsNone(two_sum([1, 2, 3], 100))
        self.assertIsNone(two_sum([], 5))

    def test_large_array(self):
        # Единственная пара это два последних элемента, то есть перебор парами
        # дошёл бы до неё в самом конце.
        arr = list(range(100_000))
        self.assertEqual(two_sum(arr, 99_998 + 99_999), (99_998, 99_999))


class TestParseNumbers(unittest.TestCase):
    def test_parses_line(self):
        self.assertEqual(parse_numbers("1 3 4 10"), [1, 3, 4, 10])

    def test_extra_whitespace(self):
        self.assertEqual(parse_numbers(" -3   7\t1\n"), [-3, 7, 1])


if __name__ == "__main__":
    unittest.main()
