from node import Node


class LinkedList:
    """Class for a singly linked list."""

    def __init__(self, iter=[]):
        """Initialize the list."""
        self._current = None
        self.head = None
        self._size = 0
        try:
            for item in iter:
                self.insert(item)
        except ValueError:
            print('Value error! Please insert an iterable.')

    def __repr__(self):
        """Return the value of the head."""
        try:
            return '<head> => {}'.format(self.head.val)
        except ValueError:
            print('Oops! The head has no value.')

    def __len__(self):
        """Return the size of the list."""
        return self._size

    def insert(self, val):
        """Insert an item into the list and reassign the head."""
        self.head = Node(val, self.head)
        self._size += 1

    def find(self, val):
        """Find a value."""
        search = self.head
        while search:
            if search.get_data() == val:
                return True
            search = search.get_next()
        return False
