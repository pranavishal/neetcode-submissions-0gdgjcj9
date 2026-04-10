class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Let A[i][j] represent the number of distinct combinations that sum to j using up to and including
        # the ith coin denomination
        # General Case: A[i][j] = A[i - 1][j] (using none of coin i) + A[i][j - coins[i]] (using at least 1 of
        # coin i)

        # Base Case: A[i][j] == 1 for i == 0 and j % coins[i] == 0, else 0
        # Base Case: A[i][j] == 1 if j == 0
        
        A = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]
        
        # Base Case
        for i in range(len(A[0])):
            if i % coins[0] == 0:
                A[0][i] = 1
            else:
                A[0][i] = 0
        
        # if amount == 0, number of combinations is 1 (no coins)
        for i in range(len(A)):
            A[i][0] = 1
        
        
        for i in range(1, len(A)):
            for j in range(1, len(A[i])):
                A[i][j] = A[i - 1][j]

                if j >= coins[i]:
                    A[i][j] += A[i][j - coins[i]]
        
        return A[-1][-1]
        