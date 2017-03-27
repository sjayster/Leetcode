"""
NOTE: Return False if duplicate elements are present.

Solution: Inorder traversal and then compare the elements in the array.

If it is a BST, we know that inorder traversal would return the elements in an increasing order.
Once we populate the list, we can compare to see if array[i-1] < array[i], if not, return False

Solution 2:
Recursion, without extra space.
We need to have an upper bound and lowerbound -> (-/+) sys.maxint
We use a helper function in this case, helper takes root, lowerbound, upperbound

1. The main function calls helper with root, -maxint and maxint as the boundaries
2. If root is None, return True
3. If root.val <= lowerbound or root.val > upperbound, we know the BST condition has been violated

If there is a left child, we set the upperbound to the current root, as the left child will be lesser than current but greater than -intmax.
If there is a right child, we set the lowerbound to the current root, as the right child will be greater than current, but lesser than intmax.

4. return helper(root.left, lowerbound, upperbound = root.val) and helper(root.right, lowerbound = root.val, upperbound)

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def helper(self, root, lowerbound, upperbound):
        if not root:
            return True

        if root.val <= lowerbound or root.val >= upperbound:
            return False

        return self.helper(root.left, lowerbound, root.val) and self.helper(root.right, root.val, upperbound)

    def isValidBST(self, root):
        if not root:
            return True
        lowerbound = -(sys.maxint - 1)
        upperbound = sys.maxint
        return self.helper(root, lowerbound, upperbound)

    """
    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right, result)
        
    def isValidBST(self, root):
        #:type root: TreeNode
        #:rtype: bool
        result = []
        self.inorder(root, result)
        for i in range(1,len(result)):
            if result[i-1] >= result[i]:
                return False
        return True
    """
