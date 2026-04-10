class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        curr_left = 0
        for i in range(len(height)):
            curr_left = max(curr_left, height[i])
            left_max[i] = curr_left
        
        curr_right = 0
        for i in range(len(height) - 1, -1, -1):
            curr_right = max(curr_right, height[i])
            right_max[i] = curr_right
        
        total_trapped = 0
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            
            total_trapped += max(0, min(left_max[i], right_max[i]) - height[i])
        
        return total_trapped

        