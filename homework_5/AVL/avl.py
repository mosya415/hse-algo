"""Задача 3. AVL-дерево: вставка, удаление и поиск."""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self, values=()):
        self.root = None
        for value in values:
            self.insert(value)

    def _height(self, node):
        return node.height if node is not None else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rebalance(self, node):
        self._update_height(node)
        balance = self._height(node.left) - self._height(node.right)

        if balance > 1:
            if self._height(node.left.left) < self._height(node.left.right):
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._height(node.right.right) < self._height(node.right.left):
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node
        return self._rebalance(node)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # У узла с двумя детьми берём наименьшее значение справа.
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)

        return self._rebalance(node)

    def search(self, value):
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def inorder(self):
        result = []

        def visit(node):
            if node is not None:
                visit(node.left)
                result.append(node.value)
                visit(node.right)

        visit(self.root)
        return result


if __name__ == "__main__":
    tree = AVL([40, 20, 60, 10, 30, 25])
    print("После вставки:", tree.inorder())
    print("Есть 25:", tree.search(25))
    tree.delete(60)
    tree.delete(40)
    print("После удаления 60 и 40:", tree.inorder())
    print("Есть 40:", tree.search(40))
