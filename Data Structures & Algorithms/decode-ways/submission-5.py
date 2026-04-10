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
        
        if s[1] == "0":
            if s[0] in ["1", "2"]:
                A[1] = 1
            else:
                return 0

        elif int(s[1]) >= 1 and int(s[1]) <= 6:
            if s[0] in ["1", "2"]:
                A[1] = 2
            else:
                A[1] = 1
        
        else:
            A[1] = 1

        for i in range(2, len(A)):
            if s[i] == "0":
                if s[i - 1] not in ["1", "2"]:
                    return 0
                A[i] = A[i - 2]
            else:
                A[i] = A[i - 1]
                if int(s[i]) >= 1 and int(s[i]) <= 6:
                    if s[i - 1] in ["1", "2"]:
                        A[i] = A[i - 2] + A[i - 1]
                else:
                    if s[i - 1] == "1":
                        A[i] = A[i - 2] + A[i - 1]
                    
        
        return A[-1]
                    
                


        