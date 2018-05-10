from radix_sort import radix


def test_radix_sort():
    """Test radix sort using integers with same number of digits."""
    list = [22, 15, 89, 12, 11, 55]
    radix(list)
    assert list == [11, 12, 15, 22, 55, 89]


def test_radix_sort_uneven():
    """Test radix sort using integers with varying numbers of digits."""
    list = [1, 63, 13, 9104, 8, 542, 23]
    radix(list)
    assert list == [1, 8, 13, 23, 63, 542, 9104]


def test_radix_sort_short():
    """Test radix sort with tiny list."""
    list = [1]
    radix(list)
    assert list == [1]
