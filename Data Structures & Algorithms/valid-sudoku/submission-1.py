class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in [0, 3, 6]:
            for k in [0, 3, 6]:
                squareSet = set()
                print('-----------------------------')
                for j in range(3):
                    for l in range(3):
                        print(board[i + j][k + l])
                        if board[i + j][k + l] in squareSet and board[i + j][k + l] != ".":
                            print("SQUARE SET FAIL")
                            return False
                        squareSet.add(board[i + j][k + l])
        
        
        for i in range(len(board)):
            horizontalSet = set()
            for j in range(len(board[0])):
                if board[i][j] in horizontalSet and board[i][j] != ".":
                    print("HORIZONTAL SET FAIL")
                    return False
                horizontalSet.add(board[i][j])
        
        for i in range(len(board[0])):
            verticalSet = set()
            for j in range(len(board)):
                if board[j][i] in verticalSet and board[j][i] != ".":
                    print("VERTICAL SET FAIL")
                    return False
                verticalSet.add(board[j][i])
        
        return True



                
                

                
            
