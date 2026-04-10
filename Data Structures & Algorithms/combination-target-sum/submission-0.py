class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        soln = []

        def combinationSum(currentCombination, index, currentSum):
            if currentSum == target:
                soln.append(currentCombination[:])
                return
            
            if currentSum > target:
                return
            
            if index >= len(nums):
                if currentSum == target:
                    soln.append(currentCombination[:])
                return
            
            else:
                currentCombination.append(nums[index])
                combinationSum(currentCombination, index, currentSum + nums[index])

                currentCombination.pop()
                combinationSum(currentCombination, index + 1, currentSum)
        
        combinationSum([], 0, 0)
        return soln

        