class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        uniqueSolutions = []

        def backtracking(target, currentList, iterator):
            if target == 0:
                uniqueSolutions.append(currentList.copy())
                return

            if target < 0:
                return


            if iterator >= len(nums):
                return    
            
            currentList.append(nums[iterator])
            backtracking(target - nums[iterator], currentList, iterator)
            currentList.pop()
            backtracking(target, currentList, iterator + 1)
        
        backtracking(target, [], 0)
        return uniqueSolutions
