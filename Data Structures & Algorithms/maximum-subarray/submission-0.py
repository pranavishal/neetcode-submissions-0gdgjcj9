class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_max = nums[0]
        max_val = prev_max
        for i in range(1, len(nums)):
            curr_max = max(nums[i], nums[i] + prev_max)
            max_val = max(curr_max, max_val)
            prev_max = curr_max
        return max_val