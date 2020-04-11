from __future__ import annotations
from adt_impl.deque_interface import DequeInterface


class Node:
    def __init__(self, data: object, next: Node):
        self.data = data
        self.next = next


class LinkedListDeque(DequeInterface):
    def __init__(self):
        super().__init__()
        self._head: Node = None

    def is_empty(self) -> bool:
        return self._head == None

    def add_front(self, item: object) -> None:
        self._head = Node(item, self._head)

    def add_rear(self, item: object) -> None:
        if self.is_empty():
            self.add_front(item)
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = Node(item, None)

    def remove_front(self) -> object:
        if self.is_empty():
            return None
        item = self._head.data
        self._head = self._head.next
        return item

    def remove_rear(self) -> object:
        if self.is_empty():
            return None
        if self._head.next is None:
            return self.remove_front()

        current = self._head
        while current.next.next is not None:
            current = current.next
        item = current.next.data
        current.next = None
        return item


class TailedLinkListDeque(LinkedListDeque):
    def __init__(self):
        super().__init__()
        self._tail = None

    def add_front(self, item: object) -> None:
        super().add_front(item)
        if self._tail is None:
            self._tail = self._head

    def add_rear(self, item: object) -> None:
        if self.is_empty():
            self.add_front(item)
        else:
            new_node = Node(item, None)
            self._tail.next = new_node
            self._tail = new_node

    def remove_front(self) -> object:
        item = super().remove_front()
        if self._head is None:
            self._tail = None
        return item

    def remove_rear(self) -> object:
        if self.is_empty():
            return None
        if self._head == self._tail:
            return self.remove_front()

        current = self._head
        while current.next is not self._tail:
            current = current.next
        item = self._tail.data
        self._tail = current
        self._tail.next = None
        return item
