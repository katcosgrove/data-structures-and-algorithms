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
        """Check whether or not a value is in the list."""
        search = self.head
        while search:
            if val == search.val:
                return True
            search = search._next
        return False

    def append(self, val):
        """Append a node to the end of the list."""
        if type(val) is not int:
            raise Exception('Please enter an integer.')
        try:
            if self.head is None:
                self.insert(val)
            else:
                search = self.head
                while search:
                    if search._next is None:
                        search._next = Node(val)
                        self._size += 1
                        break
                    search = search._next
        except (ValueError, KeyError):
            raise Exception('That is not a valid value!')

    def insert_before(self, val, newVal):
        """Insert a new node before the matching value."""
        search = self.head
        previous = None
        if type(val) is not int:
            raise Exception('Please enter an integer.')
        try:
            while search:
                if search.val == val:
                    if previous is None:
                        self.insert(newVal)
                    else:
                        new_node = Node(newVal)
                        new_node._next = search
                        previous._next = new_node
                        self._size += 1
                previous = search
                search = search._next
        except (KeyError, ValueError):
            raise Exception('Value not found!')

    def insert_after(self, val, newVal):
        """Insert a new node after the matching value."""
        search = self.head
        if type(val) is not int:
            raise Exception('Please enter an integer.')
        try:
            while search:
                if search.val == val:
                    reference = search._next
                    search._next = Node(newVal)
                    search._next._next = reference
                    self._size += 1
                search = search._next
        except (KeyError, ValueError):
            raise Exception('Value not found!')

    def kth_from_end(self, k):
        """Return value of node at k positions from end."""
        main = self.head
        reference = self.head
        counter = 0
        try:
            if type(k) is not int:
                raise Exception('Invalid value! Please enter an integer')
            if k == 0:
                raise Exception('Invalid value! Please enter a number greater than 0.')
            if(self.head is not None):
                while(counter < k):
                    if(reference is None):
                        return
                    reference = reference._next
                    counter += 1
            while(reference is not None):
                main = main._next
                reference = reference._next
            return main.val
        except (KeyError, ValueError):
            raise Exception('That is not a valid value!')

    def has_loop(self):
        """Detect whether or not a loop exists in a linked list."""
        pointer_one, pointer_two = self.head, self.head
        while pointer_one and pointer_two and pointer_two._next:
            pointer_one = pointer_one._next
            pointer_two = pointer_two._next._next
            if pointer_one is pointer_two:
                return True
        return False
