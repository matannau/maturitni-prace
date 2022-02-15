from . bot import check_if_computer

def find_4_symbols(i, j, grid, symbol, y, x):
    for num in range(1, 5):
        if grid[i + num*y][j + num*x] != [symbol]:
            return False

    return True


def loop_increment(i, j, size, grid, symbol):
    for y in range(-1, 2):
        for x in range(-1, 2):
            if not (x == y == 0):
                if check_if_computer(i + 4*y, j + 4*x, size, grid, symbol):
                    if find_4_symbols(i, j, grid, symbol, y, x):
                        return True


def loop_spots(size, grid, symbol):
    for i in range(size):
        for j in range(size):
            if grid[i][j] == [symbol]:
                if loop_increment(i, j, size, grid, symbol):
                    return True
    return False


def check_win(grid, size):
    if loop_spots(size, grid, "X"):
        return 1
    if loop_spots(size, grid, "O"):
        return 2

    return False
