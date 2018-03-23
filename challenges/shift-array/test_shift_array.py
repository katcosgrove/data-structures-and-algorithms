import shift_array as sa


def test_insertShiftArray():
    assert sa.insertShiftArray([1, 2, 3, 4], 5) == [1, 2, 5, 3, 4]


def test_empty_insertShiftArray():
    assert sa.insertShiftArray([], 200) == [200]


def test_odd_insertShiftArray():
    assert sa.insertShiftArray([1, 2, 3], 5) == [1, 2, 5, 3]