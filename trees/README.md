# Trees
<!-- Short summary or background information -->
A tree is a nonlinear hierarchical data structure that consists of nodes connected by edges.
## Challenge
<!-- Description of the challenge -->
we have to make a tree and make the pre-in-post order traversal then 
make another  class called Binary_Search_Tree and in it  should make an add method that will add a Node
to the right place in the tree 

also  should make a method called contain it will search in the tree based on the Binary search rule  

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
for all traversal methods ( pre - in - post ,order) the time was O(n) and the Space was O(1)


for the add it will be for time  O(log n) because the every round of loop the values will be the half and for Space
it will be O(1) Just add one value

for the contains it will be for time  O(log n) because the every round of loop the values will be the half and for Space
it will be O(1) because there is no space will add

## API
<!-- Description of each method publicly available in each of your trees -->

 - pre_order: it will go throw the tree to get all the nodes in it and it will move based on this rule : ``root >> left >> right``
 - in_order:  it will go throw the tree to get all the nodes in it and it will move based on this rule : ``left >> root >> right``
 - post_order:  it will go throw the tree to get all the nodes in it and it will move based on this rule : ``left >> root >> right`` and it will return an array of the nodes


 - add: it will go to the root then if it more or equal the value argument cur will go to right else will go to left until cur right or left is none  Node have the value will be added there
 - contains: it will go to the root then if it more or equal the value argument cur will return true  else will check if it more will go to the right of the tree else it will go to left until the cur value be equal to the value argument
    
