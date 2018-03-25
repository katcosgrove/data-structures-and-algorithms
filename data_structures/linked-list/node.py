
class Node:
    """Class for a node."""
    def __init__(self, val, next=None):
        """Initialize the node instance."""
        self.val = val
        self._next = next

    def __str__(self):
        """Return the value as a string."""
        return '{val}'.format(val=self.val)

    def get_data(self):
        """Return value of current node."""
        return self.val

    def get_next(self):
        """Get the next node in the list."""
        return self._next
