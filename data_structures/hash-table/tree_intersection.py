from bst import BST
from hash_table import HashTable


def tree_intersection(tree_one, tree_two):
    """Checks for duplicate values between two trees and returns those values as a set."""
    first_values = []
    second_values = []
    table = HashTable()
    dupes = set([])

    tree_one.pre_order(first_values.append)
    tree_two.pre_order(second_values.append)

    for value in first_values:
        table.set(value, value)

    for value in second_values:
        if table.get(value):
            dupes.add(value)

    if len(dupes) == 0:
        return 'There are no duplicates.'

    return dupes
