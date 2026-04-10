class Solution:
    def countSubstrings(self, s: str) -> int:
        A = [[0 for _ in range(len(s))] for _ in range(len(s))]
        total_count = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == j:
                    A[i][j] = 1
                elif j == i + 1 and s[i] == s[j]:
                    A[i][j] = 1
                total_count += A[i][j]
        
        for i in range(len(A) - 2, -1, -1):
            for j in range(1, len(A[i])):
                if j > i + 1 and s[i] == s[j]:
                    A[i][j] = A[i + 1][j - 1]
                    total_count += A[i][j]

        return total_count