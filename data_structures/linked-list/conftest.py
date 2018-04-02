from linked_list import LinkedList as LL
import pytest


@pytest.fixture
def empty_ll():
    """Empty linked list."""
    return LL()


@pytest.fixture
def small_ll():
    """Small linked list."""
    return LL([1, 2, 3, 4])


@pytest.fixture
def second_small_ll():
    """Small linked list."""
    return LL([1, 2, 3, 4])


@pytest.fixture
def large_ll():
    """Long linked list."""
    return LL([1, 2, 3, 4, 5, 6, 7, 8])
