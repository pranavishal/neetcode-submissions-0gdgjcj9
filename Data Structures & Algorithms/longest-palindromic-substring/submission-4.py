class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Here's the approach
        # Using a 2D dynamic programming approach, we will build a table
        # 1 direction will be the beginning of the substring
        # the other direction will be the end of the substring

        # Now -> we will be able to quickly determine if any substring is a palindrome

        # Note: we can determine this by checking if s[i] == s[j] and 
        # if s[i + 1] - s[j - 1] is also a palindrome

        # Once the table is built, double for loop through i and j, for every palindrome
        # we find in the table, we see the length (j - i) and record the longest length
        # and then return the substring of s from i to j inclusive

        matrix = [[0] * len(s) for _ in range(len(s))]


        for i in range(len(s)):
            for j in range(len(s)):
                if i == j:
                    matrix[i][j] = 1
                if j == i + 1:
                    if s[i] == s[j]:
                        matrix[i][j] = 1
        
        
        for i in range(len(s)):
            for j in range(len(s), -1, -1):
                if i - j >= 2:
                    if s[i] == s[j] and matrix[j + 1][i - 1] == 1:
                        matrix[j][i] = 1
        

        startingIndex = 0
        endingIndex = 0
        maxLength = 0

        print(matrix)

        for i in range(len(s)):
            for j in range(len(s)):
                if j - i + 1 > maxLength and matrix[i][j] == 1:
                    startingIndex = i
                    endingIndex = j
                    maxLength = j - i + 1
        
        return s[startingIndex : endingIndex + 1]


                
        
        





        