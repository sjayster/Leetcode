"""
Recursion:
1. If the node is None, return (base condition)
2. Keep recursing left and right until the nodes are None. 
3. Once the base condition is hit and the recursion unwinds, we will have to swap the left and the right child and return the current node.
4. By doing this, at each recursion we are swapping the sub tree and finally when we hit the root node, we swap its children thereby inverting the tree.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
