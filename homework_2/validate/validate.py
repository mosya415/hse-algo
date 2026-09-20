"""Задача 2. Проверка, что popped получается из pushed операциями стека."""

from typing import List, Sequence


def validate(pushed: Sequence[int], popped: Sequence[int]) -> bool:
    """True, если pushed и popped согласуются с работой одного стека."""
    if len(pushed) != len(popped):
        return False

    stack: List[int] = []
    i = 0
    for value in pushed:
        stack.append(value)
        # Пока вершина совпадает с тем, что ждёт popped, снимаем её.
        while stack and i < len(popped) and stack[-1] == popped[i]:
            stack.pop()
            i += 1

    # Если что-то осталось, порядок в popped стеком не воспроизводится.
    return not stack


def parse_numbers(line: str) -> List[int]:
    return [int(token) for token in line.split()]


def main() -> None:
    pushed = parse_numbers(input())
    popped = parse_numbers(input())
    print(validate(pushed, popped))


if __name__ == "__main__":
    main()
