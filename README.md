# Sudoku_Solver
> Python project
## Python Project
📌 This application is a python implementation of a Sudoku Solver.

📌 The project also contains a graphical user interface (GUI) for the game of Sudoku. 

## *Algorithm*✨
- Find some empty space
- Attempt to place the digits 1-9 in that space
- Check if that digit is valid in the current spot based on the current board
    - If the digit is valid, recursively attempt to fill the board using steps 1-3.
    - If it is not valid, reset the square you just filled and go back to the previous step.
- Once the board is full by the definition of this algorithm we have found a solution.

## *Graphical User Interface (GUI)* 👨‍💻
- The GUI is built using the Pygame library, which is a set of Python modules designed for writing video games. The Sudoku game board is represented as a 9x9 grid of cells, and the player can interact with the grid by selecting cells and entering values. The GUI supports two modes of play: placing values and sketching values.
- The GUI consists of two classes: Grid and Cube. The Grid class represents the game board and contains a two-dimensional list of Cube objects, where each Cube object represents a cell on the game board. The Cube class contains information about the cell's value, whether it is selected, and whether a temporary value has been sketched.


Select a cube and insert a temporary value             |  If the value is valid, it turns black
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/123704487/223128289-161df218-2a8b-4d5f-a08c-b50b0c2cd412.png)  |  ![image](https://user-images.githubusercontent.com/123704487/223128483-9b63f7b7-af98-4d4b-98d1-f2d710895b29.png)




