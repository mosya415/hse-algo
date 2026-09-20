"""Тесты к задаче 3. Запуск: python3 test_merge_lists.py"""

import unittest

from merge_lists import build_list, merge_with_dummy, merge_without_dummy, to_list

MERGES = (merge_with_dummy, merge_without_dummy)


class TestMerge(unittest.TestCase):
    def check(self, values1, values2, expected):
        """Обе реализации должны давать один и тот же результат."""
        for merge in MERGES:
            with self.subTest(merge=merge.__name__):
                head = merge(build_list(values1), build_list(values2))
                self.assertEqual(to_list(head), expected)

    def test_example_from_statement(self):
        self.check([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])

    def test_both_empty(self):
        self.check([], [], [])

    def test_one_empty(self):
        self.check([], [1, 2, 3], [1, 2, 3])
        self.check([1, 2, 3], [], [1, 2, 3])

    def test_single_elements(self):
        self.check([2], [1], [1, 2])
        self.check([1], [2], [1, 2])

    def test_one_list_entirely_smaller(self):
        self.check([1, 2, 3], [7, 8, 9], [1, 2, 3, 7, 8, 9])
        self.check([7, 8, 9], [1, 2, 3], [1, 2, 3, 7, 8, 9])

    def test_different_lengths(self):
        self.check([1], [2, 3, 4, 5], [1, 2, 3, 4, 5])
        self.check([0, 10], [1, 2, 3], [0, 1, 2, 3, 10])

    def test_duplicates(self):
        self.check([2, 2, 2], [2, 2], [2, 2, 2, 2, 2])

    def test_negative_values(self):
        self.check([-5, -1, 0], [-3, 4], [-5, -3, -1, 0, 4])

    def test_result_reuses_original_nodes(self):
        # По условию новый список собирается из узлов исходных, а не из копий.
        for merge in MERGES:
            with self.subTest(merge=merge.__name__):
                list1 = build_list([1, 2, 4])
                list2 = build_list([1, 3, 4])
                originals = set()
                for head in (list1, list2):
                    node = head
                    while node is not None:
                        originals.add(id(node))
                        node = node.next

                node = merge(list1, list2)
                while node is not None:
                    self.assertIn(id(node), originals)
                    node = node.next

    def test_long_lists(self):
        odd = list(range(1, 2000, 2))
        even = list(range(0, 2000, 2))
        self.check(odd, even, list(range(2000)))


if __name__ == "__main__":
    unittest.main()
