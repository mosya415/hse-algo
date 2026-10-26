"""Проверка баланса высот бинарного дерева."""


def is_balanced(root):
    if root is None:
        return True

    heights = {}
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if not visited:
            # К узлу вернёмся после его детей, когда их высоты уже известны.
            stack.append((node, True))
            if node.right is not None:
                stack.append((node.right, False))
            if node.left is not None:
                stack.append((node.left, False))
        else:
            left_height = heights.get(node.left, 0)
            right_height = heights.get(node.right, 0)
            if abs(left_height - right_height) > 1:
                return False
            heights[node] = 1 + max(left_height, right_height)

    return True


if __name__ == "__main__":
    from tree_traversal import Node

    tree = Node(8, Node(4, Node(2), Node(6)), Node(12, None, Node(14)))
    print(is_balanced(tree))
