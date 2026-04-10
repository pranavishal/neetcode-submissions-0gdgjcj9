class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        the_list = [1] * n
        
        for i in range(1, m):
            new_list = [1] * n
            for j in range(1, n):
                new_list[j] = the_list[j] + new_list[j - 1]
            the_list = new_list
        
        return the_list[-1]
        