class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Let A[i][j] = True if s[i:j+1] is a palindrome else False
        # General Case: A[i][j] = True if s[i] == s[j] and A[i + 1][j - 1] == True
        # Base Case: if i == j, A[i][j] = True, if j == i + 1, A[i][j] = s[i] == s[j]
        # Base Case: if i > j, A[i][j] = False

        A = [[False for _ in range(len(s))] for _ in range(len(s))]
        left = 0
        right = 0
        max_len = 1

        # base case:
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == j:
                    A[i][j] = True
                if j == i + 1:
                    A[i][j] = s[i] == s[j]
                    if A[i][j]:
                        left = i
                        right = j
                        max_len = max(max_len, (right - left + 1))
        
        # General case, loop from bottom to top, left to right
        for i in range(len(A) - 2, -1, -1):
            for j in range(len(A[0])):
                if j > i + 1:
                    A[i][j] = (s[i] == s[j] and A[i + 1][j - 1])
                    if A[i][j]:
                        if (j - i + 1) > max_len:
                            max_len = j - i + 1
                            left = i
                            right = j
        
        return s[left:right+1]


        