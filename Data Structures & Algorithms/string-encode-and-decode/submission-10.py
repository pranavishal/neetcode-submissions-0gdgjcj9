class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ''
        for i in range(len(strs)):
            encodedString += str(len(strs[i])) + ':'
            encodedString += (strs[i])
        
        
        print(encodedString)
        return encodedString
        

    def decode(self, s: str) -> List[str]:
        readingLength = True
        readingString = False

        decodedArray = []

        currentLengthReader = ''
        currentStringReader = ''
        currentStringLength = 0

        for i in range(len(s)):
            if readingLength:
                if s[i] == ':':
                    print('colon detected')
                    currentStringLength = int(currentLengthReader)
                    print(currentStringLength)
                    if currentStringLength == 0:
                        currentLengthReader = '' 
                        decodedArray.append('')
                        continue
                    readingLength = False
                    readingString = True
                    currentLengthReader = '' 
                    continue  
                else:
                    currentLengthReader += s[i]
                
            if readingString:
                if currentStringLength == 1:
                    currentStringReader += s[i]
                    readingLength = True
                    readingString = False
                    decodedArray.append(currentStringReader)
                    currentStringReader = ''

                else:
                    currentStringReader += s[i]
                    currentStringLength -= 1
        
        return decodedArray



        
