"""
Solution:
a. Dynamic programming:
1. Have an array filled with 1 from 0 to n+1
2. Iterate over range 2 to n+1, set res[i] = res[i-1] + res[i-2] (we can either climb 1 stair at a time or 2 stairs at a time)
Hence, i-1 is a possibility and so is i-2
3. return res[n] once the loop breaks

b. Simpler solution
1. If n < 2, return 1
2. Iterate over range 2, to n, set a to b and b to a+b
3. return b
"""


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1] * (n + 1)
        for i in range(2, n + 1):
            res[i] = res[i - 1] + res[i - 2]

        return res[n]

        # Solution 2:
        """
        if n < 2:
            return 1
        
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, a+b
            
        return b
        """
