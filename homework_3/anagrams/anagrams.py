"""Задача 2. Группировка анаграмм."""

from typing import Dict, Iterable, List


def group_anagrams(words: Iterable[str]) -> List[List[str]]:
    """Разбить слова на группы, в каждой из которых слова - анаграммы.

    Группы идут в порядке первого появления, слова внутри группы - в порядке
    из исходного списка.
    """
    groups: Dict[str, List[str]] = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


def main() -> None:
    print(group_anagrams(input().split()))


if __name__ == "__main__":
    main()
