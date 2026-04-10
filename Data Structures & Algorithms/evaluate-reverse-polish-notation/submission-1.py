class Solution:
    def evalRPN(self, tokens: List[str]) -> int:  
        numList = []

        for i in range(len(tokens)):
            match tokens[i]:
                case '+':
                    rightVal = numList.pop()
                    leftVal = numList.pop()
                    numList.append(int(leftVal) + int(rightVal))


                case '-':
                    rightVal = numList.pop()
                    leftVal = numList.pop()
                    numList.append(int(leftVal) - int(rightVal))


                case '*':
                    rightVal = numList.pop()
                    leftVal = numList.pop()
                    numList.append(int(leftVal) * int(rightVal))


                case '/':
                    rightVal = numList.pop()
                    leftVal = numList.pop()
                    numList.append(int(int(leftVal) / int(rightVal)))
                
                case _:
                    numList.append(int(tokens[i]))

        
        return numList[0]
        