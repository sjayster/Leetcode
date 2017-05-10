"""
Solution:
1. If root is None, return True
2. Use a helper function to pass the left and right child as separate trees. helper(root.left, root.right)
3. In the helper, if left and right are None, return true
4. If one is None and the other is not, return False
5. If left.val != right.val, return False
6. Recurse over the helper by checking left.left and right.right and left.right and right.left
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def helper(self, leftroot, rightroot):
        if not leftroot and not rightroot:
            return True
        if (not leftroot and rightroot) or (leftroot and not rightroot):
            return False

        if rightroot.val != leftroot.val:
            return False

        return self.helper(leftroot.left, rightroot.right) and self.helper(leftroot.right, rightroot.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.helper(root.left, root.right)
