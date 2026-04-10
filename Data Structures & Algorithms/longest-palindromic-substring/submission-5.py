class Solution:
    def longestPalindrome(self, s: str) -> str:
        matrix = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s)):
                if i == j:
                    matrix[i][j] = 1
                if i == j + 1:
                    if s[i] == s[j]:
                        matrix[i][j] = 1
        
        
        for end in range(len(s)):
            for begin in range(len(s)):
                if end - begin >= 2:
                    if s[end] == s[begin] and matrix[end - 1][begin + 1] == 1:
                        matrix[end][begin] = 1
        

        longest = 0
        beginIndex = 0
        endIndex = 0

        for end in range(len(s)):
            for begin in range(len(s)):
                if matrix[end][begin] == 1:
                    if longest < end - begin + 1:
                        longest = end - begin + 1
                        beginIndex = begin
                        endIndex = end

        print(longest)
        return s[beginIndex:endIndex+1]
        