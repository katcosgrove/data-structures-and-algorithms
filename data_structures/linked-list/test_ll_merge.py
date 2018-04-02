from ll_merge import merge_lists


def test_merge_list_equal(second_small_ll, small_ll):
    merge_lists(second_small_ll, small_ll)
    assert small_ll.__len__() == 8


def test_merge_list_large_first(large_ll, small_ll):
    merge_lists(large_ll, small_ll)
    assert large_ll._size == 13


def test_merge_list_small_first(small_ll, large_ll):
    merge_lists(small_ll, large_ll)
    assert large_ll._size == 12
