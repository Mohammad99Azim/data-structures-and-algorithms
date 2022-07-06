from tree_breadth_first.bredth_first_search import *
import pytest


def test_max_value(my_tree):
    my_tree.tree_breadth_first() == [50,40,70,30,45,60]


def test_max_value_2(my_tree):
    my_tree.root.right.left.right = Node(100)
    my_tree.tree_breadth_first() == [50,40,70,30,45,60,100]


def test_max_raise_exception():
    tree = My_Tree()
    with pytest.raises(Exception) as e:
        tree.tree_breadth_first()
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
