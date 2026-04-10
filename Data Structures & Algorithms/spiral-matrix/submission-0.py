class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        result = []
        matrix_len = len(matrix) * len(matrix[0])

        while left < right and top < bottom:
            print(left)
            print(right)
            print(top)
            print(bottom)
            print('----------------------')
            # top left to top right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            if len(result) == matrix_len:
                break

            # from top right to bottom right
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1
            if len(result) == matrix_len:
                break

            # from bottom right to bottom left
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
            if len(result) == matrix_len:
                break

            # from bottom left to top left
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            if len(result) == matrix_len:
                break
        
        return result



            
