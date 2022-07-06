# Challenge Summary
<!-- Description of the challenge -->
need make a function return a list with all node values in tree have breadth first order

## Whiteboard Process
<!-- Embedded whiteboard image -->
![breadth_first](../images/breadth_first.jpg)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
space : O(n) because i have a list save the current level nodes
time : O(n) beause of the  while loop will loop for each node in the tree

## Solution
<!-- Show how to run your code, and examples of it in action -->
```
def tree_breadth_first(tree):
    if tree.root is None:
        raise Exception("The Tree Is Empty !!!")
    root = tree.root
    queue = []
    results = []
    queue.append(root)
    while queue:
        if queue[0].left:
            queue.append(queue[0].left)

        if queue[0].right:
            queue.append(queue[0].right)

        results.append(queue[0].val)
        queue.pop(0)
    return results

```
