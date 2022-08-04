# Hashtables
<!-- Short summary or background information -->

Hash Table is a data structure which stores data in an associative manner. In a hash table, data is stored in an array format, where each data value has its own unique index value. Access of data becomes very fast if we know the index of the desired data.


## Challenge
<!-- Description of the challenge -->
Implement a Hashtable Class using these methods 

- set
- get
- contains
- keys
- hash

and add testing  for them 


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

understand how hash table data structure works then start implementing and i follow this approach to get less complexity in searching


### Big(O) for searching:  get() method

Time O(n)

Space O(1)

### Big(O) for insertion:  set() method

Time O(1)

Space O(1)



## API
<!-- Description of each method publicly available in each of your hashtable -->

1- set : this method will  hash the key and set the value and key pair in the buckets,
      also handling the collisions as needed
      Return: Nothing
      Arguments: Key , value 


2- get : Used to find the value that is associated with the passed key.
    param key: Hash key
    retern: referenced value by passed key


3- contains: This method will take a key
    returns : True if the key exists in the hashmap, and False if it doesn't exist

4- keys: this method will return a collections of all the keys in hashmap as an object 


5- hash: This method will take a key as an argument and returns 
    the index in the collection of buckets for that key.