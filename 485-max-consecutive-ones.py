"""
Solution:

1. Have 2 variables - start and final
2. Iterate over the list. If 1 is found, increment start
3. Set final to max(start, final)
4. If 0 is seen, reset start to 0

"""


class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = final = 0
        for i in nums:
            if i == 1:
                start += 1
                final = max(start, final)
            else:
                start = 0
        return final
