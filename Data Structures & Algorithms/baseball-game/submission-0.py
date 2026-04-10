class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for operation in operations:
            if operation == "+":
                stack.append(stack[-1] + stack[-2])
                total += stack[-1]
            elif operation == "D":
                stack.append(stack[-1] * 2)
                total += stack[-1]
            elif operation == "C":
                total -= stack.pop()
            else:
                total += int(operation)
                stack.append(int(operation))
        
        return total