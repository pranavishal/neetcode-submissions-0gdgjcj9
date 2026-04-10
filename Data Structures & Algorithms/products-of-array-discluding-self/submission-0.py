class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardArray = [0] * len(nums)
        reverseArray = [0] * len(nums)

        answerArray = [0] * len(nums)

        forwardArray[0] = nums[0]
        reverseArray[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(1, len(forwardArray)):
            forwardArray[i] = nums[i] * forwardArray[i - 1]
        
        for i in range(len(reverseArray) - 2, - 1, -1):
            reverseArray[i] = reverseArray[i + 1] * nums[i]

        for i in range(len(answerArray)):
            if i == 0:
                answerArray[i] = reverseArray[i + 1]

            elif i == len(answerArray) - 1:
                answerArray[i] = forwardArray[i - 1]
            
            else:
                answerArray[i] = forwardArray[i - 1] * reverseArray[i + 1]
        
        return answerArray