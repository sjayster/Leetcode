"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.


Solution: 
Swap the matching element with the last element of the array and decrement the length 

1. Get the length of the array.
2. While i < length of the array,
    compare the element with the value, if it matches, move the last element to the current position and decrement the counter
    if the element does not match with the value, increment i
    
Other solutions - Added as a comment:
Found this really simple solution in the discuss page.
https://discuss.leetcode.com/topic/23988/my-python-solution
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                nums[i] = nums[length-1]
                length -= 1
            
            else: #if nums[i] != val:
                i += 1
            
        return length
        
        """
        while val in nums:
            nums.remove(val)
        
        return len(nums)
        """
