class Solution:
    def isValid(self, s: str) -> bool:
        parenDict = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for i in range(len(s)):
            if s[i] in parenDict.values():
                stack.append(s[i])
            else:
                if not stack or parenDict[s[i]] != stack[-1]:
                    return False
                stack.pop()
        
        return len(stack) == 0
        