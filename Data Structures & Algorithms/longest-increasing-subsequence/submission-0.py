class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # recurrence relation
        # let p[i] be the longest recurrence relation that ends on index i
        # p[0] = 1 // base case
        # for every i > 0, p[i] = max(p[i - x]) + 1, where p[i] > p[x]
        p = [0] * len(nums)

        p[0] = 1

        for i in range(1, len(nums)):
            amountBigger = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    if p[j] > amountBigger:
                        amountBigger = p[j]
            p[i] = amountBigger + 1
        
        return max(p)
