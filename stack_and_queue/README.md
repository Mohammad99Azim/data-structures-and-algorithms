# Stacks and Queues
<!-- Short summary or background information -->
Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle.

Queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.
## Challenge
<!-- Description of the challenge -->
Make a Stack and Queue and make there methods to add node, check if empty  and peek and pop to remove node

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
i have some struct with building stack or queue and i have to follow them to get the type of data structure i'm trying to build  

all the methods was  O(1) for both  Space and Time complexity  for the __str__  was the O(n) for time because of the loop

## API

### Stack 



- push
  - Arguments: value
  - adds a new node with that value to the top of the stack with an O(1) Time performance.




- pop
  - Arguments: none
  - Returns: the value from node from the top of the stack
  - Removes the node from the top of the stack
  - Should raise exception when called on empty stack



- peek
  - Arguments: none
  - Returns: Value of the node located at the top of the stack
  - Should raise exception when called on empty stack



    
- is empty
  - Arguments: none
  - Returns: Boolean indicating whether or not the stack is empty.


### Queue





- enqueue
  - Arguments: value
  - adds a new node with that value to the back of the queue with an O(1) Time performance.





- dequeue
  - Arguments: none
  - Returns: the value from node from the front of the queue
  - Removes the node from the front of the queue
  - Should raise exception when called on empty queue





- peek
  - Arguments: none
  - Returns: Value of the node located at the front of the queue
  - Should raise exception when called on empty stack





- is empty
  - Arguments: none
  - Returns: Boolean indicating whether or not the queue is empty






