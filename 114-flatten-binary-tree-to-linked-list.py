"""
Solution: Get the right element before the left
Iterative:
1. Define an stack with the root element
2. While stack is not empty, pop the element and save it to tmp
3. If tmp.right, then add it to the stack
4. If tmp.left, add it to the stack. For the above example, the stack will look like this [1,5,2], where tmp is 1
5. We need to set tmp.right as 2 and tmp.left as None. tmp.right stack[-1] (if stack is not empty) and tmp.left = None

Recursive:
1. Set a class variable prev = None
2. If not root, return
3. Recurse over root.right
4. recurse over root.left
5. Once the base condition is hit, set root.left to None and root.right to prev
For the above example, the recursion will be 1 -> rec(5) -> rec(6) -> rec(None)
Here we set 6.right as None (which is our prev) and 6.left is None
7. Set self.prev to root
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    prev = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # Recursive
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root

    """
    # Iterative
    
    def flatten(self, root):
        if not root:
            return None
        stack = [root]
        while stack:
            tmp = stack.pop()
            if tmp:
                if tmp.right:
                    stack.append(tmp.right)
                if tmp.left:
                    stack.append(tmp.left)
                if stack:
                    tmp.right = stack[-1]
                tmp.left = None
    """
