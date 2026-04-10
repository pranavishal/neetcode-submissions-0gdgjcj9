class Solution:
    def rob(self, nums: List[int]) -> int:
    
        # What is the recursive relationship

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            maxList = [nums[0], max(nums[0], nums[1])]

            for i in range(2, len(nums)):
                maxAmountStolenUntilHousei = max(maxList[i - 2] + nums[i], maxList[i - 1])
                maxList.append(maxAmountStolenUntilHousei)
            

            return maxList[-1]
        