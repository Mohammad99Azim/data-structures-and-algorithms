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
            return False
        ss = self.top
        self.top = self.top.next
        self.size -= 1
        return ss.val

    def is_empty(self):
        if self.top is None:
            return True
        return False


def validate_brackets(string):
    sta = Stack()
    if len(string) == 0:
        raise Exception("The string is Empty !!!")
    for x in string:
        if x == "{" or x == "(" or x == "[":
            sta.push(x)
        elif x == "}" or x == ")" or x == "]":
            if sta.is_empty():
                return False
            if sta.top.val == "{" and x == "}" or sta.top.val == "(" and x == ")" or sta.top.val == "[" and x == "]":
                sta.pop()
            else:
                return False
    if sta.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    print(validate_brackets("{"))
