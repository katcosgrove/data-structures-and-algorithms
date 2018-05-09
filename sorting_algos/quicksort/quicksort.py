def quicksort(list, start, end):
    """Function for quicksort algorithm."""

    if start < end:
        pivot = partition(list, start, end)

        quicksort(list, start, pivot - 1)
        quicksort(list, pivot + 1, end)

    return list


def partition(list, start, end):
    """Partition helper function for quicksort."""
    sorted = False
    pivot = list[start]
    left = start + 1
    right = end

    while not sorted:
        while left <= right and list[left] <= pivot:
            left = left + 1

        while list[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            sorted = True
        else:
            temp = list[left]
            list[left] = list[right]
            list[right] = temp

    temp = list[start]
    list[start] = list[right]
    list[right] = temp

    return right
