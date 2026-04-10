class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Let matrix[i][j] represent the amount of unique combinations of ways to get to point i j
        # matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        # base case
        # matrix [0][0] = 0
        # matrix[0][j] = 1
        # matrix[i][0] = 1

        # initialising matrix to 0
        matrix = [[0] * n for _ in range(m)]
        print(matrix)

        # base case
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    matrix[i][j] = 1
        
        print(matrix)

        # general case
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0 and j > 0:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
        
        return matrix[m-1][n-1]


        return 0
        