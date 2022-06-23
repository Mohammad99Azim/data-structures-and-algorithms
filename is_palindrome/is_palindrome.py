from linked_list_kth.linked_list_kth import Node, Linked_list


def is_palindrome(linked_list):
    test_list = []

    point_now = linked_list.head
    while point_now:
        test_list.insert(0, point_now.value)
        point_now = point_now.next

    point_now = linked_list.head
    for x in range(len(test_list)):
        if test_list[x] != point_now.value:
            return False
        point_now = point_now.next
    return True


if __name__ == '__main__':

    three = Linked_list()
    three.append('L')
    three.append('L')
    three.append('L')
    three.append('L')
    three.append('M')
    three.append('L')
    three.append('L')
    three.append('L')
    # print("List One :" + one.to_string() + "\n")
    # print("List Two :" + two.to_string() + "\n")

    print(is_palindrome(three))
