from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_map = defaultdict(set) # for the squares
        width_map = defaultdict(set)
        len_map = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                # length check
                if board[i][j] in len_map[i]:
                    return False
                len_map[i].add(board[i][j])

                #width check
                if board[i][j] in width_map[j]:
                    return False
                width_map[j].add(board[i][j])

                #square check
                row_num = i // 3
                col_num = j // 3
                if board[i][j] in set_map[(row_num, col_num)]:
                    print('SQUARE')
                    return False
                set_map[(row_num, col_num)].add(board[i][j])
        
        return True

        