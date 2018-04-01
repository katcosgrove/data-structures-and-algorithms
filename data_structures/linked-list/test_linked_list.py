import pytest
from linked_list import LinkedList as LL


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


def test_append_to_end(small_ll):
    """Test append to end of list."""
    small_ll.append(5)
    assert small_ll.head._next._next._next._next.val == 5


def test_append_to_empty(empty_ll):
    """Test appending to an empty list."""
    empty_ll.append(1)
    assert empty_ll.head.val == 1


def test_append_exception(empty_ll):
    """Test exception for string argument."""
    with pytest.raises(Exception):
        empty_ll.append('a')


def test_insert_after(small_ll):
    """Test insert after matched value."""
    small_ll.insert_after(2, 5)
    assert small_ll.head._next._next._next.val == 5


def test_insert_after_empty(small_ll):
    """Test insert after at position 0."""
    small_ll.insert_after(0, 2)
    assert small_ll.head._next.val == 3


def test_insert_after_error(small_ll):
    """Test insert after raises exception."""
    with pytest.raises(Exception):
        small_ll.insert_after('1', 2)


def test_insert_before(small_ll):
    """Test if inserts before matched value."""
    small_ll.insert_before(3, 6)
    assert small_ll.head._next.val == 6


def test_insert_before_empty(small_ll):
    """Test insert before at position 0."""
    small_ll.insert_before(0, 2)
    assert small_ll.head._next.val == 3


def test_insert_before_error(small_ll):
    """Test exception in insert before."""
    with pytest.raises(Exception):
        small_ll.insert_before('1', 2)


def test_kth_from_end(small_ll):
    """Test normal insertion of value k positions from end of list."""
    assert small_ll.kth_from_end(1) == 2


def test_kth_from_end_last(small_ll):
    """Trying to test excpetion for argument of 0."""
    assert small_ll.kth_from_end(0) == 1


def test_kth_from_end_string(small_ll):
    """Trying to test exception for string argument."""
    with pytest.raises(Exception):
        small_ll.kth_from_end('a')


@pytest.fixture
def small_ll():
    """Small linked list."""
    return LL([1, 2, 3, 4])


def test_has_loop():
    """Test small linked list without loop."""
    temp = small_ll.has_loop()
    assert temp is False


def test_has_loop_true():
    """Test small linked list with immediate loop."""
    small_ll.head._next._next = small_ll.head
    assert small_ll.has_loop() is True
