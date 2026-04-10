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
        
        A = [[False for _ in range(len(s) + 1)] for _ in range(len(wordDict))]
        for i in range(len(A)):
            A[i][-1] = True

        B = [False] * (len(s) + 1)
        B[len(s)] = True
        for a in range(len(A[0]) - 2, -1, -1):
            for b in range(len(A)):
                is_prefix = s[a:].startswith(wordDict[b])
                if is_prefix:
                    if B[a + len(wordDict[b])] == True:
                        A[b][a] = True
                        B[a] = True
                
        for i in range(len(A)):
            if A[i][0]:
                return True

        return False

        