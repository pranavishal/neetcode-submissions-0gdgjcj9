import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        soln = []

        heap = []

        windowBegin = 0
        windowEnd = 0

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        soln.append(-heap[0][0])

        windowEnd = k
        windowBegin = 1

        while windowEnd < len(nums):
            heapq.heappush(heap, (-nums[windowEnd], windowEnd))
            while True:
                largest = heap[0]
                if largest[1] >= windowBegin and largest[1] <= windowEnd:
                    soln.append(-largest[0])
                    break
                else:
                    heapq.heappop(heap)

            windowEnd += 1
            windowBegin += 1
            

        
        return soln
