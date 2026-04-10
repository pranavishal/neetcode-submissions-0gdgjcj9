class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Let A[i][j] represent the LCS between text1[:i] and text2[:j]
        # Base Case: A[i][j] == 0 if i == 0 or j == 0
        # General Case A[i][j] == 1 + A[i - 1][j - 1] if text1[i - 1] == text2[j - 1], else
        # A[i][j] == max(A[i][j - 1], A[i - 1][j])
        A = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                if text1[i - 1] == text2[j - 1]:
                    A[i][j] = 1 + A[i - 1][j - 1]
                else:
                    A[i][j] = max(A[i - 1][j], A[i][j - 1])
        
        return A[-1][-1]

        