import re
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
        self.__keys = []

    def set(self, key, value):
        hashkey = self.__hash(key)
        if self.__bucket[hashkey] == None:
            ll = LinkedList()
            self.__bucket[hashkey] = ll
        self.__bucket[hashkey].insert([key, value])
        self.__keys.append(key)

    def get(self, key):
        hashkey = self.__hash(key)
        if self.__bucket[hashkey] == None:
            return None
        cur = self.__bucket[hashkey].head
        while cur:
            if cur.value[0] == key:
                return cur.value[1]
            cur = cur.next

    def contains(self, key):
        for x in self.__keys:
            if x == key:
                return True
        return False

    def __hash(self, key):
        return sum(ord(x) for x in key) * 452 % self.__size

    def keys(self):
        return self.__keys


def repeated_word(string):
    hash_table = HashTable(100)
    string = string.lower()
    list_string = re.split(r"\W+",string)

    
    for x in list_string:
        if hash_table.get(x):
            return x
        hash_table.set(x, x)

    raise Exception("There is no repeated word")


if __name__ == "__main__":
    print(repeated_word('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'))
