# Домашнее задание 2

- `stack_vs_queue/` - стек и очередь на односвязных списках
- `validate/` - проверка последовательностей push и pop
- `merge_lists/` - слияние двух отсортированных списков

Разбор, сложность и пошаговый пример лежат в README внутри каждой папки.

    python3 stack_vs_queue/stack_queue.py
    printf '1 2 3 4 5\n1 3 5 4 2\n' | python3 validate/validate.py
    printf '1 2 4\n1 3 4\n' | python3 merge_lists/merge_lists.py

Тесты у каждой задачи свои и запускаются из её папки:

    cd stack_vs_queue && python3 test_stack_queue.py
    cd validate       && python3 test_validate.py
    cd merge_lists    && python3 test_merge_lists.py

Написаны на unittest из стандартной библиотеки.
