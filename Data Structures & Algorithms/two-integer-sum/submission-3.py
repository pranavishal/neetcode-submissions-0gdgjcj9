class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            v = target - nums[i]
            if v in num_map:
                return [num_map[v], i]
            if nums[i] not in num_map:
                num_map[nums[i]] = i
        
        return None
        