import tkinter as tk
from tkinter import messagebox


# Function to solve the sudoku
def solve_sudoku(grid):
    # Iterate through each row and column of the grid
    for row in range(9):
        for col in range(9):
            # If the current cell is empty
            if grid[row][col] == 0:
                # Try each number from 1 to 9 in the current cell
                for num in range(1, 10):
                    # If the number is valid for the current cell
                    if is_valid(grid, row, col, num):
                        # Place the number in the cell
                        grid[row][col] = num
                        # Solve the rest of the grid
                        if solve_sudoku(grid):
                            return True
                        # Backtrack if no solution is found
                        grid[row][col] = 0
                return False
    return True


# Function to check if a number is valid in the current cell
def is_valid(grid, row, col, num):
    # Check if the number is present in the same row
    for i in range(9):
        if grid[row][i] == num:
            return False
    # Check if the number is present in the same column
    for i in range(9):
        if grid[i][col] == num:
            return False
    # Check if the number is present in the same 3x3 block
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[row_start + i][col_start + j] == num:
                return False
    return True


# GUI class for the sudoku solver
class SudokuSolver:
    def __init__(self, master):
        # Initialize the master window
        self.master = master
        master.title("Sudoku Solver by Alper Celik")

        # Initialize the grid with zeros
        self.grid = [[0 for x in range(9)] for y in range(9)]

        # Create a dictionary of entry widgets for the grid cells
        self.entries = {}
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(width=2, font=("Arial", 20))
                entry.grid(row=row, column=col)
                self.entries[(row, col)] = entry

        # Create a button to solve the sudoku
        solve_button = tk.Button(text="Solve", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=9, sticky="WE")

    # Function to solve the sudoku and update the grid
    def solve(self):
        # Get the values from the entry widgets and update the grid
        for row in range(9):
            for col in range(9):
                try:
                    self.grid[row][col] = int(self.entries[(row, col)].get())
                except:
                    self.grid[row][col] = 0
        # Solve the sudoku
        if solve_sudoku(self.grid):
            for row in range(9):
                for col in range(9):
                    self.entries[(row, col)].delete(0, tk.END)
                    self.entries[(row, col)].insert(0, str(self.grid[row][col]))
        else:
            messagebox.showerror("Error", "No solution found.")


root = tk.Tk()

my_gui = SudokuSolver(root)


root.mainloop()
