class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_map = {')': '(', '}': '{', ']': '['}
        stack = []
        for paren in s:
            if paren not in parenthesis_map:
                stack.append(paren)
            else:
                if len(stack) == 0 or parenthesis_map[paren] != stack.pop():
                    return False
        
        return len(stack) == 0
        