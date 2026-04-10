class Solution:
    def countSubstrings(self, s: str) -> int:
        matrix = [[0] * len(s) for _ in range(len(s))]

        # Build a matrix where matrix[i][j] represents whether string s[j : i + 1] == 1 if it is a palindrome, 0 otherwise

        # base case: when j == i or  j + 1 == i
        counter = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if j == i:
                    matrix[i][j] = 1
                    counter += 1
                if j + 1 == i:
                    if s[j] == s[i]:
                        matrix[i][j] = 1
                        counter += 1
                if i - j >= 2:
                    if s[i] == s[j] and matrix[i - 1][j + 1] == 1:
                        matrix[i][j] = 1
                        counter += 1
        
        print(matrix)

        return counter
        
