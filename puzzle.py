import numpy as np
import random
import time

# create an empty 9x9 sudoku board for puzzle
def sudoku_board():
    board = np.zeros(81, dtype = int)
    board = board.reshape(9,9)
    return board

# counter to track the number of solutions in puzzle/solve functions
count = 0 
# another 9x9 sudoku board for solved puzzle
solved  = np.ndarray(81, dtype=int)
solved = solved.reshape(9,9)


# generate a random solved python puzzle
def generate(board):
    randlist = [i for i in range(1,10)]
    random.shuffle(randlist)
    for row in range(9):
        for col in range(9):
            if isempty(row,col,board) == True:
                for num in randlist:
                    if num not in board[row,:] and num not in board[:,col] and num not in square(row, col,board):
                        board[row][col] = num
                        generate(board)
                        if 0 in board:	
                            board[row][col] = 0
                return board
    

	
# find out which 3x3 square we on
def square(row,col,board):
	if row < 3:
		if col < 3:
			return board[:3,:3]
		elif col > 2 and col < 6:
			return  board[:3,3:6]
		else:
			return board[:3,6:]

	elif row > 2 and row < 6:
		if col < 3:
			return  board[3:6,:3]
		elif col > 2 and col < 6:
			return  board[3:6,3:6]
		else:
			return  board[3:6,6:]

	else:
		if col < 3:
			return  board[6:,:3]
		elif col > 2 and col < 6:
			return  board[6:,3:6]
		else:
			return  board[6:,6:]

# find empty cell
def isempty(row,col,board):
	if board[row][col] == 0:
		return True
	else:
		return False

# create actual sudoku puzzle
def puzzle(unsolved):
	global count
	# remove 20 squares initially to make it faster
	while np.count_nonzero(unsolved == 0) < 20:
		unsolved[random.randint(0,8)][random.randint(0,8)] = 0
	# create the board with 48 empty squares and with only one solution
	while np.count_nonzero(unsolved==0) < 48: # <- adjust empty squares count for difficulty
		row = random.randint(0,8)
		col = random.randint(0,8)
		if unsolved[row][col] != 0:
			last = unsolved[row][col]
			unsolved[row][col] = 0
		count = 0
		solve(unsolved)
		# check if it has more than 1 solution
		if count > 1:
			unsolved[row][col] = last
	return unsolved

	
	

#find every solution of the given board
def solve(board):
	global count
	global solved
	for row in range(9):
		for col in range(9):
			if isempty(row,col,board) == True:
				for num in range(1,10):
					if num not in board[row,:] and num not in board[:,col] and num not in square(row, col,board):
						board[row][col] = num
						solve(board)
						board[row][col] = 0
				return board
	count +=1
	if np.count_nonzero(board == 0) == 0:
		np.copyto(solved,board)

# returns sudoku puzzle for 
def ready_puzzle():
	board = sudoku_board()
	random_board = generate(board)
	sudoku = puzzle(random_board)
	return sudoku
ready_puzzle()

