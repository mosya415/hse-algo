"""Тесты к задаче 3. Запуск: python3 test_balanced_binary_tree.py"""

import unittest

from balanced_binary_tree import Node, is_balanced


class TestBalancedBinaryTree(unittest.TestCase):
    def test_empty_tree(self):
        self.assertTrue(is_balanced(None))

    def test_single_node(self):
        self.assertTrue(is_balanced(Node(1)))

    def test_two_nodes(self):
        self.assertTrue(is_balanced(Node(1, Node(2))))
        self.assertTrue(is_balanced(Node(1, None, Node(2))))

    def test_equal_heights(self):
        root = Node(8, Node(4, Node(2), Node(6)), Node(12, Node(10), Node(14)))
        self.assertTrue(is_balanced(root))

    def test_height_difference_one(self):
        root = Node(8, Node(4, Node(2), Node(6)), Node(12))
        self.assertTrue(is_balanced(root))

    def test_three_nodes_in_chain(self):
        self.assertFalse(is_balanced(Node(1, Node(2, Node(3)))))
        self.assertFalse(is_balanced(Node(1, None, Node(2, None, Node(3)))))

    def test_unbalanced_below_root(self):
        # У корня разница высот 1, но в узле 5 она равна 2.
        root = Node(10, Node(5, Node(3, Node(1))), Node(15, Node(12), Node(18)))
        self.assertFalse(is_balanced(root))

    def test_values_do_not_affect_balance(self):
        root = Node(1, Node(9), Node(1, Node(-3)))
        self.assertTrue(is_balanced(root))

    def test_deep_tree(self):
        root = Node(0)
        node = root
        for value in range(1, 1500):
            node.right = Node(value)
            node = node.right
        self.assertFalse(is_balanced(root))


if __name__ == "__main__":
    unittest.main()
