# sudoku table :

x = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
     [6, 0, 0, 0, 7, 5, 0, 0, 9],
     [0, 0, 0, 6, 0, 1, 0, 7, 8],
     [0, 0, 7, 0, 4, 0, 2, 6, 0],
     [0, 0, 1, 0, 5, 0, 9, 3, 0],
     [9, 0, 4, 0, 6, 0, 0, 0, 5],
     [0, 7, 0, 3, 0, 0, 0, 1, 2],
     [1, 2, 0, 0, 0, 7, 4, 0, 0],
     [0, 4, 9, 2, 0, 6, 0, 0, 7]]


def is_valid_move(grid, row, col, number):
    for i in range(9):
        if grid[row][i] == number or grid[i][col] == number:
            return False

    corner_row = (row//3)*3
    corner_column = (col//3)*3

    for i in range(3):
        for j in range(3):
            if grid[corner_row+i][corner_column+j] == number:
                return False

    return True


def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col+1)

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col+1):
                return True
        grid[row][col] = 0

    return False


if solve(x, 0, 0):
    for i in range(9):
        for j in range(9):
            print(x[i][j], end=" ")
        print()

else:
    print("bad table")
