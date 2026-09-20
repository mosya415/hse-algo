"""Тесты к задаче 1. Запуск: python3 test_stack_queue.py"""

import unittest

from stack_queue import Queue, Stack


class TestStack(unittest.TestCase):
    def test_new_stack_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)

    def test_lifo_order(self):
        stack = Stack()
        for value in (1, 2, 3):
            stack.push(value)
        self.assertEqual([stack.pop(), stack.pop(), stack.pop()], [3, 2, 1])
        self.assertTrue(stack.is_empty())

    def test_peek_does_not_remove(self):
        stack = Stack([1, 2])
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.pop(), 2)

    def test_pop_from_empty(self):
        with self.assertRaises(IndexError):
            Stack().pop()
        with self.assertRaises(IndexError):
            Stack().peek()

    def test_push_after_emptying(self):
        # Стек опустошается и снова наполняется: голова должна корректно
        # вернуться из None.
        stack = Stack([1, 2])
        stack.pop()
        stack.pop()
        stack.push(7)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.pop(), 7)

    def test_mixed_operations(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual([stack.pop(), stack.pop()], [3, 1])

    def test_iteration_from_top(self):
        stack = Stack([1, 2, 3])
        self.assertEqual(list(stack), [3, 2, 1])
        self.assertEqual(len(stack), 3)

    def test_many_elements(self):
        stack = Stack(range(1000))
        self.assertEqual(len(stack), 1000)
        self.assertEqual([stack.pop() for _ in range(1000)], list(reversed(range(1000))))


class TestQueue(unittest.TestCase):
    def test_new_queue_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(len(queue), 0)

    def test_fifo_order(self):
        queue = Queue()
        for value in (1, 2, 3):
            queue.enqueue(value)
        self.assertEqual([queue.dequeue(), queue.dequeue(), queue.dequeue()], [1, 2, 3])
        self.assertTrue(queue.is_empty())

    def test_peek_does_not_remove(self):
        queue = Queue([1, 2])
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(len(queue), 2)
        self.assertEqual(queue.dequeue(), 1)

    def test_dequeue_from_empty(self):
        with self.assertRaises(IndexError):
            Queue().dequeue()
        with self.assertRaises(IndexError):
            Queue().peek()

    def test_enqueue_after_emptying(self):
        # Здесь легко потерять хвост: после опустошения он должен обнулиться,
        # иначе новый элемент привяжется к выброшенному узлу.
        queue = Queue([1, 2])
        queue.dequeue()
        queue.dequeue()
        queue.enqueue(7)
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue.dequeue(), 7)
        self.assertTrue(queue.is_empty())

    def test_mixed_operations(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 2)
        queue.enqueue(4)
        self.assertEqual([queue.dequeue(), queue.dequeue()], [3, 4])

    def test_iteration_from_head(self):
        queue = Queue([1, 2, 3])
        self.assertEqual(list(queue), [1, 2, 3])
        self.assertEqual(len(queue), 3)

    def test_many_elements(self):
        queue = Queue(range(1000))
        self.assertEqual(len(queue), 1000)
        self.assertEqual([queue.dequeue() for _ in range(1000)], list(range(1000)))


class TestDifference(unittest.TestCase):
    def test_same_input_opposite_order(self):
        # Ровно та разница, ради которой задача и называется stack vs queue.
        values = [1, 2, 3, 4]
        stack = Stack(values)
        queue = Queue(values)
        self.assertEqual([stack.pop() for _ in values], [4, 3, 2, 1])
        self.assertEqual([queue.dequeue() for _ in values], [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
