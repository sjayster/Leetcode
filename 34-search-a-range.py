"""
Binary search:
Same logic as finding the occurrence but with a twist
1. Call the binary search function twice, once for 1st and once for last occurrence and save the result in first and last variable
2. Return [first, last]

First
1. First occurrence, if the mid element is >= target, set end to mid-1, else set start to mid + 1
2. Have a final if condition, if mid element == target, save it in a index variable
3. Once the loop breaks, return the index variable

Last
1. Last occurrence, if the mid element is <= target, set start to mid + 1 else end to mid-1
2. Have a final if condition, if mid element == target, save it in a index variable
3. Once the loop breaks, return the index variable

"""


class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = self.findfirst(nums, target)
        end = self.findlast(nums, target)
        return [first, end]

    def findfirst(self, nums, target):
        start, end = 0, len(nums) - 1
        ix = -1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
            if nums[mid] == target:
                ix = mid
        return ix

    def findlast(self, nums, target):
        start, end = 0, len(nums) - 1
        ix = -1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
            if nums[mid] == target:
                ix = mid
        return ix
