class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        soln = []

        # We note that when generating a well formed parentheses string
        # we cannot have the closeCount > openCount

        def generateString(parenthesesString, openCount, closeCount):
            if closeCount > openCount:
                return
            if closeCount == openCount and closeCount == n:
                soln.append(parenthesesString)
                return
            
            if closeCount > n or openCount > n:
                return
            
            else:
                generateString(parenthesesString + '(', openCount + 1, closeCount)
                generateString(parenthesesString + ')', openCount, closeCount + 1)
        
        generateString("", 0, 0)
        return soln