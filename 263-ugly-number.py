"""
Solution:
It has been mentioned that ugly numbers are positive and are divisible only by 2,3 and 5
1. Base condition, if num is <= 0 return False
2. After trying out a series of numbers, we got to know that ugly numbers become 1 after continuously dividing it by 2,3 or 5.
3. When 2,3 and 5 are the divisors, if number % div == 0, keep reducing num by num/div
4. If it is an ugly number, it will become 1 after this process.
"""


class Solution(object):

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for div in [2, 3, 5]:
            while num % div == 0:
                num = num / div

        return num == 1
