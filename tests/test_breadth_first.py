from tree_breadth_first.bredth_first_search import *
import pytest


def test_make_empty_node():
    the_tree = My_Tree()
    the_tree.root = Node(2)
    the_tree.root.val == 2


def test_breadth_first(my_tree):
    tree_breadth_first(my_tree) == [50, 40, 70, 30, 45, 60]


def test_breadth_first_2(tree_two):
    tree_breadth_first(tree_two) == [50, 40, 70, 30, 45, 60, 100]


def test_breadth_first_3(tree_two):
    tree_breadth_first(tree_two) == [2, 7, 5, 2, 6, 4, 9, 5, 11]


def test_breadth_first_raise_exception():
    tree = My_Tree()
    with pytest.raises(Exception) as e:
        tree_breadth_first(tree)
    assert repr(e) == "<ExceptionInfo Exception('The Tree Is Empty !!!') tblen=2>"


@pytest.fixture
def my_tree():
    tree = My_Tree()

    tree.root = Node(50)

    tree.root.left = Node(40)
    tree.root.left.left = Node(30)
    tree.root.left.right = Node(45)

    tree.root.right = Node(70)
    tree.root.right.left = Node(60)

    return tree


@pytest.fixture
def tree_two():
    tree = My_Tree()

    tree.root = Node(50)

    tree.root.left = Node(40)
    tree.root.left.left = Node(30)
    tree.root.left.right = Node(45)

    tree.root.right = Node(70)
    tree.root.right.left = Node(60)

    return tree
