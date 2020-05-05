from typing import Optional


def first_idx_of_one(items: list) -> Optional[int]:
    """Finds the first index of 1 in a sorted list of 0s and 1s.

    Arguments:
        items {[type]} -- Sorted list of 0s and 1s.

    Returns:
        [type] -- The index of the first 1 if it exists, None otherwise.
    """
    begin = 0
    end = len(items) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if items[mid] == 0:
            begin = mid + 1
        else:
            end = mid - 1
        if begin <= len(items) - 1 and items[begin] == 1:
            return begin
    return None


# TODO: Move tests and add more
items = [0, 0, 0, 1, 1]
print(first_idx_of_one(items))
