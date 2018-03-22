import binary_search as bs


def test_BinarySearch():
    assert bs.BinarySearch([1, 2, 3, 4, 5], 5) == 4

    assert bs.BinarySearch([1, 2, 3, 4, 5], 8) == -1

    assert bs.BinarySearch([], 1) == -1
