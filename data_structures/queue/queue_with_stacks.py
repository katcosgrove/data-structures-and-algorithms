from stack import Stack
from node import Node


class Queue(object):
    """Initialize a queue built from two stacks."""
    def __init__(self, iter=[]):
        self._size = 0
        self.back = Stack()
        self.front = Stack()

        for item in iter:
            self.enqueue(item)

    def enqueue(self, val):
        """Add a value to the back of the queue."""
        if type(val) is not int:
            raise TypeError('Please insert an integer.')

        self.back.push(val)
        self._size += 1
        return self

    def dequeue(self):
        """Remove a value from the front of the queue."""
       pass
