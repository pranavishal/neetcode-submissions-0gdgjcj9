class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        characterMap = {}
        windowBegin = 0
        windowEnd = 1

        characterMap[s[0]] = 0

        longestSubstringLength = 1
        currentSubstringLength = 1

        while windowEnd < len(s):
            nextChar = s[windowEnd]
            if nextChar not in characterMap:
                #print(f'New character {nextChar} at index {windowEnd}')
                characterMap[nextChar] = windowEnd
                currentSubstringLength = windowEnd - windowBegin + 1
                if currentSubstringLength > longestSubstringLength:
                    longestSubstringLength = currentSubstringLength
                
            else:
                if (characterMap[nextChar] < windowBegin):
                    characterMap[nextChar] = windowEnd
                else:
                    windowBegin = characterMap[nextChar] + 1
                currentSubstringLength = windowEnd - windowBegin + 1
                if currentSubstringLength > longestSubstringLength:
                    longestSubstringLength = currentSubstringLength
                characterMap[nextChar] = windowEnd

            
            windowEnd += 1
        
        return longestSubstringLength
            


            