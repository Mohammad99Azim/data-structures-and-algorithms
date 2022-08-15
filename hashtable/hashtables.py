class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node


class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__bucket = [None] * self.__size
        self.keys = []

    def set(self, key, value):
        hashkey = self.__hash(key)
        if self.__bucket[hashkey] is None:
            ll = LinkedList()
            self.__bucket[hashkey] = ll
        self.__bucket[hashkey].insert([key, value])
        self.keys.append(key)

    def get(self, key):
        hashkey = self.__hash(key)
        if self.__bucket[hashkey] is None:
            return None
        cur = self.__bucket[hashkey].head
        while cur:
            if cur.value[0] == key:
                return cur.value[1]
            cur = cur.next

    def contains(self, key):
        for x in self.keys:
            if x == key:
                return True
        return False

    def __hash(self, key):
        return sum(ord(x) for x in key) * 452 % self.__size
    def keys(self):
        return self.keys


if __name__ == "__main__":
    table = HashTable(1000)
    table.set("mohammad", "red")
    table.set("ali", "blue")
    table.set("khaled", "green")

    print(table.get("khaled"))
