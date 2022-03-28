from . bot import check_if_computer


def find_4_symbols(i, j, grid, symbol, y, x):
    # Tries to find four same symbols directly next to each other
    symbols = [[i, j]]
    for num in range(1, 5):
        if grid[i + num*y][j + num*x] != [symbol]:
            return False, []
        symbols.append([i + num*y, j + num*x])
    return True, symbols


def loop_increment(i, j, size, grid, symbol):
    # Tries to find a win in every possible direction
    for y in range(-1, 2):
        for x in range(-1, 2):
            if not (x == y == 0):
                if check_if_computer(i + 4*y, j + 4*x, size, grid, symbol):
                    win, symbols = find_4_symbols(i, j, grid, symbol, y, x)
                    if win:
                        return True, symbols
    return False, []


def loop_spots(size, grid, symbol):
    # Tries to find a win for every placed symbol
    for i in range(size):
        for j in range(size):
            if grid[i][j] == [symbol]:
                win, symbols = loop_increment(i, j, size, grid, symbol)
                if win:
                    return True, symbols
    return False, []


def check_win(grid, size):
    # Checks if there is a win for both symbolss
    win, symbols = loop_spots(size, grid, "X")
    if win:
        return "X", symbols
    win, symbols = loop_spots(size, grid, "O")
    if win:
        return "O", symbols

    return False, []
