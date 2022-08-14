from hashtable.hashtables import HashTable


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None


def tree_intersection(tree1, tree2):

    tree1 = tree_breadth_first(tree1)
    tree2 = tree_breadth_first(tree2)
    theValues = []

    my_hash_table = HashTable(len(tree1))

    for ind,x in enumerate(tree1):
        my_hash_table.set(str(ind),x)

    for ind2 ,y in enumerate(tree2):
        val = my_hash_table.get(str(ind2))
        if val is not None and val == y:
            theValues.append(val)
    return theValues



def tree_breadth_first(tree):
    if tree.root is None:
        raise Exception("The Tree Is Empty !!!")
    root = tree.root
    queue = []
    results = []
    queue.append(root)
    while queue:
        if queue[0].left:
            queue.append(queue[0].left)

        if queue[0].right:
            queue.append(queue[0].right)

        results.append(queue[0].value)
        queue.pop(0)
    return results


if __name__ == '__main__':
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
    Tree2.root = TreeNode(150)
    Tree2.root.left = TreeNode(100)
    Tree2.root.left.left = TreeNode(75)
    Tree2.root.left.right = TreeNode(160)
    Tree2.root.left.right.left = TreeNode(125)
    Tree2.root.left.right.right = TreeNode(175)

    Tree2.root.right = TreeNode(250)
    Tree2.root.right.left = TreeNode(200)
    Tree2.root.right.right = TreeNode(350)
    Tree2.root.right.right.left = TreeNode(300)
    Tree2.root.right.right.right = TreeNode(1001)

    tree2 = Tree2


    print(tree_breadth_first(tree1))
    print(tree_intersection(tree1, tree2))
