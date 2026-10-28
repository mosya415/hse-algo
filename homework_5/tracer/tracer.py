"""Задача 1. Декоратор для вывода рекурсивных вызовов."""

from functools import wraps


_depth = 0


def _arguments(args, kwargs):
    parts = [repr(value) for value in args]
    parts.extend(f"{name}={value!r}" for name, value in kwargs.items())
    return ", ".join(parts)


def tracer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global _depth

        print(f"{'  ' * _depth}-> {func.__name__}({_arguments(args, kwargs)})")
        _depth += 1
        try:
            result = func(*args, **kwargs)
        finally:
            _depth -= 1
        print(f"{'  ' * _depth}<- {func.__name__} = {result!r}")
        return result

    return wrapper


@tracer
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print("Результат:", factorial(int(input())))
