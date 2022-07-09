import pytest
from tree_fizz_buzz.tree_fizz_buzz import *


def test_tree_interger_valuse(my_tree):
    assert my_tree.root.child[1].val == 5

    assert my_tree.root.child[2].child[1].val == 30

    assert my_tree.root.child[0].child[2].val == 6

    assert my_tree.root.child[0].child[1].val == 7

def test_tree_after_change(my_tree):

    fizz_buzz_tree(my_tree)
    assert my_tree.root.child[1].val == "Buzz"

    assert my_tree.root.child[2].child[1].val == "FizzBuzz"

    assert my_tree.root.child[0].child[2].val == "Fizz"

    assert my_tree.root.child[0].child[1].val == "7"


def test_edge_case_only_one_node():
    k_ary_tree = My_Tree()
    k_ary_tree.root = Node(9)

    assert k_ary_tree.root.val == 9

    fizz_buzz_tree(k_ary_tree)

    assert k_ary_tree.root.val == "Fizz"


def test_rais_exception_tree_empty():
    k_ary_tree = My_Tree()
    with pytest.raises(Exception) as e:
        fizz_buzz_tree(k_ary_tree)
    assert repr(e) == "<ExceptionInfo Exception('The Tree Is Empty !!!') tblen=2>"




@pytest.fixture
def my_tree():
    k_ary_tree = My_Tree()

    k_ary_tree.root = Node(9)

    k_ary_tree.root.child.append(Node(1))
    k_ary_tree.root.child.append(Node(5))
    k_ary_tree.root.child.append(Node(15))

    k_ary_tree.root.child[0].child.append(Node(12))
    k_ary_tree.root.child[0].child.append(Node(7))
    k_ary_tree.root.child[0].child.append(Node(6))

    k_ary_tree.root.child[1].child.append(Node(10))
    k_ary_tree.root.child[1].child.append(Node(19))
    k_ary_tree.root.child[1].child.append(Node(21))

    k_ary_tree.root.child[2].child.append(Node(65))
    k_ary_tree.root.child[2].child.append(Node(30))

    return k_ary_tree