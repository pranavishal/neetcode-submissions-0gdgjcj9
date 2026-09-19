class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        orig_len = len(nums)
        for i in range(orig_len):
            nums.append(nums[i])
        
        return nums