class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_val = float('inf')
        while left <= right:
            middle = (left + right) // 2
            if nums[left] <= nums[middle]:
                min_val = min(min_val, nums[left])
                left = middle + 1
            elif nums[middle] <= nums[right]:
                min_val = min(min_val, nums[middle])
                right = middle - 1

        return min_val
