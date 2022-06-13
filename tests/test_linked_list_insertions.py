from linked_list_insertions.linked_list_insertions import Node, Linked_list
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


# 1. Can successfully add a node to the end of the linked list
def test_add_to_end(new_list):
    new_list.append(22)
    actual = new_list.cur.value
    expected = 22
    assert actual == expected


# 2. Can successfully add multiple nodes to the end of a linked list
def test_add_multiple_to_end(new_list):
    new_list.append(00)
    actual = new_list.cur.value
    expected = 00
    assert actual == expected

    new_list.append(-10)
    actual = new_list.cur.value
    expected = -10
    assert actual == expected

    new_list.append(-20)
    actual = new_list.cur.value
    expected = -20
    assert actual == expected


# 3. Can successfully insert a node before a node located i the middle of a linked list
def test_insert_before_in_middle(new_list):
    new_list.insert_before(30, -22)
    actual = new_list.head.next.next.value
    expected = -22
    assert actual == expected


# 4. Can successfully insert a node before the first node of a linked list
def test_insert_to_first(new_list):
    new_list.insert_before(10, -22)
    actual = new_list.head.value
    expected = -22
    assert actual == expected


# 5. Can successfully insert after a node in the middle of the linked list
def test_insert_after_in_middle(new_list):
    new_list.insert_after(30, -22)
    actual = new_list.head.next.next.next.value
    expected = -22
    assert actual == expected


# 6. Can successfully insert a node after the last node of the linked list
def test_insert_after_last(new_list):
    new_list.insert_after(50, -22)
    actual = new_list.cur.value
    expected = -22
    assert actual == expected


# Stretch Goal

def test_delete_from_first(new_list):
    new_list.delete(10)
    actual = new_list.head.value
    expected = 20
    assert actual == expected


def test_delete_from_middle(new_list):
    new_list.delete(30)
    actual = new_list.head.next.next.value
    expected = 40
    assert actual == expected


def test_delete_from_last(new_list):
    new_list.delete(50)
    actual = new_list.cur.value
    expected = 40
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
