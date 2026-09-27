# Домашнее задание 3

- `two_sum/` - поиск двух элементов с заданной суммой
- `anagrams/` - группировка слов по анаграммам
- `hash_table/` - своя хеш-таблица

Разбор, сложность и пошаговый пример лежат в README внутри каждой папки.

    printf '1 3 4 10\n7\n' | python3 two_sum/two_sum.py
    echo "eat tea tan ate nat bat" | python3 anagrams/anagrams.py
    python3 hash_table/hash_table.py

Тесты у каждой задачи свои и запускаются из её папки:

    cd two_sum    && python3 test_two_sum.py
    cd anagrams   && python3 test_anagrams.py
    cd hash_table && python3 test_hash_table.py

Написаны на unittest из стандартной библиотеки.
