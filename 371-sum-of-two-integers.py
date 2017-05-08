"""
Solution:
No clue on how to use bit manipulation to solve this.
https://discuss.leetcode.com/topic/51999/python-solution-with-no-completely-bit-manipulation-guaranteed
"""


class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mini = 0x7FFFFFFF
        maxi = 0X80000000
        mask = 0xFFFFFFFF

        while b:
            a, b = (a ^ b) & mask, (a & b) << 1 & mask

        if a <= maxi:
            return a

        return ~(a ^ mask)
