import pytest
from queue import Queue


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    s.enqueue(5)
    return s
