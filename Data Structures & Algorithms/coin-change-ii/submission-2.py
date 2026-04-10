class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        matrix = [[0] * (amount + 1) for _ in range(len(coins))]

        # Let matrix[i][j] represent the total amount of distinct combinations of 
        # up to (and including) the ith coin denomination that add to j

        # matrix[i][j] = sum(matrix[i][j - (t * coins[i])] for 0 <= t <= floor(j / coins[i]))
        # that are valid

        # base case, when j == 0 or i == 1, the former is already taken care of
        # since all values are set to 0 by default

        # other base case -> i == 1
        for total in range(0, len(matrix[0])):
            if total % coins[0] == 0:
                matrix[0][total] = 1
        
        # general case:     
        for denomination in range(len(matrix)):
            for total in range(len(matrix[0])):
                if total == 0:
                    matrix[denomination][total] = 1
                if denomination > 0 and total > 0:
                    amountOfPossibleCoins = total // coins[denomination]
                    sumValue = 0
                    for coinAmount in range(amountOfPossibleCoins+1):
                        sumValue += matrix[denomination - 1][total - (coinAmount * coins[denomination])]
                    matrix[denomination][total] = sumValue
                
        print(matrix)
        return matrix[len(coins) - 1][amount]
                    
                        
        