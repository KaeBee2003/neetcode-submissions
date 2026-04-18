class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxv = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                if prices[j] - prices[i] > maxv:
                    maxv = prices[j] - prices[i]
        return maxv
