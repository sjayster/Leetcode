"""
Solutions: Inorder traversal will get the elements in increasing order. The kth element can be found from the list.

Recursion:

1. Helper function that populates the list from the tree using in order traversal.
2. Once the list is populated and the control returns to the main function,
return result[k-1]

Iterative:

1. Use the inorder traversal iterative method.
2. When current node is None and we pop the element from the stack, check to see if k-1 == 0, if so that is our kth smallest element
   else, decrement k by 1 and set current to current.right
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return

        stacks = []
        current = root
        while current or stacks:
            if current:
                stacks.append(current)
                current = current.left
            else:
                current = stacks.pop()
                if k - 1 == 0:
                    return current.val
                k -= 1
                current = current.right

    """
    def inorder(self, root, stacks):
        if not root:
            return
        self.inorder(root.left, stacks)
        stacks.append(root.val)
        self.inorder(root.right, stacks)
        return stacks
        
    def kthSmallest(self, root, k):
        stacks = []
        stacks = self.inorder(root, stacks=[])
        return stacks[k-1]
    """
