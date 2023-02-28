# Sudoku_Solver

This application is a python implementation of a Sudoku solver. The code is divided into four functions - **print_board(), find_empty(), valid(), and solve()** - that together solve a given Sudoku puzzle. Here is a brief explanation of each function:

**print_board(board)**: This function takes in a 9x9 Sudoku board as input and prints it in a readable format. It uses a nested loop to iterate over each element of the board and prints it along with vertical and horizontal lines to indicate the different blocks of the board.

**find_empty(board)**: This function takes in a 9x9 Sudoku board as input and searches for an empty cell (represented by 0) in the board. If it finds an empty cell, it returns its coordinates (row and column), otherwise it returns None.

**valid(board, num, row, col)**: This function takes in a 9x9 Sudoku board, a number to be inserted, and its coordinates (row and column) as input. It checks if the given number is valid to be placed in the specified cell based on the rules of Sudoku. It checks if the number is already present in the same row, column or block. It returns True if the number is valid, False otherwise.

**solve(board)**: This function takes in a 9x9 Sudoku board as input and solves it recursively using backtracking. It first calls the find_empty() function to find an empty cell. If it finds one, it tries to insert numbers from 1 to 9 in the cell and checks if the insertion is valid using the valid() function. If the insertion is valid, it proceeds to solve the next empty cell recursively using the same approach. If it reaches a dead end, it backtracks and tries a different number in the previous cell until it finds a solution or exhausts all possibilities. If it finds a solution, it returns True, otherwise False.
