from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target - num], i]

            if num not in num_map:
                num_map[num] = i