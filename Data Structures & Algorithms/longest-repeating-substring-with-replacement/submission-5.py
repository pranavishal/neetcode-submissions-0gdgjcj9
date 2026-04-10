class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freqMap = {s[0]: 1}
        mostFreqCount = 1
        maxLength = 1

        for right in range(1, len(s)):
            print(s[left:right+1])
            if s[right] not in freqMap:
                freqMap[s[right]] = 1
            else:
                freqMap[s[right]] += 1
            if freqMap[s[right]] > mostFreqCount:
                mostFreqCount = freqMap[s[right]]
            currentLength = (right - left) + 1
            print(mostFreqCount)
            print(right)
            print(left)
            if mostFreqCount + k >= currentLength:
                print('HERE')
                if currentLength > maxLength:
                    maxLength = currentLength
            else:
                while (mostFreqCount + k < (right - left) + 1):
                    freqMap[s[left]] -= 1
                    left += 1
            


        return maxLength
        