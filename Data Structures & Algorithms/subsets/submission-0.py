class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        soln = []

        def subset(current, index):
            if index > len(nums):
                return
            
            if index == len(nums):
                soln.append(current[:])
            
            else:
                current.append(nums[index])
                subset(current, index + 1)
                current.pop()
                subset(current, index + 1)
        
        subset([], 0)
        return soln
        