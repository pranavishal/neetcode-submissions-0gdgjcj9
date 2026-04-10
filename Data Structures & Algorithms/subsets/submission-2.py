class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtracking(index):
            sol.append(res.copy())
            
            for i in range(index, len(nums)):
                res.append(nums[i])
                backtracking(i + 1)
                res.pop()
        
        backtracking(0)
        return sol
                
        