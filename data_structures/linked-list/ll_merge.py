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


# def merge_lists(ll_one, ll_two):
#     """
#     Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the single list.
#     """
#     if len(ll_one) > len(ll_two):
#         current1, current2 = ll_one.head._next, ll_two.head

#         while current2 is not None:
#             ll_one.insert_before(current1.val, current2.val)
#             current1, current2 = current1._next, current2._next

#         return ll_one.head.val

#     else:
#         current1, current2 = ll_one.head, ll_two.head
#         while current1 is not None:
#             ll_two.insert_before(current2.val, current1.val)
#             current2, current1 = current2._next, current1._next

#         return ll_two.head.val
