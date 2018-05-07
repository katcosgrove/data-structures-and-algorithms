from mergesort import merge_sort


def test_merge_sort():
    """Test merge sort with small, even-numbered list."""
    temp = merge_sort([5, 6, 1, 3])
    assert temp == [1, 3, 5, 6]


def test_odd_merge_sort():
    """Test merge sort with small, odd-numbered list."""
    temp = merge_sort([1, 15, 7, 12, 3])
    assert temp == [1, 3, 7, 12, 15]


def test_already_sorted():
    """Test merge sort with too-small list."""
    temp = merge_sort([1])
    assert temp == [1]


def test_merge_sort_words():
    """Test merge sort with non-integer values."""
    temp = merge_sort(['box', 'cat', 'act'])
    assert temp == ['act', 'box', 'cat']
