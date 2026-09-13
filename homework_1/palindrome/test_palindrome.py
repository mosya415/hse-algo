"""Тесты к задаче 1. Запуск: python3 test_palindrome.py"""

import unittest

from palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_examples_from_statement(self):
        self.assertTrue(is_palindrome(121))
        self.assertFalse(is_palindrome(31))

    def test_single_digits(self):
        for digit in range(10):
            with self.subTest(digit=digit):
                self.assertTrue(is_palindrome(digit))

    def test_palindromes(self):
        for number in (11, 1221, 9009, 101, 12321, 9876789):
            with self.subTest(number=number):
                self.assertTrue(is_palindrome(number))

    def test_not_palindromes(self):
        for number in (12, 123, 1231, 100):
            with self.subTest(number=number):
                self.assertFalse(is_palindrome(number))

    def test_trailing_zero(self):
        for number in (10, 100, 1210, 1000000):
            with self.subTest(number=number):
                self.assertFalse(is_palindrome(number))

    def test_middle_digit_does_not_break_palindrome(self):
        # Центральная цифра сама себе зеркало, её замена ничего не ломает.
        self.assertTrue(is_palindrome(1234321))
        self.assertTrue(is_palindrome(1235321))

    def test_broken_mirror_pair(self):
        # Расхождение ровно в одной зеркальной паре.
        self.assertFalse(is_palindrome(1234329))
        self.assertFalse(is_palindrome(1934321))
        self.assertFalse(is_palindrome(1244321))

    def test_matches_string_check(self):
        # Сверка со строковой проверкой на всех числах до 1000.
        for number in range(1000):
            with self.subTest(number=number):
                self.assertEqual(is_palindrome(number), str(number) == str(number)[::-1])

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            is_palindrome(-121)


if __name__ == "__main__":
    unittest.main()
