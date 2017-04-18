"""
Solution: Kadane's algorithm
Note: negative numbers are in place. So set maxsum to -inf to start with

1. Have 2 variables, currsum = 0 and maxsum = -sys.maxint
2. Set currsum to max of nums[i] and currsum + nums[i]
currsum = max(nums[i], currsum+nums[i]) - as the entire series could be negative. in that case, we need to return the lowest negative number in the list. Hence, we cannot get the max of 0 and currsum+nums[i]
3. Set maxsum to max of currsum and maxsum
4. Return maxsum

"""


class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currsum = 0
        maxsum = inf = -sys.maxint
        length = len(nums)
        for i in range(length):
            currsum = max(nums[i], currsum + nums[i])
            maxsum = max(maxsum, currsum)

        return maxsum
