from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # originally is going to be populated with only rotten fruits
        queue = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        maxMinute = self.bfs(grid, queue)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return maxMinute
        

    def bfs(self, grid, queue):
        maxMinute = 0
        while queue:
            currentNode = queue.popleft()
            neighbors = []
            # Get possible top neighbor
            if currentNode[0] > 0:
                neighbors.append((currentNode[0] - 1, currentNode[1], currentNode[2] + 1))
            #get possible bottom layer
            if currentNode[0] < len(grid) - 1:
                neighbors.append((currentNode[0] + 1, currentNode[1], currentNode[2] + 1))
            #get possible left neighbor
            if currentNode[1] > 0:
                neighbors.append((currentNode[0], currentNode[1] - 1, currentNode[2] + 1))
            #get possible right neighbor
            if currentNode[1] < len(grid[0]) - 1:
                neighbors.append((currentNode[0], currentNode[1] + 1, currentNode[2] + 1))
                
            # iterate through neighbors and append the fresh fruit ones
            for neighbor in neighbors:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    queue.append(neighbor)
                    if neighbor[2] > maxMinute:
                        maxMinute = neighbor[2]
                    grid[neighbor[0]][neighbor[1]] = 2
        return maxMinute
                





        