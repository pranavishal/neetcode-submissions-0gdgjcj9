class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [nums[0]] * len(nums)
        backward = [nums[-1]] * len(nums)

        for i in range(1, len(nums)):
            forward[i] = nums[i] * forward[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            backward[i] = nums[i] * backward[i + 1]
        
        returnVal = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                returnVal[i] = backward[i+1]
                continue
            if i == len(nums) - 1:
                returnVal[i] = forward[i - 1]
                continue
            
            returnVal[i] = forward[i - 1] * backward[i + 1]
        
        return returnVal