class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Binary_Tree:

    def __init__(self):
        self.root = None

    def pre_order(self, root=None, arr=[]):
        if self.root is None:
            return None
        if root is None:
            root = self.root
        arr.append(root.val)
        if root.right:
            self.pre_order(root.right)
        if root.left:
            self.pre_order(root.left)
        return arr

    def max_value(self):
        arr = self.pre_order()
        if arr is None:
            raise Exception("The Tree Is Empty !!!")
        max = None
        for x in arr:
            if max is None:
                max = x
            elif x > max:
                max = x
        return max


if __name__ == "__main__":
    new_node = Node(10)

    the_tree = Binary_Tree()

    the_tree2 = Binary_Tree()

    the_tree.root = Node(2)
    the_tree.root.right = Node(5)
    the_tree.root.right.right = Node(9)
    the_tree.root.right.right.left = Node(4)

    the_tree.root.left = Node(7)
    the_tree.root.left.left = Node(2)
    the_tree.root.left.right = Node(6)
    the_tree.root.left.right.left = Node(5)
    the_tree.root.left.right.right = Node(11)

    print(the_tree.max_value())
