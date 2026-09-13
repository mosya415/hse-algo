"""Задача 1. Проверка числа на палиндром без использования строк."""


def is_palindrome(number: int) -> bool:
    """True, если десятичная запись числа читается одинаково в обе стороны."""
    if number < 0:
        raise ValueError("ожидается неотрицательное целое число")

    # У числа с нулём на конце первая и последняя цифры разные:
    # ведущего нуля в записи не бывает. Сам ноль - исключение.
    if number % 10 == 0 and number != 0:
        return False

    # Разворачиваем правую половину числа и сравниваем с левой.
    reversed_tail = 0
    while number > reversed_tail:
        reversed_tail = reversed_tail * 10 + number % 10
        number //= 10

    # Чётное число цифр - половины должны совпасть.
    # Нечётное - в reversed_tail осталась центральная цифра, отбрасываем её.
    return number == reversed_tail or number == reversed_tail // 10


def main() -> None:
    print(is_palindrome(int(input().strip())))


if __name__ == "__main__":
    main()
