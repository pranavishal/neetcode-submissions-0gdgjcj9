from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for letter in s:
            s_map[letter] += 1
        
        for letter in t:
            t_map[letter] += 1


        if len(s_map.items()) != len(t_map.items()):
            return False

        for letter, count in s_map.items():
            if t_map[letter] != count:
                return False

        return True  
