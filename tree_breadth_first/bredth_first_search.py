class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class My_Tree:

    def __init__(self):
        self.root = None


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

        results.append(queue[0].val)
        queue.pop(0)
    return results
