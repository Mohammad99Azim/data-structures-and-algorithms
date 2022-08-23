class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:

    def __init__(self,):
        self.head = None


# def merge(head1,head2):
#     resHead = None
#     if head1.value <= head2.value:
#         cur1=head1.next
#         temp = head1
#         resHead = head1
#         cur2 = head2
#     else:
#         cur1= head2.next
#         temp = head2
#         resHead = head2
#         cur2 = head1

#     while cur1 and cur2:

#         if cur1.value < cur2.value:
#             if temp.next is not cur1:
#                 temp.next = cur1
#                 temp = cur1
#             else:
#                 temp=cur1
#             cur1 = cur1.next 
#         elif cur2.value < cur1.value:
#             if temp.next is not cur2:
#                 temp.next = cur2
#                 temp = cur2 
#             else:
#                 temp=cur2
#             cur2 = cur2.next
#         else:
#             if temp.next is not cur1:
#                 temp.next = cur1
#                 temp = cur1
#                 cur1 = cur1.next
#             else:
#                 temp.next = cur2
#                 temp = cur2
#                 cur2 = cur2.next 
       
#     if cur1 is None:
#         temp.next = cur2
#     else:
#         temp.next = cur1
#     return resHead

def mergeLists(head1, head2):
    temp = None

    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.value <= head2.value:
        temp = head1
        temp.next = mergeLists(head1.next , head2)
    else:
        temp = head2
        temp.next = mergeLists(head1,head2.next)

    return temp
    

    
if __name__ == '__main__':

    link1 = Linked_list()
    link1.head = Node(1)
    link1= link1.head
    link1.next = Node(3)
    link1.next.next= Node(5)
    link1.next.next.next = Node(6)
    link1.next.next.next.next = Node(6)


    link2 = Linked_list()
    link2.head = Node(2)
    link2= link2.head
    link2.next = Node(4)
    link2.next.next = Node(6)
    link2.next.next.next = Node(6)
    

    

    print("hi"+ str(link2.value))

    ss =mergeLists(link1,link2)

    while ss:
        print(ss.value)
        ss = ss.next





















# class Binary_tree:
#     def __init__(self):
#         self.root = None

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# def post_order(root):
#     current = root
#     stack = []

#     while True:
#         while current:
#             stack.append(current)
#             stack.append(current)
#             current = current.left

#         if len(stack) == 0:
#             return

#         current = stack.pop()

#         if (len(stack) > 0 and stack[-1] == current):
#             current = current.right
#         else:
#             print(current.val, end = " ")
#             current = None
        

# if __name__ == "__main__":
#     tree = Binary_tree()

#     tree.root = Node(1)

#     tree.root.left = Node(2)
#     tree.root.left.right = Node(4)
#     tree.root.left.left = Node(3)

#     post_order(tree.root)