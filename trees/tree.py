class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


'''
Binary Tree
Create a Binary Tree class
Define a method for each of the depth first traversals:
pre order
in order
post order which returns an array of the values, ordered appropriately.
'''


class Binary_tree:
    def __init__(self):
        self.root = None

    def pre_order(self, root):
        '''
            root >> left >> right
            return: nothing
        '''
        print(root.val)
        if root.left:
            self.pre_order(root.left)
        if root.right:
            self.pre_order(root.right)

    def in_order(self, root):
        '''
            left >> root >> right
            return: nothing
        '''

        if root.left:
            self.in_order(root.left)
        print(root.val)
        if root.right:
            self.in_order(root.right)

    def post_order(self, root, arr=[]):
        '''
            left >> right >> root
            return: array with values ordered appropriately.
        '''

        if root.left:
            self.post_order(root.left, arr)

        if root.right:
            self.post_order(root.right, arr)

        arr.append(root.val)

        if root is self.root:
            return arr


class Binary_Search_Tree(Binary_tree):

    def add(self, value):
        '''
        :param value:
        :return: Nothing
        '''
        if not isinstance(value, int):
            raise Exception('Value Must Be Int Not ' + str(type(value)))
        cur = self.root
        new_node = Node(value)

        if self.root is None:
            self.root = Node(value)
            return

        while True:

            if cur.val <= value:
                if not cur.right:
                    cur.right = new_node
                    break
                else:
                    cur = cur.right
                    continue

            if cur.val > value:
                if not cur.left:
                    cur.left = new_node
                    break
                else:
                    cur = cur.left

    def contains(self, value):
        '''
        :param value:
        :return: boolean indicating whether or not the value is in the tree at least once.
        '''
        if not isinstance(value, int):
            raise Exception('Value Must Be Int Not ' + str(type(value)))

        cur = self.root

        while cur:
            if cur.val == value:
                return True
            else:
                if cur.val < value:
                    cur = cur.right
                else:
                    cur = cur.left
        return False


def my_post_order(root):
    cur = root
    res =[]
    stack = []

    while True:
        while cur:
            stack.append(cur)
            cur = cur.left
        
        

        if len(stack) < 1:
            return res

        node = stack[-1]


        stack.pop(len(stack)-1)

        if node.val != None:
            res.append(node.val)
            
        cur = node.left




if __name__ == "__main__":
    tree = Binary_tree()

    tree.root = Node("A")

    tree.root.left = Node("B")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")

    tree.root.right = Node("C")
    tree.root.right.left = Node("F")

    # tree.pre_order(tree.root)
    # tree.in_order(tree.root)
    print(tree.post_order(tree.root))
    print("&^"*40)
    print(my_post_order(tree.root))

    ###########################################

    ### Binary_Search_Tree
    print("#" * 50)
    print('Binary_Search_Tree')
    search_Tree = Binary_Search_Tree()

    search_Tree.root = Node(50)

    search_Tree.root.left = Node(40)
    search_Tree.root.left.left = Node(30)
    search_Tree.root.left.right = Node(45)

    search_Tree.root.right = Node(70)
    search_Tree.root.right.left = Node(60)

    search_Tree.add(499)

    print(search_Tree.contains(499))
    print("=" * 10)
    print(search_Tree.pre_order(search_Tree.root))
