class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        print(nums)
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                while left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                while right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -=1 
                
                if left >= right:
                    break;
                    
                if nums[left] + nums[right] + num == 0:
                    result.append([num, nums[left], nums[right]])
                    print(left, right)
                    left += 1
                    right -= 1
                
                elif nums[left] + nums[right] + num > 0:
                    right -= 1
                
                elif nums[left] + nums[right] + num < 0:
                    left += 1
                else:
                    print("BAD")
        
        return result
