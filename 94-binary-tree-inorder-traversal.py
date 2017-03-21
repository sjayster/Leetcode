"""
Solutions:

Recursive -
1. Function should have root, result=[]. Since it is predefined here, we will just call a helper function that does the recursion
2. if root is not None, recurse(left), add result, recurse(right)

Iterative - Using a stack
1. Have 2 arrays - result and stack
2. Assign root to current
3. If stack or current is not None, there are 2 conditions,
   a. if current is not none,
      add it to stack
      set current to current.left
   b. if current is none,
      pop the stack and set current to the popped element
      add the popped current.val to the result
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

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Iterative

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        current = root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.val)
                current = current.right
        return result

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive:
class Solution(object):
    def inorderTraversal(self, root):
        result = self.recursive(root, result = [])
        return result
        
    def recursive(self, root, result):
        if not root:
            return []
        
        if root.left:
            self.recursive(root.left, result)
        result.append(root.val)
        if root.right:
            self.recursive(root.right, result)
            
        return result
"""
