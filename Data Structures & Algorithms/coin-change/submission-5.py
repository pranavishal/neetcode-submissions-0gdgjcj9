class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Let A[i][j] represent the minimum amount of coins to represent target j using
        # up to the first ith coin denominations (0 indexed)
        # base case: if i == 0, A[i][j] = j // coins[i] if j % coins[i] == 0 else float('inf)
        # A[i][j] = 0 if j == 0
        # General Case: A[i][j] = A[i - 1][j] if coins[i] > j
        # General Case: A[i][j] = min(A[i - 1][j], 1 + A[i][j - coins[i]])
        # return A[-1][-1] if not float('inf') else return -1

        A = [[float('inf') for _ in range(amount + 1)] for _ in range(len(coins))]
        print(A)
        
        #base case
        for j in range(len(A[0])):
            if j % coins[0] == 0:
                A[0][j] = j // coins[0]
        
        for i in range(1, len(A)):
            for j in range(len(A[i])):
                if coins[i] > j:
                    A[i][j] = A[i - 1][j]
                else:
                    A[i][j] = min(A[i - 1][j], 1 + A[i][j - coins[i]])
        
        if A[-1][-1] == float('inf'):
            return -1
        return A[-1][-1]
            
        