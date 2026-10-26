"""Запуск: python3 test_validate_bst.py"""

import unittest

from tree_traversal import Node
from validate_bst import is_valid_bst


class TestValidateBST(unittest.TestCase):
    def test_empty_tree(self):
        self.assertTrue(is_valid_bst(None))

    def test_single_node(self):
        self.assertTrue(is_valid_bst(Node(0)))

    def test_valid_tree(self):
        root = Node(0, Node(-4, Node(-6), Node(-1)), Node(5, Node(2), Node(9)))
        self.assertTrue(is_valid_bst(root))

    def test_wrong_child(self):
        self.assertFalse(is_valid_bst(Node(5, Node(6))))
        self.assertFalse(is_valid_bst(Node(5, None, Node(4))))

    def test_right_subtree_breaks_root_bound(self):
        root = Node(10, Node(5), Node(15, Node(6), Node(20)))
        self.assertFalse(is_valid_bst(root))

    def test_left_subtree_breaks_root_bound(self):
        root = Node(10, Node(5, None, Node(12)), Node(15))
        self.assertFalse(is_valid_bst(root))

    def test_equal_values_are_invalid(self):
        roots = (
            Node(5, Node(5)),
            Node(5, None, Node(5)),
            Node(10, Node(5, None, Node(10)), Node(15)),
        )
        for root in roots:
            with self.subTest(root=root):
                self.assertFalse(is_valid_bst(root))

    def test_deep_tree(self):
        root = Node(0)
        node = root
        for value in range(1, 1500):
            node.right = Node(value)
            node = node.right
        self.assertTrue(is_valid_bst(root))

        node.right = Node(-1)
        self.assertFalse(is_valid_bst(root))


if __name__ == "__main__":
    unittest.main()
