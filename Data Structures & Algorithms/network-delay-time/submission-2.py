import heapq
from collections import deque, defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for time in times:
            source, destination, weight = time
            adj_list[source].append((weight, destination))
        
        heap = []
        heapq.heappush(heap, (0, k))
        results = {}
        
        while heap:
            curr_weight, node = heapq.heappop(heap)
            if node in results:
                continue
            
            results[node] = curr_weight
            
            for weight, neighbor in adj_list[node]:
                if neighbor not in results:
                    heapq.heappush(heap, (weight + curr_weight, neighbor))
        
        curr_max = float('-inf')

        for i in range(1, n + 1):
            if i not in results:
                return -1

            curr_max = max(curr_max, results[i])
        
        return curr_max
            
        