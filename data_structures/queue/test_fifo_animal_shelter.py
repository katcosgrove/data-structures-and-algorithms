from fifo_animal_shelter import AnimalShelter as shelter
from fifo_animal_shelter import Dog, Cat, Iguana
import pytest


@pytest.fixture
def empty_shelter():
    """Create an empty shelter queue."""
    return shelter()


@pytest.fixture
def small_shelter():
    """Create a short, alternating shelter queue."""
    return shelter([Dog(), Cat(), Dog(), Cat()])


def test_empty_shelter_enqueue(empty_shelter):
    empty_shelter.enqueue(Cat())
    assert empty_shelter.front.val == 'cat'


def test_enqueue_error(small_shelter):
    with pytest.raises(ValueError):
        small_shelter.enqueue(Iguana())


def test_enqueue_small(small_shelter):
    small_shelter.enqueue(Cat())
    assert small_shelter.back.val == 'cat'


def test_dequeue_empty(empty_shelter):
    with pytest.raises(IndexError):
        empty_shelter.dequeue()


def test_dequeue_cat(small_shelter):
    assert small_shelter.dequeue('cat') == 'cat'


def test_dequeue_dog(small_shelter):
    assert small_shelter.dequeue('dog') == 'dog'
