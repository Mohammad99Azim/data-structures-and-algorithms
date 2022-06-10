#
#
## TO TEST THIS FILE USE ==>  python -m pytest .\tests\test_linked_list\


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:

    def __init__(self):
        self.head = None

    @staticmethod
    def create_node(val):
        new_Node = Node(val)
        return new_Node

    def insert(self, val=None):
        if val is None:
            raise Exception("Sorry, you should enter a value")

        node_to_insert = self.create_node(val)
        node_to_insert.next = self.head
        self.head = node_to_insert

    def includes(self, value):
        checker = self.head
        while checker is not None:
            if checker.value is value:
                return True
            else:
                checker = checker.next
        return False

    def to_string(self):

        final_string = ""
        printer = self.head
        while printer:
            final_string += "{ " + f"{printer.value}" + " } -> "
            printer = printer.next
        final_string += "NULL"
        return final_string


if __name__ == '__main__':
    one = Linked_list()
    one.insert(10)
    one.insert(20)
    one.insert()

    print(one.includes([2, 3]))

    print(one.to_string())
