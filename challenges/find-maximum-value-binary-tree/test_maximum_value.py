from maximum_value import find_maximum_value
import pytest


def test_maximum_value(small_bst):
    """Test find maximum value with small BST."""
    assert find_maximum_value(small_bst) == 20


def test_maximum_value_error(empty_bst):
    """Test find maximum value with empty BST raises error."""
    with pytest.raises(ValueError):
        find_maximum_value(empty_bst)


def test_maximum_value_lopsided(lopsided):
    """Test find maximum value with lopsided BST."""
    assert find_maximum_value(lopsided) == 11
