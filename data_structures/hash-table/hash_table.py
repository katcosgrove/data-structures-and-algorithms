from linked_list import LinkedList
from functools import reduce


class HashTable:
    """Class for building a hash table."""
    def __init__(self, max_size=1024):
        self.max_size = max_size
        self.buckets = [LinkedList() for _ in range(max_size)]

    def hash_key(self, key):
        """Get a hashed key for adding to the table."""
        if type(key) is not str:
            raise TypeError

        return sum(map(lambda x: ord(x), key)) % self.max_size

    def set(self, key, val):
        """Insert a key/value pair into the hash table."""
        return self.buckets[self.hash_key(key)].insert({key: val})

    def get(self, key):
        """Return value at given key."""
        current = self.buckets[self.hash_key(key)].head

        while current:
            if key in current.val.keys():
                return current.val[key]
            current = current._next

    def remove(self, key):
        """Remove value at given key."""
        bucket = self.buckets[self.hash_key(key)]
        current = bucket.head
        last = current
        while current:
            if key in current.val.keys():
                if last is not current:
                    last._next = current._next
                else:
                    bucket.head = current._next
            try:
                return current.val[key]
            except KeyError:
                raise KeyError('That value is not in the table!')

            last = current
            current = current._next
