"""
Recursion:
1. If the node is empty, return 0. Empty tree = 0 (base condition)
2. If only the node is present and it has no left or right, we return 1.
3. With that logic, we get the maxDepth of left child and maxDepth of right child and add 1 to it.
4. But, there is a possibility that one side of the tree could be longer than the other, so we get the max of left or right and add 1 to it.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
