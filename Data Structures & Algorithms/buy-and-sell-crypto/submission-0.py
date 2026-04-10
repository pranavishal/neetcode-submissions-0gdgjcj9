class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minValue = float('inf')
        
        for i in range(len(prices)):
            if prices[i] < minValue:
                minValue = prices[i]
            
            if prices[i] - minValue > maxProfit:
                maxProfit = prices[i] - minValue
        
        return maxProfit
        