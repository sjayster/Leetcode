"""
Recursion:
Thought of it in basic terms. Both the value and the structure of the tree must be similar.
1. If the roots of both p and q are None, return True
2. Check if either both p and q exists or both does not exist. If only p exists and q doesn't then return False. The structure does not match.
3. Once we know the above conditions are True, we check the value of the node. If not equal return False
4. Finally, return function(p.left,q.left) and function(p.right, q.right)

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p and not q:
            return False
        if not p and q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
