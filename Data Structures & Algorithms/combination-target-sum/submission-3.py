class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        res = []

        def backtracking(curr_sum, res, index):
            if curr_sum == target:
                sol.append(res.copy())
                return
            
            if curr_sum > target:
                return 
            

            for i in range(index, len(nums)):
                curr_sum += nums[i]
                res.append(nums[i])
                backtracking(curr_sum, res, i)

                curr_sum -= res.pop()

        
        backtracking(0, res, 0)
        return sol




        