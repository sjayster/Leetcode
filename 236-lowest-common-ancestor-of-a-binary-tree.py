"""
Solution: 

1. If root = p or q or None, return root
2. See if either p or q is on left by setting l = recursion(root.left, p, q)
3. See if either p or q is on right by setting r = recursion(root.right, p, q)
4. If both l and r exists, then p and q are on different sub trees, return the root value
5. If only l or r is present, then both the nodes are on the same subtree, we can return the value of l or r.

example:
[[1], [2[4,5],3]]
if p and q are 2 and 3, then they will be in different sub trees and both l and r will have a value. Hence, we can return the root
if p and q are 2 and 4, they will be in the same subtree, hence either p or q (which ever comes first) will be the LCA
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p or root == q or root == None:
            return root

        isleft = self.lowestCommonAncestor(root.left, p, q)
        isright = self.lowestCommonAncestor(root.right, p, q)

        if isleft and isright:
            return root

        if isleft:
            return isleft
        else:
            return isright
