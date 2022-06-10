from linked_list_project.linked_list import Node, Linked_list
import pytest


def test_node(new_node):
    assert new_node


def test_inserting(new_list):
    new_list.insert(00)
    actual = new_list.head.value
    expected = 00
    assert actual == expected


def test_head(new_list):
    actual = new_list.head.value
    expected = 10
    assert actual == expected


def test_multiple_insert(new_list):
    new_list.insert(00)
    actual = new_list.head.value
    expected = 00
    assert actual == expected

    new_list.insert(-10)
    actual = new_list.head.value
    expected = -10
    assert actual == expected

    new_list.insert(-20)
    actual = new_list.head.value
    expected = -20
    assert actual == expected


def test_searching_found(new_list):
    actual = new_list.includes(30)
    expected = True
    assert actual == expected


def test_searching_not_found(new_list):
    actual = new_list.includes(1025)
    expected = False
    assert actual == expected


def test_printing_list(new_list):
    actual = new_list.to_string()
    expected = "{ 10 } -> { 20 } -> { 30 } -> { 40 } -> { 50 } -> NULL"
    assert actual == expected


@pytest.fixture
def new_node():
    new_node = Node(10)
    return new_node


@pytest.fixture
def new_list():
    new_list = Linked_list()
    new_list.insert(50)
    new_list.insert(40)
    new_list.insert(30)
    new_list.insert(20)
    new_list.insert(10)
    return new_list
