class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        sol = []
        res = []

        def backtracking(curr_sum, res, index):
            if curr_sum == target:
                sol.append(res.copy())
                return 
            
            if curr_sum > target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                curr_sum += candidates[i]
                res.append(candidates[i])
                backtracking(curr_sum, res, i + 1)

                curr_sum -= res.pop()
        
        backtracking(0, res, 0)
        return sol
            

        