"""
Solution: Level order traversal

1. Append root to parent. While parent is not empty
2. For node in parent, append the val to the result list as a nested list
3. Set t = [] and for node in parent if node has left or right, add it to the t list
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

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        p, r = [root], []
        while p:
            r.append([n.val for n in p])
            t = []
            for n in p:
                if n.left:
                    t.append(n.left)
                if n.right:
                    t.append(n.right)

            p = t

        return r[::-1]
