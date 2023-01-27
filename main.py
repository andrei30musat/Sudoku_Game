board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, row, col ):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, row, col):
    #num e numarul pe care vrem sa l introducem
    #(row,col) reprezinta coordonatele numarului pe care vrem sa l introducem id est num(row, col)

    # Verificam daca num este deja pe linia unde vrem sa l introducem
    for j in range(len(board[0])):
        if board[row][j] == num and col != j:
            return False

    # Verificam daca num este deja pe coloana unde vrem sa l introducem
    for i in range(len(board[0])):
        if board[i][col] == num and row != i:
            return False

    # Verificam daca num este deja pe patratul unde vrem sa l introducem
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != (row,col):
                return False

    return True


def print_board(board):
    for i in range(len(board[0])):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j] , end=" ")


def find_empty(board):
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # linia si coloana


print_board(board)
solve(board)
print("=====================")
print_board(board)
