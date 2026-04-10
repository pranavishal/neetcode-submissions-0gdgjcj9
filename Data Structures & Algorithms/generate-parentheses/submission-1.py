class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        totalParenthesis = []

        def solution(s, openCount, closedCount):
            if openCount > n or closedCount > n:
                return 

            if closedCount > openCount:
                return
            
            if closedCount == openCount and closedCount == n:
                totalParenthesis.append(s)
                return
            
            solution(s + "(", openCount + 1, closedCount)
            solution(s + ")", openCount, closedCount + 1)
            


        solution('', 0, 0)

        return totalParenthesis