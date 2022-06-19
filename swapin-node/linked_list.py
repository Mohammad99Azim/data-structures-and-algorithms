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


def swaping_node(link_list, val1, val2):
    cur1 = link_list.head
    cur2 = link_list.head

    if link_list.head.value == val1 or link_list.head.value == val2:
        head1 = link_list.head  # 1
        head_next1 = link_list.head.next  # 2
        next_next1 = link_list.head.next.next  # 3

        link_list.head = head_next1
        head1.next = next_next1
        head_next1.next = head1
        return link_list

    if link_list.head.value == val1:
        while cur2:
            if cur2.next.value == val2:
                break
            cur2 = cur2.next

        head1 = link_list.head  # 1

        current_next2 = cur2.next  # 3
        next_next2 = cur2.next.next  # 5 ##

        link_list.head = current_next2
        cur2.next.next = head1.next

        cur2.next = head1
        head1.next = next_next2

        return link_list

    if link_list.head.value == val2:
        while cur1:
            if cur1.next.value == val1:
                break
            cur1 = cur1.next

        head2 = link_list.head  # 1

        current_next1 = cur1.next  # 4
        next_next1 = cur1.next.next  # 5

        link_list.head = current_next1
        cur1.next.next = head2.next

        cur1.next = head2
        head2.next = next_next1

        return link_list

    # without the head stuff
    while cur1:
        if cur1.next.value == val1:
            break
        cur1 = cur1.next

    while cur2:
        if cur2.next.value == val2:
            break
        cur2 = cur2.next

    if cur1.next == cur2 or cur2.next == cur1:

        if cur1.next == cur2:
            current_next1 = cur1.next  # 3
            current_next2 = cur2.next  # 4

            cur1.next = cur2.next
            cur2.next = cur2.next.next
            current_next2.next = current_next1
            return link_list
        else:
            if cur2.next == cur1:
                current_next2 = cur2.next
                current_next1 = cur1.next

                cur2.next = cur1.next
                cur1.next = cur1.next.next
                current_next1.next = current_next2

            return link_list

    current_next1 = cur1.next  # 2
    next_next1 = cur1.next.next  # 3

    current_next2 = cur2.next  # 4
    next_next2 = cur2.next.next  # 5

    # starting

    cur1.next = cur2.next
    cur2.next = current_next1

    cur2.next.next = next_next2
    cur1.next.next = next_next1

    return link_list


def swap_in_list(link_list, val1, val2):
    cur1 = cur2 = link_list.head

    if link_list.head.value != val1 and link_list.head.value != val2:
        while cur1:
            if cur1.next.value == val1:
                break
            cur1 = cur1.next

        while cur2:
            if cur2.next.value == val2:
                break
            cur2 = cur2.next
    else:
        the_current = None
        if link_list.head.next.value == val1 or link_list.head.next.value == val2:

            head = link_list.head

            # switching

            link_list.head = head.next
            head.next = link_list.head.next
            link_list.head.next = head

            return link_list

        elif link_list.head.value == val1:
            while cur2:
                if cur2.next.value == val2:
                    the_current = cur2
                    break
                cur2 = cur2.next

        elif link_list.head.value != val2:
            while cur1:
                if cur1.next.value == val1:
                    the_current = cur1
                    break
                cur1 = cur1.next

        list_head = link_list.head
        list_head_next = link_list.head.next

        # switching
        link_list.head.next = the_current.next.next
        link_list.head = the_current.next

        the_current.next.next = list_head_next
        the_current.next = list_head
        return link_list

    current_next1 = cur1.next
    current_next_next1 = cur1.next.next

    if cur1.next == cur2:
        # if the val1 after val2  or <- ->
        cur1.next.next = cur2.next.next
        cur1.next = current_next_next1
        current_next_next1.next = current_next1
    else:
        # switching
        cur1.next.next = cur2.next.next
        cur1.next = cur2.next

        cur2.next.next = current_next_next1
        cur2.next = current_next1

    return link_list


if __name__ == '__main__':
    one = Linked_list()
    one.insert(10)
    one.insert(20)
    one.insert(22)
    one.insert(23)
    one.insert(24)
    one.insert(25)

    print(one.includes([2, 3]))

    print(one.to_string())
    print('After :')
    swap_in_list(one, 25, 10)

    print(one.to_string())
