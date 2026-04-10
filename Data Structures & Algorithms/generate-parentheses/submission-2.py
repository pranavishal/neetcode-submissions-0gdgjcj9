class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []

        def backtracking(curr, open_count, closed_count):
            if open_count > n or closed_count > n or closed_count > open_count:
                return
            
            if open_count == closed_count and open_count == n:
                sol.append(curr)
                return 
            
            backtracking(curr + '(', open_count + 1, closed_count)
            backtracking(curr + ')', open_count, closed_count + 1)
        
        backtracking('', 0, 0)
        return sol