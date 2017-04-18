"""
Solution: Kadane's algorithm

The problem says if we are not making a profit, we need not make a transaction.
This is an example of the max sub-array problem = Kadane's algorithm

1. Have 2 variables, currsum = maxsum = 0
2. Set currsum to max of 0 and currsum - prices[i-1] + prices[i] (Buy then sell, hence i-1 followed by i)
3. Set maxsum to max of currsum and maxsum
4. Return maxsum

"""


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxsum = currsum = 0
        length = len(prices)
        for i in range(1, length):
            currsum = max(0, currsum + prices[i] - prices[i - 1])
            maxsum = max(currsum, maxsum)

        return maxsum
