import pytest
from queue import Queue


def test_empty_stack_has_no_front(empty_queue):
    """Test empty stack has no top."""
    assert empty_queue.front is None


def test_empty_len(empty_queue):
    """Test __len__ for empty stack."""
    assert empty_queue.__len__() == 0


def test_small_len(small_queue):
    """Test __len__ for small stack."""
    assert small_queue.__len__() == 5


def test_str_empty(empty_queue):
    with pytest.raises(Exception):
        empty_queue.__str__()


def test_str(small_queue):
    assert small_queue.__str__() == '<front> => 1'


def test_insertion_empty(empty_queue):
    """Test push a value to an empty stack."""
    assert empty_queue.front is None
    empty_queue.enqueue(1)
    assert empty_queue.front.val == 1


def test_insertion_small(small_queue):
    """Test push a value to a small stack."""
    small_queue.enqueue(2)
    assert small_queue.back.val == 2


def test_insertion_string(small_queue):
    with pytest.raises(Exception):
        small_queue.enqueue('a')


def test_dequeue_empty(empty_queue):
    with pytest.raises(ValueError):
        empty_queue.dequeue()


def test_dequeue_small(small_queue):
    small_queue.dequeue()
    assert small_queue.__len__() == 4
