import numpy as np

##load 20 Sudoku puzzles and their solutions into two 20x9x9 numpy arrays.

# Load sudokus
sudokus = np.load("data/sudokus.npy")
print("Shape of one sudoku array:", sudokus[0].shape, ". Type of array values:", sudokus.dtype)

# Load solutions
solutions = np.load("data/sudoku_solutions.npy")
print("Shape of one sudoku solution array:", solutions[0].shape, ". Type of array values:", solutions.dtype, "\n")

# Print the first sudoku...
print("Sudoku #1:")
print(sudokus[14], "\n")

# ...and its solution
print("Solution of Sudoku #1:")
print(solutions[14])

##Sudoku solver

import time

start_time = time.time()

def sudoku_solver(sudoku):
    emptySqr = findEmptySquare(sudoku)
    # If there is no empty square, the sudoku is solved
    if not emptySqr:
        return True
    # Otherwise, emptySqr will return a value(row,column)
    else:
        row, column = emptySqr # The empty position
        trialNum = 1
        num = 1
        solved_sudoku = False
        while (solved_sudoku != True) and (trialNum < 10):
            if isValid(sudoku, num, (row, column)):
                # If the number is valid, place it on the board 
                sudoku[row][column] = num
                if sudoku_solver(sudoku) == True:
                    solved_sudoku = True
                    return True
                else:
                    # If i cannot finish the solution, reset that value and try a different one
                    sudoku[row][column] = 0
            trialNum += 1
            num += 1
        return solved_sudoku

# Function to change values to -1 if the sudoku has no solution
def isSolvable(sudoku):
    if sudoku_solver(sudoku) == False:
        for i in range(len(sudoku)):
            for j in range(len(sudoku[0])):
                sudoku[i][j] = -1
    else:
        return False
  
    
# Find and return the position of an empty square
def findEmptySquare(sudoku):
    # Loop through the sudoku-board to find and return an empty position
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                # Return a tuple (row-position[0], column-position[1])
                return (i,j)
    # Return None if there is non empty square
    return None

# Check if the number is valid (row, column, 3x3 box) 
def isValid(sudoku, num, position):
    
    # Check Column (Loop through every row)
    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == num and position[0] != i:
            return False 
        
    # Check Row (Loop through every column) 
    for i in range(len(sudoku[0])):
        if sudoku[position[0]][i] == num and position[1] != i:
            return False
    
    # Determine which box I'm in
    boxR = position[0] // 3 
    boxC = position[1] // 3 
    
    # Loop through all nine elements in the box 
    # Multiply by 3 to get to the last three indexes(6,7,8)
    # Loop for columns 
    for i in range(boxR * 3, boxR * 3 + 3):
        for j in range(boxC * 3, boxC * 3 + 3):
            if sudoku[i][j] == num and (i,j) != position:
                return False
    # If the number is valid (pass all checks), then I return true
    return True

## Test the code

for i in range(len(sudokus)):
    sudoku = sudokus[i].copy()
    print("This is sudoku number", i)
    print("------------------------------")
    print(sudoku)
    print("\n")
    print("This is your solution for sudoku number", i)
    print("-----------------------------------------")
    your_solution = sudoku_solver(sudokus[i])
    isSolvable(sudokus[i])
    if isSolvable != False:
        print(sudokus[i])
    else:
        print(sudokus[i])
    print("\n")
    print("Is your solution correct?")
    print(np.array_equal(sudokus[i], solutions[i]))
    print("\n")

print("--- The computation time is: %s sec ---" % (time.time() - start_time))
    

