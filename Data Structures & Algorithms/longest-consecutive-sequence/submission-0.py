class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxConsecutiveLength = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in numSet:
                consecutiveCount = 1
                value = nums[i]
                while value + 1 in numSet:
                    consecutiveCount += 1
                    value += 1
                if consecutiveCount > maxConsecutiveLength:
                    maxConsecutiveLength = consecutiveCount
            
        return maxConsecutiveLength