class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_zero = False
        first_col_zero = False

        # Store whether or not the first row and columns are 0 rows
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                first_row_zero = True
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_zero = True
        

        # for each row i, matrix[i][0] == 0 if its a 0 row, otherwise leave original value
        for i in range(1, len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    break

        # for each column i, matrix[0][i] == 0 if its a 0 col, otherwise leave original value
        for i in range(1, len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[j][i] == 0:
                    matrix[0][i] = 0
                    break
        
        
        # go through first row, and set respective columns to 0
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0

        # go through first col, and set respective row to 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        # then set first row to zero if needed 
        if first_row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        # set first col to zero if needed
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        
