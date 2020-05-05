def binary_search(items: list, to_search: object) -> bool:
    if len(items) == 0:
        return False

    median_idx = len(items) // 2
    print(f"checking if {to_search} is the median: {items[median_idx]} of {items}")
    if items[median_idx] == to_search:
        return True

    if to_search < items[median_idx]:
        print(
            f"searching {to_search} in L:{items[:median_idx]} of {items}, where median is {items[median_idx]}"
        )
        return binary_search(items[:median_idx], i)
    else:
        print(
            f"searching {to_search} in R:{items[median_idx+1:]} of {items}, where median is {items[median_idx]}"
        )
        return binary_search(items[median_idx + 1 :], to_search)


def binary_search_no_slicing(
    items: list, to_search: object, begin: int, end: int
) -> bool:
    if begin > end:
        return False

    median_idx = (begin + end) // 2
    if items[median_idx] == to_search:
        return True

    if to_search < items[median_idx]:
        return binary_search_no_slicing(items, to_search, begin, median_idx - 1)
    else:
        return binary_search_no_slicing(items, to_search, median_idx + 1, end)


def binary_search_no_recursion(
    items: list, to_search: object, begin: int, end: int
) -> bool:
    while begin <= end:
        median_idx = (begin + end) // 2
        if items[median_idx] == to_search:
            return True
        if to_search < items[median_idx]:
            end = median_idx - 1
        else:
            begin = median_idx + 1
    return False


samples = [3, 8, 12, 13, 14, 15, 29, 40, 47]
to_find = 49
print(binary_search(samples, to_find))
print(binary_search_no_slicing(samples, to_find, 0, len(samples) - 1))
print(binary_search_no_recursion(samples, to_find, 0, len(samples) - 1))
