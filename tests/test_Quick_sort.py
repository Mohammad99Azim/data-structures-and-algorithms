from sorting.quick.QuickSort import *


def test_QuickSort():
    actual = QuickSort([1, 2, 4, 6, 8, 2, 1, 4], 0, 7)
    exception = [1, 1, 2, 2, 4, 4, 6, 8]
    assert actual == exception


def test_empty_QuickSort():
    actual = QuickSort([], 0, 0)
    exception = None
    assert actual == exception


def test_QuickSort_2():
    actual = QuickSort([8, 4, 23, 42, 16, 15],0,5)
    exception = [4, 8, 15, 16, 23, 42]
    assert actual == exception
