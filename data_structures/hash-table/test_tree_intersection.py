from tree_intersection import tree_intersection


def test_tree_intersection_equal(small_bst, small_bst_two):
    """Test tree intersection with two small BSTs."""
    result = tree_intersection(small_bst, small_bst_two)
    assert result == {'20', '5'}


def test_tree_intersection_uneven(small_bst, lopsided):
    """Test tree intersection with one uneven tree."""
    result = tree_intersection(small_bst, lopsided)
    assert result == {'11', '5'}


def test_tree_intersection_empty(small_bst, empty_bst):
    """Test tree intersection with one empty tree."""
    result = tree_intersection(small_bst, empty_bst)
    assert result == 'There are no duplicates.'
