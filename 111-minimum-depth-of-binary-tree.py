"""
Solution:
Took a while to get a hang of it.

We need to return the number of nodes in the shortest part of the tree. So, if the depth of the tree is 3 on one side and 2 on the other, we need to return 2
[1,2,3,4,5,6,7] will return 3
[1,2,3,4,5,6] will also return 3, as left and right subtree heights are the same
[1,2,3,4,5] will return 2, as the left tree has 3 nodes but the right has only 2
[1,2,3,4] will return 2, as the left tree has 3 nodes (including root) but the right has only 2

There are the following 5 cases that need to be addressed
1. If the node is empty, return 0. Empty tree = 0
2. If the node is the leaf node, return 1
3. There are 2 cases where,
   a. Node has a left node but no right node -> return recurse(left) + 1
   b. Node has a right node but no left node -> return recurse(right) + 1
   
4. Kick off the recursion by calling return the min of f(left), f(right) + 1

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        if not root.left and root.right:
            return self.minDepth(root.right) + 1

        if not root.right and root.left:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
