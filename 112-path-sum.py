"""
Solution:

We need to have an addition var that tracks the sum at every level.
1. If not root, return False
2. Set currsum = sum - root.val
3. If a node is the leaf node and sum==0, we have a path that adds up to the sum. return True
4. Else, return recurse over left with root.left or currsum and root.right, currsum
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        currsum = sum - root.val
        if currsum == 0 and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, currsum) or self.hasPathSum(root.right, currsum)
