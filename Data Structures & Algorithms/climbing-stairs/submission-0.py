class Solution:
    def climbStairs(self, n: int) -> int:
        # let A[i] represent the number of distinct ways to climb to the ith stair
        # base case: A[1] = 1, A[2] = 2
        # General Case: A[n] = A[n - 1] + A[n - 2]
        if n <= 2:
            return n

        b1 = 1
        b2 = 2
        for i in range(3, n + 1):
            temp = b2
            b2 = b2 + b1
            b1 = temp
        
        return b2
        