from typing import Optional


def find_kth_smallest_log(items: list, k: int) -> Optional[object]:
    if len(items) < k:
        return None
    sorted_items = sorted(items)
    return sorted_items[k - 1]


def _partition(items: list, begin: int, end: int) -> int:
    pivot = items[end]
    i = begin - 1
    for j in range(begin, end):
        if items[j] <= pivot:
            i += 1
            items[i], items[j] = items[j], items[i]

    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


def find_kth_smallest_linear(items: list, k: int) -> Optional[object]:
    left = 0
    right = len(items) - 1
    while left <= right:
        pivotIndex = _partition(items, left, right)
        if pivotIndex == k - 1:
            return items[pivotIndex]
        # meaning the kth smallest is to the left of the pivot -> narrow down the search by adjusting right
        elif pivotIndex > k - 1:
            right = pivotIndex - 1
        # meaning the kth smallest is to the right of the pivot -> narrow down the search by adjusting left
        else:
            left = pivotIndex + 1
    return None


print(find_kth_smallest_log([3, 2, 1, 5, 4], 3))
print(find_kth_smallest_linear([3, 2, 1, 5, 4], 3))
