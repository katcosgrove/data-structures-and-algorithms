def selection(list):
    """Selection sort for an unordered list."""
    if len(list) < 2:
        return list

    for i in range(len(list)):
        current = i

        for n in range(i + 1, len(list)):
            if list[current] > list[n]:
                current = n

        list[i], list[current] = list[current], list[i]

    return list
