def check_down(i, j, symbol, grid):
    total = 0
    for x in range(5):
        if grid[i + x][j] == [symbol]:
            total += 1
    if total == 5:
        return True


def check_up(i, j, symbol, grid):
    total = 0
    for x in range(5):
        if grid[i - x][j] == [symbol]:
            total += 1
    if total == 5:
        return True


def check_left(i, j, symbol, grid):
    total = 0
    for x in range(5):
        if grid[i][j - x] == [symbol]:
            total += 1
    if total == 5:
        return True


def check_right(i, j, symbol, grid):
    total = 0
    for x in range(5):
        if grid[i][j + x] == [symbol]:
            total += 1
    if total == 5:
        return True


def check_left_up(i, j, symbol, grid):
    total = 0
    for x in range(5):
        if grid[i - x][j - x] == [symbol]:
            total += 1
    if total == 5:
        return True


def check_left_down(i, j, symbol, grid):
    total = 0
    for x in range(5):
        if grid[i + x][j - x] == [symbol]:
            total += 1
    if total == 5:
        return True


def check_right_up(i, j, symbol, grid):
    total = 0
    for x in range(5):
        if grid[i - x][j + x] == [symbol]:
            total += 1
    if total == 5:
        return True


def check_right_down(i, j, symbol, grid):
    total = 0
    for x in range(5):
        if grid[i + x][j + x] == [symbol]:
            total += 1
    if total == 5:
        return True


def check_lines(i, j, symbol, grid, size):
    if i < size - 4:
        if check_down(i, j, symbol, grid) == True:
            return True
    if i > size - 7:
        if check_up(i, j, symbol, grid) == True:
            return True
    if j < size - 4:
        if check_right(i, j, symbol, grid) == True:
            return True
    if j > size - 7:
        if check_left(i, j, symbol, grid) == True:
            return True


def check_diagonals(i, j, symbol, grid, size):
    if i > size - 7 and j > size - 7:
        if check_left_up(i, j, symbol, grid) == True:
            return True
    if i < size - 4 and j > size - 7:
        if check_left_down(i, j, symbol, grid) == True:
            return True
    if i > size - 7 and j < size - 4:
        if check_right_up(i, j, symbol, grid) == True:
            return True
    if i < size - 4 and j < size - 4:
        if check_right_down(i, j, symbol, grid) == True:
            return True