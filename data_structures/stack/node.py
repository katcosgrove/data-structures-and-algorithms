class Node:
    """Define a node class."""
    def __init__(self, val, next=None):
        self.val = val
        self._next = next

    def __repr__(self):
        return self.val
