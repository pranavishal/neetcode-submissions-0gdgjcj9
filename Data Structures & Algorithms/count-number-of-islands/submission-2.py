from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:   
        visited = set()
        totalIslands = 0

        def bfs(point, grid, visited):
            visited.add(point)
            q = deque(visited)
            
            while q:
                current = q.popleft()
                neighbors = []
                if current[0] > 0:
                    neighbors.append((current[0] - 1, current[1]))
                if current[0] < len(grid) - 1:
                    neighbors.append((current[0] + 1, current[1]))
                if current[1] > 0:
                    neighbors.append((current[0], current[1] - 1))
                if current[1] < len(grid[0]) - 1:
                    neighbors.append((current[0], current[1] + 1))
                
                for neighbor in neighbors:
                    if grid[neighbor[0]][neighbor[1]] == "1" and (neighbor[0], neighbor[1]) not in visited:
                        q.append((neighbor[0], neighbor[1]))
                        visited.add((neighbor[0], neighbor[1]))
        
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if (i, j) not in visited:
                        visited.add((i, j))
                        bfs((i, j), grid, visited)
                        totalIslands += 1
        
        return totalIslands

        