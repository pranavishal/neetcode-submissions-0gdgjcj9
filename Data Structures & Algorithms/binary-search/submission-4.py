class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = int((left + right) / 2)
        
        currentNum = nums[middle]

        while True:
            if currentNum == target:
                return middle
            
            if middle == right or middle == left:
                if nums[right] == target:
                    return right
                if nums[left] == target:
                    return left
                    
                return -1
            
            if currentNum > target:
                right = middle
            
            if currentNum < target:
                left = middle
            
            middle = int((left + right) / 2)
            currentNum = nums[middle]

        