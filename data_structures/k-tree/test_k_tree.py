import pytest
from k_tree import print_level_order, find_matches


def test_tree_repr(small_ktree):
    """Test repr magic method."""
    assert repr(small_ktree) == '<Root Val: 1>'


def test_insert_empty_tree(empty_ktree):
    """Test insert into empty tree."""
    empty_ktree.insert(1, None)
    assert empty_ktree.root.val == 1


def test_insert_small_tree(small_ktree):
    """Test insert into existing tree."""
    small_ktree.insert(15, 3)
    assert small_ktree.root.children[1].children[2].val == 15


def test_insert_failure(small_ktree):
    """Test insert error fires."""
    with pytest.raises(ValueError):
        small_ktree.insert(20, 400)


def test_preorder(small_ktree):
    """Test pre-order traversal."""
    temp = []
    small_ktree.preorder(lambda x: temp.append(x.val))
    assert temp == [1, 2, 3, 5, 6, 7, 4]


def test_preorder_empty(empty_ktree):
    """Test pre-order traversal on empty tree."""
    temp = []
    empty_ktree.preorder(lambda x: temp.append(x.vall))
    assert temp == []


def test_postorder(small_ktree):
    """Test post-order traversal."""
    temp = []
    small_ktree.postorder(lambda x: temp.append(x.val))
    assert temp == [2, 5, 7, 6, 3, 4, 1]


def test_postorder_empty(empty_ktree):
    """Test post-order traversal on empty tree."""
    temp = []
    empty_ktree.postorder(lambda x: temp.append(x.vall))
    assert temp == []


def test_breadth_first(small_ktree):
    """Test breadth-first traversal."""
    temp = []
    small_ktree.breadth_first(lambda x: temp.append(x.val))
    assert temp == [1, 2, 3, 4, 5, 6, 7]


def test_breadth_first_empty(empty_ktree):
    """Test breadth-first traversal."""
    temp = []
    empty_ktree.breadth_first(lambda x: temp.append(x.val))
    assert temp == []


def test_print_level_order(small_ktree):
    """Test print level order of small ktree."""
    temp = print_level_order(small_ktree)
    assert temp == '1\n234\n56\n7\n\n'


def test_print_level_order_empty(empty_ktree):
    """Test print level order of empty ktree."""
    with pytest.raises(AttributeError):
        print_level_order(empty_ktree)


def test_find_matches_no_dupes(small_ktree):
    """Test find matches with small ktree."""
    temp = find_matches(small_ktree, 3)
    assert len(temp) == 1


def test_find_matches_with_dupes(dupe_ktree):
    """Test find matches with ktree containing duplicates."""
    temp = find_matches(dupe_ktree, 3)
    assert len(temp) == 2


def test_find_matches_error(empty_ktree):
    """Test find matches with an emtpy ktree to raise error."""
    with pytest.raises(AttributeError):
        find_matches(empty_ktree, 1)
