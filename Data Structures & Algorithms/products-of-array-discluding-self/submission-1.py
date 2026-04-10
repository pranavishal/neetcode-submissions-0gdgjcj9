class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_products = [1] * len(nums)
        backward_products = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                forward_products[i] = nums[i]
            else:
                forward_products[i] = nums[i] * forward_products[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                backward_products[i] = nums[i]
            else:
                backward_products[i] = nums[i] * backward_products[i + 1]
        
        products = []
        for i in range(len(nums)):
            if i == 0:
                products.append(backward_products[i + 1])
            elif i == len(nums) - 1:
                products.append(forward_products[i - 1])
            else:
                products.append(forward_products[i - 1] * backward_products[i + 1])
        
        return products

        