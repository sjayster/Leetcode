"""
Solution:

Regular inorder traversal but add a filler variable

1. Call the helper function by passing the root, filler = "", res = []
2. In the helper, if the node is the leaf node, add filler + root.val to the result[]
3. If there is a left node, recurse over (root.left, filler = filler + str(root.val) + "->", res), as this could be an intermediate node
4. If there is a right node, recurse over (root.right, filler = filler + str(root.val) + "->", res), as this could be an intermediate node
5. Return result
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def helper(self, root, filler, res):
        if not root.left and not root.right:
            res.append(filler + str(root.val))
        if root.left:
            self.helper(root.left, filler + str(root.val) + '->', res)
        if root.right:
            self.helper(root.right, filler + str(root.val) + '->',  res)
        return res

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        res = self.helper(root, '', res)
        return res
