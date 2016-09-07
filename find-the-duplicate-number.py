"""
Solutions that I could think of.
1. Using a dictionary to save the 1st occurrence of the number. If the num is seen again, return
2. Sort the array and then xor the index+1 with the number. (applicable only when all numbers between 1 to n are present and 1 number is missing. If the series is disjointed, this method would fail!)
Example: nums = [5,2,3,1,2,4]
nums.sort() -> [1,2,2,3,4,5]
if index+1 xor nums[i]!=0, return nums[i]
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Solution 1:
        """
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                return num
        
        """
        Solution 2:
        
        length = len(nums)
        nums.sort()
        for i in xrange(length):
            if (i+1) ^ nums[i] != 0:
                return nums[i]
        """