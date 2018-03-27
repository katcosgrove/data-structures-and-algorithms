import pytest
from linked_list import LinkedList as LL


@pytest.fixture
def empty_ll():
    """Empty linked list."""
    return LL()


@pytest.fixture
def small_ll():
    """Small linked list."""
    return LL([1, 2, 3, 4])


def test_insert_first_node(empty_ll):
    """Test insert for an empty list."""
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


def test_repr(small_ll):
    """Test repr method."""
    test_repr = small_ll.__repr__()
    assert type(test_repr) == str


def test_len(small_ll):
    """Test size."""
    test_len = small_ll.__len__()
    assert test_len == 4


def test_search(small_ll):
    """Test positive search."""
    assert small_ll.find(2) is True


def test_fail_search(small_ll):
    """Test failing search."""
    assert small_ll.find(6) is False


def test_append(small_ll):
    """Test append to end of list."""
    assert small_ll.append(5) is not str


def test_before(small_ll):
    small_ll.insert_before(3, 10) == 3


# def test_after(small_ll):
#     assert small_ll.insert_after(3, 10) == 3
