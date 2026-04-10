class Solution:
    def trap(self, height: List[int]) -> int:
        # Find the largest index to the left and right of each element
        # subtract the element from the minimum of left and right
        # that is how much can be stored
        # do this for all elements

        # make two arrays, one storing the largest bar up untl that from left
        # The other one from right

        largestFromLeft = [0] * len(height)
        largestFromRight = [0] * len(height)
        
        largestLeft = 0
        largestRight = 0
        for i in range(len(height)):
            if height[i] > largestLeft:
                largestLeft = height[i]
            largestFromLeft[i] = largestLeft
        
        for i in range(len(height) - 1, -1, -1):
            if height[i] > largestRight:
                largestRight = height[i]
            
            largestFromRight[i] = largestRight
        

        totalRainWaterTrapped = 0
        print(largestFromLeft)
        print(largestFromRight)

        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            
            minLarger = min(largestFromLeft[i - 1], largestFromRight[i + 1])

            if minLarger - height[i] > 0:
                totalRainWaterTrapped += minLarger - height[i]
        
        return totalRainWaterTrapped


        