from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()

        def bfs(border_set):
            q = deque(border_set)

            while q:
                curr = q.popleft()
                row, col = curr
                neighbors = []

                if row > 0:
                    neighbors.append((row - 1, col))
                if row < len(heights) - 1:
                    neighbors.append((row + 1, col))
                
                if col > 0:
                    neighbors.append((row, col - 1))
                if col < len(heights[0]) - 1:
                    neighbors.append((row, col + 1))
                
                for neighbor in neighbors:
                    r, c = neighbor
                    if heights[r][c] >= heights[row][col] and (r, c) not in border_set:
                        border_set.add((r, c))
                        q.append((r, c))

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    pacific_set.add((i, j))
                
                if i == len(heights) - 1 or j == len(heights[i]) - 1:
                    atlantic_set.add((i, j))
        
        bfs(pacific_set)
        bfs(atlantic_set)
        return list(pacific_set & atlantic_set)

        



        