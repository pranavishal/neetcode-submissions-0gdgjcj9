from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        letter_set = set()

        for letter in s:
            s_map[letter] += 1
            letter_set.add(letter)

        for letter in t:
            t_map[letter] += 1
            letter_set.add(letter)
        
        for letter in letter_set:
            if letter not in s_map or letter not in t_map:
                return False
            if s_map[letter] != t_map[letter]:
                return False
        
        return True

        