import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach
        # Make a map and store element counts as you go through
        # iterate through map and store in heap
        # pop top k elements from heal

        countMap = {}

        for i in range(len(nums)):
            if nums[i] in countMap:
                countMap[nums[i]] += 1
            else:
                countMap[nums[i]] = 1
        
        kHeap = []
        
        for key, value in countMap.items():
            countTuple = (-value, key)
            heapq.heappush(kHeap, countTuple)
        
        returnList = []

        for i in range(k):
            returnList.append(heapq.heappop(kHeap)[1])

        return returnList



        