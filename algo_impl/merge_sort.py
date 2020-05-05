def merge_left_right(items: list, items_left: list, items_right: list) -> None:
    # TODO: documentation
    left_cursor = 0
    right_cursor = 0
    merged_cursor = 0

    while left_cursor < len(items_left) and right_cursor < len(items_right):
        if items_left[left_cursor] < items_right[right_cursor]:
            items[merged_cursor] = items_left[left_cursor]
            left_cursor += 1
        else:
            items[merged_cursor] = items_right[right_cursor]
            right_cursor += 1
        merged_cursor += 1

    while left_cursor < len(items_left):
        items[merged_cursor] = items_left[left_cursor]
        left_cursor += 1
        merged_cursor += 1

    while right_cursor < len(items_right):
        items[merged_cursor] = items_right[right_cursor]
        right_cursor += 1
        merged_cursor += 1


def merge_sort(items: list) -> None:
    # TODO: documentation
    if len(items) > 1:
        mid_idx = len(items) // 2
        items_left = items[:mid_idx]
        items_right = items[mid_idx:]

        merge_sort(items_left)
        merge_sort(items_right)

        merge_left_right(items, items_left, items_right)
    return items


# TODO: Move tests and add more
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(alist)
print(alist)
