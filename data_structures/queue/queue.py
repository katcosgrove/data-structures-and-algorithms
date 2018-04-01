from node import Node


class Queue:
    """Create queue object."""
    def __init__(self, iter=[]):
        self.front = None
        self.back = None
        self._size = 0
        try:
            for item in iter:
                self.enqueue(item)
        except ValueError:
            print('Value error! Please insert an iterable.')

    def __len__(self):
        """Return the size of the queue."""
        return self._size

    def __str__(self):
        """Return the value of the front."""
        try:
            return '<front> => {}'.format(self.front.val)
        except ValueError:
            print('Oops! The front has no value.')

    def enqueue(self, val):
        """Add a new node to back of queue."""
        node = Node(val, None)

        if self.back is None:
            self.front = node
            self.back = node
            self._size += 1
        else:
            self.back._next = node
            self.back = self.back._next
            self._size += 1

    def dequeue(self):
        """Remove an item from the queue."""
        if self.front is not None:
            first = self.front
            self.front = self.front._next
            self._size -= 1
            return first.val
        else:
            if self.back is not None:
                self.back = None
            raise ValueError('Queue is empty.')
