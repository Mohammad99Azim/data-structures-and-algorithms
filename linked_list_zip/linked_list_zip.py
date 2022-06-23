from linked_list_kth.linked_list_kth import Node, Linked_list


def zip_lists(list_one, list_two):
    h_one = list_one.head
    h_two = list_two.head

    if list_one.head is None or list_two.head is None:
        raise Exception('One Of the lists is Empty')

    while h_one and h_two:

        changer = h_one
        if h_one.next is None:
            changer.next = h_two
            list_one.cur = list_two.cur  # just change the cur to make it point to end of the list
            break
        h_one = h_one.next
        changer.next = h_two

        changer = changer.next
        if h_two.next is None:
            changer.next = h_one
            break
        h_two = h_two.next
        changer.next = h_one

    return list_one


def merges(list_one, list_two):
    list_one.cur.next = list_two.head
    return list_one


def reverse(linked_list):

    prev = linked_list.head
    b = linked_list.head.next
    c = linked_list.head.next.next

    linked_list.head.next = None
    while c:
        b.next = prev
        prev = b
        b = c
        c = c.next
    b.next = prev
    linked_list.head = b






if __name__ == '__main__':
    one = Linked_list()
    one.insert(40)
    one.insert(30)
    one.insert(20)
    one.insert(10)

    two = Linked_list()
    two.append('A')
    two.append('B')
    two.append('C')
    two.append('D')
    two.append('E')
    two.append('F')
    two.append('G')
    two.append('H')

    three = Linked_list()
    three.append('L')
    three.append('M')
    three.append('N')

    print("List One :" + one.to_string() + "\n")
    print("List Two :" + two.to_string() + "\n")
    print("Zip Lists :" + zip_lists(one, two).to_string() + "\n")

    # YOU CAN SEE THE LIST ( one ) WAS CHANGED BY  ( zip_lists ) METHOD
    print("Merge Lists :" + merges(three, two).to_string() + "\n")

    print ('%%%%%%%%%%%%%%%%%%%%%%%%%%%% reverse:')
    print("Before :" + three.to_string() + "\n")
    reverse(three)
    print("After :" + three.to_string() + "\n")
