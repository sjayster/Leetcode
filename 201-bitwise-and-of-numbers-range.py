"""
Solution:
The regular iterate over a range and "AND" the result timed out.

One thing I figured out was, if there was a range where there was a power of two involved, the result would always be zero.
example, m = 5 and n = 8 = 0101&1000 = 0 &(6 & 7) = 0

https://discuss.leetcode.com/topic/12133/bit-operation-solution-java

1. We will have to keep right shifting the bits until m != n
2. Keep track of a counter for every shift
3. If there is a pow of 2 involved, m and n will both be 0, if not m and n will be a power of 2 (001 or 010 or 100)
4. Left shift n by the counter times.
"""


class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        count = 0
        while m != n:
            m >>= 1
            n >>= 1
            count += 1

        n <<= count
        return n

        """
        result = n
        for i in xrange(m,n+1):
            result  &= i
            
        return result
        """
