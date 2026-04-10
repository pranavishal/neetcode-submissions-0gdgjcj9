class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1Len = len(text1)
        text2Len = len(text2)

        matrix = [[0] * (text2Len + 1) for _ in range(text1Len + 1)]  

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0 and j > 0:
                    if text1[i - 1] == text2[j - 1]:
                        matrix[i][j] = 1 + matrix[i - 1][j - 1]
                    else:
                        matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
        
        print(matrix)
        
        return matrix[len(matrix) - 1][len(matrix[0]) - 1]