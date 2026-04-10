class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Let A represent an array where A[i] = longest subsequence that ends on nums[i]
        # Base Case: A[0] = 1
        # General Case: A[i] = max (A[j] where j < i and nums[j] < nums[i])
        A = [1] * len(nums)
        max_len = 1

        for i in range(1, len(nums)):
            longest_valid_ss = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    longest_valid_ss = max(longest_valid_ss, A[j])
            A[i] += longest_valid_ss
            max_len = max(max_len, A[i])
        return max_len