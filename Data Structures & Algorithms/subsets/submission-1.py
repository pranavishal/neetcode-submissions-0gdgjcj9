class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtracking(index):
            if index == len(nums):
                sol.append(res.copy())
                return 
            
            res.append(nums[index])
            backtracking(index + 1)
            res.pop()
            backtracking(index + 1)
        
        backtracking(0)
        return sol
                
        