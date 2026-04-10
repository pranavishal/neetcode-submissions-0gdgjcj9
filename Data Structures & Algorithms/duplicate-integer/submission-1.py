class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valSet = set()

        for i in range(len(nums)):
            if nums[i] in valSet:
                return True
            
            valSet.add(nums[i])
        
        return False


        