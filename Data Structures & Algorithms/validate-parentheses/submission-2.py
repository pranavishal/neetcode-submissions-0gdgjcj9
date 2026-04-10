class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        stack = []
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            else:
                if not stack or opening.index(stack[-1]) != closing.index(s[i]):
                    return False
                stack.pop()
        
        return len(stack) == 0
        