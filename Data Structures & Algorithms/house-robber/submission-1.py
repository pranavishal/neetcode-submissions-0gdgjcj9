class Solution:
    def rob(self, nums: List[int]) -> int:
        # Let A[i] represent the maximum amount of money that can be robbed up to 
        # and including the ith house (0 indexed)
        # Base Case: A[0] = nums[0], A[1] = max(nums[0], nums[1])
        # General Case: A[i] = max(A[i - 1],  nums[i] + A[i - 2])
        A = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        A[0] = nums[0]
        A[1] = max(nums[0], nums[1])
        for i in range(2, len(A)):
            A[i] = max(A[i - 1], nums[i] + A[i - 2])
        
        return A[-1]
        