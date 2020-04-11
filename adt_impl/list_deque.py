from adt_impl.deque_interface import DequeInterface


class ListDeque(DequeInterface):
    def __init__(self):
        super().__init__()
        self._items = []

    def __len__(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self) == 0

    def add_first(self, item: object) -> None:
        self._items.insert(0, item)

    def add_last(self, item: object) -> None:
        self._items.append(item)

    def remove_first(self) -> object:
        return self._items.pop(0)

    def remove_last(self) -> object:
        return self._items.pop()


ld = ListDeque()
print(ld._items)
print(isinstance(ld, ListDeque))
