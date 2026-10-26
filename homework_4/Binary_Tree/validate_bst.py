"""Проверка произвольного бинарного дерева на свойства BST."""


def is_valid_bst(root):
    if root is None:
        return True

    # Вместе с узлом храним строгие нижнюю и верхнюю границы его значения.
    stack = [(root, None, None)]
    while stack:
        node, lower, upper = stack.pop()
        if lower is not None and node.value <= lower:
            return False
        if upper is not None and node.value >= upper:
            return False

        if node.right is not None:
            stack.append((node.right, node.value, upper))
        if node.left is not None:
            stack.append((node.left, lower, node.value))

    return True


if __name__ == "__main__":
    from tree_traversal import Node

    tree = Node(10, Node(5), Node(15, Node(6), Node(20)))
    print(is_valid_bst(tree))
