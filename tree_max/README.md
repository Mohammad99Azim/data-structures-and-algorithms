# Challenge Summary
<!-- Description of the challenge -->
i have a tree ( Binary Tree ) and i have to return the max value 

## Whiteboard Process
<!-- Embedded whiteboard image -->
![max_tree](../images/max_tree.jpg)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

time : it will be O(n) because it will loop through all the nodes
space : it will be O(n) because we made an array in the pre_order method

## Solution
<!-- Show how to run your code, and examples of it in action -->
```

    def max_value(self):
        if self.pre_order() is None:
            raise Exception("The Tree Is Empty !!!")
        return max(self.pre_order())


    def pre_order(self, root=None, arr=[]):
        if self.root is None:
            return None
        if root is None:
            root = self.root
        arr.append(root.val)
        if root.right:
            self.pre_order(root.right)
        if root.left:
            self.pre_order(root.left)
        return arr

```