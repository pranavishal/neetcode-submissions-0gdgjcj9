from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                neighbors = []
                if r < len(grid) - 1:
                    neighbors.append((r + 1, c))
                if r > 0:
                    neighbors.append((r - 1, c))
                if c < len(grid[0]) - 1:
                    neighbors.append((r, c + 1))
                if c > 0:
                    neighbors.append((r, c - 1))
                
                for neighbor in neighbors:
                    nr, nc = neighbor
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            
            if not q:
                break
            
            minutes += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
                    
        return minutes