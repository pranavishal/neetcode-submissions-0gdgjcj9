from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_islands = 0
        def bfs(pos):
            q = deque([pos])

            while q:
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
                    if grid[r][c] == "1" and (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    num_islands += 1
                    visited.add((i, j))
                    bfs((i, j))
        
        return num_islands

        
        