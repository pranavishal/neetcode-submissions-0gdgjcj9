class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_tuple = [0] * 26
        for s in s1:
            s1_tuple[ord(s) - ord('a')] += 1
        
        s1_tuple = tuple(s1_tuple)
        s1_set = {s1_tuple}
        s2_tuple = [0] * 26

        for i in range(len(s1)):
            s2_tuple[ord(s2[i]) - ord('a')] += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if tuple(s2_tuple) in s1_set:
                return True
            
            s2_tuple[ord(s2[right]) - ord('a')] += 1
            s2_tuple[ord(s2[left]) - ord('a')] -= 1
            left += 1
        
        return tuple(s2_tuple) in s1_set



        