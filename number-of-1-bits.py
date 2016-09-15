"""
Bit manipulation

If we & num with num-1, it will take number of 1's in a num times before it reaches 0
Example: num = 15 = 1111, count = 0
while num != 0: num & (num-1); count += 1
1111 & 1110 = 1110 count -> 1
1110 & 1101 = 1100 count -> 2
1100 & 1011 = 1000 count -> 3
1000 & 0111 = 0    count -> 4

It takes 4 steps (number of 1's in the number) for num to reach 0
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        
        return count