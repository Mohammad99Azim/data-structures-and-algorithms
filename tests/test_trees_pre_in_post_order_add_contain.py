from trees.tree import *
import pytest
import builtins


# 1- Can successfully instantiate an empty tree
def test_instantiate_an_empty_tree():
    empty = Binary_tree()
    assert empty.root is None


# 2- Can successfully instantiate a tree with a single root node
def test_instantiate_an_one_node_tree():
    one = Binary_tree()
    one.root = Node(50)
    assert one.root.val == 50
    assert one.root.right is None
    assert one.root.left is None


# 3- For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_add_to_left_and_right():
    right_left = Binary_Search_Tree()
    right_left.add(50)
    assert right_left.root.val == 50
    right_left.add(80)
    assert right_left.root.right.val == 80
    right_left.add(30)
    assert right_left.root.left.val == 30


# 4- Can successfully return a collection from a preorder traversal
def test_pre_order_traversal(my_tree):
    real_print = builtins.print

    text = ""

    def mock_print(*args):
        nonlocal text
        text += "".join(args) + "\n"

    builtins.print = mock_print

    my_tree.pre_order(my_tree.root)
    assert text == 'A\nB\nD\nE\nC\nF\n'

    builtins.print = real_print


# 5- Can successfully return a collection from an inorder traversal
def test_in_order_traversal(my_tree):
    real_print = builtins.print

    text = ""

    def mock_print(*args):
        nonlocal text
        text += "".join(args) + "\n"

    builtins.print = mock_print

    my_tree.in_order(my_tree.root)
    assert text == 'D\nB\nE\nA\nF\nC\n'

    builtins.print = real_print


# 6- Can successfully return a collection from a postorder traversal
def test_post_order_traversal(my_tree):
    expected = my_tree.post_order(my_tree.root)
    actual = ['D', 'E', 'B', 'F', 'C', 'A']
    assert actual == expected


# 7- Test the contains method
def test_contains_true_false(my_search_tree):
    # True
    assert my_search_tree.contains(50) is True
    assert my_search_tree.contains(30) is True
    assert my_search_tree.contains(60) is True
    # False
    assert my_search_tree.contains(1000) is False
    assert my_search_tree.contains(10) is False
    assert my_search_tree.contains(46) is False


def test_contains_rais_exception(my_search_tree):
    with pytest.raises(Exception) as e:
        my_search_tree.contains("str")
    assert repr(e) == '<ExceptionInfo Exception("Value Must Be Int Not <class \'str\'>") tblen=2>'


def test_add_rais_exception(my_search_tree):
    with pytest.raises(Exception) as e:
        my_search_tree.add("str")
    assert repr(e) == '<ExceptionInfo Exception("Value Must Be Int Not <class \'str\'>") tblen=2>'

@pytest.fixture
def my_tree():
    tree = Binary_tree()

    tree.root = Node("A")

    tree.root.left = Node("B")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")

    tree.root.right = Node("C")
    tree.root.right.left = Node("F")

    return tree


@pytest.fixture
def my_search_tree():
    tree = Binary_Search_Tree()

    tree.root = Node(50)

    tree.root.left = Node(40)
    tree.root.left.left = Node(30)
    tree.root.left.right = Node(45)

    tree.root.right = Node(70)
    tree.root.right.left = Node(60)

    return tree
