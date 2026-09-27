class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + '#' + word
        
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        returnVal = []
        reading_len = True
        str_len = ''
        num_len = 0
        i = 0
        while i < len(s):
            if s[i] == '#' and reading_len:
                num_len = int(str_len)
                str_len = ''
                reading_len = False
                i += 1

            elif reading_len:
                str_len += s[i]
                i += 1
            
            if not reading_len:
                word = ""
                for x in range(i, i + num_len):
                    word += s[x]
                i += num_len
                returnVal.append(word)
                reading_len = True
        
        return returnVal

                
                
            


