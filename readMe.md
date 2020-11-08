# Sudoku solver implemented in Python.

The objective is to fill each cell with a digit ranging from 1 to 9 so that each row, column and 3×3 section contain every digit from 1 and 9.  
For example, each row of the grid has nine cells; to solve the puzzle correctly, every digit from 1 to 9 must be present in each row. Some of the cells are already filled in with digits; these digits cannot be altered.

The function "sudoku_solver()" takes one Sudoku puzzle (a  9×9  numpy array) as input and returns the solved Sudoku as a  9×9  numpy array.

Note that the test set I was using when working in this project contained invalid Sudokus, that is, Sudokus with no solution. In such a case, my function returns a  9×9  numpy array whose values are all equal to -1. 