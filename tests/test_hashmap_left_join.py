import sys 
sys.path.append("./")
import pytest

from hashmap_left_join.hashmap_left_join import leftJoin
from hashtable.hashtables import HashTable


def test_left_join(table1,table2):
    actual = leftJoin(table1,table2)
    expected = [['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['outfit', 'garb', None], ['wrath', 'anger', 'delight']]
    assert actual == expected

def test_left_join2(table1):
    actual = leftJoin(table1,table1)
    expected = [['diligent', 'employed', 'employed'], ['fond', 'enamored', 'enamored'], ['guide', 'usher', 'usher'], ['outfit', 'garb', 'garb'], ['wrath', 'anger', 'anger']]
    assert actual == expected

def test_left_join3(table1):
    hashtable2 = HashTable(1024)

    actual = leftJoin(table1,hashtable2)
    expected = [['diligent', 'employed', None], ['fond', 'enamored', None], ['guide', 'usher', None], ['outfit', 'garb', None], ['wrath', 'anger', None]]
    assert actual == expected



@pytest.fixture
def table1():
    hashtable1 = HashTable(1024)
    hashtable1.set('diligent', 'employed')
    hashtable1.set('fond', 'enamored')
    hashtable1.set('guide', 'usher')
    hashtable1.set('outfit', 'garb')
    hashtable1.set('wrath', 'anger')

    return hashtable1


@pytest.fixture
def table2():
    hashtable2 = HashTable(1024)
    hashtable2.set('diligent', 'idle')
    hashtable2.set('fond', 'averse')
    hashtable2.set('guide', 'follow')
    hashtable2.set('flow', 'jam')
    hashtable2.set('wrath', 'delight')

    return hashtable2







