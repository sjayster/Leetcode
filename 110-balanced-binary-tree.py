"""
Recursion: Calculate height of left tree and right tree and see if the difference is <= 1

Careful: We need to see if the subtrees are balanced too.
example:
1-2-3-4-null-null-5-6-null-null-7 -> the height of the main tree is good but the subtree is not balanced.

1. If the tree is empty, return True
2. Get the height of the left tree (root.left)
3. Get the height of the right tree (root.right)
4. return abs(left_height - right_height) <= 1 and recurse over the left and right subtrees to see if it is balanced too

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        leftheight = self.height(root.left)
        rightheight = self.height(root.right)

        return abs(leftheight - rightheight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
