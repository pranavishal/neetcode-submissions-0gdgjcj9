class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Let A[i] represent the length of the longest subsequence that ENDS on nums[i]
        # Base Case: A[0] = 1
        # General Case: A[i] = max(A[j], where 0 <= j < i and nums[j] < nums[i]) else 0
        A = [0] * len(nums)
        A[0] = 1

        for i in range(1, len(A)):
            lis = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    lis = max(lis, A[j])
            A[i] = lis + 1
        
        return max(A)

        