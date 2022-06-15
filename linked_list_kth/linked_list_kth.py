class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:

    def __init__(self):
        self.head = None
        self.cur = None
        self.node_counter = 0

    @staticmethod
    def create_node(val):
        new_Node = Node(val)
        return new_Node

    def insert(self, val=None):
        if val is None:
            raise Exception("Sorry, you should enter a value")

        node_to_insert = self.create_node(val)

        if self.head is None:
            self.cur = node_to_insert

        node_to_insert.next = self.head
        self.head = node_to_insert
        self.node_counter += 1

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

    def append(self, value):
        if value is None:
            raise Exception("Sorry, you should enter a value")

        new_node = self.create_node(value)
        if self.head is None:
            self.head = new_node
            self.cur = new_node
        else:
            self.cur.next = new_node
            self.cur = new_node
        self.node_counter += 1

    def insert_before(self, value, new_value):
        if value is None or new_value is None:
            raise Exception("Sorry, you should enter a value in the list and new value you want to add it before the "
                            "value in the list")

        new_node = self.create_node(new_value)
        checker = self.head

        if checker is None:
            raise Exception("Sorry, the list is Empty")

        if checker.value == value:
            self.insert(new_value)
            return

        while checker.next:
            if checker.next.value == value:
                new_node.next = checker.next
                checker.next = new_node
                self.node_counter += 1
                return
            checker = checker.next
        raise Exception("the value you want insert before it not found in the list")

    def insert_after(self, value, new_value):
        if value is None or new_value is None:
            raise Exception("Sorry, you should enter a value in the list and new value you want to add it after the "
                            "value in the list")

        new_node = self.create_node(new_value)
        checker = self.head

        if checker is None:
            raise Exception("Sorry, the list is Empty")

        while checker:
            if checker.value == value:
                if checker == self.cur:
                    self.append(new_value)
                    return
                new_node.next = checker.next
                checker.next = new_node
                self.node_counter += 1
                return
            checker = checker.next
        raise Exception("the value you want insert after it not found in the list")

    def delete(self, value):
        checker = self.head

        if self.head.value == value:
            self.head = self.head.next
            self.node_counter -= 1
            return

        while checker:
            if checker.next == self.cur and checker.next.value == self.cur.value:
                self.cur = checker
                checker.next = None
                self.node_counter -= 1
                return
            if checker.next.value == value:
                checker.next = checker.next.next
                self.node_counter -= 1
                return
            checker = checker.next
        raise Exception("Sorry, the value you want to delete not found")

    def kth_from_end(self, k):

        if k < 0:
            raise Exception("k must be 0 or positive value !!!")

        if self.node_counter <= 0:
            raise Exception("Sorry, the List is Empty !!!")

        if self.node_counter - 1 < k:
            raise Exception("Sorry, the index you enter out of range !!!")

        counter = self.node_counter - 1 - k
        cur = self.head

        for x in range(0, counter):
            cur = cur.next
        return cur.value

    def find_middle_node(self):
        if self.node_counter <= 0:
            raise Exception("Sorry, the List is Empty !!!")
        cur = self.head
        middle = self.node_counter // 2
        for x in range(0, middle):
            cur = cur.next
        return cur.value


if __name__ == '__main__':
    one = Linked_list()
    one.insert(10)
    one.insert(20)
    one.insert(30)
    one.append(100)
    one.insert_after(100, 59)
    one.insert_before(30, 22)
    print(one.to_string())
    one.delete(22)
    print(one.includes(220))
    print(one.to_string())

    print(one.node_counter)
    print(one.kth_from_end(0))
    print(one.find_middle_node())
