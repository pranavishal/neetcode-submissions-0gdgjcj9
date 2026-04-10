class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_num = 0
        for i in range(1, len(nums) + 1):
            xor_num = xor_num ^ i
        
        for i in range(len(nums)):
            xor_num = xor_num ^ nums[i]
        
        return xor_num
        