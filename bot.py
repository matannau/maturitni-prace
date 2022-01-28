import random


def create_grid(size):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(["_"])

        grid.append(row)

    return grid, size


def load_grid(grid, size):
    for i in range(size):
        for j in range(size):
            if j == size - 1:
                print(grid[i][j])
            else:
                print(grid[i][j], end="")

    print("\n")


def place_symbol(grid, symbol, coordinates):
    if grid[coordinates[0]][coordinates[1]] == ["_"]:
        grid[coordinates[0]][coordinates[1]] = [symbol]
    else:
        print("You can not chose this spot")


def check_spaces(i, j, size, grid, player_symbol):
    # Checks if grid[i][j] is in the grid and player's symbol isn't there
    if i >= 0 and j >= 0 and i < size and j < size and grid[i][j] != [player_symbol]:
        return True
    return False


def check_if_empty(i, j, size, grid):
    # Checks if grid[i][j] is in the grid and is playable
    if i >= 0 and j >= 0 and i < size and j < size and grid[i][j] == ["_"]:
        return True
    return False


def loop_increment_basic(i, j, size, grid, player_symbol):
    # Calls functions check_if_empty, check_spaces and check_potential_development
    # in all 8 directions and then creates a list of possible moves
    possible_move = []
    for y in range(-1, 2):
        for x in range(-1, 2):
            if not (x == y == 0):
                if check_if_empty(i + y, j + x, size, grid) and check_spaces(i + 4*y, j + 4*x, size, grid, player_symbol):
                    move = check_potential_development(
                        i, j, grid, player_symbol, y, x)
                    if move not in possible_move:
                        possible_move.append(move)

    return possible_move


def loop_increment_primary(i, j, size, grid, player_symbol):
    # Calls function check_spaces in all 8 directions and returns a number
    # of different moves that can be played
    value = 8
    for y in range(-1, 2):
        for x in range(-1, 2):
            if not check_spaces(i + y, j + x, size, grid, player_symbol):
                value -= 1

    return value


def filter_moves(moves):
    # Takes a list of coordinates and its values
    #
    # If one spot has multiple values, it calculates the average
    possible_moves = []
    len_moves = len(moves)
    for i in range(1, len_moves):
        if moves[i][0] == moves[i - 1][0] and moves[i][1] == moves[i - 1][1]:
            value = (moves[i][2] + moves[i - 1][2]) / 2
            possible_moves.append([moves[i][0], moves[i][1], value])
        else:
            if i == 1:
                possible_moves.append(moves[i - 1])
            if i < len_moves - 1:
                if moves[i][0] == moves[i + 1][0] and moves[i][1] == moves[i + 1][1]:
                    continue
                else:
                    possible_moves.append(moves[i])
            else:
                possible_moves.append(moves[i])

    return possible_moves


def find_best_move_value(moves):
    # Takes a list of possible moves, then calls filter_moves 7 times to ensure
    # that one spot has only one value
    #
    # After, it finds the smallest value of all spots and returns it wih possible moves
    for _ in range(7):
        moves = filter_moves(moves)
    value = float("inf")
    for move in moves:
        if move[2] < value:
            value = move[2]

    return value, moves


def check_potential_development(i, j, grid, player_symbol, y, x):
    # Checks 4 spots next to grid[i, j] in selected direction and then
    # counts the value od grid[i, j] based on it
    #
    # y -> i, x -> j
    value = 0
    for num in range(1, 5):
        space = grid[i + num * y][j + num * x]
        if space == ["_"]:
            value += 1
        elif space == [player_symbol]:
            value += 10
            break

    move = [i, j, value]
    return move


def find_primary_value(grid, size, player_symbol):
    # Counts the value of each spot in the grid and then it add it with
    # coordinates to possible moves
    possible_moves = []
    best_value = float("-inf")
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ["_"]:
                value = loop_increment_primary(i, j, size, grid, player_symbol)

                if value > best_value:
                    best_value = value
                possible_moves.append([i, j, value])

    return best_value, possible_moves


def find_move_value(grid, size, player_symbol):
    # Creates a list of all possible moves for the whole grid
    possible_moves = []
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ["_"]:
                possible_moves.extend(loop_increment_basic(
                    i, j, size, grid, player_symbol))

    return possible_moves


def get_move(best_value, possible_moves):
    # Selects all best moves based on the best value and then
    # choses one randomly
    best_moves = []
    x = len(possible_moves)
    for i in range(x - 1):
        if possible_moves[i][2] == best_value:
            best_moves.append(possible_moves[i])

    return random.choice(best_moves)


'''
Tests :)
'''

gamegrid, size = create_grid(10)
place_symbol(gamegrid, "X", [5, 4, 4])
place_symbol(gamegrid, "X", [5, 3, 4])
place_symbol(gamegrid, "X", [8, 5, 4])
# x, y, grid = find_primary_value(gamegrid, size)
# load_grid(grid, size)
size = 10
i, j = 6, 7
list = find_move_value(gamegrid, size, "X")
print(find_best_move_value(list))
