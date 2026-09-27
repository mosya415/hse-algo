"""Задача 1. Поиск двух элементов с заданной суммой."""

from typing import List, Optional, Sequence, Tuple


def two_sum(arr: Sequence[int], k: int) -> Optional[Tuple[int, int]]:
    """Индексы двух элементов, дающих в сумме k, по возрастанию.

    По условию такая пара ровно одна. Если её нет, возвращается None.
    """
    seen = {}  # значение -> его индекс
    for index, value in enumerate(arr):
        complement = k - value
        if complement in seen:
            return seen[complement], index
        # Запоминаем первое вхождение: более ранний индекс нам и нужен.
        if value not in seen:
            seen[value] = index
    return None


def parse_numbers(line: str) -> List[int]:
    return [int(token) for token in line.split()]


def main() -> None:
    arr = parse_numbers(input())
    k = int(input())
    answer = two_sum(arr, k)
    print("{} {}".format(*answer) if answer else "пара не найдена")


if __name__ == "__main__":
    main()
