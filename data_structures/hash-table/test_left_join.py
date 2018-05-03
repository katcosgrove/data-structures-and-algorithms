from left_join import left_join
import pytest


def test_left_join_error():
    """Test left join throws error without hash table argument."""
    with pytest.raises(TypeError):
        left_join('test', 42)


def test_left_join_perfect(even_table_one, even_table_two):
    """Test left join with perfect matches."""
    result = left_join(even_table_one, even_table_two)
    assert result == {'diligent': ['employed', 'idle'], 'fond': ['enamored', 'averse'], 'wrath': ['anger', 'delight']}


def test_left_join_null(even_table_two, uneven_table):
    """Test left join with null values."""
    result = left_join(even_table_two, uneven_table)
    assert result == {'diligent': ['idle', 'NULL'], 'fond': ['averse', 'averse'], 'wrath': ['delight', 'delight']}
