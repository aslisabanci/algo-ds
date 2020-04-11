from __future__ import annotations
from adt_impl.linkedlist_deque import Node
from adt_impl.deque_interface import DequeInterface


class DoubleNode(Node):
    def __init__(self, data: object, next: DoubleNode, prev: DoubleNode):
        super().__init__(data, next)
        self.prev = prev

        if self.next is not None:
            self.next.prev = self
        if self.prev is not None:
            self.prev.next = self


class DoubleLinkedListDeque(DequeInterface):
    def __init__(self):
        super().__init__()
        self._head: DoubleNode = None
        self._tail: DoubleNode = None

    def is_empty(self) -> bool:
        return self._head == None

    def add_first(self, item: object) -> None:
        new_node = DoubleNode(data=item, prev=None, next=self._head)
        self._head = new_node
        if self._tail is None:
            self._tail = self._head

    def add_last(self, item: object) -> None:
        if self.is_empty():
            self.add_first(item)
        else:
            new_node = DoubleNode(data=item, next=None, prev=self._tail)
            self._tail.next = new_node
            self._tail = new_node

    def remove_first(self) -> object:
        if self.is_empty():
            return None
        item = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        else:
            self._head.prev = None
        return item

    def remove_last(self) -> object:
        if self.is_empty():
            return None
        if self._head == self._tail:
            return self.remove_first()

        item = self._tail.data
        self._tail = self._tail.prev
        self._tail.next = None
        return item
