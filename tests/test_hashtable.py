import pytest
from hashtable.hashtables import *

# Setting a key/value to your hashtable results in the value being in the data structure
def test_set_method_setting(hashtable):
    expect = hashtable._HashTable__bucket[98 * 452 % 1024].head.value[1]
    actual = "b value"
    assert expect == actual

# Retrieving based on a key returns the value stored
def test_get_method_retrieving(hashtable):
    expect = hashtable.get("b")
    actual = "b value"
    assert expect == actual

# Successfully returns null for a key that does not exist in the hashtable
def test_contains(hashtable):
    expect = hashtable.get("z")
    actual = None
    assert expect == actual

# Successfully returns a list of all unique keys that exist in the hashtable
def test_keys_method(hashtable):
    expect = hashtable.keys()
    actual = ["b"]
    assert expect == actual


# Successfully handle a collision within the hashtable
def test_handle_collision():
    # ord("!") == 33 
    # ord("B") == 66
    # ord("!") + ord("!") == ord("B")
    hashtable = HashTable(1024)
    aa = hashtable.set("B", "B value")
    bb = hashtable.set("!!", "!! value")
    assert aa == bb == None
    expect = hashtable.get("B")
    actual = "B value"
    assert expect == actual

    expect = hashtable.get("!!")
    actual = "!! value"
    assert expect == actual

# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_retrieve_from_collision():
    # ord("!") == 33 
    # ord("B") == 66
    # ord("!") + ord("!") == ord("B")
    hashtable = HashTable(1024)
    hashtable.set("B", "B value")
    hashtable.set("!!", "!! value")
   
    expect = hashtable.get("B")
    actual = "B value"
    assert expect == actual

    expect = hashtable.get("!!")
    actual = "!! value"
    assert expect == actual

# Successfully hash a key to an in-range value
def test_hash_method():
    hashtable = HashTable(1024)

    number = hashtable._HashTable__hash("zzzzzzzzzzzzzzzzzzzzzz")
    assert number < 1024

@pytest.fixture
def hashtable():
    hashtable = HashTable(1024)
    hashtable.set("b", "b value")
    return hashtable