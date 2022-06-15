from linked_list_kth.linked_list_kth import Node, Linked_list
import pytest


# Where k is greater than the length of the linked list
def test_k_greater_than_length(new_list):
    with pytest.raises(Exception) as e:
        new_list.kth_from_end(10)

    assert (
            repr(e)
            == """<ExceptionInfo Exception('Sorry, the index you enter out of range !!!') tblen=2>"""
    )


# Where k and the length of the list are the same
def test_k_equal_length(new_list):
    with pytest.raises(Exception) as e:
        new_list.kth_from_end(5)

    assert (
            repr(e)
            == """<ExceptionInfo Exception('Sorry, the index you enter out of range !!!') tblen=2>"""
    )


# Where k is not a positive integer
def test_k_not_positive(new_list):
    with pytest.raises(Exception) as e:
        new_list.kth_from_end(-5)

    assert (
            repr(e)
            == """<ExceptionInfo Exception('k must be 0 or positive value !!!') tblen=2>"""
    )


# Where the linked list is of a size 1
def test_kth_list_size_one():
    new_list = Linked_list()
    new_list.insert(50)
    actual = new_list.kth_from_end(0)
    expected = 50
    assert actual == expected


# where k is not at the end, but somewhere in the middle of the linked list
def test_k_in_middle(new_list):
    actual = new_list.kth_from_end(2)
    expected = 30
    assert actual == expected


@pytest.fixture
def new_list():
    new_list = Linked_list()
    new_list.insert(50)
    new_list.insert(40)
    new_list.insert(30)
    new_list.insert(20)
    new_list.insert(10)
    return new_list
