class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # general idea
        # if nums[middle] > nums[left], then the left half is sorted
        # if its not then the right half is sorted
        # if the left half is sorted and the target is in that range, then search left half
        # if the left half is sorted and the target is not in that range, search right half
        
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2

        while True:
            if middle == left or middle == right:
                if nums[left] == target:
                    return left
                if nums[right] == target:
                    return right
                
                return -1
            
            if nums[middle] == target:
                return middle
            
            if nums[middle] > nums[left]:
                if target >= nums[left] and target < nums[middle]:
                    right = middle
                else:
                    left = middle
            
            else:
                if target > nums[middle] and target <= nums[right]:
                    left = middle
                else:
                    right = middle
            
            middle = (left + right) // 2
        