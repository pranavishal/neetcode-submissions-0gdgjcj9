class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_min = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - curr_min)
            curr_min = min(curr_min, prices[i])
            
        return profit
