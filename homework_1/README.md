# Домашнее задание 1

- `palindrome/` - задача 1, проверка числа на палиндром без строк
- `sum/` - задача 2, максимальная сумма элементов, делящаяся на 2
- `prime/` - задача 3, количество простых чисел меньше N

Разбор алгоритма, сложность и пошаговый пример лежат в README внутри каждой папки. Решения читают вход со stdin:

    echo 121           | python3 palindrome/palindrome.py
    echo "5 7 13 2 14" | python3 sum/max_even_sum.py
    echo 10            | python3 prime/prime.py

Тесты у каждой задачи свои и запускаются из её папки:

    cd palindrome && python3 test_palindrome.py
    cd sum        && python3 test_max_even_sum.py
    cd prime      && python3 test_prime.py

Написаны на unittest из стандартной библиотеки.
