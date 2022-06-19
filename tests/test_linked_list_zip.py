from linked_list_zip.linked_list_zip import *
import pytest


def test_list_one_longer(list_one, list_two):
    actual = zip_lists(list_one, list_two)  # Switching the Argument i pass to the function

    new_list = Linked_list()
    new_list.insert(50)
    new_list.insert(40)
    new_list.insert(30)
    new_list.insert('B')
    new_list.insert(20)
    new_list.insert('A')
    new_list.insert(10)

    expected = new_list

    a = expected.head
    b = actual.head

    while a is not None and b is not None:
        assert a.value == b.value
        a = a.next
        b = b.next


def test_list_two_longer(list_one, list_two):
    actual = zip_lists(list_two, list_one)  # Switching the Argument i pass to the function
    new_list = Linked_list()
    new_list.insert(50)
    new_list.insert(40)
    new_list.insert(30)
    new_list.insert(20)
    new_list.insert('B')
    new_list.insert(10)
    new_list.insert('A')
    expected = new_list

    a = expected.head
    b = actual.head

    while a is not None and b is not None:
        assert a.value == b.value
        a = a.next
        b = b.next


def test_k_greater_than_length(list_one, list_three):
    with pytest.raises(Exception) as e:
        zip_lists(list_one, list_three)

    assert (
            repr(e)
            == """<ExceptionInfo Exception('One Of the lists is Empty') tblen=2>"""
    )


@pytest.fixture
def list_one():
    list_one = Linked_list()
    list_one.insert(50)
    list_one.insert(40)
    list_one.insert(30)
    list_one.insert(20)
    list_one.insert(10)
    return list_one


@pytest.fixture
def list_two():
    list_two = Linked_list()
    list_two.insert('B')
    list_two.insert('A')
    return list_two


@pytest.fixture
def list_three():
    list_three = Linked_list()
    return list_three
