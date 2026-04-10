import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        proc_s = re.sub(r"[^A-Za-z0-9]", '', s.lower())
        left = 0
        right = len(proc_s) - 1
        while left < right:
            if proc_s[left] != proc_s[right]:
                return False
            left += 1
            right -= 1
        
        return True