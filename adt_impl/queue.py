class Queue:

    EMPTY_QUEUE_ERR_MSG = "Cannot do this operation on an empty queue."

    def __init__(self):
        self._items = []

    def __len__(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self) == 0

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        try:
            return self._items.pop(0)
        except IndexError:
            raise RuntimeError(Queue.EMPTY_QUEUE_ERR_MSG)

    def peek(self):
        try:
            return self._items[0]
        except IndexError:
            raise RuntimeError(Queue.EMPTY_QUEUE_ERR_MSG)


class QueueWithFakeDeleteAndCleanUp(Queue):
    def __init__(self):
        super().__init__()
        self._head = 0

    def peek(self):
        return self._items[self._head]

    def dequeue(self):
        item = self.peek()
        self._head += 1
        if self._head > len(self._items) // 2:
            self._items = self._items[self._head :]
            self._head = 0
        return item

    def __len__(self):
        return super().__len__() - self._head
