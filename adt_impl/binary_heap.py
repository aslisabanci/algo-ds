class BinaryHeap:
    def __init__(self):
        self.items = [0]
        self.size = 0

    def _move_up_item_at(self, i):
        while i // 2 > 0:
            if self.items[i // 2] > self.items[i]:
                temp = self.items[i // 2]
                self.items[i // 2] = self.items[i]
                self.items[i] = temp
            i //= 2

    def _move_down_item_at(self, i):
        while i * 2 < len(self.items):
            min_child_idx = self._min_child_for(i)
            print(f"min child for {self.items[i]} is {self.items[min_child_idx]}")
            if self.items[min_child_idx] < self.items[i]:
                temp = self.items[min_child_idx]
                self.items[min_child_idx] = self.items[i]
                self.items[i] = temp
                i = min_child_idx
            else:
                break

    def _min_child_for(self, i):
        if i * 2 + 1 >= len(self.items):
            return i * 2
        return i * 2 if self.items[i * 2] < self.items[i * 2 + 1] else i * 2 + 1

    def push(self, item: object):
        self.items.append(item)
        self._move_up_item_at(len(self.items) - 1)

    def pop(self) -> object:
        if len(self.items) == 1:
            return None
        popped = self.items[1]
        self.items[1] = self.items[-1]
        self._move_down_item_at(1)
        self.items.pop()
        return popped

    def build(self, items):
        self.items = [0] + items[:]
        for i in range(1, len(self.items)):
            print(f"item at i:{i} is {self.items[i]}, whole list is :{self.items}")
            self._move_down_item_at(i)
