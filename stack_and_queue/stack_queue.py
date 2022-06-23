class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        loo = self.top
        print('\u2193 Stack \u2193 \n')
        while loo:
            print("   " + str(loo.val) + "\n")
            loo = loo.next
        return " _______"

    def push(self, value):
        new_Node = Node(value)
        new_Node.next = self.top
        self.top = new_Node
        self.size += 1

    def pop(self):  # need Rais
        if self.is_empty():
            raise Exception("Can't pop the Stack is Empty")
        ss = self.top
        self.top = self.top.next
        self.size -= 1
        return ss.val

    def peek(self):
        if self.is_empty():
            raise Exception("the Stack is Empty")
        return self.top.val

    def is_empty(self):
        if self.top is None:
            return True
        return False


class Queue:
    def __init__(self):
        self.front = None
        self.rare = None

    def __str__(self):
        loo = self.front
        print('\u2190 Queue \u2190 \n')
        print('\u2190   \u2190  \u2190')
        while loo:
            print(str(loo.val) + " ", end="")
            loo = loo.next
        return "\n _______"

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.rare = new_node
        else:
            self.rare.next = new_node
            self.rare = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Can't dequeue The Queue is Empty")
        va = self.front.val
        self.front = self.front.next
        return va

    def peek(self):
        if self.is_empty():
            raise Exception("Can't peek The Queue is Empty")
        return self.front.val

    def is_empty(self):
        if self.front is None:
            return True
        return False


if __name__ == '__main__':
    ase = Stack()

    ase.push(10)
    ase.push(11)
    ase.push(12)
    ase.push(13)
    ase.push(14)
    ase.pop()
    print("This is Peek: " + str(ase.peek()) + "\n")
    print("This is IsEmpty: " + str(ase.is_empty()) + "\n")
    print(ase)

    q = Queue()
    q.peek()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")
    q.enqueue("E")
    print(q)
    print(q.peek())
    print(q.is_empty())
    print(q.dequeue())
    print(q.dequeue())
