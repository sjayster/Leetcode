"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Iterate over list and add the elements to the dictionary with the index as the value.
Iterate over the list again and see if an element (target - nums[index]) exists in the dictionary.
See if the value is less (or greater) than the current index (to avoid duplication, like [1,3,3,3])
Append it to a list.

Update: Reduced the traversal from 2 to 1. 

"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        length = len(nums)
        for i in range(length):
            if (target - nums[i]) in d:
                return d[target-nums[i]], i
            d[nums[i]] = i