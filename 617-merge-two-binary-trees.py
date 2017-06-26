"""
Solution:
Similar to convert an array to a tree problem

1. If t1 and t2 are None, we can return None
2. t3 = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
3. Set t3.left = recurse(t1 and t1.left, t2 and t2.left) # Because, one tree might not have a left node but the other might.
4. Set t3.right = recurse(t1 and t1.right, t2 and t2.right) # Because, one tree might not have a right node but the other might.
5. return t3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None

        t3 = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        t3.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        t3.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)

        return t3
