class Solution:
    def countSubstrings(self, s: str) -> int:
        # same idea as last time but keep a recurring count
        A = [[False for _ in range(len(s))] for _ in range(len(s))]

        total_count = 0
        # base case
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == j:
                    A[i][j] = True
                    total_count += 1

                if j == i + 1:
                    A[i][j] = s[i] == s[j]
                    if A[i][j]:
                        total_count += 1


        # general case, loop bottom to top, left to right
        for i in range(len(A) - 2, -1, -1):
            for j in range(len(A[i])):
                if j > i + 1:
                    A[i][j] = (s[i] == s[j] and A[i + 1][j - 1])
                    if A[i][j]:
                        total_count += 1
        
        return total_count
