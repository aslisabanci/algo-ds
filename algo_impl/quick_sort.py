def quick_sort(items: list, begin: int, end: int) -> None:
    """Sorts a list of items, by picking a pivot item and partitioning the list around the pivot, to keep items that are less than the pivot to its left and items that are larger than the pivot to its right. Then applies the same method on the partitioned left and right sub lists.

    Arguments:
        items {list} -- List to sort in place
        begin_idx {int} -- Beginning index of the items to sort
        end_idx {int} -- End index of the items to sort
    """
    if begin < end:
        partition_idx = partition(items, begin, end)
        quick_sort(items, begin, partition_idx - 1)
        quick_sort(items, partition_idx + 1, end)


def partition(items: list, begin: int, end: int) -> int:
    """Partitions the list by placing the selected pivot item (which is initially the last element of the list) to its final place. After the pivot is placed, items that are less than it are gathered on its left and items larger than it are gathered on its right.

    Arguments:
        items {list} -- List of items to partition
        begin {int} -- Beginning index of the items to partition
        end {int} -- End index of the items to partition

    Returns:
        int -- The final place of the pivot item in the given list
    """
    pivot = items[end]
    i = begin - 1
    for j in range(begin, end):
        if items[j] <= pivot:
            i += 1
            items[i], items[j] = items[j], items[i]

    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


# TODO: Move tests and add more
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist, 0, len(alist) - 1)
print(alist)
