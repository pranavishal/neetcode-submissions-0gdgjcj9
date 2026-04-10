class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        A = [[0, 0] for _ in range(len(nums))]
        A[0] = [nums[0], nums[0]]
        max_val = nums[0]

        for i in range(1, len(nums)):
            val_1, val_2 = A[i - 1][0] * nums[i], A[i - 1][1] * nums[i]
            A[i][0] = max(nums[i], val_1, val_2)
            A[i][1] = min(nums[i], val_1, val_2)
            max_val = max(max_val, A[i][0])
        
        return max_val
        