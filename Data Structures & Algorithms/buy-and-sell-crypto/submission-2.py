class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            curr_min = min(curr_min, prices[i])
            profit = max(profit, prices[i] - curr_min)
        
        return profit
        