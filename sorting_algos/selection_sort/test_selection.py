from selection import selection


def test_selection_sort():
    """Test selection sort with small, even-numbered list."""
    temp = selection([1, 5, 2, 18])
    assert temp == [1, 2, 5, 18]


def test_selection_sort_odd():
    """Test selection sort with small, odd-nubered list."""
    temp = selection([1, 5, 2, 18, 4])
    assert temp == [1, 2, 4, 5, 18]


def test_selection_sort_ordered():
    """Test selection sort with tiny list."""
    temp = selection([1])
    assert temp == [1]


def test_selection_sort_words():
    """Test selection sort with words."""
    temp = selection(['box', 'act', 'cat'])
    assert temp == ['act', 'box', 'cat']
