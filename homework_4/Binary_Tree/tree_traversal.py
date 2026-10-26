"""Бинарное дерево поиска и шесть обходов."""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self, values=()):
        self.root = None
        for value in values:
            self.insert(value)

    def insert(self, value):
        """Добавить значение. Повторная вставка ничего не меняет."""
        if self.root is None:
            self.root = Node(value)
            return

        node = self.root
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    return
                node = node.left
            elif value > node.value:
                if node.right is None:
                    node.right = Node(value)
                    return
                node = node.right
            else:
                return

    def _traverse(self, order):
        """N: записать узел, L: обойти слева, R: обойти справа."""
        result = []
        stack = [(self.root, False)]

        while stack:
            node, visit = stack.pop()
            if node is None:
                continue
            if visit:
                result.append(node.value)
                continue

            # Стек выдаёт последнее добавленное, поэтому кладём в обратном порядке.
            for action in reversed(order):
                if action == "N":
                    stack.append((node, True))
                elif action == "L":
                    stack.append((node.left, False))
                else:
                    stack.append((node.right, False))

        return result

    def preorder(self):
        return self._traverse("NLR")

    def inorder(self):
        return self._traverse("LNR")

    def postorder(self):
        return self._traverse("LRN")

    def reverse_preorder(self):
        return self._traverse("NRL")

    def reverse_inorder(self):
        return self._traverse("RNL")

    def reverse_postorder(self):
        return self._traverse("RLN")


if __name__ == "__main__":
    tree = BST(int(value) for value in input().split())
    print("preorder:", tree.preorder())
    print("inorder:", tree.inorder())
    print("postorder:", tree.postorder())
    print("reverse preorder:", tree.reverse_preorder())
    print("reverse inorder:", tree.reverse_inorder())
    print("reverse postorder:", tree.reverse_postorder())
