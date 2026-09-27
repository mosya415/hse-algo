"""Тесты к задаче 3. Запуск: python3 test_hash_table.py"""

import random
import unittest

from hash_table import HashTable


class Collider:
    """Ключ с фиксированным хешем: все такие ключи лезут в одну ячейку."""

    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return 42

    def __eq__(self, other):
        return isinstance(other, Collider) and self.name == other.name

    def __repr__(self):
        return "Collider({!r})".format(self.name)


class TestBasics(unittest.TestCase):
    def test_empty_table(self):
        table = HashTable()
        self.assertEqual(len(table), 0)
        self.assertNotIn("a", table)

    def test_put_and_get(self):
        table = HashTable()
        table.put("a", 1)
        table.put("b", 2)
        self.assertEqual(table.get("a"), 1)
        self.assertEqual(table.get("b"), 2)
        self.assertEqual(len(table), 2)

    def test_put_replaces_value(self):
        table = HashTable()
        table.put("a", 1)
        table.put("a", 2)
        self.assertEqual(table.get("a"), 2)
        self.assertEqual(len(table), 1)

    def test_missing_key(self):
        table = HashTable()
        with self.assertRaises(KeyError):
            table.get("нет")
        self.assertIsNone(table.get("нет", None))
        self.assertEqual(table.get("нет", 0), 0)

    def test_remove(self):
        table = HashTable([("a", 1), ("b", 2)])
        table.remove("a")
        self.assertNotIn("a", table)
        self.assertEqual(table.get("b"), 2)
        self.assertEqual(len(table), 1)

    def test_remove_missing_key(self):
        with self.assertRaises(KeyError):
            HashTable().remove("нет")

    def test_dict_syntax(self):
        table = HashTable()
        table["a"] = 1
        self.assertEqual(table["a"], 1)
        self.assertIn("a", table)
        del table["a"]
        self.assertNotIn("a", table)

    def test_none_as_value(self):
        # None это обычное значение, а не признак пустой ячейки.
        table = HashTable()
        table.put("a", None)
        self.assertIn("a", table)
        self.assertIsNone(table.get("a"))
        self.assertEqual(len(table), 1)

    def test_mixed_key_types(self):
        table = HashTable()
        for key in (1, "1", (1, 2), None, True, 3.5):
            table.put(key, str(key))
        # True и 1 это один и тот же ключ, как и у обычного dict.
        self.assertEqual(table.get(1), "True")
        self.assertEqual(table.get("1"), "1")
        self.assertEqual(table.get((1, 2)), "(1, 2)")
        self.assertEqual(table.get(None), "None")

    def test_unhashable_key(self):
        with self.assertRaises(TypeError):
            HashTable().put([1, 2], "значение")

    def test_iteration(self):
        table = HashTable([("a", 1), ("b", 2), ("c", 3)])
        self.assertEqual(sorted(table.keys()), ["a", "b", "c"])
        self.assertEqual(sorted(table.values()), [1, 2, 3])
        self.assertEqual(sorted(table.items()), [("a", 1), ("b", 2), ("c", 3)])
        self.assertEqual(sorted(table), ["a", "b", "c"])


class TestCollisions(unittest.TestCase):
    def test_keys_with_equal_hashes(self):
        table = HashTable()
        keys = [Collider(name) for name in "abcde"]
        for number, key in enumerate(keys):
            table.put(key, number)
        self.assertEqual(len(table), 5)
        for number, key in enumerate(keys):
            self.assertEqual(table.get(key), number)

    def test_lookup_survives_deletion_in_the_middle(self):
        # Главная ловушка открытой адресации: если на месте удалённого ключа
        # оставить пустую ячейку, цепочка оборвётся и всё, что лежит за ней,
        # перестанет находиться.
        table = HashTable()
        first, second, third = Collider("a"), Collider("b"), Collider("c")
        table.put(first, 1)
        table.put(second, 2)
        table.put(third, 3)
        table.remove(second)
        self.assertEqual(table.get(first), 1)
        self.assertEqual(table.get(third), 3)
        self.assertNotIn(second, table)

    def test_tombstone_is_reused(self):
        # После удаления вставка того же ключа должна занять надгробие,
        # а не тянуть цепочку дальше.
        table = HashTable()
        key = Collider("a")
        for _ in range(100):
            table.put(key, 1)
            table.remove(key)
        table.put(key, 1)
        self.assertEqual(len(table), 1)
        self.assertEqual(table.capacity, HashTable.MIN_CAPACITY)


class TestResize(unittest.TestCase):
    def test_table_grows(self):
        table = HashTable()
        start_capacity = table.capacity
        for number in range(100):
            table.put(number, number * 10)
        self.assertGreater(table.capacity, start_capacity)
        self.assertLessEqual(table.load_factor, HashTable.MAX_LOAD)
        for number in range(100):
            self.assertEqual(table.get(number), number * 10)

    def test_table_shrinks(self):
        table = HashTable()
        for number in range(200):
            table.put(number, number)
        big_capacity = table.capacity
        for number in range(195):
            table.remove(number)
        self.assertLess(table.capacity, big_capacity)
        self.assertEqual(len(table), 5)
        for number in range(195, 200):
            self.assertEqual(table.get(number), number)

    def test_capacity_never_below_minimum(self):
        table = HashTable([("a", 1)])
        table.remove("a")
        self.assertEqual(table.capacity, HashTable.MIN_CAPACITY)

    def test_initial_capacity(self):
        table = HashTable(capacity=100)
        self.assertEqual(table.capacity, 128)

    def test_data_survives_many_rehashes(self):
        table = HashTable()
        for number in range(5000):
            table.put(number, number)
        self.assertEqual(len(table), 5000)
        self.assertEqual(sorted(table.keys()), list(range(5000)))


class TestAgainstDict(unittest.TestCase):
    def test_random_operations(self):
        # Таблица должна вести себя как обычный dict, поэтому гоняю на них
        # одни и те же случайные операции и сравниваю состояние.
        rnd = random.Random(1)
        table = HashTable()
        reference = {}
        for _ in range(3000):
            key = rnd.randrange(50)
            if rnd.random() < 0.6:
                value = rnd.randrange(1000)
                table.put(key, value)
                reference[key] = value
            elif key in reference:
                table.remove(key)
                del reference[key]
            self.assertEqual(len(table), len(reference))
        self.assertEqual(sorted(table.items()), sorted(reference.items()))


if __name__ == "__main__":
    unittest.main()
