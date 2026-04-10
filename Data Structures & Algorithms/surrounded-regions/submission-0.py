from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        not_surrounded = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    if board[i][j] == 'O':
                        not_surrounded.add((i, j))
        

        def bfs(border):
            q = deque(not_surrounded)
            while q:
                row, col = q.popleft()
                neighbors = []
                if row < len(board) - 1:
                    neighbors.append((row + 1, col))
                if row > 0:
                    neighbors.append((row - 1, col))
                if col < len(board[0]) - 1:
                    neighbors.append((row, col + 1))
                if col > 0:
                    neighbors.append((row, col - 1))
                
                for neighbor in neighbors:
                    r, c = neighbor
                    if board[r][c] == 'O' and (r, c) not in not_surrounded:
                        q.append((r, c))
                        not_surrounded.add((r, c))

        

        bfs(not_surrounded)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in not_surrounded:
                    board[i][j] = 'X'
        