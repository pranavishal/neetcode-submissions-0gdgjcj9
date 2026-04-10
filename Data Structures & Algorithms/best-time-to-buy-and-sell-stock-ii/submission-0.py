class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float('inf')
        prof = 0
        for i in range(len(prices)):
            curr_min = min(curr_min, prices[i])
            if prices[i] > curr_min:
                prof += prices[i] - curr_min
                curr_min = prices[i]
        
        return prof
        