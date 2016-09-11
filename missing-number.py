"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

2 solutions:

1. Sum of length * length+1 /2 - sum(array) 
2. Xor the index with the corresponding number. All the numbers except the missing one will get cancelled out.
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Method 2:
        mask = 0
        for i in xrange(len(nums)):
            mask = mask ^ (i+1) ^ nums[i]
        
        return mask
        """
        
        # Method 1:
        length = len(nums)
        return (length*(length+1)/2) - sum(nums)