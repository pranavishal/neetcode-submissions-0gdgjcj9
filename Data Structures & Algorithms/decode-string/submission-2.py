class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        idx = len(s) - 1
        while idx >= 0:
            dig_val = ""
            while idx >= 0 and s[idx].isdigit():
                dig_val = s[idx] + dig_val
                idx -= 1
            if dig_val:
                stack.pop()
                str_val = ""
                while stack[-1] != "]":
                    str_val += stack.pop()
                stack.pop()
                stack.append(str_val * int(dig_val))
            else:
                stack.append(s[idx])
                idx -= 1
            
        return_val = ""
        for comp in reversed(stack):
            return_val += comp
        
        return return_val

        
    


        