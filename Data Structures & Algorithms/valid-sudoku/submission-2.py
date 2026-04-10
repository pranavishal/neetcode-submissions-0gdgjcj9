from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "." and board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])

                if board[i][j] != "." and board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])

                sq_r, sq_c = i // 3, j // 3
                if board[i][j] != "." and board[i][j] in squares[(sq_r, sq_c)]:
                    return False
                squares[(sq_r, sq_c)].add(board[i][j])
        
        return True
                    
        