from stack import Stack
import pytest


def test_empty_stack_has_no_top(empty_stack):
    """Test empty stack has no top."""
    assert empty_stack.top is None


def test_empty_len(empty_stack):
    """Test __len__ for empty stack."""
    assert empty_stack.__len__() == 0


def test_small_len(small_stack):
    """Test __len__ for small stack."""
    assert small_stack.__len__() == 5


def test_insertion(empty_stack):
    """Test push a value to an empty stack."""
    assert empty_stack.top is None
    assert empty_stack.push(1).val == 1


def test_insertion_small(small_stack):
    """Test push a value to a small stack."""
    assert small_stack.push(2).val == 2


def test_empty_val_on_insert(empty_stack):
    """Test push with no value raises exception."""
    with pytest.raises(TypeError):
        empty_stack.push()


def test_pop_small_stack(small_stack):
    """Test pop from small stack."""
    assert small_stack.pop() == 5
    assert small_stack._size == 4


def test_pop_empty_stack(empty_stack):
    """Test pop on empty stack raises exception."""
    with pytest.raises(Exception):
        empty_stack.pop(2)


def test_peek_empty_stack(empty_stack):
    """Test peek on empty stack raises exception."""
    with pytest.raises(Exception):
        empty_stack.peek()


def test_peek_small_stack(small_stack):
    """Test peek on small stack."""
    assert small_stack.peek() == 5
