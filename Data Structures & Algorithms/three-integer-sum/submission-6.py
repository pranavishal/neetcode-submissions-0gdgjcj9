class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        print(nums)
        last_num = None
        for i, num in enumerate(nums):
            if num == last_num:
                continue
            last_num = num
            left = i + 1
            right = len(nums) - 1
            curr_target = num
            while left < right:
                total = nums[left] + nums[right] + curr_target             
                left_val = nums[left]
                right_val = nums[right]
                if total < 0:
                    left += 1
                    while left < len(nums) and nums[left] == left_val:
                        left += 1
                    

                elif total > 0:
                    right -= 1
                    while right > i and nums[right] == right_val:
                        right -= 1

                else:
                    sol.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < len(nums) and nums[left] == left_val:
                        left += 1

                    while right > i and nums[right] == right_val:
                        right -= 1
        return sol