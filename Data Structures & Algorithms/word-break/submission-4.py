class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Let B be an array where B[i] represents whether s[i:] can be represented via wordDict
        # Base case: B[len(s):] = True
        # General Case: if S[i:].startsWith(word) where word in wordDict
        # if B[i + len(word):] -> B[i] = True
        # return B[0]
        # s = cat, wordDict = [cat]
        # B = [True, False, False, True]

        B = [False] * (len(s) + 1)
        B[len(s)] = True
        for i in range(len(B) - 2, -1, -1):
            for word in wordDict:
                if s[i:].startswith(word) and B[i + len(word)]:
                    B[i] = True
        
        return B[0]

        