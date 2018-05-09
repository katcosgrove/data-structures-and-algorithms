from quicksort import quicksort


def test_quicksort():
    """Test quicksort algorithm with odd-numbered list."""
    list = [13, 28, 5]
    assert quicksort(list, 0, len(list) - 1) == [5, 13, 28]


def test_quicksort_even():
    """Test quicksort algorithm with even-numbered list."""
    list = [13, 28, 5, 40]
    assert quicksort(list, 0, len(list) - 1) == [5, 13, 28, 40]


def test_quicksort_small():
    """Test quicksort with two-element list."""
    list = [3, 2]
    assert quicksort(list, 0, len(list) - 1) == [2, 3]
