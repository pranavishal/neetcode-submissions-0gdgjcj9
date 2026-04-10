class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Let A[i][j] represent the minimum amount of coins needed to reach target j with the first
        # i denominations
        # General Case: A[i][j] = min(a + (j - coins[i]*a)) for 0 <= a <= j // coins[i]
        # Base Case: A[i][j] = j / coins[i] for i == 0 and j % coins[i] == 0, else float('inf')
        # Base Case: 0 if j == 0
        # Keep track of J[i][j] to see how much of coin type i is in the optimal solution to A[i][j]
        A = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]
        #J = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

        for i in range(len(A[0])):
            if i % coins[0] == 0:
                A[0][i] = i // coins[0]
                #J[0][i] = A[0][i]
            else:
                A[0][i] = float('inf')
                #J[0][i] = float('inf')
        

        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                # by default set the amount of coins of ith denomination to 0
                A[i][j] = A[i-1][j]

                # for loop below won't run if coins[i] == j

                for a in range(1, (j // coins[i]) + 1):
                    # best using 'a' ith coins
                    if A[i - 1][j - (a * coins[i])] == float('inf'):
                        continue
                    val = (a + A[i - 1][j - (a * coins[i])])
                    if val < A[i][j]:
                        A[i][j] = val
                        #J[i][j] = a

        if A[-1][-1] == float('inf'):
            return -1 

        return A[-1][-1]
        