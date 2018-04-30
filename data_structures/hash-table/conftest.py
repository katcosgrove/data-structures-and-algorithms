from hash_table import HashTable
import pytest


@pytest.fixture
def small_hash_table():
    """Not empty hash table."""
    return HashTable(1)


@pytest.fixture
def empty_hash_table():
    """Empty hash table."""
    return HashTable()
