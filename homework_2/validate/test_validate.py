"""Тесты к задаче 2. Запуск: python3 test_validate.py"""

import unittest

from validate import parse_numbers, validate


class TestValidate(unittest.TestCase):
    def test_examples_from_statement(self):
        self.assertTrue(validate([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]))
        self.assertFalse(validate([1, 2, 3], [3, 1, 2]))

    def test_single_element(self):
        self.assertTrue(validate([1], [1]))

    def test_empty(self):
        self.assertTrue(validate([], []))

    def test_same_order(self):
        # Каждый push сразу гасится pop.
        self.assertTrue(validate([1, 2, 3, 4], [1, 2, 3, 4]))

    def test_reversed_order(self):
        # Сначала все push, потом все pop.
        self.assertTrue(validate([1, 2, 3, 4], [4, 3, 2, 1]))

    def test_pop_from_the_middle(self):
        self.assertTrue(validate([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))

    def test_order_broken_deeper_in_stack(self):
        # 1 лежит под 2 и 3, взять его раньше них нельзя.
        self.assertFalse(validate([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
        self.assertFalse(validate([1, 2, 3, 4], [2, 4, 1, 3]))

    def test_different_lengths(self):
        self.assertFalse(validate([1, 2, 3], [1, 2]))

    def test_large_input(self):
        # Верхняя граница из условия, обратный порядок.
        n = 100_000
        pushed = list(range(n))
        self.assertTrue(validate(pushed, pushed[::-1]))
        # И невозможный вариант той же длины: после последнего элемента
        # снять можно только предпоследний, а не первый.
        self.assertFalse(validate(pushed, [n - 1] + pushed[:-1]))


class TestParseNumbers(unittest.TestCase):
    def test_parses_line(self):
        self.assertEqual(parse_numbers("1 2 3 4 5"), [1, 2, 3, 4, 5])

    def test_extra_whitespace(self):
        self.assertEqual(parse_numbers("  1   2\t3\n"), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
