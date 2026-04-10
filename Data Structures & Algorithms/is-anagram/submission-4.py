class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = 0
            else:
                sMap[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in tMap:
                tMap[t[i]] = 0
            else:
                tMap[t[i]] += 1
        
        for key, value in sMap.items():
            if key not in tMap or sMap[key] != tMap[key]:
                return False
        
        for key, value in tMap.items():
            if key not in sMap or sMap[key] != tMap[key]:
                return False
        
        return True
        
        