from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        curr_min = 0
        min_right = 0
        min_left = 0

        t_count = Counter(t)
        letters_needed = len(t)
        s_count = defaultdict(int)

        left = 0
        for right, letter in enumerate(s):
            if letter in t_count:
                s_count[letter] += 1
                if s_count[letter] <= t_count[letter]:
                    letters_needed -= 1
            if letters_needed == 0:
                break
        if letters_needed > 0:
            return ""
        
        def shrink_window(left):
            while True:
                letter = s[left]
                if letter in t_count:
                    if s_count[letter] - 1 < t_count[letter]:
                        break
                    else:
                        s_count[letter] -= 1
                        left += 1
                else:
                    left += 1
            
            return left

        left = shrink_window(0)
        curr_min = (right - left + 1)
        min_right = right
        min_left = left
        
        for i in range(right + 1, len(s)):
            letter = s[i]
            if letter in t_count:
                s_count[letter] += 1
                left = shrink_window(left)
                if i - left + 1 < curr_min:
                    min_right = i
                    min_left = left
        
        return s[min_left:min_right + 1]

                    

        

        



            