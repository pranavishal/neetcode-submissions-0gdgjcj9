import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        results = {}
        pos_heap = []
        heapq.heappush(pos_heap, (grid[0][0], 0, 0))

        while pos_heap:
            weight, row, col = heapq.heappop(pos_heap)
            if (row, col) in results:
                continue
            
            results[(row, col)] = weight
            neighbors = []
            if row < len(grid) - 1:
                neighbors.append((row + 1, col))
            if row > 0:
                neighbors.append((row - 1, col))
            if col < len(grid[0]) - 1:
                neighbors.append((row, col + 1))
            if col > 0:
                neighbors.append((row, col - 1))
            
            for neighbor in neighbors:
                r, c = neighbor
                if (r, c) not in results:
                    if grid[r][c] > weight:
                        heapq.heappush(pos_heap, (weight + (grid[r][c] - weight), r, c))
                    else:
                        heapq.heappush(pos_heap, (weight, r, c))
        
        return results[(len(grid) - 1, len(grid) - 1)]

            
            

        