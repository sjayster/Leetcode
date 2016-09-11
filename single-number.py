"""
Given an array of integers, every element appears twice except for one. Find that single one.

Solution:
xor all the numbers in the list. The dups cancel each other out and whatever remains is the answer
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]
        
        return result