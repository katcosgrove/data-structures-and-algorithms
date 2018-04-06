import towers_of_hanoi as towers
import pytest


def test_tower_exception_type():
    """Test TypeError in tower function."""
    with pytest.raises(TypeError):
        towers.towers_of_hanoi('n')


# def test_tower_integer():
#     """Test tower function returns integer."""
#     assert towers.towers_of_hanoi(3) == 


# def test_move_tower_ideal():
#     """Test move tower function with three discs."""
#     towers.move_tower(3, 'A', 'B', 'C')


# def test_move_tower_short():
#     """Test move tower function with two discs."""
#     towers.move_tower(2, 'A', 'B', 'C') == [1, 2]
