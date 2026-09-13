"""Тесты к задаче 2. Запуск: python3 test_max_even_sum.py"""

import itertools
import random
import unittest

from max_even_sum import max_even_sum, parse_numbers


def brute_force(numbers):
    """Эталон для сверки: перебор всех подмножеств."""
    best = 0
    for size in range(len(numbers) + 1):
        for subset in itertools.combinations(numbers, size):
            total = sum(subset)
            if total % 2 == 0 and total > best:
                best = total
    return best


class TestMaxEvenSum(unittest.TestCase):
    def test_examples_from_statement(self):
        self.assertEqual(max_even_sum([5, 7, 13, 2, 14]), 36)
        self.assertEqual(max_even_sum([3]), 0)

    def test_empty_array(self):
        self.assertEqual(max_even_sum([]), 0)

    def test_single_even_element(self):
        self.assertEqual(max_even_sum([8]), 8)

    def test_all_even(self):
        self.assertEqual(max_even_sum([2, 4, 6, 100]), 112)

    def test_even_count_of_odds(self):
        # 1 + 3 + 5 + 7 = 16, чётная, выкидывать нечего.
        self.assertEqual(max_even_sum([1, 3, 5, 7]), 16)

    def test_odd_count_of_odds(self):
        # 1 + 3 + 5 = 9, нечётная, убираем единицу.
        self.assertEqual(max_even_sum([1, 3, 5]), 8)

    def test_minimal_odd_is_not_the_first_element(self):
        # Сумма 9 + 5 + 1 = 15 нечётная, убрать нужно единицу в конце.
        self.assertEqual(max_even_sum([9, 5, 1]), 14)

    def test_duplicated_minimal_odd(self):
        # Из трёх одинаковых единиц убирается ровно одна.
        self.assertEqual(max_even_sum([1, 1, 1, 10]), 12)

    def test_min_odd_is_bigger_than_some_even(self):
        # Двойка меньше тройки, но убирать её бесполезно: чётность не изменится.
        self.assertEqual(max_even_sum([2, 3]), 2)

    def test_matches_brute_force(self):
        # Решение основано на рассуждении, поэтому сверяю его с перебором.
        rnd = random.Random(42)
        for _ in range(50):
            numbers = [rnd.randint(1, 30) for _ in range(rnd.randint(0, 7))]
            with self.subTest(numbers=numbers):
                self.assertEqual(max_even_sum(numbers), brute_force(numbers))


class TestParseNumbers(unittest.TestCase):
    def test_parses_line(self):
        self.assertEqual(parse_numbers("5 7 13 2 14"), [5, 7, 13, 2, 14])

    def test_extra_whitespace(self):
        self.assertEqual(parse_numbers("  3   4\t5\n"), [3, 4, 5])

    def test_empty_line(self):
        self.assertEqual(parse_numbers("   "), [])


if __name__ == "__main__":
    unittest.main()
