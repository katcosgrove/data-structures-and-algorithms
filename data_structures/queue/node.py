class Node:
    """Class for a node."""
    def __init__(self, val, next=None):
        """Initialize the node instance."""
        self.val = val
        self._next = next

    def __str__(self):
        """Return the value as a string."""
        return self.val
