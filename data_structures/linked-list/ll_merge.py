def merge_lists(list_one, list_two):
    """Merge two lists."""

    if list_one._size > list_two._size:
        current, current_two = list_one.head._next, list_two.head

        while current_two is not None:
            list_one.insert_before(current.val, current_two.val)
            current, current_two = current._next, current_two._next
        return list_one.head.val

    else:
        current, current_two = list_one.head, list_two.head
        while current is not None:
            list_two.insert_before(current_two.val, current.val)
            current, current_two = current._next, current_two._next
        return list_two.head.val
