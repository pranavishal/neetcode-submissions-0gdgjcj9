class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decreasingStack = [(temperatures[0], 0)]
        resultArray = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            print(temperatures[i])
            print(decreasingStack)
            if temperatures[i] > temperatures[i - 1]:
                while len(decreasingStack) > 0 and decreasingStack[-1][0] < temperatures[i]:
                    topStack = decreasingStack.pop()
                    diffInDays = i - topStack[1]
                    resultArray[topStack[1]] = diffInDays
                
            
            decreasingStack.append((temperatures[i], i))
        
        return resultArray



        