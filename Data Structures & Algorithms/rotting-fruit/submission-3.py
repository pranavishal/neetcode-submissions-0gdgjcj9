from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        total_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] != 0:
                    total_oranges += 1
        
        def bfs(q):
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
                        if grid[r][c] == 1:
                            q.append(neighbor)
                            grid[r][c] = 2
                if q:
                    time += 1
            
            return time
        
        min_time = bfs(q)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return min_time


        