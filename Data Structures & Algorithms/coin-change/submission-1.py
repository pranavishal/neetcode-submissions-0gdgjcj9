class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 2D Dynamic Programming approach
        matrix = [[0] * (amount + 1) for _ in range(len(coins))]
        
        #initialize matrix with base case (only 1 coin type)
        for i in range(len(matrix[0])):
            if i % coins[0] == 0:
                matrix[0][i] = i // coins[0]
            else:
                matrix[0][i] = -1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0 and j > 0:
                    diffAmountsOfCoinIType = j // coins[i]
                    minAmount = -1
                    for k in range(diffAmountsOfCoinIType + 1):
                        if matrix[i - 1][j - (k * coins[i])] < 0:
                            continue
                        if matrix[i - 1][j - (k * coins[i])] >= 0:
                            if minAmount < 0:
                                minAmount = k + matrix[i - 1][j - (k * coins[i])]
                                continue
                            if minAmount > 0:
                                if minAmount > k + matrix[i - 1][j - (k * coins[i])]:
                                    minAmount = k + matrix[i - 1][j - (k * coins[i])]

                    matrix[i][j] = minAmount
        
        print(matrix)
        return matrix[len(coins) - 1][amount]
        