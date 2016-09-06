"""
Asked in Amazon
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