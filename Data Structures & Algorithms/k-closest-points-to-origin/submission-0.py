import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for i in range(len(points)):
            x, y = points[i]
            distance = math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(closest, (-distance, x, y))
            if len(closest) > k:
                heapq.heappop(closest)
        
        results = []
        for point in closest:
            dst, x, y = point
            results.append([x, y])
        
        return results