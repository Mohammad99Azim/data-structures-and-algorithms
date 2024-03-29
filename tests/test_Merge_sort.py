from sorting.merge.MergSort import *


def test_InsertionSort():
    actual = mergesort([1, 2, 4, 6, 8, 2, 1, 4])
    exception = [1, 1, 2, 2, 4, 4, 6, 8]
    assert actual == exception


def test_empty_InsertionSort():
    actual = mergesort([])
    exception = []
    assert actual == exception


def test_InsertionSort_2():
    actual = mergesort([8, 4, 23, 42, 16, 15])
    exception = [4, 8, 15, 16, 23, 42]
    assert actual == exception
