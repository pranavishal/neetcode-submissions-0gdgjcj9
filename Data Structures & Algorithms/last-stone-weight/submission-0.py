import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = []
        for stone in stones:
            heapq.heappush(stone_heap, -stone)
        
        while len(stone_heap) >= 2:
            first = -heapq.heappop(stone_heap)
            second = -heapq.heappop(stone_heap)

            result = abs(first - second)
            if result:
                heapq.heappush(stone_heap, -result)
        
        if stone_heap:
            return -stone_heap[0]
        
        return 0