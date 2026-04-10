class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # let's rethink about our approach
        # Let A[i, x] represent whether or not wordDict[i] can be used in a valid solution as 
        # representing a prefix of s[x:]
        # A[i] = True if s[x:].startswith(wordDict[i]) 
        #      AND
        # A[j, x + len(wordDict[i])] == True for some  0 <= j <= len(wordDict)
        # if !s[x:].startswith(wordDict[i]): -> A[i, x] = False
        # Base Case, if s == "" return True, Aka A[i, len(s)]

        B = [False] * (len(s) + 1)
        B[len(s)] = True
        for a in range(len(B) - 2, -1, -1):
            for b in range(len(wordDict)):
                is_prefix = s[a:].startswith(wordDict[b])
                if is_prefix:
                    if B[a + len(wordDict[b])] == True:
                        B[a] = True
                
        return B[0]

        