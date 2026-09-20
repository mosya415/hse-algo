"""Задача 3. Слияние двух отсортированных односвязных списков."""

from typing import Iterable, List, Optional


class ListNode:
    """Узел односвязного списка."""

    __slots__ = ("val", "next")

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __repr__(self):
        return "ListNode({})".format(self.val)


def build_list(values: Iterable[int]) -> Optional[ListNode]:
    """Собрать список из последовательности значений, вернуть голову."""
    head = None
    tail = None
    for value in values:
        node = ListNode(value)
        if tail is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    """Выписать значения списка в обычный питоновский список."""
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


def merge_with_dummy(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Слияние через фиктивный узел."""
    dummy = ListNode()
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Один из списков кончился, остаток второго уже отсортирован.
    tail.next = list1 if list1 is not None else list2
    return dummy.next


def merge_without_dummy(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Слияние без фиктивного узла: голова выбирается отдельно."""
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    tail = head
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2
    return head


def main() -> None:
    list1 = build_list(int(token) for token in input().split())
    list2 = build_list(int(token) for token in input().split())
    print(to_list(merge_with_dummy(list1, list2)))


if __name__ == "__main__":
    main()
