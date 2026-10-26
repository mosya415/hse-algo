"""Запуск: python3 test_tree_traversal.py"""

import unittest

from tree_traversal import BST


TRAVERSALS = (
    "preorder", "inorder", "postorder",
    "reverse_preorder", "reverse_inorder", "reverse_postorder",
)


class TestTreeTraversal(unittest.TestCase):
    def test_empty_tree(self):
        tree = BST()
        for name in TRAVERSALS:
            with self.subTest(traversal=name):
                self.assertEqual(getattr(tree, name)(), [])

    def test_single_node(self):
        tree = BST([5])
        for name in TRAVERSALS:
            with self.subTest(traversal=name):
                self.assertEqual(getattr(tree, name)(), [5])

    def test_insert(self):
        tree = BST([8, 3, 10, 6, 4])
        self.assertEqual(tree.root.value, 8)
        self.assertEqual(tree.root.left.value, 3)
        self.assertEqual(tree.root.right.value, 10)
        self.assertEqual(tree.root.left.right.value, 6)
        self.assertEqual(tree.root.left.right.left.value, 4)

    def test_all_traversals(self):
        tree = BST([8, 3, 10, 1, 6, 14, 4, 7, 13])
        expected = {
            "preorder": [8, 3, 1, 6, 4, 7, 10, 14, 13],
            "inorder": [1, 3, 4, 6, 7, 8, 10, 13, 14],
            "postorder": [1, 4, 7, 6, 3, 13, 14, 10, 8],
            "reverse_preorder": [8, 10, 14, 13, 3, 6, 7, 4, 1],
            "reverse_inorder": [14, 13, 10, 8, 7, 6, 4, 3, 1],
            "reverse_postorder": [13, 14, 10, 7, 4, 6, 1, 3, 8],
        }
        for name, values in expected.items():
            with self.subTest(traversal=name):
                self.assertEqual(getattr(tree, name)(), values)

    def test_duplicate_is_skipped(self):
        tree = BST([8, 3, 10, 8, 3])
        self.assertEqual(tree.preorder(), [8, 3, 10])
        self.assertEqual(tree.inorder(), [3, 8, 10])

    def test_negative_values_and_zero(self):
        tree = BST([0, -5, 3, -2, -8])
        self.assertEqual(tree.inorder(), [-8, -5, -2, 0, 3])
        self.assertEqual(tree.reverse_inorder(), [3, 0, -2, -5, -8])

    def test_deep_one_sided_trees(self):
        values = list(range(1500))
        for insertion_order in (values, values[::-1]):
            tree = BST(insertion_order)
            expected = {
                "preorder": insertion_order,
                "inorder": values,
                "postorder": insertion_order[::-1],
                "reverse_preorder": insertion_order,
                "reverse_inorder": values[::-1],
                "reverse_postorder": insertion_order[::-1],
            }
            for name, result in expected.items():
                with self.subTest(root=tree.root.value, traversal=name):
                    self.assertEqual(getattr(tree, name)(), result)


if __name__ == "__main__":
    unittest.main()
