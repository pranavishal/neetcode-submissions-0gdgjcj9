from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        left = 0
        max_freq = 0
        max_len = 0
        for right, letter in enumerate(s):
            counter[letter] += 1
            max_freq = max(max_freq, counter[letter])
            while max_freq + k < (right - left + 1):
                counter[s[left]] -= 1
                left += 1
            max_len = max(max_len, (right - left + 1))
        return max_len
        