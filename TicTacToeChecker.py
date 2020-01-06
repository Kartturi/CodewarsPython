# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? 
# Our goal is to create a function that will check that for us!

# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2
#  if it is an "O", like so:

# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:

# -1 if the board is not yet finished (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

def isSolved(board):
    for i,lis in enumerate(board):
        if len(set(lis))==1 and lis[0] != 0:
            return lis[0]
        else:
            tempList = []
            for lis in board:
                tempList.append(lis[i])
            if(len(set(tempList))==1) and tempList[0] != 0:
                return lis[0]
    
    if len(set([board[0][0],board[1][1],board[2][2]])) == 1 and board[0][0] != 0:
        return board[0][0]
    elif len(set([board[0][2],board[1][1],board[2][0]])) == 1:
        return board[0][2]
    else:
        for i,lis in enumerate(board):
            if(0 in lis):
                return -1
        return 0

board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]

board1 = [[1, 2, 2],
         [1, 2, 1],
         [2, 2, 2]]

board2 = [[1, 2, 1],
         [1, 1, 1],
         [1, 2, 2]]
board3 = [[0,0,2], [0,0,0], [1,0,1]]
print(isSolved(board3))

    
