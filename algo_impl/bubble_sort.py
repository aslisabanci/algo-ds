def bubble_sort(items: list) -> None:
    """Sorts the given list by making multiple passes over it; exchanging adjacent items if they are out-of-place. 

    Arguments:
    items {list} -- List to sort in place
    """
    for comp_count in range(len(items) - 1, 0, -1):
        for idx in range(comp_count):
            if items[idx] > items[idx + 1]:
                temp = items[idx]
                items[idx] = items[idx + 1]
                items[idx + 1] = temp


def bubble_sort_early_stop(items: list) -> None:
    """Bubble-sorts a list, with the ability of early stopping if no pairs is out-of-place.

    Arguments:
    items {list} -- List to sort in place
    """
    exchanged = True
    for comp_count in range(len(items) - 1, 0, -1):
        print(f"{comp_count}")
        if exchanged == False:
            print(f"no exchanges anymore, stopping here:{comp_count}")
            break
        for idx in range(comp_count):
            exchanged = False
            if items[idx] > items[idx + 1]:
                exchanged = True
                temp = items[idx]
                items[idx] = items[idx + 1]
                items[idx + 1] = temp


# TODO: Move tests
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(alist)
print(alist)

alist2 = [3]
bubble_sort(alist2)
print(alist2)


alist3 = []
bubble_sort(alist3)
print(alist3)


alist4 = [17, 20, 26, 31, 44, 54, 55, 77, 93]
bubble_sort(alist4)
print(alist4)


alist5 = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
bubble_sort_early_stop(alist5)
print(alist5)

alist6 = [54, 26, 20, 93, 17, 31, 44, 55, 77]
bubble_sort_early_stop(alist6)
print(alist6)
