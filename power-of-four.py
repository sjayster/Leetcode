"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Same as power of 3
Power of 4 numbers would always have a reminder of one. Keep doing that over a loop while n > 1 and n/=4
Finally, if n == 1 return True, else False
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0:
            while num % 4 == 0:
                num /=4
        
        return num == 1