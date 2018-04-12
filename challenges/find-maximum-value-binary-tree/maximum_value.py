def find_maximum_value(tree):
    """Find largest value in binary tree."""
    temp = []
    largest = 0

    if tree.root is None:
        raise ValueError('The tree is empty!')

    tree.in_order(lambda x: temp.append(x.val))
    print(temp)

    for item in temp:
        if item > largest:
            largest = item
    return largest
