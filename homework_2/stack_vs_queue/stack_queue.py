"""Задача 1. Стек и очередь на односвязных списках."""


class Node:
    """Узел односвязного списка: значение и ссылка на следующий узел."""

    __slots__ = ("value", "next")

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Stack:
    """Стек, LIFO. Голова списка это вершина стека."""

    def __init__(self, values=()):
        self._head = None
        self._size = 0
        for value in values:
            self.push(value)

    def push(self, value):
        """Положить значение на вершину."""
        self._head = Node(value, self._head)
        self._size += 1

    def pop(self):
        """Снять значение с вершины и вернуть его."""
        if self._head is None:
            raise IndexError("pop из пустого стека")
        node = self._head
        self._head = node.next
        self._size -= 1
        return node.value

    def peek(self):
        """Посмотреть вершину, не снимая её."""
        if self._head is None:
            raise IndexError("peek у пустого стека")
        return self._head.value

    def is_empty(self):
        return self._head is None

    def __len__(self):
        return self._size

    def __iter__(self):
        """Обход от вершины к дну, сам стек не меняется."""
        node = self._head
        while node is not None:
            yield node.value
            node = node.next


class Queue:
    """Очередь, FIFO. Голова списка это начало очереди, хвост это конец."""

    def __init__(self, values=()):
        self._head = None
        self._tail = None
        self._size = 0
        for value in values:
            self.enqueue(value)

    def enqueue(self, value):
        """Добавить значение в конец очереди."""
        node = Node(value)
        if self._tail is None:
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        """Забрать значение из начала очереди."""
        if self._head is None:
            raise IndexError("dequeue из пустой очереди")
        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.value

    def peek(self):
        """Посмотреть начало очереди, не забирая элемент."""
        if self._head is None:
            raise IndexError("peek у пустой очереди")
        return self._head.value

    def is_empty(self):
        return self._head is None

    def __len__(self):
        return self._size

    def __iter__(self):
        """Обход от начала очереди к концу, сама очередь не меняется."""
        node = self._head
        while node is not None:
            yield node.value
            node = node.next


def main() -> None:
    stack = Stack([1, 2, 3])
    queue = Queue([1, 2, 3])
    print("стек:  ", [stack.pop() for _ in range(len(stack))])
    print("очередь:", [queue.dequeue() for _ in range(len(queue))])


if __name__ == "__main__":
    main()
