class Node:
    def __init__(self, val):
        self.val = val
        self.child = []


class My_Tree:

    def __init__(self):
        self.root = None


def fizz_buzz_tree(k_ary_tree):
    if k_ary_tree.root is None:
        raise Exception("The Tree Is Empty !!!")
    lists = [k_ary_tree.root]

    while lists:
        if lists[0].val % 5 == 0 and lists[0].val % 3 == 0:
            lists[0].val = "FizzBuzz"
        elif lists[0].val % 3 == 0:
            lists[0].val = "Fizz"
        elif lists[0].val % 5 == 0:
            lists[0].val = "Buzz"
        else:
            lists[0].val = str(lists[0].val)

        for x in lists[0].child:
            lists.append(x)
        lists.pop(0)


if __name__ == "__main__":
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


    print(k_ary_tree.root.child[1].val)
    print(k_ary_tree.root.child[2].child[1].val)

    fizz_buzz_tree(k_ary_tree)

    print(k_ary_tree.root.child[1].val)
    print(k_ary_tree.root.child[2].child[1].val)