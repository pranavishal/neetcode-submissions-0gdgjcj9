class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        temp_stack = []
        for i in range(len(temperatures)):
            while temp_stack and temperatures[i] > temp_stack[-1][0]:
                temp = temp_stack.pop()
                results[temp[1]] = i - temp[1]
            temp_stack.append((temperatures[i], i))
        
        return results
        