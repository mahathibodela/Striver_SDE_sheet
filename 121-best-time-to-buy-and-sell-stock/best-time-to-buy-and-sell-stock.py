class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        ans = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            ans = min(ans, prices[i])
            profit = max(profit, prices[i] - ans)
        
        return profit

        