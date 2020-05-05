def selection_sort(items: list) -> None:
    """Sorts the given list by making multiple passes over it; looking for the largest value and placing it in the proper location for that pass.

    Arguments:
        items {list} -- List to sort in place
    """
    for comp_count in range(len(items) - 1, 0, -1):
        max_item_pos = 0
        for idx in range(comp_count + 1):
            if items[idx] > items[max_item_pos]:
                max_item_pos = idx

        temp = items[max_item_pos]
        items[max_item_pos] = items[comp_count]
        items[comp_count] = temp


# TODO: Move tests
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(alist)
print(alist)


alist2 = [3]
selection_sort(alist2)
print(alist2)


alist3 = []
selection_sort(alist3)
print(alist3)


alist4 = [17, 20, 26, 31, 44, 54, 55, 77, 93]
selection_sort(alist4)
print(alist4)
