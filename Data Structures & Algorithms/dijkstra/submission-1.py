import heapq
from collections import defaultdict
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = defaultdict(list)
        for edge in edges:
            source, dst, w = edge
            adj_list[source].append((dst, w))
        
        results = {}
        node_heap = []
        heapq.heappush(node_heap, (0, src))
        while node_heap:
            total, node = heapq.heappop(node_heap)
            if node in results:
                continue
            results[node] = total

            for dst, w in adj_list[node]:
                if dst not in results:
                    heapq.heappush(node_heap, (w + total, dst))
        
        for i in range(n):
            if i not in results:
                results[i] = -1
        
        return results
            