"""
Power of 3 numbers would always have a reminder of one. Keep doing that over a loop while n > 1
Finally, if n == 1 then return True, else False
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 1:
            while n%3 == 0:
                n /= 3
        return n == 1