import shift_array as sa


def test_insertShiftArray():
    assert sa.insertShiftArray([1, 2, 3, 4], 5) == [1, 2, 5, 3, 4]
    assert sa.insertShiftArray([1, 2, 3, 4, 5, 6, 7, 8], 5) == [1, 2, 3, 4, 5, 5, 6, 7, 8]
    assert sa.insertShiftArray([20, 30, 59, 70], 200) == [20, 30, 200, 59, 70]