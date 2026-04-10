from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    visited.add((i, j))
                    islandArea = self.bfs(grid, visited, (i, j))
                    if islandArea > maxArea:
                        maxArea = islandArea
        
        return maxArea
    
    def bfs(self, grid, visited, startNode):
        queue = deque([startNode])
        area = 1

        while queue:
            node = queue.popleft()

            neighbors = []
            if node[0] > 0:
                neighbors.append((node[0] - 1, node[1]))
            if node[0] < len(grid) - 1:
                neighbors.append((node[0] + 1, node[1]))
            if node[1] > 0:
                neighbors.append((node[0], node[1] - 1))
            if node[1] < len(grid[0]) - 1:
                neighbors.append((node[0], node[1] + 1))
            
            for neighbor in neighbors:
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] == 1:
                    area += 1
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return area


        