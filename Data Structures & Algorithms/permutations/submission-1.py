class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        res = []

        used = [False] * len(nums)

        def backtracking(res):
            if len(res) == len(nums):
                sol.append(res.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                res.append(nums[i])
                backtracking(res)

                res.pop()
                used[i] = False
        
        backtracking(res)
        return sol


        
        