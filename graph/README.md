# Graphs
<!-- Short summary or background information -->
#### Graphs:

 in data structures are non-linear data structures made up of a finite number of nodes or vertices and the edges that connect them. Graphs in data structures are used to address real-world problems in which it represents the problem area as a network like telephone networks, circuit networks, and social networks.

## Challenge
<!-- Description of the challenge -->
Implement a Graph. The graph should be represented as an adjacency list

and this is the method you should make 

- add node

- add edge

- get nodes

- get neighbors

- size

also you need to make a Vertex class, and Edge class 

in the end you should test all method you wrote 

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Single Responsibility each method do only one thing 

and graph was represented as an adjacency list that will give less space complexity but more time complexity

Space: for adjacency list it will take  O(n) for the space (when you trying to check if two vertexes are neighbors)

Time: adjacency list it will take O(n) for time complexity  (when you trying to check if two vertexes are neighbors)

- add node  Time:O(1)  Space:O(1)

- add edge  Time:O(1)  Space:O(1)

- get nodes Time:O(n)  Space:O(n) **from the built in function key** [Python-TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

- get neighbors Time:O(1)  Space:O(n) the space because if we have N of neighbors

- size  Time:O(1)  Space:O(1) the built in function len() is O(1) [complexity-of-len](https://blog.finxter.com/python-list-length-whats-the-runtime-complexity-of-len/) 

- breadth_first:  Time:O(n^2)  Space: O(n)  worst case when the graph is complete graph


## API
<!-- Description of each method publicly available in your Graph -->

- add node: Add the node to __graph_list as key and value it will be an empty list.

- add edge: if the vertexes are valid will make two instances from Edge class then it will add start_vertex as neighbor for the end_vertex and vice versa.

- get nodes: it will return a list of all keys in the graph

- get neighbors: will return all the neighbors (have common edge) with the vertex you will pass to it as an argument

- size: return the number of vertexes you have in the graph

- breadth_first: it will iterate through the graph then return  all the values in he vertexes  