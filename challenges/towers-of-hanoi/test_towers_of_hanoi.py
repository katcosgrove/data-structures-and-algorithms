import towers_of_hanoi as towers
import pytest


def test_tower_exception_type():
    """Test TypeError in tower function."""
    with pytest.raises(TypeError):
        towers.towers_of_hanoi('n')


def test_tower_return_three():
    """Test tower of hanoi function returns correct last move with three."""
    assert towers.towers_of_hanoi(3) == 'move disk from A to C'


def test_tower_return_two():
    """Test tower of hanoi function returns correct last move with two."""
    assert towers.towers_of_hanoi(2) == 'move disk from A to C'


def test_tower_with_zero():
    assert towers.towers_of_hanoi(1) == 'move disk from A to C'
