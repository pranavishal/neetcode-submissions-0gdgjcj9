from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificNodesQueue = deque([])
        pacificNodesVisited = set()
        atlanticNodesQueue = deque([])
        atlanticNodesVisited = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    if (i, j) not in pacificNodesVisited:
                        pacificNodesQueue.append((i, j))
                        pacificNodesVisited.add((i, j))
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    if (i, j) not in atlanticNodesVisited:
                        atlanticNodesQueue.append((i, j))
                        atlanticNodesVisited.add((i, j))
        
        pacificReachableGrid = self.bfs(heights, pacificNodesQueue, pacificNodesVisited)
        atlanticReachableGrid = self.bfs(heights, atlanticNodesQueue, atlanticNodesVisited)

        reachBothList = []
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacificReachableGrid[i][j] == 1 and atlanticReachableGrid[i][j] == 1:
                    reachBothList.append([i, j])
        
        return reachBothList
    
    def bfs(self, grid, queue, visited):
        reachableGrid = [[0] * len(grid[0]) for _ in range(len(grid))]

        for i in range(len(reachableGrid)):
            for j in range(len(reachableGrid[0])):
                if (i, j) in visited:
                    reachableGrid[i][j] = 1

        while queue:
            currentNode = queue.popleft()
            neighbors = []
            # Top Neighbor
            if currentNode[0] > 0:
                neighbors.append((currentNode[0] - 1, currentNode[1]))
            
            # bottom neighbor
            if currentNode[0] < len(reachableGrid) - 1:
                neighbors.append((currentNode[0] + 1, currentNode[1]))
            
            # left neighbor
            if currentNode[1] > 0:
                neighbors.append((currentNode[0], currentNode[1] - 1))
            
            # right neighbor
            if currentNode[1] < len(reachableGrid[0]) - 1:
                neighbors.append((currentNode[0], currentNode[1] + 1))
            
            for neighbor in neighbors:
                if grid[neighbor[0]][neighbor[1]] >= grid[currentNode[0]][currentNode[1]] and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        for i in range(len(reachableGrid)):
            for j in range(len(reachableGrid[0])):
                if (i, j) in visited:
                    reachableGrid[i][j] = 1

        return reachableGrid




        