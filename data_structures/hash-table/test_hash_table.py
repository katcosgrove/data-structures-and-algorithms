import pytest


def test_hash_key(empty_hash_table):
    """Test hash with simple word."""
    assert empty_hash_table.hash_key('test') == 448


def test_large_hash_key(empty_hash_table):
    """Test larger hash."""
    assert empty_hash_table.hash_key('xylophone') == 998


def test_hash_key_error(empty_hash_table):
    """Test hash key throws error."""
    with pytest.raises(TypeError):
        empty_hash_table.hash_key(40)


def test_set_empty(empty_hash_table):
    """Test set in empty hash table."""
    empty_hash_table.set('test', 't')
    assert empty_hash_table.buckets[448].head.val['test'] == 't'


def test_set_small(small_hash_table):
    """Test set in empty hash table."""
    small_hash_table.set('test', 't')
    assert small_hash_table.buckets[0].head.val['test'] == 't'


def test_get(empty_hash_table):
    """Test get in empty table."""
    empty_hash_table.set('test', 't')
    assert empty_hash_table.get('test') == 't'


def test_get_from_bucket(small_hash_table):
    """Test gets from bucket with multiple values."""
    small_hash_table.set('cat', 'c')
    small_hash_table.set('act', 'a')
    assert small_hash_table.get('cat') == 'c'
    assert small_hash_table.get('act') == 'a'


def test_remove(small_hash_table):
    """Test normal remove."""
    small_hash_table.set('test', 't')
    small_hash_table.remove('test')
    assert small_hash_table.get('test') is None


def test_remove_empty(empty_hash_table):
    """Test remove when value is not in table."""
    with pytest.raises(KeyError):
        empty_hash_table.set('act', 'a')
        empty_hash_table.remove('cat')
        assert empty_hash_table.get('act') == 'a'
