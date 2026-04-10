from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasureNodes = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasureNodes.append((i, j, 0))
        
        self.bfs(grid, treasureNodes)
    
    def bfs(self, grid, treasureNodes):
        queue = treasureNodes

        while queue:
            currentNode = queue.popleft()
            neighbors = []
            if currentNode[0] > 0:
                neighbors.append((currentNode[0] - 1, currentNode[1], currentNode[2] + 1))
            if currentNode[0] < len(grid) - 1:
                neighbors.append((currentNode[0] + 1, currentNode[1], currentNode[2] + 1))
            if currentNode[1] > 0:
                neighbors.append((currentNode[0], currentNode[1] - 1, currentNode[2] + 1))
            if currentNode[1] < len(grid[0]) - 1:
                neighbors.append((currentNode[0], currentNode[1] + 1, currentNode[2] + 1))
            
            for neighbor in neighbors:
                if grid[neighbor[0]][neighbor[1]] == 2147483647:
                    queue.append(neighbor)
                    grid[neighbor[0]][neighbor[1]] = neighbor[2]

            

            

                
