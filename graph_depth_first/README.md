# Depth First Traversal
<!-- Short summary or background information -->
Depth first Traversal have three types

- in-order: (Left, Root, Right)  
 
- post-order: (Left, Right, Root)
 
- pre-order : (Root, Left, Right)

## Challenge
<!-- Description of the challenge -->
you have graph and you should make method  return A collection of nodes in their pre-order depth-first traversal order

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
as it required i tack the pre-order approach root,left,right 


## Solution
<!-- Embedded whiteboard image -->
![pre-order](../images/graph_depth_first.jpg)



## Code 

```

    def depth_first(self,root):
        visited = []
        
        def _walk(root):
            visited.append(root.value)
            for x in self.get_neighbors(root):
                if x.vertex.value not in visited:
                    _walk(x.vertex)
        _walk(root)          
        return visited

```