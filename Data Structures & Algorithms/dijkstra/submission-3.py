from collections import defaultdict
import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = defaultdict(list)
        for edge in edges:
            s, d, w = edge
            adj_list[s].append((w, d))
        
        node_heap = []
        heapq.heappush(node_heap, (0, src))
        results = {}

        while node_heap:
            total, node = heapq.heappop(node_heap)
            if node in results:
                continue
            
            results[node] = total
            
            for weight, destination in adj_list[node]:
                if destination not in results:
                    heapq.heappush(node_heap, (total + weight, destination))
        
        for i in range(n):
            if i not in results:
                results[i] = -1
        
        return results
        