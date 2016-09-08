"""
Loop over the index
Have a count variable that increments when a 0 is encountered.
Once a non-zero number is seen and if count > 0, replace nums[index-count] with nums[index] and nums[index] with 0. Essentially swapping.
eg: 1,0,2,3,0
In second iteration, count will be 1. 
In the third iteration (index =2), nums[2-count] = nums[2] -> 1,2,2
nums[2] = 0 --> 1,2,0
4th iteration -> nums[3-count] = nums[3] -> 1,2,3,3
nums[3] = 0 -> 1,2,3,0

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for i in xrange(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            elif nums[i] != 0 and zero_count:
                nums[i-zero_count] = nums[i]
                nums[i] = 0
            else:
                continue