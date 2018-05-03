from hash_table import HashTable


def left_join(table_one, table_two):
    """Return result of a left join on two hash tables as a dictionary."""
    joined = {}

    if type(table_one) is not HashTable or type(table_two) is not HashTable:
        raise TypeError('You must use hash tables!')

    for key in table_one:
        joined[key] = [table_one.get(key), 'NULL']

    for key in table_two:
        if key in joined:
            joined[key][1] = table_two.get(key)

    return joined
