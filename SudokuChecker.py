class Solution:
    def isValidSudoku(self, board) -> bool:
        #Check rows
        for row in board:
            r = [i for i in row if i != "."]
            while len(r) >1:
                if r.pop(0) in r:
                    return False
        #check for collumns
        
        for x in range(9):
            r = []
            for y in range(9):
                if board[y][x] != ".":
                    if board[y][x] in r:
                        return False
                    r.append(board[y][x])
        #check squares
        for i in range(3):
            for j in range(3):
                r = []
                for x in range(i*3,3+i*3):
                    for y in range(j*3,3+j*3):
                        if board[y][x] != ".":
                            if board[y][x] in r:
                                return False
                            r.append(board[y][x])                        
        return True

board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution.isValidSudoku("",board))