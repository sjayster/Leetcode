"""
Solution: Recursion

Since the array is sorted, we know the mid element is going to be the root.
1. Base: If not nums, return None
2. Get the mid element, len(nums)/2
3. Create the root node, TreeNode(nums[mid])
4. root.left = recursion of left sub tree => nums[:mid]
5. root.right = recursion of right sub tree => nums[mid+1:]
6. return root
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
