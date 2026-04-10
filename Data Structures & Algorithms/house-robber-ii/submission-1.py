class Solution:
    def rob(self, nums: List[int]) -> int:
        A = [0] * (len(nums) - 1)
        B = [0] * (len(nums) - 1)

        if len(nums) < 4:
            return max(nums)

        A[0] = nums[0]
        A[1] = max(nums[0], nums[1])

        B[0] = nums[1]
        B[1] = max(nums[1], nums[2])

        for i in range(len(nums)):
            if i > 1 and i < len(nums) - 1:
                A[i] = max(A[i - 1], nums[i] + A[i - 2])
            if i > 2:
                B[i - 1] = max(B[i - 2], nums[i] + B[i - 3])
        
        return max(A[-1], B[-1])