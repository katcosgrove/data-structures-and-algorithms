from hash_table import HashTable
from bst import BST
import pytest


@pytest.fixture
def small_hash_table():
    """Not empty hash table."""
    return HashTable(1)


@pytest.fixture
def empty_hash_table():
    """Empty hash table."""
    return HashTable()


@pytest.fixture
def even_table_one():
    """Synonyms hash table."""
    table = HashTable()
    table.set('fond', 'enamored')
    table.set('wrath', 'anger')
    table.set('diligent', 'employed')
    return table


@pytest.fixture
def even_table_two():
    """Antonyms hash table."""
    table = HashTable()
    table.set('fond', 'averse')
    table.set('wrath', 'delight')
    table.set('diligent', 'idle')
    return table


@pytest.fixture
def uneven_table():
    """Antonym table without all matches."""
    table = HashTable()
    table.set('fond', 'averse')
    table.set('wrath', 'delight')
    table.set('flow', 'jam')
    return table


@pytest.fixture
def small_bst():
    return BST(['20', '5', '10', '11'])


@pytest.fixture
def small_bst_two():
    return BST(['20', '5', '7', '12'])


@pytest.fixture
def lopsided():
    return BST(['1', '3', '5', '7', '9', '11'])


@pytest.fixture
def empty_bst():
    return BST()
