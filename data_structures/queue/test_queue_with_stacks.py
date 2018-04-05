import pytest


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
    """Test inserting a string raises error."""
    with pytest.raises(Exception):
        small_queue.enqueue('a')


def test_dequeue_empty(empty_queue):
    """Test dequeue of an empty list raises error."""
    with pytest.raises(ValueError):
        empty_queue.dequeue()


def test_dequeue_small(small_queue):
    """Test dequeue works."""
    small_queue.dequeue()
    assert small_queue.__len__() == 4
