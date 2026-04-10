class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(pos, index):
            if index >= len(word):
                return True
            
            row, col = pos
            letter = board[row][col]
            board[row][col] = "#"
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
                if board[r][c] == word[index]:
                    if dfs((r, c), index + 1):
                        return True
            
            board[row][col] = letter

            return False
        
        starting_pos = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    starting_pos.append((i, j))
        
        for pos in starting_pos:
            if dfs(pos, 1):
                return True
        
        return False

                    
            
            


        