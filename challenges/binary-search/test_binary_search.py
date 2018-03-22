import binary_search as bs


def test_match_BinarySearch():
    assert bs.BinarySearch([1, 2, 3, 4, 5], 5) == 4


def test_no_BinarySearch():
    assert bs.BinarySearch([1, 2, 3, 4, 5], 8) == -1


def test_empty_BinarySearch():
    assert bs.BinarySearch([], 1) == -1
