
from hashtable.hashtables import *

# keys, and a synonym of the key as values.
hashtable1 = HashTable(1024)
hashtable1.set('diligent', 'employed')
hashtable1.set('fond', 'enamored')
hashtable1.set('guide', 'usher')
hashtable1.set('outfit', 'garb')
hashtable1.set('wrath', 'anger')


# keys, and antonyms of the key as values.
hashtable2 = HashTable(1024)
hashtable2.set('diligent', 'idle')
hashtable2.set('fond', 'averse')
hashtable2.set('guide', 'follow')
hashtable2.set('flow', 'jam')
hashtable2.set('wrath', 'delight')


def leftJoin(hashT1, hashT2):
    hashResult = []
    for x in hashT1.keys:
        val1 = hashT1.get(x)
        val2 = hashT2.get(x)
        hashResult.append([x, val1, val2])
    return hashResult

##### Stretch Goals #####
#
# def leftJoin(hashT1, hashT2, is_left=True):
#     hashResult = []
#     if is_left is not True:
#         cur = hashT1
#         hashT1 = hashT2
#         hashT2 = cur
#     for x in hashT1.keys:
#         val1 = hashT1.get(x)
#         val2 = hashT2.get(x)
#         hashResult.append([x, val1, val2])
#     return hashResult


if __name__ == "__main__":
    results = leftJoin(hashtable1, hashtable2)
    print(results)

    print("#"*40)
    for y in results:
        print(y)
