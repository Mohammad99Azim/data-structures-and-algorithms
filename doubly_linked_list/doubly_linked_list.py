class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.head = None
        self.cur = None

    def insert(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.cur = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.cur = new_node
        else:
            self.cur.next = new_node
            new_node.prev = self.cur
            self.cur = new_node

    def list_print(self):
        curr = self.head
        string = ""
        while curr:
            string += f"[ {curr.val} ]-->"
            curr = curr.next
        string += " None"
        print(string)

    def back_print(self):
        holder = self.cur
        string = ""
        while holder:
            string += f"[ {holder.val} ]-->"
            holder = holder.prev
        string += " None"
        print(string)

    def inclued(self, val):
        searcher = self.head
        while searcher:
            if searcher.val == val:
                return True
            searcher = searcher.next
        return False

# lis = List()
#
# lis.insert(10)
# lis.insert(20)
# lis.insert(30)
# lis.insert(40)
# lis.append(-40)
# lis.append(-30)
# lis.append(-20)
# lis.list_print()
# lis.back_print()
# print(lis.inclued(-10))
