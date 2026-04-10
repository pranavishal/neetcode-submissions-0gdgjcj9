class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_farthest = 0
        for i in range(len(nums)):
            if i > curr_farthest:
                return False
            curr_farthest = max(curr_farthest, i + nums[i])
            if curr_farthest >= len(nums) - 1:
                return True
        return False
            
        