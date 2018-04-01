import pytest
from stack import Stack


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def small_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    return s


@pytest.fixture
def large_stack():
    s = Stack()

    for num in range(1000):
        s.push(num)

    return s
