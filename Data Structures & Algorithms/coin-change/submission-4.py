class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Let A[i][j] represent the fewest amount of coins needed to make up the exact target
        # using up to and including the first i coin denominations, with target j
        # General Case: A[i][j] = min(A[i - 1][j], 1 + A[i][j - value[i]])
        # Base Case: if i == 1, A[i][j] = j / value[i] if j % i == 0 else float('inf')
        # Base Case: A[i][j] = 0 if j = 0

        A = [[float('inf') for _ in range(amount + 1)] for _ in range(len(coins))]
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == 0 and j % coins[i] == 0:
                    A[i][j] = int(j / coins[i])

                if j == 0:
                    A[i][j] = 0
        
        
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                if coins[i] > j:
                    A[i][j] = A[i - 1][j]
                else:
                    A[i][j] = min(A[i - 1][j], 1 + A[i][j - coins[i]])

        if A[-1][-1] == float('inf'):
            return -1
        
        return A[-1][-1]