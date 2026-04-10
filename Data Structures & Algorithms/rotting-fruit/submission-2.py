from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_set = set()
        total_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_set.add((i, j))
                if grid[i][j] != 0:
                    total_oranges += 1
        
        def bfs(rotten_set):
            q = deque(rotten_set)
            time = 0
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
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
                        if neighbor not in rotten_set and grid[r][c] == 1:
                            q.append(neighbor)
                            rotten_set.add(neighbor)
                if q:
                    time += 1
            
            return time
        
        min_time = bfs(rotten_set)

        if len(rotten_set) != total_oranges:
            return -1
        
        return min_time


        