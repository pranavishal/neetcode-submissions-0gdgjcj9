class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if nums[left] > nums[right] and nums[middle] > nums[left]
        #       ---> if nums[middle] > target ---> right = middle

        #       ---> if nums[middle] < target ----> left = middle

        # if nums[left] > nums[right] and nums[middle] < nums[right]
        #       ---> if nums[middle] < target and nums[right] > target
        #             ---> left = middle
        #.      ---> if nums[middle] < target and nums[right] < target
        #               ----> right = middle
        #.      ---> if nums[middle] > target, then right = middle
        #  

        # if nums[left] > nums[right] ---> regular binary search

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
            
            if nums[left] > nums[right]:
                if nums[middle] > nums[left]:
                    if nums[middle] > target:
                        if nums[left] < target:
                            right = middle
                        elif nums[left] > target:
                            left = middle
                        else:
                            return left
                    elif nums[middle] < target:
                        left = middle
                    else:
                        print('BAD CASE OH NO')
                
                elif nums[middle] < nums[right]:
                    if nums[middle] < target and nums[right] >= target:
                        left = middle
                    elif nums[middle] < target and nums[right] < target:
                        right = middle
                    elif nums[middle] > target:
                        right = middle
                    
                    else:
                        return -1
                else:
                    print(left)
                    print(right)
                    print(middle)
                    return -1
            
            else:
                if nums[middle] > target:
                    right = middle
                else:
                    left = middle
            
            middle = (left + right) // 2
            
