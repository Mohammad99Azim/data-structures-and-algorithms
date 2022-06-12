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

    def delete(self, val):
        searcher = self.head
        while searcher:
            if searcher.val == val:
                if searcher.next and searcher.prev != None:
                    searcher.next.prev = searcher.prev
                    searcher.prev.next = searcher.next
                elif searcher.next == None:
                    self.cur = searcher.prev
                    searcher.prev.next = None
                    searcher.prev = None
                elif searcher.prev == None:
                    self.head = searcher.next
                    searcher.next.prev = None
                    searcher.next = None

            searcher = searcher.next
        return "Not Found ..!!"

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
# lis.delete(-20)
# lis.delete(40)
# lis.delete(10)
# lis.back_print()