class Solution:
    def numDecodings(self, s: str) -> int:
        # Let A[i] represent how many ways you can decode s[:i+1]
        # Base Case: A[i] == 1 if i == 0 and int(s[i]) != 0
        # General Case: A[i] = 1 + A[i - 1] if 1 <= int(s[i-1:i+1]) <= 26
        # General Case: return 0 if i > 0 and s[i] = 0, and 1 <= int(s[i-1:i+1]) <= 26
        A = [0] * len(s)
        if int(s[0]) == 0:
            return 0
        
        A[0] = 1
        if len(s) == 1:
            return A[0]
        
        A[1] = 1
        if s[0] == "1":
            if s[1] != "0":
                A[1] = 2
        elif s[0] == "2":
            if int(s[1]) >= 1 and int(s[1]) <= 6:
                A[1] = 2
        elif s[1] == "0":
            return 0

        for i in range(2, len(A)):
            if s[i] == "0":
                if s[i - 1] not in ["1", "2"]:
                    return 0
                A[i] = A[i - 2]
            else:
                A[i] = A[i - 1]
                if s[i - 1] == "1":
                    A[i] = A[i - 1] + A[i - 2]
                elif s[i - 1] == "2":
                    if int(s[i]) >= 1 and int(s[i]) <= 6:
                        A[i] = A[i - 1] + A[i - 2]
                    
        
        return A[-1]
                    
                


        