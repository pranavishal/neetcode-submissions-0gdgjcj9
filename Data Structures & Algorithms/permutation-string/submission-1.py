class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # make a 26 size tuple for s1
        s1LetterTuple = ([0] * 26)
        s2LetterTuple = ([0] * 26)

        for i in range(len(s1)):
            s1LetterTuple[ord(s1[i]) - ord('a')] += 1
        

        # Get original window of size s1 in s2
        for i in range(len(s1)):
            s2LetterTuple[ord(s2[i]) - ord('a')] += 1
        

        if s1LetterTuple == s2LetterTuple:
            return True
        
        windowStart = 0
        windowEnd = len(s1) - 1

        while windowEnd < len(s2):
            print(s2LetterTuple)
            if s1LetterTuple == s2LetterTuple:
                return True
            
            if windowEnd == len(s2) - 1:
                return False
            
            s2LetterTuple[ord(s2[windowStart]) - ord('a')] -= 1
            windowStart += 1
            windowEnd += 1
            s2LetterTuple[ord(s2[windowEnd]) - ord('a')] += 1

        
        return False

        

        

        
        