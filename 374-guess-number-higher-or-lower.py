"""
Binary search: Similar to find the 1st occurrence of a number
1. Set start to 0 and end to n-1
2. While start<=end, Get the mid point and see if it is a bad version
3. If guess(m) is 1, set start to m+1, 
4. Else if guess(m) is -1, set end to m-1
5. Else return m
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, e = 1, n
        while s <= e:
            m = (s + e) / 2
            if guess(m) == -1:
                e = m - 1
            elif guess(m) == 1:
                s = m + 1
            else:
                return m
