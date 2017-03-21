"""
Solutions:

Recursive -
1. Function should have root, result=[]. Since it is predefined here, we will just call a helper function that does the recursion
2. if root is not None, add root.val to result, recurse(left), recurse(right)
3. return result

Iterative - Using a stack
1. Have 2 arrays - result and stack
2. Assign root to current
3. If stack or current is not None, there are 2 conditions,
   a. if current is not none,
      add currnt to stack and current.val to result
      set current to current.left
   b. if current is none,
      pop the stack and set current to the popped element
      set current to current.right
      
Learned about Morris solution from Geeksforgeeks.com
http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def helper(self, root, result):
        if not root:
            return []
        if root:
            result.append(root.val)
            if root.left:
                self.helper(root.left, result)
            if root.right:
                self.helper(root.right, result)

        return result

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = self.helper(root, result=[])
        return result

    """
    # Iterative
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = []
        result = []
        current = root
        while stack or current:
            if current:
                stack.append(current)
                result.append(current.val)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return result
    """
