"""Тесты к задаче 1. Запуск из homework_5: python3 -m unittest tracer.test_tracer"""

import io
import unittest
from contextlib import redirect_stdout

from tracer.tracer import tracer


class TestTracer(unittest.TestCase):
    def test_recursive_calls_and_results(self):
        @tracer
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)

        output = io.StringIO()
        with redirect_stdout(output):
            result = factorial(3)

        self.assertEqual(result, 6)
        self.assertEqual(output.getvalue().splitlines(), [
            "-> factorial(3)",
            "  -> factorial(2)",
            "    -> factorial(1)",
            "    <- factorial = 1",
            "  <- factorial = 2",
            "<- factorial = 6",
        ])

    def test_branching_recursion(self):
        @tracer
        def fib(n):
            if n < 2:
                return n
            return fib(n - 1) + fib(n - 2)

        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(fib(2), 1)
        self.assertEqual(output.getvalue().splitlines(), [
            "-> fib(2)",
            "  -> fib(1)",
            "  <- fib = 1",
            "  -> fib(0)",
            "  <- fib = 0",
            "<- fib = 1",
        ])

    def test_keyword_arguments(self):
        @tracer
        def multiply(left, right=1):
            return left * right

        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(multiply(3, right=4), 12)
        self.assertEqual(output.getvalue().splitlines(), [
            "-> multiply(3, right=4)",
            "<- multiply = 12",
        ])

    def test_no_arguments_and_none_result(self):
        @tracer
        def empty():
            return None

        output = io.StringIO()
        with redirect_stdout(output):
            self.assertIsNone(empty())
        self.assertEqual(output.getvalue(), "-> empty()\n<- empty = None\n")

    def test_depth_resets_between_calls(self):
        @tracer
        def identity(value):
            return value

        output = io.StringIO()
        with redirect_stdout(output):
            identity(1)
            identity(2)
        self.assertEqual(output.getvalue().splitlines()[2], "-> identity(2)")

    def test_nested_decorated_functions(self):
        @tracer
        def inner(value):
            return value + 1

        @tracer
        def outer(value):
            return inner(value)

        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(outer(4), 5)
        self.assertEqual(output.getvalue().splitlines(), [
            "-> outer(4)",
            "  -> inner(4)",
            "  <- inner = 5",
            "<- outer = 5",
        ])

    def test_depth_resets_after_exception(self):
        @tracer
        def fail(n):
            if n == 0:
                raise ValueError("ошибка")
            return fail(n - 1)

        @tracer
        def value():
            return 7

        output = io.StringIO()
        with redirect_stdout(output):
            with self.assertRaises(ValueError):
                fail(2)
            value()
        self.assertEqual(output.getvalue().splitlines()[-2:], [
            "-> value()", "<- value = 7",
        ])

    def test_function_name_and_docstring_are_preserved(self):
        @tracer
        def example():
            """Пример функции."""
            return 1

        self.assertEqual(example.__name__, "example")
        self.assertEqual(example.__doc__, "Пример функции.")


if __name__ == "__main__":
    unittest.main()
