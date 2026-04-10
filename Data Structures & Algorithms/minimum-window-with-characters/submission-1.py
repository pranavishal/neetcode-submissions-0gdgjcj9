class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needMap = {}
        haveMap = {}
        requiredCharsToMatch = 0
        matchedCharsInS = 0

        for letter in t:
            if letter in needMap:
                needMap[letter] += 1
            else:
                needMap[letter] = 1
                requiredCharsToMatch += 1

        r = 0
        l = r
        print(needMap)
        while r < len(s):
            if s[r] in needMap:
                if s[r] in haveMap:
                    haveMap[s[r]] += 1
                else:
                    haveMap[s[r]] = 1

                if haveMap[s[r]] == needMap[s[r]]:
                    matchedCharsInS += 1

            if matchedCharsInS == requiredCharsToMatch:
                break
            
            r += 1
        
        lastCurrentSubstring = ''
        minCurrentSubstring = ''

        if matchedCharsInS == requiredCharsToMatch:
            minCurrentSubstring = s[0:r+1]
            lastCurrentSubstring = minCurrentSubstring
            print(minCurrentSubstring)
        else:
            return minCurrentSubstring
        
        print(haveMap)
        
        while l < r:
            if s[l] in needMap:
                haveMap[s[l]] -= 1
                if haveMap[s[l]] < needMap[s[l]]:
                    haveMap[s[l]] += 1
                    break

            
            l += 1

        minCurrentSubstring = s[l:r+1]
        print(minCurrentSubstring)

        r += 1
        if r < len(s):
            if s[r] in needMap:
                haveMap[s[r]] += 1
                if haveMap[s[r]] == needMap[s[r]]:
                    matchedCharsInS += 1
        
        if s[l] in needMap:
            haveMap[s[l]] -= 1
            if haveMap[s[l]] == needMap[s[l]] - 1:
                matchedCharsInS -= 1
        l += 1

        print('-------------------')
        print(matchedCharsInS)
        print(requiredCharsToMatch)
        while r < len(s):
            if matchedCharsInS == requiredCharsToMatch:
                print(s[l:r+1])
                while l < r:
                    if s[l] in needMap:
                        haveMap[s[l]] -= 1
                        if haveMap[s[l]] < needMap[s[l]]:
                            haveMap[s[l]] += 1
                            break
                    l += 1
                minCurrentSubstring = s[l:r+1]

            r += 1
            if r < len(s):
                if s[r] in needMap:
                    haveMap[s[r]] += 1
                    if haveMap[s[r]] == needMap[s[r]]:
                        matchedCharsInS += 1
        
            if s[l] in needMap:
                haveMap[s[l]] -= 1
                if haveMap[s[l]] == needMap[s[l]] - 1:
                    matchedCharsInS -= 1
            l += 1


        return minCurrentSubstring