"""Тесты к задаче 2. Запуск из homework_5: python3 -m unittest permutations.test_permutations"""

import io
import unittest
from contextlib import redirect_stdout

from permutations.permutations import permutations


class TestPermutations(unittest.TestCase):
    def test_examples_from_statement(self):
        self.assertEqual(permutations([1, 2, 3], trace=False), [
            [1, 2, 3], [1, 3, 2], [2, 1, 3],
            [2, 3, 1], [3, 1, 2], [3, 2, 1],
        ])
        self.assertEqual(permutations([0, 1], trace=False), [[0, 1], [1, 0]])
        self.assertEqual(permutations([1], trace=False), [[1]])

    def test_empty_array(self):
        self.assertEqual(permutations([], trace=False), [[]])

    def test_negative_values_and_zero(self):
        self.assertEqual(permutations([0, -1, 2], trace=False), [
            [0, -1, 2], [0, 2, -1], [-1, 0, 2],
            [-1, 2, 0], [2, 0, -1], [2, -1, 0],
        ])

    def test_unsorted_input(self):
        self.assertEqual(permutations([3, 1, 2], trace=False), [
            [3, 1, 2], [3, 2, 1], [1, 3, 2],
            [1, 2, 3], [2, 3, 1], [2, 1, 3],
        ])

    def test_repeated_values(self):
        self.assertEqual(permutations([1, 1, 2], trace=False), [
            [1, 1, 2], [1, 2, 1], [2, 1, 1],
        ])

    def test_all_values_equal(self):
        self.assertEqual(permutations([4, 4, 4], trace=False), [[4, 4, 4]])

    def test_four_elements(self):
        result = permutations([2, 4, 6, 8], trace=False)
        self.assertEqual(len(result), 24)
        self.assertEqual(len({tuple(row) for row in result}), 24)
        for row in result:
            self.assertEqual(sorted(row), [2, 4, 6, 8])

    def test_trace_is_enabled_by_default(self):
        output = io.StringIO()
        with redirect_stdout(output):
            result = permutations([2, 4])
        self.assertEqual(result, [[2, 4], [4, 2]])
        self.assertEqual(output.getvalue().splitlines(), [
            "-> generate([2, 4])",
            "  -> generate([4])",
            "    -> generate([])",
            "    <- generate = [[]]",
            "  <- generate = [[4]]",
            "  -> generate([2])",
            "    -> generate([])",
            "    <- generate = [[]]",
            "  <- generate = [[2]]",
            "<- generate = [[2, 4], [4, 2]]",
        ])

    def test_trace_can_be_disabled(self):
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(permutations([1], trace=False), [[1]])
        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
