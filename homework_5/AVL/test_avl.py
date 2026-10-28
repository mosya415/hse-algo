"""Тесты к задаче 3. Запуск из homework_5: python3 -m unittest AVL.test_avl"""

import unittest

from AVL.avl import AVL


class TestAVL(unittest.TestCase):
    def check_tree(self, tree, expected):
        values = []

        def visit(node, lower=None, upper=None):
            if node is None:
                return 0
            if lower is not None:
                self.assertGreater(node.value, lower)
            if upper is not None:
                self.assertLess(node.value, upper)

            left_height = visit(node.left, lower, node.value)
            values.append(node.value)
            right_height = visit(node.right, node.value, upper)
            height = 1 + max(left_height, right_height)
            self.assertEqual(node.height, height)
            self.assertLessEqual(abs(left_height - right_height), 1)
            return height

        visit(tree.root)
        self.assertEqual(values, sorted(expected))
        self.assertEqual(tree.inorder(), values)

    def test_empty_tree(self):
        tree = AVL()
        self.assertFalse(tree.search(1))
        self.assertIsNone(tree.root)
        self.check_tree(tree, [])

    def test_single_node(self):
        tree = AVL([8])
        self.assertTrue(tree.search(8))
        self.assertEqual(tree.root.height, 1)
        self.check_tree(tree, [8])

    def test_four_insertion_rotations(self):
        cases = (
            ("LL", [30, 20, 10]),
            ("RR", [10, 20, 30]),
            ("LR", [30, 10, 20]),
            ("RL", [10, 30, 20]),
        )
        for name, values in cases:
            with self.subTest(rotation=name):
                tree = AVL()
                for index, value in enumerate(values):
                    tree.insert(value)
                    self.check_tree(tree, values[:index + 1])
                self.assertEqual(tree.root.value, 20)

    def test_duplicate_is_skipped(self):
        tree = AVL([8, 3, 10, 8, 3])
        self.check_tree(tree, [3, 8, 10])

    def test_negative_values_and_zero(self):
        tree = AVL([0, -4, 7, -2, -8])
        self.check_tree(tree, [-8, -4, -2, 0, 7])
        self.assertTrue(tree.search(0))
        self.assertTrue(tree.search(-8))

    def test_search(self):
        tree = AVL([40, 20, 60, 10, 30, 25])
        for value in (40, 20, 60, 10, 30, 25):
            self.assertTrue(tree.search(value))
        self.assertFalse(tree.search(0))
        self.assertFalse(tree.search(100))

    def test_delete_leaf(self):
        tree = AVL([20, 10, 30])
        tree.delete(10)
        self.assertFalse(tree.search(10))
        self.check_tree(tree, [20, 30])

    def test_delete_node_with_one_child(self):
        tree = AVL([20, 10, 30, 25])
        tree.delete(30)
        self.check_tree(tree, [10, 20, 25])

    def test_delete_node_with_two_children(self):
        tree = AVL([20, 10, 30, 5, 15, 25, 35])
        tree.delete(20)
        self.assertFalse(tree.search(20))
        self.check_tree(tree, [5, 10, 15, 25, 30, 35])

    def test_delete_successor_with_right_child(self):
        tree = AVL([40, 20, 60, 10, 30, 50, 70, 55])
        tree.delete(40)
        self.check_tree(tree, [10, 20, 30, 50, 55, 60, 70])

    def test_delete_single_root(self):
        tree = AVL([9])
        tree.delete(9)
        self.assertIsNone(tree.root)
        self.check_tree(tree, [])

    def test_delete_root_with_one_child(self):
        tree = AVL([9, 4])
        tree.delete(9)
        self.assertEqual(tree.root.value, 4)
        self.check_tree(tree, [4])

    def test_delete_missing_value(self):
        tree = AVL([10, 5, 15])
        tree.delete(99)
        self.check_tree(tree, [5, 10, 15])
        empty = AVL()
        empty.delete(1)
        self.check_tree(empty, [])

    def test_four_deletion_rotations(self):
        cases = (
            ("LL", [4, 2, 5, 1, 3], 5, 2),
            ("RR", [2, 1, 4, 3, 5], 1, 4),
            ("LR", [5, 2, 7, 1, 4, 8, 3], 8, 4),
            ("RL", [5, 3, 8, 2, 6, 9, 7], 2, 6),
        )
        for name, values, removed, root_value in cases:
            with self.subTest(rotation=name):
                tree = AVL(values)
                self.check_tree(tree, values)
                tree.delete(removed)
                self.assertEqual(tree.root.value, root_value)
                self.check_tree(tree, [value for value in values if value != removed])

    def test_example_from_readme(self):
        tree = AVL([40, 20, 60, 10, 30, 25])
        self.assertEqual(tree.root.value, 30)
        self.check_tree(tree, [10, 20, 25, 30, 40, 60])
        tree.delete(60)
        self.check_tree(tree, [10, 20, 25, 30, 40])
        tree.delete(40)
        self.assertEqual(tree.root.value, 20)
        self.check_tree(tree, [10, 20, 25, 30])

    def test_sequential_insertions_and_deletions(self):
        tree = AVL()
        expected = set()
        for value in range(40):
            tree.insert(value)
            expected.add(value)
            self.check_tree(tree, expected)

        for value in list(range(0, 40, 2)) + list(range(1, 40, 2)):
            tree.delete(value)
            expected.remove(value)
            self.assertFalse(tree.search(value))
            self.check_tree(tree, expected)
        self.assertIsNone(tree.root)


if __name__ == "__main__":
    unittest.main()
