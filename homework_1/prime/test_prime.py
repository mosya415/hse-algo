"""Тесты к задаче 3. Запуск: python3 test_prime.py"""

import unittest

from prime import count_primes


def is_prime_naive(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


class TestCountPrimes(unittest.TestCase):
    def test_examples_from_statement(self):
        self.assertEqual(count_primes(10), 4)   # 2, 3, 5, 7
        self.assertEqual(count_primes(1), 0)

    def test_small_values(self):
        expected = {0: 0, 1: 0, 2: 0, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 4}
        for n, value in expected.items():
            with self.subTest(n=n):
                self.assertEqual(count_primes(n), value)

    def test_negative_input(self):
        self.assertEqual(count_primes(-5), 0)

    def test_bound_is_exclusive(self):
        # 7 простое: при N = 7 оно не считается, при N = 8 уже считается.
        self.assertEqual(count_primes(7), 3)
        self.assertEqual(count_primes(8), 4)

    def test_known_values(self):
        for n, value in ((100, 25), (1000, 168), (10 ** 4, 1229)):
            with self.subTest(n=n):
                self.assertEqual(count_primes(n), value)

    def test_square_of_prime(self):
        # 25 = 5 * 5 вычёркивается только на шаге p = 5.
        self.assertEqual(count_primes(25), 9)
        self.assertEqual(count_primes(26), 9)
        self.assertEqual(count_primes(27), 9)

    def test_matches_naive_check(self):
        expected = 0
        for n in range(300):
            with self.subTest(n=n):
                self.assertEqual(count_primes(n), expected)
            if is_prime_naive(n):
                expected += 1


if __name__ == "__main__":
    unittest.main()
