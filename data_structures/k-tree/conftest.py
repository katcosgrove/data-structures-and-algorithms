from k_tree import KTree
import pytest


@pytest.fixture
def small_ktree():
    """Return small k-ary tree."""
    tree = KTree()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    tree.insert(4, 1)
    tree.insert(5, 3)
    tree.insert(6, 3)
    tree.insert(7, 6)
    return tree


@pytest.fixture
def empty_ktree():
    """Return empty k-ary tree."""
    return KTree()
