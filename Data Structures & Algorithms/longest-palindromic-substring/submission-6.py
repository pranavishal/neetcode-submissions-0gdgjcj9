class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Let A[i][j] == True if s[i:j+1] is a palindrome, False otherwise, where j > i
        # General Case: A[i][j] == True if s[i] == s[j] and A[i + 1][j - 1] == True
        # Base Case: A[i][j] == True if i == j and A[i][j] == False if j < i
        # Base Case: if j == i + 1, A[i][j] = s[i] == s[j]
        A = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == j:
                    A[i][j] = True
                if j == i + 1:
                    A[i][j] = s[i] == s[j]

        lps = 0
        lps_str = s[0]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(A[0])):
                if j > i + 1:
                    A[i][j] = s[i] == s[j] and A[i + 1][j - 1]
                if A[i][j] and (j - i + 1) > lps:
                    lps = (j - i + 1)
                    lps_str = s[i:j + 1]
        
        return lps_str

        
        
        