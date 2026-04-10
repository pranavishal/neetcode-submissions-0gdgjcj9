class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        res = []
        def backtracking(index, current_sum):
            if current_sum == target:
                sol.append(res.copy())
            
            if current_sum > target:
                return
            
            for i in range(index, len(nums)):
                res.append(nums[i])
                backtracking(i, current_sum + nums[i])
                res.pop()
        
        backtracking(0, 0)
        return sol