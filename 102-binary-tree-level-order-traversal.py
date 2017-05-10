"""
Solution: Level order traversal

1. Append root to parent. While parent is not empty
2. For node in parent, append the val to the result list as a nested list
3. Set t = [] and if root has left or right, add it to the t list
4. Set parent = t
5. Once the loop breaks, return result
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        parent = [root]
        result = []
        while parent:
            result.append([node.val for node in parent])
            t = []
            for node in parent:
                if node.left:
                    t.append(node.left)
                if node.right:
                    t.append(node.right)
            parent = t

        return result
