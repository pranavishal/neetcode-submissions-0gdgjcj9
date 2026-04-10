class Solution:
    def numDecodings(self, s: str) -> int:
        # let N[i] represent the amount of ways you can decode string s up to and including index i (s[:i])
        # Base case: i == 0 -> N[0] = 1
        # Base case: i == 1 -> N[1] = m(s[0:2]) where m(s) returns 1 if a 2 character string can be decoded together, 0 otherwise
        # General case: N[i] = N[i - 1] + m(s[i - 1: i + 1]) 

        def m(s):
            if s[0] == '0':
                return 0

            if int(s) <= 26:
                return 1
            
            return 0

        if len(s) == 1:
            if s[0] != '0':
                return 1
            else:
                return 0
        
        N = [0] * len(s)
        if s[0] == '0':
            N[0] = 0
        else:
            N[0] = 1

        if s[1] == '0':
            print(m(s[0:2]))
            if m(s[0:2]) == 0:
                N[1] = 0
            else:
                N[1] = 1

        else:
            if s[0] == '0':
                N[1] = 0
                return 0
            else:
                N[1] = 1 + m(s[0:2]) 
            

        for i in range(2, len(s)):
            if s[i] == '0':
                if m(s[i - 1: i + 1]) == 0:
                    N[i] = 0
                else:
                    N[i] = N[i - 2]
            else:
                if s[i - 1] == '0':
                    if N[i - 1] == 0:
                        N[0] = 0
                        return 0
                    else:
                        N[i] = N[i - 1]
                else:
                    if m(s[i - 1: i + 1]) == 1:
                        N[i] = N[i - 1] + N[i - 2]
                    else:
                        N[i]  = N[i - 1]


        
        print(N)
        return N[len(N) - 1]
