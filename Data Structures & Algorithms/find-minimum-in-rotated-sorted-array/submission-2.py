class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if left > right and middle > left ---> left = middle
        # if left > right and middle < right --> store middle as min and right = middle
        # if right > left --> store left as min and right = middle

        left = 0
        right = len(nums) - 1
        middle = int((left + right) / 2)

        storedMin = 9999

        while True:
            if middle == left or middle == right:
                print(nums[middle])
                return min(storedMin, nums[left], nums[right])
            
            if nums[left] > nums[right]:
                if nums[middle] > nums[left]:
                    left = middle
                
                elif nums[middle] < nums[right]:
                    storedMin = nums[middle]
                    right = middle
                
                else:
                    print('BAD CASE')
                    return storedMin
            
            else:
                storedMin = nums[left]
                right = middle
            
            middle = int((left + right) / 2)
        



        