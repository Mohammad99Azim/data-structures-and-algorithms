class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class My_Tree:

    def __init__(self):
        self.root = None

    def tree_breadth_first(self, root=None):
        if self.root is None:
            raise Exception("The Tree Is Empty !!!")
        if root is None:
            root = self.root

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


if __name__ == "__main__":
    the_tree = My_Tree()

    the_tree.root = Node(2)
    the_tree.root.right = Node(5)
    the_tree.root.right.right = Node(9)
    the_tree.root.right.left = Node(4)

    the_tree.root.left = Node(7)
    the_tree.root.left.left = Node(2)
    the_tree.root.left.right = Node(6)
    the_tree.root.left.right.left = Node(5)
    the_tree.root.left.right.right = Node(11)
    print(the_tree.tree_breadth_first(the_tree.root))
