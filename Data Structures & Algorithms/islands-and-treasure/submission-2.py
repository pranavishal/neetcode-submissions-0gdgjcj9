from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        dist = 1
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                row, col = curr
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
                    if grid[r][c] == INF:
                        grid[r][c] = dist
                        q.append((r, c))
                
            dist += 1

        
        