import random
import copy
from wincheck import check_win


def create_grid(size):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(["_"])

        grid.append(row)

    return grid, size


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


def check_if_computer(i, j, size, grid, computer_symbol):
    # Checks if grid[i][j] is in the grid and computer's symbol is there
    if i >= 0 and j >= 0 and i < size and j < size and grid[i][j] == [computer_symbol]:
        return True
    return False


def find_all_empty_spots(grid, size):
    # Creates a list of all spots with no symbols
    empty_spots = []
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ["_"]:
                empty_spots.append([i, j, 10])

    return empty_spots


def find_a_4(i, j, size, grid, computer_symbol, y, x):
    # Checks for fours and then returns winning move
    value = 0
    if check_if_empty(i + 4*y, j + 4*x, size, grid):
        for num in range(1, 4):
            if grid[i + y*num][j + num*x] == [computer_symbol]:
                value += 1
    if value == 3:
        return True, [i + 4*y, j + 4*x, 1]

    return False, []


def find_a_3(i, j, size, grid, player_symbol, computer_symbol, y, x):
    # Finds a 3 and then decides which side is more suitable for playing
    value = 0
    if check_if_empty(i + 3*y, j + 3*x, size, grid) and check_if_empty(i - y, j - x, size, grid):
        if grid[i + 3*y][j + 3*x] == ["_"] and grid[i - y][j - x] == ["_"]:
            for num in range(1, 3):
                if grid[i + y*num][j + num*x] == [computer_symbol]:
                    value += 1

    if value == 2:
        if check_spaces(i - 2*y, j - 2*x, size, grid, player_symbol) and check_spaces(i + 3*y, j + 3*x, size, grid, player_symbol):
            return True, [[i - y, j - x, 1.75], [i + 3*y, j + 3*x, 1.75]]
        elif not check_spaces(i - 2*y, j - 2*x, size, grid, player_symbol) and check_spaces(i + 3*y, j + 3*x, size, grid, player_symbol):
            return True, [[i + 3*y, j + 3*x, 1.75]]
        elif check_spaces(i - 2*y, j - 2*x, size, grid, player_symbol) and not check_spaces(i + 3*y, j + 3*x, size, grid, player_symbol):
            return True, [[i - y, j - x, 1.75]]

    return False, []


def loop_increment_basic(i, j, size, grid, player_symbol, computer_symbol):
    # For the given spot it tries to find fours, then threes and then if the
    # direction is convenient for playing in every possible direction
    possible_move = []
    for y in range(-1, 2):
        for x in range(-1, 2):
            if not (x == y == 0):
                boolean4, spot4 = find_a_4(
                    i, j, size, grid, computer_symbol, y, x)
                boolean3, spot3 = find_a_3(
                    i, j, size, grid, player_symbol, computer_symbol, y, x)
                if boolean4:
                    possible_move.append(spot4)

                elif boolean3:
                    for item in spot3:
                        possible_move.append(item)

                elif check_if_empty(i + y, j + x, size, grid):
                    if check_spaces(i + 2*y, j + 2*x, size, grid, player_symbol) and check_spaces(i - 2*y, j - 2*x, size, grid, player_symbol):
                        move = check_potential_development(
                            i, j, size, grid, player_symbol, computer_symbol, y, x)
                        if move not in possible_move:
                            possible_move.append(move)

    return possible_move


def loop_increment_primary(i, j, size, grid, player_symbol):
    # Calls function check_spaces in all 8 directions and returns a number
    # of different moves that can be played
    value = 8
    for y in range(-1, 2):
        for x in range(-1, 2):
            if not check_spaces(i + 2*y, j + 2*x, size, grid, player_symbol):
                value -= 1

    return value


def find_forks(moves):
    # Tries to find forks by comparing multiple values of one spot
    moves = sorted(moves)
    possible_moves = [moves[0]]
    len_moves = len(moves)
    for i in range(1, len_moves):
        if moves[i][0] == moves[i - 1][0] and moves[i][1] == moves[i - 1][1]:
            if moves[i][2] == 3:
                if moves[i - 1][2] == 3:
                    possible_moves.append([moves[i][0], moves[i][1], 1.75])
                elif moves[i - 1][2] == 2:
                    possible_moves.append([moves[i][0], moves[i][1], 1.5])
            elif moves[i][2] == 2:
                if moves[i - 1][2] == 3:
                    possible_moves.append([moves[i][0], moves[i][1], 1.5])
                elif moves[i - 1][2] == 2:
                    possible_moves.append([moves[i][0], moves[i][1], 1.5])
            else:
                if moves[i] not in possible_moves:
                    possible_moves.append(moves[i])
        else:
            if moves[i] not in possible_moves:
                possible_moves.append(moves[i])

    return possible_moves


def find_best_move_value(grid, size, player_symbol, computer_symbol):
    # Creates a list of coordinates with its values and then loops through
    # them to find the best one
    moves = find_move_value(grid, size, player_symbol, computer_symbol)

    moves = find_forks(moves)

    value = float("inf")
    for move in moves:
        if move[2] < value:
            value = move[2]

    return value, moves


def get_direction(i, j):
    # 1 - right, left
    # 2 - up, down
    # 3 - rightup, lefudown
    # 4 - leftup, right down
    if i == 0:
        return 1
    if j == 0:
        return 2
    if i == 1:
        if j == 1:
            return 4
        return 3
    if i == -1:
        if j == 1:
            return 3
        return 4


def check_potential_development(i, j, size, grid, player_symbol, computer_symbol, y, x):
    # Checks 4 spots next to grid[i, j] in selected direction and then
    # counts the value od grid[i, j] based on it
    #
    # y -> i, x -> j
    value = 0
    for num in range(-2, 3):
        space = grid[i + num * y][j + num * x]
        if space == ["_"]:
            value += 1
        elif space == [player_symbol]:
            value += 10

    if value > 1:
        if not check_spaces(i + 3*y, j + 3*x, size, grid, player_symbol):
            value += 1
        if not check_spaces(i - 3*y, j - 3*x, size, grid, player_symbol):
            value += 1

    if check_if_computer(i + 3*y, j + 3*x, size, grid, computer_symbol):
        value -= 1
    if check_if_computer(i - 3*y, j - 3*x, size, grid, computer_symbol):
        value -= 1

    move = [i + y, j + x, value, get_direction(y, x)]
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


def find_move_value(grid, size, player_symbol, computer_symbol):
    # Creates a list of all possible moves for the whole grid
    possible_moves = []
    for i in range(size):
        for j in range(size):
            if grid[i][j] == [computer_symbol]:
                moves = loop_increment_basic(
                    i, j, size, grid, player_symbol, computer_symbol)
                for item in moves:
                    if item not in possible_moves:
                        possible_moves.append(item)

    if possible_moves == []:
        moves = find_all_empty_spots(grid, size)
        for item in moves:
            possible_moves.append(item)

    return possible_moves


def need_to_block(grid, size, computer_symbol, player_symbol):
    # Calls find_best_move_value on the other symbol and if
    # the value of it is less than 3, returns True
    value, moves = find_best_move_value(
        grid, size, computer_symbol, player_symbol)

    if value < 3:
        return True, value, moves
    else:
        return False, [], []


def filter_moves(best_value, possible_moves):
    # Creates a list of the best moves (moves with the least value)
    best_moves = []
    x = len(possible_moves)
    for i in range(x):
        if possible_moves[i][2] == best_value:
            best_moves.append(possible_moves[i])

    return best_moves


def make_a_move(grid, size, player_symbol, computer_symbol):
    value, moves = find_best_move_value(
        grid, size, player_symbol, computer_symbol)
    block, value2, moves2 = need_to_block(
        grid, size, computer_symbol, player_symbol)
    if block:
        if value2 <= value:
            arr = get_move(value2, moves2)
        else:
            arr = get_move(value, moves)
    else:
        arr = get_move(value, moves)
    place_symbol(grid, computer_symbol, arr)

    load_grid(grid, size)

    return arr


def prediction(grid, size, player_symbol, computer_symbol):
    value, moves = find_best_move_value(
        grid, size, player_symbol, computer_symbol)
    print(moves)
    moves = filter_moves(value, moves)
    win_in = []

    for item in moves:
        grid2 = copy.deepcopy(grid)
        place_symbol(grid2, "X", item)

        x = 0  # Number of moves in which player wins
        y = 1  # NUmber of moves in which computer wins
        first_player_move = []
        won = False
        while not won:
            if x > 40 or y > 20:
                x, y = float("inf"), float("inf")
                break
            else:
                coordinates = make_a_move(
                    grid2, size, computer_symbol, player_symbol)
                if x == 0:
                    first_player_move = coordinates
                if check_win(grid2, size):
                    won = True
                    print("Hrac vyhral")
                    break
                x += 1

                make_a_move(grid2, size, player_symbol, computer_symbol)
                if check_win(grid2, size):
                    print("Pocitac vyhral")
                    won = True
                    break
                y += 1

        win_in.append([item, first_player_move, x, y])

    return win_in


def get_move(best_value, possible_moves):
    # Chooses randomly one of the best moves
    best_moves = filter_moves(best_value, possible_moves)

    return random.choice(best_moves)


'''
Tests :)
'''
if __name__ == "__main__":
    gamegrid, size = [
        [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
        [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
        [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
        [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
        [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
        [["_"], ["X"], ["O"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"]],
        [["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["O"], ["_"], ["_"], ["_"]],
        [["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"]],
        [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
        [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
    ], 10
    print(prediction(gamegrid, size, "O", "X"))
