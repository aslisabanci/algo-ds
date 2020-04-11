class Stack:

    EMPTY_STACK_ERR_MSG = "Cannot do this operation on an empty stack."

    def __init__(self):
        self._items = []

    def __len__(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self) == 0

    def push(self, item) -> None:
        self._items.append(item)

    def pop(self) -> object:
        try:
            return self._items.pop()
        except IndexError:
            raise RuntimeError(Stack.EMPTY_STACK_ERR_MSG)

    def peek(self) -> object:
        try:
            return self._items[-1]
        except IndexError:
            raise RuntimeError(Stack.EMPTY_STACK_ERR_MSG)
