class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dist = 0
        for i in range(len(nums)):
            if i > max_dist:
                return False
            max_dist = max(max_dist, i + nums[i])
        
        return True