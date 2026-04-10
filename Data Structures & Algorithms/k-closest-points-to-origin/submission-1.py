import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            distance = math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(heap, (-distance, [x, y]))
            while len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for p in heap:
            val = p[1]
            result.append(val)
        
        return result
        