from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        def bfs(pos):
            area = 0
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
                    n_row, n_col = neighbor
                    if grid[n_row][n_col] == 1 and (n_row, n_col) not in visited:
                        visited.add((n_row, n_col))
                        q.append(((n_row, n_col)))
                
                area += 1
            
            return area


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    max_area = max(max_area, bfs((i, j)))
        
        return max_area
        