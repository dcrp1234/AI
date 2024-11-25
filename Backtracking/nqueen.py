import numpy as np

def getMatrixDimension():
    n = input("Input the dimesnsion of your matrix must be greater than 3:")
    return n

def setUpMatrix(n):
    board = [[0]*n for _ in range(n)]  # Properly initialize the board
    return board

def updateBoard(board, position, j, n, value):
    print(np.array(board), "\ni = ", position, "j = ", j)
    # position is row value
    #for vertical
    print(np.array(board))
    i = 0
    for i in range(n):
        board[i][j] = value
    #for horizontal
    k = 0
    for k in range(n):
        board[position][k]= value
    #for diagonal
    i = position
    right = j+1
    left = j-1
    while i>0:
        i = i -1
        if(right <= n-1):
            board[i][right] = value
            right = right+1
        if(left >= 0):
            board[i][left] = value
            left = left-1
    i = position
    right = j+1
    left = j-1
    while i<n-1:
        i = i +1
        if(right <= n-1):
            board[i][right] = value
            right = right+1
        if(left >= 0):
            board[i][left] = value
            left = left-1
    print(np.array(board), "Update done!\n")

    return board

def playGame(board, position,solution, n):
    if(position == n):
        print("Solution found")
        return True

    print("For level:", position)
    print("State of board\n", np.array(board))
    for j in range(n):
        if board[position][j] == 0:
            updateBoard(board, position, j, n, 1)
            solution = str(solution)+ str(j)
            print("Adding to solution", solution)
            if playGame(board, position+1,solution, n):
              return True
            print()
            print("Undoing last move:")
            updateBoard(board, position, j, n, 0)
            solution = solution[0: len(solution)-1]
            print(solution)
            print("Restoring to last state")
            i = 0
            sol = solution
            print("Sol:", sol)
            while i <= position-1:
              updateBoard(board, i, int(sol[0]), n, 1)
              if(sol != ''):
                sol = sol[1:len(sol)]
              i +=1

    print("Not possible to put queen in this row.")
    return False

def setUpGame():
    global n
    n = int(getMatrixDimension())
    while n <= 3:
        print("Try again")
        n = int(getMatrixDimension())
    board = setUpMatrix(n)
    level = 0
    playGame(board, level,"", n)


setUpGame()
#print(board)

'''
Need to find way to undo mov ein such a way that it depends on the move taken not on th elast state of game
'''