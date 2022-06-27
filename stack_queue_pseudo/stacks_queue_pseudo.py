class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_Node = Node(value)
        new_Node.next = self.top
        self.top = new_Node
        self.size += 1

    def pop(self):  # need Rais

        ss = self.top
        self.top = self.top.next
        self.size -= 1
        return ss.val

    def peek(self):
        if self.top is None:
            raise Exception("The PseudoQueue is Empty")
        return self.top.val


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __str__(self):
        loo = self.stack2.top
        print('\u2190 Queue \u2190 \n')
        print('\u2190   \u2190  \u2190')
        while loo:
            print(str(loo.val) + " ", end="")
            loo = loo.next
        return "\n _______"

    def enqueue(self, value):
        self.stack1.push(value)
        self.stack2.top = None

        t = self.stack1.top
        while t:
            self.stack2.push(t.val)
            t = t.next

    def dequeue(self):
        self.stack1.peek()
        self.stack2.top = None

        t = self.stack1.top
        while t:
            self.stack2.push(t.val)
            t = t.next
        self.stack2.pop()

        self.stack1.top = None
        t = self.stack2.top
        while t:
            self.stack1.push(t.val)
            t = t.next


if __name__ == '__main__':
    ase = PseudoQueue()

    ase.enqueue(10)
    ase.enqueue(11)
    ase.enqueue(12)
    ase.enqueue(13)
    ase.enqueue(14)
    print(ase)
    ase.dequeue()
    ase.dequeue()
    print(ase)
