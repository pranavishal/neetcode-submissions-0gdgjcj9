class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Let B be an array where B[i] represents the maximum you can profit if I own on day i
        # Let S be an array where S[i] represents the maximum you can profit if  don't own on day i
        # Base Case: B[0] = -prices[0], B[1] = max(-prices[0], -prices[1])
        # Base Case: S[0] = 0, S[1] = min(S[0], B[0] + prices[1])
        # general case: B[0] = min(S[i - 2] - prices[i], B[i - 1])
        # general case: S[i] = min(S[i - 1], B[i - 1] + prices[i])
        B = [0] * len(prices)
        S = [0] * len(prices)

        #base Case
        B[0] = -prices[0]
        S[0] = 0

        for i in range(1, len(prices)):
            if i == 1:
                B[i] = max(-prices[0], -prices[1])
                S[i] = max(B[i - 1] + prices[i], S[i - 1])
            
            else:
                B[i] = max(B[i - 1], S[i - 2] - prices[i])
                S[i] = max(B[i - 1] + prices[i], S[i - 1])

        
        return S[-1]