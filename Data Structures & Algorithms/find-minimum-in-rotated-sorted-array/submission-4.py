class Solution:
    def findMin(self, nums: List[int]) -> int:
        # general idea, if nums[middle] > nums[right], then the min is in the right half
        # otherwise, the min is in the left half or is the middle

        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2

        minimum = float('inf')

        while True:
            if middle == left or middle == right:
                return min(nums[left], nums[right], minimum)
            
            if nums[middle] < nums[right]:
                minimum = nums[middle]
                right = middle
            else:
                left = middle
            
            middle = (left + right) // 2
            





        