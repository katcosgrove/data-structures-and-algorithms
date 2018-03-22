
def BinarySearch(arr, val):
    """
    Arguments: A list and value to search for
    Output: The index of the matched value, or -1 if no match
    """
    if len(arr) == 0:
        return -1

    counter = 0
    for item in arr:
        counter += 1
        if item == val:
            return counter - 1
    return -1
