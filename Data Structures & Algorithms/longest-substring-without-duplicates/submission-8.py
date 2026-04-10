class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_map = {}
        longest = 0
        left = 0
        for right in range(len(s)):
            if s[right] in sub_map and sub_map[s[right]] >= left:
                left = sub_map[s[right]] + 1
            sub_map[s[right]] = right
            longest = max(longest, right - left + 1)
        
        return longest

        