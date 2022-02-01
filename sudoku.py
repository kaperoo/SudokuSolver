import copy

board = [[1,0,0,0,0,0,0,0,3],
         [0,4,0,0,8,9,0,2,0],
         [0,0,2,0,0,3,9,5,0],
         [0,0,0,4,1,0,5,0,0],
         [0,0,0,0,2,0,0,0,0],
         [0,0,5,0,3,7,0,0,0],
         [0,3,4,8,0,0,6,0,0],
         [0,2,0,6,7,0,0,3,0],
         [6,0,0,0,0,0,0,0,9]]

counter = 0

# for i in range(9):
    # print(board[i])
def solveSudoku(board,counter):
    b = copy.deepcopy(board)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for k in range(1,10):
                    if check(b,i,j,k):
                        b[i][j] = k
                        counter += 1
                        if solveSudoku(b,counter):
                            return True
                        else:
                            b[i][j] = 0
                            counter -= 1
                return False
            elif i==8 and j==8 and board[i][j] != 0:
                for i in range(9):
                    print(board[i])
                return True
                

def check(board,row,column,num):
    if num in board[row]:
        return False
    for i in range(9):
        if board[i][column] == num:
            return False

    x = (row - (row%3))
    y = (column - (column%3))

    for i in range(3):
        for j in range(3):
            if (i,j)==(row,column):
                continue
            if board[x+j][y+i] == num:
                return False
    return True
    
print("Processing...")
solveSudoku(board,counter)
