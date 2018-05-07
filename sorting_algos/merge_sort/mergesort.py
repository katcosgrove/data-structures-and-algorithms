def merge(list_a, list_b):
    """Merges two lists in order."""
    temp = []

    while len(list_a) is not 0 and len(list_b) is not 0:
        if list_a[0] < list_b[0]:
            temp.append(list_a[0])
            list_a.remove(list_a[0])
        else:
            temp.append(list_b[0])
            list_b.remove(list_b[0])

    if len(list_a) == 0:
        temp += list_b
    if len(list_b) == 0:
        temp += list_a

    return temp


def merge_sort(list):
    """Split a list recursively for a merge sort."""
    if len(list) < 2:
        return list

    split = len(list) // 2
    left = merge_sort(list[:split])
    right = merge_sort(list[split:])
    return merge(left, right)
