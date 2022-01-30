from wincheck import check_lines, check_diagonals
from bot import find_best_move_value, get_move, find_primary_value
from grid import create_grid

def load_grid(grid, size):
    print("    0    1    2    3    4    5    6    7    8    9")
    for i in range(size):
        for j in range(size):
            if j == 0:
                print(i, grid[i][j], end="")
            elif j == size - 1:
                print(grid[i][j])
            else:
                print(grid[i][j], end="")

    print("\n")

def check_win(grid, size):
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ["X"]:
                if check_lines(i, j, "X", grid, size) == True:
                    return "X has won"
                if check_diagonals(i, j, "X", grid, size) == True:
                    return "X has won"
            if grid[i][j] == ["O"]:
                if check_lines(i, j, "O", grid, size) == True:
                    return "O has won"
                if check_diagonals(i, j, "O", grid, size) == True:
                    return "O has won"
    return "No one has won"

def place_symbol(grid, symbol, coordinates):
    if grid[coordinates[0]][coordinates[1]] == ["_"]:
        grid[coordinates[0]][coordinates[1]] = [symbol]
    else:
        print("You can not chose this spot")

gamegrid, size = create_grid(10)
l = int(input("Zadej y souradnici: "))
m = int(input("Zadej x souradnici: "))
place_symbol(gamegrid, "X", [l, m])
x, y = find_primary_value(gamegrid, size, "X")
arr = get_move(x, y)
place_symbol(gamegrid, "O", arr)
load_grid(gamegrid, size)

while True:
    l = int(input("Zadej y souradnici: "))
    m = int(input("Zadej x souradnici: "))
    place_symbol(gamegrid, "X", [l, m])
    x, y = find_best_move_value(gamegrid, size, "X", "O")
    arr = get_move(x, y)
    place_symbol(gamegrid, "O", arr)
    load_grid(gamegrid, size)

    if check_win(gamegrid, size) != "No one has won":
        break



load_grid(gamegrid, size)
print(check_win(gamegrid, size))
