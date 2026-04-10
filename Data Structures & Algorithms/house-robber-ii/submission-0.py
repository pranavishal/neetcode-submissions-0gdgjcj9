class Solution:
    def rob(self, nums: List[int]) -> int:
        # Same approach as last problem, but need to store if we 
        # selected first house

        # If we did, final house selection must take into consideration 
        # of letting go of first house value

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            # See the max value not including the first house
            # See the max value not including the last house
            # Return which is larger

            # Not including first house
            maxList = [nums[1], max(nums[1], nums[2])]

            for i in range(2, len(nums) - 1):
                maxAmountToAdd = max(maxList[i - 2] + nums[i + 1], maxList[i - 1])
                maxList.append(maxAmountToAdd)
            
            maxNotIncludingFirst = maxList[-1]

            maxList.clear()

            # Not including last house
            maxList = [nums[0], max(nums[0], nums[1])]

            for i in range(2, len(nums) - 1):
                maxAmountToAdd = max(maxList[i - 2] + nums[i], maxList[i - 1])
                maxList.append(maxAmountToAdd)
            
            maxNotIncludingLast = maxList[-1]

            if maxNotIncludingFirst > maxNotIncludingLast:
                return maxNotIncludingFirst
            else:
                return maxNotIncludingLast



        