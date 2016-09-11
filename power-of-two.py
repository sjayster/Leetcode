"""
Given an integer, write a function to determine if it is a power of two.

Power of 2: Bit manipulation
    if x and (x-1) == 0, then x is a power of 2 (except when x == 0).
    example: x = 8
    8 & 7 = 1000 & 0111 = 0
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return n & (n-1) == 0