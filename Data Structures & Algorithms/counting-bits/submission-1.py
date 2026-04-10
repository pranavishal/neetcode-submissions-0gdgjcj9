class Solution:
    def countBits(self, n: int) -> List[int]:
        # we take a dynamic programming approach to this question
        # let dp[i] represent the amount of set bits in integer i
        # dp[i] = 1 + dp[i - offset]
        # this is because whenever we hit a power of 2, we repeat the amount of bits
        # offset before with an extra bit at the beginning (the added digit)
        dp = [0] * (n + 1)
        dp[0] = 0
        offset = 1

        for i in range(1, n + 1):
            if i == 2 * offset:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp
        