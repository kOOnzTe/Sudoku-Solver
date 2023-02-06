# Basic Sudoku Solver

#### This is a python code for a Sudoku solver using a GUI created with the tkinter library. It has two main parts: the solve_sudoku function and the SudokuSolver class.

#### The solve_sudoku function is a ***Recursive Implementation of the Backtracking Algorithm*** to solve a 9x9 sudoku puzzle. It iterates over the grid and when it finds a cell with a value of 0, it tries to fill it with a number from 1 to 9. If the number is valid, it moves on to the next cell, otherwise it backtracks.

#### The SudokuSolver class is responsible for creating the GUI. It initializes a 9x9 grid, creates a dictionary of tkinter. Entry widgets for each cell, and creates a button to solve the sudoku. When the "Solve" button is clicked, the function retrieves the values from the cells and passes them to the solve_sudoku function. If a solution is found, it updates the values in the GUI, otherwise it shows an error message.

#### Also, there is an is_valid function to check if a number is valid in the current cell.

#### Finally, the root Tk object is created and the SudokuSolver is instantiated and associated with it, and the mainloop method is called to start the GUI event loop.
