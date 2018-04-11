import pytest
from bst import BST


def test_init(small_bst):
    """Test init for small BST."""
    assert small_bst.root.val == 20


def test_init_empty(empty_bst):
    """Test init for empty BST."""
    assert empty_bst.root is None


def test_str(small_bst):
    """Test str for small BST."""
    assert small_bst.__str__() == 20


def test_str_empty(empty_bst):
    """Test str for empty BST."""
    with pytest.raises(AttributeError):
        empty_bst.__str__()


def test_repr(small_bst):
    """Test repr for a small BST."""
    assert small_bst.__repr__() == '<BST Root 20>'


def test_repr_empty(empty_bst):
    """Test str for empty BST."""
    with pytest.raises(AttributeError):
        empty_bst.__repr__()


def test_insert_empty(empty_bst):
    """Test insert of new node in empty BST."""
    empty_bst.insert(5)
    assert empty_bst.root.val == 5


def test_insert_small(small_bst):
    """Test insert of new node in existing BST."""
    small_bst.insert(50)
    assert small_bst.root.right.val == 50


def test_inorder(small_bst):
    """Test inorder traversal on small BST."""
    temp = []
    small_bst.in_order(lambda x: temp.append(x.val))
    assert temp == [5, 10, 11, 20]


def test_inorder_empty(empty_bst):
    """Test inorder traversal on empty BST."""
    temp = []
    empty_bst.in_order(lambda x: temp.append(x.val))
    assert temp == []


def test_preorder(small_bst):
    """Test preorder traversal of small BST."""
    temp = []
    small_bst.pre_order(lambda x: temp.append(x.val))
    assert temp == [20, 5, 10, 11]


def test_preorder_empty(empty_bst):
    """Test preorder traversal of empty BST."""
    temp = []
    empty_bst.post_order(lambda x: temp.append(x.val))
    assert temp == []


def test_postorder(small_bst):
    """Test postorder traversal of small BST."""
    temp = []
    small_bst.post_order(lambda x: temp.append(x.val))
    assert temp == [11, 10, 5, 20]


def test_postorder_empty(empty_bst):
    """Test postorder traversal of empty BST."""
    temp = []
    empty_bst.post_order(lambda x: temp.append(x.val))
    assert temp == []


def test_breadth_first(small_bst):
    """Test breadth first traversal with small BST."""
    temp = []
    small_bst.breadth_first_traversal(lambda x: temp.append(x.val))
    assert temp == [20, 5, 10, 11]


def test_breadth_first_lopsided(lopsided):
    """Test breadth first traversal with small BST."""
    temp = []
    lopsided.breadth_first_traversal(lambda x: temp.append(x.val))
    assert temp == [1, 3, 5, 7, 9, 11]


def test_breadth_first_empty(empty_bst):
    """Test breadth first traversal with empty BST."""
    temp = []
    with pytest.raises(IndexError):
        empty_bst.breadth_first_traversal(lambda x: temp.append(x.val))
