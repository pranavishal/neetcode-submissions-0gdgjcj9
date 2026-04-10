class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            last_index = i
            while stack and stack[-1][1] >= height:
                curr_bar = stack.pop()
                last_index = curr_bar[0]
                area = (i - curr_bar[0]) * curr_bar[1]
                max_area = max(max_area, area)
            
            stack.append((last_index, height))
        
        for bar in stack:
            area = (len(heights) - bar[0]) * bar[1]
            max_area = max(max_area, area)
        
        return max_area

                
            

            