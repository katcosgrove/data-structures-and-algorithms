class Node:
    """Node class for use in k-ary tree."""
    def __init__(self, val=None):
        """Initialize node with value and children."""
        self.val = val
        self.children = []

    def __repr__(self):
        """Return a little bit of formatted information about the node."""
        return '<Node Val: {}'.format(self.val)

    def __str__(self):
        """Return the value of the node."""
        return self.val


class KTree:
    """Class for a k-ary tree."""
    def __init__(self, iter=[]):
        """Initialize the tree with a root."""
        self.root = None

    def __repr__(self):
        """Return a little bit of formatted information about tree root."""
        return '<Root Val: {}>'.format(self.root.val)

    def __str__(self):
        """Return the value of the root."""
        return self.root.val

    def preorder(self, operation):
        """Pre-order traversal."""
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            for child in node.children:
                _walk(child)

        _walk(self.root)

    def postorder(self, operation):
        """Post-order traversal."""
        def _walk(node=None):
            if node is None:
                return

            for child in node.children:
                _walk(child)

            operation(node)

        _walk(self.root)

    def breadth_first(self, operation):
        """Breadth first traversal."""
        def _walk(nodes=None):
            temp = []
            for node in nodes:
                operation(node)
                for child in node.children:
                    temp.append(child)

            if len(temp):
                _walk(temp)

        if self.root:
            _walk([self.root])

    def insert(self, val, parent_val):
        """Insert new node at defined parent value."""
        node = Node(val)
        current = self.root

        if parent_val is None:
            if self.root is None:
                self.root = node
                return node
            raise ValueError('There is no parent value.')

        def _walk(current=None):
            if current.val == parent_val:
                current.children.append(node)
                return node

            for child in current.children:
                temp = _walk(child)
                if temp:
                    return temp

        node = _walk(self.root)

        if node is None:
            raise ValueError('Parent value not found')
        return node
