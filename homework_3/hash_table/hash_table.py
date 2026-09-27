"""Задача 3. Своя хеш-таблица на открытой адресации.

Данные лежат в одном списке ячеек. Ячейка бывает трёх видов:
    None       - пустая, тут никогда ничего не лежало;
    _DELETED   - надгробие, элемент отсюда удалили;
    [key, val] - занятая, пара хранится обычным списком из двух элементов.
"""

from typing import Any, Iterable, Iterator, List, Tuple

# Уникальный объект-маркер. Сравнивается по ссылке, так что спутать его
# с пользовательским значением невозможно.
_DELETED = object()

_MISSING = object()


class HashTable:
    """Хеш-таблица с линейным пробированием и авторасширением."""

    MIN_CAPACITY = 8
    MAX_LOAD = 0.75    # доля занятых ячеек, после которой таблица перестраивается
    MIN_LOAD = 0.125   # доля, ниже которой таблица сжимается

    def __init__(self, items: Iterable[Tuple[Any, Any]] = (), capacity: int = MIN_CAPACITY):
        self._capacity = self._round_capacity(capacity)
        self._slots: List[Any] = [None] * self._capacity
        self._size = 0          # реальное число пар
        self._tombstones = 0    # число надгробий
        for key, value in items:
            self.put(key, value)

    # --- служебное ---------------------------------------------------------

    @classmethod
    def _round_capacity(cls, capacity: int) -> int:
        """Округлить вместимость вверх до степени двойки."""
        result = cls.MIN_CAPACITY
        while result < capacity:
            result *= 2
        return result

    def _index(self, key) -> int:
        """Номер ячейки, с которой начинается поиск ключа.

        Вместимость всегда степень двойки, поэтому взятие остатка заменяется
        побитовым И - это то же самое, но дешевле.
        """
        return hash(key) & (self._capacity - 1)

    def _probe(self, key) -> Tuple[int, int]:
        """Пройти цепочку ячеек для ключа.

        Возвращает пару (индекс ключа или -1, индекс ячейки для вставки).
        Надгробия при поиске пропускаются, но запоминается первое из них:
        именно в него выгоднее вставлять, чтобы таблица не росла зря.
        """
        index = self._index(key)
        free = -1
        while True:
            slot = self._slots[index]
            if slot is None:
                return -1, index if free == -1 else free
            if slot is _DELETED:
                if free == -1:
                    free = index
            elif slot[0] == key:
                return index, index
            index = (index + 1) & (self._capacity - 1)

    def _resize(self, capacity: int) -> None:
        """Перестроить таблицу в новой вместимости.

        Заодно исчезают все надгробия: в новый список переносятся только
        живые пары, причём заново хешированные.
        """
        old_slots = self._slots
        self._capacity = self._round_capacity(capacity)
        self._slots = [None] * self._capacity
        self._tombstones = 0
        for slot in old_slots:
            if slot is not None and slot is not _DELETED:
                _, free = self._probe(slot[0])
                self._slots[free] = slot

    # --- основные операции -------------------------------------------------

    def put(self, key, value) -> None:
        """Вставить пару или заменить значение у существующего ключа."""
        index, free = self._probe(key)
        if index != -1:
            self._slots[index][1] = value
            return

        if self._slots[free] is _DELETED:
            self._tombstones -= 1
        self._slots[free] = [key, value]
        self._size += 1

        # Считаем занятыми и надгробия: они тоже удлиняют цепочки поиска.
        if (self._size + self._tombstones) >= self._capacity * self.MAX_LOAD:
            # Если места мало из-за надгробий, а не из-за данных, растить
            # таблицу незачем - хватит перестройки в той же вместимости.
            grow = self._size >= self._capacity * self.MAX_LOAD / 2
            self._resize(self._capacity * 2 if grow else self._capacity)

    def get(self, key, default=_MISSING):
        """Значение по ключу. Без default отсутствие ключа это KeyError."""
        index, _ = self._probe(key)
        if index == -1:
            if default is _MISSING:
                raise KeyError(key)
            return default
        return self._slots[index][1]

    def remove(self, key) -> None:
        """Удалить пару по ключу."""
        index, _ = self._probe(key)
        if index == -1:
            raise KeyError(key)

        # Ячейку нельзя просто обнулить: она может стоять в середине цепочки,
        # и тогда ключи за ней перестанут находиться. Ставим надгробие.
        self._slots[index] = _DELETED
        self._size -= 1
        self._tombstones += 1

        if self._capacity > self.MIN_CAPACITY and self._size < self._capacity * self.MIN_LOAD:
            self._resize(self._capacity // 2)

    def contains(self, key) -> bool:
        index, _ = self._probe(key)
        return index != -1

    # --- удобства ----------------------------------------------------------

    def keys(self) -> Iterator:
        for slot in self._slots:
            if slot is not None and slot is not _DELETED:
                yield slot[0]

    def values(self) -> Iterator:
        for slot in self._slots:
            if slot is not None and slot is not _DELETED:
                yield slot[1]

    def items(self) -> Iterator[Tuple[Any, Any]]:
        for slot in self._slots:
            if slot is not None and slot is not _DELETED:
                yield slot[0], slot[1]

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def load_factor(self) -> float:
        return (self._size + self._tombstones) / self._capacity

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.remove(key)

    def __contains__(self, key):
        return self.contains(key)

    def __len__(self):
        return self._size

    def __iter__(self):
        return self.keys()

    def __repr__(self):
        inside = ", ".join("{!r}: {!r}".format(k, v) for k, v in self.items())
        return "HashTable({" + inside + "})"


def main() -> None:
    table = HashTable()
    for number, word in enumerate(["ноль", "один", "два", "три"]):
        table[number] = word
    print(table)
    print("table[2] =", table[2])
    del table[1]
    print("после удаления:", table, "размер", len(table), "вместимость", table.capacity)


if __name__ == "__main__":
    main()
