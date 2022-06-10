
# Singly Linked List
A singly linked list is a type of linked list that is unidirectional, that is, it can be traversed in only one direction from head to the last node

Each element in a linked list is called a node. A single node contains data and a pointer to the next node




## Challenge
The Challenge requirements is basic create a Singly linked list 

and node class to create node that will be added to the list 

then you should have insert method to let you insert node also you should have an includes method
that will check if the value you pass it inside the linked list or not 

last thing is the to string method it will print the linked list  with this forma  

`` "{ a } -> { b } -> { c } -> NULL" ``

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
while i using the OOP i always follow the DRY ( don't repeat yourself ) so that is my roll

for the complexity  the insert method was   O(1) 

for the includes method was O(n)

for the to_string and it was O(n)

and last one create_node O(1)

## API
<!-- Description of each method publicly available to your Linked List -->

### insert method 

it will insert a node  to the linked list at the first of it ( on the head of the list )

input => ``val`` the value you want insert it to the list 

process => insert node at the first on the list

output => it will return nothing 

### includes method 

it will search in the link list to find the value you pass to it

input => ``val`` the value you want to search if it in the list

process => searching in every node 

output => it will return boolean  True if it found else will return False


### to_string method 

it will print the link list from first node to the end

input => Nothing

process => loop through the list and  save the content to string 

output => it will return string of the list like this formula `` "{ a } -> { b } -> { c } -> NULL"  ``



