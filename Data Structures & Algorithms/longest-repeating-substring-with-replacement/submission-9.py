from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = defaultdict(int)
        left = 0
        most_common = 0
        longest = 0
        for right in range(len(s)):
            char_map[s[right]] += 1
            most_common = max(most_common, char_map[s[right]])
            while (right - left + 1) - most_common - k > 0:
                char_map[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest   