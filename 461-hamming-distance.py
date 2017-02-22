"""
Solution:

Took a shot in the dark.

1. Calculate the xor of the two numbers - The number of ones in that will give us the hamming distance between the 2 numbers
2. Use the procedure to get the number of 1s in a number - x&(x-1) until 0

"""


class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        distance = 0
        while xor != 0:
            distance += 1
            xor = (xor) & (xor - 1)

        return distance
