from tree_max.tree_max import *
import pytest


def test_max_value(my_tree):
    my_tree.max_value() == 70


def test_max_value_2(my_tree):
    my_tree.root.right.left.right = Node(1000)
    my_tree.max_value() == 1000


def test_max_raise_exception():
    tree = Binary_Tree()
    with pytest.raises(Exception) as e:
        tree.max_value()
    assert repr(e) == "<ExceptionInfo Exception('The Tree Is Empty !!!') tblen=2>"


@pytest.fixture
def my_tree():
    tree = Binary_Tree()

    tree.root = Node(50)

    tree.root.left = Node(40)
    tree.root.left.left = Node(30)
    tree.root.left.right = Node(45)

    tree.root.right = Node(70)
    tree.root.right.left = Node(60)

    return tree
