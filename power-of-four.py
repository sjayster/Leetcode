"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Same as power of 3
Power of 4 numbers would always have a reminder of one. Keep doing that over a loop while n > 1 and n/=4
Finally, if n == 1 return True, else False

Solution 2:

1. 0xAA equates to 10101010 in binary. Meaning, all the even bits are set to 1
   For 32 bits we need 8 As.
2. num & num-1 == 0 is also true for pow of 2
3. But powers of 4 are 1, 10000, 1000000, 100000000
4. As we can see, for every pow of 4, the MSB is 1 and that MSB is in the odd position
5. Upon & with a mask that has 1 in odd positions, we should get 0.
"""


class Solution(object):

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0:
            while num % 4 == 0:
                num /= 4

        return num == 1

    """
    def isPowerOfFour(self, num):
        mask = 0xAAAAAAAA
        if num > 0 and num &(num-1) == 0 and num&mask == 0:
            return True
        return False
    """
