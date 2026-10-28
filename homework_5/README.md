# Домашнее задание 5

- `tracer/` - декоратор для вывода рекурсивных вызовов
- `permutations/` - перестановки массива с выводом стека
- `AVL/` - AVL-дерево с вставкой, удалением и поиском

Разбор, сложность и пошаговый пример лежат в README внутри каждой папки.

Команды запускаются из `homework_5`:

    echo 4 | python3 -m tracer.tracer
    echo "2 4 7" | python3 -m permutations.permutations
    python3 -m AVL.avl

Тесты у каждой задачи запускаются отдельно из той же папки:

    python3 -m unittest tracer.test_tracer
    python3 -m unittest permutations.test_permutations
    python3 -m unittest AVL.test_avl

Написаны на unittest из стандартной библиотеки. Перестановки используют декоратор из `tracer`, поэтому запуск идёт через `-m` из общей папки домашнего задания.
