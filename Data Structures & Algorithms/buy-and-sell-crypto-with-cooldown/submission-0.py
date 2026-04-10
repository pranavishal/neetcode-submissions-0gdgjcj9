class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we take a DP approach
        # let buy[i] be the maximum profit obtained at end of day i if I'm holding a neetcoin
        # let sell[i] be the maximum profit obtained at end of day i if I'm not holding a neetcoin

        # base case:
        # buy[0] = -prices[0] 
        # sell[0] = 0 (don't buy, can't sell anything since you never had anything to begin with)

        # buy[1] = max(-prices[0], -prices[1])
        # sell[1] = max(0, buy[0] + prices[1])

        # general case:
        # buy[i] = max(sell[i-2] - prices[i], buy[i-1]) since you can't buy today if you sold yesterday
        # sell[i] = max(buy[i - 1] + sell[i], sell[i - 1])

        buy = [0] * len(prices)
        sell = [0] * len(prices)
        
        buy[0] = -prices[0]
        sell[0] = 0

        if len(prices) == 1:
            return 0

        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(0, buy[0] + prices[1])

        for i in range(2, len(prices)):
            buy[i] = max(sell[i-2] + -prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
        
        return sell[len(prices) - 1]