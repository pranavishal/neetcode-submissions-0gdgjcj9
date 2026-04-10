from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for time in times:
            src, dst, w = time
            adj_list[src].append((dst, w))
        
        node_heap = []
        heapq.heappush(node_heap, (0, k))
        results = {}

        while node_heap:
            cost, node = heapq.heappop(node_heap)
            if node in results:
                continue 
            
            results[node] = cost

            for dst, w in adj_list[node]:
                if dst not in results:
                    heapq.heappush(node_heap, (cost + w, dst))
            

        max_time = float('-inf')
        print(results)
        for i in range(1, n + 1):
            if i not in results:
                return -1
            max_time = max(max_time, results[i])
        
        return max_time


        