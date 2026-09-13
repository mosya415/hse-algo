"""Задача 2. Максимальная сумма элементов массива, делящаяся на 2."""

from typing import Iterable, List


def max_even_sum(numbers: Iterable[int]) -> int:
    """Наибольшая сумма подмножества numbers, которая делится на 2."""
    total = 0
    min_odd = None
    for value in numbers:
        total += value
        if value % 2 == 1 and (min_odd is None or value < min_odd):
            min_odd = value

    # Сумма всех элементов максимальна, если она чётная - больше ничего не нужно.
    if total % 2 == 0:
        return total

    # Иначе чётность исправляется только выбрасыванием нечётного элемента,
    # и терять выгоднее самый маленький. Раз сумма нечётная, такой элемент есть.
    return total - min_odd


def parse_numbers(line: str) -> List[int]:
    """Разбор строки вида "5 7 13 2 14"."""
    return [int(token) for token in line.split()]


def main() -> None:
    print(max_even_sum(parse_numbers(input())))


if __name__ == "__main__":
    main()
