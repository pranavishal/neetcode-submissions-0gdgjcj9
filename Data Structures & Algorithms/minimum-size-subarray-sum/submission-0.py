class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = 0
        running_sum = 0
        for right in range(len(nums)):
            running_sum += nums[right]
            while running_sum - nums[left] >= target:
                running_sum -= nums[left]
                left += 1
            if running_sum >= target:
                min_len = min(min_len, right - left + 1)
        
        return min_len if min_len < float('inf') else 0
