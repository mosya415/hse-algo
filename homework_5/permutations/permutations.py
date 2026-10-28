"""Задача 2. Перестановки массива с выводом рекурсивных вызовов."""

from tracer.tracer import tracer


def permutations(nums, trace=True):
    def generate(remaining):
        if not remaining:
            return [[]]

        result = []
        chosen = set()
        for index, value in enumerate(remaining):
            # Одинаковое значение на этой позиции выбираем один раз.
            if value in chosen:
                continue
            chosen.add(value)
            rest = remaining[:index] + remaining[index + 1:]
            for tail in generate(rest):
                result.append([value] + tail)
        return result

    if trace:
        generate = tracer(generate)
    return generate(list(nums))


if __name__ == "__main__":
    nums = [int(value) for value in input().split()]
    print("Результат:", permutations(nums))
