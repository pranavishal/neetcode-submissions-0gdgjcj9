from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        curr_sum = 0
        subarray_count = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            subarray_count += prefix_map[curr_sum - k]
            prefix_map[curr_sum] += 1
        
        return subarray_count