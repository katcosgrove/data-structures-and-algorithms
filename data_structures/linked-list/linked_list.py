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
        search = self.head
        while search:
            if val == search.val:
                return True
            search = search._next
        return False

    # I think these should work, but I'm trying to figure out how to write tests for them

    def append(self, val):
        """Append a node to the end of the list."""
        search = self.head
        while search._next is not None:
            search = search._next
        search._next = Node(val)

    def insert_before(self, val, new_val):
        """Insert a new node before the matching value."""
        try:
            search = self.head
            while search._next.val != val:
                search = search._next
            search = Node(new_val, search._next)
        except (ValueError, KeyError):
            print('That is not a valid value!')

    def insert_after(self, val, new_val):
        """Insert a new node after the matching value."""
        try:
            search = self.head
            while search.val != val:
                search = search._next
            search.next = Node(new_val, search._next)
        except (ValueError, KeyError):
            print('That is not a valid value!')
