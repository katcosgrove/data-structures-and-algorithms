import towers_of_hanoi as towers
import pytest


def test_tower_exception_type():
    """Test TypeError in tower function."""
    with pytest.raises(TypeError):
        towers.towers_of_hanoi('n')


def test_tower_return_three():
    """Test tower of hanoi function returns correct last move with three."""
    temp = towers.towers_of_hanoi(3)
    assert temp == ['move disk from A to C']


def test_tower_return_two():
    """Test tower of hanoi function returns correct last move with two."""
    temp = towers.towers_of_hanoi(2)
    assert temp == ['move disk from A to C']


def test_tower_with_zero():
    temp = towers.towers_of_hanoi(1)
    assert temp == ['move disk from A to C']
