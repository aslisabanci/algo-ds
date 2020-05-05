def insertion_sort(items: list) -> None:
    """Sorts a given list by maintaining a sorted sublist in the lower positions of the list and each new item gets inserted back into this sublist in the correct place.

    Arguments:
        items {list} -- List to be sorted in place
    """
    if len(items) <= 1:
        return
    for idx in range(1, len(items)):
        to_reposition = items[idx]
        compare_idx = idx
        while to_reposition < items[compare_idx - 1] and compare_idx > 0:
            items[compare_idx] = items[compare_idx - 1]
            compare_idx -= 1

        items[compare_idx] = to_reposition


# TODO: Move tests
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)

alist2 = [3]
insertion_sort(alist2)
print(alist2)


alist3 = []
insertion_sort(alist3)
print(alist3)


alist4 = [17, 20, 26, 31, 44, 54, 55, 77, 93]
insertion_sort(alist4)
print(alist4)
