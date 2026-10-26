# Домашнее задание 4

- `tree_traversal/` - дерево поиска и шесть обходов
- `validate_bst/` - проверка дерева на свойства BST
- `balanced_binary_tree/` - проверка баланса высот дерева

Разбор, сложность и пошаговый пример лежат в README внутри каждой папки.

    echo "8 3 10 1 6 14 4 7 13" | python3 tree_traversal/tree_traversal.py
    python3 validate_bst/validate_bst.py
    python3 balanced_binary_tree/balanced_binary_tree.py

Тесты у каждой задачи свои и запускаются из её папки:

    cd tree_traversal       && python3 test_tree_traversal.py
    cd validate_bst         && python3 test_validate_bst.py
    cd balanced_binary_tree && python3 test_balanced_binary_tree.py

Написаны на unittest из стандартной библиотеки.
