from bst import BST
import pytest


@pytest.fixture
def small_bst():
    return BST([20, 5, 10, 11])


@pytest.fixture
def lopsided():
    return BST([1, 3, 5, 7, 9, 11])


@pytest.fixture
def empty_bst():
    return BST()
