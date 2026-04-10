class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_container = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            curr = min(heights[left], heights[right]) * (right - left)
            max_container = max(curr, max_container)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return max_container