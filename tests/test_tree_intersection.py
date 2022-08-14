import pytest
from tree_intersection.tree_intersection import *


def test_two_trees(my_tree1,my_tree2):
    actual = tree_intersection(my_tree1,my_tree2)
    expected = [40, 30, 45, 60]
    assert actual == expected

def test_two_trees_V2(my_tree1):
    Tree1 = Tree()
    Tree1.root = TreeNode(150)
    Tree1.root.left = TreeNode(100)
    Tree1.root.left.left = TreeNode(75)
    Tree1.root.left.right = TreeNode(160)
    Tree1.root.left.right.left = TreeNode(125)
    Tree1.root.left.right.right = TreeNode(175)

    Tree1.root.right = TreeNode(250)
    Tree1.root.right.left = TreeNode(200)
    Tree1.root.right.right = TreeNode(350)
    Tree1.root.right.right.left = TreeNode(300)
    Tree1.root.right.right.right = TreeNode(500)

    tree1 = Tree1

    actual = tree_intersection(my_tree1,tree1)
    expected = []
    assert actual == expected


def test_two_trees_V3():
    Tree1 = Tree()
    Tree1.root = TreeNode(150)
    Tree1.root.left = TreeNode(100)
    Tree1.root.left.left = TreeNode(75)
    Tree1.root.left.right = TreeNode(160)
    Tree1.root.left.right.left = TreeNode(125)
    Tree1.root.left.right.right = TreeNode(175)

    Tree1.root.right = TreeNode(250)
    Tree1.root.right.left = TreeNode(200)
    Tree1.root.right.right = TreeNode(350)
    Tree1.root.right.right.left = TreeNode(300)
    Tree1.root.right.right.right = TreeNode(500)

    tree1 = Tree1



    Tree2 = Tree()
    Tree2.root = TreeNode(42)
    Tree2.root.left = TreeNode(100)
    Tree2.root.left.left = TreeNode(15)
    Tree2.root.left.right = TreeNode(160)
    Tree2.root.left.right.left = TreeNode(125)
    Tree2.root.left.right.right = TreeNode(175)

    Tree2.root.right = TreeNode(600)
    Tree2.root.right.left = TreeNode(200)
    Tree2.root.right.right = TreeNode(350)
    Tree2.root.right.right.left = TreeNode(4)
    Tree2.root.right.right.right = TreeNode(500)

    tree2 = Tree2

    actual = tree_intersection(tree1,tree2)
    expected = [100, 160, 200, 350, 125, 175, 500]
    assert actual == expected



def test_raise_exception():
    tree = Tree()
    with pytest.raises(Exception) as e:
        tree.tree_intersection(tree,tree)
    assert repr(e) == '<ExceptionInfo AttributeError("\'Tree\' object has no attribute \'tree_intersection\'") tblen=1>'


@pytest.fixture
def my_tree1():
    tree1 = Tree()

    tree1.root = TreeNode(50)

    tree1.root.left = TreeNode(40)
    tree1.root.left.left = TreeNode(30)
    tree1.root.left.right = TreeNode(45)

    tree1.root.right = TreeNode(70)
    tree1.root.right.left = TreeNode(60)

    return tree1

@pytest.fixture
def my_tree2():
    tree1 = Tree()

    tree1.root = TreeNode(3)

    tree1.root.left = TreeNode(40)
    tree1.root.left.left = TreeNode(30)
    tree1.root.left.right = TreeNode(45)

    tree1.root.right = TreeNode(5)
    tree1.root.right.left = TreeNode(60)

    return tree1

