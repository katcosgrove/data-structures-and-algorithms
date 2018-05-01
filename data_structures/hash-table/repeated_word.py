from hash_table import HashTable


def repeated_word(string):
    """Takes a string as an argument. Returns the first word to be repeated."""
    if type(string) is not str:
        raise TypeError('Please input a string.')

    words = string.split(' ')
    table = HashTable()

    for word in words:
        if table.get(word):
            return word
        table.set(word, word)

    raise KeyError('There are no duplicate words!')
