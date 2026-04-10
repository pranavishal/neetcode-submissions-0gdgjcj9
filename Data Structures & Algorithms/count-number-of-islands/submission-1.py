from collections import deque

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numberOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    numberOfIslands += 1
                    visited.add((i, j))
                    self.bfs(grid, (i, j), visited)
        
        return numberOfIslands

    

    def bfs(self, grid: List[List[str]], startNode, visited):
        queue = deque([startNode])
        
        while queue:
            currentNode = queue.popleft()
            neighbors = []
            if currentNode[0] > 0:
                neighbors.append((currentNode[0] - 1, currentNode[1]))
            if currentNode[0] < len(grid) - 1:
                neighbors.append((currentNode[0] + 1, currentNode[1]))
            if currentNode[1] > 0:
                neighbors.append((currentNode[0], currentNode[1] - 1))
            if currentNode[1] < len(grid[0]) - 1:
                neighbors.append((currentNode[0], currentNode[1] + 1))
            

            for neighbor in neighbors:
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] == '1':
                    visited.add((neighbor[0], neighbor[1]))
                    queue.append((neighbor[0], neighbor[1]))







        