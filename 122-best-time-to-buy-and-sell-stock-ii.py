"""
Solution: Just buy if you make a profit.
Price of today < price of tomorrow, add it to the profit

1. Set profit to 0
2. Iterate over len(prices)-1
3. If prices[i] < prices[i+1] (today's price lesser than tomorrow, we buy today and sell tomorrow)
profit = profit + prices[i+1] - prices[i]
4. Return profit
"""


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        length = len(prices)
        for i in range(length - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]

        return profit
