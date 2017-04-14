"""
NOTE: Return False if duplicate elements are present.

Solution 1: Inorder traversal without needing to traverse the array after populating it

1. Have a prev node set to None to start with
2. Similar to the kth smallest element, if current node is None, 
    current = stack.pop()
    if prev is not None and current.val <= prev.val -> previous node is greater than the current node => return False
    else, set prev to current and current = current.right
3. Finally return True, as all the elements are in ascending order

Solution 2: Inorder traversal and then compare the elements in the array.

If it is a BST, we know that inorder traversal would return the elements in an increasing order.
Once we populate the list, we can compare to see if array[i-1] < array[i], if not, return False

Solution 3:
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
    # Solution 1

    def isValidBST(self, root):
        if not root:
            return True
        stacks = []
        current, prev = root, None
        while current or stacks:
            if current:
                stacks.append(current)
                current = current.left
            else:
                current = stacks.pop()
                if prev != None and current.val <= prev.val:
                    return False
                prev = current
                current = current.right
        return True

    """
    # Solution 2:
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
    """
    # Solution 3:
    def helper(self, root, lowerbound, upperbound):
        if not root:
            return True
        
        if root.val <= lowerbound or root.val >= upperbound:
            return False
        
        return self.helper(root.left, lowerbound, root.val) and self.helper(root.right, root.val, upperbound)
    
    def isValidBST(self, root):
        if not root:
            return True
        lowerbound = -(sys.maxint-1)
        upperbound = sys.maxint
        return self.helper(root, lowerbound, upperbound)
    """
