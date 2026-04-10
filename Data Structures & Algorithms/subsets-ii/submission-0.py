class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        res = []

        def backtracking(res, index):
            sol.append(res.copy())
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                res.append(nums[i])
                backtracking(res, i + 1)
                res.pop()
        
        backtracking(res, 0)
        return sol

            

        