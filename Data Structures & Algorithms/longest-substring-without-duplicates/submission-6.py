from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        val_map = defaultdict(int)
        left = 0
        for right, letter in enumerate(s):            
            if letter in val_map and val_map[letter] >= left:
                left = val_map[letter] + 1
            else:
                max_len = max(max_len, (right - left + 1))
            val_map[letter] = right
        return max_len
        