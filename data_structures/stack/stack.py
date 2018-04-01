from node import Node


class Stack:
    """Define stack object."""
    def __init__(self, iter=[]):
        self.top = None
        self._size = 0
        # self.items = []
        try:
            for item in iter:
                self.push(item)
        except TypeError:
            print('Value error! Please insert an iterable.')

    def __len__(self):
        """Return the size of the stack."""
        return self._size

    def __repr__(self):
        """Return the value of the top."""
        try:
            return '<top> => {}'.format(self.top.val)
        except ValueError:
            print('Oops! The top has no value.')

    def push(self, val):
        """Push a value to the stack."""
        self.top = Node(val, self.top)
        self._size += 1
        return self.top

    def pop(self):
        """Return the top value and removes it from the stack."""
        if self._size > 0:
            temp = self.top.val
            self.top = self.top._next
            self._size -= 1
            return temp
        else:
            raise ValueError('There is nothing in the stack!')

    def peek(self):
        """Look at the top of the stack."""
        if self._size > 0:
            return self.top.val
        else:
            raise ValueError('There is nothing in the stack!')
